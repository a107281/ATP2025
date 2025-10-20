# TPC5: Aplicação para gestão de Alunos

## Beatriz Maia Oliveira A107281

## Resumo
- O TPC5 consistiu em desenvolver o código, em Python, para uma aplicação para gestão de alunos.

### O programa
Considere que o modelo do aluno e da turma têm a seguinte estrutura:

`aluno = (nome, id, [notaTPC, notaProj, notaTeste])`

`turma = [aluno]`

* Cria uma aplicação que coloca no monitor o seguinte menu de operações:
    - 1: Criar uma turma;
    - 2: Inserir um aluno na turma;
    - 3: Listar a turma;
    - 4: Consultar um aluno por id;
    - 8: Guardar a turma em ficheiro;
    - 9: Carregar uma turma dum ficheiro;
    - 0: Sair da aplicação
* No fim de executar a operação selecionada, a aplicação deverá colocar novamente o menu e pedir ao utilizador a opção para continuar;
* Utiliza a tua aplicação para criar uma turma com 5 alunos.

## Resultados
```python
def menu():
    print("-------------------- MENU ---------------------")
    print("(1) Criar uma turma")
    print("(2) Inserir um aluno na turma")
    print("(3) Listar a turma")
    print("(4) Consultar um aluno por ID")
    print("(5) Guardar a turma em ficheiro")
    print("(6) Carregar uma turma dum ficheiro")
    print("(0) Sair da Aplicação")
    print("-----------------------------------------------")


def Criar_Turma():
    return []


def Inserir_Aluno(turma):
    nome = input("Nome do aluno: ")
    id = input("ID do aluno: ")
    notaTPC = float(input("Nota do TPC: "))
    notaProj = float(input("Nota do Projeto: "))
    notaTeste = float(input("Nota do Teste: "))

    aluno = (nome, id, [notaTPC, notaProj, notaTeste])
    turma.append(aluno)
    print(f"O(A) aluno(a) {nome} foi adicionado(a) com sucesso!")
    return turma


def Listar_Turma(turma):
    if turma:
        print("Listagem da turma:")
        for aluno in turma:
            print(f"\nNome: {aluno[0]} \nID: {aluno[1]} \nNota do TPC: {aluno[2][0]} \nNota do Projeto: {aluno[2][1]} \nNota do Teste: {aluno[2][2]}")
    else:
        print("A turma está vazia.")



def Consultar_por_ID(turma):
    id_consultar = input("Digite o ID do aluno que deseja consultar: ")
    aluno_encontrado = False
    for aluno in turma:
        if id_consultar == aluno[1]:
            aluno_encontrado = True
            print(f"Aluno encontrado! \nNome: {aluno[0]} \nNota do TPC: {aluno[2][0]} \nNota do Projeto: {aluno[2][1]} \nNota do Teste: {aluno[2][2]}")
        if not aluno_encontrado:
            print("Aluno não encontrado.")



def Guardar_Turma_num_Ficheiro(turma):
    nome_ficheiro = input("Nome do ficheiro para guardar a turma (exemplo: turma.txt): ")
    
    file = open(nome_ficheiro, "w", encoding="utf-8")
    for aluno in turma:
        linha = f"{aluno[0]},{aluno[1]},{aluno[2][0]},{aluno[2][1]},{aluno[2][2]}\n"
        file.write(f"{linha}")
    file.close()
    print(f"Turma guardada com sucesso no ficheiro {nome_ficheiro}!")



def Carregar_Turma_de_Ficheiro():
    nome_ficheiro = input("Nome do ficheiro para carregar (ex: turma.txt): ")
    turma = []

    file = open(nome_ficheiro, "r", encoding="utf-8")
    for linha in file:
                dados = linha.strip().split(",")
                nome = dados[0]
                id = dados[1]
                notas = [float(dados[2]), float(dados[3]), float(dados[4])]
                aluno = (nome, id, notas)
                turma.append(aluno)
    file.close()
    print(f"Turma carregada com sucesso do ficheiro {nome_ficheiro}!")
    print(turma)
    return turma



def main():
    turma = []
    cond = True

    while cond:
        menu()
        opcao = input("Introduza uma opção: ")

        if opcao == "1":
            turma = Criar_Turma()
            print("Nova turma criada.")

        elif opcao == "2":
            turma = Inserir_Aluno(turma)

        elif opcao == "3":
            Listar_Turma(turma)

        elif opcao == "4":
            Consultar_por_ID(turma)

        elif opcao == "5":
            Guardar_Turma_num_Ficheiro(turma)

        elif opcao == "6":
            turma = Carregar_Turma_de_Ficheiro()

        elif opcao == "0":
            cond = False
            print("Até à próxima!")

main()
