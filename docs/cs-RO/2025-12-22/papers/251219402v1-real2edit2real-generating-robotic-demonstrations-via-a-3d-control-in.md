---
layout: default
title: "Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface"
---

# Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19402" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19402v1</a>
  <a href="https://arxiv.org/pdf/2512.19402.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19402v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19402v1', 'Real2Edit2Real: Generating Robotic Demonstrations via a 3D Control Interface')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yujie Zhao, Hongwei Fan, Di Chen, Shengcong Chen, Liliang Chen, Xiaoqi Li, Guanghui Ren, Hao Dong

**分类**: cs.RO, cs.CV, cs.GR

**发布日期**: 2025-12-22

---

## 💡 一句话要点

**Real2Edit2Real：通过3D控制界面生成机器人操作演示数据，提升数据效率。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人学习` `数据增强` `3D重建` `视频生成` `操作任务`

## 📋 核心要点

1. 机器人学习依赖大规模数据集，但收集多样化的操作演示数据成本高昂，限制了策略的鲁棒性。
2. Real2Edit2Real框架通过3D控制界面，利用3D编辑和多条件视频生成，从少量真实数据生成大量增强数据。
3. 实验表明，使用该框架生成的数据训练的策略，在数据效率上比使用真实数据训练的策略提升了10-50倍。

## 📝 摘要（中文）

为了减少机器人学习中重复的数据收集，特别是操作任务中的空间泛化问题，本文提出了Real2Edit2Real框架，该框架通过3D可编辑性与2D视觉数据桥接，利用3D控制界面生成新的演示数据。该方法首先使用度量尺度的3D重建模型从多视角RGB观测中重建场景几何。基于重建的几何体，对点云进行深度可靠的3D编辑，生成新的操作轨迹，同时几何校正机器人姿态以恢复物理一致的深度，作为合成新演示的可靠条件。最后，提出了一个以深度为主要控制信号，结合动作、边缘和射线图的多条件视频生成模型，以合成空间增强的多视角操作视频。在四个真实操作任务上的实验表明，仅用1-5个源演示数据生成的训练数据，可以匹配甚至超过用50个真实演示数据训练的策略，数据效率提高了10-50倍。此外，高度和纹理编辑的实验结果证明了该框架的灵活性和可扩展性，表明其有潜力作为统一的数据生成框架。

## 🔬 方法详解

**问题定义**：现有机器人学习方法依赖大量真实演示数据，尤其是在操作任务中，收集具有空间泛化能力的演示数据成本很高。这限制了策略的鲁棒性和泛化能力。因此，如何利用少量真实数据生成高质量的增强数据，是本论文要解决的核心问题。

**核心思路**：论文的核心思路是通过3D可编辑性将2D视觉数据与3D控制界面连接起来，从而实现对机器人操作轨迹的编辑和生成。通过在3D空间中编辑场景几何和机器人姿态，可以生成新的、物理上合理的轨迹，并利用这些轨迹合成新的视觉演示数据。这种方法避免了直接在像素空间进行编辑，从而保证了生成数据的物理一致性。

**技术框架**：Real2Edit2Real框架包含以下几个主要模块：1) **3D重建模块**：从多视角RGB图像重建场景的3D几何结构，得到度量尺度的点云模型。2) **3D编辑模块**：在重建的点云上进行深度可靠的3D编辑，包括改变物体的位置、形状等，并相应地调整机器人姿态，以保证物理一致性。3) **多条件视频生成模块**：基于编辑后的3D场景和机器人姿态，生成新的多视角操作视频。该模块以深度图为主要控制信号，同时结合动作、边缘和射线图等信息，生成高质量的视频。

**关键创新**：该论文的关键创新在于将3D编辑引入到机器人演示数据的生成过程中。与传统的基于图像的增强方法不同，该方法在3D空间中进行编辑，可以更好地保证生成数据的物理合理性。此外，论文提出的多条件视频生成模型，能够有效地利用深度信息和其他辅助信息，生成高质量的多视角视频。

**关键设计**：在3D编辑模块中，论文采用了深度可靠的编辑方法，即在编辑过程中始终保持深度信息的物理一致性。在多条件视频生成模块中，论文使用了深度图作为主要控制信号，并结合动作、边缘和射线图等信息，以提高生成视频的质量。具体的网络结构和损失函数细节在论文中有详细描述，但摘要中未明确提及。

## 📊 实验亮点

实验结果表明，使用Real2Edit2Real框架生成的数据训练的机器人策略，在四个真实操作任务上，仅使用1-5个真实演示数据，就能达到甚至超过使用50个真实演示数据训练的策略的性能。数据效率提升了10-50倍，显著降低了数据收集成本。

## 🎯 应用场景

该研究成果可应用于各种机器人操作任务的数据增强，例如装配、抓取、放置等。通过少量真实数据即可生成大量训练数据，降低了机器人学习的成本，加速了机器人技术的落地。该框架还具有一定的通用性，可以扩展到其他需要数据增强的领域，例如虚拟现实、游戏等。

## 📄 摘要（原文）

> Recent progress in robot learning has been driven by large-scale datasets and powerful visuomotor policy architectures, yet policy robustness remains limited by the substantial cost of collecting diverse demonstrations, particularly for spatial generalization in manipulation tasks. To reduce repetitive data collection, we present Real2Edit2Real, a framework that generates new demonstrations by bridging 3D editability with 2D visual data through a 3D control interface. Our approach first reconstructs scene geometry from multi-view RGB observations with a metric-scale 3D reconstruction model. Based on the reconstructed geometry, we perform depth-reliable 3D editing on point clouds to generate new manipulation trajectories while geometrically correcting the robot poses to recover physically consistent depth, which serves as a reliable condition for synthesizing new demonstrations. Finally, we propose a multi-conditional video generation model guided by depth as the primary control signal, together with action, edge, and ray maps, to synthesize spatially augmented multi-view manipulation videos. Experiments on four real-world manipulation tasks demonstrate that policies trained on data generated from only 1-5 source demonstrations can match or outperform those trained on 50 real-world demonstrations, improving data efficiency by up to 10-50x. Moreover, experimental results on height and texture editing demonstrate the framework's flexibility and extensibility, indicating its potential to serve as a unified data generation framework.

