---
layout: default
title: "SMAR: Soft Modality-Aware Routing Strategy for MoE-based Multimodal Large Language Models Preserving Language Capabilities"
---

# SMAR: Soft Modality-Aware Routing Strategy for MoE-based Multimodal Large Language Models Preserving Language Capabilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06406" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06406v2</a>
  <a href="https://arxiv.org/pdf/2506.06406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06406v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06406v2', 'SMAR: Soft Modality-Aware Routing Strategy for MoE-based Multimodal Large Language Models Preserving Language Capabilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guoyang Xia, Yifeng Ding, Fengfa Li, Lei Ren, Wei Chen, Fangxiang Feng, Xiaojie Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-06 (更新: 2025-06-25)

---

## 💡 一句话要点

**提出SMAR以解决多模态MoE模型语言能力下降问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `混合专家` `多模态学习` `语言模型` `Kullback-Leibler散度` `路由策略` `视觉指令调优` `专家选择` `模型正则化`

## 📋 核心要点

1. 现有多模态MoE模型在训练成本高或语言能力下降方面存在显著挑战。
2. 本文提出的SMAR通过Kullback-Leibler散度控制模态路由概率，促进专家专业化。
3. 实验结果显示，SMAR在仅2.5%文本数据下，语言能力保留率达到86.6%，优于现有基线。

## 📝 摘要（中文）

混合专家（MoE）架构已成为扩展大型语言模型的关键方法，尤其是在多模态任务中的应用日益受到关注。然而，现有构建多模态MoE模型的方法往往面临高训练成本或在适应预训练模型时语言能力下降的问题。为了解决这一问题，本文提出了一种新颖的正则化技术——软模态感知路由（SMAR），通过使用Kullback-Leibler散度控制模态间的路由概率分布，鼓励专家专业化，而无需修改模型架构或过度依赖文本数据。在视觉指令调优实验中，SMAR在仅使用2.5%纯文本的情况下，语言能力保留率达到86.6%，超越了基线，同时保持了强大的多模态性能。该方法为在多模态MoE模型中平衡模态差异化和语言能力提供了实用高效的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态MoE模型在适应预训练语言模型时，面临的高训练成本和语言能力下降的问题。现有方法往往无法有效平衡模态间的差异化与语言能力的保留。

**核心思路**：SMAR通过引入Kullback-Leibler散度作为正则化手段，控制不同模态间的路由概率分布，鼓励模型在不改变架构的情况下实现专家的专业化。此设计旨在减少对文本数据的依赖，同时保持语言能力。

**技术框架**：该方法的整体架构包括模态路由模块和专家选择机制。模态路由模块负责根据输入数据的特征动态调整路由概率，而专家选择机制则确保在每次推理时选择最合适的专家进行处理。

**关键创新**：SMAR的主要创新在于其使用Kullback-Leibler散度来优化模态间的路由策略，这一方法与传统的基于硬路由或简单加权的策略有本质区别，能够更好地适应多模态输入。

**关键设计**：在实现过程中，SMAR设置了特定的损失函数以平衡模态间的路由概率，并通过调节超参数来优化模型的性能。网络结构上，保持了原有的MoE架构，增加了模态感知的路由机制。

## 📊 实验亮点

实验结果表明，SMAR在视觉指令调优任务中，语言能力保留率达到86.6%，仅需2.5%的纯文本数据，显著优于现有基线，展示了其在多模态任务中的强大性能。

## 🎯 应用场景

该研究的潜在应用领域包括多模态自然语言处理、视觉问答系统和智能助手等。通过有效平衡模态间的差异化和语言能力，SMAR能够提升多模态模型在实际应用中的表现，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Mixture of Experts (MoE) architectures have become a key approach for scaling large language models, with growing interest in extending them to multimodal tasks. Existing methods to build multimodal MoE models either incur high training costs or suffer from degraded language capabilities when adapting pretrained models. To address this, we propose Soft ModalityAware Routing (SMAR), a novel regularization technique that uses Kullback Leibler divergence to control routing probability distributions across modalities, encouraging expert specialization without modifying model architecture or heavily relying on textual data. Experiments on visual instruction tuning show that SMAR preserves language ability at 86.6% retention with only 2.5% pure text, outperforming baselines while maintaining strong multimodal performance. Our approach offers a practical and efficient solution to balance modality differentiation and language capabilities in multimodal MoE models.

