from classes.game import Person, bColors

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
        {"name": "Thunder", "cost": 10, "dmg": 124},
        {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print("AN ENEMY ATTACKS!")

while running:
    print("================")
    player.choose_action()
    choice = input("Choose Action: ")
    index = int(choice) - 1 
    
    print("================")
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for " + str(dmg) + " points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose Magic: ")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)
        
        current_mp = player.get_mp()
        
        if cost > current_mp:
            print("You do not have enough MP to cast this spell!")
            continue
        
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print("Your spell caused " + str(magic_dmg) + " points of damage.")
        
        
    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for " + str(enemy_dmg) + " points of damage.")
    print("================")
    print("Enemys HP: " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()))
    print("================")
    print("Your HP: " + str(player.get_hp()) + "/" + str(player.get_max_hp()))
    print("Your MP: " + str(player.get_mp()) + "/" + str(player.get_max_mp()))
    
    if enemy.get_hp() == 0:
        print("You Win!")
        running = False
    elif player.get_hp() == 0:
        print("Your enemy has defeated you...")
        running = False