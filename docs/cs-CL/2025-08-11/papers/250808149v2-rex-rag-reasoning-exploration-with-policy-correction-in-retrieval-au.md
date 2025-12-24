---
layout: default
title: "REX-RAG: Reasoning Exploration with Policy Correction in Retrieval-Augmented Generation"
---

# REX-RAG: Reasoning Exploration with Policy Correction in Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08149" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08149v2</a>
  <a href="https://arxiv.org/pdf/2508.08149.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08149v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08149v2', 'REX-RAG: Reasoning Exploration with Policy Correction in Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wentao Jiang, Xiang Feng, Zengmao Wang, Yong Luo, Pingbo Xu, Zhe Chen, Bo Du, Jing Zhang

**分类**: cs.CL

**发布日期**: 2025-08-11 (更新: 2025-08-12)

**备注**: 17 pages, 4 figures; updated references

**🔗 代码/项目**: [GITHUB](https://github.com/MiliLab/REX-RAG)

---

## 💡 一句话要点

**提出REX-RAG以解决推理路径无效问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `检索增强生成` `推理路径` `策略优化` `问答系统` `重要性采样` `模型性能提升`

## 📋 核心要点

1. 现有方法在策略驱动的轨迹采样中，LLMs常常陷入无效推理路径，导致决策质量下降。
2. REX-RAG通过混合采样策略和策略修正机制，探索替代推理路径并优化策略学习。
3. 在七个问答基准上，REX-RAG在Qwen2.5-3B和Qwen2.5-7B模型上分别提升了5.1%和3.6%的性能。

## 📝 摘要（中文）

强化学习（RL）作为一种强大的范式，正在推动大型语言模型（LLMs）执行复杂推理任务。将RL与检索增强生成（RAG）结合，可以使LLMs动态整合外部知识，从而实现更为明智和稳健的决策。然而，现有方法在策略驱动的轨迹采样中面临重大挑战，LLMs常常陷入无效的推理路径，导致过于自信但错误的结论。为了解决这一问题，本文提出了REX-RAG（推理探索与策略修正框架），该框架在保持严格的策略学习的同时，探索替代推理路径。我们引入了混合采样策略和策略修正机制，显著提升了模型的推理能力。实验结果表明，REX-RAG在多个问答基准上表现优异，平均提升5.1%和3.6%。

## 🔬 方法详解

**问题定义**：本文旨在解决LLMs在策略驱动轨迹采样中陷入无效推理路径的问题，导致决策质量下降。现有方法在探索过程中容易产生过于自信但错误的结论，影响策略优化效果。

**核心思路**：REX-RAG的核心思路是通过引入混合采样策略和策略修正机制，探索替代推理路径，从而提高模型的推理能力和决策质量。混合采样策略结合了新颖的探测采样方法和探索性提示，帮助模型逃离无效路径。

**技术框架**：REX-RAG的整体架构包括两个主要模块：混合采样模块和策略修正模块。混合采样模块负责生成多样化的推理路径，而策略修正模块则通过重要性采样来校正由混合采样引起的分布偏移，确保策略学习的有效性。

**关键创新**：REX-RAG的两大创新点在于混合采样策略和策略修正机制。混合采样策略通过结合探测采样和探索性提示，显著提升了模型的探索能力；而策略修正机制则有效减小了梯度估计偏差，确保了策略学习的稳定性。

**关键设计**：在关键设计上，REX-RAG采用了重要性采样来校正分布偏移，并在损失函数中引入了额外的正则化项，以平衡探索与利用之间的关系。模型结构上，采用了多层Transformer架构，以增强模型的表达能力和推理能力。

## 📊 实验亮点

在七个问答基准上，REX-RAG在Qwen2.5-3B和Qwen2.5-7B模型上分别实现了5.1%和3.6%的性能提升，显示出在多个数据集上的竞争力，超越了多个强基线模型。

## 🎯 应用场景

REX-RAG的研究成果在多个领域具有潜在应用价值，尤其是在需要复杂推理和决策支持的场景，如智能问答系统、对话系统和知识图谱构建等。通过提高模型的推理能力，REX-RAG能够为用户提供更为准确和可靠的信息，推动人工智能在实际应用中的发展。

## 📄 摘要（原文）

> Reinforcement learning (RL) is emerging as a powerful paradigm for enabling large language models (LLMs) to perform complex reasoning tasks. Recent advances indicate that integrating RL with retrieval-augmented generation (RAG) allows LLMs to dynamically incorporate external knowledge, leading to more informed and robust decision making. However, we identify a critical challenge during policy-driven trajectory sampling: LLMs are frequently trapped in unproductive reasoning paths, which we refer to as "dead ends", committing to overconfident yet incorrect conclusions. This severely hampers exploration and undermines effective policy optimization. To address this challenge, we propose REX-RAG (Reasoning Exploration with Policy Correction in Retrieval-Augmented Generation), a novel framework that explores alternative reasoning paths while maintaining rigorous policy learning through principled distributional corrections. Our approach introduces two key innovations: (1) Mixed Sampling Strategy, which combines a novel probe sampling method with exploratory prompts to escape dead ends; and (2) Policy Correction Mechanism, which employs importance sampling to correct distribution shifts induced by mixed sampling, thereby mitigating gradient estimation bias. We evaluate it on seven question-answering benchmarks, and the experimental results show that REX-RAG achieves average performance gains of 5.1% on Qwen2.5-3B and 3.6% on Qwen2.5-7B over strong baselines, demonstrating competitive results across multiple datasets. The code is publicly available at https://github.com/MiliLab/REX-RAG.

