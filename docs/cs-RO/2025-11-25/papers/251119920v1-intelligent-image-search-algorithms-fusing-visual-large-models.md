---
layout: default
title: Intelligent Image Search Algorithms Fusing Visual Large Models
---

# Intelligent Image Search Algorithms Fusing Visual Large Models

**arXiv**: [2511.19920v1](https://arxiv.org/abs/2511.19920) | [PDF](https://arxiv.org/pdf/2511.19920.pdf)

**作者**: Kehan Wang, Tingqiong Cui, Yang Zhang, Yu Chen, Shifeng Wu, Zhenzhang Li

---

## 💡 一句话要点

**提出DetVLM框架，融合目标检测与视觉大模型，解决细粒度图像检索中的状态搜索和零样本搜索问题。**

**关键词**: `细粒度图像检索` `视觉大模型` `目标检测` `零样本搜索` `状态搜索`

## 📋 核心要点

1. 核心问题：传统方法在细粒度图像检索中缺乏状态判断和零样本能力，视觉大模型空间定位差且计算成本高。
2. 方法要点：采用两阶段流程，YOLO检测器进行组件筛选，视觉大模型进行二次验证和状态判断。
3. 实验效果：在车辆组件数据集上，整体检索准确率达94.82%，零样本搜索准确率达94.95%。

## 📄 摘要（原文）

> Fine-grained image retrieval, which aims to find images containing specific object components and assess their detailed states, is critical in fields like security and industrial inspection. However, conventional methods face significant limitations: manual features (e.g., SIFT) lack robustness; deep learning-based detectors (e.g., YOLO) can identify component presence but cannot perform state-specific retrieval or zero-shot search; Visual Large Models (VLMs) offer semantic and zero-shot capabilities but suffer from poor spatial grounding and high computational cost, making them inefficient for direct retrieval. To bridge these gaps, this paper proposes DetVLM, a novel intelligent image search framework that synergistically fuses object detection with VLMs. The framework pioneers a search-enhancement paradigm via a two-stage pipeline: a YOLO detector first conducts efficient, high-recall component-level screening to determine component presence; then, a VLM acts as a recall-enhancement unit, performing secondary verification for components missed by the detector. This architecture directly enables two advanced capabilities: 1) State Search: Guided by task-specific prompts, the VLM refines results by verifying component existence and executing sophisticated state judgments (e.g., "sun visor lowered"), allowing retrieval based on component state. 2) Zero-shot Search: The framework leverages the VLM's inherent zero-shot capability to recognize and retrieve images containing unseen components or attributes (e.g., "driver wearing a mask") without any task-specific training. Experiments on a vehicle component dataset show DetVLM achieves a state-of-the-art overall retrieval accuracy of 94.82\%, significantly outperforming detection-only baselines. It also attains 94.95\% accuracy in zero-shot search for driver mask-wearing and over 90\% average accuracy in state search tasks.

