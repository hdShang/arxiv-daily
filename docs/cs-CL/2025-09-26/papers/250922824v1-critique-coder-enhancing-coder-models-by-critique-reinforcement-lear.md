---
layout: default
title: "Critique-Coder: Enhancing Coder Models by Critique Reinforcement Learning"
---

# Critique-Coder: Enhancing Coder Models by Critique Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22824" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22824v1</a>
  <a href="https://arxiv.org/pdf/2509.22824.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22824v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22824v1', 'Critique-Coder: Enhancing Coder Models by Critique Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi Ruan, Dongfu Jiang, Yubo Wang, Wenhu Chen

**分类**: cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出Critique-Coder，通过批判强化学习提升代码生成模型性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `代码生成` `强化学习` `批判学习` `大型语言模型` `推理能力`

## 📋 核心要点

1. 现有强化学习方法在训练代码生成模型时，缺乏对模型批判和反思能力的明确培养。
2. 提出批判强化学习(CRL)，通过让模型生成对代码的批判并根据批判的正确性进行奖励，来提升模型的推理能力。
3. Critique-Coder在代码生成和通用推理任务上均优于仅使用RL训练的模型，表明CRL能够有效提升模型的推理和批判能力。

## 📝 摘要（中文）

强化学习(RL)已成为一种流行的训练范式，尤其是在与推理模型结合使用时。然而，它主要关注生成响应，缺乏明确培养批判或反思的机制。最近的一些研究表明，明确地教导大型语言模型(LLM)如何进行批判是有益的。受此启发，我们提出了批判强化学习(CRL)，其中模型被要求为给定的(问题，解决方案)对生成批判。奖励完全取决于生成的批判的最终判断标签是否与真实判断一致。在此基础上，我们引入了Critique-Coder，它通过将20%的标准RL数据替换为CRL数据，在RL和CRL的混合数据上进行训练。我们在不同的基准上对多个模型(Critique-Coder)进行微调和评估，以展示它们相对于仅使用RL的模型的优势。结果表明，Critique-Coder在所有评估的基准上始终优于仅使用RL的基线。值得注意的是，我们的Critique-Coder-8B在LiveCodeBench (v5)上可以达到60%以上，优于其他推理模型，如DeepCoder-14B和GPT-o1。除了代码生成，Critique-Coder还表现出增强的通用推理能力，这体现在其在BBEH数据集中的逻辑推理任务上的更好性能。这表明在编码数据集上应用CRL可以增强通用推理和批判能力，这些能力可以跨广泛的任务转移。因此，我们认为CRL是LLM推理的标准RL的一个很好的补充。

## 🔬 方法详解

**问题定义**：论文旨在解决代码生成模型缺乏有效批判和反思能力的问题。现有强化学习方法主要关注生成正确的代码，而忽略了模型对自身代码进行评估和改进的能力，导致模型在复杂任务上的表现受限。

**核心思路**：论文的核心思路是通过引入批判环节，让模型学习如何评估和改进自身生成的代码。具体来说，模型需要为给定的问题和解决方案生成批判，并根据批判的正确性获得奖励。这种方式能够促使模型更深入地理解问题和解决方案，从而提升代码生成的质量。

**技术框架**：Critique-Coder的训练框架是基于强化学习的。在标准的强化学习训练过程中，论文引入了批判强化学习(CRL)的数据。具体来说，将20%的标准RL数据替换为CRL数据。在CRL阶段，模型接收问题和解决方案作为输入，生成对解决方案的批判，并根据批判的正确性获得奖励。最终的模型通过混合RL和CRL的数据进行训练。

**关键创新**：论文的关键创新在于提出了批判强化学习(CRL)的概念，并将其应用于代码生成模型的训练中。与传统的强化学习方法相比，CRL能够更有效地提升模型的推理和批判能力。此外，Critique-Coder通过混合RL和CRL的数据进行训练，实现了性能的提升。

**关键设计**：在CRL阶段，奖励函数的设计至关重要。论文采用的奖励函数是基于生成的批判的最终判断标签是否与真实判断一致。如果生成的批判是正确的，则给予正向奖励；否则，给予负向奖励。这种奖励函数能够有效地引导模型学习如何生成正确的批判。

## 📊 实验亮点

Critique-Coder在LiveCodeBench (v5)上达到了超过60%的准确率，优于DeepCoder-14B和GPT-o1等其他推理模型。此外，Critique-Coder在BBEH数据集的逻辑推理任务上也表现出更好的性能，表明该方法能够提升模型的通用推理能力。实验结果表明，CRL能够有效提升代码生成模型的性能。

## 🎯 应用场景

该研究成果可应用于各种代码生成场景，例如自动化软件开发、代码补全、程序修复等。通过提升代码生成模型的推理和批判能力，可以提高代码生成的质量和效率，降低软件开发的成本。此外，该方法还可以推广到其他需要推理和批判能力的领域，例如自然语言处理、问答系统等。

## 📄 摘要（原文）

> Reinforcement Learning (RL) has emerged as a popular training paradigm, particularly when paired with reasoning models. While effective, it primarily focuses on generating responses and lacks mechanisms to explicitly foster critique or reflection. Several recent studies, like Critique-Fine-Tuning (CFT) and Critique-Guided-Distillation (CGD) have shown the benefits of explicitly teaching LLMs how to critique. Motivated by them, we propose Critique Reinforcement Learning (CRL), where the model is tasked with generating a critique for a given (question, solution) pair. The reward is determined solely by whether the final judgment label $c \in \{\texttt{True}, \texttt{False}\}$ of the generated critique aligns with the ground-truth judgment $c^*$. Building on this point, we introduce \textsc{Critique-Coder}, which is trained on a hybrid of RL and CRL by substituting 20\% of the standard RL data with CRL data. We fine-tune multiple models (\textsc{Critique-Coder}) and evaluate them on different benchmarks to show their advantages over RL-only models. We show that \textsc{Critique-Coder} consistently outperforms RL-only baselines on all the evaluated benchmarks. Notably, our \textsc{Critique-Coder-8B} can reach over 60\% on LiveCodeBench (v5), outperforming other reasoning models like DeepCoder-14B and GPT-o1. Beyond code generation, \textsc{Critique-Coder} also demonstrates enhanced general reasoning abilities, as evidenced by its better performance on logic reasoning tasks from the BBEH dataset. This indicates that the application of CRL on coding datasets enhances general reasoning and critique abilities, which are transferable across a broad range of tasks. Hence, we believe that CRL works as a great complement to standard RL for LLM reasoning.

