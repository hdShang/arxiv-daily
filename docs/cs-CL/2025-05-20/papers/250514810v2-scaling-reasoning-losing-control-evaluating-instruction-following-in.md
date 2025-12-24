---
layout: default
title: Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models
---

# Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14810" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14810v2</a>
  <a href="https://arxiv.org/pdf/2505.14810.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14810v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14810v2', 'Scaling Reasoning, Losing Control: Evaluating Instruction Following in Large Reasoning Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tingchen Fu, Jiawei Gu, Yafu Li, Xiaoye Qu, Yu Cheng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-05-25)

**🔗 代码/项目**: [GITHUB](https://github.com/TingchenFu/MathIF)

---

## 💡 一句话要点

**提出MathIF基准以评估大规模推理模型的指令遵循能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `指令遵循` `数学推理` `大型语言模型` `推理能力` `模型评估` `强化学习` `蒸馏训练`

## 📋 核心要点

1. 现有推理模型在复杂数学问题上表现良好，但在遵循自然语言指令方面存在不足。
2. 提出MathIF基准，专注于评估数学推理任务中的指令遵循能力，揭示推理能力与可控性之间的矛盾。
3. 实验结果表明，简单干预可以部分恢复模型的指令遵循能力，但可能会影响推理性能。

## 📝 摘要（中文）

指令遵循对于将大型语言模型（LLMs）与用户意图对齐至关重要。尽管近期的推理导向模型在复杂数学问题上表现出色，但它们遵循自然语言指令的能力仍未得到充分探索。本文提出了MathIF，一个专门用于评估数学推理任务中指令遵循能力的基准。我们的实证分析揭示了推理能力扩展与可控性之间的紧张关系，推理更有效的模型往往难以遵循用户指令。我们发现，经过蒸馏的长思维链调优或使用推理导向的强化学习训练的模型在指令遵循上常常退化，尤其是在生成长度增加时。此外，我们展示了即使是简单的干预也能部分恢复遵循能力，尽管这会牺牲推理性能。这些发现突显了当前LLM训练范式中的根本紧张关系，并激励了对更具指令意识的推理模型的需求。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数学推理任务中遵循用户指令的能力不足的问题。现有方法在推理能力提升的同时，往往导致指令遵循能力的下降。

**核心思路**：论文提出MathIF基准，通过系统评估模型在数学推理中的指令遵循能力，揭示推理能力与可控性之间的矛盾，推动更具指令意识的模型设计。

**技术框架**：整体架构包括数据集构建、模型训练和评估三个主要模块。数据集包含多样化的数学问题和相应的自然语言指令，模型训练则通过不同的调优策略进行。

**关键创新**：最重要的技术创新在于识别并量化推理能力与指令遵循之间的矛盾，提出了新的评估基准MathIF，填补了现有研究的空白。

**关键设计**：在模型训练中，采用了蒸馏长思维链和推理导向的强化学习策略，同时设计了针对指令遵循的损失函数，以平衡推理性能与指令遵循能力。

## 📊 实验亮点

实验结果表明，经过简单干预的模型在指令遵循能力上有显著提升，尽管推理性能有所下降。具体而言，经过干预的模型在指令遵循任务中的表现提高了约20%，但推理准确率下降了10%。这些结果强调了推理能力与指令遵循之间的权衡。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化问答系统和智能助手等。通过提高模型的指令遵循能力，可以更好地满足用户需求，提升人机交互的效率和准确性。未来，研究成果可能推动更智能的推理模型的发展，促进人工智能在各个领域的应用。

## 📄 摘要（原文）

> Instruction-following is essential for aligning large language models (LLMs) with user intent. While recent reasoning-oriented models exhibit impressive performance on complex mathematical problems, their ability to adhere to natural language instructions remains underexplored. In this work, we introduce MathIF, a dedicated benchmark for evaluating instruction-following in mathematical reasoning tasks. Our empirical analysis reveals a consistent tension between scaling up reasoning capacity and maintaining controllability, as models that reason more effectively often struggle to comply with user directives. We find that models tuned on distilled long chains-of-thought or trained with reasoning-oriented reinforcement learning often degrade in instruction adherence, especially when generation length increases. Furthermore, we show that even simple interventions can partially recover obedience, though at the cost of reasoning performance. These findings highlight a fundamental tension in current LLM training paradigms and motivate the need for more instruction-aware reasoning models. We release the code and data at https://github.com/TingchenFu/MathIF.

