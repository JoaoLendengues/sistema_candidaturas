import mysql.connector
from app_web.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

def conectar():
    try:
        conn = mysql.connector.connect(
            host="10.1.1.9",
            user="Joao",
            password="@Jvpdata03",
            database="sistema_candidaturas"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

