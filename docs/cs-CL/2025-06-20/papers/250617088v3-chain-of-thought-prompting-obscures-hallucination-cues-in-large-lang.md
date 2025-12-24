---
layout: default
title: "Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation"
---

# Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17088" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17088v3</a>
  <a href="https://arxiv.org/pdf/2506.17088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17088v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17088v3', 'Chain-of-Thought Prompting Obscures Hallucination Cues in Large Language Models: An Empirical Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Cheng, Tiancheng Su, Jia Yuan, Guoxiu He, Jiawei Liu, Xinqi Tao, Jingwen Xie, Huaxia Li

**分类**: cs.CL

**发布日期**: 2025-06-20 (更新: 2025-09-16)

**备注**: Accepted at EMNLP 2025 Findings

**🔗 代码/项目**: [GITHUB](https://github.com/ECNU-Text-Computing/cot-hallu-detect)

---

## 💡 一句话要点

**提出链式思维提示以解决大型语言模型的幻觉检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `幻觉检测` `链式思维` `逐步推理` `实证评估`

## 📋 核心要点

1. 现有的大型语言模型在生成内容时常常出现幻觉，导致输出不准确的信息，影响实际应用效果。
2. 本文提出通过链式思维提示（CoT）来改善幻觉现象，同时系统评估其对幻觉检测的影响。
3. 实验结果显示，CoT提示能够降低幻觉频率，但也会影响检测信号的清晰度，降低检测方法的有效性。

## 📝 摘要（中文）

大型语言模型（LLMs）常常出现幻觉现象，即生成事实不准确或语义不相关的内容。链式思维（CoT）提示可以通过鼓励逐步推理来减轻幻觉，但其对幻觉检测的影响尚未深入探讨。为此，本文进行了系统的实证评估。通过初步实验发现，CoT推理显著影响LLM的内部状态和标记概率分布。进一步评估了不同CoT提示方法对主流幻觉检测方法的影响，研究了幻觉评分分布的变化、检测准确率的变化以及检测信心的变化。研究结果表明，尽管CoT提示有助于减少幻觉频率，但也会模糊检测所需的关键信号，从而削弱各种检测方法的有效性。该研究揭示了推理使用中的一个被忽视的权衡。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成内容时出现的幻觉现象，现有方法在幻觉检测方面存在信号模糊的问题。

**核心思路**：通过引入链式思维提示（CoT），鼓励模型进行逐步推理，从而改善生成内容的准确性，同时评估其对幻觉检测的影响。

**技术框架**：研究首先进行初步实验，分析CoT推理对模型内部状态的影响，随后评估不同CoT提示方法对幻觉检测的影响，涵盖幻觉评分分布、检测准确率和检测信心等多个维度。

**关键创新**：本研究的创新点在于系统性地揭示了CoT提示在降低幻觉频率的同时，可能会模糊幻觉检测的关键信号，这一权衡在以往研究中未被充分探讨。

**关键设计**：在实验中，设置了多种CoT提示方法，并使用主流的幻觉检测技术进行对比，关注参数设置和模型的推理过程。具体的损失函数和网络结构细节在代码中公开。

## 📊 实验亮点

实验结果表明，链式思维提示能够显著降低幻觉频率，但同时也导致幻觉检测的信号模糊，影响检测准确性。具体数据显示，尽管幻觉频率降低，但检测准确率有所下降，揭示了使用推理的潜在权衡。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和信息检索等。通过改进幻觉检测，能够提升大型语言模型在实际应用中的可靠性和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) often exhibit \textit{hallucinations}, generating factually incorrect or semantically irrelevant content in response to prompts. Chain-of-Thought (CoT) prompting can mitigate hallucinations by encouraging step-by-step reasoning, but its impact on hallucination detection remains underexplored. To bridge this gap, we conduct a systematic empirical evaluation. We begin with a pilot experiment, revealing that CoT reasoning significantly affects the LLM's internal states and token probability distributions. Building on this, we evaluate the impact of various CoT prompting methods on mainstream hallucination detection methods across both instruction-tuned and reasoning-oriented LLMs. Specifically, we examine three key dimensions: changes in hallucination score distributions, variations in detection accuracy, and shifts in detection confidence. Our findings show that while CoT prompting helps reduce hallucination frequency, it also tends to obscure critical signals used for detection, impairing the effectiveness of various detection methods. Our study highlights an overlooked trade-off in the use of reasoning. Code is publicly available at: https://github.com/ECNU-Text-Computing/cot-hallu-detect .

