---
layout: default
title: Mapping and Classification of Trees Outside Forests using Deep Learning
---

# Mapping and Classification of Trees Outside Forests using Deep Learning

**arXiv**: [2510.25239v1](https://arxiv.org/abs/2510.25239) | [PDF](https://arxiv.org/pdf/2510.25239.pdf)

**作者**: Moritz Lucas, Hamid Ebrahimy, Viacheslav Barkov, Ralf Pecenka, Kai-Uwe Kühnberger, Björn Waske

---

## 💡 一句话要点

**评估深度学习模型以分类德国农业景观中的森林外树木**

**关键词**: `语义分割` `深度学习` `森林外树木分类` `高分辨率遥感` `模型比较` `泛化实验`

## 📋 核心要点

1. 核心问题：森林外树木分类常被视为单一类别或依赖规则阈值，限制生态解释和跨区域适应性。
2. 方法要点：比较CNN、视觉变换器和混合模型，使用六种语义分割架构映射四类木本植被。
3. 实验或效果：FT-UNetFormer表现最佳，平均IoU 0.74，F1分数0.84，但复杂结构分类仍具挑战。

## 📄 摘要（原文）

> Trees Outside Forests (TOF) play an important role in agricultural landscapes
> by supporting biodiversity, sequestering carbon, and regulating microclimates.
> Yet, most studies have treated TOF as a single class or relied on rigid
> rule-based thresholds, limiting ecological interpretation and adaptability
> across regions. To address this, we evaluate deep learning for TOF
> classification using a newly generated dataset and high-resolution aerial
> imagery from four agricultural landscapes in Germany. Specifically, we compare
> convolutional neural networks (CNNs), vision transformers, and hybrid
> CNN-transformer models across six semantic segmentation architectures (ABCNet,
> LSKNet, FT-UNetFormer, DC-Swin, BANet, and U-Net) to map four categories of
> woody vegetation: Forest, Patch, Linear, and Tree, derived from previous
> studies and governmental products. Overall, the models achieved good
> classification accuracy across the four landscapes, with the FT-UNetFormer
> performing best (mean Intersection-over-Union 0.74; mean F1 score 0.84),
> underscoring the importance of spatial context understanding in TOF mapping and
> classification. Our results show good results for Forest and Linear class and
> reveal challenges particularly in classifying complex structures with high edge
> density, notably the Patch and Tree class. Our generalization experiments
> highlight the need for regionally diverse training data to ensure reliable
> large-scale mapping. The dataset and code are openly available at
> https://github.com/Moerizzy/TOFMapper

