# Sistema de TAREFAS (To-Do List)

TAREFAS = []
proximo_ID = 1  # Variável global para controlar o ID


def linhas():
    print("=" * 60)


# Função 1: CREATE - Insere uma nova tarefa.
def cadastrar_tarefa():
    global proximo_ID

    print("\n--- CADASTRAR NOVA TAREFA ---")

    # 1. Solicitação: Nome da Tarefa
    nome = input("Nome da tarefa (Título curto): ").strip()
    if not nome:
        print("ERRO: O nome da tarefa não pode ser vazio.")
        return

    # 2. Solicitação da descrição
    descricao = input("Descrição detalhada: ").strip()
    if not descricao:
        print("ERRO: A descrição não pode ser vazia.")
        return

    prazo = input("Prazo (ex: 'Hoje', '02/12'): ")

    # Criação do dicionário
    nova_tarefa = {
        "id": proximo_ID,
        "nome": nome,
        "descricao": descricao,
        "status": "Pendente",
        "prazo": prazo,
    }

    TAREFAS.append(nova_tarefa)
    print(f"\nTarefa '{nome}' cadastrada com sucesso! (ID: {proximo_ID})")
    proximo_ID += 1


# Função 2: READ - Exibe os registros
def listar_TAREFAS():
    print("\n--- LISTA DE TAREFAS ---")

    if not TAREFAS:
        print("Nenhuma tarefa cadastrada.")
        return

    # Cabeçalho ajustado para incluir o NOME
    print(f"{'ID':<5} {'Status':<15} {'Prazo':<12} {'Nome':<20} {'Descrição':<30}")
    print("-" * 85)

    for t in TAREFAS:
        # Exibe cada campo formatado
        print(
            f"{t['id']:<5} "
            f"{t['status']:<15} "
            f"{t['prazo']:<12} "
            f"{t['nome']:<20} "
            f"{t['descricao']:<30}"
        )
    print("-" * 85)


def buscar_tarefa(tarefa_id):
    for t in TAREFAS:
        if t["id"] == tarefa_id:
            return t
    return None


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
            elif op_status == "2":
                tarefa_atual["status"] = "Em Andamento"
            elif op_status == "3":
                tarefa_atual["status"] = "Concluída"
            if __name__ == "__main__":
                menu()
