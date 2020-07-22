
# Instalando

pip install -r requirements.txt

Baixar o https://github.com/mozilla/geckodriver/releases correspondente ao firefox instalado.

# Executar

O programa vai baixar o mais novo arquivo aberto de domínios e renomear para sites.txt
http://dados.gov.br/dataset/dominios-gov-br

python check_site.py  - Tira um printscreen dos sites do governo e cria lista com os erros e sites que deram ok.

python check_barra.py - Checa se a barra brasil está presente e se está de forma dinâmica ou não.

# Atenção

Esse programa só checa os subdomínios 'www' e não percorre todos os subdomínios de um domínio
