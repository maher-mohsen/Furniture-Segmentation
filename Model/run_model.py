import argparse

import os
from ultralytics import YOLO
HOME = os.getcwd()
def load_model(model_path):
    model = YOLO(model_path)
    return model


def run_inference(model, image):
    results = model.predict(source=image, conf=0.25)
    results[0].show()
    results[0].save(f"{HOME}/output/sample.jpg")
    print(f"Saved predicted image to: {HOME}/output/sample.jpg")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run YOLOv8 model on an image.')
    parser.add_argument('--model', type=str, help='Path to the YOLOv8 model file.')
    parser.add_argument('--image', type=str, help='Path to the image file.')
    parser.add_argument('--output', type=str, help='Output folder for the segmented image.')

    args = parser.parse_args()

    model = load_model(args.model)
    
    prediction = run_inference(model, args.image)
    
    # Assuming your image file has a format and you want to maintain its name in the output folder
    image_name = args.image.split('/')[-1]  # Extracts filename from the provided path

