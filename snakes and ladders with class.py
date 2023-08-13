import random
import time
class game:
   ladders=[]
   snakes=[]
   flag=False   
   finishgame=False
   dice=[1,2,3,4,5,6]
   board=list(range(1,101))

   def __init__(self,gamename):
    self.x=2
    self.y=2
    self.players=2
    print(f"game for {self.players} players is preparing.please wait some seconds.")
    print("game started.roll the dice")
    self.playerposition=list(map(lambda x: 0, range(self.players)))
    self.gamename=gamename
    self.laddersofthegame()
    self.sanakesofthegame()
    
    

      #make ladders

   def laddersofthegame(self):
    for _ in range(self.x):
      start=random.randint(1,99)
      for index in range(0, len(self.ladders),2):
         if start==self.ladders[index]:
            self.flag=True
            break
         else: 
            self.flag=False

      if not self.flag:
         end=random.randint(start+1,100)
         self.ladders.append(start)
         self.ladders.append(end)
      
   #make snakes
   
   def sanakesofthegame(self):
    for _ in range(self.y):
      start=random.randint(1,99)
      for index in range(0, len(self.snakes),2):
         if start==self.snakes[index]:
            self.flag=True
            break
         else: 
            self.flag=False

      if not self.flag:
         end=random.randint(0,start-1)
         self.snakes.append(start)
         self.snakes.append(end)
      
   def simulate_action(self,wich_player):
    if  self.finishgame==False: 
      while True:
         rollingdice=random.choice(self.dice)
         if self.playerposition[wich_player]==0 and rollingdice==6:
            self.playerposition[wich_player]=1
         elif self.playerposition[wich_player]!=0 :
            if (self.playerposition[wich_player]+rollingdice)>100:
               print("over value")
            else:
               self.playerposition[wich_player]+=rollingdice
         
         print(f"{self.gamename} player {wich_player} dice number:",rollingdice,"     place:",self.playerposition[wich_player])
         for index in range (0,len(self.ladders),2):
            if self.playerposition[wich_player]==self.ladders[index]:
               self.playerposition[wich_player]=self.ladders[index+1]
               higherspot=self.ladders[index+1]
               print(f"use ladders and go from your current spot to {higherspot}")
         for index in range (0,len(self.snakes),2):
            if self.playerposition[wich_player]==self.snakes[index]:
               self.playerposition[wich_player]=self.snakes[index-1]
               lowerspot=self.snakes[index+1]
               print(f"you dumped by snake and have to go to {lowerspot}")
               print(wich_player)
         if self.playerposition[wich_player]==100:
            print(f"player {self.gamename} {wich_player} win ;)")
            self.finishgame=True
            
         if rollingdice!=6:
            break
         print("prize")
   


table=game('game between of kimia and ali!')
table2=game('game between of behrooz and majid!')
table3=game('game between of a and b!')
table4=game('game between of c and d!')



while True:
      for player in range (0,table.players):
         table.simulate_action(player)
         table2.simulate_action(player)
         table3.simulate_action(player)
         table4.simulate_action(player)
         if table.finishgame and table2.finishgame and table3.finishgame and table4.finishgame==True:
            exit()
         time.sleep(.5)
         
 
