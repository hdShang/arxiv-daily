---
layout: default
title: "DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos"
---

# DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09997" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09997v1</a>
  <a href="https://arxiv.org/pdf/2506.09997.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09997v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09997v1', 'DGS-LRM: Real-Time Deformable 3D Gaussian Reconstruction From Monocular Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chieh Hubert Lin, Zhaoyang Lv, Songyin Wu, Zhen Xu, Thu Nguyen-Phuoc, Hung-Yu Tseng, Julian Straub, Numair Khan, Lei Xiao, Ming-Hsuan Yang, Yuheng Ren, Richard Newcombe, Zhao Dong, Zhengqin Li

**分类**: cs.GR, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-06-11

**备注**: Project page: https://hubert0527.github.io/dgslrm/

---

## 💡 一句话要点

**提出DGS-LRM以解决动态场景单目视频重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `动态场景重建` `3D高斯表示` `单目视频` `实时处理` `变换器网络`

## 📋 核心要点

1. 现有方法主要局限于静态场景，无法有效处理动态物体的重建，面临训练数据稀缺和3D表示不足等挑战。
2. 论文提出了一种可变形3D高斯表示，结合增强的数据集和大型变换器网络，能够实现实时动态场景重建。
3. 实验结果表明，DGS-LRM在动态场景重建质量上与优化方法相当，且在真实场景中显著优于现有预测动态重建方法。

## 📝 摘要（中文）

我们介绍了可变形高斯斑点大规模重建模型（DGS-LRM），这是首个从单目姿态视频中预测可变形3D高斯斑点的前馈方法。前馈场景重建因其快速创建真实环境数字复制品的能力而受到广泛关注。然而，大多数现有模型仅限于静态场景，无法重建动态物体的运动。为了解决这些挑战，我们提出了几个关键技术贡献：增强的大规模合成数据集，具有真实视角视频和稠密3D场景流监督；每像素可变形3D高斯表示，易于学习，支持高质量动态视图合成和长距离3D跟踪；以及一个大型变换器网络，实现实时、可泛化的动态场景重建。大量定性和定量实验表明，DGS-LRM在动态场景重建质量上可与基于优化的方法相媲美，同时在真实案例中显著超越了最先进的预测动态重建方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决从单目视频中重建动态场景的挑战，现有方法无法处理动态物体的运动，且训练数据稀缺。

**核心思路**：提出可变形3D高斯表示，结合增强的数据集和大型变换器网络，旨在实现高质量的动态场景重建。

**技术框架**：整体架构包括数据预处理、可变形3D高斯表示学习、动态视图合成和长距离3D跟踪，采用前馈方式进行实时重建。

**关键创新**：最重要的技术创新在于引入每像素可变形3D高斯表示，支持高质量动态视图合成，并能适应长距离3D跟踪任务。

**关键设计**：采用增强的大规模合成数据集，设计了适合动态场景的损失函数和网络结构，确保模型在训练过程中能够有效学习动态特征。

## 📊 实验亮点

实验结果显示，DGS-LRM在动态场景重建质量上与基于优化的方法相当，并在真实场景中显著超越了现有的预测动态重建方法，表现出更高的准确性和适应性。具体性能数据表明，DGS-LRM在长距离3D跟踪任务中达到了与最先进的单目视频3D跟踪方法相当的效果。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实、机器人导航和自动驾驶等。通过实现高质量的动态场景重建，DGS-LRM能够为这些领域提供更为真实的环境模拟，提升用户体验和系统性能。未来，该技术有望在实时3D跟踪和动态场景理解方面发挥重要作用。

## 📄 摘要（原文）

> We introduce the Deformable Gaussian Splats Large Reconstruction Model (DGS-LRM), the first feed-forward method predicting deformable 3D Gaussian splats from a monocular posed video of any dynamic scene. Feed-forward scene reconstruction has gained significant attention for its ability to rapidly create digital replicas of real-world environments. However, most existing models are limited to static scenes and fail to reconstruct the motion of moving objects. Developing a feed-forward model for dynamic scene reconstruction poses significant challenges, including the scarcity of training data and the need for appropriate 3D representations and training paradigms. To address these challenges, we introduce several key technical contributions: an enhanced large-scale synthetic dataset with ground-truth multi-view videos and dense 3D scene flow supervision; a per-pixel deformable 3D Gaussian representation that is easy to learn, supports high-quality dynamic view synthesis, and enables long-range 3D tracking; and a large transformer network that achieves real-time, generalizable dynamic scene reconstruction. Extensive qualitative and quantitative experiments demonstrate that DGS-LRM achieves dynamic scene reconstruction quality comparable to optimization-based methods, while significantly outperforming the state-of-the-art predictive dynamic reconstruction method on real-world examples. Its predicted physically grounded 3D deformation is accurate and can readily adapt for long-range 3D tracking tasks, achieving performance on par with state-of-the-art monocular video 3D tracking methods.

