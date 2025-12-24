---
layout: default
title: "Absolute Zero: Reinforced Self-play Reasoning with Zero Data"
---

# Absolute Zero: Reinforced Self-play Reasoning with Zero Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03335" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03335v3</a>
  <a href="https://arxiv.org/pdf/2505.03335.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03335v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03335v3', 'Absolute Zero: Reinforced Self-play Reasoning with Zero Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Zhao, Yiran Wu, Yang Yue, Tong Wu, Quentin Xu, Yang Yue, Matthieu Lin, Shenzhi Wang, Qingyun Wu, Zilong Zheng, Gao Huang

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-06 (更新: 2025-10-16)

---

## 💡 一句话要点

**提出Absolute Zero以解决无数据强化学习中的推理问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `自我学习` `推理能力` `无监督学习` `代码执行` `任务生成` `人工智能` `模型自适应`

## 📋 核心要点

1. 现有的零设置RLVR方法依赖于人工策划的数据，限制了其长期扩展性和适应性。
2. 本文提出的Absolute Zero范式允许模型在没有外部数据的情况下，自主生成和解决任务，从而提升推理能力。
3. AZR在编码和数学推理任务上表现出色，超越了依赖数万条人工示例的现有模型，展示了其广泛的适用性。

## 📝 摘要（中文）

强化学习与可验证奖励（RLVR）在提升大型语言模型推理能力方面展现出潜力。现有的零设置RLVR方法依赖于人工策划的问题和答案进行训练，缺乏高质量的人工示例限制了其长期扩展性。为了解决这一问题，本文提出了一种新的RLVR范式Absolute Zero，允许模型在没有外部数据的情况下，自主提出任务以最大化学习进展，并通过解决这些任务来提升推理能力。我们引入了Absolute Zero Reasoner（AZR），该系统通过代码执行器自我进化训练课程和推理能力，验证提出的代码推理任务和答案，成为可验证奖励的统一来源。AZR在编码和数学推理任务上实现了SOTA性能，超越了依赖大量人工策划示例的现有模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有零设置RLVR方法对人工数据的依赖问题，限制了模型的学习能力和扩展性。

**核心思路**：提出Absolute Zero范式，允许模型自主生成任务并通过解决这些任务来提升自身的推理能力，完全不依赖外部数据。

**技术框架**：AZR系统包含任务生成模块、代码执行器和验证模块，模型通过自我进化的方式不断优化训练课程和推理能力。

**关键创新**：AZR的最大创新在于其完全不依赖外部数据的学习方式，通过自我生成和验证任务来实现学习，区别于传统方法依赖人工策划示例。

**关键设计**：AZR使用特定的损失函数来优化任务生成和验证过程，网络结构设计上兼容多种模型规模，确保其在不同任务上的适应性和性能。

## 📊 实验亮点

AZR在编码和数学推理任务上实现了SOTA性能，显著超越了依赖数万条人工策划示例的现有模型，展示了在无数据学习环境下的强大能力和灵活性。

## 🎯 应用场景

该研究的潜在应用领域包括自动化编程、智能问答系统和复杂问题解决等。通过自主学习和推理，AZR能够在没有人工干预的情况下不断提升其能力，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Reinforcement learning with verifiable rewards (RLVR) has shown promise in enhancing the reasoning capabilities of large language models by learning directly from outcome-based rewards. Recent RLVR works that operate under the zero setting avoid supervision in labeling the reasoning process, but still depend on manually curated collections of questions and answers for training. The scarcity of high-quality, human-produced examples raises concerns about the long-term scalability of relying on human supervision, a challenge already evident in the domain of language model pretraining. Furthermore, in a hypothetical future where AI surpasses human intelligence, tasks provided by humans may offer limited learning potential for a superintelligent system. To address these concerns, we propose a new RLVR paradigm called Absolute Zero, in which a single model learns to propose tasks that maximize its own learning progress and improves reasoning by solving them, without relying on any external data. Under this paradigm, we introduce the Absolute Zero Reasoner (AZR), a system that self-evolves its training curriculum and reasoning ability by using a code executor to both validate proposed code reasoning tasks and verify answers, serving as an unified source of verifiable reward to guide open-ended yet grounded learning. Despite being trained entirely without external data, AZR achieves overall SOTA performance on coding and mathematical reasoning tasks, outperforming existing zero-setting models that rely on tens of thousands of in-domain human-curated examples. Furthermore, we demonstrate that AZR can be effectively applied across different model scales and is compatible with various model classes.

