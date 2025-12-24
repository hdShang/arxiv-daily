---
layout: default
title: "History Rhymes: Accelerating LLM Reinforcement Learning with RhymeRL"
---

# History Rhymes: Accelerating LLM Reinforcement Learning with RhymeRL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.18588" class="toolbar-btn" target="_blank">📄 arXiv: 2508.18588v1</a>
  <a href="https://arxiv.org/pdf/2508.18588.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.18588v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.18588v1', 'History Rhymes: Accelerating LLM Reinforcement Learning with RhymeRL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingkai He, Tianjian Li, Erhu Feng, Dong Du, Qian Liu, Tao Liu, Yubin Xia, Haibo Chen

**分类**: cs.LG, cs.DC

**发布日期**: 2025-08-26

---

## 💡 一句话要点

**提出RhymeRL以解决大语言模型强化学习中的GPU利用率低下问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `强化学习` `GPU利用率` `HistoSpec` `HistoPipe` `训练效率` `推理能力`

## 📋 核心要点

1. 现有的强化学习方法在GPU利用率上存在显著不足，主要由于回滚阶段的主导性和回滚长度的不平衡。
2. 本文提出RhymeRL，通过HistoSpec和HistoPipe两项创新，利用历史回滚的相似性来加速回滚生成和优化工作负载。
3. 在实际生产环境中，RhymeRL实现了从数十到数千个GPU的可扩展性，性能提升达到2.6倍，且不影响训练精度。

## 📝 摘要（中文）

随着大语言模型（LLMs）的快速发展，强化学习（RL）成为提升LLMs推理能力的重要方法。然而，现有RL系统面临GPU利用率低下的问题，主要由于回滚阶段主导了整个RL过程，以及同一批次内回滚长度的不平衡。尽管以往的解决方案如异步执行和截断提供了部分缓解，但可能会牺牲训练精度。基于历史回滚响应的相似性，本文提出了RhymeRL，通过HistoSpec和HistoPipe两项创新加速RL训练。实验结果表明，RhymeRL在不影响精度的情况下，实现了2.6倍的性能提升。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型强化学习中GPU利用率低下的问题，现有方法在回滚阶段的主导性和回滚长度的不平衡导致了GPU资源的浪费。

**核心思路**：通过观察到的历史回滚响应相似性，提出RhymeRL系统，利用HistoSpec和HistoPipe优化回滚生成和调度策略，从而加速RL训练。

**技术框架**：RhymeRL的整体架构包括两个主要模块：HistoSpec用于生成回滚草稿，HistoPipe用于调度回滚工作，确保负载均衡。

**关键创新**：HistoSpec通过历史回滚序列的相似性生成准确的回滚草稿，而HistoPipe则通过两级调度策略解决了回滚气泡问题，这些创新显著提升了训练效率。

**关键设计**：在HistoSpec中，采用了基于历史数据的推测解码引擎；在HistoPipe中，设计了基于历史回滚分布的负载均衡策略，确保各个回滚工作者的工作量均衡。

## 📊 实验亮点

实验结果表明，RhymeRL在实际生产环境中实现了2.6倍的性能提升，相较于现有方法，显著提高了GPU的利用率，同时保持了训练的准确性，未对RL范式进行修改。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能助手等，能够显著提升大语言模型在实际应用中的推理能力和训练效率。未来，RhymeRL可能推动更大规模的模型训练，使得复杂任务的处理更加高效。

## 📄 摘要（原文）

> With the rapid advancement of large language models (LLMs), reinforcement learning (RL) has emerged as a pivotal methodology for enhancing the reasoning capabilities of LLMs. Unlike traditional pre-training approaches, RL encompasses multiple stages: rollout, reward, and training, which necessitates collaboration among various worker types. However, current RL systems continue to grapple with substantial GPU underutilization, due to two primary factors: (1) The rollout stage dominates the overall RL process due to test-time scaling; (2) Imbalances in rollout lengths (within the same batch) result in GPU bubbles. While prior solutions like asynchronous execution and truncation offer partial relief, they may compromise training accuracy for efficiency.
>   Our key insight stems from a previously overlooked observation: rollout responses exhibit remarkable similarity across adjacent training epochs. Based on the insight, we introduce RhymeRL, an LLM RL system designed to accelerate RL training with two key innovations. First, to enhance rollout generation, we present HistoSpec, a speculative decoding inference engine that utilizes the similarity of historical rollout token sequences to obtain accurate drafts. Second, to tackle rollout bubbles, we introduce HistoPipe, a two-tier scheduling strategy that leverages the similarity of historical rollout distributions to balance workload among rollout workers. We have evaluated RhymeRL within a real production environment, demonstrating scalability from dozens to thousands of GPUs. Experimental results demonstrate that RhymeRL achieves a 2.6x performance improvement over existing methods, without compromising accuracy or modifying the RL paradigm.

