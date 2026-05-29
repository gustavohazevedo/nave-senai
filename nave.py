##Definir as variaveis
combustivel = 100
tripulantes = []

##Definir funções

def viajar():
    ##Aqui vamos gastar o combustivel
    global combustivel ##Avisa a função que vamos modificar um variavel externa
    if(combustivel> 30):
        combustivel = combustivel - 30
        print("A nave viajou")
    else:
        print("Você está sem combustivel suficiente. Abasteça!")

def abastecer():
    global combustivel
    combustivel = 100
    print("Tanque cheio! ⛽")

def status_nave():
    ##Mostre a quantidade de combustivel e os tripulantes
    print("----------STATUS NAVE----------")
    print(f"Temos{combustivel} de combustivel")
    print(f"Os tripulantes são: {tripulantes} ")
    print("-----------------------------\n")


def registrar_tripulante():
    ##Essa função pergunta o nome do tripulante e adiciona na lista de tripulantes
    novo_Tripulante = input("Qual nome do tripulante?") ##pergunta quem
    tripulantes.append(novo_Tripulante) ##Inserimos o fulaninho
    print("Tripulante inserido com sucesso!🧑‍🚀🚀")


## Criar um menu

while True:
   print("Bem vindo ao menu interativo da nave. Por favor selecione uma opção:")
   print("\n1- Mostrar status da nave | 2- Viajar | 3- Abastecer | 05- Sair")
   opcao = input("Escolher: ")
  
   if(opcao == "1"):
       status_nave()
   elif(opcao == "2"):
       viajar()
   elif(opcao =="3"):
       abastecer()
   elif(opcao =="4"):
       registrar_tripulante()
   elif(opcao =="5"):
    print("Viagem encerrada")
    break


    


       



# status_nave()
# viajar()
# viajar()
# status_nave()
# viajar()
# viajar()
# abastecer()
# viajar()
# status_nave()
        

