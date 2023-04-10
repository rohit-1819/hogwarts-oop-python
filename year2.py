class Wizard:
    wizard_name = None
    wizard_patronus = None
    wizard_birth_year = None
    wizard_house = None
    wizard_wand = None

    def __init__(self, name, patronus, birth_year):
        self.wizard_name = name
        self.wizard_patronus = patronus
        self.wizard_birth_year = birth_year

harry = Wizard("Harry Potter", "Stag", 1980)
print(harry.wizard_name)
print(harry.wizard_birth_year)
print(harry.wizard_patronus)
hermoine = Wizard("Hermoine Granger", "Otter", 1979)
print(hermoine.wizard_name)
print(hermoine.wizard_birth_year)
print(hermoine.wizard_patronus)