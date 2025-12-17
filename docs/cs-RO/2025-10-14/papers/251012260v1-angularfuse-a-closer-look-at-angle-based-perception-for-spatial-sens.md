---
layout: default
title: AngularFuse: A Closer Look at Angle-based Perception for Spatial-Sensitive Multi-Modality Image Fusion
---

# AngularFuse: A Closer Look at Angle-based Perception for Spatial-Sensitive Multi-Modality Image Fusion

**arXiv**: [2510.12260v1](https://arxiv.org/abs/2510.12260) | [PDF](https://arxiv.org/pdf/2510.12260.pdf)

**作者**: Xiaopeng Liu, Yupei Lin, Sen Zhang, Xiao Wang, Yukai Shi, Liang Lin

---

## 💡 一句话要点

**提出AngularFuse框架，通过角度感知损失解决可见光-红外图像融合中的细节和亮度问题。**

**关键词**: `图像融合` `角度感知损失` `跨模态互补` `无监督学习` `梯度约束`

## 📋 核心要点

1. 核心问题：现有无监督融合方法依赖手工损失函数，导致细节缺失和亮度不均。
2. 方法要点：引入跨模态互补掩码模块和角度感知损失，同时约束梯度幅值和方向。
3. 实验或效果：在MSRS等数据集上优于主流方法，生成图像更锐利和详细。

## 📄 摘要（原文）

> Visible-infrared image fusion is crucial in key applications such as
> autonomous driving and nighttime surveillance. Its main goal is to integrate
> multimodal information to produce enhanced images that are better suited for
> downstream tasks. Although deep learning based fusion methods have made
> significant progress, mainstream unsupervised approaches still face serious
> challenges in practical applications. Existing methods mostly rely on manually
> designed loss functions to guide the fusion process. However, these loss
> functions have obvious limitations. On one hand, the reference images
> constructed by existing methods often lack details and have uneven brightness.
> On the other hand, the widely used gradient losses focus only on gradient
> magnitude. To address these challenges, this paper proposes an angle-based
> perception framework for spatial-sensitive image fusion (AngularFuse). At
> first, we design a cross-modal complementary mask module to force the network
> to learn complementary information between modalities. Then, a fine-grained
> reference image synthesis strategy is introduced. By combining Laplacian edge
> enhancement with adaptive histogram equalization, reference images with richer
> details and more balanced brightness are generated. Last but not least, we
> introduce an angle-aware loss, which for the first time constrains both
> gradient magnitude and direction simultaneously in the gradient domain.
> AngularFuse ensures that the fused images preserve both texture intensity and
> correct edge orientation. Comprehensive experiments on the MSRS, RoadScene, and
> M3FD public datasets show that AngularFuse outperforms existing mainstream
> methods with clear margin. Visual comparisons further confirm that our method
> produces sharper and more detailed results in challenging scenes, demonstrating
> superior fusion capability.

