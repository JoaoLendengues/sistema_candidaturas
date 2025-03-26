from .conexao import conectar

def salvar_candidato(nome, email, telefone, curriculum):
    try:
        print("Conectando ao banco de dados...")
        conn = conectar()  # Conecta ao banco
        cursor = conn.cursor()
        print(f"Inserindo dados {nome}, {email}, {telefone}, {curriculum}")
        query = """
        INSERT INTO candidatos (nome, email, telefone, curriculum) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (nome, email, telefone, curriculum))
        conn.commit()  # Salva as alterações no banco
        print("Dados inseridos com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao salvar: {err}")
    finally:
        cursor.close()
        conn.close()

