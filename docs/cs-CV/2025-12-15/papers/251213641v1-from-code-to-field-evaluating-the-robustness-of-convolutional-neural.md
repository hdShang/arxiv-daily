---
layout: default
title: From Code to Field: Evaluating the Robustness of Convolutional Neural Networks for Disease Diagnosis in Mango Leaves
---

# From Code to Field: Evaluating the Robustness of Convolutional Neural Networks for Disease Diagnosis in Mango Leaves

**arXiv**: [2512.13641v1](https://arxiv.org/abs/2512.13641) | [PDF](https://arxiv.org/pdf/2512.13641.pdf)

**作者**: Gabriel Vitorino de Andrade, Saulo Roberto dos Santos, Itallo Patrick Castro Alves da Silva, Emanuel Adler Medeiros Pereira, Erick de Andrade Barboza

---

## 💡 一句话要点

**提出评估卷积神经网络在芒果叶病害诊断中鲁棒性的方法，以应对图像损坏场景。**

**关键词**: `卷积神经网络` `鲁棒性评估` `芒果叶病害诊断` `图像损坏` `轻量级模型` `农业智能系统`

## 📋 核心要点

1. 核心问题：缺乏针对芒果叶病害诊断模型在噪声、模糊等图像损坏下的鲁棒性研究。
2. 方法要点：基于MangoLeafDB数据集生成MangoLeafDB-C，包含19种人工损坏类型和五个严重级别。
3. 实验或效果：比较五种架构，发现轻量级LCNN在真实场景损坏下表现更优，且平均损坏误差最低。

## 📄 摘要（原文）

> The validation and verification of artificial intelligence (AI) models through robustness assessment are essential to guarantee the reliable performance of intelligent systems facing real-world challenges, such as image corruptions including noise, blurring, and weather variations. Despite the global importance of mango (Mangifera indica L.), there is a lack of studies on the robustness of models for the diagnosis of disease in its leaves. This paper proposes a methodology to evaluate convolutional neural networks (CNNs) under adverse conditions. We adapted the MangoLeafDB dataset, generating MangoLeafDB-C with 19 types of artificial corruptions at five severity levels. We conducted a benchmark comparing five architectures: ResNet-50, ResNet-101, VGG-16, Xception, and LCNN (the latter being a lightweight architecture designed specifically for mango leaf diagnosis). The metrics include the F1 score, the corruption error (CE) and the relative mean corruption error (relative mCE). The results show that LCNN outperformed complex models in corruptions that can be present in real-world scenarios such as Defocus Blur, Motion Blur, while also achieving the lowest mCE. Modern architectures (e.g., ResNet-101) exhibited significant performance degradation in corrupted scenarios, despite their high accuracy under ideal conditions. These findings suggest that lightweight and specialized models may be more suitable for real-world applications in edge devices, where robustness and efficiency are critical. The study highlights the need to incorporate robustness assessments in the development of intelligent systems for agriculture, particularly in regions with technological limitations.

