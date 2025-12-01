# 📋 Projeto Final - Sistema de Gestão de Tarefas (To-Do List)

![Static Badge](https://camo.githubusercontent.com/8cdbf3ae389801b84e9f67d2533b9c40d837016d1d55a5dd5455809da863998c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5374617475732d50726f6e746f253242)                                                                              ![Static Badge](https://img.shields.io/badge/python-3.10+-blue?logo=python)


Este projeto implementa um **Sistema de Gerenciamento de Tarefas** (To-Do List) no terminal, desenvolvido em Python. [cite_start]Ele atende aos requisitos do Trabalho Final da disciplina de **Programação I** (Python) [cite: 4] [cite_start]do Bacharelado em Engenharia de Software [cite: 3] [cite_start]do Centro Universitário Santo Agostinho (FSA)[cite: 2].

[cite_start]O sistema utiliza a arquitetura **CRUD (Create, Read, Update, Delete)** [cite: 8] [cite_start]para gerenciar todos os registros de tarefas, seguindo o tema sugerido de "Sistema de Tarefas (descrição, status, prazo)".

## 👤 Equipe de Desenvolvimento

| Nome | GitHub Username | Link do Perfil |
| :--- | :--- | :--- |
| **João Eduardo** | JeytheJo | [https://github.com/JeytheJo](https://github.com/JeytheJo) |
| **Pedro Rufino** | pedrorufass | [https://github.com/pedrorufass](https://github.com/pedrorufass) |

## 🚀 Funcionalidades Implementadas

[cite_start]O programa apresenta um menu interativo [cite: 15] [cite_start]com funções separadas para cada operação [cite: 16][cite_start], garantindo clareza e organização do código[cite: 46].

| Opção no Menu | Funcionalidade | Descrição (Operação CRUD) | [cite_start]Requisito [cite: 17, 23, 24] |
| :---: | :--- | :--- | :--- |
| **1** | Cadastrar Nova Tarefa | Adiciona um novo registro à lista, com ID único. | **C**reate |
| **2** | Listar Tarefas | Exibe todos os registros de forma tabular e organizada. | **R**ead |
| **3** | Atualizar Tarefa | Permite editar Nome, Descrição, Prazo e Status de uma tarefa. | **U**pdate |
| **4** | Deletar Tarefa | Remove um registro específico da lista, utilizando o ID. | **D**elete |
| **5** | Relatório de Status | Gera uma análise simples, contando o número de tarefas por Status. | Relatório/Resumo |
| **6** | Sair | Encerra o programa de forma segura. | Sair do Programa |

## 💡 Recursos e Tecnologias

[cite_start]O sistema foi desenvolvido seguindo os requisitos técnicos obrigatórios [cite: 29] da disciplina:

***Estrutura de Dados:** Uso obrigatório de **Lista de Dicionários** para armazenar os registros (`TAREFAS` é a lista principal).
***Funções:** Mínimo de 5 funções, cada uma com responsabilidade clara (`cadastrar_tarefa()`, `listar_TAREFAS()`, `atualizar_tarefa()`, `deletar_tarefa()`, `gerar_relatorio()`, `menu()`).
***Controle de Fluxo:** Utilização de `while True` para o menu principal (repetição) e `if`/`elif`/`else` para tomada de decisões e validações.
***Interação:** Entrada e saída de dados com `input()` e `print()`.
* **Melhoria Visual (BÔNUS):** Utilização de **Códigos de Escape ANSI** para colorir o *Status* das tarefas no terminal (Verde para Concluída, Vermelho para Pendente), uma funcionalidade extra para legibilidade.

## ⚙️ Como Executar o Programa

1.  **Pré-requisitos:** Certifique-se de ter o Python 3 instalado na sua máquina.
2.  **Clonar o Repositório:**
    ```bash
    git clone [https://github.com/JeytheJo/projeto-final-python-JeytheJo-pedrorufass](https://github.com/JeytheJo/projeto-final-python-JeytheJo-pedrorufass)
    cd projeto-final-python-JeytheJo-pedrorufass
    ```
3.  **Executar o Script:**
    ```bash
    sistema_tarefas.py
    ```

## 🖼️ Exemplo de Uso (Menu Principal)

Ao iniciar, o programa exibirá o menu interativo:
### Exemplo de Saída (Opção 2 - Listar Tarefas com Cores)

O sistema apresenta a lista de tarefas, utilizando o ID único [cite: 67] para fácil gerenciamento:

| ID | Status | Prazo | Nome | Descrição |
| :---: | :---: | :---: | :---: | :---: |
| 1 | **(VERDE)** Concluída | 10/11 | Projeto README | Finalizar documentação. |
| 2 | **(VERMELHO)** Pendente | Hoje | Compras | Ir ao supermercado. |

---
*Desenvolvido como Trabalho Final para a disciplina de Programação I - Python, FSA.* 
