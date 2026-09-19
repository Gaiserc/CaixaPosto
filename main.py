from models.combustivel import Combustivel
from models.funcionario import Funcionario
from models.bico import Bico
from models.registro_bico_turno import Registro_bico_turno
from models.turno import Turno

from database.database import conexao, salvar_funcionario, listar_funcionarios, buscar_funcionario

# registrando funcionario
print(listar_funcionarios())


###nome = input("Qual o seu nome: ")
###idade = int(input("Qual a sua idade: "))
matricula = int(input("Qual a sua matricula: "))
funcionario_dados = buscar_funcionario(matricula)

funcionario = Funcionario(
    funcionario_dados[1],
    funcionario_dados[2],
    funcionario_dados[3],
)

print(funcionario.nome)
print(funcionario.idade)
print(funcionario.matricula)

###funcionario = Funcionario(nome, idade, matricula)
###salvar_funcionario(funcionario)

"""
# adicionando combustivel
combustivel1 = Combustivel("Etanol", 4.78)
combustivel2 = Combustivel("Aditivada", 6.69)
combustivel3 = Combustivel("Gasolina", 6.57)
combustivel4 = Combustivel("S500", 6.94)
combustivel5 = Combustivel("S10", 6.99)

# registrando bico
bico1 = Bico(1, combustivel1)
bico2 = Bico(2, combustivel2)
bico3 = Bico(3, combustivel3)

# dicionario dos bicos
bicos = {
    1: bico1,
    2: bico2,
    3: bico3,
}

# lista de bicos disponiveis para escolher
busca = [1, 2, 3]

bicos_escolhidos = []

# criando o turno
turno = Turno("Manhã", funcionario )

def iniciar_turno():
    escolha = input(f"Quais bicos você vai trabalhar? \n 1 - Bico 1 (Etanol) \n 2 - Bico 2 (Aditivada) \n 3 - Bico 3 (Gasolina) \n \n Digite os números dos bicos: ")

    escolhido = escolha.split(", ")

    convertido = []

    for item in escolhido:
        convertido.append(int(item))

    for numero_escolhido in convertido:
        for bic in busca:
            encontrou = False

            if bic == numero_escolhido:
                correspondente = bicos.get(numero_escolhido)
                bicos_escolhidos.append(correspondente)

                print(f"Bico {correspondente.numero} →  {correspondente.combustivel.nome}")

                encontrou = True

    for bico in bicos_escolhidos:
        encerrante = int(
            input(f"Digite o encerrante inicial do bico {bico.numero}: ")
        )
        registro = Registro_bico_turno(
            bico,
            encerrante,
            bico.combustivel.preco_atual
        )

        turno.add_registro_bico(registro)

        encerrante_final = int(
            input(f"Digite o encerrante final do bico {bico.numero}: ")
        )

        registro.registrar_encerrante_final(encerrante_final)
iniciar_turno()


turno.mostrar_registros()
turno.resumo_turno()
turno.resumo_financeiro()
"""