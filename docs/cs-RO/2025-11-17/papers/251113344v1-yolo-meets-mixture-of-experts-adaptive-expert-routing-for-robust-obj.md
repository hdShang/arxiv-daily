---
layout: default
title: YOLO Meets Mixture-of-Experts: Adaptive Expert Routing for Robust Object Detection
---

# YOLO Meets Mixture-of-Experts: Adaptive Expert Routing for Robust Object Detection

**arXiv**: [2511.13344v1](https://arxiv.org/abs/2511.13344) | [PDF](https://arxiv.org/pdf/2511.13344.pdf)

**作者**: Ori Meiraz, Sharon Shalev, Avishai Weizman

---

## 💡 一句话要点

**提出自适应专家路由的混合专家框架，以提升目标检测的鲁棒性和精度。**

**关键词**: `目标检测` `混合专家` `自适应路由` `YOLOv9-T` `特征专业化`

## 📋 核心要点

1. 核心问题：单一YOLOv9-T模型在目标检测中可能缺乏动态特征专业化能力。
2. 方法要点：集成多个YOLOv9-T专家，通过自适应路由实现动态特征选择。
3. 实验或效果：相比单模型，实现了更高的mAP和AR指标。

## 📄 摘要（原文）

> This paper presents a novel Mixture-of-Experts framework for object detection, incorporating adaptive routing among multiple YOLOv9-T experts to enable dynamic feature specialization and achieve higher mean Average Precision (mAP) and Average Recall (AR) compared to a single YOLOv9-T model.

