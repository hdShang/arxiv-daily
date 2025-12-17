---
layout: default
title: DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors
---

# DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors

**arXiv**: [2512.14536v1](https://arxiv.org/abs/2512.14536) | [PDF](https://arxiv.org/pdf/2512.14536.pdf)

**作者**: Yiheng Huang, Junhong Chen, Anqi Ning, Zhanhong Liang, Nick Michiels, Luc Claesen, Wenyin Liu

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 8 pages, 7 figures

**DOI**: [10.1109/LRA.2025.3644148](https://doi.org/10.1109/LRA.2025.3644148)

---

## 💡 一句话要点

**提出DASP框架，利用时空先验进行自监督夜间单目深度估计，以解决低可见度和动态物体导致的性能下降问题。**

🎯 **匹配领域**: **自动驾驶** **深度估计** **视觉里程计**

**关键词**: `自监督学习` `单目深度估计` `夜间视觉` `时空先验` `对抗网络` `3D一致性投影` `多尺度特征提取` `动态物体处理`

## 📋 核心要点

1. 现有自监督单目深度估计方法在夜间因低可见度和动态物体导致纹理缺失和模糊区域，性能显著下降。
2. DASP框架结合对抗分支提取时空先验和自监督分支学习，通过SPLB模块捕获多尺度时空特征以恢复纹理和估计模糊区域。
3. 在Oxford RobotCar和nuScenes数据集上实现最先进性能，消融研究验证了各组件有效性，提升了夜间深度估计准确性。

## 📝 摘要（中文）

自监督单目深度估计在白天条件下已取得显著成功，但在夜间由于低可见度和变化光照（如光线不足导致纹理缺失区域，移动物体带来模糊区域）而性能显著下降。为此，我们提出了一个名为DASP的自监督框架，利用时空先验进行夜间深度估计。具体来说，DASP包括一个用于提取时空先验的对抗分支和一个用于学习的自监督分支。在对抗分支中，我们首先设计了一个对抗网络，其中判别器由四个设计的时空先验学习块（SPLB）组成，以利用白天先验。特别地，SPLB包含一个基于空间的时序学习模块（STLM），使用正交差分沿时间轴提取与运动相关的变化，以及一个轴向空间学习模块（ASLM），采用局部非对称卷积和全局轴向注意力来捕获多尺度结构信息。通过结合STLM和ASLM，我们的模型能够获取足够的时空特征来恢复纹理缺失区域并估计由动态物体引起的模糊区域。在自监督分支中，我们提出了一个3D一致性投影损失，将目标帧和源帧双边投影到一个共享的3D空间中，并计算两个投影帧之间的3D差异作为损失，以优化3D结构一致性和白天先验。在Oxford RobotCar和nuScenes数据集上的大量实验表明，我们的方法在夜间深度估计方面实现了最先进的性能。消融研究进一步验证了每个组件的有效性。

## 🔬 方法详解

DASP框架包括对抗分支和自监督分支。对抗分支中，判别器由四个时空先验学习块（SPLB）组成，每个SPLB结合基于空间的时序学习模块（STLM）和轴向空间学习模块（ASLM），STLM使用正交差分提取时间轴运动变化，ASLM采用局部非对称卷积和全局轴向注意力捕获多尺度空间结构。自监督分支提出3D一致性投影损失，将目标帧和源帧投影到共享3D空间，计算3D差异作为损失以优化结构一致性和先验。与现有方法相比，DASP通过时空先验学习有效处理夜间低可见度和动态物体问题，而非仅依赖图像重建或简单时序建模。

## 📊 实验亮点

在Oxford RobotCar和nuScenes数据集上，DASP实现了最先进的夜间深度估计性能，通过消融研究验证了SPLB模块和3D一致性投影损失的有效性，显著提升了纹理缺失和模糊区域的估计准确性。

## 🎯 应用场景

该研究可应用于自动驾驶、机器人导航和监控系统等领域，特别是在夜间或低光照环境下，通过提升单目深度估计的鲁棒性，增强环境感知能力，支持安全决策和路径规划。

## 📄 摘要（原文）

> Self-supervised monocular depth estimation has achieved notable success under daytime conditions. However, its performance deteriorates markedly at night due to low visibility and varying illumination, e.g., insufficient light causes textureless areas, and moving objects bring blurry regions. To this end, we propose a self-supervised framework named DASP that leverages spatiotemporal priors for nighttime depth estimation. Specifically, DASP consists of an adversarial branch for extracting spatiotemporal priors and a self-supervised branch for learning. In the adversarial branch, we first design an adversarial network where the discriminator is composed of four devised spatiotemporal priors learning blocks (SPLB) to exploit the daytime priors. In particular, the SPLB contains a spatial-based temporal learning module (STLM) that uses orthogonal differencing to extract motion-related variations along the time axis and an axial spatial learning module (ASLM) that adopts local asymmetric convolutions with global axial attention to capture the multiscale structural information. By combining STLM and ASLM, our model can acquire sufficient spatiotemporal features to restore textureless areas and estimate the blurry regions caused by dynamic objects. In the self-supervised branch, we propose a 3D consistency projection loss to bilaterally project the target frame and source frame into a shared 3D space, and calculate the 3D discrepancy between the two projected frames as a loss to optimize the 3D structural consistency and daytime priors. Extensive experiments on the Oxford RobotCar and nuScenes datasets demonstrate that our approach achieves state-of-the-art performance for nighttime depth estimation. Ablation studies further validate the effectiveness of each component.

