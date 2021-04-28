from classes.game import Person, bColors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
        {"name": "Thunder", "cost": 10, "dmg": 80},
        {"name": "Blizzard", "cost": 10, "dmg": 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print("AN ENEMY ATTACKS!")

while running:
    print("================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1
    
    # print("You chose " + player.get_spell_name(int(choice)))
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for " + str(dmg) + "Points of damage. Enemy HP: " + str(enemy.get_hp()))
    
    # running = False