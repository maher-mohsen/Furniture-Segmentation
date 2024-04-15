# Furniture-Segmentation
## Project Overview
Welcome to our furniture segmentation project, where we leverage the cutting-edge capabilities of YOLOv8m, combined with the data management and augmentation powers of Roboflow, to accurately identify and segment various furniture items in images. This project aims to facilitate applications in interior design, e-commerce, and augmented reality, among others.
## Features
- <b>Furniture Detection:</b> Accurately detect multiple furniture categories within an image.
- <b>Segmentation:</b> Percise segmentation of each detected furniture item.
- <b>Efficiency:</b>  Optimized for both speed and accuracy, making it suitable for real-time applications.
- <b>Dataset Managemen:</b> Utilization of Roboflow for dataset augmentation and preprocessing, ensuring robust model performance.
## Tech Stack

<p align="left"> <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/1/10/PyTorch_logo_icon.svg" alt="pytroch" width="40" height="40"/> </a> <a href="https://roboflow.com/" target="_blank" rel="noreferrer"> <img src="https://app.roboflow.com/images/logomark-color.svg" alt="roboflow" width="40" height="40"/> </a> <a href="https://www.ultralytics.com/" target="_blank" rel="noreferrer"> <img src="https://assets-global.website-files.com/646dd1f1a3703e451ba81ecc/64994922cf2a6385a4bf4489_UltralyticsYOLO_mark_blue.svg" alt="ultralytics" width="40" height="40"/> </a> <a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354139/opencv.svg" alt="open-cv" width="40" height="40"/></a>
<a href="https://share.streamlit.io/" target="_blank" rel="noreferrer"> <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="streamlit" width="40" height="40"/> </a>
<a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://git-scm.com/images/logos/downloads/Git-Icon-1788C.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.python.org/" target="_blank" rel="noreferrer"> <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" alt="python" width="40" height="40"/> </a> <a href="https://code.visualstudio.com/" target="_blank" rel="noreferrer"> <img src="https://code.visualstudio.com/assets/images/code-stable.png" alt="vscode" width="40" height="40"/> </a> <a href="https://desktop.github.com/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Github-desktop-logo-symbol.svg/192px-Github-desktop-logo-symbol.svg.png" alt="github-desktop" width="40" height="40"/> </a>

# Getting Started
## Prerequisites
What things you need to install the software and how to install them:
```py
python >= 3.8
torch
roboflow
ultralytics > 1.08
```
You can install the required Python packages using:
```bash
pip install -r requirements.txt
```
## Installation
A step-by-step series of commands that tells you how to get a development environment running.

Clone the repository:
```bash
git clone https://github.com/maher-mohsen/Furniture-Segmentation.git
```
Navigate into the project directory:
```cmd
cd Furniture-Segmentation\Model
```
Install the dependencies:
```cmd
pip install -r requirements.txt
```
## Training the Model
Instructions on how to train the model, including any specific settings or parameters used.
```cmd
python train.py --img 640  --epochs 1  --model yolov8m.pt
```
## Running Inference
Instructions on how to run the model to segment furniture in new images.
```cmd
python run_model.py --model yolov8x-seg.pt --image sample.jpg
```
# Results
![Confusion matrix VAl](/Model/runs/segment/val/confusion_matrix.png)
![MaskF1 Curve VAl](/Model/runs/segment/val/MaskF1_curve.png)
![Prediction example VAl](/Model/runs/segment/val/val_batch2_pred.jpg)

# Built with
- <a href="https://github.com/ultralytics/ultralytics"> YOLO v8</a>
- <a href="https://roboflow.com/">Roboflow</a>

# Authors
- Maher Mohsen <a href="https://github.com/maher-mohsen">maher-mohsen</a>

# Acknowledgments
- Hat tip to anyone whose code was used
- This project presented for <b>El-Jamel Architecture</b>
# Acknowledgments
You can find online Streamlit demo here
<a href="https://furniture-segmentation-ksjybhqxybpbxwov3jafvj.streamlit.app/">
  <img src="https://i.imgur.com/YOg0fTA.png" alt="Logo" width="40">
</a> 

