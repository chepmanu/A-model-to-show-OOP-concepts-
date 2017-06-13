class Mobile(object):
    """
    Parent class of all mobile phones
    """
    def __init__(self, model=""):
        self.__initialize()  # Private method of the class
        self.model = model
        self.size = 0

    def narrate(self):
        print "Creating {} inches for an {}".format(self.size, self.model)

    def get_make(self):
        raise NotImplementedError("This attribute has not been set")

    def create_screen(self):
        print "Creating default size"
        self.size = 5.1

    #  Encapsulation : Trailing double underscore to depict a private method although python is not strict about this
    def __initialize(self):
        self.can_call = True
        self.can_send_message = True



class Iphone(Mobile):  # Inheritance from the parent Mobile class

    #  Polymorphism is used in this case
    def get_make(self):
        return "Iphone"

    def create_screen(self):
        self.size = 4.7
        self.narrate()




class Samsung(Mobile):  # Inheritance from the parent Mobile class

    #  #  Polymorphism is used in this case
    def get_make(self):
        return "Samsung"

    def create_screen(self):
        self.size = 6.2
        self.narrate()


mobile = Mobile()

s7 = Iphone("Iphone S7")
s7.create_screen()

galaxy = Samsung("Galaxy S8")
galaxy.create_screen()


print s7.get_make()
print galaxy.get_make()
print mobile.get_make()

