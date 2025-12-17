---
layout: default
title: Language-Guided Open-World Anomaly Segmentation
---

# Language-Guided Open-World Anomaly Segmentation

**arXiv**: [2512.01427v1](https://arxiv.org/abs/2512.01427) | [PDF](https://arxiv.org/pdf/2512.01427.pdf)

**作者**: Klara Reichard, Nikolas Brasch, Nassir Navab, Federico Tombari

---

## 💡 一句话要点

**提出Clipomaly方法，基于CLIP实现自动驾驶中的开放世界与异常分割**

**关键词**: `开放世界分割` `异常分割` `零样本学习` `CLIP模型` `自动驾驶` `语义标签`

## 📋 核心要点

1. 现有方法难以对未知区域分配语义标签，且区分未知类表示困难
2. Clipomaly利用CLIP共享图像-文本嵌入空间，零样本分割未知对象并赋予可解释名称
3. 在异常分割基准上达到先进性能，无需异常训练数据，推理时动态扩展词汇

## 📄 摘要（原文）

> Open-world and anomaly segmentation methods seek to enable autonomous driving systems to detect and segment both known and unknown objects in real-world scenes. However, existing methods do not assign semantically meaningful labels to unknown regions, and distinguishing and learning representations for unknown classes remains difficult. While open-vocabulary segmentation methods show promise in generalizing to novel classes, they require a fixed inference vocabulary and thus cannot be directly applied to anomaly segmentation where unknown classes are unconstrained. We propose Clipomaly, the first CLIP-based open-world and anomaly segmentation method for autonomous driving. Our zero-shot approach requires no anomaly-specific training data and leverages CLIP's shared image-text embedding space to both segment unknown objects and assign human-interpretable names to them. Unlike open-vocabulary methods, our model dynamically extends its vocabulary at inference time without retraining, enabling robust detection and naming of anomalies beyond common class definitions such as those in Cityscapes. Clipomaly achieves state-of-the-art performance on established anomaly segmentation benchmarks while providing interpretability and flexibility essential for practical deployment.

