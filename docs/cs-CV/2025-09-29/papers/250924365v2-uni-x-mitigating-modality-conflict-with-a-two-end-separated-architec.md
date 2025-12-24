---
layout: default
title: "Uni-X: Mitigating Modality Conflict with a Two-End-Separated Architecture for Unified Multimodal Models"
---

# Uni-X: Mitigating Modality Conflict with a Two-End-Separated Architecture for Unified Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24365" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24365v2</a>
  <a href="https://arxiv.org/pdf/2509.24365.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24365v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24365v2', 'Uni-X: Mitigating Modality Conflict with a Two-End-Separated Architecture for Unified Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jitai Hao, Hao Liu, Xinyan Xiao, Qiang Huang, Jun Yu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-29 (更新: 2025-11-29)

**🔗 代码/项目**: [GITHUB](https://github.com/CURRENTF/Uni-X)

---

## 💡 一句话要点

**提出Uni-X模型，通过两端分离架构缓解多模态统一模型中的模态冲突问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `统一模型` `梯度冲突` `Transformer` `模型架构` `图像生成` `视觉理解`

## 📋 核心要点

1. 现有统一多模态模型在训练时，浅层和深层Transformer存在视觉和文本模态间的梯度冲突，影响模型性能。
2. Uni-X采用两端分离、中间共享的X形架构，缓解了模态间的梯度冲突，提升了训练效率和模型性能。
3. 实验结果表明，Uni-X在训练效率上优于基线模型，并且在扩展到3B参数时，性能可媲美7B参数的模型。

## 📝 摘要（中文）

统一多模态模型(UMMs)因其架构的简洁性而备受关注，它们通常基于共享的自回归(AR) Transformer。然而，我们发现了一个关键限制：当在多模态输入上训练时，模态共享的Transformer会遭受视觉和文本之间严重的梯度冲突，尤其是在浅层和深层。我们将此问题追溯到图像和文本的低级统计属性的根本差异，同时注意到冲突在表示变得更抽象和语义对齐的中间层有所减少。为了克服这个挑战，我们提出了Uni-X，一种两端分离、中间共享的架构。Uni-X将其初始层和最终层专用于模态特定的处理，同时在中间层保持共享参数以进行高级语义融合。这种X形设计不仅消除了两端的梯度冲突，而且进一步缓解了共享层中的残余冲突。大量的实验验证了Uni-X的有效性。在相同的训练条件下，Uni-X实现了优于强基线的训练效率。当使用更大的训练数据扩展到3B参数时，Uni-X匹配或超过了7B基于AR的UMM，在图像生成方面实现了82的GenEval分数，同时在文本和视觉理解任务中表现出色。这些结果确立了Uni-X作为未来统一多模态建模的参数高效且可扩展的基础。

## 🔬 方法详解

**问题定义**：论文旨在解决统一多模态模型（UMMs）中，由于视觉和文本模态的低级统计属性差异，导致在共享Transformer的浅层和深层出现严重的梯度冲突问题。这种冲突阻碍了模型的有效训练和性能提升。

**核心思路**：论文的核心思路是采用一种两端分离、中间共享的X形架构（Uni-X）。通过将模型的初始层和最终层设计为模态特定的处理层，专门处理各自模态的低级特征，从而消除两端的梯度冲突。中间层则保持共享，用于进行高级语义融合。

**技术框架**：Uni-X模型的整体架构由三个主要部分组成：模态特定的初始层、共享的中间层和模态特定的最终层。输入数据首先通过各自模态的初始层进行处理，提取模态特定的低级特征。然后，这些特征被传递到共享的中间层进行高级语义融合。最后，融合后的特征通过各自模态的最终层进行处理，生成最终的输出。

**关键创新**：Uni-X的关键创新在于其X形架构，这种架构能够有效地缓解多模态统一模型中的模态冲突问题。与传统的共享Transformer架构相比，Uni-X通过两端分离的设计，避免了在浅层和深层出现梯度冲突，从而提高了训练效率和模型性能。

**关键设计**：Uni-X的关键设计包括：1) 模态特定层的具体结构（例如，卷积层用于视觉模态，嵌入层用于文本模态）；2) 共享中间层的Transformer块数量和参数设置；3) 损失函数的设计，可能包括模态特定的损失函数和跨模态的对齐损失函数；4) 模型训练的优化策略，例如学习率调度和正则化方法。

## 📊 实验亮点

Uni-X在相同的训练条件下，训练效率优于强基线模型。当扩展到3B参数并使用更大的训练数据集时，Uni-X的性能与7B参数的自回归UMM模型相匹配甚至超越，在图像生成任务中GenEval得分达到82，同时在文本和视觉理解任务中也表现出强大的性能。

## 🎯 应用场景

Uni-X模型具有广泛的应用前景，包括但不限于：跨模态信息检索、图像/视频描述生成、视觉问答、多模态对话系统等。该模型的高效性和可扩展性使其能够应用于资源受限的设备，并为未来的统一多模态建模提供了一个有力的基础。

## 📄 摘要（原文）

> Unified Multimodal Models (UMMs) built on shared autoregressive (AR) transformers are attractive for their architectural simplicity. However, we identify a critical limitation: when trained on multimodal inputs, modality-shared transformers suffer from severe gradient conflicts between vision and text, particularly in shallow and deep layers. We trace this issue to the fundamentally different low-level statistical properties of images and text, while noting that conflicts diminish in middle layers where representations become more abstract and semantically aligned. To overcome this challenge, we propose Uni-X, a two-end-separated, middle-shared architecture. Uni-X dedicates its initial and final layers to modality-specific processing, while maintaining shared parameters in the middle layers for high-level semantic fusion. This X-shaped design not only eliminates gradient conflicts at both ends but also further alleviates residual conflicts in the shared layers. Extensive experiments validate the effectiveness of Uni-X. Under identical training conditions, Uni-X achieves superior training efficiency compared to strong baselines. When scaled to 3B parameters with larger training data, Uni-X matches or surpasses 7B AR-based UMMs, achieving a GenEval score of 82 for image generation alongside strong performance in text and vision understanding tasks. These results establish Uni-X as a parameter-efficient and scalable foundation for future unified multimodal modeling. Our code is available at https://github.com/CURRENTF/Uni-X

