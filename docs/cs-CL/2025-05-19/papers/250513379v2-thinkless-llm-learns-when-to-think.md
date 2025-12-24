---
layout: default
title: Thinkless: LLM Learns When to Think
---

# Thinkless: LLM Learns When to Think

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13379" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13379v2</a>
  <a href="https://arxiv.org/pdf/2505.13379.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13379v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13379v2', 'Thinkless: LLM Learns When to Think')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-19 (更新: 2025-06-26)

**🔗 代码/项目**: [GITHUB](https://github.com/VainF/Thinkless)

---

## 💡 一句话要点

**提出Thinkless框架以提高推理语言模型的计算效率**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理语言模型` `强化学习` `控制标记` `解耦优化` `计算效率` `任务复杂性` `响应生成` `模型训练`

## 📋 核心要点

1. 现有推理语言模型在处理所有查询时均采用复杂推理，导致计算效率低下，尤其是在简单问题上。
2. 本文提出Thinkless框架，通过控制标记自适应选择推理方式，结合强化学习进行训练，优化推理效率。
3. 实验结果显示，Thinkless在多个基准测试中将长链推理使用减少50%-90%，显著提升了模型的计算效率。

## 📝 摘要（中文）

推理语言模型在复杂逻辑推理任务中表现出色，但对所有查询都采用复杂推理会导致计算效率低下。为此，本文提出了Thinkless，一个可学习的框架，使得语言模型能够根据任务复杂性和模型能力自适应选择简短或详细的推理方式。Thinkless在强化学习框架下训练，使用控制标记<short>和<think>来分别表示简洁和详细的响应。核心方法是解耦组相对策略优化（DeGRPO）算法，将混合推理的学习目标分解为控制标记损失和响应损失两个部分，从而提高了训练的稳定性和效率。在多个基准测试中，Thinkless能够将长链推理的使用减少50%-90%，显著提升了推理语言模型的效率。

## 🔬 方法详解

**问题定义**：本文旨在解决推理语言模型在处理简单问题时过度使用复杂推理导致的计算效率低下问题。现有方法未能有效区分任务复杂性，导致资源浪费。

**核心思路**：提出Thinkless框架，使模型能够根据任务复杂性和自身能力自适应选择简短或详细的推理方式，从而提高计算效率。通过引入控制标记，模型可以灵活调整推理策略。

**技术框架**：Thinkless框架基于强化学习，包含两个主要模块：控制标记选择模块和响应生成模块。控制标记模块通过<short>和<think>标记来指示推理模式，而响应生成模块则负责生成最终答案。

**关键创新**：核心创新在于解耦组相对策略优化（DeGRPO）算法，该算法将混合推理的学习目标分为控制标记损失和响应损失，提供了更细粒度的控制，避免了传统方法中的训练崩溃问题。

**关键设计**：在损失函数设计上，控制标记损失用于优化推理模式选择，响应损失则用于提升生成答案的准确性。通过这种解耦设计，模型训练更加稳定，效果显著提升。

## 📊 实验亮点

在多个基准测试（如Minerva Algebra、MATH-500和GSM8K）中，Thinkless显著减少了长链推理的使用，降低幅度达50%-90%。这一结果表明，Thinkless在提升推理语言模型效率方面具有显著优势，能够有效应对复杂推理任务。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和医疗等需要复杂推理的场景。通过提高推理语言模型的效率，Thinkless可以在实时决策支持、自动问答系统等方面发挥重要作用，未来可能推动智能助手和自动化系统的发展。

## 📄 摘要（原文）

> Reasoning Language Models, capable of extended chain-of-thought reasoning, have demonstrated remarkable performance on tasks requiring complex logical inference. However, applying elaborate reasoning for all queries often results in substantial computational inefficiencies, particularly when many problems admit straightforward solutions. This motivates an open question: Can LLMs learn when to think? To answer this, we propose Thinkless, a learnable framework that empowers an LLM to adaptively select between short-form and long-form reasoning, based on both task complexity and the model's ability. Thinkless is trained under a reinforcement learning paradigm and employs two control tokens, <short> for concise responses and <think> for detailed reasoning. At the core of our method is a Decoupled Group Relative Policy Optimization (DeGRPO) algorithm, which decomposes the learning objective of hybrid reasoning into two components: (1) a control token loss that governs the selection of the reasoning mode, and (2) a response loss that improves the accuracy of the generated answers. This decoupled formulation enables fine-grained control over the contributions of each objective, stabilizing training and effectively preventing collapse observed in vanilla GRPO. Empirically, on several benchmarks such as Minerva Algebra, MATH-500, and GSM8K, Thinkless is able to reduce the usage of long-chain thinking by 50% - 90%, significantly improving the efficiency of Reasoning Language Models. The code is available at https://github.com/VainF/Thinkless

