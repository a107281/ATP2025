def Existe_Cinema(cinema, filme):
    cond = False
    for sala in cinema:
        if sala[2] == filme:
            cond = True
    return cond


def Inserir_Sala(cinema, sala):
    if not Existe_Cinema(cinema, sala[2]):
        cinema.append(sala)
        print(f"A sala para o filme foi adicionada.")
    else:
        print(f"A sala com o filme {sala[2]} já existe.")
    return cinema


def Listar(cinema):
    print ("----------------- Lista de Filmes -----------------")
    for sala in cinema:
        nlugares, vendidos, nomef = sala                           
        print(f"Filme: {nomef}       | Nº Lugares: {nlugares}")
    print("---------------------------------------------------")
    return


def Disponivel(cinema, filme, lugar):
    cond = False
    for sala in cinema:
        nlugares, vendidos, nomef = sala
        if nomef == filme and lugar <= nlugares and lugar not in vendidos:
                cond = True
    return cond 


def Vende_Bilhete(cinema, filme, lugar):
    if Disponivel(cinema, filme, lugar):
        for sala in cinema:
            nlugares, vendidos, nomef = sala
            if nomef == filme:
                vendidos.append(lugar)
                return f"O lugar {lugar} para o filme {filme} foi obtido com sucesso!"
    return f"O lugar {lugar} para o filme {filme} não se encontra disponível. Selecione outra opção."
        

def Listar_Disponibilidades(cinema):
    print("----------------- Disponibilidade do Cinema -----------------")
    for sala in cinema:
        nlugares, vendidos, nomef = sala
        disponiveis = nlugares - len(vendidos)       
        print (f"Nome: {nomef}      | Lugares Disponíveis: {disponiveis}")
    print("------------------------------------------------------------")
    return



def menu(cinema):
    cond = True
    opcoes = ("1" , "2" , "3" , "4" , "0") 
    while cond:
        print("--------------- Gestão de Salas de Cinema ----------------")
        print("(1) Listar todos os filmes")
        print("(2) Listar a disponibilidade das salas")
        print("(3) Vender bilhetes para um filme")
        print("(4) Adiciona uma nova sala de cinema")
        print("(0) Sair")
        print("-----------------------------------------------------------")

        escolha = input("Introduza a opção pretendida:")

        if escolha in opcoes:

            if escolha == "1":
                Listar(cinema)
            
            if escolha == "2":
                Listar_Disponibilidades(cinema)
            
            if escolha == "3":
                filme = str(input("Introduza o nome do filme que deseja ver:"))
                lugar = int(input(f"Introduza o número do lugar, entre 1 e o número máximo de lugares da sala, para o filme {filme}:"))
                res = Vende_Bilhete(cinema, filme, lugar)
                print(res)

            if escolha == "4":
                filme = str(input("Introduza o nome do filme:"))
                nlugares = int(input(f"Introduza o número de lugares da sala do filme {filme}:"))
                novoFilme = [nlugares, [], filme]   
                cinema = Inserir_Sala( cinema, novoFilme )
            
            if escolha == "0":
                cond = False
                print("Até à próxima!")
                
        else:
            print("Opção inválida. Por favor, escolha outra opção.")


sala1 = (150, [], "Twilight")
sala2 = (200, [13, 48, 49, 175], "Hannibal")

cinema1 =[sala1, sala2]

menu(cinema1)