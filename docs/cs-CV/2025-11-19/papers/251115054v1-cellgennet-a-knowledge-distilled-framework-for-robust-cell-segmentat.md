---
layout: default
title: CellGenNet: A Knowledge-Distilled Framework for Robust Cell Segmentation in Cancer Tissues
---

# CellGenNet: A Knowledge-Distilled Framework for Robust Cell Segmentation in Cancer Tissues

**arXiv**: [2511.15054v1](https://arxiv.org/abs/2511.15054) | [PDF](https://arxiv.org/pdf/2511.15054.pdf)

**作者**: Srijan Ray, Bikesh K. Nirala, Jason T. Yustein, Sundaresh Ram

---

## 💡 一句话要点

**提出CellGenNet知识蒸馏框架以解决癌症组织细胞分割的鲁棒性问题**

**关键词**: `细胞分割` `知识蒸馏` `师生架构` `混合损失函数` `全切片图像` `癌症组织分析`

## 📋 核心要点

1. 核心问题：显微镜全切片图像中细胞核分割因染色、成像和组织形态变异而困难
2. 方法要点：采用师生架构，教师生成软伪标签，学生结合真实标签和混合损失优化
3. 实验或效果：在多种癌症组织WSI上，CellGenNet提升分割准确性和泛化能力

## 📄 摘要（原文）

> Accurate nuclei segmentation in microscopy whole slide images (WSIs) remains challenging due to variability in staining, imaging conditions, and tissue morphology. We propose CellGenNet, a knowledge distillation framework for robust cross-tissue cell segmentation under limited supervision. CellGenNet adopts a student-teacher architecture, where a capacity teacher is trained on sparse annotations and generates soft pseudo-labels for unlabeled regions. The student is optimized using a joint objective that integrates ground-truth labels, teacher-derived probabilistic targets, and a hybrid loss function combining binary cross-entropy and Tversky loss, enabling asymmetric penalties to mitigate class imbalance and better preserve minority nuclear structures. Consistency regularization and layerwise dropout further stabilize feature representations and promote reliable feature transfer. Experiments across diverse cancer tissue WSIs show that CellGenNet improves segmentation accuracy and generalization over supervised and semi-supervised baselines, supporting scalable and reproducible histopathology analysis.

