lista = []
x = 0

#MENU INICIO
while x == 0:

    print("Bem Vindo a sua bliblioteca de jogos!!!\n")
    print("Abaixo estão listadas algumas funções. Comece adicionando alguns jogos a sua bliblioteca basta digitar 1\n")

    print("[1] Inserir game")
    print("[2] Consultar games")
    print("[3] Alterar game")
    print("[4] Excluir game")
    print("[5] Salvar bliblioteca")
    print("[6] Importar bliblioteca")
    print("[7] Sair\n")


    resposta = int(input("Digite a opção desejada : "))
#MENU FIM

#INSERT
    if resposta == 1:
        insira = str(input("\nO que deseja incluir ?\n"))
        lista.append(insira)
        print("Item inserido com sucesso!!!\n")
        print(lista)

#Select
    elif resposta == 2:
        consultar = str(input("\nQual elemento vc gostaria de verificar ?\n"))
        if consultar in lista:
            print("O item está na lista\n")
        else:
            consultarn = consultar+'\n'
            if consultarn in lista:
                print("O item está na lista\n")
            else:
                print("O item não esta na lista. Gostaria de adicionar ?\n")
                print("[1] Sim")
                print("[2] Não\n")
                cond_consu = int(input("Selecione : "))
                if cond_consu == 1:
                    lista.append(consultar)
                    print("\nItem adicionado\n")
                    print(lista,"\n")
                else:
                    print("\nVoltando para o menu")

#Alterar
    elif resposta == 3:
        print(lista)
        alteracao = str(input("\nEscreva o item para fazer a substituição : \n"))
        count = int(input("Selecione a posição do item que deseja alterar (ATENÇÃO : A CONTAGEM COMEÇA DO 0)\n"))
        lista[count] = alteracao
        print(lista)

#Delete
    elif resposta == 4:
        print("\nSelecione o elemento a ser removido\n")
        print(lista)
        remover = str(input("Digite o elemento para ser removido (NÃO ESCREVA : '\_n') : \n"))
        if remover in lista:
            lista.remove(remover)
        else:
            removern = remover+'\n'
            lista.remove(removern)
        print(lista)

#Gravar arquivo
    elif resposta == 5:
        arquivo = open("texto.txt","a")
        arquivo.writelines(line + "\n" for line in lista)

#Importar arquivo
    elif resposta == 6:
        arquivo = open("texto.txt","r")
        lista = arquivo.readlines()
        print(lista)


#Exit
    elif resposta == 7:
        exit()
