---
layout: default
title: DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors
---

# DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14536" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14536v1</a>
  <a href="https://arxiv.org/pdf/2512.14536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14536v1" onclick="toggleFavorite(this, '2512.14536v1', 'DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiheng Huang, Junhong Chen, Anqi Ning, Zhanhong Liang, Nick Michiels, Luc Claesen, Wenyin Liu

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: 8 pages, 7 figures

**DOI**: [10.1109/LRA.2025.3644148](https://doi.org/10.1109/LRA.2025.3644148)

---

## 💡 一句话要点

**DASP：利用时空先验域适应的自监督夜间单目深度估计**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自监督学习` `深度估计` `夜间场景` `时空先验` `域适应`

## 📋 核心要点

1. 夜间场景光照不足、动态模糊等问题导致现有自监督深度估计方法性能显著下降。
2. DASP框架利用对抗分支提取白天场景的时空先验知识，并将其迁移到夜间场景的深度估计中。
3. 实验结果表明，DASP在夜间深度估计任务上取得了state-of-the-art的性能，并验证了各模块的有效性。

## 📝 摘要（中文）

自监督单目深度估计在白天条件下取得了显著成功。然而，由于低能见度和变化的光照，其在夜间的性能显著下降，例如，光线不足导致无纹理区域，移动物体带来模糊区域。为此，我们提出了一个名为DASP的自监督框架，该框架利用时空先验进行夜间深度估计。具体来说，DASP由一个用于提取时空先验的对抗分支和一个用于学习的自监督分支组成。在对抗分支中，我们首先设计一个对抗网络，其中判别器由四个设计的时空先验学习块（SPLB）组成，以利用白天先验。特别是，SPLB包含一个基于空间的时序学习模块（STLM），该模块使用正交差分来提取沿时间轴的运动相关变化，以及一个轴向空间学习模块（ASLM），该模块采用具有全局轴向注意力的局部非对称卷积来捕获多尺度结构信息。通过结合STLM和ASLM，我们的模型可以获得足够的时空特征来恢复无纹理区域并估计由动态对象引起的模糊区域。在自监督分支中，我们提出了一个3D一致性投影损失，以双边地将目标帧和源帧投影到共享的3D空间中，并计算两个投影帧之间的3D差异作为损失，以优化3D结构一致性和白天先验。在Oxford RobotCar和nuScenes数据集上的大量实验表明，我们的方法实现了最先进的夜间深度估计性能。消融研究进一步验证了每个组件的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决夜间单目深度估计问题。现有自监督方法在白天表现良好，但在夜间由于光照不足、动态物体模糊等因素，导致深度估计精度大幅下降。现有方法难以有效利用夜间场景的时空信息，并且缺乏对白天场景先验知识的有效迁移。

**核心思路**：论文的核心思路是利用对抗学习框架，将白天场景的时空先验知识迁移到夜间场景的深度估计中。通过设计特定的时空先验学习模块，模型能够更好地理解夜间场景中的结构信息和运动信息，从而提高深度估计的准确性。同时，利用3D一致性投影损失，进一步约束深度估计结果的几何一致性。

**技术框架**：DASP框架包含两个主要分支：对抗分支和自监督分支。对抗分支负责提取白天场景的时空先验知识，并将其作为指导信息传递给自监督分支。自监督分支则利用重投影误差和3D一致性投影损失进行深度估计学习。对抗分支包含一个生成器和一个判别器，判别器由多个时空先验学习块（SPLB）组成。SPLB包含空间时序学习模块（STLM）和轴向空间学习模块（ASLM）。

**关键创新**：论文的关键创新在于提出了时空先验学习块（SPLB），该模块能够有效地提取和利用白天场景的时空先验知识。SPLB通过结合STLM和ASLM，能够同时捕捉时间轴上的运动信息和空间上的结构信息，从而更好地处理夜间场景中的无纹理区域和动态模糊问题。此外，3D一致性投影损失的引入，进一步提升了深度估计的几何一致性。

**关键设计**：STLM使用正交差分提取时间轴上的运动相关变化；ASLM采用局部非对称卷积和全局轴向注意力机制，捕获多尺度结构信息。对抗损失用于促使生成器生成的深度图具有与白天场景相似的时空特征。3D一致性投影损失通过双边投影目标帧和源帧到3D空间，并计算3D差异来优化结构一致性。

## 📊 实验亮点

在Oxford RobotCar和nuScenes数据集上的实验结果表明，DASP方法在夜间深度估计任务上取得了state-of-the-art的性能。相较于现有方法，DASP能够更准确地估计夜间场景的深度信息，尤其是在处理无纹理区域和动态模糊区域时表现更佳。消融实验验证了SPLB、STLM、ASLM以及3D一致性投影损失等各个模块的有效性。

## 🎯 应用场景

该研究成果可应用于夜间自动驾驶、夜间机器人导航、夜间安防监控等领域。通过提高夜间深度估计的准确性，可以提升相关系统在低光照环境下的感知能力和决策能力，从而增强其安全性和可靠性。未来，该方法可以进一步扩展到其他夜间视觉任务，如目标检测、语义分割等。

## 📄 摘要（原文）

> Self-supervised monocular depth estimation has achieved notable success under daytime conditions. However, its performance deteriorates markedly at night due to low visibility and varying illumination, e.g., insufficient light causes textureless areas, and moving objects bring blurry regions. To this end, we propose a self-supervised framework named DASP that leverages spatiotemporal priors for nighttime depth estimation. Specifically, DASP consists of an adversarial branch for extracting spatiotemporal priors and a self-supervised branch for learning. In the adversarial branch, we first design an adversarial network where the discriminator is composed of four devised spatiotemporal priors learning blocks (SPLB) to exploit the daytime priors. In particular, the SPLB contains a spatial-based temporal learning module (STLM) that uses orthogonal differencing to extract motion-related variations along the time axis and an axial spatial learning module (ASLM) that adopts local asymmetric convolutions with global axial attention to capture the multiscale structural information. By combining STLM and ASLM, our model can acquire sufficient spatiotemporal features to restore textureless areas and estimate the blurry regions caused by dynamic objects. In the self-supervised branch, we propose a 3D consistency projection loss to bilaterally project the target frame and source frame into a shared 3D space, and calculate the 3D discrepancy between the two projected frames as a loss to optimize the 3D structural consistency and daytime priors. Extensive experiments on the Oxford RobotCar and nuScenes datasets demonstrate that our approach achieves state-of-the-art performance for nighttime depth estimation. Ablation studies further validate the effectiveness of each component.

