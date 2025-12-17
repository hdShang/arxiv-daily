---
layout: default
title: Impugan: Learning Conditional Generative Models for Robust Data Imputation
---

# Impugan: Learning Conditional Generative Models for Robust Data Imputation

**arXiv**: [2512.05950v1](https://arxiv.org/abs/2512.05950) | [PDF](https://arxiv.org/pdf/2512.05950.pdf)

**作者**: Zalish Mahmud, Anantaa Kotal, Aritran Piplai

---

## 💡 一句话要点

**提出Impugan条件生成对抗网络以解决异构数据缺失值填补问题**

**关键词**: `数据填补` `条件生成对抗网络` `异构数据集成` `对抗训练` `缺失值处理`

## 📋 核心要点

1. 现实应用中数据常因传感器故障或来源差异而缺失，传统方法依赖线性假设易产生偏差
2. Impugan利用cGAN学习观测与缺失变量间的非线性多模态关系，通过对抗训练生成真实填补值
3. 在基准测试中，相比基线方法，Impugan显著降低Earth Mover's Distance和互信息偏差

## 📄 摘要（原文）

> Incomplete data are common in real-world applications. Sensors fail, records are inconsistent, and datasets collected from different sources often differ in scale, sampling rate, and quality. These differences create missing values that make it difficult to combine data and build reliable models. Standard imputation methods such as regression models, expectation-maximization, and multiple imputation rely on strong assumptions about linearity and independence. These assumptions rarely hold for complex or heterogeneous data, which can lead to biased or over-smoothed estimates. We propose Impugan, a conditional Generative Adversarial Network (cGAN) for imputing missing values and integrating heterogeneous datasets. The model is trained on complete samples to learn how missing variables depend on observed ones. During inference, the generator reconstructs missing entries from available features, and the discriminator enforces realism by distinguishing true from imputed data. This adversarial process allows Impugan to capture nonlinear and multimodal relationships that conventional methods cannot represent. In experiments on benchmark datasets and a multi-source integration task, Impugan achieves up to 82\% lower Earth Mover's Distance (EMD) and 70\% lower mutual-information deviation (MI) compared to leading baselines. These results show that adversarially trained generative models provide a scalable and principled approach for imputing and merging incomplete, heterogeneous data. Our model is available at: github.com/zalishmahmud/impuganBigData2025

