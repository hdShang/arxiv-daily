---
layout: default
title: From One Attack Domain to Another: Contrastive Transfer Learning with Siamese Networks for APT Detection
---

# From One Attack Domain to Another: Contrastive Transfer Learning with Siamese Networks for APT Detection

**arXiv**: [2511.20500v1](https://arxiv.org/abs/2511.20500) | [PDF](https://arxiv.org/pdf/2511.20500.pdf)

**作者**: Sidahmed Benabderrahmane, Talal Rahwan

---

## 💡 一句话要点

**提出混合迁移框架以提升APT检测的跨域泛化能力**

**关键词**: `APT检测` `迁移学习` `对比学习` `Siamese网络` `可解释AI` `特征选择`

## 📋 核心要点

1. 核心问题：APT检测面临类别不平衡、高维特征和跨域性能下降挑战
2. 方法要点：结合迁移学习、对比学习和Siamese网络，使用注意力自编码器和SHAP进行特征选择
3. 实验或效果：在DARPA TC数据集上验证，检测分数优于经典和深度基线方法

## 📄 摘要（原文）

> Advanced Persistent Threats (APT) pose a major cybersecurity challenge due to their stealth, persistence, and adaptability. Traditional machine learning detectors struggle with class imbalance, high dimensional features, and scarce real world traces. They often lack transferability-performing well in the training domain but degrading in novel attack scenarios. We propose a hybrid transfer framework that integrates Transfer Learning, Explainable AI (XAI), contrastive learning, and Siamese networks to improve cross-domain generalization. An attention-based autoencoder supports knowledge transfer across domains, while Shapley Additive exPlanations (SHAP) select stable, informative features to reduce dimensionality and computational cost. A Siamese encoder trained with a contrastive objective aligns source and target representations, increasing anomaly separability and mitigating feature drift. We evaluate on real-world traces from the DARPA Transparent Computing (TC) program and augment with synthetic attack scenarios to test robustness. Across source to target transfers, the approach delivers improved detection scores with classical and deep baselines, demonstrating a scalable, explainable, and transferable solution for APT detection.

