import io
import torch
import cv2
import numpy as np
import albumentations as A
import segmentation_models_pytorch as smp
from PIL import Image
import base64

def init_context(context):
    context.logger.info("Initializing segmentation model...")

    # Load model and preprocessing only once
    checkpoint = "smp-hub/segformer-b5-640x640-ade-160k"
    context.model = smp.from_pretrained(checkpoint).eval()
    context.preprocessing = A.Compose.from_pretrained(checkpoint)

def handler(context, event):
    # Get the image data from the event (list of images)
    data = event.body

    results = []
    for item in data:
        image_data = base64.b64decode(item["image"])
        image = np.array(Image.open(io.BytesIO(image_data)).convert("RGB"))

        # Preprocess
        image_preprocessed = context.preprocessing(image=image)["image"]
        input_tensor = torch.as_tensor(image_preprocessed).permute(2, 0, 1).unsqueeze(0)

        # Inference
        with torch.no_grad():
            output = context.model(input_tensor)

        # Resize mask to original size
        mask = torch.nn.functional.interpolate(
            output, size=(image.shape[0], image.shape[1]),
            mode="bilinear", align_corners=False
        )
        mask = mask.argmax(1).squeeze().cpu().numpy()

        # Extract polygons
        shapes = []
        for class_id in np.unique(mask):
            if class_id == 0:
                continue  # skip background

            binary_mask = np.uint8(mask == class_id) * 255
            contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                if len(contour) >= 3:
                    points = contour.squeeze().tolist()
                    if isinstance(points[0], list):
                        shapes.append({
                            "label": str(class_id),
                            "points": points,
                            "type": "polygon"
                        })

        results.append({
            "shapes": shapes
        })

    return results
