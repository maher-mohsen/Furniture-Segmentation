import os
import ultralytics
from ultralytics import YOLO
from IPython.display import display, Image
import argparse
import subprocess
import shlex
import sys
HOME = os.getcwd()
os.chdir(HOME)


def train(model, epochs, imgsz):
 data_yaml_path = f"{HOME}\\datasets\\furniture\\data.yaml"
 command = f"yolo task=segment mode=train model=\"{model}\" data=\"{data_yaml_path}\" epochs={epochs} imgsz={imgsz}"
 os.system(command)

def train_report():
   image1win = f"start runs\\segment\\train\\confusion_matrix.png"
   image2win = f"start runs\\segment\\train\\results.png"
   image3win = f"start runs\\segment\\train\\val_batch0_pred.jpg"

   image1lin = f"xdg-open runs\\segment\\train\\confusion_matrix.png"
   image2lin = f"xdg-open runs\\segment\\train\\results.png"
   image3lin = f"xdg-open runs\\segment\\train\\val_batch0_pred.jpg"

   image1mac = f"open runs\\segment\\train\\confusion_matrix.png"
   image2mac = f"open runs\\segment\\train\\results.png"
   image3mac = f"open runs\\segment\\train\\val_batch0_pred.jpg"

   if sys.platform.startswith('linux'):
    os.system(image1lin)
    os.system(image2lin)
    os.system(image3lin)
   elif sys.platform.startswith('win32'):
    
    os.system(image1win)
    os.system(image2win)
    os.system(image3win)
   elif sys.platform.startswith('darwin'):
    os.system(image1mac)
    os.system(image2mac)
    os.system(image3mac)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train YOLOv8 model on dataset.')
    parser.add_argument('--img', type=str, help='Img size.')
    parser.add_argument('--epochs', type=str, help='Number of epochs')
    parser.add_argument('--model', type=str, help='Path to pretrained .pt model.')
    args = parser.parse_args()
    train(args.model, args.epochs, args.img)
    train_report()