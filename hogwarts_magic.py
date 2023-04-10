# creating a class Wizard
class Wizard:

    def __init__(self, name, patronus, birth_year):
        self.wizard_name = name
        self.wizard_patronus = patronus
        self.wizard_birth_year = birth_year
        self.wizard_house = None
        self.wizard_wand = None

    def assign_wand(self, wand):
        # wand is an object of Wand Class
        self.wizard_wand = wand

    def assign_house(self, house):
        #import pdb
        #pdb.set_trace()
        # house is not a variable, its an object of House Class
        self.wizard_house = house

#creating a class House
class House:

    def __init__(self, name, founder, colors, animal):
        self.house_name = name
        self.house_founder = founder
        self.house_color = colors
        self.house_animal = animal
        self.house_members = []
        self.house_points = 0

    # method to add members to the house_members
    def add_member(self, member):
        if member not in self.house_members:
            self.house_members.append(member)

    # method to add members to the house_members
    def remove_member(self, member):
        self.house_members.remove(member)

    # method to update points of the house 
    def update_points(self, points):
        self.house_points += points

    def get_house_details(self):
        details = {
            "Name": self.house_name,
            "Founder": self.house_founder,
            "Colors": self.house_color,
            "Animal": self.house_animal,
            "Points": self.house_points
        }
        print(details)

# creating a Class Wand
class Wand:

    def __init__(self, wood, core, length):
        self.wood = wood
        self.core = core
        self.length = length