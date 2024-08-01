# TBSA-Calculator
## Overview
This repository contains a deep learning model designed to accurately calculate burn wounds' Total Body Surface Area (TBSA). The model utilizes deep learning techniques to segment burn wounds from images and subsequently converts these segments into a percentage of TBSA based on pixel count.

By automating the TBSA estimation process, this project aims to:

* Improve accuracy: Reduce human error inherent in manual TBSA estimation.
* Increase efficiency: Streamline the burn assessment process for medical professionals.
* Support clinical decision-making: Provide quantitative data for triage, acute management, and patient transfer.


## Applications
* Burns classification & segmentation.
* Calculate burn wounds' Total Body Surface Area (TBSA).
* Create a medical report contains:
  * the fluid resuscitation.
  * the survival probability.

## Medical Assumptions
* For %TBSA: Palmer method(rule of hand).
* For fluid resuscitation: Parkland formula (4ml * weight * %TBSA).
* For survival probability: R-Baux score(Age + %TBSA + 17[Inhalation injury]).

## Getting Started

### Prerequisites
All prerequisites in `requirements.txt` file

### Installation
Follow the steps below to set up the project on your local machine:
1. Clone the repository:
   
   ```bash
   git clone https://github.com/MohamedSameh410/TBSA-Calculator/TBSA-Calculator.git
   cd TBSA-Calculator
   ```
2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```
3. Run the command-line tool to get results

   ```bash
   python main.py --name "patient name" --age age --weight weight --inhalation_injury 0 --hand_image /path/to/hand.jpg --burn_images /path/to/burn1.jpg /path/to/burn2.jpg ...
   ```
   Note that you must replace `"patient name"`,`age`,and`weight` with a real name, age, and weight.

   The `--inhalation_injury` it's default value is 0 but if the patient has an inhalation injury then the value will be      1.
   
   And Replace `/path/to/hand.jpg` with the path to the hand image, The last one is `/path/to/burn1.jpg /path/to/burn2.jpg ...` Replace it with the burn's paths separated by spaces.

   For getting help run this command
   ```bash
   python main.py -h
   ```
## Known Limitations
The current version of the system has a few limitations:
  1. **2D Representation of 3D Structures:** Burn wound images are flat representations of complex, curved body surfaces, similar to the limitations of world maps.
  2. **Camera Distance Impact:** While camera distance can be adjusted using a formula, its effect on image accuracy is relatively straightforward.
  3. **Recommended Practices:** To minimize the impact of the camera angle and improve accuracy, it is suggested to maintain a constant camera distance of approximately 30-50 cm and hold the camera parallel to the wound bed.
     
