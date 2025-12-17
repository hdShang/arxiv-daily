---
layout: default
title: Reliable Detection of Minute Targets in High-Resolution Aerial Imagery across Temporal Shifts
---

# Reliable Detection of Minute Targets in High-Resolution Aerial Imagery across Temporal Shifts

**arXiv**: [2512.11360v1](https://arxiv.org/abs/2512.11360) | [PDF](https://arxiv.org/pdf/2512.11360.pdf)

**作者**: Mohammad Sadegh Gholizadeh, Amir Arsalan Rezapour, Hamidreza Shayegh, Ehsan Pazouki

---

## 💡 一句话要点

**提出基于迁移学习的Faster R-CNN方法，以解决高分辨率航拍图像中水稻幼苗微小目标检测的挑战。**

**关键词**: `微小目标检测` `高分辨率航拍图像` `迁移学习` `Faster R-CNN` `农业视觉` `域泛化`

## 📋 核心要点

1. 核心问题：高分辨率航拍图像中微小目标检测困难，且环境变化影响模型泛化能力。
2. 方法要点：利用迁移学习初始化Faster R-CNN，并构建大规模无人机数据集进行训练。
3. 实验或效果：在三个不同时间间隔的测试集上验证，模型在域偏移下保持稳定性能。

## 📄 摘要（原文）

> Efficient crop detection via Unmanned Aerial Vehicles is critical for scaling precision agriculture, yet it remains challenging due to the small scale of targets and environmental variability. This paper addresses the detection of rice seedlings in paddy fields by leveraging a Faster R-CNN architecture initialized via transfer learning. To overcome the specific difficulties of detecting minute objects in high-resolution aerial imagery, we curate a significant UAV dataset for training and rigorously evaluate the model's generalization capabilities. Specifically, we validate performance across three distinct test sets acquired at different temporal intervals, thereby assessing robustness against varying imaging conditions. Our empirical results demonstrate that transfer learning not only facilitates the rapid convergence of object detection models in agricultural contexts but also yields consistent performance despite domain shifts in image acquisition.

