import os
import random
import shutil

# SET RANDOM SEED (reproducibility)
random.seed(42)

# INPUT & OUTPUT DIRECTORIES
RAW_DATA_DIR = "raw_data"
OUTPUT_DIR = "data"

SPLITS = {
    "train": 0.70,
    "val": 0.15,
    "test": 0.15
}

# CREATE OUTPUT FOLDERS
for split in SPLITS:
    for class_name in ["bird", "drone"]:
        os.makedirs(os.path.join(OUTPUT_DIR, split, class_name), exist_ok=True)

# SPLIT DATA
for class_name in ["bird", "drone"]:
    class_dir = os.path.join(RAW_DATA_DIR, class_name)
    images = os.listdir(class_dir)
    random.shuffle(images)

    total = len(images)
    train_end = int(SPLITS["train"] * total)
    val_end = train_end + int(SPLITS["val"] * total)

    train_imgs = images[:train_end]
    val_imgs = images[train_end:val_end]
    test_imgs = images[val_end:]

    for img in train_imgs:
        shutil.copy(
            os.path.join(class_dir, img),
            os.path.join(OUTPUT_DIR, "train", class_name, img)
        )

    for img in val_imgs:
        shutil.copy(
            os.path.join(class_dir, img),
            os.path.join(OUTPUT_DIR, "val", class_name, img)
        )

    for img in test_imgs:
        shutil.copy(
            os.path.join(class_dir, img),
            os.path.join(OUTPUT_DIR, "test", class_name, img)
        )

    print(f"{class_name}: {len(train_imgs)} train, {len(val_imgs)} val, {len(test_imgs)} test")

print("✅ Dataset successfully split!")
