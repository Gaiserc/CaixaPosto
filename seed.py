from database.database import conexao

conexao.execute("""
    INSERT INTO combustiveis (nome, preco_atual) 
    VALUES ('Etanol', 4.78),
           ('Aditivada', 6.69),
           ('Gasolina', 6.57)
    """)

conexao.commit()

conexao.execute("""
    INSERT INTO bicos (id, combustiveis_id) 
    VALUES (1, 1), 
           (2, 2),
           (3, 3)    
""")

conexao.commit()

conexao.execute("""
    INSERT INTO funcionarios (nome, idade, matricula) 
    VALUES ('Erick', 25, 3421),
           ('João', 30, 231),
           ('Maria', 28, 132)
""")

conexao.commit()

print("sementes plantadas com sucesso")