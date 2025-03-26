import os

# Configurações do Flask
SECRET_KEY = os.urandom(24) # Chave secreta para sessões
UPLOAD_FOLDER = 'uploads/' # Diretório para armazenar os curriculos em PDF
ALLOWED_EXTENSIONS = {'pdf'} # Tipos de arquivos permitidos

# Configurações do banco de dados (MySQL)
MYSQL_HOST = '10.1.1.9'
MYSQL_USER = 'Joao'
MYSQL_PASSWORD = '@Jvpdata03'
MYSQL_DB = 'sistema_candidaturas'