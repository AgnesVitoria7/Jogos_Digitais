import random

class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive=True
        self.ammo=5
        self.armor=60

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

number_tanks = int(input("Quantos tanques deseja criar no jogo? [Min 2, Max 10] "))
while number_tanks < 2 or number_tanks > 10:
    print("Respeite os limites de quantidades mínima e máxima ")
    number_tanks = int(input("Quantos tanques deseja criar no jogo? [Min 2, Max 10] "))


letras = ['a','b','c','d','e','f','g','h','i','j']
custom_tanks = {}

for i in range(number_tanks):
    tank_name = input("Digite o nome do tanque que deseja criar ")
    custom_tanks[letras[0]] = Tank(tank_name)
    del letras[0]


jogadores = []
for tanque in custom_tanks:
    jogadores.append(tanque)


empate = False

while len(custom_tanks) > 1:

    attacker_index = random.randint(0, len(custom_tanks)-1)

    alvos_disponiveis = []
    print("Atacante da rodada: ", custom_tanks[jogadores[attacker_index]].name)
    print("Lista de alvos disponíveis: ")
    for x, y in custom_tanks.items():
        if custom_tanks[jogadores[attacker_index]].name not in y.name:
            print(x, y.name)
            alvos_disponiveis.append(x)

    target_index = input("Selecione a letra correspondente a quem você deseja atingir ")
    while target_index not in alvos_disponiveis:
        target_index = input("Selecione um alvo válido para atingi-lo ")

    custom_tanks[jogadores[attacker_index]].fire_at(custom_tanks[target_index])
    print("Blindagem restante de ", custom_tanks[target_index].name, end = " ")
    print(": ", custom_tanks[target_index].armor)

    if custom_tanks[target_index].alive == False:
        del custom_tanks[target_index]
        if target_index in jogadores:
            jogadores.remove(target_index)

    print('------------ Status geral ------------')
    for item in custom_tanks:
        print("-----------------------------------")
        print("Jogador :", custom_tanks[item].name)
        print("Situação da blindagem :", custom_tanks[item].armor)
        print("Quantidade de munições :", custom_tanks[item].ammo)
        print("-----------------------------------")



if empate:
      print("Empate. Os remanescentes ficaram sem munição")
else:
    print("Vencedor da guerra de tanques: ")
    for tanque in custom_tanks:
          print(custom_tanks[tanque])