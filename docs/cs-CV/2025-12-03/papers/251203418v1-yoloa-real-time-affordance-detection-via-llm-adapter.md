---
layout: default
title: YOLOA: Real-Time Affordance Detection via LLM Adapter
---

# YOLOA: Real-Time Affordance Detection via LLM Adapter

**arXiv**: [2512.03418v1](https://arxiv.org/abs/2512.03418) | [PDF](https://arxiv.org/pdf/2512.03418.pdf)

**作者**: Yuqi Ji, Junjie Ke, Lihuo He, Jun Liu, Kaifan Zhang, Yu-Kun Lai, Guiguang Ding, Xinbo Gao

---

## 💡 一句话要点

**提出YOLOA模型，通过LLM适配器联合处理物体检测与可供性学习，实现实时可供性检测。**

**关键词**: `可供性检测` `实时检测` `LLM适配器` `物体检测` `多任务学习` `轻量级模型`

## 📋 核心要点

1. 核心问题：现有可供性检测方法常忽略物体识别与定位，或缺乏任务间交互与实时性。
2. 方法要点：采用轻量级检测器，结合LLM适配器优化物体检测和可供性学习分支，提升预测精度。
3. 实验或效果：在ADG-Det和IIT-Heat基准上达到SOTA准确率，同时保持高帧率实时性能。

## 📄 摘要（原文）

> Affordance detection aims to jointly address the fundamental "what-where-how" challenge in embodied AI by understanding "what" an object is, "where" the object is located, and "how" it can be used. However, most affordance learning methods focus solely on "how" objects can be used while neglecting the "what" and "where" aspects. Other affordance detection methods treat object detection and affordance learning as two independent tasks, lacking effective interaction and real-time capability. To overcome these limitations, we introduce YOLO Affordance (YOLOA), a real-time affordance detection model that jointly handles these two tasks via a large language model (LLM) adapter. Specifically, YOLOA employs a lightweight detector consisting of object detection and affordance learning branches refined through the LLM Adapter. During training, the LLM Adapter interacts with object and affordance preliminary predictions to refine both branches by generating more accurate class priors, box offsets, and affordance gates. Experiments on our relabeled ADG-Det and IIT-Heat benchmarks demonstrate that YOLOA achieves state-of-the-art accuracy (52.8 / 73.1 mAP on ADG-Det / IIT-Heat) while maintaining real-time performance (up to 89.77 FPS, and up to 846.24 FPS for the lightweight variant). This indicates that YOLOA achieves an excellent trade-off between accuracy and efficiency.

