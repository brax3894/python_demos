class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def __repr__(self):
        return f"{self.name} is a  {self.species}"
    def make_sound(self, sound):
        print (f"this animal says {sound}")
class Cat(Animal):
    def __init__(self, name, species, breed, toy):
        #########this is duplication codevvvvvvvvvv
        #self.name = name
        #self.species = species
        #########this is duplication code^^^^^^^^^

        ###this vvvvv is the vvvvvv proper way to inherit parent properties###
        #Animal.__init__(self, name, species)
        #########^^^^^^^^^^^^^^^^^^

        #however theres this idea called super
        super().__init__(name, species)
        self.breed = breed
        self.toy = toy

ed = Cat( "Ed", "Cat", "Scotish Fold", "laser pointer" )
print(ed)
print(ed.species)
print(ed.breed)
print(ed.toy)