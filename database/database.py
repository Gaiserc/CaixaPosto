import sqlite3

conexao = sqlite3.connect('caixa.db')


conexao.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY,                                             
    nome TEXT,                                             
    idade INTEGER,                                           
    matricula INTEGER
    )
    """)

conexao.commit()

conexao.execute("""
    CREATE TABLE IF NOT EXISTS turnos (
    id INTEGER PRIMARY KEY,
    funcionario_id INTEGER,
    periodo TEXT,
    status TEXT,
    data_abertura TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(funcionario_id) REFERENCES funcionarios(id)
    )
    """)

conexao.commit()

conexao.execute("""
    CREATE TABLE IF NOT EXISTS registros_vendas (
    id INTEGER PRIMARY KEY,
    funcionario_id INTEGER,
    turno_id INTEGER,
    bico INTEGER,
    combustivel TEXT,
    encerrante_inicial REAL,
    encerrante_final REAL,
    litros_vendidos REAL,
    preco_praticado REAL,
    valor_venda REAL,
    data_registro DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(funcionario_id) REFERENCES funcionarios(id),
    FOREIGN KEY(turno_id) REFERENCES turnos(id)
    )
    """)

conexao.commit()

conexao.execute("""
    CREATE TABLE IF NOT EXISTS combustiveis (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    preco_atual REAL
    )
    """)

conexao.commit()

conexao.execute("""
    CREATE TABLE IF NOT EXISTS bicos (
    id INTEGER PRIMARY KEY,
    combustiveis_id INTEGER,
    FOREIGN KEY(combustiveis_id) REFERENCES combustiveis(id)
    )
    """)

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
