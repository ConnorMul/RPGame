from classes.game import Person
from classes.magic import Spell
from classes.inventory import Item

# CREATE BLACK MAGIC
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 124, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 15, 200, "black")
quake = Spell("Earthquake", 15, 150, "black")

# CREATE WHITE MAGIC
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")


# CREATE SOME ITEMS
potion = Item("Potion", "Potion", "Heals 50 HP", 50)
high_potion = Item("High Potion", "Potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "Potion", "Heals 500 HP", 500)
exilir = Item("Elixir", "Elixir", "Fully restores MP/HP of one party member", 9999)
mega_elixir = Item("Mega Elixir", "Elixir", "Fully restores MP/Hp of all party members", 9999)

grenade = Item("Grenade", "Attack", "Deals 500 Damage", 500)

player_magic = [fire, thunder, blizzard, quake, meteor, cure, cura]
player_items = [super_potion, grenade]

# INSTANTIATE PEOPLE
player = Person(460, 65, 60, 34, player_magic, player_items)
enemy = Person(1200, 65, 45, 25, [fire, thunder, blizzard, quake, meteor, cure, cura], [])

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
        
        if magic_choice == -1:
            continue
        
        cost = player.get_spell_mp_cost(magic_choice)
        
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_dmg()
        
        current_mp = player.get_mp()
        
        if spell.cost > current_mp:
            print("You do not have enough MP to cast this spell!")
            continue
        
        player.reduce_mp(cost)
        
        if spell.type == "white":
            player.heal(magic_dmg)
            print(spell.name + " heals for " + str(magic_dmg) + "HP.")
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(spell.name + " caused " + str(magic_dmg) + " points of damage.")
        
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose Item: ")) - 1
        
        if item_choice == -1:
            continue
        
        item = player.items[item_choice]
        
        if item.type == "Potion":
            player.heal(item.prop)
            print("\n" + "You were healed by potion for " + str(item.prop) + "HP.")
            
    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for " + str(enemy_dmg) + " points of damage.")
    print("================")
    print("Enemy HP: " + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()))
    print("================")
    print("Your HP: " + str(player.get_hp()) + "/" + str(player.get_max_hp()))
    print("Your MP: " + str(player.get_mp()) + "/" + str(player.get_max_mp()))
    
    if enemy.get_hp() == 0:
        print("You Win!")
        running = False
    elif player.get_hp() == 0:
        print("Your enemy has defeated you...")
        running = False