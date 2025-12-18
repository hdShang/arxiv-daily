---
layout: default
title: LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving
---

# LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.16049" class="toolbar-btn" target="_blank">📄 arXiv: 2511.16049v1</a>
  <a href="https://arxiv.org/pdf/2511.16049.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.16049v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.16049v1', 'LiSTAR: Ray-Centric World Models for 4D LiDAR Sequences in Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pei Liu, Songtao Wang, Lang Zhang, Xingyue Peng, Yuandong Lyu, Jiaxin Deng, Songxin Lu, Weiliang Ma, Xueyang Zhang, Yifei Zhan, XianPeng Lang, Jun Ma

**分类**: cs.CV

**发布日期**: 2025-11-20

**🔗 代码/项目**: [PROJECT_PAGE](https://ocean-luna.github.io/LiSTAR.gitub.io)

---

## 💡 一句话要点

**LiSTAR：面向自动驾驶，提出基于射线中心世界模型的4D激光雷达序列生成方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自动驾驶` `激光雷达` `4D数据生成` `世界模型` `时空建模`

## 📋 核心要点

1. 现有方法难以在自动驾驶仿真中生成高保真、可控的4D激光雷达数据，主要挑战在于传感器几何特性、点云时序稀疏性和动态场景复杂性。
2. LiSTAR提出一种基于射线中心的世界模型，利用混合柱面-球面表示和时空注意力机制，直接在传感器原生几何结构上进行数据生成。
3. 实验表明，LiSTAR在4D激光雷达重建、预测和条件生成任务上显著优于现有方法，例如生成MMD降低76%，重建IoU提高32%。

## 📝 摘要（中文）

本文提出LiSTAR，一种新颖的生成式世界模型，直接在传感器的原生几何结构上运行，用于合成高保真且可控的4D激光雷达数据，以创建可扩展的自动驾驶仿真环境。LiSTAR引入混合柱面-球面（HCS）表示，通过减轻笛卡尔网格中常见的量化伪影来保持数据保真度。为了从稀疏的时间数据中捕获复杂的动态，它利用了具有射线中心Transformer的时空注意力（START），该注意力显式地对沿着各个传感器射线的特征演化进行建模，以实现鲁棒的时间一致性。此外，为了实现可控合成，我们提出了一种新颖的4D点云对齐体素布局用于条件控制，以及相应的离散掩码生成START（MaskSTART）框架，该框架学习场景的紧凑、token化的表示，从而实现高效、高分辨率和布局引导的组合生成。综合实验验证了LiSTAR在4D激光雷达重建、预测和条件生成方面的最先进性能，并取得了显著的定量收益：生成MMD降低了76%，重建IoU提高了32%，预测L1 Med降低了50%。这种性能水平为创建逼真且可控的自动驾驶系统仿真提供了一个强大的新基础。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶仿真环境中4D激光雷达数据生成的问题。现有方法在处理激光雷达数据的特殊几何结构（球形）、时序稀疏性以及复杂动态场景时存在不足，导致生成的数据保真度不高，难以控制。这些问题限制了自动驾驶仿真环境的可扩展性和真实性。

**核心思路**：LiSTAR的核心思路是直接在激光雷达传感器的原生几何结构上进行数据建模和生成，避免了传统方法中将数据转换为笛卡尔坐标系而引入的量化误差。通过设计混合柱面-球面（HCS）表示，更好地保留了原始数据的空间信息。同时，利用射线中心Transformer来建模时序信息，从而更好地捕捉动态场景的变化。

**技术框架**：LiSTAR的整体框架包含以下几个主要模块：1) 混合柱面-球面（HCS）表示：将激光雷达数据转换为HCS格式，以保留原始几何信息。2) 具有射线中心Transformer的时空注意力（START）：利用Transformer结构建模时序信息，并引入射线中心注意力机制，关注每个射线上的特征演化。3) 4D点云对齐体素布局：用于条件控制，允许用户指定场景的布局。4) 离散掩码生成START（MaskSTART）：学习场景的token化表示，用于高效、高分辨率的生成。

**关键创新**：LiSTAR的关键创新在于：1) 混合柱面-球面（HCS）表示，更适合激光雷达数据的几何特性。2) 射线中心Transformer，能够更好地建模时序信息。3) 4D点云对齐体素布局和MaskSTART框架，实现了可控的场景生成。这些创新使得LiSTAR能够生成更高质量、更可控的4D激光雷达数据。

**关键设计**：HCS表示的具体实现方式是将空间划分为柱面和球面两部分，并根据激光雷达的扫描方式进行离散化。START模块中的射线中心注意力机制通过计算每个射线上的特征之间的相关性来建模时序信息。MaskSTART框架使用离散的token来表示场景，并通过Transformer学习这些token之间的关系。损失函数包括重建损失、对抗损失等，用于提高生成数据的质量。

## 📊 实验亮点

实验结果表明，LiSTAR在4D激光雷达重建、预测和条件生成任务上取得了显著的性能提升。在生成任务中，LiSTAR将MMD指标降低了76%，表明生成的数据分布更接近真实数据。在重建任务中，LiSTAR将IoU指标提高了32%，表明重建的点云更准确。在预测任务中，LiSTAR将L1 Med指标降低了50%，表明预测结果更精确。这些数据充分验证了LiSTAR的优越性。

## 🎯 应用场景

LiSTAR的研究成果可广泛应用于自动驾驶仿真、算法验证和数据增强等领域。通过生成逼真且可控的4D激光雷达数据，可以构建更可靠的自动驾驶仿真环境，加速算法的开发和测试。此外，LiSTAR还可以用于生成合成数据，扩充训练数据集，提高自动驾驶系统的鲁棒性和泛化能力。该研究对于推动自动驾驶技术的发展具有重要意义。

## 📄 摘要（原文）

> Synthesizing high-fidelity and controllable 4D LiDAR data is crucial for creating scalable simulation environments for autonomous driving. This task is inherently challenging due to the sensor's unique spherical geometry, the temporal sparsity of point clouds, and the complexity of dynamic scenes. To address these challenges, we present LiSTAR, a novel generative world model that operates directly on the sensor's native geometry. LiSTAR introduces a Hybrid-Cylindrical-Spherical (HCS) representation to preserve data fidelity by mitigating quantization artifacts common in Cartesian grids. To capture complex dynamics from sparse temporal data, it utilizes a Spatio-Temporal Attention with Ray-Centric Transformer (START) that explicitly models feature evolution along individual sensor rays for robust temporal coherence. Furthermore, for controllable synthesis, we propose a novel 4D point cloud-aligned voxel layout for conditioning and a corresponding discrete Masked Generative START (MaskSTART) framework, which learns a compact, tokenized representation of the scene, enabling efficient, high-resolution, and layout-guided compositional generation. Comprehensive experiments validate LiSTAR's state-of-the-art performance across 4D LiDAR reconstruction, prediction, and conditional generation, with substantial quantitative gains: reducing generation MMD by a massive 76%, improving reconstruction IoU by 32%, and lowering prediction L1 Med by 50%. This level of performance provides a powerful new foundation for creating realistic and controllable autonomous systems simulations. Project link: https://ocean-luna.github.io/LiSTAR.gitub.io.

