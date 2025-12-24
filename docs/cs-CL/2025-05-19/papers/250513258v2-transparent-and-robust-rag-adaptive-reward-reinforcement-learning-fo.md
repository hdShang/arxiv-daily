---
layout: default
title: Transparent and Robust RAG: Adaptive-Reward Reinforcement Learning for Decision Traceability
---

# Transparent and Robust RAG: Adaptive-Reward Reinforcement Learning for Decision Traceability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13258" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13258v2</a>
  <a href="https://arxiv.org/pdf/2505.13258.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13258v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13258v2', 'Transparent and Robust RAG: Adaptive-Reward Reinforcement Learning for Decision Traceability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jingyi Ren, Yekun Xu, Xiaolong Wang, Weitao Li, Weizhi Ma, Yang Liu

**分类**: cs.CL

**发布日期**: 2025-05-19 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出ARENA以解决RAG生成中的透明性与稳定性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `检索增强生成` `强化学习` `透明性` `稳定性` `自适应奖励` `多跳问答` `结构化推理`

## 📋 核心要点

1. 现有的RAG生成方法在透明性方面不足，无法明确指出推理过程中使用的引用，限制了解释性和可见性。
2. 本文提出的ARENA框架通过自适应奖励机制和KL散度稳定化模块，提升了RAG生成器的透明性和稳定性。
3. 在多个基准测试中，ARENA在多跳问答数据集上实现了10-30%的准确率提升，表现与先进的闭源大模型相当。

## 📝 摘要（中文）

检索增强生成（RAG）在知识密集型应用中具有重要价值，但现有方法在透明性和稳定性方面存在不足。本文提出了自适应奖励证据导航代理（ARENA），通过设计奖励来训练RAG生成器，解决了引用透明性和训练不稳定性的问题。ARENA能够识别关键证据，进行结构化推理，并生成可解释的决策轨迹。实验结果表明，ARENA在多个多跳问答数据集上实现了10-30%的准确率提升，并且在未见数据集和任务上具有良好的泛化能力。

## 🔬 方法详解

**问题定义**：现有的RAG生成方法在推理过程中缺乏透明性，无法明确指出所用的引用，导致解释性不足。此外，现有的基于强化学习的方法在训练过程中可能出现梯度尖峰，导致不稳定性。

**核心思路**：ARENA通过设计自适应奖励和KL散度稳定化机制，旨在提升RAG生成器的透明性和训练稳定性，使其能够识别关键证据并进行结构化推理。

**技术框架**：ARENA框架包括三个主要模块：自适应奖励计算模块、KL散度稳定化模块和结构化推理模块。自适应奖励模块根据生成的答案和引用的质量动态调整奖励，KL散度模块则用于平滑训练过程。

**关键创新**：ARENA的主要创新在于其自适应奖励机制和KL散度稳定化设计，使得生成器不仅能够提供可解释的决策轨迹，还能在训练过程中保持稳定性。这与传统方法的静态奖励和不稳定训练过程形成鲜明对比。

**关键设计**：在参数设置上，ARENA采用了动态调整的奖励函数，结合了生成质量和引用有效性。同时，网络结构上引入了多层次的推理模块，以增强模型的推理能力和透明性。通过这些设计，ARENA能够在多跳问答任务中表现出色。

## 📊 实验亮点

ARENA在多个多跳问答数据集上实现了10-30%的准确率提升，表现优于多个基准模型，并且在未见数据集上展现出良好的泛化能力。这些结果表明，ARENA在透明性和稳定性方面的创新设计显著提升了RAG生成器的性能。

## 🎯 应用场景

ARENA的研究成果在知识密集型应用中具有广泛的潜在应用价值，如智能问答系统、知识图谱构建和信息检索等领域。其透明性和稳定性提升将有助于增强用户对AI系统的信任，推动更广泛的实际应用。未来，ARENA的设计理念也可能被应用于其他类型的生成模型中，促进更高效的推理和决策过程。

## 📄 摘要（原文）

> Retrieval-Augmented Generation (RAG) delivers substantial value in knowledge-intensive applications. Many recent works use reinforcement learning (RL) to elicit strong reasoning in RAG generators. However, two key challenges remain unresolved: (1) Transparency: most prior methods do not explicitly indicate which references are actually used during the reasoning that leads to the final answer, limiting interpretability and visibility; (2) Stability: the KL divergence estimator used in existing RL-based approaches may cause gradient spikes, leading to unstable training. To address these challenges, we propose Adaptive-Rewarded Evidence Navigation Agent (ARENA), a transparent and robust RAG generator framework trained via RL with designed rewards. Based on our structured protocol, KL divergence stabilization, and adaptive reward calculation modules, ARENA enables the RAG generator to identify key evidence, perform structured reasoning, and generate answers with interpretable decision traces. Applied to Qwen2.5-7B-Instruct and Llama3.1-8B-Instruct, extensive experiments across multiple baselines show 10-30% accuracy improvements on three multi-hop QA datasets, comparable to advanced closed-source LLMs (e.g., OpenAI o1, DeepSeek R1). Further analyses show that ARENA generalizes well to unseen datasets and tasks. Our models and codes are publicly released.

