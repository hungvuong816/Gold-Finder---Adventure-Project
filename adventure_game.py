import random
from random import randrange
class Game:
    def __init__(self,hero_health,monster_health):
        self.hero_health = hero_health
        self.monster_health = monster_health
        self.get_gold = 0
        self.total_gold = 0 
        
    def getGold(self):
        self.get_gold = randrange(1,100)
        self.total_gold = self.total_gold + self.get_gold
        return self.get_gold
    
    def updateGold(self):
        return self.total_gold
        
    def heroAttack(self):
        self.hero_damage = randrange(5,30,5)
        self.monster_health = self.monster_health - self.hero_damage
        return self.hero_damage
    
    def monsterAttack(self):
        self.monster_damage = randrange(5,30,5)
        self.hero_health = self.hero_health - self.monster_damage
        return self.monster_damage
        
    def updateHeroHealth(self):
        return self.hero_health
    
    def updateMonsterHealth(self):
        return self.monster_health
    
    def __repr__(self):
        return "You reached the treasure chest!\nAn inside you found... spiders that spin a web to hold you in the hallway for all eternity\nEnding Health:{}\nEnding Gold: {}".format(self.hero_health,self.total_gold)
           

def main():
    steps = 10
    game = Game(50,30)
    herohealth = game.updateHeroHealth()
    monsterhealth = game.updateMonsterHealth()
    print("You are in a dark hallway and see a treasure chest just 10 steps in front of you".format(steps))
    for step in range(steps):
         if herohealth <= 0 or steps < 0:
                break
         inputs = input("Only {} steps left. Step forward (y/n)? ".format(steps))
         if inputs == "y":
            options = random.choice(["Gold","Battle"])
            steps = steps - 1 
            if options == "Gold":
                getgold = game.getGold()
                updategold = game.updateGold()
                print("You found {0} gold pieces! Now you have {1} gold pieces\n".format(getgold,updategold))
            else:
                if monsterhealth > 0:
                    battles = random.choice(["heroAttack","monsterAttack"])
                    if battles == "heroAttack":
                        heroattack = game.heroAttack()
                        monsterhealth = game.updateMonsterHealth()
                        if monsterhealth <= 0:
                            print("Monster has {} points left. Congratulation. You killed the Monster".format(monsterhealth))
                        else:
                            print("Attacking Zombie ! Monster loses {0} health points. {1} health points left\n".format(heroattack,monsterhealth))
                    else:
                        monsterattack = game.monsterAttack()
                        herohealth = game.updateHeroHealth()
                        print("It's a Zombie! He'll kill your political aspirations and then shoot you in the back! \n You lost {0} health points. {1} health points left\n".format( monsterattack,herohealth)) 
                else:
                    getgold = game.getGold()
                    updategold = game.updateGold()
                    print("You found {0} gold pieces! Now you have {1} gold pieces\n".format(getgold,updategold))
    if herohealth <= 0:
        print("You have no health points left. Game Over")
    else:
        print(game)
main()