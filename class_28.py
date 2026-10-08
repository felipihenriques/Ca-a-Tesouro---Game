print("""

  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88  

""")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Bem-vindo  à ilha do Tesouro.\nA sua missão é encontrar o tesouro.")
pergunta_1 = int(input("[1] - Esquerda\n[2] - Direita\nQual a sua escolha? "))

if pergunta_1 == 1:
    print("Você passou da fase [1]!")

    pergunta_2 = int(input("[1] - Nadar\n[2] - Esperar\nQual você escolhe? "))

    if pergunta_2 == 2:
        print('Você passou da fase [2]\n')

        pergunta_3 = int(input("Qual a porta?\n[1] - Vermelho\n[2] - Azul\n[3] - Amarela\nQual a sua escolha? "))

        if pergunta_3 == 1:
            print("Queimado pelo fogo. Fim de jogo!")
        elif pergunta_3 == 2:
            print("Devorado por feras. Fim de jogo!")
        elif pergunta_3 == 3:
            print("Você venceu!")
        else: 
            print("Fim de jogo.")

    elif pergunta_2 == 1:
        print("Atacado por uma truta. Fim de jogo!")    

elif pergunta_1 == 2:
    print("Você caiu em um buraco. Fim de jogo!")

else:
    print("Você escolheu um número que não consta no formulário. Tente novamente! ")