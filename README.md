# Sistema de Gerenciamento de Caixa para Postos de Combustível

## O Problema e a Solução
Durante a minha rotina como frentista, o fechamento financeiro dos caixas era confuso, manual e lento. Para solucionar esse problema, desenvolvi este sistema em Python para organizar os turnos, registrar os bicos trabalhados e automatizar os cálculos financeiros no encerramento do expediente.

## Status do Projeto
**Versão Atual:** Produto Mínimo Viável (MVP) concluído e funcional no terminal.
O sistema atualmente suporta o ciclo de vida completo de cada expediente:
1. Autenticação e abertura de turno.
2. Seleção dinâmica dos bicos trabalhados e inserção das leituras (encerrantes) iniciais.
3. Loop contínuo
4. Fechamento do turno com o registro das leituras finais e cálculo automático das vendas.

## Arquitetura e Tecnologias
O projeto foi construído focando nas melhores práticas de desenvolvimento backend:
* **Python (Orientação a Objetos):** Regras de negócio encapsuladas em classes (`Turno`, `Bico`, `Combustivel`, `Registro_bico_turno`) e separadas em módulos.
* **Banco de Dados Relacional (SQLite):** Fim dos dados em memória. A aplicação cria e gerencia o banco local `caixa.db`.
* **Modelagem de Dados:** Uso de `PRIMARY KEY` e `FOREIGN KEY` relacionando vendas, turnos, bicos e frentistas.
* **Consultas Avançadas:** População dinâmica dos menus utilizando `JOIN` para cruzar tabelas de bicos e combustíveis.
* **Blindagem (Resiliência):** Tratamento de exceções com blocos `try/except` para impedir que o sistema quebre caso o usuário digite letras em vez de números durante a operação.
* **Segurança e Versionamento:** Proteção do banco de dados de produção através da correta configuração do `.gitignore`.

## Próximos Passos (Roadmap)
 As próximas etapas da trilha técnica incluem:
1. Construção da interface gerencial (cálculo de comissões, faturamento mensal, volume por combustível) delegando a carga de processamento das agregações (`SUM`, `COUNT`, `GROUP BY`) para o banco de dados.
2. Transformação em API: Refatoração da arquitetura atual para transformar o sistema de terminal em um backend web que responde via requisições REST (JSON).
3. Migração do banco local para PostgreSQL e adoção de testes automatizados (`pytest`).
