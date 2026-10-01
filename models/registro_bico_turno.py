class Registro_bico_turno():
    def __init__(self, bico, encerrante_inicial, preco_praticado, funcionario_id, combustivel, turno_id):
        self.bico = bico
        self.encerrante_inicial = encerrante_inicial
        self.preco_praticado = preco_praticado
        self.funcionario_id = funcionario_id
        self.combustivel = combustivel
        self.turno_id = turno_id

    def registrar_encerrante_final(self, encerrante):
        if encerrante < self.encerrante_inicial:
            raise ValueError("Valores indevidos")
        self.encerrante_final = encerrante

    def calcular_venda(self):
        venda = self.encerrante_final - self.encerrante_inicial
        return venda

    def valor_da_venda(self):
        valor = self.preco_praticado * self.calcular_venda()
        return valor

    def salvar_no_banco(self,conexao):
        comando_sql = """
        INSERT INTO registros_vendas (
            funcionario_id, bico, combustivel, encerrante_inicial, encerrante_final, litros_vendidos, preco_praticado, valor_venda, turno_id
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        dados = (self.funcionario_id,
                 self.bico,
                 self.combustivel,
                 self.encerrante_inicial,
                 self.encerrante_final,
                 self.calcular_venda(),
                 self.preco_praticado,
                 self.valor_da_venda(),
                 self.turno_id
                 )

        conexao.execute(comando_sql, dados)

        conexao.commit()