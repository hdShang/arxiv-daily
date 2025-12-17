---
layout: default
title: Reevaluating Automated Wildlife Species Detection: A Reproducibility Study on a Custom Image Dataset
---

# Reevaluating Automated Wildlife Species Detection: A Reproducibility Study on a Custom Image Dataset

**arXiv**: [2512.07305v1](https://arxiv.org/abs/2512.07305) | [PDF](https://arxiv.org/pdf/2512.07305.pdf)

**作者**: Tobias Abraham Haider

---

## 💡 一句话要点

**复现研究评估预训练CNN在野生动物物种检测中的可重复性与泛化性**

**关键词**: `野生动物物种检测` `预训练卷积神经网络` `可重复性研究` `泛化性评估` `相机陷阱图像` `迁移学习`

## 📋 核心要点

1. 核心问题：评估预训练模型在野生动物物种检测中的可重复性和泛化性，尤其当标签与ImageNet类别不直接对齐时。
2. 方法要点：从零开始复现实验，使用公开资源和不同数据集（900张图像，90个物种），进行最小预处理。
3. 实验或效果：整体分类准确率62%，接近原研究71%，但宏F1分数0.28显示类间性能差异大，确认预训练CNN可作为基线但需物种特定适应。

## 📄 摘要（原文）

> This study revisits the findings of Carl et al., who evaluated the pre-trained Google Inception-ResNet-v2 model for automated detection of European wild mammal species in camera trap images. To assess the reproducibility and generalizability of their approach, we reimplemented the experiment from scratch using openly available resources and a different dataset consisting of 900 images spanning 90 species. After minimal preprocessing, we obtained an overall classification accuracy of 62%, closely aligning with the 71% reported in the original work despite differences in datasets. As in the original study, per-class performance varied substantially, as indicated by a macro F1 score of 0.28,highlighting limitations in generalization when labels do not align directly with ImageNet classes. Our results confirm that pretrained convolutional neural networks can provide a practical baseline for wildlife species identification but also reinforce the need for species-specific adaptation or transfer learning to achieve consistent, high-quality predictions.

