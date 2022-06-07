from datetime import datetime
import os

ping = str
lan = str
uni = str

#!/usr/bin/python3

# lista com as pessoas, vazia por enquanto.
pessoas = []
for o in range(10):
    pergunta = int(input("\n1-Novo equipamento\n2-Registos\n:"))
    if pergunta == 1:

        # coloquei apenas 1 para não ficar cansativo mas pode ser qualquer valor.
        #Vai fazer perguntas e guardar na variavel temprariamente
        for i in range(1):
            name = input("\nNome do cliente: ")
            sn = input('SN: ')
            qrrouter = input('Router QR: ')
            mac = input('MAC: ')
            estado = input('O equipamento está em condições(sim/não): ')
            formatar = input('Formatou o equipamento(sim/não): ') 

        # cria um dicionário com o que foi entrado e adiciona à lista.
        pessoas.append({'Cliente': name, 'SN': sn, 'Router QR': qrrouter, 'MAC': mac, 'Dual band':ping, 'Lan:':lan,'Unidade liga:':uni,'Unidade formatada:':formatar  })
        print("\n")
        #Guardar no ficheiro de texto dados.txt
        arquivo = open('dados.txt','a')
        arquivo.write("Cliente: "+name + "\n")
        arquivo.write("Sn: "+sn + "\n")
        arquivo.write("Router: "+qrrouter + "\n")
        arquivo.write("Mac: "+mac + "\n")
        arquivo.write("Equipamento estado em condiçôes: "+estado + "\n")
        arquivo.write("Formatou o equipamento: "+formatar + "\n")
        #Buscar data e hora do exato momento
        now = datetime.now()


        #encontrar ip
        externalIP  = os.popen('curl -s ifconfig.me').readline()

        #Fazer ping internet
        print(externalIP)
        ping_connection = os.popen(f"ping {externalIP}").read()
        print(ping_connection)

        #caso funcione exibe
        if "Received = 4" in ping_connection:
            print(f" {externalIP} Teste Dual band sucesso")
            ping = "Funcional"
            print(ping)
            lan = "Funcional"
            uni="Sim"
            arquivo.write("Dual band: "+ping + "\n")
            arquivo.write("Unidade liga: "+uni + "\n")
           

        #caso não funcione exibe
        else:
            print(f"{externalIP} Teste Dual band sem sucesso")
            ping = "Não funciona"
            lan = "Não funcional"
            uni="Não"

            arquivo.write("Dual band: "+ping + "\n")
            arquivo.write("Unidade liga: "+uni + "\n")

        

        #Pergunta para dar tempo para ligar cabo
        #input usado somente para dar o momento de pausa para ligar o cabo
        Lan = input('Conecte o cabo antes de fazer o teste lan e pressione enter:\n')

        print(externalIP)
        ping_connection = os.popen(f"ping {externalIP}").read()
        print(ping_connection)

        #caso funcione
        if "Received = 4" in ping_connection:
            print(f" {externalIP} Teste Dual band sucesso")
            ping = "Funcional"
            print(ping)
            lan = "Funcional"
            
            arquivo.write("Lan: "+lan + "\n")

        #caso não funcione
        else:
            print(f"{externalIP} Teste Dual band sem sucesso")
            
            lan = "Não funcional"

            arquivo.write("Dual band: "+ping + "\n")
            arquivo.write("Lan: "+lan + "\n")
        date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
        arquivo.write(date_time + "\n")
        arquivo.write("----------------\n")
        print("Operação concluída no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
        arquivo.close()

        
        

    #Caso escolha 2 na primeira pergunta vai exibir os dados do ficheiro dados.txt
    elif pergunta == 2:
      with open('dados.txt') as f:
            contents = f.read()
            print(contents)

    else:
        print("valor incorreto")

#C:\Users\hfauser é onde e guardado