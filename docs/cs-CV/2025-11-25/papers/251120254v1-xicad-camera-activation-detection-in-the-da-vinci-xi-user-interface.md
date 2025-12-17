---
layout: default
title: XiCAD: Camera Activation Detection in the Da Vinci Xi User Interface
---

# XiCAD: Camera Activation Detection in the Da Vinci Xi User Interface

**arXiv**: [2511.20254v1](https://arxiv.org/abs/2511.20254) | [PDF](https://arxiv.org/pdf/2511.20254.pdf)

**作者**: Alexander C. Jenke, Gregor Just, Claas de Boer, Martin Wagner, Sebastian Bodenstedt, Stefanie Speidel

---

## 💡 一句话要点

**提出XiCAD方法以检测达芬奇Xi手术系统中摄像头激活状态**

**关键词**: `摄像头激活检测` `机器人辅助手术` `卷积神经网络` `手术数据科学` `实时元数据提取`

## 📋 核心要点

1. 核心问题：机器人辅助微创手术中，内窥镜视频是唯一视觉反馈，需自动检测摄像头激活状态以提供元数据。
2. 方法要点：基于ResNet18卷积神经网络构建轻量级管道，定位摄像头图块并识别其激活状态。
3. 实验或效果：在三个公共数据集上评估，F1分数达0.993至1.000，无假阳性多摄像头检测。

## 📄 摘要（原文）

> Purpose: Robot-assisted minimally invasive surgery relies on endoscopic video as the sole intraoperative visual feedback. The DaVinci Xi system overlays a graphical user interface (UI) that indicates the state of each robotic arm, including the activation of the endoscope arm. Detecting this activation provides valuable metadata such as camera movement information, which can support downstream surgical data science tasks including tool tracking, skill assessment, or camera control automation.
>   Methods: We developed a lightweight pipeline based on a ResNet18 convolutional neural network to automatically identify the position of the camera tile and its activation state within the DaVinci Xi UI. The model was fine-tuned on manually annotated data from the SurgToolLoc dataset and evaluated across three public datasets comprising over 70,000 frames.
>   Results: The model achieved F1-scores between 0.993 and 1.000 for the binary detection of active cameras and correctly localized the camera tile in all cases without false multiple-camera detections.
>   Conclusion: The proposed pipeline enables reliable, real-time extraction of camera activation metadata from surgical videos, facilitating automated preprocessing and analysis for diverse downstream applications. All code, trained models, and annotations are publicly available.

