---
layout: default
title: Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge
---

# Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08316" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08316v1</a>
  <a href="https://arxiv.org/pdf/2510.08316.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08316v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08316v1', 'Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yu Huang, Zelin Peng, Changsong Wen, Xiaokang Yang, Wei Shen

**分类**: cs.CV

**发布日期**: 2025-10-09

**备注**: Work in process

---

## 💡 一句话要点

**提出CMAT和CAST，利用2D语义知识提升3D可供性分割性能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D可供性分割` `跨模态学习` `语义知识迁移` `视觉基础模型` `Transformer`

## 📋 核心要点

1. 现有3D可供性分割方法依赖通用点云编码器，难以应对3D数据的稀疏性和几何歧义。
2. 论文提出CMAT预训练策略，将2D视觉基础模型的语义知识迁移到3D领域，提升特征的语义一致性。
3. 构建CAST模型，融合多模态提示和预训练特征，在标准数据集上取得了SOTA性能。

## 📝 摘要（中文）

可供性分割旨在将3D物体解析为功能上不同的部分，从而连接识别和交互，应用于机器人操作、具身智能和增强现实。现有方法通常依赖点云编码器作为通用特征提取器，忽略了3D数据的稀疏性、噪声和几何歧义等内在挑战。因此，孤立学习的3D特征通常缺乏清晰且语义一致的功能边界。为了解决这个瓶颈，我们提出了一种语义引导的学习范式，将来自大规模2D视觉基础模型(VFMs)的丰富语义知识转移到3D领域。具体来说，我们引入了跨模态亲和力转移(CMAT)，这是一种预训练策略，使3D编码器与提升的2D语义对齐，并联合优化重建、亲和力和多样性，以产生语义组织的表示。在此基础上，我们进一步设计了跨模态可供性分割Transformer (CAST)，它将多模态提示与CMAT预训练的特征集成，以生成精确的、提示感知的分割图。在标准基准上的大量实验表明，我们的框架为3D可供性分割建立了新的最先进的结果。

## 🔬 方法详解

**问题定义**：现有的3D可供性分割方法主要依赖于直接在3D数据上训练的点云编码器。这些方法忽略了3D数据的固有挑战，例如数据稀疏、噪声以及几何形状的模糊性。因此，学习到的3D特征往往缺乏清晰的、语义一致的功能边界，限制了分割的准确性。

**核心思路**：论文的核心思路是将2D视觉基础模型（VFMs）中蕴含的丰富语义知识迁移到3D领域。2D图像数据量大，语义信息丰富，通过合适的迁移策略，可以有效提升3D特征的语义表达能力，从而改善3D可供性分割的性能。

**技术框架**：整体框架包含两个主要部分：CMAT预训练和CAST分割。首先，CMAT（Cross-Modal Affinity Transfer）预训练模块用于将2D语义知识迁移到3D编码器。然后，CAST（Cross-modal Affordance Segmentation Transformer）分割模块利用CMAT预训练的特征，结合多模态提示，生成最终的分割结果。

**关键创新**：论文的关键创新在于提出了CMAT预训练策略。CMAT通过联合优化重建损失、亲和力损失和多样性损失，使得3D编码器能够学习到与2D语义对齐的、具有良好语义组织性的表示。这种跨模态的知识迁移方式，有效克服了3D数据自身的局限性。

**关键设计**：CMAT预训练阶段，使用了三种损失函数：1) 重建损失，保证3D特征能够重建原始3D数据；2) 亲和力损失，促使3D特征在语义相似的点之间具有更高的亲和力；3) 多样性损失，鼓励3D特征在不同类别之间具有更高的区分度。CAST分割阶段，使用了Transformer结构，将多模态提示（例如文本或视觉提示）与CMAT预训练的3D特征进行融合，从而生成prompt-aware的分割结果。

## 📊 实验亮点

论文在标准3D可供性分割数据集上进行了大量实验，结果表明，所提出的CMAT和CAST框架显著优于现有的方法，取得了state-of-the-art的性能。具体而言，在多个指标上都取得了明显的提升，证明了该方法的有效性。

## 🎯 应用场景

该研究成果可广泛应用于机器人操作、具身智能和增强现实等领域。例如，机器人可以利用可供性分割的结果，更好地理解物体的功能，从而执行更复杂的抓取、放置等操作。在AR应用中，可以根据用户的交互意图，动态地分割3D场景中的物体，提供更智能的交互体验。

## 📄 摘要（原文）

> Affordance segmentation aims to parse 3D objects into functionally distinct parts, bridging recognition and interaction for applications in robotic manipulation, embodied AI, and AR. While recent studies leverage visual or textual prompts to guide this process, they often rely on point cloud encoders as generic feature extractors, overlooking the intrinsic challenges of 3D data such as sparsity, noise, and geometric ambiguity. As a result, 3D features learned in isolation frequently lack clear and semantically consistent functional boundaries. To address this bottleneck, we propose a semantic-grounded learning paradigm that transfers rich semantic knowledge from large-scale 2D Vision Foundation Models (VFMs) into the 3D domain. Specifically, We introduce Cross-Modal Affinity Transfer (CMAT), a pre-training strategy that aligns a 3D encoder with lifted 2D semantics and jointly optimizes reconstruction, affinity, and diversity to yield semantically organized representations. Building on this backbone, we further design the Cross-modal Affordance Segmentation Transformer (CAST), which integrates multi-modal prompts with CMAT-pretrained features to generate precise, prompt-aware segmentation maps. Extensive experiments on standard benchmarks demonstrate that our framework establishes new state-of-the-art results for 3D affordance segmentation.

