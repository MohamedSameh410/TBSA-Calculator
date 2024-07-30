##Imports needed libraries
from Classes.user_data import User
from Classes.image_processing import ImageProcessing
from Classes.medical_report import MedicalReport
from ultralytics import YOLO
from PIL import Image



##Get user data
user = User(name= "Jak Smith", age= 22, weight= 75, inhalation_injury= 0)



##Load the models
#Load hand segmentation model
hand_model = YOLO('Models/Hand segmentation model/train/weights/best.pt')

#Load burn segmentation model
burn_model = YOLO('Models/Burn segmentation model/train/weights/best.pt')



##Get the pixels
#load hand image
hand_img = Image.open('Test_case/Hand.jpg')
#Resize the image
hand_img_resized = hand_img.resize((640, 640))
#Calculate the hand mask pixels
hand_pixels = ImageProcessing.hand_mask_pixels(hand_model, hand_img_resized)
print("Number of hand pixels of interest:", hand_pixels)


#load burn images paths
burn_imgs_pathes = ['Test_case/Burn_1.jpg',
                    'Test_case/Burn_2.jpg',
                    'Test_case/Burn_3.jpg',
                    'Test_case/Burn_4.jpg']
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