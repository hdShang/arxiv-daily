---
layout: default
title: "O-MaMa: Learning Object Mask Matching between Egocentric and Exocentric Views"
---

# O-MaMa: Learning Object Mask Matching between Egocentric and Exocentric Views

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06026" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06026v2</a>
  <a href="https://arxiv.org/pdf/2506.06026.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06026v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06026v2', 'O-MaMa: Learning Object Mask Matching between Egocentric and Exocentric Views')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lorenzo Mur-Labadia, Maria Santos-Villafranca, Jesus Bermudez-Cameo, Alejandro Perez-Yus, Ruben Martinez-Cantin, Jose J. Guerrero

**分类**: cs.CV

**发布日期**: 2025-06-06 (更新: 2025-09-24)

**备注**: Accepted at ICCV 2025. Code: https://github.com/Maria-SanVil/O-MaMa Project page: https://maria-sanvil.github.io/O-MaMa/

---

## 💡 一句话要点

**提出O-MaMa以解决不同视角下物体分割问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `物体分割` `多视角学习` `掩码匹配` `对比损失` `特征融合`

## 📋 核心要点

1. 现有方法在不同视角下物体分割的准确性和一致性不足，导致智能系统理解环境的能力受限。
2. 本文提出的O-MaMa方法通过掩码匹配任务重定义跨图像分割，结合多视角特征融合与对比损失，提升了物体识别能力。
3. O-MaMa在Ego-Exo4D基准测试中表现优异，相较于基线在IoU指标上实现了显著提升，展示了其有效性。

## 📝 摘要（中文）

理解世界的多视角是智能系统协作的关键，而在不同视角间分割共同物体仍然是一个未解决的问题。本文提出了一种新方法，将跨图像分割重新定义为掩码匹配任务。该方法包括：1) 掩码上下文编码器，利用密集的DINOv2语义特征从FastSAM掩码候选中获取区分性物体级表示；2) 自我与外部交叉注意力，融合多视角观察；3) 掩码匹配对比损失，在共享潜在空间中对齐跨视图特征；4) 硬负样本相邻挖掘策略，鼓励模型更好地区分相邻物体。O-MaMa在Ego-Exo4D对应基准上达到了最先进的水平，在Ego2Exo和Exo2Ego IoU上相较于官方基线分别提升了22%和76%。

## 🔬 方法详解

**问题定义**：本文旨在解决在不同视角下物体分割的挑战，现有方法在处理多视角信息时的准确性和一致性不足，限制了智能系统的环境理解能力。

**核心思路**：O-MaMa通过将跨图像分割问题重新定义为掩码匹配任务，利用多视角观察的特征融合，提升了物体级别的表示能力。

**技术框架**：该方法包括四个主要模块：1) 掩码上下文编码器，2) 自我与外部交叉注意力，3) 掩码匹配对比损失，4) 硬负样本相邻挖掘策略，整体流程通过这些模块实现特征的有效对齐与区分。

**关键创新**：最重要的创新在于将掩码匹配作为核心任务，并引入交叉注意力机制和对比损失，显著提升了跨视图特征的对齐能力，与传统方法相比，能够更好地处理相邻物体的区分。

**关键设计**：在模型设计中，采用了DINOv2语义特征进行特征提取，使用了FastSAM掩码候选，损失函数设计为掩码匹配对比损失，并引入了硬负样本挖掘策略，以增强模型的学习能力。

## 📊 实验亮点

O-MaMa在Ego-Exo4D基准测试中取得了显著的实验结果，在Ego2Exo和Exo2Ego IoU上分别提升了22%和76%，相较于最先进的技术，使用仅1%的训练参数仍实现了13%和6%的提升，展示了其高效性与优越性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人视觉、增强现实和自动驾驶等场景，能够帮助智能系统更好地理解和互动于复杂环境。通过提升不同视角下的物体识别能力，O-MaMa有望在多模态感知和人机协作中发挥重要作用。

## 📄 摘要（原文）

> Understanding the world from multiple perspectives is essential for intelligent systems operating together, where segmenting common objects across different views remains an open problem. We introduce a new approach that re-defines cross-image segmentation by treating it as a mask matching task. Our method consists of: (1) A Mask-Context Encoder that pools dense DINOv2 semantic features to obtain discriminative object-level representations from FastSAM mask candidates, (2) an Ego$\leftrightarrow$Exo Cross-Attention that fuses multi-perspective observations, (3) a Mask Matching contrastive loss that aligns cross-view features in a shared latent space, and (4) a Hard Negative Adjacent Mining strategy to encourage the model to better differentiate between nearby objects. O-MaMa achieves the state of the art in the Ego-Exo4D Correspondences benchmark, obtaining relative gains of +22% and +76% in the Ego2Exo and Exo2Ego IoU against the official challenge baselines, and a +13% and +6% compared with the SOTA with 1% of the training parameters.

