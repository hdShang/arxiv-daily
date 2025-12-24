---
layout: default
title: "Facts Fade Fast: Evaluating Memorization of Outdated Medical Knowledge in Large Language Models"
---

# Facts Fade Fast: Evaluating Memorization of Outdated Medical Knowledge in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04304" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04304v1</a>
  <a href="https://arxiv.org/pdf/2509.04304.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04304v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04304v1', 'Facts Fade Fast: Evaluating Memorization of Outdated Medical Knowledge in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juraj Vladika, Mahdi Dhaini, Florian Matthes

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-04

**备注**: Accepted to Findings of EMNLP 2025

---

## 💡 一句话要点

**提出MedRevQA和MedChangeQA数据集，评估大语言模型对过时医学知识的记忆**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `医学知识` `知识时效性` `问答数据集` `临床推理`

## 📋 核心要点

1. 现有大语言模型在医疗领域的应用受限于其对静态训练数据的依赖，导致模型可能记忆并输出过时的医学知识。
2. 论文核心在于构建MedRevQA和MedChangeQA两个数据集，用于评估LLM对医学知识时效性的掌握程度。
3. 实验结果表明，多个主流LLM在所构建的数据集上表现出对过时医学知识的依赖，揭示了现有模型的局限性。

## 📝 摘要（中文）

大型语言模型(LLM)在医疗保健领域具有巨大潜力，可以辅助医学研究人员和医生。然而，当医学建议随着新的研究进展而不断发展时，LLM对静态训练数据的依赖构成了一个主要风险。如果LLM记住了过时的医学知识，它们可能会提供有害的建议或在临床推理任务中失败。为了研究这个问题，我们引入了两个新的问答(QA)数据集，它们来自系统综述：MedRevQA(包含16,501个QA对，涵盖一般的生物医学知识)和MedChangeQA(包含512个QA对的子集，其中医学共识随时间发生了变化)。我们对八个主流LLM在这些数据集上的评估表明，所有模型都一致依赖于过时的知识。此外，我们还分析了过时的预训练数据和训练策略的影响，以解释这种现象，并提出了未来的缓解方向，为开发更具时效性和可靠性的医学AI系统奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在医疗领域应用时，由于依赖静态训练数据而导致的记忆和输出过时医学知识的问题。现有方法无法有效评估和解决LLM对医学知识时效性的掌握程度，存在潜在的误导或危害。

**核心思路**：论文的核心思路是通过构建专门的问答数据集，即MedRevQA和MedChangeQA，来评估LLM对医学知识时效性的掌握程度。MedChangeQA特别关注医学共识随时间发生变化的情况，从而能够更准确地衡量LLM是否能够区分新旧知识。

**技术框架**：论文的技术框架主要包括以下几个阶段：1) 数据集构建：从系统综述中提取QA对，构建MedRevQA和MedChangeQA数据集。2) 模型评估：选择多个主流LLM，在构建的数据集上进行评估。3) 结果分析：分析实验结果，探讨过时预训练数据和训练策略对模型性能的影响。4) 未来方向：提出缓解模型依赖过时知识的未来研究方向。

**关键创新**：论文的关键创新在于构建了MedRevQA和MedChangeQA两个数据集，为评估LLM在医学领域对知识时效性的掌握程度提供了新的benchmark。MedChangeQA数据集的构建尤其具有创新性，它关注医学共识随时间的变化，能够更准确地衡量LLM是否能够区分新旧知识。

**关键设计**：MedRevQA数据集包含16,501个QA对，涵盖一般的生物医学知识。MedChangeQA数据集是MedRevQA的子集，包含512个QA对，其中医学共识随时间发生了变化。论文没有涉及具体的模型结构或损失函数设计，而是侧重于数据集的构建和模型评估。

## 📊 实验亮点

实验结果表明，所有被评估的LLM都表现出对过时医学知识的依赖。例如，在MedChangeQA数据集上，模型在回答关于已发生变化的医学共识的问题时，倾向于给出过时的答案。这一结果突显了现有LLM在处理时效性医学知识方面的局限性，并强调了开发更具时效性和可靠性的医学AI系统的必要性。

## 🎯 应用场景

该研究成果可应用于开发更可靠的医学AI系统，辅助医生进行诊断和治疗决策。通过评估和改进LLM对医学知识时效性的掌握，可以减少模型输出过时或错误信息的风险，提高医疗服务的质量和安全性。未来的研究可以进一步探索如何利用该数据集来训练和优化LLM，使其能够更好地适应医学知识的快速更新。

## 📄 摘要（原文）

> The growing capabilities of Large Language Models (LLMs) show significant potential to enhance healthcare by assisting medical researchers and physicians. However, their reliance on static training data is a major risk when medical recommendations evolve with new research and developments. When LLMs memorize outdated medical knowledge, they can provide harmful advice or fail at clinical reasoning tasks. To investigate this problem, we introduce two novel question-answering (QA) datasets derived from systematic reviews: MedRevQA (16,501 QA pairs covering general biomedical knowledge) and MedChangeQA (a subset of 512 QA pairs where medical consensus has changed over time). Our evaluation of eight prominent LLMs on the datasets reveals consistent reliance on outdated knowledge across all models. We additionally analyze the influence of obsolete pre-training data and training strategies to explain this phenomenon and propose future directions for mitigation, laying the groundwork for developing more current and reliable medical AI systems.

