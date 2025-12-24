---
layout: default
title: "Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens"
---

# Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13775" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13775v3</a>
  <a href="https://arxiv.org/pdf/2505.13775.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13775v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13775v3', 'Beyond Semantics: The Unreasonable Effectiveness of Reasonless Intermediate Tokens')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Karthik Valmeekam, Kaya Stechly, Vardhan Palod, Atharva Gundawar, Subbarao Kambhampati

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-19 (更新: 2025-11-22)

---

## 💡 一句话要点

**提出无语义中间标记以挑战推理模型的传统理解**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理模型` `链式思维` `中间标记` `自然语言处理` `强化学习` `模型训练` `推理能力`

## 📋 核心要点

1. 现有方法在推理模型的中间标记上过于依赖语义，导致对模型推理过程的误解。
2. 本文通过训练模型于形式可验证的推理痕迹，系统性地研究其对模型性能的影响。
3. 实验结果显示，训练于错误痕迹的模型在某些任务上表现优于仅训练于正确痕迹的模型。

## 📝 摘要（中文）

近年来，大型推理模型的显著成果被解读为链式思维（CoT）的成功，尤其是通过从基础大型语言模型（LLM）中采样的CoT进行训练。然而，尽管这些推理痕迹似乎有助于模型性能，但它们如何影响模型仍不明确。本文通过控制实验研究推理痕迹的作用，发现即使在完全正确的推理痕迹上训练的模型也可能产生无效的推理痕迹。此外，训练于错误痕迹的模型在某些任务上表现与正确痕迹相似，甚至更具泛化能力。这些结果挑战了中间标记反映可预测推理行为的假设，并警示不要过度解读这些输出。

## 🔬 方法详解

**问题定义**：本文旨在探讨推理模型中间标记的有效性，现有方法往往假设这些标记具有明确的语义和推理能力，但实际情况可能并非如此。

**核心思路**：通过训练模型于形式上可验证的推理痕迹，研究其对模型推理能力的影响，尤其是中间标记的有效性与推理结果之间的关系。

**技术框架**：研究采用控制实验设计，训练Transformer模型于不同类型的推理痕迹，包括完全正确和错误的痕迹，评估其在推理任务上的表现。

**关键创新**：本文的主要创新在于揭示了中间推理痕迹的有效性并不总是与最终解决方案的正确性相关，挑战了传统的推理模型设计理念。

**关键设计**：实验中使用了多种损失函数和网络结构，特别关注了推理痕迹的长度与推理复杂性之间的关系，发现其并不直接相关。通过GRPO基础的强化学习后训练，虽然提高了解决方案的准确性，但未改善推理痕迹的有效性。

## 📊 实验亮点

实验结果显示，训练于错误推理痕迹的模型在某些任务上与训练于正确痕迹的模型表现相似，甚至在分布外任务上泛化能力更强。这一发现挑战了中间标记的传统理解，强调了推理过程的复杂性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动推理工具。通过对推理模型的深入理解，可以提升模型在复杂任务中的表现，推动更智能的AI系统的发展。未来，研究结果可能影响推理模型的设计和训练方法，促进更高效的推理过程。

## 📄 摘要（原文）

> Recent impressive results from large reasoning models have been interpreted as a triumph of Chain of Thought (CoT), especially of training on CoTs sampled from base LLMs to help find new reasoning patterns. While these traces certainly seem to help model performance, it is not clear how they actually influence it, with some works ascribing semantics to the traces and others cautioning against relying on them as transparent and faithful proxies of the model's internal computational process. To systematically investigate the role of end-user semantics of derivational traces, we set up a controlled study where we train transformer models from scratch on formally verifiable reasoning traces and the solutions they lead to. We notice that, despite significant gains over the solution-only baseline, models trained on entirely correct traces can still produce invalid reasoning traces even when arriving at correct solutions. More interestingly, our experiments also show that models trained on corrupted traces, whose intermediate reasoning steps bear no relation to the problem they accompany, perform similarly to those trained on correct ones, and even generalize better on out-of-distribution tasks. We also study the effect of GRPO-based RL post-training on trace validity, noting that while solution accuracy increase, this is not accompanied by any improvements in trace validity. Finally, we examine whether reasoning-trace length reflects inference-time scaling and find that trace length is largely agnostic to the underlying computational complexity of the problem being solved. These results challenge the assumption that intermediate tokens or ``Chains of Thought'' reflect or induce predictable reasoning behaviors and caution against anthropomorphizing such outputs or over-interpreting them (despite their mostly seemingly forms) as evidence of human-like or algorithmic behaviors in language models.

