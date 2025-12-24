---
layout: default
title: "DSMentor: Enhancing Data Science Agents with Curriculum Learning and Online Knowledge Accumulation"
---

# DSMentor: Enhancing Data Science Agents with Curriculum Learning and Online Knowledge Accumulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14163" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14163v1</a>
  <a href="https://arxiv.org/pdf/2505.14163.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14163v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14163v1', 'DSMentor: Enhancing Data Science Agents with Curriculum Learning and Online Knowledge Accumulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: He Wang, Alexander Hanbo Li, Yiqun Hu, Sheng Zhang, Hideo Kobayashi, Jiani Zhang, Henry Zhu, Chung-Wei Hang, Patrick Ng

**分类**: cs.AI

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出DSMentor以优化数据科学代理的推理过程**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `课程学习` `长期记忆` `推理优化` `数据科学代理` `因果推理` `大型语言模型` `智能学习`

## 📋 核心要点

1. 现有方法在推理过程中未充分考虑任务处理顺序，导致数据科学代理的性能未能达到最佳。
2. 论文提出DSMentor框架，通过课程学习策略优化任务处理顺序，并引入长期记忆来提升学习效果。
3. 实验结果显示，DSMentor在DSEval和QRData基准上提高了最多5.2%的通过率，并在因果推理问题上提升了8.8%。

## 📝 摘要（中文）

大型语言模型（LLM）代理在生成代码以解决复杂数据科学问题方面表现出色。然而，现有研究主要集中在通过改进搜索、采样和规划技术来增强上下文学习，忽视了推理过程中问题处理顺序的重要性。本文提出了一种新颖的推理时间优化框架DSMentor，利用课程学习策略，先处理简单任务，再逐步过渡到更复杂的任务，从而提升LLM代理在数据科学任务中的表现。该框架通过组织任务的难度顺序和引入长期记忆来指导学习进程，实验结果表明，DSMentor在DSEval和QRData基准上相比基线代理提高了通过率，尤其在因果推理问题上表现更为突出。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM代理在推理过程中未考虑任务顺序的问题，导致其在复杂数据科学任务中的表现不佳。现有方法往往忽视了学习者在处理问题时的认知负担，未能有效利用先前的经验。

**核心思路**：DSMentor框架的核心思想是采用课程学习策略，先引入简单任务，随着学习者能力的提升逐步过渡到更复杂的任务。这种方法模仿了人类学习过程，强调了知识的积累和利用。

**技术框架**：DSMentor的整体架构包括任务难度排序模块和长期记忆模块。任务难度排序模块负责组织数据科学任务的顺序，而长期记忆模块则用于存储和检索先前的学习经验，以指导后续的学习过程。

**关键创新**：DSMentor的主要创新在于将课程学习与长期记忆结合，形成了一种新的推理优化策略。这种方法与传统的单一任务处理方式有本质区别，能够更有效地提升代理的学习效率和推理能力。

**关键设计**：在设计中，DSMentor采用了动态任务排序算法，并结合了记忆增强机制，以确保代理能够在处理新任务时有效利用历史经验。此外，损失函数的设计也考虑了任务难度的变化，以适应不同阶段的学习需求。

## 📊 实验亮点

实验结果显示，DSMentor在DSEval和QRData基准上相比基线代理提高了最多5.2%的通过率。此外，在因果推理问题上，DSMentor的表现更为突出，相比于使用Program-of-Thoughts提示的GPT-4，提升了8.8%的通过率，显示出更强的因果推理能力。

## 🎯 应用场景

该研究的潜在应用领域包括教育技术、智能辅导系统和数据科学工具等。通过优化数据科学代理的学习过程，DSMentor能够在实际应用中提供更高效的学习支持，帮助用户更好地解决复杂问题，提升工作效率。未来，该方法可能为其他领域的智能代理提供新的思路，推动人工智能在学习和推理方面的进一步发展。

## 📄 摘要（原文）

> Large language model (LLM) agents have shown promising performance in generating code for solving complex data science problems. Recent studies primarily focus on enhancing in-context learning through improved search, sampling, and planning techniques, while overlooking the importance of the order in which problems are tackled during inference. In this work, we develop a novel inference-time optimization framework, referred to as DSMentor, which leverages curriculum learning -- a strategy that introduces simpler task first and progressively moves to more complex ones as the learner improves -- to enhance LLM agent performance in challenging data science tasks. Our mentor-guided framework organizes data science tasks in order of increasing difficulty and incorporates a growing long-term memory to retain prior experiences, guiding the agent's learning progression and enabling more effective utilization of accumulated knowledge. We evaluate DSMentor through extensive experiments on DSEval and QRData benchmarks. Experiments show that DSMentor using Claude-3.5-Sonnet improves the pass rate by up to 5.2% on DSEval and QRData compared to baseline agents. Furthermore, DSMentor demonstrates stronger causal reasoning ability, improving the pass rate by 8.8% on the causality problems compared to GPT-4 using Program-of-Thoughts prompts. Our work underscores the importance of developing effective strategies for accumulating and utilizing knowledge during inference, mirroring the human learning process and opening new avenues for improving LLM performance through curriculum-based inference optimization.

