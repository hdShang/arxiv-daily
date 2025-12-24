---
layout: default
title: "Fin-PRM: A Domain-Specialized Process Reward Model for Financial Reasoning in Large Language Models"
---

# Fin-PRM: A Domain-Specialized Process Reward Model for Financial Reasoning in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15202" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15202v1</a>
  <a href="https://arxiv.org/pdf/2508.15202.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15202v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15202v1', 'Fin-PRM: A Domain-Specialized Process Reward Model for Financial Reasoning in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuanchen Zhou, Shuo Jiang, Jie Zhu, Junhui Li, Lifan Guo, Feng Chen, Chi Zhang

**分类**: cs.CL

**发布日期**: 2025-08-21

**🔗 代码/项目**: [GITHUB](https://github.com/aliyun/qwen-dianjin)

---

## 💡 一句话要点

**提出Fin-PRM以解决金融领域推理模型不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `过程奖励模型` `金融推理` `领域专用模型` `轨迹感知` `强化学习` `监督学习` `模型评估`

## 📋 核心要点

1. 现有的过程奖励模型在金融等领域的推理中表现不足，缺乏针对性和结构化的评估机制。
2. Fin-PRM通过结合步骤级和轨迹级奖励监督，专门设计用于金融任务的中间推理评估。
3. 在CFLUE和FinQA等金融推理基准上，Fin-PRM在轨迹选择质量上显著优于通用模型，带来了12.9%的监督学习提升。

## 📝 摘要（中文）

过程奖励模型（PRMs）作为监督大型语言模型（LLMs）中间推理的有前景框架，现有模型主要训练于一般或STEM领域，难以满足金融等特定领域的需求。本文提出了Fin-PRM，一种针对金融任务的领域专用、轨迹感知的PRM，能够评估中间推理步骤。Fin-PRM结合了步骤级和轨迹级的奖励监督，支持高质量推理轨迹选择、密集过程级奖励提供以及测试时的奖励引导推理。实验结果表明，Fin-PRM在金融推理基准上优于通用PRMs和强基线，显著提升了下游模型的表现。

## 🔬 方法详解

**问题定义**：现有的过程奖励模型（PRMs）主要训练于一般领域，难以满足金融领域推理的结构化和符号化需求，导致在金融任务中的表现不佳。

**核心思路**：Fin-PRM通过引入轨迹感知的奖励机制，结合步骤级和轨迹级的奖励监督，旨在提供更精细的推理评估，适应金融领域的特殊需求。

**技术框架**：Fin-PRM的整体架构包括数据输入模块、轨迹评估模块和奖励计算模块。数据输入模块负责接收金融任务数据，轨迹评估模块分析推理步骤，奖励计算模块则根据评估结果生成相应的奖励信号。

**关键创新**：Fin-PRM的主要创新在于其轨迹感知的奖励设计，能够在步骤级和轨迹级上进行细致的评估，与传统的通用PRMs相比，提供了更符合金融逻辑的奖励机制。

**关键设计**：在模型设计中，Fin-PRM采用了特定的损失函数以优化奖励信号的准确性，并在网络结构上进行了调整，以更好地捕捉金融推理的复杂性。

## 📊 实验亮点

实验结果显示，Fin-PRM在CFLUE和FinQA基准上表现优异，轨迹选择质量显著高于通用PRMs，监督学习提升达12.9%，强化学习提升5.2%，测试时性能提升5.1%。这些结果表明，领域专用的奖励建模对金融推理的有效性至关重要。

## 🎯 应用场景

Fin-PRM在金融领域的潜在应用广泛，包括金融决策支持、风险评估和合规性检查等。通过提供高质量的推理轨迹和奖励信号，能够显著提升金融模型的智能化水平，帮助金融机构更好地应对复杂的市场环境。

## 📄 摘要（原文）

> Process Reward Models (PRMs) have emerged as a promising framework for supervising intermediate reasoning in large language models (LLMs), yet existing PRMs are primarily trained on general or Science, Technology, Engineering, and Mathematics (STEM) domains and fall short in domain-specific contexts such as finance, where reasoning is more structured, symbolic, and sensitive to factual and regulatory correctness. We introduce \textbf{Fin-PRM}, a domain-specialized, trajectory-aware PRM tailored to evaluate intermediate reasoning steps in financial tasks. Fin-PRM integrates step-level and trajectory-level reward supervision, enabling fine-grained evaluation of reasoning traces aligned with financial logic. We apply Fin-PRM in both offline and online reward learning settings, supporting three key applications: (i) selecting high-quality reasoning trajectories for distillation-based supervised fine-tuning, (ii) providing dense process-level rewards for reinforcement learning, and (iii) guiding reward-informed Best-of-N inference at test time. Experimental results on financial reasoning benchmarks, including CFLUE and FinQA, demonstrate that Fin-PRM consistently outperforms general-purpose PRMs and strong domain baselines in trajectory selection quality. Downstream models trained with Fin-PRM yield substantial improvements with baselines, with gains of 12.9\% in supervised learning, 5.2\% in reinforcement learning, and 5.1\% in test-time performance. These findings highlight the value of domain-specialized reward modeling for aligning LLMs with expert-level financial reasoning. Our project resources will be available at https://github.com/aliyun/qwen-dianjin.

