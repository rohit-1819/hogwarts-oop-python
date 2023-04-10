import hogwarts_magic
# from hogwarts_magic import *
# from hogwarts_magic import Wizard, House, Wand

# creating an object named harry
harry = hogwarts_magic.Wizard("Harry Potter", "Stag", 1980)

# creating an object named hermoine
hermoine = hogwarts_magic.Wizard("Hermoine Granger", "Otter", 1979)

# import pdb
# pdb.set_trace()

# creating an object named gryffindor of House Class
gryffindor = hogwarts_magic.House("Gryffindor", "Godric Gryffindor", "Red and Gold", "Lion")

# testing for gryffindor
print(gryffindor.house_name)
gryffindor.get_house_details()
print("Checking members of the house...")
print(gryffindor.house_members)
print("Adding member to the house")
gryffindor.add_member(harry.wizard_name)
print("Checking members of the house...")
print(gryffindor.house_members)
harry.assign_house(gryffindor)
# printing harry house - None
print('*'*20)
print(harry.wizard_house.house_name)
print(harry.wizard_house.house_animal)

#printing house members
print(gryffindor.house_members)

# Create an oject named wand1
wand1 = hogwarts_magic.Wand("holly", "pheonix feather", "11 inches")

# Create an object named wand2
wand2 = hogwarts_magic.Wand("vine wood", "dragon heartstring", "15 inches")

# testing for harry
print("Wizard's Name is: ")
print(harry.wizard_name)
print("Born in: ")
print(harry.wizard_birth_year)
print("his patronus is: ")
print(harry.wizard_patronus)
print("his wand's attributes is: ")
harry.assign_wand(wand1)
print(harry.wizard_wand.wood)
print(harry.wizard_wand.core)
print(harry.wizard_wand.length)

# testing for hermoine
print("Wizard's Name is: ")
print(hermoine.wizard_name)
print("Born in: ")
print(hermoine.wizard_birth_year)
print("her patronus is: ")
print(hermoine.wizard_patronus)
print("her wand's attributes is: ")
hermoine.assign_wand(wand2)
print(hermoine.wizard_wand.wood)
print(hermoine.wizard_wand.core)
print(hermoine.wizard_wand.length)