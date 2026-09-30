class Turno:
    def __init__(self, periodo, funcionario):
        self.periodo = periodo
        self.funcionario = funcionario
        self.registros_bicos = []


    def add_registro_bico(self, registro):

        encontrou = False

        for bico_existente in self.registros_bicos:

            if registro.bico.numero == bico_existente.bico:
                encontrou = True
                print("esse bico ja existe")

        if not encontrou:
            self.registros_bicos.append(registro)

    def mostrar_registros(self):

        for registro in self.registros_bicos:
            print(f"Bico {registro.bico} | Inicial: {registro.encerrante_inicial} | Final: {registro.encerrante_final} | Venda:  {registro.calcular_venda()}")

    def resumo_turno(self):
        total = 0
        for resumo in self.registros_bicos:
            total += resumo.calcular_venda()
        print(f"Total de vendas: {total}litros")

    def resumo_financeiro(self):
        total = 0
        for registro in self.registros_bicos:
            total += registro.valor_da_venda()
        print(f"Total de vendas: R$ {total:.2f}")