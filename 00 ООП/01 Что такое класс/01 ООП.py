class Hockey_Player:

    def __init__(self,name,surname,age,team):
        self.name = name
        self.surname = surname
        self.age = age
        self.team = team

    def getFullNAME(self):
        return  self.name , self.surname

player1 = Hockey_Player('Никита','Чудновский',22,17)
print(Hockey_Player.getFullNAME("Никита",'sdas'))
