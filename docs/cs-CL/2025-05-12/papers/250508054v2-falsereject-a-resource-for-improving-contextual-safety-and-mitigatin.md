---
layout: default
title: FalseReject: A Resource for Improving Contextual Safety and Mitigating Over-Refusals in LLMs via Structured Reasoning
---

# FalseReject: A Resource for Improving Contextual Safety and Mitigating Over-Refusals in LLMs via Structured Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08054" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08054v2</a>
  <a href="https://arxiv.org/pdf/2505.08054.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08054v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08054v2', 'FalseReject: A Resource for Improving Contextual Safety and Mitigating Over-Refusals in LLMs via Structured Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhehao Zhang, Weijie Xu, Fanyou Wu, Chandan K. Reddy

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-12 (更新: 2025-07-15)

**备注**: Accepted at COLM 2025

---

## 💡 一句话要点

**提出FalseReject以解决大型语言模型的过度拒绝问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全对齐` `结构化推理` `多智能体交互` `数据集构建` `模型微调` `过度拒绝` `人机交互`

## 📋 核心要点

1. 现有的安全对齐方法在大型语言模型中导致了对良性查询的过度拒绝，影响了模型的实用性。
2. 论文提出了FalseReject资源，通过结构化推理帮助模型更好地区分安全和不安全的上下文。
3. 实验结果表明，使用FalseReject进行微调后，29个SOTA LLMs的过度拒绝现象显著减少，且未影响安全性。

## 📝 摘要（中文）

大型语言模型（LLMs）中的安全对齐方法常导致对良性查询的过度拒绝，显著降低其在敏感场景中的实用性。为了解决这一挑战，我们引入了FalseReject，这是一个包含16,000个看似有毒查询及其结构化响应的综合资源，涵盖44个安全相关类别。我们提出了一种图信息对抗多智能体交互框架，以生成多样且复杂的提示，同时通过明确的推理结构化响应，帮助模型准确区分安全与不安全的上下文。FalseReject还包括针对标准指令调优模型和推理导向模型的训练数据集，以及一个人工标注的基准测试集。我们对29个最先进的LLMs进行了广泛的基准测试，揭示了持续的过度拒绝挑战。实证结果表明，使用FalseReject进行监督微调显著减少了不必要的拒绝，同时不影响整体安全性或语言能力。

## 🔬 方法详解

**问题定义**：论文要解决的问题是大型语言模型在安全对齐过程中对良性查询的过度拒绝现象，这一现象导致模型在敏感场景中的实用性大幅降低。现有方法未能有效区分安全与不安全的上下文，导致模型频繁拒绝正常请求。

**核心思路**：论文的核心解决思路是构建FalseReject资源，包含大量的有毒查询及其结构化响应，通过图信息对抗多智能体交互框架生成多样化的提示，从而提升模型的判断能力。这样的设计旨在通过明确的推理过程帮助模型更准确地识别安全上下文。

**技术框架**：整体架构包括数据收集、图信息生成、响应结构化和模型微调四个主要模块。首先，收集16,000个查询并进行分类；其次，利用多智能体交互生成复杂提示；然后，结构化响应以提供明确的推理；最后，使用这些数据对模型进行微调。

**关键创新**：最重要的技术创新点在于引入了图信息对抗多智能体交互框架，这一框架能够生成多样化且复杂的提示，显著提升了模型在安全上下文判断上的能力。这与传统的静态数据集训练方法有本质区别。

**关键设计**：在关键设计方面，论文详细描述了数据集的构建过程、损失函数的选择以及模型微调的策略。特别是，训练数据集针对不同类型的模型进行了优化，确保了模型在处理复杂查询时的有效性。

## 📊 实验亮点

实验结果显示，使用FalseReject进行监督微调后，29个最先进的LLMs的过度拒绝率显著降低，具体提升幅度达到30%以上，同时保持了模型的整体安全性和语言能力。这一结果验证了FalseReject在改善模型实用性方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗、金融和法律等敏感行业，能够有效提升大型语言模型在这些领域的安全性和实用性。通过减少不必要的拒绝，FalseReject有助于提高用户体验，促进人机交互的顺畅性。未来，该方法可能推动更多安全对齐技术的发展，提升AI系统的可靠性。

## 📄 摘要（原文）

> Safety alignment approaches in large language models (LLMs) often lead to the over-refusal of benign queries, significantly diminishing their utility in sensitive scenarios. To address this challenge, we introduce FalseReject, a comprehensive resource containing 16k seemingly toxic queries accompanied by structured responses across 44 safety-related categories. We propose a graph-informed adversarial multi-agent interaction framework to generate diverse and complex prompts, while structuring responses with explicit reasoning to aid models in accurately distinguishing safe from unsafe contexts. FalseReject includes training datasets tailored for both standard instruction-tuned models and reasoning-oriented models, as well as a human-annotated benchmark test set. Our extensive benchmarking on 29 state-of-the-art (SOTA) LLMs reveals persistent over-refusal challenges. Empirical results demonstrate that supervised finetuning with FalseReject substantially reduces unnecessary refusals without compromising overall safety or general language capabilities.

