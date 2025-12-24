---
layout: default
title: "Surg-InvNeRF: Invertible NeRF for 3D tracking and reconstruction in surgical vision"
---

# Surg-InvNeRF: Invertible NeRF for 3D tracking and reconstruction in surgical vision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09681" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09681v1</a>
  <a href="https://arxiv.org/pdf/2508.09681.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09681v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09681v1', 'Surg-InvNeRF: Invertible NeRF for 3D tracking and reconstruction in surgical vision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gerardo Loza, Junlei Hu, Dominic Jones, Sharib Ali, Pietro Valdastri

**分类**: cs.CV, cs.AI, cs.RO

**发布日期**: 2025-08-13

**备注**: 10 pages

---

## 💡 一句话要点

**提出Invertible NeRF以解决外科视觉中的3D跟踪与重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D点跟踪` `可逆神经辐射场` `外科视觉` `测试时优化` `多尺度HexPlanes` `像素重投影` `渲染方法` `深度学习`

## 📋 核心要点

1. 现有的点跟踪方法在获取一致的运动信息时存在困难，且大多数方法仅限于2D运动，无法满足外科视觉的需求。
2. 我们提出了一种基于可逆神经辐射场（InvNeRF）的测试时优化方法，能够同时进行2D和3D点跟踪，利用渲染方法的优势。
3. 在STIR和SCARE数据集上进行的实验表明，我们的方法在2D点跟踪中精度提高近50%，在3D点跟踪中首次结合了可变形重建的优势。

## 📝 摘要（中文）

我们提出了一种新颖的测试时优化（TTO）方法，基于NeRF架构实现长期3D点跟踪。现有的点跟踪方法在获取一致运动方面存在困难，或仅限于2D运动。我们的TTO方法通过参数化一个函数，利用新的可逆神经辐射场（InvNeRF）架构，能够在外科场景中同时进行2D和3D跟踪。该方法通过监督像素对应关系的重投影，利用渲染方法的优势，并采用双向可变形标准映射来高效处理定义的工作空间。实验结果表明，在STIR和SCARE数据集上，我们的2D点跟踪精度比现有TTO方法提高近50%，而3D点跟踪则首次结合了可变形NeRF重建的优势。

## 🔬 方法详解

**问题定义**：本研究旨在解决外科视觉中的长期3D点跟踪问题。现有方法在运动一致性和2D/3D跟踪能力上存在明显不足，无法有效应用于复杂的外科场景。

**核心思路**：我们提出了一种新的测试时优化（TTO）方法，通过引入可逆神经辐射场（InvNeRF）架构，能够在外科场景中实现高效的2D和3D点跟踪。该方法通过优化函数来聚合来自其他先进方法的对应关系，从而提高跟踪的准确性和一致性。

**技术框架**：整体架构包括多个模块，首先通过InvNeRF进行像素重投影，然后利用双向可变形标准映射来处理工作空间，最后通过多尺度HexPlanes实现快速推理和高效采样。

**关键创新**：本研究的主要创新在于引入可逆神经辐射场（InvNeRF），使得TTO方法能够同时处理2D和3D跟踪，并有效利用渲染方法的优势，显著提高了跟踪精度。

**关键设计**：在网络结构上，我们设计了多尺度HexPlanes以加速推理，并提出了一种新的像素采样和收敛标准算法，以提高整体效率和准确性。具体的损失函数和参数设置也经过精心调整，以确保最佳性能。

## 📊 实验亮点

在STIR和SCARE数据集上的实验结果显示，我们的方法在2D点跟踪中比现有TTO方法的平均精度提高近50%，在3D点跟踪中首次实现了结合可变形NeRF重建的优势，超越了传统的前馈方法。

## 🎯 应用场景

该研究在外科手术视觉系统中具有重要的应用潜力，能够提升手术过程中的实时3D跟踪与重建能力，进而提高手术的安全性和有效性。未来，该技术还可扩展到其他需要高精度3D跟踪的领域，如机器人导航和增强现实等。

## 📄 摘要（原文）

> We proposed a novel test-time optimisation (TTO) approach framed by a NeRF-based architecture for long-term 3D point tracking. Most current methods in point tracking struggle to obtain consistent motion or are limited to 2D motion. TTO approaches frame the solution for long-term tracking as optimising a function that aggregates correspondences from other specialised state-of-the-art methods. Unlike the state-of-the-art on TTO, we propose parametrising such a function with our new invertible Neural Radiance Field (InvNeRF) architecture to perform both 2D and 3D tracking in surgical scenarios. Our approach allows us to exploit the advantages of a rendering-based approach by supervising the reprojection of pixel correspondences. It adapts strategies from recent rendering-based methods to obtain a bidirectional deformable-canonical mapping, to efficiently handle a defined workspace, and to guide the rays' density. It also presents our multi-scale HexPlanes for fast inference and a new algorithm for efficient pixel sampling and convergence criteria. We present results in the STIR and SCARE datasets, for evaluating point tracking and testing the integration of kinematic data in our pipeline, respectively. In 2D point tracking, our approach surpasses the precision and accuracy of the TTO state-of-the-art methods by nearly 50% on average precision, while competing with other approaches. In 3D point tracking, this is the first TTO approach, surpassing feed-forward methods while incorporating the benefits of a deformable NeRF-based reconstruction.

