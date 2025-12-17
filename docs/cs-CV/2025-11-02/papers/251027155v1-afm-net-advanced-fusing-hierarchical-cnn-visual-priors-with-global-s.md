---
layout: default
title: AFM-Net: Advanced Fusing Hierarchical CNN Visual Priors with Global Sequence Modeling for Remote Sensing Image Scene Classification
---

# AFM-Net: Advanced Fusing Hierarchical CNN Visual Priors with Global Sequence Modeling for Remote Sensing Image Scene Classification

**arXiv**: [2510.27155v1](https://arxiv.org/abs/2510.27155) | [PDF](https://arxiv.org/pdf/2510.27155.pdf)

**作者**: Yuanhao Tang, Xuechao Zou, Zhengpei Hu, Junliang Xing, Chengkun Zhang, Jianqiang Huang

---

## 💡 一句话要点

**提出AFM-Net融合CNN与Mamba以解决遥感图像场景分类中的多尺度与全局建模问题**

**关键词**: `遥感图像场景分类` `CNN与Mamba融合` `层次特征融合` `多尺度建模` `全局序列建模` `混合专家分类器`

## 📋 核心要点

1. 核心问题：遥感图像场景分类因复杂空间结构和多尺度特征而具挑战性
2. 方法要点：通过CNN分支提取层次视觉先验，Mamba分支进行高效全局序列建模
3. 实验效果：在AID等数据集上准确率超93%，优于现有方法，平衡性能与效率

## 📄 摘要（原文）

> Remote sensing image scene classification remains a challenging task,
> primarily due to the complex spatial structures and multi-scale characteristics
> of ground objects. Existing approaches see CNNs excel at modeling local
> textures, while Transformers excel at capturing global context. However,
> efficiently integrating them remains a bottleneck due to the high computational
> cost of Transformers. To tackle this, we propose AFM-Net, a novel Advanced
> Hierarchical Fusing framework that achieves effective local and global
> co-representation through two pathways: a CNN branch for extracting
> hierarchical visual priors, and a Mamba branch for efficient global sequence
> modeling. The core innovation of AFM-Net lies in its Hierarchical Fusion
> Mechanism, which progressively aggregates multi-scale features from both
> pathways, enabling dynamic cross-level feature interaction and contextual
> reconstruction to produce highly discriminative representations. These fused
> features are then adaptively routed through a Mixture-of-Experts classifier
> module, which dispatches them to the most suitable experts for fine-grained
> scene recognition. Experiments on AID, NWPU-RESISC45, and UC Merced show that
> AFM-Net obtains 93.72, 95.54, and 96.92 percent accuracy, surpassing
> state-of-the-art methods with balanced performance and efficiency. Code is
> available at https://github.com/tangyuanhao-qhu/AFM-Net.

