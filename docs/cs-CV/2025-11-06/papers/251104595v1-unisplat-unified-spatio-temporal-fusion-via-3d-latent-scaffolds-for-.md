---
layout: default
title: UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction
---

# UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04595" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04595v1</a>
  <a href="https://arxiv.org/pdf/2511.04595.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04595v1" onclick="toggleFavorite(this, '2511.04595v1', 'UniSplat: Unified Spatio-Temporal Fusion via 3D Latent Scaffolds for Dynamic Driving Scene Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Shi, Shaoshuai Shi, Xiaoyang Lyu, Chunyang Liu, Kehua Sheng, Bo Zhang, Li Jiang

**分类**: cs.CV

**发布日期**: 2025-11-06

---

## 💡 一句话要点

**UniSplat：通过3D潜在支架实现动态驾驶场景的统一时空融合重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `动态场景重建` `时空融合` `3D潜在支架` `自动驾驶` `新视角合成`

## 📋 核心要点

1. 现有自动驾驶场景重建方法难以应对稀疏、非重叠相机视角和复杂场景动态的联合挑战。
2. UniSplat通过构建3D潜在支架，并在此支架上进行时空信息融合，实现鲁棒的动态场景重建。
3. 实验表明，UniSplat在新视角合成方面达到了SOTA性能，即使在原始相机覆盖范围之外也能提供高质量渲染。

## 📝 摘要（中文）

本文提出UniSplat，一个通用的前馈框架，通过统一的潜在时空融合学习鲁棒的动态场景重建。UniSplat构建了一个3D潜在支架，利用预训练的基础模型捕获几何和语义场景上下文。为了有效地整合跨空间视角和时间帧的信息，引入了一种高效的融合机制，该机制直接在3D支架内运行，从而实现一致的时空对齐。为了确保完整和详细的重建，设计了一个双分支解码器，通过结合点锚定细化和基于体素的生成，从融合的支架中生成动态感知高斯分布，并保持静态高斯分布的持久记忆，以实现超出当前相机覆盖范围的流式场景补全。在真实世界数据集上的大量实验表明，UniSplat在新的视角合成方面实现了最先进的性能，同时即使对于原始相机覆盖范围之外的视角，也能提供鲁棒和高质量的渲染。

## 🔬 方法详解

**问题定义**：现有方法在自动驾驶场景重建中，难以有效处理来自稀疏、非重叠相机视角的动态场景信息，导致重建质量下降，尤其是在新视角合成时表现不佳。这些方法通常难以捕捉场景的完整几何和语义信息，并且缺乏有效的时空一致性建模能力。

**核心思路**：UniSplat的核心思路是构建一个3D潜在支架，作为场景的统一表示，并在此支架上进行时空信息的融合。通过利用预训练的基础模型，该支架能够捕获丰富的几何和语义上下文。直接在3D支架内进行融合，可以实现更有效的时空对齐，从而提高重建的鲁棒性和质量。

**技术框架**：UniSplat的整体框架包含以下几个主要模块：1) 3D潜在支架构建模块，利用预训练模型提取特征并构建3D场景表示；2) 时空融合模块，在3D支架内进行跨视角和跨时间的信息融合；3) 双分支解码器，从融合的支架中生成动态感知高斯分布，用于场景重建；4) 静态高斯记忆模块，用于维护静态场景信息，实现流式场景补全。

**关键创新**：UniSplat的关键创新在于其统一的时空融合机制，该机制直接在3D潜在支架内运行，能够有效地整合来自不同视角和时间帧的信息，从而实现更鲁棒和一致的场景重建。此外，双分支解码器和静态高斯记忆模块的设计，进一步提高了重建的质量和完整性。

**关键设计**：UniSplat使用预训练的视觉基础模型来初始化3D潜在支架，从而获得丰富的先验知识。时空融合模块采用注意力机制，自适应地融合来自不同视角和时间帧的特征。双分支解码器包含一个点锚定细化分支和一个基于体素的生成分支，分别用于提高重建的精度和完整性。静态高斯记忆模块采用滑动窗口机制，维护静态场景信息的持久性。

## 📊 实验亮点

UniSplat在真实世界数据集上取得了显著的性能提升，尤其是在新视角合成方面。实验结果表明，UniSplat在多个指标上均优于现有方法，能够生成更清晰、更完整的场景重建结果，即使对于原始相机覆盖范围之外的视角，也能提供高质量的渲染效果。具体的性能数据和对比基线信息需要在论文中查找。

## 🎯 应用场景

UniSplat在自动驾驶领域具有广泛的应用前景，可以用于高精地图构建、自动驾驶感知、虚拟现实场景生成等。该研究成果有助于提高自动驾驶系统的环境感知能力和安全性，并为虚拟现实应用提供更逼真的场景体验。未来，该技术还可以扩展到其他需要动态场景重建的领域，如机器人导航、增强现实等。

## 📄 摘要（原文）

> Feed-forward 3D reconstruction for autonomous driving has advanced rapidly, yet existing methods struggle with the joint challenges of sparse, non-overlapping camera views and complex scene dynamics. We present UniSplat, a general feed-forward framework that learns robust dynamic scene reconstruction through unified latent spatio-temporal fusion. UniSplat constructs a 3D latent scaffold, a structured representation that captures geometric and semantic scene context by leveraging pretrained foundation models. To effectively integrate information across spatial views and temporal frames, we introduce an efficient fusion mechanism that operates directly within the 3D scaffold, enabling consistent spatio-temporal alignment. To ensure complete and detailed reconstructions, we design a dual-branch decoder that generates dynamic-aware Gaussians from the fused scaffold by combining point-anchored refinement with voxel-based generation, and maintain a persistent memory of static Gaussians to enable streaming scene completion beyond current camera coverage. Extensive experiments on real-world datasets demonstrate that UniSplat achieves state-of-the-art performance in novel view synthesis, while providing robust and high-quality renderings even for viewpoints outside the original camera coverage.

