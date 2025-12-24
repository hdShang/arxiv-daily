---
layout: default
title: "SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting"
---

# SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00800" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00800v1</a>
  <a href="https://arxiv.org/pdf/2509.00800.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00800v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00800v1', 'SWAGSplatting: Semantic-guided Water-scene Augmented Gaussian Splatting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhuodong Jiang, Haoran Wang, Guoxi Huang, Brett Seymour, Nantheera Anantrasirichai

**分类**: cs.CV

**发布日期**: 2025-08-31

**备注**: Submitted to SIGGRAPH Asia 2025 Technical Communications

---

## 💡 一句话要点

**提出SWAGSplatting以解决水下环境3D重建问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水下3D重建` `高斯溅射` `语义引导` `多模态融合` `深海场景重建` `AI技术` `阶段性训练` `海洋感知`

## 📋 核心要点

1. 水下环境的3D重建面临光线失真、浑浊等挑战，现有AI方法未能充分整合语言与视觉处理。
2. 提出SWAGSplatting框架，通过将语义特征嵌入高斯原语，增强训练过程中的语义和结构意识。
3. 在SeaThru-NeRF和Submerged3D数据集上，方法在PSNR指标上平均提升3.09 dB，超越现有技术。

## 📝 摘要（中文）

在水下环境中，准确的3D重建仍然是一个复杂的挑战，主要由于光线失真、浑浊和有限的可见性等问题。尽管已有基于AI的技术应用于此，但现有方法尚未充分利用AI的潜力，特别是在语言模型与视觉处理的结合方面。本文提出了一种新颖的框架，利用多模态跨知识创建语义引导的3D高斯溅射，以实现稳健且高保真的深海场景重建。通过将额外的语义特征嵌入每个高斯原语，并由CLIP提取的语义特征进行监督，我们的方法在训练过程中强化了语义和结构意识。专门的语义一致性损失确保了与高层场景理解的一致性。此外，我们提出了一种新的阶段性训练策略，结合粗到细的学习和后期参数细化，进一步提升了稳定性和重建质量。大量结果表明，我们的方法在SeaThru-NeRF和Submerged3D数据集上在三个指标上始终优于现有最先进的方法，PSNR平均提升高达3.09 dB，使其成为水下探索和海洋感知应用的强有力候选者。

## 🔬 方法详解

**问题定义**：本文旨在解决水下环境中3D重建的准确性问题，现有方法在光线失真和浑浊等条件下表现不佳，未能有效利用AI的潜力。

**核心思路**：通过将语义特征与高斯原语结合，利用CLIP提取的语义特征进行监督，增强模型的语义和结构理解能力。

**技术框架**：整体框架包括语义特征嵌入、专门的语义一致性损失和阶段性训练策略，分为粗到细的学习和后期参数细化两个阶段。

**关键创新**：最重要的创新在于将语义引导与高斯溅射结合，确保模型在训练过程中保持语义一致性，与现有方法相比，显著提升了重建质量。

**关键设计**：采用专门设计的损失函数以确保语义一致性，结合阶段性训练策略以提高模型的稳定性和重建质量，具体参数设置和网络结构细节在实验中进行了优化。

## 📊 实验亮点

实验结果显示，SWAGSplatting方法在SeaThru-NeRF和Submerged3D数据集上表现优异，PSNR指标平均提升达3.09 dB，超越了当前最先进的重建方法，证明了其在水下场景重建中的有效性和优势。

## 🎯 应用场景

该研究在水下探索和海洋感知领域具有广泛的应用潜力。通过提高水下3D重建的准确性，可以为海洋生物研究、环境监测和水下机器人导航等提供更可靠的数据支持，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Accurate 3D reconstruction in underwater environments remains a complex challenge due to issues such as light distortion, turbidity, and limited visibility. AI-based techniques have been applied to address these issues, however, existing methods have yet to fully exploit the potential of AI, particularly in integrating language models with visual processing. In this paper, we propose a novel framework that leverages multimodal cross-knowledge to create semantic-guided 3D Gaussian Splatting for robust and high-fidelity deep-sea scene reconstruction. By embedding an extra semantic feature into each Gaussian primitive and supervised by the CLIP extracted semantic feature, our method enforces semantic and structural awareness throughout the training. The dedicated semantic consistency loss ensures alignment with high-level scene understanding. Besides, we propose a novel stage-wise training strategy, combining coarse-to-fine learning with late-stage parameter refinement, to further enhance both stability and reconstruction quality. Extensive results show that our approach consistently outperforms state-of-the-art methods on SeaThru-NeRF and Submerged3D datasets across three metrics, with an improvement of up to 3.09 dB on average in terms of PSNR, making it a strong candidate for applications in underwater exploration and marine perception.

