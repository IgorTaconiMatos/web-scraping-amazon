# Web Scraping Com Python no site da Amazon
O objetivo desse programa é realizar um Web Scraping no site amazon.com.br.
Foi coletado os dados da primeira página da busca por iphone.
O nome e o preço foram armazenados em um arquivo csv.
## Começando
Clone o projeto em sua máquina
```
git clone https://github.com/taconi/web-scraping-amazon.git
```
## Pré-requisitos
Para você rodar o software é necessário tem instalado em sua máquina o __Python3.6.+__.   
## Virtualenv
Recomendo não instalar nada em sua máquina e criar um virtualenv para não quebrar algum possível projeto que esteja em sua máquina e que possa estar usando as bibliotecas ou frameworks aqui instalados em uma outra versão. Mas, fique a fontade.
### Criando o virtualenv com Python3
Entre no diretório clonado e execute o comando.
```
cd web-scraping-amazon
python -m venv .venv
```
### Ativando o virtualenv
```
source .venv/bin/activate
```
## Instalado as dependências
```
pip install -r requirements.txt
```
## Executar
Para executar o script use o código abaixo:
```
python create_csv.py
```
Um arquivo com nome products.csv irá ser criado.
## Contribuindo
Sinta-se à vontade para enviar pull requests.
