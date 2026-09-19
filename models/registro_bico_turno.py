class Registro_bico_turno():
    def __init__(self, bico, encerrante_inicial, preco_praticado):
        self.bico = bico
        self.encerrante_inicial = encerrante_inicial
        self.preco_praticado = preco_praticado
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