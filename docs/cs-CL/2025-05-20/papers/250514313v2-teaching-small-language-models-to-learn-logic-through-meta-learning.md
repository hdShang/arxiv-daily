---
layout: default
title: Teaching Small Language Models to Learn Logic through Meta-Learning
---

# Teaching Small Language Models to Learn Logic through Meta-Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14313" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14313v2</a>
  <a href="https://arxiv.org/pdf/2505.14313.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14313v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14313v2', 'Teaching Small Language Models to Learn Logic through Meta-Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Leonardo Bertolazzi, Manuel Vargas Guzmán, Raffaella Bernardi, Maciej Malicki, Jakub Szymanik

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-07)

---

## 💡 一句话要点

**通过元学习提升小型语言模型的逻辑推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑推理` `元学习` `小型语言模型` `三段论` `知识迁移` `少样本学习` `模型微调`

## 📋 核心要点

1. 现有的大型语言模型在逻辑推理任务中的能力尚未得到充分验证，尤其是在三段论推理方面。
2. 本文提出通过少样本元学习的方法，使模型能够提取跨任务的推理规则，从而提升逻辑推理能力。
3. 实验结果显示，经过元学习微调的小型模型在三段论推理任务中表现优异，尤其在数据稀缺的情况下效果显著。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理任务中的表现日益受到关注，但其逻辑能力仍存在争议。为了解决这一问题，本文研究了LLMs在一个明确的逻辑片段中的推理能力：三段论推理。我们将该问题视为前提选择，并构建受控数据集以隔离逻辑能力。我们提出在该领域应用少样本元学习，鼓励模型提取跨任务的规则，而非仅仅记忆任务内的模式。实验结果表明，经过元学习微调的小型模型（1.5B-7B）在泛化能力上取得了显著提升，尤其在低数据环境下表现突出。这些元学习模型在我们的三段论推理任务中超越了GPT-4o和o3-mini。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在逻辑推理，特别是三段论推理中的能力不足问题。现有方法往往依赖于大量数据进行训练，导致模型在新结构上的泛化能力较差。

**核心思路**：我们提出将少样本元学习应用于逻辑推理领域，鼓励模型从多个任务中提取通用推理规则，而非仅仅记忆特定任务的模式。这种方法旨在提高模型在面对新颖推理结构时的适应能力。

**技术框架**：整体架构包括数据集构建、元学习算法设计和模型训练三个主要模块。首先，构建受控数据集以隔离逻辑能力；其次，设计元学习算法以优化模型的学习过程；最后，通过微调小型模型实现逻辑推理能力的提升。

**关键创新**：本文的主要创新在于将元学习引入逻辑学习的研究中，填补了这一领域的空白。与传统方法相比，我们的方法更注重模型的泛化能力，而非单一任务的记忆。

**关键设计**：在模型训练中，我们采用了特定的损失函数以促进模型在不同任务间的知识迁移，同时调整了网络结构以适应少样本学习的需求。

## 📊 实验亮点

实验结果表明，经过元学习微调的小型模型在三段论推理任务中表现优异，超越了GPT-4o和o3-mini，尤其在低数据环境下，泛化能力提升显著，展示了元学习在逻辑推理中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、法律推理、人工智能助手等。通过提升小型语言模型的逻辑推理能力，可以更好地支持复杂决策和推理任务，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly evaluated on reasoning tasks, yet their logical abilities remain contested. To address this, we study LLMs' reasoning in a well-defined fragment of logic: syllogistic reasoning. We cast the problem as premise selection and construct controlled datasets to isolate logical competence. Beyond evaluation, an open challenge is enabling LLMs to acquire abstract inference patterns that generalize to novel structures. We propose to apply few-shot meta-learning to this domain, thereby encouraging models to extract rules across tasks rather than memorize patterns within tasks. Although meta-learning has been little explored in the context of logic learnability, our experiments show that it is effective: small models (1.5B-7B) fine-tuned with meta-learning demonstrate strong gains in generalization, with especially pronounced benefits in low-data regimes. These meta-learned models outperform GPT-4o and o3-mini on our syllogistic reasoning task.

