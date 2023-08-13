import random
import time
x=int(input(" please enter the number of ladders:"))
y=int(input("please enter the number of snakes:"))
players=int(input("please enter the number of players:"))
ladders=[]
snakes=[]
board=list(range(1,101))
playerposition=list(map(lambda x: 0, range(players)))
print(playerposition)

for index in range(players) :
   playerposition.append(0)


dice=[1,2,3,4,5,6]
flag=False

    #make ladders
for ladder in range(x):
    start=random.randint(1,99)
    for index in range(0, len(ladders),2):
      if start==ladders[index]:
         flag=True
         break
      else: 
         flag=False

    if not flag:
      end=random.randint(start+1,100)
      ladders.append(start)
      ladders.append(end)

print("ladders",ladders)

flag=False
 #make snakes
for snake in range(y):
    start=random.randint(1,99)
    for index in range(0, len(snakes),2):
      if start==snakes[index]:
         flag=True
         break
      else: 
         flag=False

    if not flag:
      end=random.randint(0,start-1)
      snakes.append(start)
      snakes.append(end)

print("snakes",snakes)



   
def simulate_action(wich_player): 
    while True:
      rollingdice=random.choice(dice)
      if playerposition[wich_player]==0 and rollingdice==6:
         playerposition[wich_player]=1
      elif playerposition[wich_player]!=0 :
         if (playerposition[wich_player]+rollingdice)>101:
            print("over value")
         else:
            playerposition[wich_player]+=rollingdice
      
      print(f"player {wich_player} dice number:",rollingdice,"     place:",playerposition[wich_player])
      for index in range (0,len(ladders),2):
         if playerposition[wich_player]==ladders[index]:
            playerposition[wich_player]=ladders[index+1]
            print("use laders")
      for index in range (0,len(snakes),2):
         if playerposition[wich_player]==snakes[index]:
            playerposition[wich_player]=snakes[index-1]
            print("dump by snake")
            print(wich_player)
      if playerposition[wich_player]>=100:
         print(f"player {wich_player} win ;)")
         exit()
         
      if rollingdice!=6:
         break
      print("prize")
 

while True:
   
   for player in range (0,players):
      simulate_action(player)
      time.sleep(3)
   
