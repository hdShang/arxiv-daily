---
layout: default
title: "DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors"
---

# DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14536" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14536v1</a>
  <a href="https://arxiv.org/pdf/2512.14536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14536v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14536v1', 'DASP: Self-supervised Nighttime Monocular Depth Estimation with Domain Adaptation of Spatiotemporal Priors')" title="添加到收藏夹">☆ 收藏</button>
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

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `夜间深度估计` `自监督学习` `时空先验` `域适应` `对抗学习` `单目视觉` `深度学习`

## 📋 核心要点

1. 夜间场景光照不足、纹理缺失以及运动模糊等问题，导致现有自监督单目深度估计方法性能显著下降。
2. DASP框架利用对抗分支提取白天场景的时空先验知识，并将其迁移到夜间场景的深度估计中，从而提升性能。
3. 实验结果表明，DASP在夜间深度估计任务上取得了state-of-the-art的性能，并且消融实验验证了各个模块的有效性。

## 📝 摘要（中文）

本文提出了一种名为DASP的自监督框架，利用时空先验进行夜间深度估计。DASP包含一个用于提取时空先验的对抗分支和一个用于学习的自监督分支。在对抗分支中，设计了一个对抗网络，其判别器由四个设计的时空先验学习块(SPLB)组成，以利用白天先验。SPLB包含一个基于空间的时序学习模块(STLM)，该模块使用正交差分来提取沿时间轴的运动相关变化，以及一个轴向空间学习模块(ASLM)，该模块采用具有全局轴向注意力的局部非对称卷积来捕获多尺度结构信息。通过结合STLM和ASLM，该模型可以获得足够的时空特征来恢复无纹理区域并估计由动态对象引起的模糊区域。在自监督分支中，提出了一个3D一致性投影损失，以双边地将目标帧和源帧投影到共享的3D空间中，并计算两个投影帧之间的3D差异作为损失，以优化3D结构一致性和白天先验。在Oxford RobotCar和nuScenes数据集上的大量实验表明，该方法在夜间深度估计方面取得了最先进的性能。消融研究进一步验证了每个组件的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决夜间单目深度估计问题。现有自监督方法在白天表现良好，但在夜间由于光照不足、纹理缺失和运动模糊等因素，性能显著下降。这些因素导致深度估计的准确性和鲁棒性降低。

**核心思路**：论文的核心思路是利用白天场景的时空先验知识来指导夜间场景的深度估计。通过对抗学习，将白天场景中学习到的运动模式和结构信息迁移到夜间场景，从而弥补夜间场景的不足。

**技术框架**：DASP框架包含两个主要分支：对抗分支和自监督分支。对抗分支负责提取白天场景的时空先验，并将其传递给自监督分支。自监督分支则利用这些先验知识进行夜间深度估计。对抗分支包含一个生成器和一个判别器，判别器由多个时空先验学习块（SPLB）组成。自监督分支使用3D一致性投影损失来优化深度估计结果。

**关键创新**：论文的关键创新在于提出了时空先验学习块（SPLB），它能够有效地提取白天场景中的时空特征。SPLB包含一个基于空间的时序学习模块（STLM）和一个轴向空间学习模块（ASLM）。STLM通过正交差分提取运动相关信息，ASLM通过非对称卷积和轴向注意力捕获多尺度结构信息。

**关键设计**：判别器由四个SPLB组成，每个SPLB都包含STLM和ASLM。STLM使用正交差分来提取时间轴上的运动变化。ASLM采用局部非对称卷积和全局轴向注意力来捕获多尺度结构信息。自监督分支使用3D一致性投影损失，该损失通过将目标帧和源帧投影到共享的3D空间中，并计算它们之间的差异来优化深度估计。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14536v1/fig9-mask.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14536v1/fig3-tmp4.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14536v1/fig2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DASP在Oxford RobotCar和nuScenes数据集上进行了评估，实验结果表明，DASP在夜间深度估计方面取得了state-of-the-art的性能。相较于现有方法，DASP能够更准确地估计夜间场景的深度信息，尤其是在纹理缺失和运动模糊的区域。消融实验验证了SPLB、STLM、ASLM以及3D一致性投影损失的有效性。

## 🎯 应用场景

该研究成果可应用于夜间自动驾驶、夜间监控、夜间机器人导航等领域。通过提高夜间深度估计的准确性和鲁棒性，可以提升这些应用在低光照环境下的性能和安全性。未来，该技术还可以扩展到其他夜间视觉任务，如夜间目标检测和夜间场景理解。

## 📄 摘要（原文）

> Self-supervised monocular depth estimation has achieved notable success under daytime conditions. However, its performance deteriorates markedly at night due to low visibility and varying illumination, e.g., insufficient light causes textureless areas, and moving objects bring blurry regions. To this end, we propose a self-supervised framework named DASP that leverages spatiotemporal priors for nighttime depth estimation. Specifically, DASP consists of an adversarial branch for extracting spatiotemporal priors and a self-supervised branch for learning. In the adversarial branch, we first design an adversarial network where the discriminator is composed of four devised spatiotemporal priors learning blocks (SPLB) to exploit the daytime priors. In particular, the SPLB contains a spatial-based temporal learning module (STLM) that uses orthogonal differencing to extract motion-related variations along the time axis and an axial spatial learning module (ASLM) that adopts local asymmetric convolutions with global axial attention to capture the multiscale structural information. By combining STLM and ASLM, our model can acquire sufficient spatiotemporal features to restore textureless areas and estimate the blurry regions caused by dynamic objects. In the self-supervised branch, we propose a 3D consistency projection loss to bilaterally project the target frame and source frame into a shared 3D space, and calculate the 3D discrepancy between the two projected frames as a loss to optimize the 3D structural consistency and daytime priors. Extensive experiments on the Oxford RobotCar and nuScenes datasets demonstrate that our approach achieves state-of-the-art performance for nighttime depth estimation. Ablation studies further validate the effectiveness of each component.

