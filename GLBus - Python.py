rotas = {1:'Alagoas',2:'Bonito/MG',3:'Brasília',4:'Goiânia',5:'Montes Claros',6:'Porto Seguro',7:'Rio de Janeiro',8:'Salvador',9:'Tocantins'}
dist = [1436,51,511,708,170,873,1050,1035,1070]
tempo = [23,1,12,13,3,14,15,16,18]
#PREÇO -> Considerando o Diesel R$ 4,50/L e o ônibus realizando 5km/L ... Ex: 100Km, gastaria 20L, equivalente a 90$
preco = [260,10,92,128,31,157,189,187,193]
vagasDisp = [40,40,40,40,40,40,40,40,40]

##vagasOcup = ['O']*40
##vagasOcup = {1: 'O'*40,2: 'O'*40,3: 'O'*40,4: 'O'*40,5: 'O'*40,6: 'O'*40,7: 'O'*40,8: 'O'*40,9: 'O'*40}
##print(vagasOcup) 

##def getVagas():
##    consultaTodasRotas()
##    optConsulta = int(input("Insira o nº de uma Rota para exibir o mapa de Vagas:\n"))
##    for optConsulta in range(0,len(vagasOcup[optConsulta])//2):
##        print(vagasOcup[optConsulta], end=' ')
##    print()
##    for optConsulta in range(len(vagasOcup[optConsulta])//2,len(vagasOcup[optConsulta])):
##        print(vagasOcup[optConsulta], end=' ')
##    print("\n")

listaCliente = []
total = 0

def setCliente():
    print("Seja bem vindo(a)! Por favor, insira seus dados...\n")
    nome = input("Nome: ").lower()
    ok = False
    while ok == False:
        numID = (input("Nº de Identificação (ID) (Maior que 0): "))
        try:
            numID = int(numID)
            if numID <=0:
                print("ATENÇÃO! Favor inserir um Nº Maior que 0!!\n")
            else:
                ok = True
                for elemento in listaCliente:
                    if elemento[0] == numID:
                        print("ATENÇÃO! ID já existente! Favor escolher outro!")
                        ok = False
                        break
        except:
            print("Favor inserir um Número inteiro!")
    if ok == True:
        listaCliente.append([numID,nome])
        print("Cadastro realizado com sucesso!\n")
    
def getCliente():
    ok = False
    while ok == False:
        numID = (input("Insira o seu nº ID de Cadastro ou 0 para Cadastrar: "))
        try:
            numID = int(numID)
            if numID <0:
                print("ATENÇÃO! Favor inserir um Nº Maior que 0!!\n")
            elif numID == 0:
                ok = True
                setCliente()
            elif numID !=0:
                if numID in listaCliente[0]:
                    ok = True
            else:
                print("ID %d não encontrado!\n"% numID)
        except:
            print("ID %d não encontrado!\n"% numID)

def getVendas(vagasDisp,total):
    print("Exibindo Lucro e Vagas Disponíveis de todas as rotas:\n")
    for i in rotas:
        print(rotas[i],"\tVendas - R$",preco[i-1]*(40-vagasDisp[i-1]),",00 \tPassagens Vendidas - ",40-vagasDisp[i-1],"\tVagas - ",vagasDisp[i-1])
        total += preco[i-1]*(40-vagasDisp[i-1])
    print("\nTOTAL: R$",total,",00\n")
    
def getVagas():
    consultaTodasRotas()
    valida = False
    while valida == False:
        optConsulta = input("Insira o nº de uma Rota para exibir o nº de Vagas:\n")
        try:
            optConsulta = int(optConsulta)
            if optConsulta <=0 or optConsulta > len(rotas):
                print("ATENÇÃO! Favor inserir uma opção válida! ( 1 ~",len(rotas),")")
            else:
                valida = True
                if vagasDisp[optConsulta-1] != 0:
                    print("Vagas Disponíveis: ",vagasDisp[optConsulta-1],"\n")
                else:
                    print("NÃO há mais vagas para este ônibus!!")
        except:
            print('Opção DEVE ser um número!!')
            
    
def consultaTodasRotas():
    for i in rotas:
        print(i,'-',rotas[i])

def consultaRotaEspecifica():
    consultaTodasRotas()
    valida = False
    while valida == False:
        print("\n")
        optRotas = input("Insira o nº de uma Rota para exibir maiores informações:\n")
        try:
            optRotas = int(optRotas)
            if optRotas <=0 or optRotas > len(rotas):
                print("ATENÇÃO! Favor inserir uma opção válida! ( 1 ~",len(rotas),")")
            else:
                valida = True
                print("Exibindo informações da Rota para %s:\n" % (rotas[optRotas]) ) 
                print("Distância (Km): ",dist[optRotas-1],"\n") #Considerando que o índice começa do 0 , mas será exibido ao usuário a partir do 1 (logo, optRotas-1)
                print("Tempo (Horas): ",tempo[optRotas-1],"\n")
                print("Preço (R$): ",preco[optRotas-1],',00\n')
                print("Vagas Disponíveis: ",vagasDisp[optRotas-1],"\n")
        except:
            print('Opção DEVE ser um número!!')
            
def comprarPassagem(vagasDisp):
    consultaTodasRotas()
    repetir = 's'
    getCliente()
    while repetir == 's':
        optCompra = input("Insira o nº de uma Rota para realizar a compra (0 para Encerrar): \n")
        try:
            optCompra = int(optCompra)
            if optCompra == 0:
                print("Voltando ao menu inicial...\n")
                break
            elif optCompra < 0 or optCompra > 9:
                print("ATENÇÃO! Favor inserir uma opção válida! (0 ~ %d)\n"% len(rotas))
            
            elif vagasDisp[optCompra-1] == 0:
                print("ATENÇÃO!! Não há mais vagas para este ônibus!!\n")
            else:     
                quantCompra = int(input("Deseja comprar quantas passagens? (%d Disponíveis) \n" % vagasDisp[optCompra-1]))
                if quantCompra <1:
                    print("ATENÇÃO!! Favor inserir uma quantidade válida!!\n")
                elif quantCompra > vagasDisp[optCompra-1]:
                    print("ATENÇÃO!! NÃO foi possível concluir a compra. O ônibus possui somente ",vagasDisp[optCompra-1]," vagas disponíveis!\n")
                else:
                    confirma = input("Valor: R$%d,00. Deseja confirmar?(S/N): \n"% (quantCompra*(preco[optCompra-1]))).lower()
                    if confirma == 's':
                        vagasDisp[optCompra-1]-= quantCompra
                        repetir = input("Passagens reservadas com sucesso! Deseja continuar comprando? (S/N): \n").lower()
                    else:
                        print("Compra NÃO confirmada!\n")
        except:
            print('Opção DEVE ser um número!!')

def menu():
    opt = -1
    while opt!=0:
        print("=============================================================")
        print("-------------------SISTEMA GLBus v1.0------------------------")
        opt = input("|Escolha uma opção:\n|1- Consultar Todas as Rotas\n|2- Consultar Rota Específica\n|3- Consultar Vagas em um Ônibus\n|4- Comprar Passagem\n|5- Relatório de Vendas\n|6- Cadastrar Cliente\n|0- ENCERRAR: ")
        print("=============================================================")
        try:
            opt = int(opt)
            if opt <0 or opt>6:
                print("ATENÇÃO! Favor inserir uma opção válida! (0~6)")
            elif opt == 1:
                consultaTodasRotas()
            elif opt == 2:
                consultaRotaEspecifica()
            elif opt == 3:
                getVagas()
            elif opt == 4:
                comprarPassagem(vagasDisp)
            elif opt == 5:
                getVendas(vagasDisp,total)
            elif opt == 6:
                setCliente()
            elif opt == 0:
                print("Encerrando...")
                break
        except:
            print("Opção DEVE ser um número!!")

if __name__ == '__main__':
    menu()
