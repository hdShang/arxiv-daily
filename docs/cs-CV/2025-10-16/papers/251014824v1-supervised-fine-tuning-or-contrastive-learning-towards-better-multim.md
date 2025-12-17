---
layout: default
title: Supervised Fine-Tuning or Contrastive Learning? Towards Better Multimodal LLM Reranking
---

# Supervised Fine-Tuning or Contrastive Learning? Towards Better Multimodal LLM Reranking

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14824" target="_blank" class="toolbar-btn">arXiv: 2510.14824v1</a>
    <a href="https://arxiv.org/pdf/2510.14824.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14824v1" 
            onclick="toggleFavorite(this, '2510.14824v1', 'Supervised Fine-Tuning or Contrastive Learning? Towards Better Multimodal LLM Reranking')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Ziqi Dai, Xin Zhang, Mingxin Li, Yanzhao Zhang, Dingkun Long, Pengjun Xie, Meishan Zhang, Wenjie Li, Min Zhang

**分类**: cs.CL, cs.CV, cs.IR

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**针对多模态LLM重排序，对比监督微调与对比学习的优劣**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `大型语言模型` `重排序` `对比学习` `监督微调` `信息检索` `权重分析` `方向分析`

## 📋 核心要点

1. 现有基于LLM的重排序模型训练方法选择存在争议，对比学习和监督微调孰优孰劣尚不明确。
2. 论文将训练目标分解为权重和方向两个组成部分，提出了一个统一的框架来分析对比学习和监督微调的交互。
3. 实验结果表明，监督微调在LLM重排序中具有优势，并在MRB基准测试中取得了新的state-of-the-art结果。

## 📝 摘要（中文）

在信息检索中，重排序模型的训练主要集中于两种目标：度量学习（例如，使用对比损失来增加相关查询-文档对的预测分数）和分类（对相关与不相关的二元标签进行预测）。对于BERT风格的编码器，大量研究表明对比学习（CL）比判别式（分类）学习更有效。然而，对于大型语言模型（LLM），通过监督微调（SFT）进行分类，即预测相关（或不相关）对的“是”（或“否”）token，似乎更有前景，因为它与LLM的生成特性非常吻合。这种差异提出了一个核心问题：哪种目标更适合基于LLM的重排序？其差异的潜在机制是什么？在这项工作中，我们对CL和SFT在重排序方面进行了全面的比较和分析，并将通用多模态检索（UMR）作为实验平台。我们首先将目标分解为两个组成部分：权重（控制更新幅度）和方向（指导模型更新），然后提出了一个统一的框架来理解它们的相互作用。通过探测实验，我们发现SFT提供了比CL更强的加权方案，而首选的评分方向没有明显的赢家。总而言之，这些结果表明SFT在LLM重排序方面具有一致的优势。为了进一步验证我们的发现，我们使用SFT进行了大规模训练，并在MRB基准测试中提出了新的最先进的重排序器。我们还提供了关于SFT设置的消融研究，并期望我们的发现能够有益于该领域未来的研究和应用。

## 🔬 方法详解

**问题定义**：论文旨在解决在多模态信息检索中，如何有效地训练基于大型语言模型（LLM）的重排序模型的问题。现有方法，特别是对比学习（CL）和监督微调（SFT），在应用于LLM时表现出差异。对于BERT类模型，CL通常更有效，但对于LLM，SFT似乎更具潜力。因此，论文要探究哪种训练目标更适合LLM重排序，并解释其内在机制。

**核心思路**：论文的核心思路是将训练目标分解为两个关键组成部分：权重（weight）和方向（direction）。权重控制模型更新的幅度，而方向指导模型更新的方向。通过分析CL和SFT在这两个方面的差异，论文旨在理解它们在LLM重排序中的表现差异。这种分解提供了一个统一的框架，用于比较和理解不同训练目标之间的交互作用。

**技术框架**：论文采用通用多模态检索（UMR）作为实验平台。整体流程包括：1) 使用CL或SFT训练LLM重排序模型；2) 将训练目标分解为权重和方向；3) 通过探测实验分析权重和方向的影响；4) 在MRB基准测试上评估模型性能。该框架允许研究人员深入了解不同训练目标对LLM重排序的影响。

**关键创新**：论文最重要的技术创新在于将训练目标分解为权重和方向，并提出了一个统一的框架来理解CL和SFT的交互作用。这种分解方法提供了一种新的视角，可以更深入地理解不同训练目标对LLM重排序的影响。与现有方法相比，该方法不仅关注模型的性能，还关注训练过程中的内在机制。

**关键设计**：论文的关键设计包括：1) 使用对比损失（CL）和监督微调（SFT）作为两种主要的训练目标；2) 设计探测实验来分析权重和方向的影响；3) 在MRB基准测试上进行大规模训练和评估；4) 对SFT设置进行消融研究，以进一步验证研究结果。论文还特别关注了如何将SFT应用于LLM，例如，通过预测“是”或“否”token来表示相关性。

## 📊 实验亮点

实验结果表明，监督微调（SFT）在LLM重排序方面具有一致的优势。通过大规模训练，论文提出的SFT重排序器在MRB基准测试中取得了新的state-of-the-art结果。探测实验表明，SFT提供了比对比学习（CL）更强的加权方案。消融研究进一步验证了SFT设置对模型性能的影响。

## 🎯 应用场景

该研究成果可应用于各种多模态信息检索场景，例如图像搜索、视频搜索、跨模态检索等。通过选择合适的训练目标，可以显著提高LLM重排序模型的性能，从而提升用户体验。该研究还有助于推动LLM在信息检索领域的应用，并为未来的研究提供指导。

## 📄 摘要（原文）

> In information retrieval, training reranking models mainly focuses on two types of objectives: metric learning (e.g. contrastive loss to increase the predicted scores on relevant query-document pairs) and classification (binary label prediction of relevance vs. irrelevance). For BERT-style encoders, various studies have shown that contrastive learning (CL) can be more effective than discriminative (classification) learning. However, for large language models (LLMs), classification via supervised fine-tuning (SFT), which predicts ''yes'' (resp. ''no'') token for relevant (resp. irrelevant) pairs, appears more promising as it aligns well with the generative nature of LLMs. This divergence raises a central question: which objective is intrinsically better suited to LLM-based reranking, and what mechanism underlies the difference? In this work, we conduct a comprehensive comparison and analysis between CL and SFT for reranking, taking the universal multimodal retrieval (UMR) as the experimental playground. We first decompose the objectives into two components: weight, which controls the magnitude of those updates, and direction, which guides the model updates, then present a unified framework for understanding their interactions. Through probing experiments, we find that SFT provides a substantially stronger weighting scheme than CL, whereas the preferred scoring direction shows no clear winner. Taken together, these results point to a consistent advantage of SFT over CL for LLM reranking. To further validate our findings, we conduct large-scale training with SFT and present new state-of-the-art rerankers on the MRB benchmark. We also provide ablations on SFT settings and expect our findings to benefit future research and applications in this area.

