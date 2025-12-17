---
layout: default
title: An AI-Powered Autonomous Underwater System for Sea Exploration and Scientific Research
---

# An AI-Powered Autonomous Underwater System for Sea Exploration and Scientific Research

**arXiv**: [2512.07652v1](https://arxiv.org/abs/2512.07652) | [PDF](https://arxiv.org/pdf/2512.07652.pdf)

**作者**: Hamad Almazrouei, Mariam Al Nasseri, Maha Alzaabi

---

## 💡 一句话要点

**提出AI驱动的自主水下系统，集成目标检测与LLM生成报告，以提升海洋探索效率。**

**关键词**: `自主水下车辆` `目标检测` `特征提取` `聚类分析` `大语言模型` `海洋探索`

## 📋 核心要点

1. 传统海洋探索面临极端条件和高成本挑战，导致大片区域未勘探。
2. 系统结合YOLOv12 Nano、CNN、PCA和K-Means++进行实时检测与聚类，并集成LLM生成结构化报告。
3. 在55,000+图像数据集上评估，mAP@0.5达0.512，PCA降维保留98%方差，LLM有效生成洞察总结。

## 📄 摘要（原文）

> Traditional sea exploration faces significant challenges due to extreme conditions, limited visibility, and high costs, resulting in vast unexplored ocean regions. This paper presents an innovative AI-powered Autonomous Underwater Vehicle (AUV) system designed to overcome these limitations by automating underwater object detection, analysis, and reporting. The system integrates YOLOv12 Nano for real-time object detection, a Convolutional Neural Network (CNN) (ResNet50) for feature extraction, Principal Component Analysis (PCA) for dimensionality reduction, and K-Means++ clustering for grouping marine objects based on visual characteristics. Furthermore, a Large Language Model (LLM) (GPT-4o Mini) is employed to generate structured reports and summaries of underwater findings, enhancing data interpretation. The system was trained and evaluated on a combined dataset of over 55,000 images from the DeepFish and OzFish datasets, capturing diverse Australian marine environments. Experimental results demonstrate the system's capability to detect marine objects with a mAP@0.5 of 0.512, a precision of 0.535, and a recall of 0.438. The integration of PCA effectively reduced feature dimensionality while preserving 98% variance, facilitating K-Means clustering which successfully grouped detected objects based on visual similarities. The LLM integration proved effective in generating insightful summaries of detections and clusters, supported by location data. This integrated approach significantly reduces the risks associated with human diving, increases mission efficiency, and enhances the speed and depth of underwater data analysis, paving the way for more effective scientific research and discovery in challenging marine environments.

