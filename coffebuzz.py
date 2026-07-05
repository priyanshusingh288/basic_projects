class Coffee:

    def __init__(self,water,name,instructions,time,amount):
        self.name = name
        self.water = water
        self.instructions = instructions
        self.time = time
        self.amount = amount
        

    def show_recipe(self):
     print(f"\n recipe for:{self.name}")
     print(f"\n water needed for {self.name} is about:{self.water}")
     print(f"\n amount of coffee required for recipe:{self.amount}")
     print(f"\n follow up these steps \n{self.instructions}")
     print(f"\n time -*30")
    

espresso = Coffee(
    name="Espresso", 
    water="30ml", 
    time="25-30 seconds", 
    amount="18g", 
    instructions="Finely grind the coffee, tamp it, and force hot water through it."
)

latte = Coffee(
    name="Latte", 
    water="30ml (for the espresso base)", 
    time="3 minutes", 
    amount="18g", 
    instructions="Brew a shot of espresso, steam your milk, and pour the milk over the espresso."
)

americano = Coffee(
    name="Americano",
    water="200ml",
    time="2 minutes",
    amount="18g",
    instructions="Brew an espresso shot and dilute it with hot water."
)

coffee_types={
   "1":espresso,
   "2":latte,
   "3":americano
}

print("----------welcome to coffbuzz!!------------")
print("please choose your coffe from 1:2:3")
choice = input("")
if choice in coffee_types:
   selected_coffe = coffee_types[choice]
   selected_coffe.show_recipe()
else:
   print("no this coffe recipe is not available!!")