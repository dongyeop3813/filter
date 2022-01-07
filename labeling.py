from ai import predict
from dataset import Dataset
from pathlib import Path
from PIL import Image
import csv

predict_result = []

outcome = Dataset(Path("../filtered/dataset1"))

for idx in range(len(outcome)):
    img = Image.open(outcome.dir / f"{idx}.jpg")
    pred = predict(img)
    filename = f"{idx}.npy"

    predict_result.append([filename, pred])
    img.close()

    if idx % 1000 == 0:
        print(f"[+] Completed {idx}-th image")

with open("./label.csv", newline='', mode='w') as csvfile:
    writer = csv.writer(csvfile)
    for row in predict_result:
        writer.writerow(row)
