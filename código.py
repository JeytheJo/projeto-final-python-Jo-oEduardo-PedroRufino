# SISTEMA DE TAREFAS (To-Do List)

TAREFAS = []
proximo_ID = 1  # Variável global para controlar o ID

VERMELHO = "\033[91m"
AMARELO = "\033[93m"
VERDE = "\033[92m"
RESET = "\033[0m"

MAPA_CORES = {
    "Pendente": VERMELHO,
    "Em Andamento": AMARELO,
    "Concluída": VERDE,
}


def linhas():
    print("=" * 60)


def buscar_tarefa(tarefa_id):
    for t in TAREFAS:
        if t["id"] == tarefa_id:
            return t
    return None


# Função 1: CREATE - Insere uma nova tarefa.
def cadastrar_tarefa():
    """Permite ao usuário inserir uma nova tarefa na lista TAREFAS."""
    global proximo_ID

    print("\n--- CADASTRAR NOVA TAREFA ---")

    nome = input("Nome da tarefa (Título curto): ").strip()
    if not nome:
        print("ERRO: O nome da tarefa não pode ser vazio.")
        return

    descricao = input("Descrição detalhada: ").strip()
    if not descricao:
        print("ERRO: A descrição não pode ser vazia.")
        return

    prazo = input("Prazo (ex: 'Hoje', '02/12'): ")

    nova_tarefa = {
        "id": proximo_ID,
        "nome": nome,
        "descricao": descricao,
        "status": "Pendente",  # Status inicial padrão
        "prazo": prazo,
    }

    TAREFAS.append(nova_tarefa)
    print(f"\nTarefa '{nome}' cadastrada com sucesso! (ID: {proximo_ID})")
    proximo_ID += 1
    linhas()


# Função 2: READ - Exibe os registros
def listar_TAREFAS():
    print("\n--- LISTA DE TAREFAS ---")

    if not TAREFAS:
        print("Nenhuma tarefa cadastrada.")
        linhas()
        return

    print(f"{'ID':<5} {'Status':<20} {'Prazo':<12} {'Nome':<20} {'Descrição':<30}")
    print("-" * 85)

    for t in TAREFAS:
        # Lógica para aplicar a cor
        status_texto = t["status"]
        cor = MAPA_CORES.get(
            status_texto, RESET
        )  # Busca a cor, usa RESET como padrão se não encontrar

        status_colorido = f"{cor}{status_texto}{RESET}"

        print(
            f"{t['id']:<5} "
            f"{status_colorido:<20} "  # Usamos a string colorida aqui
            f"{t['prazo']:<12} "
            f"{t['nome']:<20} "
            f"{t['descricao']:<30}"
        )
    print("-" * 85)
    linhas()


# Função 3: UPDATE - Atualiza um registro existente.
def atualizar_tarefa():
    print("\n--- ATUALIZAR TAREFA ---")

    listar_TAREFAS()
    if not TAREFAS:
        return

    try:
        tarefa_id = int(input("\nDigite o ID da tarefa que deseja atualizar: "))
    except ValueError:
        print("ERRO: O ID deve ser um número inteiro.")
        return

    tarefa_atual = buscar_tarefa(tarefa_id)

    if tarefa_atual:
        print(f"\nTarefa selecionada: {tarefa_atual['nome']}")
        print(f"Status atual: {tarefa_atual['status']}")

        print("\nO que deseja atualizar?")
        print("1. Nome (Título)")
        print("2. Descrição")
        print("3. Status")
        print("4. Prazo")

        escolha = input("Escolha a opção (1-4): ")

        if escolha == "1":
            novo_nome = input(f"Novo Nome (Atual: {tarefa_atual['nome']}): ").strip()
            if novo_nome:
                tarefa_atual["nome"] = novo_nome
                print("Nome atualizado!")
            else:
                print("Nome não pode ser vazio.")

        elif escolha == "2":
            nova_desc = input(
                f"Nova Descrição (Atual: {tarefa_atual['descricao']}): "
            ).strip()
            if nova_desc:
                tarefa_atual["descricao"] = nova_desc
                print("Descrição atualizada!")
            else:
                print("Descrição não pode ser vazia.")

        elif escolha == "3":
            print("\nNovos Status Disponíveis: ")
            print("1. Pendente")
            print("2. Em Andamento")
            print("3. Concluída")

            op_status = input("Escolha (1-3): ")
            if op_status == "1":
                tarefa_atual["status"] = "Pendente"
                print(f"Status atualizado para: {tarefa_atual['status']}")
            elif op_status == "2":
                tarefa_atual["status"] = "Em Andamento"
                print(f"Status atualizado para: {tarefa_atual['status']}")
            elif op_status == "3":
                tarefa_atual["status"] = "Concluída"
                print(f"Status atualizado para: {tarefa_atual['status']}")
            else:
                print("Opção de status inválida.")

        elif escolha == "4":
            novo_prazo = input(f"Novo Prazo (Atual: {tarefa_atual['prazo']}): ")
            tarefa_atual["prazo"] = novo_prazo
            print("Prazo atualizado!")

        else:
            print("Opção de atualização inválida.")

    else:
        print(f"ERRO: Tarefa com ID {tarefa_id} não encontrada.")
    linhas()


# Função 4: DELETE - Remove um registro existente (FUNÇÃO SUGERIDA)
def deletar_tarefa():
    """Remove uma tarefa da lista TAREFAS com base no seu ID."""
    print("\n--- DELETAR TAREFA ---")

    listar_TAREFAS()
    if not TAREFAS:
        return

    try:
        tarefa_id = int(input("\nDigite o ID da tarefa que deseja DELETAR: "))
    except ValueError:
        print("ERRO: O ID deve ser um número inteiro.")
        return

    # Usamos o `buscar_tarefa` para verificar se existe
    tarefa_a_remover = buscar_tarefa(tarefa_id)

    if tarefa_a_remover:
        TAREFAS.remove(tarefa_a_remover)
        print(
            f"Tarefa ID {tarefa_id} ('{tarefa_a_remover['nome']}') foi deletada com sucesso."
        )
    else:
        print(f"ERRO: Tarefa com ID {tarefa_id} não encontrada.")
    linhas()


# Estrutura principal do Menu
def menu():
    while True:
        linhas()
        print("         MENU - SISTEMA DE GESTÃO DE TAREFAS")
        linhas()
        print("1. Cadastrar Nova Tarefa (CREATE)")
        print("2. Listar Tarefas (READ)")
        print("3. Atualizar Tarefa (UPDATE)")
        print("4. Deletar Tarefa (DELETE)")  # Adicionada para completar o CRUD
        print("5. Sair")
        linhas()

        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "1":
            cadastrar_tarefa()
        elif escolha == "2":
            listar_TAREFAS()
        elif escolha == "3":
            atualizar_tarefa()
        elif escolha == "4":
            deletar_tarefa()  # Nova função
        elif escolha == "5":
            print("\nObrigado por usar o Sistema de Tarefas. Até logo!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha um número entre 1 e 5.")


# Bloco principal do programa
if __name__ == "__main__":
    menu()
