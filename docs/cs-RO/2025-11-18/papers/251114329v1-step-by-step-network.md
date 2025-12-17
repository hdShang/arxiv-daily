---
layout: default
title: Step by Step Network
---

# Step by Step Network

**arXiv**: [2511.14329v1](https://arxiv.org/abs/2511.14329) | [PDF](https://arxiv.org/pdf/2511.14329.pdf)

**作者**: Dongchen Han, Tianzhu Ye, Zhuofan Xia, Kaiyi Chen, Yulin Wang, Hanting Chen, Gao Huang

---

## 💡 一句话要点

**提出Step by Step Network以解决深度网络中的捷径退化和宽度限制问题**

**关键词**: `深度神经网络` `残差架构` `捷径退化` `宽度限制` `渐进学习` `图像分类`

## 📋 核心要点

1. 核心问题：深度残差网络存在捷径退化和宽度限制，阻碍理论能力发挥
2. 方法要点：沿通道维度分离特征，通过宽度递增的块堆叠实现渐进学习
3. 实验或效果：在图像分类、目标检测等任务中一致优于残差模型

## 📄 摘要（原文）

> Scaling up network depth is a fundamental pursuit in neural architecture design, as theory suggests that deeper models offer exponentially greater capability. Benefiting from the residual connections, modern neural networks can scale up to more than one hundred layers and enjoy wide success. However, as networks continue to deepen, current architectures often struggle to realize their theoretical capacity improvements, calling for more advanced designs to further unleash the potential of deeper networks. In this paper, we identify two key barriers that obstruct residual models from scaling deeper: shortcut degradation and limited width. Shortcut degradation hinders deep-layer learning, while the inherent depth-width trade-off imposes limited width. To mitigate these issues, we propose a generalized residual architecture dubbed Step by Step Network (StepsNet) to bridge the gap between theoretical potential and practical performance of deep models. Specifically, we separate features along the channel dimension and let the model learn progressively via stacking blocks with increasing width. The resulting method mitigates the two identified problems and serves as a versatile macro design applicable to various models. Extensive experiments show that our method consistently outperforms residual models across diverse tasks, including image classification, object detection, semantic segmentation, and language modeling. These results position StepsNet as a superior generalization of the widely adopted residual architecture.

