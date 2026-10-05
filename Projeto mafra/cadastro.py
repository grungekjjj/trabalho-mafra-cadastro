alunos = []

def exibir_menu():
    print("1. Adicionar aluno")
    print("2. Listar todos")
    print("3. Buscar aluno")
    print("4. Remover aluno")
    print("5. Média das notas")
    print("6. Sair")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print('Vamos dar inicio ao cadastro!')
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        nota = float(input("Digite a nota do aluno(0 a 10): "))

        while nota < 0 or nota > 10:
            print('Nota invalida digite novamente!')
            nota = float(input('Digite a nota do aluno(0 a 10): '))
        aluno = {
            'nome': nome,
            'idade': idade,
            'nota': nota,
        }
        alunos.append(aluno)
        print('Aluno cadastrado com sucesso!')

    elif opcao == '2':
        print('Lista de todos os alunos:')
        if len(alunos) == 0:
            print('Nenhum aluno cadastrado!')
        else:
            for aluno in alunos:
                print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")

    elif opcao == '3':
        busca = input('Digite o nome do aluno que deseja buscar: ')
        encontrado = False
        for aluno in alunos:
            if aluno['nome'].lower() == busca.lower():  
                print(f"Nome: {aluno['nome']}\nIdade: {aluno['idade']}\nNota: {aluno['nota']}")
                encontrado = True
        if not encontrado:
            print('Aluno não encontrado!')


    elif opcao == '4':
        remover_aluno = input('Digite o nome do aluno que deseja remover:')
        for aluno in alunos:
            if aluno['nome'].lower() == remover_aluno.lower():
                alunos.remove(aluno)
                print('Aluno removido com sucesso!')
                break
            else:
                print('Aluno não encontrado!')
    
    elif opcao == '5':
        if len(alunos) == 0:
            print('Nenhum aluno cadastrado!')
        else:
            soma = 0
            for aluno in alunos:
                soma += aluno['nota']
            media = soma / len(alunos)
            print(f'Média das notas: {media:.2f}')
            
    elif opcao == '6':
        print('Saindo do programa...')
        break
    
    else:
        print('Opção invalida, tente uma opção existente (1 a 6)!')