import torch
from wdmilfast.wildlife_detector_mil import WildlifeDetectorMIL, load_yolo
from torchvision import transforms
from wdmilfast.wildlife_postprocessor import WildlifeMilPostProcessor
from PIL import ImageDraw, ImageFont
import io
import base64


class WDMilFastManager:
    def __init__(
        self,
        num_classes=10,
        model_path="wdmilfast/model_4.pth",
        yolo_model_path="megadetector/MDV6-yolov9e.pt",
        yolo_base="ultralytics",
        classifier="convnext",
        yolo_th=0.6,
    ):
        self.device = "cpu"
        self.model = self.load(
            num_classes, model_path, yolo_model_path, yolo_base, classifier, yolo_th
        )
        self.num_classes = num_classes
        self.model_path = model_path
        self.yolo_model_path = yolo_model_path
        self.yolo_base = yolo_base
        self.classifier = classifier
        self.yolo_th = yolo_th
        self.main_transform = transforms.Compose(
            [
                transforms.Resize((640, 640)),
                transforms.ToTensor(),
            ]
        )
        self.postprocessor = WildlifeMilPostProcessor(
            10, [640, 640], [224, 224], 0.3, "xyxy", "xyxy"
        )

    def load(
        self, num_classes, model_path, yolo_model_path, yolo_base, classifier, yolo_th
    ):
        model = WildlifeDetectorMIL(
            num_classes,
            yolo_model_path,
            yolo_base,
            classifier,
            yolo_th,
        )
        model.load_state_dict(torch.load(model_path), strict=False)
        model.yolo = load_yolo(yolo_model_path, yolo_base)
        model.resnet.eval()
        return model

    def unmount(self):
        self.model.to("cpu")
        self.device = "cpu"

    def mount(self):
        self.model.to("cuda")
        self.device = "cuda"

    def predict(self, x):
        with torch.inference_mode():
            results = self.model(
                self.main_transform(x).unsqueeze(0).to(self.device),
                self.model.resnet_transform(x).unsqueeze(0).to(self.device),
            )
        results = self.postprocessor(results, x.size[0], x.size[1], True, True)
        new_image = draw_predictions(x, results[0])

        buffer = io.BytesIO()
        new_image.save(buffer, format="JPEG")

        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return {
            "predictions": results[0],
            "annotated_image": image_base64,
        }


def draw_predictions(image, predictions, class_names=None):
    """
    Args:
        image: PIL Image.
        predictions: Dictionary containing boxes, scores, labels.
                     Can also be a single-image output from your postprocessor.
        class_names: Optional list of class names.

    Returns:
        PIL Image with bounding boxes and labels drawn.
    """
    image = image.copy()
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except OSError:
        font = ImageFont.load_default()

    boxes = predictions["boxes"]
    scores = predictions["scores"]
    labels = predictions["labels"]

    for box, score, label in zip(boxes, scores, labels):
        x1, y1, x2, y2 = map(float, box)

        label = int(label)
        score = float(score)

        class_name = class_names[label] if class_names is not None else str(label)

        text = f"{class_name}: {score:.2f}"

        # Draw bounding box
        draw.rectangle(
            [x1, y1, x2, y2],
            outline="red",
            width=3,
        )

        # Draw label background
        text_bbox = draw.textbbox((x1, y1), text, font=font)
        draw.rectangle(text_bbox, fill="red")

        # Draw label text
        draw.text(
            (x1, y1),
            text,
            fill="white",
            font=font,
        )

    return image
