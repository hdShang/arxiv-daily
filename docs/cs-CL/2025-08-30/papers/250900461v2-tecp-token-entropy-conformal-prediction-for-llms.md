---
layout: default
title: "TECP: Token-Entropy Conformal Prediction for LLMs"
---

# TECP: Token-Entropy Conformal Prediction for LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00461" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00461v2</a>
  <a href="https://arxiv.org/pdf/2509.00461.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00461v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00461v2', 'TECP: Token-Entropy Conformal Prediction for LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Beining Xu, Yongming Lu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-30 (更新: 2025-09-05)

---

## 💡 一句话要点

**提出TECP以解决大语言模型的不确定性量化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `不确定性量化` `开放式语言生成` `保形预测` `令牌熵` `黑箱模型` `大型语言模型` `自一致性方法`

## 📋 核心要点

1. 现有方法在黑箱环境下难以有效量化生成模型的不确定性，导致预测结果缺乏可靠性。
2. TECP框架通过令牌级熵作为不确定性度量，结合分裂保形预测，提供了无逻辑、无参考的解决方案。
3. 在多个大型语言模型上进行的实验表明，TECP在覆盖率和预测集紧凑性方面优于传统的自一致性方法。

## 📝 摘要（中文）

不确定性量化（UQ）在开放式语言生成中仍然是一个关键但未被充分探索的挑战，尤其是在黑箱约束下，内部模型信号无法访问。本文提出了Token-Entropy Conformal Prediction（TECP），这是一个新颖的框架，利用令牌级熵作为无逻辑、无参考的不确定性度量，并将其整合到分裂的保形预测（CP）管道中，以构建具有正式覆盖保证的预测集。与依赖语义一致性启发式或白箱特征的现有方法不同，TECP直接从采样生成的令牌熵结构中估计认知不确定性，并通过CP分位数校准不确定性阈值，以确保可证明的错误控制。在六个大型语言模型和两个基准（CoQA和TriviaQA）上的实证评估表明，TECP始终实现可靠的覆盖和紧凑的预测集，超越了先前基于自一致性的UQ方法。我们的方法为黑箱LLM环境中的可信生成提供了一个有原则且高效的解决方案。

## 🔬 方法详解

**问题定义**：本文旨在解决开放式语言生成中的不确定性量化问题，现有方法在黑箱约束下无法有效利用内部模型信号，导致不确定性评估不准确。

**核心思路**：TECP通过令牌级熵直接估计认知不确定性，避免了依赖语义一致性或白箱特征的局限性，并通过分裂保形预测校准不确定性阈值，确保错误控制。

**技术框架**：TECP的整体架构包括令牌熵计算模块和分裂保形预测模块，前者用于生成的令牌熵评估，后者用于构建具有覆盖保证的预测集。

**关键创新**：TECP的主要创新在于利用令牌级熵作为无逻辑的、不依赖参考的度量，直接从生成样本中提取不确定性信息，显著提升了不确定性量化的准确性。

**关键设计**：在TECP中，熵的计算方式和分位数的选择是关键设计，确保了不确定性阈值的有效校准，并通过实验验证了其在不同模型和数据集上的有效性。

## 📊 实验亮点

在六个大型语言模型的实验中，TECP在CoQA和TriviaQA基准上实现了超过90%的覆盖率，且预测集的紧凑性显著优于传统的自一致性方法，展示了其在不确定性量化中的有效性和优势。

## 🎯 应用场景

TECP框架在开放式语言生成、对话系统和自动问答等领域具有广泛的应用潜力。通过提供可靠的不确定性量化，TECP能够提升生成模型的可信度，促进人机交互的安全性和有效性。未来，该方法可能在更多黑箱模型的应用中发挥重要作用。

## 📄 摘要（原文）

> Uncertainty quantification (UQ) for open-ended language generation remains a critical yet underexplored challenge, especially under black-box constraints where internal model signals are inaccessible. In this paper, we introduce Token-Entropy Conformal Prediction (TECP), a novel framework that leverages token-level entropy as a logit-free, reference-free uncertainty measure and integrates it into a split conformal prediction (CP) pipeline to construct prediction sets with formal coverage guarantees. Unlike existing approaches that rely on semantic consistency heuristics or white-box features, TECP directly estimates epistemic uncertainty from the token entropy structure of sampled generations and calibrates uncertainty thresholds via CP quantiles to ensure provable error control. Empirical evaluations across six large language models and two benchmarks (CoQA and TriviaQA) demonstrate that TECP consistently achieves reliable coverage and compact prediction sets, outperforming prior self-consistency-based UQ methods. Our method provides a principled and efficient solution for trustworthy generation in black-box LLM settings.

