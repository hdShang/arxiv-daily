---
layout: default
title: Fair and Interpretable Deepfake Detection in Videos
---

# Fair and Interpretable Deepfake Detection in Videos

**arXiv**: [2510.17264v1](https://arxiv.org/abs/2510.17264) | [PDF](https://arxiv.org/pdf/2510.17264.pdf)

**作者**: Akihito Yoshii, Ryosuke Sonoda, Ramya Srinivasan

---

## 💡 一句话要点

**提出公平感知的深度伪造检测框架，集成时序特征学习和人口统计感知数据增强以提升公平性和可解释性。**

**关键词**: `深度伪造检测` `公平性增强` `时序建模` `数据增强` `可解释性` `人口统计感知`

## 📋 核心要点

1. 现有深度伪造检测方法存在偏见、缺乏透明度，且忽略时序信息，导致跨人口群体决策不可靠。
2. 方法结合序列聚类进行时序建模和概念提取，并引入人口统计感知数据增强以平衡群体和保留伪造伪影。
3. 在多个数据集上实验显示，该方法在公平性和准确性间取得最佳权衡，优于现有技术。

## 📄 摘要（原文）

> Existing deepfake detection methods often exhibit bias, lack transparency,
> and fail to capture temporal information, leading to biased decisions and
> unreliable results across different demographic groups. In this paper, we
> propose a fairness-aware deepfake detection framework that integrates temporal
> feature learning and demographic-aware data augmentation to enhance fairness
> and interpretability. Our method leverages sequence-based clustering for
> temporal modeling of deepfake videos and concept extraction to improve
> detection reliability while also facilitating interpretable decisions for
> non-expert users. Additionally, we introduce a demography-aware data
> augmentation method that balances underrepresented groups and applies
> frequency-domain transformations to preserve deepfake artifacts, thereby
> mitigating bias and improving generalization. Extensive experiments on
> FaceForensics++, DFD, Celeb-DF, and DFDC datasets using state-of-the-art (SoTA)
> architectures (Xception, ResNet) demonstrate the efficacy of the proposed
> method in obtaining the best tradeoff between fairness and accuracy when
> compared to SoTA.

