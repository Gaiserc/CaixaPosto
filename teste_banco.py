from database.database import conexao
try:
    cursor = conexao.execute("""SELECT * FROM registros_vendas
    """)
    conexao.commit()
    registros = cursor.fetchall()

    print(registros)
except Exception as erro:
    print("erro ao acessar o banco de dados")