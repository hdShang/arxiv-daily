---
layout: default
title: MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability
---

# MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20285" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20285v2</a>
  <a href="https://arxiv.org/pdf/2505.20285.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20285v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20285v2', 'MaskSearch: A Universal Pre-Training Framework to Enhance Agentic Search Capability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiqi Wu, Xin Guan, Shen Huang, Yong Jiang, Pengjun Xie, Fei Huang, Jiuxin Cao, Hai Zhao, Jingren Zhou

**分类**: cs.CL

**发布日期**: 2025-05-26 (更新: 2025-05-27)

**备注**: Code is available at https://github.com/Alibaba-NLP/MaskSearch

---

## 💡 一句话要点

**提出MaskSearch框架以增强智能搜索能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `检索增强模型` `预训练框架` `智能搜索` `多跳问答` `强化学习` `监督微调` `课程学习`

## 📋 核心要点

1. 现有方法在智能搜索能力上受限于任务特定数据，无法有效提升通用性。
2. 提出MaskSearch框架，通过RAMP任务使模型学习利用搜索工具填充掩码，从而增强检索和推理能力。
3. 实验结果表明，MaskSearch在开放域多跳问答任务中显著提升了LLM搜索代理的性能，验证了其有效性。

## 📝 摘要（中文）

检索增强语言模型（RALMs）是一种经典范式，通过专门模块利用外部知识来增强生成能力。尽管现有训练方法展现出潜力，但其智能能力受到任务特定数据的限制。为此，本文提出了一种新颖的预训练框架MaskSearch。在预训练阶段，引入了检索增强掩码预测（RAMP）任务，使模型能够利用搜索工具填充大量预训练数据中的掩码，从而获得通用的检索和推理能力。模型在下游任务上进一步训练，结合监督微调和强化学习，最终在开放域多跳问答场景中显著提升了基于LLM的搜索代理的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有智能搜索代理在通用性和能力上的不足，尤其是受限于任务特定数据的训练方法。

**核心思路**：通过引入检索增强掩码预测（RAMP）任务，使模型在预训练阶段学习如何利用搜索工具填充掩码，从而获得更强的检索和推理能力。

**技术框架**：整体框架包括预训练阶段和下游任务训练阶段。在预训练阶段，模型通过RAMP任务学习；在下游任务中，结合监督微调（SFT）和强化学习（RL）进行进一步训练。

**关键创新**：最重要的创新在于RAMP任务的引入，使模型能够在大规模数据上学习通用的检索能力，而不是仅依赖于特定任务的数据。

**关键设计**：在SFT中，采用多代理系统生成训练数据，结合规划者、重写者和观察者；在RL中，使用DAPO框架和混合奖励系统，设计了逐步学习的课程学习方法。

## 📊 实验亮点

实验结果显示，MaskSearch在开放域多跳问答任务中，相较于基线模型，性能提升显著，具体提升幅度达到XX%（具体数据待补充），验证了其在不同领域的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括开放域问答系统、智能助手和信息检索等。通过提升模型的检索和推理能力，MaskSearch能够在多种实际场景中提供更为准确和高效的搜索结果，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Retrieval-Augmented Language Models (RALMs) represent a classic paradigm where models enhance generative capabilities using external knowledge retrieved via a specialized module. Recent advancements in Agent techniques enable Large Language Models (LLMs) to autonomously utilize tools for retrieval, planning, and reasoning. While existing training-based methods show promise, their agentic abilities are limited by inherent characteristics of the task-specific data used during training. To further enhance the universal search capability of agents, we propose a novel pre-training framework, MaskSearch. In the pre-training stage, we introduce the Retrieval Augmented Mask Prediction (RAMP) task, where the model learns to leverage search tools to fill masked spans on a large number of pre-training data, thus acquiring universal retrieval and reasoning capabilities for LLMs. After that, the model is trained on downstream tasks to achieve further improvement. We apply both Supervised Fine-tuning (SFT) and Reinforcement Learning (RL) for training. For SFT, we combine agent-based and distillation-based methods to generate training data, starting with a multi-agent system consisting of a planner, rewriter, observer, and followed by a self-evolving teacher model. While for RL, we employ DAPO as the training framework and adopt a hybrid reward system consisting of answer rewards and format rewards. Additionally, we introduce a curriculum learning approach that allows the model to learn progressively from easier to more challenging instances based on the number of masked spans. We evaluate the effectiveness of our framework in the scenario of open-domain multi-hop question answering. Through extensive experiments, we demonstrate that MaskSearch significantly enhances the performance of LLM-based search agents on both in-domain and out-of-domain downstream tasks.

