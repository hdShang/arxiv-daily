---
layout: default
title: A Modular Object Detection System for Humanoid Robots Using YOLO
---

# A Modular Object Detection System for Humanoid Robots Using YOLO

**arXiv**: [2510.13625v1](https://arxiv.org/abs/2510.13625) | [PDF](https://arxiv.org/pdf/2510.13625.pdf)

**作者**: Nicolas Pottier, Meng Cheng Lau

---

## 💡 一句话要点

**提出基于YOLOv9的模块化物体检测系统，用于人形机器人视觉任务。**

**关键词**: `物体检测` `YOLOv9` `机器人视觉` `ROS1` `性能评估` `FIRA Hurocup`

## 📋 核心要点

1. 机器人视觉系统效率低是主要障碍，影响任务执行。
2. 采用YOLOv9框架，在ROS1中实现模块，适配机器人计算受限环境。
3. 在FIRA Hurocup数据集上训练，YOLO模型精度与几何模型相当，但计算成本更高、鲁棒性更强。

## 📄 摘要（原文）

> Within the field of robotics, computer vision remains a significant barrier
> to progress, with many tasks hindered by inefficient vision systems. This
> research proposes a generalized vision module leveraging YOLOv9, a
> state-of-the-art framework optimized for computationally constrained
> environments like robots. The model is trained on a dataset tailored to the
> FIRA robotics Hurocup. A new vision module is implemented in ROS1 using a
> virtual environment to enable YOLO compatibility. Performance is evaluated
> using metrics such as frames per second (FPS) and Mean Average Precision (mAP).
> Performance is then compared to the existing geometric framework in static and
> dynamic contexts. The YOLO model achieved comparable precision at a higher
> computational cost then the geometric model, while providing improved
> robustness.

