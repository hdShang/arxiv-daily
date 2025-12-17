---
layout: default
title: On-Device Continual Learning for Unsupervised Visual Anomaly Detection in Dynamic Manufacturing
---

# On-Device Continual Learning for Unsupervised Visual Anomaly Detection in Dynamic Manufacturing

**arXiv**: [2512.13497v1](https://arxiv.org/abs/2512.13497) | [PDF](https://arxiv.org/pdf/2512.13497.pdf)

**作者**: Haoyu Ren, Kay Koehle, Kirill Dorofeev, Darko Anicic

---

## 💡 一句话要点

**提出基于设备端持续学习的无监督视觉异常检测方法，以应对动态制造中的快速产品变化和资源限制。**

**关键词**: `设备端持续学习` `无监督视觉异常检测` `动态制造` `边缘计算` `核心集更新` `工业应用`

## 📋 核心要点

1. 核心问题：动态制造中产品频繁变化、边缘设备资源有限及异常数据稀缺，导致传统视觉异常检测难以适应。
2. 方法要点：扩展PatchCore，采用轻量特征提取器和基于k中心选择的增量核心集更新机制，实现设备端在线学习。
3. 实验或效果：在工业用例中，AUROC提升12%，内存使用减少80%，训练速度优于批量重训练。

## 📄 摘要（原文）

> In modern manufacturing, Visual Anomaly Detection (VAD) is essential for automated inspection and consistent product quality. Yet, increasingly dynamic and flexible production environments introduce key challenges: First, frequent product changes in small-batch and on-demand manufacturing require rapid model updates. Second, legacy edge hardware lacks the resources to train and run large AI models. Finally, both anomalous and normal training data are often scarce, particularly for newly introduced product variations. We investigate on-device continual learning for unsupervised VAD with localization, extending the PatchCore to incorporate online learning for real-world industrial scenarios. The proposed method leverages a lightweight feature extractor and an incremental coreset update mechanism based on k-center selection, enabling rapid, memory-efficient adaptation from limited data while eliminating costly cloud retraining. Evaluations on an industrial use case are conducted using a testbed designed to emulate flexible production with frequent variant changes in a controlled environment. Our method achieves a 12% AUROC improvement over the baseline, an 80% reduction in memory usage, and faster training compared to batch retraining. These results confirm that our method delivers accurate, resource-efficient, and adaptive VAD suitable for dynamic and smart manufacturing.

