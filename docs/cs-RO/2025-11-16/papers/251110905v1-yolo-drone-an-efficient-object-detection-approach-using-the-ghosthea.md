---
layout: default
title: YOLO-Drone: An Efficient Object Detection Approach Using the GhostHead Network for Drone Images
---

# YOLO-Drone: An Efficient Object Detection Approach Using the GhostHead Network for Drone Images

**arXiv**: [2511.10905v1](https://arxiv.org/abs/2511.10905) | [PDF](https://arxiv.org/pdf/2511.10905.pdf)

**作者**: Hyun-Ki Jung

---

## 💡 一句话要点

**提出YOLO-Drone以解决无人机图像中物体检测的挑战**

**关键词**: `无人机图像检测` `YOLO算法` `GhostHead网络` `VisDrone数据集` `物体检测精度`

## 📋 核心要点

1. 核心问题：无人机图像从高空拍摄，物体识别困难。
2. 方法要点：基于YOLOv11n，引入GhostHead网络改进头部结构。
3. 实验或效果：在VisDrone数据集上，精度、召回率、F1分数和mAP均提升0.4-0.6%。

## 📄 摘要（原文）

> Object detection using images or videos captured by drones is a promising technology with significant potential across various industries. However, a major challenge is that drone images are typically taken from high altitudes, making object identification difficult. This paper proposes an effective solution to address this issue. The base model used in the experiments is YOLOv11, the latest object detection model, with a specific implementation based on YOLOv11n. The experimental data were sourced from the widely used and reliable VisDrone dataset, a standard benchmark in drone-based object detection. This paper introduces an enhancement to the Head network of the YOLOv11 algorithm, called the GhostHead Network. The model incorporating this improvement is named YOLO-Drone. Experimental results demonstrate that YOLO-Drone achieves significant improvements in key detection accuracy metrics, including Precision, Recall, F1-Score, and mAP (0.5), compared to the original YOLOv11. Specifically, the proposed model recorded a 0.4% increase in Precision, a 0.6% increase in Recall, a 0.5% increase in F1-Score, and a 0.5% increase in mAP (0.5). Additionally, the Inference Speed metric, which measures image processing speed, also showed a notable improvement. These results indicate that YOLO-Drone is a high-performance model with enhanced accuracy and speed compared to YOLOv11. To further validate its reliability, comparative experiments were conducted against other high-performance object detection models, including YOLOv8, YOLOv9, and YOLOv10. The results confirmed that the proposed model outperformed YOLOv8 by 0.1% in mAP (0.5) and surpassed YOLOv9 and YOLOv10 by 0.3% and 0.6%, respectively.

