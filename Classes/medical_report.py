### This class for calculating the TBSA, the fluid resuscitation, and the survival probability ###

class MedicalReport :


    def __init__(self, hand_pixels, burn_pixels, weight, age, inhalation_injury) :
        
        self.hand_pixels = hand_pixels
        self.burn_pixels = burn_pixels
        self.weight = weight
        self.age = age
        self.inhalation_injury = inhalation_injury
        self.TBSA = 0
        self.fluid_amount = 0


    ##calculate the %TBSA by palmer method(rule of hand)##
    def calculate_the_TBSA(self) :
        #calculate the %TBSA
        self.TBSA = ((self.burn_pixels * 3.3) * 0.8) / (self.hand_pixels)

        return self.TBSA
    

    ##calculate the fluid resuscitation##
    #the equation that used in this step is parkland formula (4ml * weight * %TBSA)
    def calculate_the_fluid_amount(self) :
        # (4ml * weight * %TBSA) = x ml
        self.fluid_amount = 4 * self.weight * self.TBSA

        return self.fluid_amount
    

    ##calculate the survival probability##
    #the equation that used in this step is R-Baux score(Age + %TBSA + 17[Inhalation injury])
    def calculate_the_survival_probability(self):
        #calculate the R-Baux score
        r_baux_score = self.age + self.TBSA + (17 * self.inhalation_injury)

        #return the survival probability
        if (r_baux_score >= 100):
            r_baux_score = 100
            return 100

        else:
            return 100 - r_baux_score
        
    

    ##Create the mdeical report
    @staticmethod
    def create_medical_report(data):
  
        # Determine column widths
        col_widths = [max(len(str(item)) for item in col) for col in zip(*data)]

        # Create the top border
        top_border = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"
        print(top_border)

        # Create the rows
        for row in data:
            print("+", end="")
            for item, width in zip(row, col_widths):
                print(f" {item:<{width}} |", end="")
            print()
            print("+", end="")
            print("+".join("-" * (width + 2) for width in col_widths) + "+")
