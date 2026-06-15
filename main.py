
'''Desenvolva um sistema em Python para controlar pedidos de uma lanchonete. O
programa deverá apresentar um menu de opções para que o usuário possa
visualizar o cardápio, adicionar itens ao pedido, remover itens, consultar o pedido
atual e finalizar a compra.
O sistema deve possuir um cardápio com pelo menos 5 itens, contendo nome e
preço. O usuário poderá escolher os produtos desejados e adicioná-los a uma lista
de pedido. Também deverá ser possível remover itens dessa lista antes de finalizar
a compra.
Ao finalizar o pedido, o sistema deverá exibir todos os itens escolhidos e calcular o
valor total da compra.
Requisitos técnicos obrigatórios
O projeto deve conter:
● Estrutura de decisão/condição, como if, elif e else.
● Laço de repetição, como while ou for.
● Lista, obrigatoriamente manipulada durante o sistema.

Funcionalidades mínimas
● Exibir menu principal.
● Exibir cardápio.
● Adicionar item ao pedido.
● Remover item do pedido.
● Listar itens do pedido.
● Calcular e mostrar o valor total.
● Encerrar o sistema.'''

pedidos = []
cardapio = ["Coxinha", "Pastel", "Kibe", "Empadão", "Refrigerante", "Suco Natural"]
precos = [3.50, 9.00, 5.00, 8.00, 9.50, 8.50]

def removePedido(remItem):
    remItem -= 1
    pedidos.pop(remItem)


def calcularTotal():
    total = 0.0
    for itemPedido in pedidos:
        
        for i in range(len(cardapio)):
            if cardapio[i] in itemPedido:
                total += precos[i]
                break
    return total

def pedido():
    while True:
        item = input("(TECLE ENTER PARA FINALIZAR O PEDIDO) \n\nInforme o número do item desejado:  ")
        
        if item == "":
            break
        
        item = int(item) - 1
        prod = cardapio[item]
        
        precoProd = round(precos[item], 2)
        
        itemStr = str(prod) + "  R$" + str(precoProd).replace(".", ",")
        pedidos.append(itemStr)
        
        print("\n=====PEDIDOS=====")
        contador = 1
        for i in pedidos:
            print(f"{contador}.  {i}")
            contador += 1
                
        print("="*50)
        
        print(f"TOTAL:   R$ {calcularTotal():.2f}".replace(".", ","))
        print("\n")
    
def menu(): 
    while True:
        print("="*30)
        print("======MENU PRINCIPAL======")
        print("\n")
        print("1.  CARDÁPIO")
        print("2.  CADASTRAR PEDIDO")
        print("3.  VER PEDIDOS")
        print("4.  REMOVER PEDIDO")
        print("\nTECLE ENTER PARA FINALIZAR")
        print("="*30)
        print("\n")
        teste = input("Informe a opção desejada:  ")

        if teste == "1":
            cardapios(cardapio, precos)
            
        elif teste == "2":
            cardapios(cardapio, precos)
            pedido()
            
        elif teste == "3":
            print("\n=====LISTA DE PEDIDOS=====")
            if not pedidos:
                print("Nenhum pedido cadastrado ainda.")
            else:
                contador = 1
                for i in pedidos:
                    print(f"{contador}.  {i}")
                    contador += 1
                print("="*30)
                
                print(f"TOTAL DO PEDIDO: R$ {calcularTotal():.2f}".replace(".", ","))
            print("\n")
                
        elif teste == "4":
            if not pedidos:
                print("\nNão há pedidos para remover.")
                continue
                
            contador = 1
            for i in pedidos:
                print(f"{contador}.  {i}")
                contador += 1
            
            item = int(input("\nInforme o número do item à ser excluído: "))
            removePedido(item)

        elif teste == "":
            
            print("\nObrigado! Espere seu pedido ser finalizado!")
            break
        
def cardapios (listaCardapio, listaPrecos):
    print("==========CARDÁPIO==========")
    larguraColuna = 25
    for i in range(len(listaCardapio)):
        item = listaCardapio[i]
        preco = listaPrecos[i]
        numItem = f"{i + 1}. "
        
        precoForm = f" R$ {preco:.2f}"
        espacoG = len(numItem) + len(item) + len(precoForm)
        pontos = larguraColuna - espacoG

        if pontos < 2:
            pontos = 2

        ponto = "." * pontos
        print(f"{numItem} {item} {ponto} {precoForm}")

menu()












         
      


        


    










    
    
    

