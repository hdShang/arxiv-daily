---
layout: default
title: "CHARM: Collaborative Harmonization across Arbitrary Modalities for Modality-agnostic Semantic Segmentation"
---

# CHARM: Collaborative Harmonization across Arbitrary Modalities for Modality-agnostic Semantic Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03060" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03060v2</a>
  <a href="https://arxiv.org/pdf/2508.03060.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03060v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03060v2', 'CHARM: Collaborative Harmonization across Arbitrary Modalities for Modality-agnostic Semantic Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lekang Wen, Jing Xiao, Liang Liao, Jiajun Chen, Mi Wang

**分类**: cs.CV

**发布日期**: 2025-08-05 (更新: 2025-08-06)

---

## 💡 一句话要点

**提出CHARM以解决多模态语义分割中的同质化问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `多模态语义分割` `互补学习` `模态和谐化` `隐式对齐` `跨模态交互` `双路径优化` `自动驾驶` `医学影像分析`

## 📋 核心要点

1. 现有的多模态语义分割方法往往依赖显式特征对齐，导致模态优势的丧失和互补性破坏。
2. CHARM通过互感知单元和双路径优化策略，实现模态间的隐式对齐和互补融合，保留模态特定优势。
3. 实验结果显示，CHARM在多个数据集上表现优异，尤其在脆弱模态上显著提升性能，超越了现有基线。

## 📝 摘要（中文）

多模态语义分割（MaSS）旨在实现对任意输入模态组合的稳健场景理解。现有方法通常依赖于显式特征对齐来实现模态同质化，这会削弱每种模态的独特优势并破坏它们的内在互补性。为实现协作和谐而非同质化，本文提出了CHARM，一个新颖的互补学习框架，旨在通过两个组件隐式对齐内容，同时保留模态特定优势：1）互感知单元（MPU），通过基于窗口的跨模态交互实现隐式对齐；2）双路径优化策略，将训练解耦为互补融合学习的协作学习策略（CoL）和保护模态特定优化的个体增强策略（InE）。在多个数据集和骨干网络上的实验表明，CHARM在脆弱模态上显著超越基线，推动了从模型同质化到和谐化的转变。

## 🔬 方法详解

**问题定义**：本文解决的是多模态语义分割中的模态同质化问题。现有方法通过显式特征对齐来实现模态融合，导致模态特征的独特性被削弱，无法充分利用各模态的互补优势。

**核心思路**：CHARM的核心思路是通过互感知单元（MPU）实现模态间的隐式对齐，允许模态作为查询和上下文相互作用，从而发现模态间的交互对应关系，同时采用双路径优化策略来保护模态特定的优势。

**技术框架**：CHARM的整体架构包括两个主要模块：互感知单元（MPU）用于实现跨模态的隐式对齐，双路径优化策略则将训练过程分为协作学习和个体增强两个阶段，以实现互补融合和模态特定优化。

**关键创新**：CHARM的创新点在于其从模态同质化转向模态和谐化，强调模态间的互补性，而非简单的特征对齐。这种设计使得各模态的独特优势得以保留，促进了更为有效的多模态融合。

**关键设计**：在技术细节上，CHARM采用了窗口基础的交互机制来实现MPU，并在损失函数设计上考虑了模态特定的优化策略，以确保在训练过程中各模态的特征得以有效保留和增强。

## 📊 实验亮点

实验结果表明，CHARM在多个数据集上均显著超越了基线模型，尤其在脆弱模态上提升幅度达到XX%。这一成果验证了CHARM在实现模态和谐化方面的有效性，为多模态语义分割提供了新的思路。

## 🎯 应用场景

CHARM的研究成果在自动驾驶、医学影像分析和机器人视觉等领域具有广泛的应用潜力。通过实现更为有效的多模态融合，该方法能够提升系统在复杂场景下的理解能力，进而推动智能系统的实际应用和发展。

## 📄 摘要（原文）

> Modality-agnostic Semantic Segmentation (MaSS) aims to achieve robust scene understanding across arbitrary combinations of input modality. Existing methods typically rely on explicit feature alignment to achieve modal homogenization, which dilutes the distinctive strengths of each modality and destroys their inherent complementarity. To achieve cooperative harmonization rather than homogenization, we propose CHARM, a novel complementary learning framework designed to implicitly align content while preserving modality-specific advantages through two components: (1) Mutual Perception Unit (MPU), enabling implicit alignment through window-based cross-modal interaction, where modalities serve as both queries and contexts for each other to discover modality-interactive correspondences; (2) A dual-path optimization strategy that decouples training into Collaborative Learning Strategy (CoL) for complementary fusion learning and Individual Enhancement Strategy (InE) for protected modality-specific optimization. Experiments across multiple datasets and backbones indicate that CHARM consistently outperform the baselines, with significant increment on the fragile modalities. This work shifts the focus from model homogenization to harmonization, enabling cross-modal complementarity for true harmony in diversity.

