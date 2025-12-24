---
layout: default
title: "DA$^{2}$: Depth Anything in Any Direction"
---

# DA$^{2}$: Depth Anything in Any Direction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26618" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26618v5</a>
  <a href="https://arxiv.org/pdf/2509.26618.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26618v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26618v5', 'DA$^{2}$: Depth Anything in Any Direction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haodong Li, Wangguangdong Zheng, Jing He, Yuhao Liu, Xin Lin, Xin Yang, Ying-Cong Chen, Chunchao Guo

**分类**: cs.CV

**发布日期**: 2025-09-30 (更新: 2025-11-08)

**备注**: Work primarily done during an internship at Tencent Hunyuan. Project page: https://depth-any-in-any-dir.github.io/

**🔗 代码/项目**: [PROJECT_PAGE](https://depth-any-in-any-dir.github.io/)

---

## 💡 一句话要点

**提出DA²，解决全景深度估计的零样本泛化与效率问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `全景深度估计` `零样本学习` `数据增强` `球形几何` `Transformer`

## 📋 核心要点

1. 现有全景深度估计方法受限于数据稀缺，零样本泛化能力差，且常依赖透视分割导致效率低下。
2. DA²通过数据引擎生成大规模全景深度数据，并提出SphereViT利用球坐标增强几何一致性。
3. 实验表明，DA²在多个数据集上取得SOTA性能，零样本泛化能力甚至超越领域内方法，且效率更高。

## 📝 摘要（中文）

本文提出DA²：一个精确、零样本泛化且完全端到端的全景深度估计器。为了扩展全景数据，我们引入了一个数据管理引擎，用于从透视图像生成高质量的全景深度数据，创建了约54.3万个全景RGB-depth对，总数达到约60.7万个。为了进一步缓解球形失真，我们提出了SphereViT，它显式地利用球坐标来增强全景图像特征中的球形几何一致性，从而提高性能。在多个数据集上的综合基准测试清楚地表明了DA²的SoTA性能，在AbsRel指标上比最强的零样本基线平均提高了38%。令人惊讶的是，DA²甚至优于先前的领域内方法，突出了其卓越的零样本泛化能力。此外，作为一个端到端解决方案，DA²比基于融合的方法表现出更高的效率。代码和整理的全景数据均已发布。

## 🔬 方法详解

**问题定义**：全景深度估计旨在从360°x180°全景图像中预测每个像素的深度值。现有方法受限于全景数据的稀缺性，导致模型在未见过的场景中泛化能力较差。此外，全景图像固有的球形失真使得许多方法需要将全景图分割成多个透视图像（如立方体贴图）进行处理，这降低了计算效率，并且分割操作可能引入额外的误差。

**核心思路**：DA²的核心思路是通过大规模数据增强和显式地建模球形几何结构来提升全景深度估计的零样本泛化能力和效率。通过数据增强，模型可以学习到更丰富的场景信息，从而提高泛化能力。通过SphereViT，模型可以直接在球形坐标系下处理全景图像，避免了透视分割带来的问题。

**技术框架**：DA²包含两个主要组成部分：数据管理引擎和SphereViT。数据管理引擎负责从透视图像生成高质量的全景深度数据，用于训练模型。SphereViT是一个基于ViT的全景深度估计网络，它显式地利用球坐标来增强全景图像特征中的球形几何一致性。整个流程是端到端的，输入全景图像，输出深度图。

**关键创新**：DA²的关键创新在于：1) 提出了一个数据管理引擎，能够高效地生成大规模的全景深度数据，解决了数据稀缺的问题。2) 提出了SphereViT，通过显式地建模球形几何结构，提高了全景深度估计的精度和效率。与现有方法相比，DA²不需要进行透视分割，可以直接在球形坐标系下处理全景图像。

**关键设计**：数据管理引擎使用深度估计模型和图像拼接技术从透视图像生成全景深度数据。SphereViT在ViT的基础上引入了球坐标信息，具体来说，在计算自注意力时，考虑了像素之间的球形距离。损失函数包括深度回归损失和几何一致性损失，用于约束深度估计的准确性和几何一致性。

## 📊 实验亮点

DA²在多个全景深度估计数据集上取得了显著的性能提升。例如，在zero-shot设置下，DA²在AbsRel指标上比最强的基线方法平均提高了38%。更令人惊讶的是，DA²甚至超越了在特定领域数据上训练的模型，证明了其卓越的零样本泛化能力。此外，DA²作为一个端到端解决方案，比基于融合的方法具有更高的效率。

## 🎯 应用场景

DA²可应用于自动驾驶、机器人导航、虚拟现实/增强现实等领域。在自动驾驶中，全景深度估计可以帮助车辆更好地理解周围环境，提高安全性。在机器人导航中，可以帮助机器人进行三维重建和路径规划。在VR/AR中，可以提供更逼真的沉浸式体验。该研究有助于推动三维视觉技术的发展，并为相关应用提供更可靠的基础。

## 📄 摘要（原文）

> Panorama has a full FoV (360$^\circ\times$180$^\circ$), offering a more complete visual description than perspective images. Thanks to this characteristic, panoramic depth estimation is gaining increasing traction in 3D vision. However, due to the scarcity of panoramic data, previous methods are often restricted to in-domain settings, leading to poor zero-shot generalization. Furthermore, due to the spherical distortions inherent in panoramas, many approaches rely on perspective splitting (e.g., cubemaps), which leads to suboptimal efficiency. To address these challenges, we propose $\textbf{DA}$$^{\textbf{2}}$: $\textbf{D}$epth $\textbf{A}$nything in $\textbf{A}$ny $\textbf{D}$irection, an accurate, zero-shot generalizable, and fully end-to-end panoramic depth estimator. Specifically, for scaling up panoramic data, we introduce a data curation engine for generating high-quality panoramic depth data from perspective, and create $\sim$543K panoramic RGB-depth pairs, bringing the total to $\sim$607K. To further mitigate the spherical distortions, we present SphereViT, which explicitly leverages spherical coordinates to enforce the spherical geometric consistency in panoramic image features, yielding improved performance. A comprehensive benchmark on multiple datasets clearly demonstrates DA$^{2}$'s SoTA performance, with an average 38% improvement on AbsRel over the strongest zero-shot baseline. Surprisingly, DA$^{2}$ even outperforms prior in-domain methods, highlighting its superior zero-shot generalization. Moreover, as an end-to-end solution, DA$^{2}$ exhibits much higher efficiency over fusion-based approaches. Both the code and the curated panoramic data has be released. Project page: https://depth-any-in-any-dir.github.io/.

