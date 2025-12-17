---
layout: default
title: EndoCIL: A Class-Incremental Learning Framework for Endoscopic Image Classification
---

# EndoCIL: A Class-Incremental Learning Framework for Endoscopic Image Classification

**arXiv**: [2510.17200v1](https://arxiv.org/abs/2510.17200) | [PDF](https://arxiv.org/pdf/2510.17200.pdf)

**作者**: Bingrong Liu, Jun Shi, Yushan Zheng

---

## 💡 一句话要点

**提出EndoCIL框架以解决内窥镜图像分类中的类增量学习问题**

**关键词**: `类增量学习` `内窥镜图像分类` `灾难性遗忘` `分布对齐` `类不平衡` `梯度校准`

## 📋 核心要点

1. 核心问题：现有重放方法因领域差异和类不平衡导致灾难性遗忘
2. 方法要点：集成分布对齐重放、先验正则化损失和梯度校准组件
3. 实验或效果：在四个数据集上优于先进方法，平衡稳定性和可塑性

## 📄 摘要（原文）

> Class-incremental learning (CIL) for endoscopic image analysis is crucial for
> real-world clinical applications, where diagnostic models should continuously
> adapt to evolving clinical data while retaining performance on previously
> learned ones. However, existing replay-based CIL methods fail to effectively
> mitigate catastrophic forgetting due to severe domain discrepancies and class
> imbalance inherent in endoscopic imaging. To tackle these challenges, we
> propose EndoCIL, a novel and unified CIL framework specifically tailored for
> endoscopic image diagnosis. EndoCIL incorporates three key components: Maximum
> Mean Discrepancy Based Replay (MDBR), employing a distribution-aligned greedy
> strategy to select diverse and representative exemplars, Prior Regularized
> Class Balanced Loss (PRCBL), designed to alleviate both inter-phase and
> intra-phase class imbalance by integrating prior class distributions and
> balance weights into the loss function, and Calibration of Fully-Connected
> Gradients (CFG), which adjusts the classifier gradients to mitigate bias toward
> new classes. Extensive experiments conducted on four public endoscopic datasets
> demonstrate that EndoCIL generally outperforms state-of-the-art CIL methods
> across varying buffer sizes and evaluation metrics. The proposed framework
> effectively balances stability and plasticity in lifelong endoscopic diagnosis,
> showing promising potential for clinical scalability and deployment.

