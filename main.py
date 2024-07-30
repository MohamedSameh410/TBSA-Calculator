##Imports needed libraries
import argparse
from Classes.user_data import User
from Classes.image_processing import ImageProcessing
from Classes.medical_report import MedicalReport
from ultralytics import YOLO
from PIL import Image


def main(Name, Age, Weight, Inhalation_injury, Hand_img, Burn_imgs_pathes) :

    ##Get user data
    user = User(name= Name, age= Age, weight= Weight, inhalation_injury= Inhalation_injury)



    ##Load the models
    #Load hand segmentation model
    hand_model = YOLO('Models/Hand segmentation model/train/weights/best.pt')
    #Load burn segmentation model
    burn_model = YOLO('Models/Burn segmentation model/train/weights/best.pt')



    ##Get the pixels
    #load hand image
    hand_img = Image.open(Hand_img)
    #Resize the image
    hand_img_resized = hand_img.resize((640, 640))
    #Calculate the hand mask pixels
    hand_pixels = ImageProcessing.hand_mask_pixels(hand_model, hand_img_resized)
    print("Number of hand pixels of interest:", hand_pixels)


    #load burn images paths
    burn_imgs_pathes = Burn_imgs_pathes
    #Resize the images
    burn_imgs_resized = ImageProcessing.resize_images(burn_imgs_pathes, 352, 352)
    #Calculate the burn masks pixels
    burn_pixels = ImageProcessing.burn_mask_pixels(burn_model, burn_imgs_resized)
    print("Number of burn pixels of interest:", burn_pixels)



    ##Create the medical report
    patient_medical_report = MedicalReport(hand_pixels= hand_pixels, burn_pixels= burn_pixels, weight= user.Weight,
                                           age= user.Age, inhalation_injury= user.Inhalation_Injury)

    #calculate the %TBSA
    TBSA = patient_medical_report.calculate_the_TBSA()

    #calculate the fluid resuscitation
    fluid_resuscitation = patient_medical_report.calculate_the_fluid_amount()

    #calculate the survival probability
    survival_probability = patient_medical_report.calculate_the_survival_probability()



    ##Print the medicall report
    patient_data = [
        ["Key", "value"],
        ["Name:", user.Name],
        ["Age:", user.Age],
        ["Weight:", f'{user.Weight} kg'],
        ["Inhalation injury:", user.inhalation_injury()],
        ["%TBSA:", f'{round(TBSA, 2)} %'],
        ["Fluids amount:", f'{round(fluid_resuscitation, 2)} ml'],
        ["Survival probability:", f'{round(survival_probability, 2)} %']
    ]

    MedicalReport.create_medical_report(data = patient_data)




if __name__ == "__main__" :
    parser = argparse.ArgumentParser(description="Calculate the TBSA using the Palmer method(rule of hand) by computer vision.")

    # User data arguments
    parser.add_argument("--name", type=str, required=True, help="Patient's name.")
    parser.add_argument("--age", type=int, required=True, help="Patient's age.")
    parser.add_argument("--weight", type=float, required=True, help="Patient's weight (kg).")
    parser.add_argument("--inhalation_injury", type=int, default=0, help="Inhalation injury (0 for no, 1 for yes).")

    # Image paths arguments
    parser.add_argument("--hand_image", type=str, required=True, help="Path to the hand image.")
    parser.add_argument("--burn_images", type=str, nargs="+", required=True, help="Paths to the burn images (separate by spaces).")

    args = parser.parse_args()

    # Calculate the TBSA% and create the medical report
    main(Name= args.name, Age= args.age, Weight= args.weight, Inhalation_injury= args.inhalation_injury,
         Hand_img= args.hand_image, Burn_imgs_pathes= args.burn_images)
