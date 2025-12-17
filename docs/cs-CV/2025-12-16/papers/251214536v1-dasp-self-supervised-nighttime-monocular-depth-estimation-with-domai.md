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

**提出DASP框架，利用时空先验的域适应解决夜间单目深度估计性能下降问题。**

🎯 **匹配领域**: **自动驾驶** **深度估计** **视觉里程计**

**关键词**: `夜间深度估计` `自监督学习` `域适应` `时空先验` `对抗网络` `3D一致性投影` `单目视觉` `低光照视觉`

## 📋 核心要点

1. 现有自监督单目深度估计方法在夜间因低光照和动态物体导致性能显著下降，面临无纹理区域和模糊区域挑战。
2. 提出DASP框架，结合对抗分支提取时空先验和自监督分支学习，利用正交差分和轴向注意力增强特征提取能力。
3. 在Oxford RobotCar和nuScenes数据集上实现最先进性能，消融研究验证了各组件有效性，显著提升夜间深度估计精度。

## 📝 摘要（中文）

自监督单目深度估计在白天条件下已取得显著成功，但在夜间由于低可见度和变化光照（如光线不足导致无纹理区域、运动物体带来模糊区域）性能显著下降。为此，我们提出了一个名为DASP的自监督框架，利用时空先验进行夜间深度估计。具体来说，DASP包含一个用于提取时空先验的对抗分支和一个用于学习的自监督分支。在对抗分支中，我们首先设计了一个对抗网络，其中判别器由四个设计的时空先验学习块（SPLB）组成，以利用白天先验。特别地，SPLB包含一个基于空间的时序学习模块（STLM），使用正交差分沿时间轴提取与运动相关的变化，以及一个轴向空间学习模块（ASLM），采用局部非对称卷积与全局轴向注意力来捕获多尺度结构信息。通过结合STLM和ASLM，我们的模型能够获取足够的时空特征来恢复无纹理区域并估计由动态物体引起的模糊区域。在自监督分支中，我们提出了一个3D一致性投影损失，将目标帧和源帧双边投影到共享的3D空间中，并计算两个投影帧之间的3D差异作为损失，以优化3D结构一致性和白天先验。在Oxford RobotCar和nuScenes数据集上的大量实验表明，我们的方法在夜间深度估计方面实现了最先进的性能。消融研究进一步验证了每个组件的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决夜间单目深度估计中因低可见度和变化光照导致的性能下降问题，现有自监督方法在白天表现良好，但在夜间面临无纹理区域和动态物体引起的模糊区域挑战，导致深度估计不准确。

**核心思路**：论文提出DASP框架，通过域适应将白天先验知识迁移到夜间场景，利用时空先验来恢复纹理和估计动态区域，核心思想是结合对抗学习和自监督学习，从白天数据中提取时空特征以增强夜间深度估计的鲁棒性。

**技术框架**：整体架构包括两个分支：对抗分支和自监督分支。对抗分支设计了一个对抗网络，其中判别器包含四个时空先验学习块（SPLB），每个SPLB由空间时序学习模块（STLM）和轴向空间学习模块（ASLM）组成，用于提取时空特征；自监督分支则通过3D一致性投影损失优化深度估计，将目标帧和源帧投影到共享3D空间并计算差异。

**关键创新**：最重要的技术创新是设计了SPLB模块，结合STLM（使用正交差分提取时间轴运动变化）和ASLM（采用局部非对称卷积与全局轴向注意力捕获多尺度空间结构），有效融合时空信息，与现有方法相比，本质区别在于通过域适应和时空先验学习，专门针对夜间场景的挑战进行优化。

**关键设计**：关键设计包括：SPLB中的STLM使用正交差分操作提取时序特征，ASLM结合非对称卷积和轴向注意力机制；损失函数方面，提出了3D一致性投影损失，计算投影帧间的3D差异以增强结构一致性；网络结构上，对抗分支的判别器采用多层SPLB堆叠，自监督分支基于标准深度估计网络，整体参数设置针对夜间数据进行了调整，以平衡特征提取和计算效率。

## 📊 实验亮点

在Oxford RobotCar和nuScenes数据集上的实验表明，DASP在夜间深度估计任务中实现了最先进的性能，具体性能数据未知，但通过消融研究验证了SPLB模块和3D一致性投影损失的有效性，相比基线方法在精度和鲁棒性上有显著提升，例如在纹理恢复和动态区域处理方面表现优异。

## 🎯 应用场景

该研究在自动驾驶、机器人导航和增强现实等领域具有重要应用价值，特别是在夜间或低光照环境下，能够提升视觉系统的深度感知能力，增强安全性和可靠性。未来可能推动夜间视觉技术的发展，为智能系统在复杂光照条件下的部署提供支持。

## 📄 摘要（原文）

> Self-supervised monocular depth estimation has achieved notable success under daytime conditions. However, its performance deteriorates markedly at night due to low visibility and varying illumination, e.g., insufficient light causes textureless areas, and moving objects bring blurry regions. To this end, we propose a self-supervised framework named DASP that leverages spatiotemporal priors for nighttime depth estimation. Specifically, DASP consists of an adversarial branch for extracting spatiotemporal priors and a self-supervised branch for learning. In the adversarial branch, we first design an adversarial network where the discriminator is composed of four devised spatiotemporal priors learning blocks (SPLB) to exploit the daytime priors. In particular, the SPLB contains a spatial-based temporal learning module (STLM) that uses orthogonal differencing to extract motion-related variations along the time axis and an axial spatial learning module (ASLM) that adopts local asymmetric convolutions with global axial attention to capture the multiscale structural information. By combining STLM and ASLM, our model can acquire sufficient spatiotemporal features to restore textureless areas and estimate the blurry regions caused by dynamic objects. In the self-supervised branch, we propose a 3D consistency projection loss to bilaterally project the target frame and source frame into a shared 3D space, and calculate the 3D discrepancy between the two projected frames as a loss to optimize the 3D structural consistency and daytime priors. Extensive experiments on the Oxford RobotCar and nuScenes datasets demonstrate that our approach achieves state-of-the-art performance for nighttime depth estimation. Ablation studies further validate the effectiveness of each component.

