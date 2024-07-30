### This class for doing some image processing for the results to get the number of pixels for each mask ###

from ultralytics import YOLO
import torch
from PIL import Image



class ImageProcessing :
    
    #get the number of pixels for burn's images
    @staticmethod
    def burn_mask_pixels(burn_model, imgs) :
        #get predictions
        results = burn_model(imgs, conf=0.5)

        #get the masks and calculate the number of pixels
        num_pixels = 0
        for i, result in enumerate(results):
            mask = result.masks.data
            num_pixels = torch.count_nonzero(mask) + num_pixels
            #save the result
            result.save(filename = f'Test_case/prediction{i}.jpg')


        return num_pixels.item()
    


    #get the number of pixels for hand's image
    @staticmethod
    def hand_mask_pixels(hand_model, img):
        #get predictions
        results = hand_model(img, conf=0.5)

        #get the mask
        mask = results[0].masks.data
        #calculate the number of pixels
        num_pixels = torch.count_nonzero(mask)
        #save the result
        results[0].save(filename = 'Test_case/hand_seg.jpg')

        return num_pixels.item()
    


    #images resize
    @staticmethod
    def resize_images(image_paths, new_width, new_height):
        resized_images = []
        for path in image_paths:
            img = Image.open(path)
            img_resized = img.resize((new_width, new_height))
            resized_images.append(img_resized)
        return resized_images
    




