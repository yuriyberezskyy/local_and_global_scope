################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope

# def drink_potion():
#   potion_strength = 2
#   print(potion_strength)

# drink_potion()

# Global scobe

player_health = 10

def healthy_drink():
  print(player_health)

def game():
  def drink_potion():
    portion_food = 2
    print(portion_food)
  return(drink_potion())

game()

#Modifying global scope

enemies = 1

# def increase_enemies():
#   global enemies  
#   enemies+=1
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside the function {enemies}")
