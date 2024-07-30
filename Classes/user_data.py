### This class will contain user's data ###

class User:

    def __init__(self, name, age, weight, inhalation_injury) :

        self.Name = name
        self.Age = age
        self.Weight = weight
        
        if inhalation_injury == 0 or inhalation_injury == 1 :
            self.Inhalation_Injury = inhalation_injury
        else :
            print("Invalid input")


    def inhalation_injury (self) :
        
        if self.Inhalation_Injury == 0 :
            return "no"
        else :
            return "yes"
