---
layout: default
title: "From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents"
---

# From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23071" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23071v1</a>
  <a href="https://arxiv.org/pdf/2509.23071.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23071v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23071v1', 'From Evidence to Trajectory: Abductive Reasoning Path Synthesis for Training Retrieval-Augmented Generation Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muzhi Li, Jinhu Qi, Yihong Wu, Minghao Zhao, Liheng Ma, Yifan Li, Xinyu Wang, Yingxue Zhang, Ho-fung Leung, Irwin King

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-27

---

## 💡 一句话要点

**提出EviPath，通过证据增强的推理路径合成，提升RAG Agent的训练效果。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `RAG Agent` `检索增强生成` `推理路径合成` `演绎推理` `对话式微调`

## 📋 核心要点

1. 现有RAG Agent训练缺乏过程级监督，导致任务分解和决策能力不足，强化学习方法面临奖励稀疏问题。
2. EviPath通过演绎式子任务规划、忠实子问题回答和对话式微调，合成高质量的Agent-环境交互轨迹。
3. 实验表明，使用EviPath训练的80亿参数模型在开放域问答中显著优于现有方法，EM值提升14.7%。

## 📝 摘要（中文）

检索增强生成（RAG）Agent的开发受到缺乏过程级监督的阻碍，难以有效指导Agent的任务分解、检索器调用和逐步决策等能力。强化学习虽然是一种潜在的解决方案，但面临奖励稀疏和大语言模型（LLM）推理能力有限的问题。同时，现有的数据合成方法仅生成思维链推理，无法模拟环境交互。本文提出了EviPath，一种用于RAG Agent开发的证据锚定推理路径合成范式。EviPath包括：（i）演绎式子任务规划，将问题分解为子问题，并基于它们之间的依赖关系迭代地规划最优解决方案路径；（ii）忠实的子问题回答，使用支持性证据构建代理环境，为每个子问题生成推理思路和答案；（iii）对话式微调，将完整的Agent-环境交互轨迹格式化为适合监督微调的对话格式。EviPath使LLM能够直接从合成数据中学习复杂的推理和工具使用能力。在广泛使用的问答基准上的大量实验表明，使用EviPath合成数据训练的80亿参数模型，显著且持续地优于最先进的基线，在开放域问答中获得了14.7%的绝对EM增益。

## 🔬 方法详解

**问题定义**：现有RAG Agent的训练面临缺乏过程级监督的问题，难以有效地指导Agent进行任务分解、检索器调用和逐步决策。强化学习方法虽然可以尝试解决这个问题，但由于奖励稀疏以及大语言模型本身推理能力的限制，效果并不理想。此外，现有的数据合成方法通常只关注生成思维链式的推理过程，而忽略了Agent与环境之间的交互。

**核心思路**：EviPath的核心思路是通过合成高质量的Agent-环境交互轨迹来解决RAG Agent训练中缺乏过程级监督的问题。它通过演绎式子任务规划将复杂问题分解为一系列相互依赖的子问题，然后利用证据构建代理环境来生成每个子问题的推理思路和答案，最后将整个交互过程转化为对话形式，方便进行监督微调。这样设计的目的是让Agent能够从合成数据中学习到复杂的推理和工具使用能力。

**技术框架**：EviPath包含三个主要模块：
1. **演绎式子任务规划（Abductive Subtask Planning）**：将原始问题分解为一系列子问题，并规划出解决这些子问题的最优路径。这个过程考虑到子问题之间的依赖关系，确保最终能够得到完整的解决方案。
2. **忠实的子问题回答（Faithful Sub-question Answering）**：利用检索到的证据构建一个代理环境，然后基于这个环境生成每个子问题的推理过程和答案。这个模块的目标是确保生成的答案是基于可靠的证据，并且推理过程是可信的。
3. **对话式微调（Conversational Fine-Tuning）**：将Agent与环境的完整交互轨迹转化为对话形式，然后使用这些数据对大语言模型进行监督微调。这样可以使模型更好地学习如何进行对话式的交互，并提高其推理和工具使用能力。

**关键创新**：EviPath的关键创新在于它提出了一种证据锚定的推理路径合成范式，能够生成高质量的Agent-环境交互轨迹。与现有的数据合成方法相比，EviPath不仅关注推理过程，还模拟了Agent与环境之间的交互，从而使Agent能够更好地学习如何进行复杂的推理和工具使用。此外，EviPath还采用了演绎式子任务规划的方法，能够有效地将复杂问题分解为一系列可解决的子问题。

**关键设计**：在演绎式子任务规划中，需要设计合适的算法来分解问题并规划最优路径。在忠实的子问题回答中，需要选择合适的证据检索方法和代理环境构建方法。在对话式微调中，需要设计合适的对话格式和损失函数。论文中可能包含关于这些方面的具体技术细节，但摘要中未明确提及。

## 📊 实验亮点

实验结果表明，使用EviPath合成数据训练的80亿参数模型在开放域问答任务中取得了显著的性能提升，相对于最先进的基线方法，获得了14.7%的绝对EM增益。这一结果表明EviPath方法能够有效地提升RAG Agent的推理和工具使用能力，并使其在实际应用中表现出更强的竞争力。

## 🎯 应用场景

EviPath方法可以广泛应用于各种需要RAG Agent的场景，例如开放域问答、知识图谱推理、智能客服等。通过合成高质量的训练数据，可以显著提升Agent的推理和工具使用能力，从而提高其在实际应用中的性能和可靠性。该研究的成果有助于推动RAG Agent技术的发展，并为构建更智能、更高效的AI系统提供新的思路。

## 📄 摘要（原文）

> Retrieval-augmented generation agents development is hindered by the lack of process-level supervision to effectively guide agentic capabilities like task decomposition, retriever invocation, and stepwise decision-making. While reinforcement learning offers a potential solution, it suffers from sparse rewards and the limited reasoning capabilities of large language models (LLMs). Meanwhile, existing data synthesis methods only produce chain-of-thought rationales and fail to model environmental interactions. In this paper, we propose EviPath, an evidence-anchored reasoning path synthesis paradigm for RAG agent development. EviPath comprises: (i) Abductive Subtask Planning, which decomposes the problem into sub-questions and iteratively plans an optimal solution path based on the dependencies between them; (ii) Faithful Sub-question Answering, which uses supporting evidence to construct a proxy environment to generate reasoning thoughts and answers for each sub-question; and (iii) Conversational Fine-Tuning, which formats the complete agent-environment interaction trajectory into a dialogue format suitable for Supervised Fine-Tuning. EviPath allows LLMs to learn complex reasoning and tool-use capabilities directly from synthesized data. Extensive experiments on widely-used question-answering benchmarks show that an 8B parameter model trained with EviPath-synthesized data significantly and consistently outperforms state-of-the-art baselines with a double-digit absolute EM gain of 14.7% in open-domain question answering.

