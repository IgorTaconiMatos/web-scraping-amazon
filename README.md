O objetivo desse programa é realizar um Web Scraping no site da amazon, apenas por motivos educacionais.
Foi usado os dados da primeira página de busca quando se pesquisa por iphone. O nome e o preço foram armazenados em um arquivo csv.

Para você rodar o software é necessário tem instalado em sua máquina o Python da versão 3 para cima.
Instale as seguintes bibliotecas Python:
	request - Requests é a única biblioteca HTTP não-GMO para Python, segura para consumo humano;
	bs4 - Biblioteca para extrair dados de arquivos HTML e XML;

Com:
pip install -r requirements.txt

Para executar o código:
	python table.py
Um arquivo com nome iphone_amazon.csv irá ser criado e pode ser aberto no excel.
