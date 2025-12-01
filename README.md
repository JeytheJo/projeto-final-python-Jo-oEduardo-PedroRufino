# 📋 Projeto Final - Sistema de Gestão de Tarefas (To-Do List)

![Static Badge](https://camo.githubusercontent.com/8cdbf3ae389801b84e9f67d2533b9c40d837016d1d55a5dd5455809da863998c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374617475732d50726f6e746f253242)        ![Static Badge](https://img.shields.io/badge/python-3.10+-blue?logo=python)                ![Static Badge](https://img.shields.io/badge/to_do-list+-green?logo=ok)


Este projeto implementa um **Sistema de Gerenciamento de Tarefas** (To-Do List) no terminal, desenvolvido em Python. Ele atende aos requisitos do Trabalho Final da disciplina de **Programação I** (Python) do Bacharelado em Engenharia de Software do Centro Universitário Santo Agostinho (FSA).

O sistema utiliza a arquitetura **CRUD (Create, Read, Update, Delete)** para gerenciar todos os registros de tarefas, seguindo o tema sugerido de "Sistema de Tarefas (descrição, status, prazo)".

## 👤 Equipe de Desenvolvimento

| Nome | GitHub Username | Link do Perfil |
| :--- | :--- | :--- |
| **João Eduardo** | JeytheJo | [https://github.com/JeytheJo](https://github.com/JeytheJo) |
| **Pedro Rufino** | pedrorufass | [https://github.com/pedrorufass](https://github.com/pedrorufass) |

---

## 🚀 Funcionalidades Implementadas

O programa apresenta um **menu interativo** com funções separadas para cada operação, garantindo clareza e organização do código.

| Opção no Menu | Funcionalidade | Descrição (Operação CRUD) | Requisito |
| :---: | :--- | :--- | :--- |
| **1** | Cadastrar Nova Tarefa | Insere um novo registro com ID único. | **C**reate |
| **2** | Listar Tarefas | Exibe todos os registros de forma tabular. | **R**ead |
| **3** | Atualizar Tarefa | Permite editar detalhes de um registro existente. | **U**pdate |
| **4** | Deletar Tarefa | Exclui um registro da lista, utilizando o ID. | **D**elete |
| **5** | Relatório de Status | Gera uma análise de resumo, contando tarefas por status. | Relatório/Resumo |
| **6** | Filtrar por Status | **(EXTRA)** Permite listar apenas tarefas de um status específico. | Estrutura Sofisticada |
| **7** | Sair | Encerra o sistema de forma segura. | Sair do Programa |

---

## 💡 Recursos e Tecnologias

O sistema foi desenvolvido seguindo todos os requisitos técnicos obrigatórios.

* **Estrutura de Dados:** Uso obrigatório de **Lista de Dicionários** para armazenar os registros (`TAREFAS` é a lista principal).
* **Funções:** Mínimo de 5 funções, cada uma com responsabilidade clara (`menu()`, `cadastrar_tarefa()`, `listar_TAREFAS()`, `atualizar_tarefa()`, `deletar_tarefa()`, `gerar_relatorio()`, `filtrar_tarefas()`).
* **Controle de Fluxo:** Utilização de estruturas de repetição (`while` e `for`) para o menu e percorrer registros, e condicionais (`if`/`elif`/`else`) para controle de decisões.
* **Boas Práticas:** Código com indentação, comentários, nomes de variáveis e funções significativos, e mensagens amigáveis ao usuário.

### 🌟 Bônus Implementado (0,5 Ponto Extra)

Para buscar o ponto extra, foi implementada uma estrutura mais sofisticada:

* **List Comprehension:** Utilizada na função **`filtrar_tarefas()`** para criar de forma concisa e eficiente uma nova lista contendo apenas as tarefas que correspondem ao status desejado.

* **Melhoria Visual:** Utilização de **Códigos de Escape ANSI** para colorir o *Status* das tarefas no terminal (Verde para Concluída, Vermelho para Pendente) para melhorar a legibilidade.

---

## ⚙️ Como Executar o Programa

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado na sua máquina.
2.  **Clonar o Repositório:**
    ```bash
    https://github.com/JeytheJo/projeto-final-python-Jo-oEduardo-PedroRufino
    cd projeto-final-python-Jo-oEduardo-PedroRufino
    ```
3.  **Executar o Script:**
    Assumindo que o nome do arquivo principal é `sistema_tarefas.py`:
    ```bash
    python sistema_tarefas.py
    ```

---

## 🖼️ Exemplo de Uso (Menu Principal)

Ao iniciar, o programa exibirá o menu interativo:

Ao iniciar, o programa exibirá o menu interativo:
### Exemplo de Saída (Opção 2 - Listar Tarefas com Cores)

O sistema apresenta a lista de tarefas, utilizando o ID único [cite: 67] para fácil gerenciamento:

| ID | Status | Prazo | Nome | Descrição |
| :---: | :---: | :---: | :---: | :---: |
| 1 | **(VERDE)** Concluída | 10/11 | Projeto README | Finalizar documentação. |
| 2 | **(VERMELHO)** Pendente | Hoje | Compras | Ir ao supermercado. |

---
*Desenvolvido como Trabalho Final para a disciplina de Programação I - Python, FSA.* 
