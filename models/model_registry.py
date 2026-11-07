from megadetector.yolo_manager import YOLOManager
from wdmilfast.wdmilfast_manager import WDMilFastManager

MODEL_REGISTRY = {
    "megadetector": YOLOManager,
    "wdmilfast": WDMilFastManager,
}
