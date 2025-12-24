---
layout: default
title: "Intent Factored Generation: Unleashing the Diversity in Your Language Model"
---

# Intent Factored Generation: Unleashing the Diversity in Your Language Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09659" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09659v1</a>
  <a href="https://arxiv.org/pdf/2506.09659.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09659v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09659v1', 'Intent Factored Generation: Unleashing the Diversity in Your Language Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eltayeb Ahmed, Uljad Berdica, Martha Elliott, Danijela Horak, Jakob N. Foerster

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-06-11

---

## 💡 一句话要点

**提出意图分解生成方法以解决语言模型样本多样性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `生成模型` `多样性增强` `意图分解` `对话系统` `强化学习` `内容生成`

## 📋 核心要点

1. 现有方法在生成多样化样本时仅在词元级别进行操作，导致生成的内容缺乏探索性和吸引力。
2. 本文提出的意图分解生成（IFG）方法通过将采样过程分为意图采样和最终响应生成两个阶段，提升了生成的多样性。
3. 实验结果显示，该方法在数学和代码任务上提高了pass@k和基于反馈的强化学习效果，同时在对话生成中保持了高质量。

## 📝 摘要（中文）

从大型语言模型中获取多个有意义且多样化的高质量样本仍然是一个开放性挑战。现有方法通常仅在词元级别上增加多样性，导致生成的响应缺乏探索性和吸引力。为此，本文提出了意图分解生成（IFG）方法，将采样过程分为两个阶段：首先采样语义密集的意图，然后在此基础上生成最终响应。通过这种方式，能够在意图阶段使用较高的温度以促进概念多样性，而在最终生成阶段使用较低的温度以确保输出的一致性。实验结果表明，该方法在多种任务上均表现出色，显著提高了生成的多样性和质量。

## 🔬 方法详解

**问题定义**：本文旨在解决从大型语言模型中生成多样化高质量样本的挑战。现有方法往往在词元级别进行多样性增强，导致生成内容的重复性和缺乏深度。

**核心思路**：论文提出的意图分解生成（IFG）方法通过将生成过程分为两个阶段，首先生成语义意图，然后基于该意图生成最终响应，从而提高生成内容的多样性和一致性。

**技术框架**：IFG方法的整体架构包括两个主要模块：意图采样模块和响应生成模块。在意图采样阶段，使用较高的温度以促进多样性；在响应生成阶段，使用较低的温度以确保输出的连贯性和一致性。

**关键创新**：该方法的创新在于将生成过程分解为意图和响应两个阶段，这一设计使得模型能够在保持生成质量的同时，显著提高样本的多样性。与现有方法相比，IFG能够更好地探索不同的概念和思路。

**关键设计**：在具体实现中，模型在每个生成步骤之前被提示明确其意图，这对于推理任务尤为重要。此外，结合直接偏好优化（DPO）进行指令调优，以增强对话的多样性而不牺牲奖励。

## 📊 实验亮点

实验结果表明，IFG方法在数学和代码任务上显著提高了pass@k和基于反馈的强化学习效果。此外，在对话生成任务中，该方法结合直接偏好优化，成功提升了生成的多样性，同时保持了高质量的输出。

## 🎯 应用场景

该研究的潜在应用领域包括智能对话系统、内容生成和教育辅助工具等。通过提高生成内容的多样性和质量，IFG方法能够提升用户体验，增强人机交互的自然性和有效性。未来，该方法还可能在其他生成任务中发挥重要作用，推动语言模型的进一步发展。

## 📄 摘要（原文）

> Obtaining multiple meaningfully diverse, high quality samples from Large Language Models for a fixed prompt remains an open challenge. Current methods for increasing diversity often only operate at the token-level, paraphrasing the same response. This is problematic because it leads to poor exploration on reasoning problems and to unengaging, repetitive conversational agents. To address this we propose Intent Factored Generation (IFG), factorising the sampling process into two stages. First, we sample a semantically dense intent, e.g., a summary or keywords. Second, we sample the final response conditioning on both the original prompt and the intent from the first stage. This allows us to use a higher temperature during the intent step to promote conceptual diversity, and a lower temperature during the final generation to ensure the outputs are coherent and self-consistent. Additionally, we find that prompting the model to explicitly state its intent for each step of the chain-of-thought before generating the step is beneficial for reasoning tasks. We demonstrate our method's effectiveness across a diverse set of tasks. We show this method improves both pass@k and Reinforcement Learning from Verifier Feedback on maths and code tasks. For instruction-tuning, we combine IFG with Direct Preference Optimisation to increase conversational diversity without sacrificing reward. Finally, we achieve higher diversity while maintaining the quality of generations on a general language modelling task, using a new dataset of reader comments and news articles that we collect and open-source. In summary, we present a simple method of increasing the sample diversity of LLMs while maintaining performance. This method can be implemented by changing the prompt and varying the temperature during generation, making it easy to integrate into many algorithms for gains across various applications.

