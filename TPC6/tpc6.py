import matplotlib.pyplot as plt

tabMeteo = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]  


def Menu():
    print(" ------------------------------------- MENU ------------------------------------------- ")
    print("(1) Calcular a Temperatura média de cada dia")
    print("(2) Guardar a tabela meteorológica num ficheiro de texto")
    print("(3) Carregar a tabela meteorológica de um ficheiro de texto")
    print("(4) Calcular a Temperatura mínima mais baixa da tabela")
    print("(5) Calcular a amplitude térmica de cada dia")
    print("(6) Calcular o dia da precipitação máxima")
    print("(7) Calcular o número de dias em que a precipitação é maior que um valor p")
    print("(8) Calcular o maior número de dias consecutivos com precipitação abaixo do limite p")
    print("(9) Desenhar os gráficos da Temperatura mínima, Temperatura máxima e pluviosidade")
    print("(0) Sair")
    print(" -------------------------------------------------------------------------------------- ")



def Calcula_Medias(tabMeteo):
    res = []

    for dia in tabMeteo:   
        Temp_Media = (dia[1] + dia[2]) / 2
        data = dia[0]
        res.append((data, Temp_Media))
    return res


def Guarda_TabMeteo(t, fnome):
    file = open(fnome, "w")

    for data, min, max, prec in t:
        ano, mes, dia = data
        registo = f"{ano}-{mes}-{dia}|{min}|{max}|{prec}\n"
        file.write(registo)
    file.close()
    return


def Carrega_TabMeteo(fnome):
    res = []
    file = open(fnome, "r")

    for line in file:         
        line = line.strip()      
        campos = line.split("|")  
        data, min, max, prec = campos  
        ano, mes, dia = data.split("-") 
        tuplo = ((int(ano), int(mes), int(dia)), float(min), float(max), float(prec))
        res.append(tuplo)
    file.close()
    return res


def Temp_minMin(tabMeteo):
    minimo = tabMeteo[0][1]

    for _ , min, * _ in tabMeteo: 
        if min < minimo:
            minimo = min
    return minimo


def Ampl_Term(tabMeteo):
    res = []
    
    for elem in tabMeteo:
        ampl = (elem[2] - elem[1])
        data = elem[0]
        res.append((data, ampl))
    return res


def Max_Chuva(tabMeteo):
    max_data = None
    max_prec = 0

    for data, Tmin, Tmax, prec in tabMeteo:
        if prec > max_prec:
            max_data = data
            max_prec = prec
    return(max_data, max_prec)


def Dias_Chuv(tabMeteo, p):
    res = []

    for data, min, max, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res


def Max_Periodo_Calor(tabMeteo, p):
    local_consec = 0
    global_consec = 0
    
    for data, min, max, prec in tabMeteo:
        if prec < p:
            local_consec = local_consec + 1
        else:
            if local_consec > global_consec:
                global_consec = local_consec
            local_consec = 0
    
    if local_consec > global_consec:
        global_consec = local_consec
          
    return global_consec


def Graf_TabMeteo(t):
    x = [f"{data[0]}-{data[1]}-{data[2]}" for data, * _ in t]
    y_min = [min for data, min, * _ in t]
    y_max = [max for data, min, max, prec in t]
    y_precs = [prec for data, min, max, prec in t]

    plt.plot(x,y_min, label="Temperatura Mínima (ºC)", color="pink", marker="o")       
    plt.plot(x,y_max, label="Temperatura Máxima (ºC)", color="purple", marker="o")        
    plt.legend()
    plt.grid()
    plt.xticks(rotation = 45)
    plt.show()

    plt.bar(x,y_precs, label = "Precipitação", color="grey")                              
    plt.legend()
    plt.xticks(rotation = 45)
    plt.show()

    return



def Main():
    tabMeteo =[]
    fnome = "meteorologia.txt"
    p = None

    while True:
        Menu()
        opcao = input("Escolha uma das seguintes opções: ")

        if opcao == "1":
            resultado = Calcula_Medias(tabMeteo)
            print(f"Temperatura média de cada dia: {resultado}")

        elif opcao == "2":
            Guarda_TabMeteo(tabMeteo, fnome)
            print(f"Tabela guardada com sucesso em: {fnome}")

        elif opcao == "3":
            tabMeteo = Carrega_TabMeteo(fnome)
            print(f"Tabela carregada: {tabMeteo}")

        elif opcao == "4":
            resultado = Temp_minMin(tabMeteo)
            print(f"Temperatura mínima mais baixa registada: {resultado}")

        elif opcao == "5":
            resultado = Ampl_Term(tabMeteo)
            print(f"Amplitude térmica de cada dia: {resultado}")

        elif opcao == "6":
            resultado = Max_Chuva(tabMeteo)
            print(f"Dia de precipitação máxima: {resultado}")
        
        elif opcao == "7":
            p = float(input("Introduza um valor para o limite p:"))
            resultado = Dias_Chuv(tabMeteo, p)
            print(f"Dias com precipitação maior que {p}: {resultado}")
        
        elif opcao == "8":
            p = float(input("Introduza um valor para o limite p:"))
            resultado = Max_Periodo_Calor(tabMeteo, p)
            print(f"Número máximo de dias consecutivos com precipitação abaixo de {p}: {resultado}")

        elif opcao == "9":
            if tabMeteo:
                Graf_TabMeteo(tabMeteo)
            else:
                print("Insira na tabela os dados necessários para a criação dos gráficos.")
        
        elif opcao == "0":
            print("Até à próxima!")
            return


Main()