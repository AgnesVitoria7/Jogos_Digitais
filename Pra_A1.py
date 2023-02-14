import random
class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive= True
        self.ammo= 5
        self.armor= 60

    def __str__(self):
        if self.alive:
            return "%s (%i armor, %i shells)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (DEADE)" % self.name

    def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

tanque1 = Tank("Tank1")
tanque2 = Tank("Tank2")
tanque3 = Tank("Tank3")
tanque4 = Tank("Tank4")
tanque5 = Tank("Tank5")

#Ex1
array = [tanque1, tanque2, tanque3, tanque4, tanque5]

#Ex2
while(len(array)!=1):
    num = random.randint(0,len(array)-1)
    num2 = random.randint(0,len(array)-1)
    while num2 == num:
        num2 = random.randint(0,len(array)-1)

    array[num].fire_at(array[num2])
    if(array[num2].alive != True):
        array.remove(array[num2])

print("\nO tanque", array[0].name, "venceu")

#Ex3
tankQtde = int(input("Digite o numero de tanques para o jogo (min 2 max 10): "))
while tankQtde < 2 or tankQtde > 10:
    tankQtde = int(input("Numero invalido, digite novamente: "))

tankList = {}


alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))


keyList = []
for a in range(1, tankQtde + 1):
    nome = input("Digite o nome do tanque: ")
    tank = Tank(nome)
    key = alphabet[a-1]
    tankList[key] = tank
    keyList.append(key)

while len(tankList) > 1:
    random.shuffle(keyList) 
    shooter = tankList[keyList[1]] 
    print("\nVez do", shooter.name)
    target = input("\nDigite a chave do tanque que deseja atacar: ")
    while target not in keyList or target == keyList[1]:
        target = input("Chave inválida, digite novamente: ")
        
    enemy = tankList[target]
    shooter.fire_at(enemy)
    if enemy.alive == False:
        del tankList[target]
        keyList.remove(target)
        
    keyList.sort() 
    for a in keyList:
        tank = tankList[a]
        print("O tanque do", tank.name, "possui", tank.ammo, "de munição e", tank.armor, "de armadura")
        winner = tank

print("\nO vencedor é", winner.name)
