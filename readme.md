# TIFF Film Data Scraper

Este script foi desenvolvido como um projeto freelancer para extrair informações relacionadas a filmes do site do TIFF (Festival Internacional de Cinema de Toronto). O script realiza a coleta de dados sobre novos lançamentos, detalhes dos eventos e informações relevantes.

## Funcionalidades

O script realiza as seguintes tarefas:

1. Utiliza a biblioteca `playwright.sync_api` para controlar um navegador e carregar a página de "Novos Lançamentos" do site do TIFF.
2. Extrai links para as páginas individuais de eventos de filmes a partir do conteúdo da página.
3. Coleta detalhes como título, agente de vendas, distribuidores, sinopse, gêneros, diretores, elenco, países, idiomas, duração, status do projeto e detalhes dos festivais/marketings.
4. Organiza os dados coletados em um DataFrame usando a biblioteca `pandas` e, em seguida, os salva em um arquivo CSV chamado `films_release_TIFF_2023.csv`.

## Bibliotecas Utilizadas

- **playwright.sync_api**: Automatiza a interação com páginas da web através do controle de navegadores.
- **BeautifulSoup**: Extrai informações de HTML e XML para análise.
- **re (Expressões Regulares)**: Utilizado para buscar padrões em strings.
- **requests**: Realiza requisições HTTP para obtenção de conteúdo web.
- **pandas**: Manipulação e organização de dados em formato tabular.

## Como Usar

1. Instale as bibliotecas necessárias executando o seguinte comando:
   ```
   pip install playwright beautifulsoup4 pandas requests
   ```

2. Execute o script usando o seguinte comando:
   ```
   python nome_do_script.py
   ```

3. O script coletará dados do site do TIFF, processará as informações e as salvará em um arquivo CSV chamado `films_release_TIFF_2023.csv`.

## Notas

- O script inclui tratamento de erros para garantir que o processo continue mesmo se alguns elementos de dados estiverem ausentes ou indisponíveis.
- Para evitar sobrecarga no servidor, há um atraso de 1 segundo após cada página processada.

Este projeto foi desenvolvido como um trabalho freelancer e é uma demonstração do uso de automação para coletar informações valiosas de um site.

---

**Nota:** Substitua `nome_do_script.py` pelo nome real do seu arquivo de script Python.

Se você tiver alguma dúvida ou sugestão de melhoria para este README, sinta-se à vontade para personalizá-lo de acordo com suas necessidades.