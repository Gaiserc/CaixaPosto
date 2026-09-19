import sqlite3

conexao = sqlite3.connect('caixa.db')


conexao.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (id INTEGER PRIMARY KEY, 
                                            nome TEXT, 
                                            idade INTEGER,
                                            matricula INTEGER)""")

conexao.commit()

def salvar_funcionario(funcionario):
    conexao.execute("""
    INSERT INTO funcionarios (nome, idade, matricula) 
    VALUES (?, ?, ?)
    """, (funcionario.nome, funcionario.idade, funcionario.matricula))

    conexao.commit()

def listar_funcionarios():
    resultado = conexao.execute("""
        SELECT * FROM funcionarios 
        """)
    funcionarios = resultado.fetchall()
    return funcionarios

def buscar_funcionario(matricula):
    resultado = conexao.execute("""
    SELECT * FROM funcionarios 
    WHERE matricula = ?
    """, (matricula,))

    funcionario = resultado.fetchone()

    if funcionario is None:
        raise ValueError("funcionario não encontrado")

    return funcionario


print("banco conectado")
