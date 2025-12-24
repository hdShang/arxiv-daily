---
layout: default
title: "Auto-Patching: Enhancing Multi-Hop Reasoning in Language Models"
---

# Auto-Patching: Enhancing Multi-Hop Reasoning in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00483" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00483v1</a>
  <a href="https://arxiv.org/pdf/2506.00483.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00483v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00483v1', 'Auto-Patching: Enhancing Multi-Hop Reasoning in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aviv Jan, Dean Tahory, Omer Talmi, Omar Abo Mokh

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-31

**备注**: 8 pages, 5 figures

---

## 💡 一句话要点

**提出Auto-Patch以增强语言模型的多跳推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多跳推理` `语言模型` `动态修补` `PatchScopes` `深度学习` `自然语言处理` `模型优化`

## 📋 核心要点

1. 现有的大型语言模型在处理多跳推理问题时，常常无法有效链接跨多个推理步骤的信息，导致解题率低下。
2. 论文提出的Auto-Patch方法通过动态修补隐藏状态，利用学习到的分类器来选择性地修改内部表示，从而增强多跳推理能力。
3. 在MuSiQue数据集上的实验结果显示，Auto-Patch将解题率从18.45%提升至23.63%，显示出显著的性能提升。

## 📝 摘要（中文）

多跳问题仍然困扰着大型语言模型（LLMs），这些模型在跨多个推理步骤链接信息时表现不佳。我们提出了Auto-Patch，这是一种在推理过程中动态修补隐藏状态的新方法，以增强LLMs的多跳推理能力。基于PatchScopes框架，Auto-Patch使用学习到的分类器选择性地修改内部表示。在MuSiQue数据集上的评估显示，Auto-Patch的解题率从基线的18.45%提升至23.63±0.7%（3次运行），缩小了与链式思维提示（27.44%）之间的差距。我们的结果突显了动态隐藏状态干预在推进LLMs复杂推理中的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在多跳推理中无法有效链接信息的问题。现有方法在处理复杂推理任务时表现不佳，解题率较低。

**核心思路**：Auto-Patch的核心思路是通过动态修补隐藏状态，利用学习到的分类器对内部表示进行选择性修改，以提升模型的推理能力。这样的设计旨在增强模型在多跳推理任务中的表现。

**技术框架**：Auto-Patch基于PatchScopes框架，整体流程包括输入数据的处理、隐藏状态的动态修补和分类器的应用。主要模块包括数据预处理、模型推理和后处理。

**关键创新**：Auto-Patch的主要创新在于动态干预隐藏状态的能力，这与传统方法的静态处理方式有本质区别。通过这种动态修补，模型能够更好地适应复杂的推理任务。

**关键设计**：在技术细节上，Auto-Patch采用了特定的损失函数来优化分类器的性能，并在网络结构中引入了适应性调整机制，以确保隐藏状态的有效修补。

## 📊 实验亮点

实验结果表明，Auto-Patch在MuSiQue数据集上的解题率从基线的18.45%提升至23.63±0.7%，与链式思维提示的27.44%相比，缩小了显著的差距。这一提升展示了动态隐藏状态干预的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的问答系统、对话系统以及复杂信息检索等场景。通过提升多跳推理能力，Auto-Patch能够为这些应用提供更准确的答案和更自然的交互体验，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multi-hop questions still stump large language models (LLMs), which struggle to link information across multiple reasoning steps. We introduce Auto-Patch, a novel method that dynamically patches hidden states during inference to enhance multi-hop reasoning in LLMs. Building on the PatchScopes framework, Auto-Patch selectively modifies internal representations using a learned classifier. Evaluated on the MuSiQue dataset, Auto-Patch improves the solve rate from 18.45\% (baseline) to 23.63~$\pm$~0.7\% (3 runs), narrowing the gap to Chain-of-Thought prompting (27.44\%). Our results highlight the potential of dynamic hidden state interventions for advancing complex reasoning in LLMs.

