---
layout: default
title: "MonoPartNeRF:Human Reconstruction from Monocular Video via Part-Based Neural Radiance Fields"
---

# MonoPartNeRF:Human Reconstruction from Monocular Video via Part-Based Neural Radiance Fields

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08798" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08798v1</a>
  <a href="https://arxiv.org/pdf/2508.08798.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08798v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08798v1', 'MonoPartNeRF:Human Reconstruction from Monocular Video via Part-Based Neural Radiance Fields')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Lu, Jiawei Li, Ming Jiang

**分类**: cs.CV

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出MonoPartNeRF以解决单目视频中人类重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态人类重建` `神经辐射场` `单目视频` `姿态嵌入` `遮挡恢复` `纹理建模` `计算机视觉`

## 📋 核心要点

1. 现有方法在复杂姿态变化下常导致部件边界处的不自然过渡，且无法准确重建被遮挡区域。
2. 提出MonoPartNeRF框架，通过双向变形模型和部分姿态嵌入机制来解决动态人类渲染中的挑战。
3. 在ZJU-MoCap和MonoCap数据集上的实验表明，该方法在关节对齐和纹理保真度上显著优于现有方法。

## 📝 摘要（中文）

近年来，神经辐射场（NeRF）在动态人类重建和渲染方面取得了显著进展。基于部分的渲染范式通过人体分割引导灵活的参数分配，提升了表示效率。然而，现有方法在复杂姿态变化下仍存在困难，常导致部件边界处的不自然过渡，并且在单目设置中无法准确重建被遮挡区域。我们提出了MonoPartNeRF，一个新颖的单目动态人类渲染框架，确保平滑过渡和强大的遮挡恢复。通过建立双向变形模型，结合刚性和非刚性变换，构建观察空间与典型空间之间的连续可逆映射。实验结果表明，我们的方法在复杂姿态和遮挡条件下显著优于先前的方法，达到了更好的关节对齐、纹理保真度和结构连续性。

## 🔬 方法详解

**问题定义**：本论文旨在解决单目视频中动态人类重建的挑战，现有方法在复杂姿态和遮挡情况下表现不佳，导致重建结果不自然且缺乏准确性。

**核心思路**：提出MonoPartNeRF框架，通过结合刚性和非刚性变换的双向变形模型，建立观察空间与典型空间之间的连续可逆映射，以改善姿态变化和遮挡恢复的效果。

**技术框架**：整体架构包括双向变形模型、部分姿态嵌入机制和可学习的外观编码。首先，通过变形模型处理输入数据，然后利用姿态嵌入进行特征采样，最后通过外观编码实现动态纹理变化的建模。

**关键创新**：最重要的创新在于引入了双向变形模型和部分姿态嵌入机制，这使得模型能够更好地处理复杂的姿态变化和遮挡问题，显著提升了重建效果。

**关键设计**：在损失函数设计上，采用了一致性损失来抑制变形引起的伪影和不连续性，同时在姿态嵌入中采用了基于身体区域的局部关节嵌入，以增强特征的姿态感知能力。整体网络结构经过优化，以适应动态人类的重建需求。

## 📊 实验亮点

实验结果显示，MonoPartNeRF在ZJU-MoCap和MonoCap数据集上显著优于现有方法，关节对齐精度提升了XX%，纹理保真度提高了YY%，在复杂姿态和遮挡条件下表现出色，验证了其有效性和鲁棒性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在虚拟现实、增强现实和动画制作等领域。通过实现高质量的人类重建，MonoPartNeRF能够为游戏开发、影视特效和人机交互提供更为真实的视觉体验，推动相关技术的发展与应用。

## 📄 摘要（原文）

> In recent years, Neural Radiance Fields (NeRF) have achieved remarkable progress in dynamic human reconstruction and rendering. Part-based rendering paradigms, guided by human segmentation, allow for flexible parameter allocation based on structural complexity, thereby enhancing representational efficiency. However, existing methods still struggle with complex pose variations, often producing unnatural transitions at part boundaries and failing to reconstruct occluded regions accurately in monocular settings. We propose MonoPartNeRF, a novel framework for monocular dynamic human rendering that ensures smooth transitions and robust occlusion recovery. First, we build a bidirectional deformation model that combines rigid and non-rigid transformations to establish a continuous, reversible mapping between observation and canonical spaces. Sampling points are projected into a parameterized surface-time space (u, v, t) to better capture non-rigid motion. A consistency loss further suppresses deformation-induced artifacts and discontinuities. We introduce a part-based pose embedding mechanism that decomposes global pose vectors into local joint embeddings based on body regions. This is combined with keyframe pose retrieval and interpolation, along three orthogonal directions, to guide pose-aware feature sampling. A learnable appearance code is integrated via attention to model dynamic texture changes effectively. Experiments on the ZJU-MoCap and MonoCap datasets demonstrate that our method significantly outperforms prior approaches under complex pose and occlusion conditions, achieving superior joint alignment, texture fidelity, and structural continuity.

