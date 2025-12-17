---
layout: default
title: From Passive Perception to Active Memory: A Weakly Supervised Image Manipulation Localization Framework Driven by Coarse-Grained Annotations
---

# From Passive Perception to Active Memory: A Weakly Supervised Image Manipulation Localization Framework Driven by Coarse-Grained Annotations

**arXiv**: [2511.20359v1](https://arxiv.org/abs/2511.20359) | [PDF](https://arxiv.org/pdf/2511.20359.pdf)

**作者**: Zhiqing Guo, Dongdong Xi, Songlin Li, Gaobo Yang

---

## 💡 一句话要点

**提出BoxPromptIML框架以解决图像篡改定位中标注成本与精度平衡问题**

**关键词**: `图像篡改定位` `弱监督学习` `知识蒸馏` `粗粒度标注` `特征融合` `轻量模型`

## 📋 核心要点

1. 核心问题：图像篡改定位需平衡像素级标注高成本与图像级标签定位精度不足的困境
2. 方法要点：采用粗粒度区域标注与知识蒸馏，结合双引导特征融合提升定位准确性
3. 实验或效果：在分布内外数据集上表现优于或媲美全监督模型，泛化性强且部署高效

## 📄 摘要（原文）

> Image manipulation localization (IML) faces a fundamental trade-off between minimizing annotation cost and achieving fine-grained localization accuracy. Existing fully-supervised IML methods depend heavily on dense pixel-level mask annotations, which limits scalability to large datasets or real-world deployment.In contrast, the majority of existing weakly-supervised IML approaches are based on image-level labels, which greatly reduce annotation effort but typically lack precise spatial localization. To address this dilemma, we propose BoxPromptIML, a novel weakly-supervised IML framework that effectively balances annotation cost and localization performance. Specifically, we propose a coarse region annotation strategy, which can generate relatively accurate manipulation masks at lower cost. To improve model efficiency and facilitate deployment, we further design an efficient lightweight student model, which learns to perform fine-grained localization through knowledge distillation from a fixed teacher model based on the Segment Anything Model (SAM). Moreover, inspired by the human subconscious memory mechanism, our feature fusion module employs a dual-guidance strategy that actively contextualizes recalled prototypical patterns with real-time observational cues derived from the input. Instead of passive feature extraction, this strategy enables a dynamic process of knowledge recollection, where long-term memory is adapted to the specific context of the current image, significantly enhancing localization accuracy and robustness. Extensive experiments across both in-distribution and out-of-distribution datasets show that BoxPromptIML outperforms or rivals fully-supervised models, while maintaining strong generalization, low annotation cost, and efficient deployment characteristics.

