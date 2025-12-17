---
layout: default
title: DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors
---

# DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14536" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14536</a>
  <a href="https://arxiv.org/pdf/2512.14536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14536" onclick="toggleFavorite(this, '2512.14536', 'DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiheng Huang, Junhong Chen, Anqi Ning, Zhanhong Liang, Nick Michiels, Luc Claesen, Wenyin Liu

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**DASP：利用时空先验域适应的自监督夜间单目深度估计**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `自监督学习` `深度估计` `夜间场景` `域适应` `时空先验` `对抗学习` `单目视觉`

## 📋 核心要点

1. 夜间场景光照不足和动态模糊导致现有自监督单目深度估计方法性能显著下降。
2. DASP框架利用对抗学习提取白天场景的时空先验知识，并将其迁移到夜间深度估计中。
3. 实验表明，DASP在夜间深度估计任务上取得了state-of-the-art的性能，并验证了各模块的有效性。

## 📝 摘要（中文）

本文提出了一种名为DASP的自监督框架，利用时空先验进行夜间深度估计。DASP包含一个用于提取时空先验的对抗分支和一个用于学习的自监督分支。在对抗分支中，设计了一个对抗网络，其判别器由四个设计的时空先验学习块（SPLB）组成，以利用白天先验。SPLB包含一个基于空间的时序学习模块（STLM），它使用正交差分来提取沿时间轴的运动相关变化，以及一个轴向空间学习模块（ASLM），它采用具有全局轴向注意力的局部非对称卷积来捕获多尺度结构信息。通过结合STLM和ASLM，该模型可以获得足够的时空特征来恢复无纹理区域并估计由动态对象引起的模糊区域。在自监督分支中，提出了一个3D一致性投影损失，以双边地将目标帧和源帧投影到共享的3D空间中，并计算两个投影帧之间的3D差异作为损失，以优化3D结构一致性和白天先验。在Oxford RobotCar和nuScenes数据集上的大量实验表明，该方法实现了最先进的夜间深度估计性能。消融研究进一步验证了每个组件的有效性。

## 🔬 方法详解

**问题定义**：现有自监督单目深度估计方法在白天场景表现良好，但在夜间场景中，由于光照不足导致的纹理缺失以及运动物体造成的模糊，性能会显著下降。因此，论文旨在解决夜间单目深度估计问题，提高在低光照和动态环境下的深度估计精度。

**核心思路**：论文的核心思路是利用白天场景的时空先验知识来辅助夜间深度估计。通过对抗学习，将白天场景中丰富的纹理信息和运动模式迁移到夜间场景，从而弥补夜间场景中信息不足的问题。这种域适应的方法能够有效地提高夜间深度估计的准确性和鲁棒性。

**技术框架**：DASP框架包含两个主要分支：对抗分支和自监督分支。对抗分支负责提取白天场景的时空先验知识，并将其迁移到夜间场景。该分支包含一个生成器和一个判别器，判别器由四个时空先验学习块（SPLB）组成。自监督分支则利用3D一致性投影损失来优化深度估计结果，并保持3D结构的一致性。两个分支协同工作，共同提高夜间深度估计的性能。

**关键创新**：论文的关键创新在于提出了时空先验学习块（SPLB），它能够有效地提取白天场景的时空特征。SPLB包含一个基于空间的时序学习模块（STLM）和一个轴向空间学习模块（ASLM）。STLM利用正交差分提取时间轴上的运动信息，ASLM利用局部非对称卷积和全局轴向注意力捕获多尺度结构信息。这种时空特征提取方法能够有效地恢复无纹理区域和估计模糊区域。

**关键设计**：在对抗分支中，判别器由四个SPLB组成，每个SPLB都包含STLM和ASLM。STLM使用正交差分来提取运动信息，ASLM使用局部非对称卷积和全局轴向注意力来捕获多尺度结构信息。在自监督分支中，使用3D一致性投影损失来优化深度估计结果。该损失函数将目标帧和源帧投影到共享的3D空间中，并计算两个投影帧之间的3D差异。通过最小化该差异，可以提高深度估计的准确性和鲁棒性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14536/fig9-mask.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14536/fig3-tmp4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14536/fig2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DASP在Oxford RobotCar和nuScenes数据集上进行了广泛的实验，结果表明其在夜间深度估计任务上取得了state-of-the-art的性能。相较于现有方法，DASP能够更准确地估计夜间场景的深度信息，尤其是在纹理缺失和动态模糊的区域。消融实验验证了SPLB、STLM、ASLM以及3D一致性投影损失的有效性。

## 🎯 应用场景

该研究成果可应用于自动驾驶、机器人导航、智能监控等领域，尤其是在夜间或低光照环境下的应用。更准确的深度估计能够提高自动驾驶车辆在夜间的感知能力，增强机器人在复杂环境中的导航能力，并提升智能监控系统的目标检测和跟踪性能。该研究对提升夜间视觉系统的可靠性和安全性具有重要意义。

## 📄 摘要（原文）

> Self-supervised monocular depth estimation has achieved notable success under daytime conditions. However, its performance deteriorates markedly at night due to low visibility and varying illumination, e.g., insufficient light causes textureless areas, and moving objects bring blurry regions. To this end, we propose a self-supervised framework named DASP that leverages spatiotemporal priors for nighttime depth estimation. Specifically, DASP consists of an adversarial branch for extracting spatiotemporal priors and a self-supervised branch for learning. In the adversarial branch, we first design an adversarial network where the discriminator is composed of four devised spatiotemporal priors learning blocks (SPLB) to exploit the daytime priors. In particular, the SPLB contains a spatial-based temporal learning module (STLM) that uses orthogonal differencing to extract motion-related variations along the time axis and an axial spatial learning module (ASLM) that adopts local asymmetric convolutions with global axial attention to capture the multiscale structural information. By combining STLM and ASLM, our model can acquire sufficient spatiotemporal features to restore textureless areas and estimate the blurry regions caused by dynamic objects. In the self-supervised branch, we propose a 3D consistency projection loss to bilaterally project the target frame and source frame into a shared 3D space, and calculate the 3D discrepancy between the two projected frames as a loss to optimize the 3D structural consistency and daytime priors. Extensive experiments on the Oxford RobotCar and nuScenes datasets demonstrate that our approach achieves state-of-the-art performance for nighttime depth estimation. Ablation studies further validate the effectiveness of each component.

