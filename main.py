from models.combustivel import Combustivel
from models.funcionario import Funcionario
from models.bico import Bico
from models.registro_bico_turno import Registro_bico_turno
from models.turno import Turno

from database.database import conexao, salvar_funcionario, listar_funcionarios, buscar_funcionario


# registrando funcionario
print(listar_funcionarios())



while True:
    matricula_escolhida = int(input("Digite a matricula do funcionario: \n"))
    try:
        funcionario_dados = buscar_funcionario(matricula_escolhida)

        funcionario = Funcionario(
            funcionario_dados[1],
            funcionario_dados[2],
            funcionario_dados[3],
        )

        print(f"Nome: {funcionario.nome} | Idade: {funcionario.idade} | matricula: {funcionario.matricula} \n ")
        break
    except ValueError as erro:
        print(erro)

# --- INÍCIO DA BUSCA DINÂMICA ---
cursor = conexao.execute("""
    SELECT bicos.id, combustiveis.nome, combustiveis.preco_atual 
    FROM bicos 
    JOIN combustiveis ON bicos.combustiveis_id = combustiveis.id
""")
dados_bicos = cursor.fetchall()

bicos = {}
busca = []
texto_menu = "Quais bicos você vai trabalhar?\n"  # Texto dinâmico para o input

for linha in dados_bicos:
    bico_id = linha[0]
    nome_combustivel = linha[1]
    preco_combustivel = linha[2]

    combustivel_obj = Combustivel(nome_combustivel, preco_combustivel)
    bico_obj = Bico(bico_id, combustivel_obj)

    bicos[bico_id] = bico_obj
    busca.append(bico_id)

    # Monta as opções do menu dinamicamente com base no banco
    texto_menu += f" {bico_id} - Bico {bico_id} ({nome_combustivel})\n"

texto_menu += "\nDigite os números dos bicos: "
# --- FIM DA BUSCA DINÂMICA ---

bicos_escolhidos = []

bicos_escolhidos = []

# criando o turno
turno = Turno("Manhã", funcionario )
turno.abrir_turno_banco(conexao)
print(f"Turno aberto no banco com ID: {turno.id} \n")

def iniciar_turno():

    escolha = input(texto_menu)

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
         while True:
             try:
                encerrante = int(
                    input(f"Digite o encerrante inicial do bico {bico.numero}: ")
                )
                break
             except ValueError:
                print("Erro: Por favor, digite somente numeros inteiros")
         registro = Registro_bico_turno(
            bico.numero,
            encerrante,
            bico.combustivel.preco_atual,
            funcionario.matricula,
            bico.combustivel.nome,
            turno.id
                )

         turno.add_registro_bico(registro)
    # No final da função, joga o turno para fora para o menu poder usar
    return turno


def encerrar_turno(turno):

    if turno is None:
        print("\nErro: Não há nenhum turno aberto no momento!")
        return None

    print(f"\n--- ENCERRANDO O TURNO {turno.id} ---")

    for registro in turno.registro_bicos:

        while True:
            try:
                encerrante_final = int(
                    input(f"Digite o encerrante final do bico {registro.numero_bico}:")
                )
                break
            except ValueError:
                print("Erro: Por favor, digite somente numeros inteiros")

        # Salva a resposta na memória e no banco
        registro.registrar_encerrante_final(encerrante_final)
        # salva o registro completo no banco de dados
        registro.salvar_no_banco(conexao)

    turno.fechar_turno_banco(conexao)
    turno.resumo_financeiro()

turno_atual = None

while True:
    print("\n --- - -- - CAIXA --- - - - - ")
    print("1. Iniciar Turno")
    print("2. Encerrar Turno")
    print("3. Sair do Sistema")
    opcao = input("Escolha: ")

    if opcao == "1":
        turno_atual = iniciar_turno()
        print(f"\nTurno {turno_atual.id} iniciado com sucesso!")

    elif opcao == "2":
        print("Iniciando Encerramento")
        encerrar_turno(turno_atual)
        turno_atual = None
        break
    elif opcao == "3":
        print("Saindo do Sistema")
        break
    else:
        print("Opção invalida")


"""
turno.mostrar_registros()
turno.resumo_turno()


print("Turno encerrado e salvo com sucesso no banco de dados!")"""



