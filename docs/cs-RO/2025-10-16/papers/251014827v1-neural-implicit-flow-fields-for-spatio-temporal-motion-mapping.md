---
layout: default
title: Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping
---

# Neural Implicit Flow Fields for Spatio-Temporal Motion Mapping

**arXiv**: [2510.14827v1](https://arxiv.org/abs/2510.14827) | [PDF](https://arxiv.org/pdf/2510.14827.pdf)

**作者**: Yufei Zhu, Shih-Min Yang, Andrey Rudenko, Tomasz P. Kucner, Achim J. Lilienthal, Martin Magnusson

---

## 💡 一句话要点

**提出基于隐式神经函数的连续时空运动映射方法，以提升机器人在复杂人类环境中的安全与效率。**

**关键词**: `隐式神经表示` `动态地图建模` `时空运动模式` `机器人导航` `高斯混合模型`

## 📋 核心要点

1. 核心问题：现有动态地图使用离散空间采样，构建成本高且难以处理不均匀采样区域。
2. 方法要点：利用隐式神经函数直接映射坐标到半包裹高斯混合模型参数，实现连续时空建模。
3. 实验或效果：在真实世界人类跟踪数据集上，相比基线方法，精度更高、稀疏区域速度分布更平滑。

## 📄 摘要（原文）

> Safe and efficient robot operation in complex human environments can benefit
> from good models of site-specific motion patterns. Maps of Dynamics (MoDs)
> provide such models by encoding statistical motion patterns in a map, but
> existing representations use discrete spatial sampling and typically require
> costly offline construction. We propose a continuous spatio-temporal MoD
> representation based on implicit neural functions that directly map coordinates
> to the parameters of a Semi-Wrapped Gaussian Mixture Model. This removes the
> need for discretization and imputation for unevenly sampled regions, enabling
> smooth generalization across both space and time. Evaluated on a large public
> dataset with long-term real-world people tracking data, our method achieves
> better accuracy of motion representation and smoother velocity distributions in
> sparse regions while still being computationally efficient, compared to
> available baselines. The proposed approach demonstrates a powerful and
> efficient way of modeling complex human motion patterns.

