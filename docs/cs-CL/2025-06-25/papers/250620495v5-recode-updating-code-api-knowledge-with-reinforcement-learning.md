---
layout: default
title: "ReCode: Updating Code API Knowledge with Reinforcement Learning"
---

# ReCode: Updating Code API Knowledge with Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20495" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20495v5</a>
  <a href="https://arxiv.org/pdf/2506.20495.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20495v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20495v5', 'ReCode: Updating Code API Knowledge with Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoze Wu, Yunzhi Yao, Wenhao Yu, Ningyu Zhang

**分类**: cs.CL, cs.AI, cs.IR, cs.LG, cs.SE

**发布日期**: 2025-06-25 (更新: 2025-11-23)

**备注**: AAAI 2026

**🔗 代码/项目**: [GITHUB](https://github.com/zjunlp/ReCode)

---

## 💡 一句话要点

**提出ReCode框架以解决LLMs在API更新中的适应性问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码生成` `API更新` `强化学习` `版本迁移` `代码评估` `动态环境`

## 📋 核心要点

1. 现有大型语言模型在面对外部库API的频繁更新时，无法有效适应，导致代码生成的可靠性下降。
2. 本文提出ReCode框架，通过构建训练集和引入新的评估指标，模拟人类程序员对API变化的适应能力。
3. 实验结果显示，ReCode在多个LLMs和强化学习算法上均实现了性能提升，特别是在CodeUpdateArena任务中表现优异。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码生成方面表现出色，但在适应外部库API的频繁更新时存在显著不足。这一问题源于它们依赖于过时的API知识，即使能够访问当前文档，也会影响在动态环境中的可靠代码生成。为了解决这一问题，本文提出了ReCode（基于规则的强化学习代码更新框架），该框架模拟人类程序员对API变化的适应。我们构建了一个包含约2000条数据的训练集，使LLMs能够基于更新信息进行版本迁移。同时，我们引入了一种修改后的字符串相似度度量作为强化学习的奖励。实验表明，ReCode显著提升了LLMs在动态API场景下的代码生成性能，尤其是在未见过的CodeUpdateArena任务上。与监督微调相比，ReCode对LLMs的通用代码生成能力影响较小。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在动态API环境中代码生成能力不足的问题。现有方法依赖于过时的API知识，无法有效适应频繁的API更新。

**核心思路**：ReCode框架通过模拟人类程序员对API变化的适应过程，利用强化学习来更新模型的API知识，从而提升代码生成的准确性和可靠性。

**技术框架**：ReCode的整体架构包括数据集构建、强化学习训练和代码评估三个主要模块。首先，构建包含2000条数据的训练集；其次，利用强化学习算法对模型进行训练；最后，使用修改后的字符串相似度度量进行代码评估。

**关键创新**：ReCode的创新点在于引入了强化学习机制来更新API知识，并设计了新的代码评估指标。这一方法与传统的监督学习微调方式有本质区别，能够更灵活地适应API的变化。

**关键设计**：在训练过程中，使用了特定的奖励机制来评估代码生成的质量，采用了GRPO和DAPO等强化学习算法，确保了模型在动态环境中的适应性和性能提升。

## 📊 实验亮点

实验结果显示，ReCode显著提升了LLMs在动态API场景下的代码生成性能，特别是在CodeUpdateArena任务中，Qwen2.5-Coder-7B模型的表现超越了32B参数的代码指令调优模型，展示了强化学习在代码更新中的有效性。

## 🎯 应用场景

ReCode框架具有广泛的应用潜力，尤其适用于需要频繁更新API的开发环境，如软件开发、自动化测试和智能编程助手等领域。通过提升代码生成的准确性和可靠性，ReCode能够有效支持开发者在快速变化的技术环境中保持高效生产力。

## 📄 摘要（原文）

> Large Language Models (LLMs) exhibit remarkable code generation capabilities but falter when adapting to frequent updates in external library APIs. This critical limitation, stemming from reliance on outdated API knowledge from their training data, even with access to current documentation, impedes reliable code generation in dynamic environments. To tackle this issue, we propose ReCode (rule-based Reinforcement learning for Code Update), a novel framework that mimics human programmer adaptation to API changes. Specifically, we construct a dataset of approximately 2,000 data entries to train the LLMs to perform version migration based on updated information. Then, we introduce a modified string similarity metric for code evaluation as the reward for reinforcement learning. Our experiments demonstrate that ReCode substantially boosts LLMs' code generation performance in dynamic API scenarios, especially on the unseen CodeUpdateArena task. Crucially, compared to supervised fine-tuning, ReCode has less impact on LLMs' general code generation abilities. We apply ReCode on various LLMs and reinforcement learning algorithms (GRPO and DAPO), all achieving consistent improvements. Notably, after training, Qwen2.5-Coder-7B outperforms that of the 32B parameter code instruction-tuned model and the reasoning model with the same architecture. Code is available at https://github.com/zjunlp/ReCode.

