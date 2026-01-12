# DroneNet
dataset link:https://drive.google.com/file/d/1Q342HFH24LO-QXaKANWXTFyqKRT1uRzT/view

# 🚁 Drone vs Bird Detection using Deep Learning

This project implements a **binary image classification system** to distinguish between **Drones** and **Birds** using **Deep Learning (ResNet-18)**.  
The system is designed as a simplified prototype for **aerial object detection** in defense and surveillance scenarios.

---

## 📌 Problem Statement
Automatically classify aerial images into:
- **Drone**
- **Bird**

Birds are chosen as the negative class because they are the **most common real-world false positives** in drone detection systems.

---

## 🧠 Approach & Model
- **Model**: ResNet-18 (Transfer Learning)
- **Framework**: PyTorch
- **Task**: Binary Image Classification
- **Execution Mode**: CPU (GPU disabled due to hardware compatibility)

### Why ResNet-18?
- Lightweight and fast
- Strong feature extraction
- Works well with limited datasets
- Industry-standard baseline CNN

---
📊 Dataset Preparation

The dataset is automatically split into:

70% Training

15% Validation

15% Testing

Using:

py -3.10 split_data.py

---

If you want, I can also:
- Write a **short project report (PDF)**
- Add **results table + confusion matrix**
- Make a **resume-ready project description**
- Prepare **viva / interview answers**
---
## 📂 Project Structure
```text
drone_detection/
│
├── raw_data/                 # Original images
│   ├── bird/
│   └── drone/
│
├── data/                     # Segregated dataset
│   ├── train/
│   ├── val/
│   └── test/
│
├── train.py                  # Model training script
├── split_data.py             # Dataset splitting script
├── test_image.py             # Single image inference
├── drone_bird_resnet18.pth   # Trained model weights
├── requirements.txt
└── README.md



Just tell me 👍
