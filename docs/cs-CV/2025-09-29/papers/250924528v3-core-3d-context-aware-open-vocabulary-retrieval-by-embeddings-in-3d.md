---
layout: default
title: "CORE-3D: Context-aware Open-vocabulary Retrieval by Embeddings in 3D"
---

# CORE-3D: Context-aware Open-vocabulary Retrieval by Embeddings in 3D

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24528" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24528v3</a>
  <a href="https://arxiv.org/pdf/2509.24528.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24528v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24528v3', 'CORE-3D: Context-aware Open-vocabulary Retrieval by Embeddings in 3D')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamad Amin Mirzaei, Pantea Amoie, Ali Ekhterachian, Matin Mirzababaei, Babak Khalaj

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-29 (更新: 2025-12-07)

**备注**: Submitted for ICLR 2026 conference

---

## 💡 一句话要点

**CORE-3D：通过3D嵌入和上下文感知，实现开放词汇的3D场景检索**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景理解` `开放词汇检索` `视觉-语言模型` `语义分割` `对象检索`

## 📋 核心要点

1. 现有方法直接使用视觉-语言模型生成的掩码进行3D语义映射，导致掩码质量差和语义分配不准确。
2. CORE-3D利用SemanticSAM生成高质量对象级掩码，并结合上下文感知的CLIP编码，提升语义理解能力。
3. 实验结果表明，CORE-3D在3D语义分割和基于语言查询的对象检索任务上显著优于现有方法。

## 📝 摘要（中文）

本文提出了一种基于3D嵌入的上下文感知开放词汇检索方法CORE-3D，旨在提升具身AI和机器人领域中3D场景理解的性能。现有方法通常直接利用视觉-语言模型（VLMs）生成的2D类别无关掩码，并将其投影到3D空间，导致掩码碎片化和语义分配不准确。为了解决这个问题，我们利用SemanticSAM进行渐进式粒度细化，生成更准确和丰富的对象级掩码，从而减轻了传统SAM等掩码生成模型中常见的过度分割问题，并改善了下游的3D语义分割效果。此外，我们采用了一种上下文感知的CLIP编码策略，该策略集成了每个掩码的多个上下文视图，并使用经验确定的权重进行加权，从而提供更丰富的视觉上下文。我们在多个3D场景理解任务（包括3D语义分割和基于语言查询的对象检索）以及多个基准数据集上评估了我们的方法。实验结果表明，与现有方法相比，我们的方法取得了显著的改进，突出了我们方法的有效性。

## 🔬 方法详解

**问题定义**：现有基于视觉-语言模型的3D场景理解方法，依赖于将2D掩码投影到3D空间。这些方法直接使用原始掩码，容易产生碎片化和不准确的语义分配，尤其是在复杂环境中，限制了其有效性。现有方法的痛点在于缺乏对掩码质量的优化和对上下文信息的充分利用。

**核心思路**：CORE-3D的核心思路是首先通过SemanticSAM生成高质量的对象级掩码，然后利用上下文感知的CLIP编码策略，将每个掩码的多个上下文视图进行整合，从而提供更丰富的视觉上下文信息。这样设计的目的是为了提升掩码的准确性和语义的完整性，从而改善3D场景理解的性能。

**技术框架**：CORE-3D的整体框架包含以下几个主要阶段：1) 使用SemanticSAM进行掩码生成，通过渐进式粒度细化，得到更准确的对象级掩码；2) 对每个掩码提取多个上下文视图；3) 使用上下文感知的CLIP编码策略，对这些视图进行编码，并使用经验确定的权重进行加权；4) 将编码后的特征投影到3D空间，用于3D语义分割和对象检索等任务。

**关键创新**：CORE-3D的关键创新点在于：1) 利用SemanticSAM生成高质量对象级掩码，有效缓解了传统SAM等掩码生成模型中常见的过度分割问题；2) 提出了一种上下文感知的CLIP编码策略，通过整合多个上下文视图，显著提升了语义理解能力。

**关键设计**：在上下文感知的CLIP编码策略中，关键的设计在于如何选择上下文视图以及如何确定每个视图的权重。论文中提到，权重的确定是基于经验的，具体方法未知。此外，SemanticSAM的参数设置和训练细节，以及3D投影的具体方法，也是影响最终性能的关键因素，但论文中没有详细说明。

## 📊 实验亮点

实验结果表明，CORE-3D在3D语义分割和基于语言查询的对象检索任务上取得了显著的提升。具体性能数据未知，但论文强调了CORE-3D优于现有方法，证明了其在提升3D场景理解方面的有效性。通过利用SemanticSAM和上下文感知的CLIP编码，CORE-3D能够生成更准确的掩码和更丰富的语义信息。

## 🎯 应用场景

CORE-3D在具身AI和机器人领域具有广泛的应用前景，例如机器人导航、场景理解、物体交互等。该技术可以帮助机器人更好地理解周围环境，从而实现更智能、更可靠的交互和导航。此外，该方法还可以应用于虚拟现实、增强现实等领域，提升用户在3D环境中的体验。

## 📄 摘要（原文）

> 3D scene understanding is fundamental for embodied AI and robotics, supporting reliable perception for interaction and navigation. Recent approaches achieve zero-shot, open-vocabulary 3D semantic mapping by assigning embedding vectors to 2D class-agnostic masks generated via vision-language models (VLMs) and projecting these into 3D. However, these methods often produce fragmented masks and inaccurate semantic assignments due to the direct use of raw masks, limiting their effectiveness in complex environments. To address this, we leverage SemanticSAM with progressive granularity refinement to generate more accurate and numerous object-level masks, mitigating the over-segmentation commonly observed in mask generation models such as vanilla SAM, and improving downstream 3D semantic segmentation. To further enhance semantic context, we employ a context-aware CLIP encoding strategy that integrates multiple contextual views of each mask using empirically determined weighting, providing much richer visual context. We evaluate our approach on multiple 3D scene understanding tasks, including 3D semantic segmentation and object retrieval from language queries, across several benchmark datasets. Experimental results demonstrate significant improvements over existing methods, highlighting the effectiveness of our approach.

