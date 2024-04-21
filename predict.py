import argparse
from ultralytics import YOLO

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--version", help="Model version (1, 2), default=1", type=int, default=1)
parser.add_argument("--source", help="Path to source", type=str, required=True)
parser.add_argument("--show", help="Show result", action="store_true", default=False)
args = parser.parse_args()
print(args)

model = YOLO("app/models/best.pt" if args.version == 1 else "app/models/best1.pt" if args.version == 2 else None)
res = model.predict(args.source, save=True)

if args.show:
    for i in res:
        i.show()
