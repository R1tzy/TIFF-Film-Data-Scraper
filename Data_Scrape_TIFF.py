from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

def get_page_content_release(url):
    url_release = url + '/calendar?newreleases'
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url_release)
        page.wait_for_load_state("load")
        content = page.content()
        browser.close()
    return content

def convert_to_bs4(page_content, link):
    bs = BeautifulSoup(page_content, 'html.parser')
    result = bs.find('div', {'id': 'resultsList'})
    if result is not None:
        #se der erro aqui, é por causa do carregamento da página. É só tentar novamente ou adicionar um atraso
        li_release = result.find_all('li') 
        for li in li_release:
            try:
                link.append(li.find('h2').find('a').attrs['href'])
            except Exception as e:
                return e
    else:
        print("The result element was not found.")


def find_name_event(links, names):
    for link in links:
        name_find = re.findall('/events/([\w-]+)', link)
        if name_find:
            names.append(name_find[0])

def get_event_details(names, data, links):
    for name, link in zip(names, links):
        new_url = f"https://www.tiff.net/yearroundfilmtemplatejson/{name}"
        response = requests.get(new_url)
        json_res = response.json()
        title = json_res['title']
        sales_agent = ', '.join(json_res['filmCredits']["internationalSalesAgent"])
        sold_to = ', '.join(json_res['filmCredits']['canadianDistributors'])
        cancon = json_res['isCanadian']
        if cancon:
            cancon = 'Yes'
        else:
            cancon = 'No'
        long_line_html = json_res['filmMain']['pitch']
        soup = BeautifulSoup(long_line_html, 'html.parser')
        long_line_text = soup.get_text()
        genre = ', '.join(json_res['filmMain']['genre'])
        directors = [director['displayName'] for director in json_res['filmHeader']['director']]
        cast = ', '.join(json_res['filmCredits']['cast'])
        country = ', '.join(json_res['filmCredits']['countries'])
        language = ', '.join(json_res['filmCredits']['languages'])
        runtime = json_res['filmCredits']['runtime']
        status = 'Completed'
        festival_titles = [festival['title'] for festival in json_res['filmCredits']['webProgrammes']]
        festival_seasons = [festival['season'] for festival in json_res['filmCredits']['webProgrammes']]
        festival_string = ', '.join(festival_titles)
        season_string = ', '.join(festival_seasons)
        link = 'https://www.tiff.net/' + link
        data.append([
            title, sales_agent, sold_to, cancon, long_line_text, genre, ', '.join(directors), cast,
            country, language, runtime, link, festival_string, status, season_string
        ])

def save_csv(data):
    df = pd.DataFrame(data, columns=[
        'Title', 'Licensor/Sales Agent', 'Sold To', 'Cancon', 'Logline', 'Genres', 'Director', 'Cast',
        'Country', 'Language', 'Runtime', 'Project Link', 'Festival Program', 'Project Status', 
        'Festival/Market'])
    
    df = df.replace("", "N/A")
    
    df.to_csv('films_release_TIFF_2023.csv', sep=';', encoding='utf-8', index=False)
    print(f'Data saved for {len(data)} pages')

def main():
    link = [] 
    data = []
    names = []
    url = 'https://www.tiff.net'
    page_content = get_page_content_release(url)
    convert_to_bs4(page_content, link)
    find_name_event(link, names)
    get_event_details(names, data, link)
    save_csv(data)

if __name__ == "__main__":
    main()
