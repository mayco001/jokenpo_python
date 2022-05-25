import random
import time

computador = random.randint(1,3)

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO")
time.sleep(1)
print("----------------------------")
print("----------🤘JOKENPO🤘----------")
print("1.Rock👊 | 2.Paper✋ | 3.Scissors✌")
jogador = int(input("Enter the desired option: "))
time.sleep(0.1)
print("Loader...")
time.sleep(1)
print("----------------------------")

#player logic
if jogador == 1:
    print("Player chose rock👊")
    print("----------------------------")
elif jogador == 2:  
    print("Player chose paper✋")  
    print("----------------------------")
elif jogador == 3:
    print("Player chose scissors✌")
    print("----------------------------")
else:
    print("❌Error❌")    
    print("----------------------------")


#computer logic
if computador == 1:
    print("Computer chose rock👊")
    print("----------------------------")
elif computador == 2:  
    print("Computer chose paper✋")  
    print("----------------------------")
elif computador == 3:
    print("Computer chose Scissors✌")   
    print("----------------------------")

#logic to determine the winner
if computador == jogador:
    print("tie in this game!!😭")
elif jogador == 1 and computador == 3 or jogador == 2 and computador == 1 or jogador == 3 and computador == 2:
    print("Player Won!!😄")
else:
    print("Computer Won!!🤖")    