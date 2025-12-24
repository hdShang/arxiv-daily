---
layout: default
title: "Pay What LLM Wants: Can LLM Simulate Economics Experiment with 522 Real-human Persona?"
---

# Pay What LLM Wants: Can LLM Simulate Economics Experiment with 522 Real-human Persona?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03262" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03262v1</a>
  <a href="https://arxiv.org/pdf/2508.03262.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03262v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03262v1', 'Pay What LLM Wants: Can LLM Simulate Economics Experiment with 522 Real-human Persona?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhyuk Choi, Hyeonchu Park, Haemin Lee, Hyebeen Shin, Hyun Joung Jin, Bugeun Kim

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-05

**备注**: Preprint

---

## 💡 一句话要点

**通过真实人类数据评估LLM在经济决策模拟中的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `经济决策` `真实人类数据` `多模态学习` `个体预测` `群体行为` `提示技术`

## 📋 核心要点

1. 现有研究多依赖虚构人物，缺乏对真实人类经济决策的有效模拟，限制了LLMs的应用。
2. 本文通过真实人类数据，系统评估LLMs在经济决策模拟中的表现，比较不同人物注入方法的效果。
3. 实验结果表明，LLMs在个体预测上存在挑战，但在群体行为趋势上表现良好，提示技术的改进效果有限。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展引发了对其模拟人类行为能力的广泛关注，但大多数研究依赖于虚构的人物而非实际人类数据。本文通过对522名真实人类参与者的“随意支付”（PWYW）定价实验进行评估，探讨LLMs在个体经济决策预测中的能力。研究系统比较了三种最先进的多模态LLMs，分析了个体选择的再现能力及人物注入方法对预测性能的影响。结果显示，尽管LLMs在个体层面的预测上存在困难，但在群体层面的行为趋势上表现合理。此外，常用的提示技术与简单提示方法相比并无显著提升。我们认为这些发现为LLMs在使用真实人类数据模拟经济行为的能力提供了首次全面评估，为计算社会科学中的基于人物的模拟提供了实证指导。

## 🔬 方法详解

**问题定义**：本文旨在解决LLMs在模拟真实人类经济决策时的不足，尤其是缺乏基于真实数据的评估，现有方法多依赖虚构人物，导致结果的局限性。

**核心思路**：通过使用522名真实参与者的PWYW定价实验数据，评估LLMs在个体经济决策预测中的能力，并探讨不同人物注入方法对预测性能的影响。

**技术框架**：研究采用三种最先进的多模态LLMs，结合详细的人物信息进行比较，主要模块包括数据收集、模型训练、预测评估和结果分析。

**关键创新**：本研究的创新在于首次使用真实人类数据全面评估LLMs的经济行为模拟能力，揭示了个体预测的局限性和群体行为的合理性。

**关键设计**：在实验中，采用了多种提示技术进行模型训练，比较了常用提示与简单提示方法的效果，发现后者在性能上并无显著提升。具体的参数设置和损失函数设计未在摘要中详细说明，需参考原文。

## 📊 实验亮点

实验结果显示，LLMs在个体层面的预测准确性较低，但在群体行为趋势上表现合理。常用的提示技术与简单提示方法相比，未能显著提升预测性能，表明在人物注入方法上的改进空间有限。

## 🎯 应用场景

该研究的潜在应用领域包括市场营销、消费者行为分析和经济学研究等。通过更准确地模拟人类经济决策，LLMs可以为企业提供更有效的定价策略和市场预测，推动计算社会科学的发展。未来可能影响政策制定和商业决策的方式。

## 📄 摘要（原文）

> Recent advances in Large Language Models (LLMs) have generated significant interest in their capacity to simulate human-like behaviors, yet most studies rely on fictional personas rather than actual human data. We address this limitation by evaluating LLMs' ability to predict individual economic decision-making using Pay-What-You-Want (PWYW) pricing experiments with real 522 human personas. Our study systematically compares three state-of-the-art multimodal LLMs using detailed persona information from 522 Korean participants in cultural consumption scenarios. We investigate whether LLMs can accurately replicate individual human choices and how persona injection methods affect prediction performance. Results reveal that while LLMs struggle with precise individual-level predictions, they demonstrate reasonable group-level behavioral tendencies. Also, we found that commonly adopted prompting techniques are not much better than naive prompting methods; reconstruction of personal narrative nor retrieval augmented generation have no significant gain against simple prompting method. We believe that these findings can provide the first comprehensive evaluation of LLMs' capabilities on simulating economic behavior using real human data, offering empirical guidance for persona-based simulation in computational social science.

