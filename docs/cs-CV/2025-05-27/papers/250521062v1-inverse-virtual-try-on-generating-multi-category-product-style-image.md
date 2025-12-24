---
layout: default
title: Inverse Virtual Try-On: Generating Multi-Category Product-Style Images from Clothed Individuals
---

# Inverse Virtual Try-On: Generating Multi-Category Product-Style Images from Clothed Individuals

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21062" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21062v1</a>
  <a href="https://arxiv.org/pdf/2505.21062.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21062v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21062v1', 'Inverse Virtual Try-On: Generating Multi-Category Product-Style Images from Clothed Individuals')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davide Lobba, Fulvio Sanguigni, Bin Ren, Marcella Cornia, Rita Cucchiara, Nicu Sebe

**分类**: cs.CV

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出TEMU-VTOFF以解决虚拟试穿逆问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚拟试脱` `多模态融合` `服装生成` `计算机视觉` `深度学习`

## 📋 核心要点

1. 现有的虚拟试脱方法在处理遮挡和复杂姿势时，常常导致视觉伪影，且仅限于单一类别服装，限制了其应用范围。
2. 本文提出的TEMU-VTOFF架构通过双重DiT基础网络和多模态注意力机制，能够从多种模态中提取服装信息，支持多类别服装生成。
3. 在VITON-HD和Dress Code数据集上的实验表明，TEMU-VTOFF在视觉质量和服装忠实度上均显著优于现有方法，设立了新的性能基准。

## 📝 摘要（中文）

本论文提出了一种新颖的虚拟试脱（VTOFF）任务，旨在从穿着服装的真实照片中生成标准化的服装产品图像。与虚拟试穿（VTON）不同，VTOFF的输出格式更加一致，通常为平铺样式的服装表示。现有的VTOFF方法面临两个主要挑战：一是难以从遮挡和复杂姿势中分离服装特征，二是仅适用于单一类别的服装。为了解决这些问题，本文提出了文本增强多类别虚拟试脱（TEMU-VTOFF），其架构采用双重DiT基础网络和改进的多模态注意力机制，以实现稳健的服装特征提取。实验结果表明，TEMU-VTOFF在VTOFF任务上设立了新的最先进水平，显著提高了视觉质量和对目标服装的忠实度。

## 🔬 方法详解

**问题定义**：本论文旨在解决虚拟试脱（VTOFF）任务，即从穿着服装的真实照片中生成标准化的服装图像。现有方法面临的痛点包括难以从遮挡和复杂姿势中分离服装特征，以及仅适用于单一类别服装，限制了其通用性。

**核心思路**：论文提出的TEMU-VTOFF架构通过引入双重DiT基础网络和改进的多模态注意力机制，能够有效提取服装特征，并支持多类别服装的生成。这样的设计使得模型能够处理来自不同模态的信息，提高了生成的准确性和多样性。

**技术框架**：TEMU-VTOFF的整体架构包括多个主要模块：首先是双重DiT基础网络用于特征提取，其次是多模态注意力机制用于融合不同模态的信息，最后是对齐模块用于进一步细化生成的视觉细节。

**关键创新**：最重要的技术创新点在于引入了多模态信息处理能力，使得模型能够在多类别服装生成任务中表现出色。这与现有方法的单一类别限制形成了鲜明对比。

**关键设计**：在网络结构上，TEMU-VTOFF采用了双重DiT基础网络，结合了多模态注意力机制以增强特征提取能力。此外，设计了特定的损失函数以优化生成图像的质量和对目标服装的忠实度。

## 📊 实验亮点

在VITON-HD和Dress Code数据集上的实验结果显示，TEMU-VTOFF在VTOFF任务上设立了新的最先进水平，视觉质量和对目标服装的忠实度均有显著提升，具体性能数据未详述，但提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括电子商务、时尚行业和虚拟试衣间等。通过生成高质量的服装产品图像，商家可以更好地展示商品，提升用户体验。此外，TEMU-VTOFF还可以用于数据集增强，帮助训练更强大的计算机视觉模型，推动相关领域的发展。

## 📄 摘要（原文）

> While virtual try-on (VTON) systems aim to render a garment onto a target person image, this paper tackles the novel task of virtual try-off (VTOFF), which addresses the inverse problem: generating standardized product images of garments from real-world photos of clothed individuals. Unlike VTON, which must resolve diverse pose and style variations, VTOFF benefits from a consistent and well-defined output format -- typically a flat, lay-down-style representation of the garment -- making it a promising tool for data generation and dataset enhancement. However, existing VTOFF approaches face two major limitations: (i) difficulty in disentangling garment features from occlusions and complex poses, often leading to visual artifacts, and (ii) restricted applicability to single-category garments (e.g., upper-body clothes only), limiting generalization. To address these challenges, we present Text-Enhanced MUlti-category Virtual Try-Off (TEMU-VTOFF), a novel architecture featuring a dual DiT-based backbone with a modified multimodal attention mechanism for robust garment feature extraction. Our architecture is designed to receive garment information from multiple modalities like images, text, and masks to work in a multi-category setting. Finally, we propose an additional alignment module to further refine the generated visual details. Experiments on VITON-HD and Dress Code datasets show that TEMU-VTOFF sets a new state-of-the-art on the VTOFF task, significantly improving both visual quality and fidelity to the target garments.

