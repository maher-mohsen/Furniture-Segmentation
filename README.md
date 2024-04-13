# Furniture-Segmentation
Welcome to our furniture segmentation project, where we leverage the cutting-edge capabilities of YOLOv8m, combined with the data management and augmentation powers of Roboflow, to accurately identify and segment various furniture items in images. This project aims to facilitate applications in interior design, e-commerce, and augmented reality, among others.
## Project Overview
Briefly describe the aim of your project, what problems it solves, and how it contributes to the broader field of image segmentation and furniture recognition.
## Features
- <b>Furniture Detection:</b> Accurately detect multiple furniture categories within an image.
- <b>Segmentation:</b> Percise segmentation of each detected furniture item.
- <b>Efficiency:</b>  Optimized for both speed and accuracy, making it suitable for real-time applications.
- <b>Dataset Management:</b> Utilization of Roboflow for dataset augmentation and preprocessing, ensuring robust model performance.

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