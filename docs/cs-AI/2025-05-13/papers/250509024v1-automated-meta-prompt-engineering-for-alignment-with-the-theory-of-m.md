---
layout: default
title: Automated Meta Prompt Engineering for Alignment with the Theory of Mind
---

# Automated Meta Prompt Engineering for Alignment with the Theory of Mind

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.09024" class="toolbar-btn" target="_blank">📄 arXiv: 2505.09024v1</a>
  <a href="https://arxiv.org/pdf/2505.09024.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.09024v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.09024v1', 'Automated Meta Prompt Engineering for Alignment with the Theory of Mind')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aaron Baughman, Rahul Agarwal, Eduardo Morales, Gozde Akay

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-13

**备注**: 9 pages, 6 figures, 3 tables

---

## 💡 一句话要点

**提出自动化元提示工程以解决心智理论对齐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `元提示工程` `心智理论` `代理强化学习` `大型语言模型` `内容生成` `人类心理预期` `实时内容优化`

## 📋 核心要点

1. 现有方法在生成复杂文本时，难以满足人类的心理预期，导致内容质量不高。
2. 本文提出的元提示方法通过代理强化学习，优化LLM生成内容的过程，使其更符合人类的心理预期。
3. 实验表明，使用该方法后，人类内容审阅者与AI的对齐率达到53.8%，显著提升了内容生成的质量。

## 📝 摘要（中文）

本文介绍了一种元提示方法，该方法能够为复杂任务生成流畅文本，同时优化人类心理预期与大型语言模型（LLM）神经处理之间的相似性。通过代理强化学习技术，LLM作为评判者（LLMaaJ）通过上下文学习教导另一LLM如何生成内容，解释生成文本的意图和意外特征。用户在2024年美国网球公开赛前修改AI生成的长篇文章，以测量人类对内容生成的心理信念。LLMaaJ能够通过预测并纳入人类编辑来解决心智理论对齐问题。实验结果显示，人类内容审阅者的期望与AI的对齐率为53.8%，平均迭代次数为4.38。内容特征的几何解释结合了空间体积与顶点对齐，使LLMaaJ能够优化人类心智理论，从而提高内容质量，扩展网球动作的覆盖范围。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLM）在生成内容时与人类心理预期之间的对齐问题。现有方法往往无法准确捕捉人类的意图和期望，导致生成内容的质量和相关性不足。

**核心思路**：论文提出了一种元提示方法，通过代理强化学习的方式，让一个LLM（作为评判者）教导另一个LLM生成更符合人类心理预期的内容。通过这种方式，LLM能够在生成过程中考虑人类的编辑和反馈，从而提高内容的质量和相关性。

**技术框架**：整体架构包括两个主要模块：LLMaaJ（评判者）和目标LLM。评判者通过上下文学习分析生成文本的特征，并指导目标LLM进行内容生成。整个流程涉及人类编辑的反馈循环，以不断优化生成内容。

**关键创新**：最重要的技术创新在于引入了代理强化学习机制，使得LLM能够在生成内容时主动考虑人类的心理预期。这一方法与传统的单向生成方法有本质区别，后者通常不考虑人类反馈。

**关键设计**：在模型设计上，采用了几何解释的方法来分析内容特征，如事实性、创新性、重复性和相关性，并通过Hilbert向量空间进行优化。关键参数设置和损失函数的设计旨在最大化人类心理预期的对齐度。实验中使用的迭代次数和反馈机制也经过精心设计，以确保生成内容的质量。

## 📊 实验亮点

实验结果显示，使用LLMaaJ进行内容生成时，人类内容审阅者的期望与AI的对齐率达到了53.8%，且平均迭代次数为4.38。这表明该方法在提升内容质量和相关性方面具有显著效果，尤其是在动态场景下的应用。

## 🎯 应用场景

该研究的潜在应用领域包括体育、娱乐等实时内容生成场景。通过优化LLM与人类心理预期的对齐，可以显著提升内容质量，满足用户需求，未来可扩展至更多行业，如新闻报道、社交媒体内容生成等。

## 📄 摘要（原文）

> We introduce a method of meta-prompting that jointly produces fluent text for complex tasks while optimizing the similarity of neural states between a human's mental expectation and a Large Language Model's (LLM) neural processing. A technique of agentic reinforcement learning is applied, in which an LLM as a Judge (LLMaaJ) teaches another LLM, through in-context learning, how to produce content by interpreting the intended and unintended generated text traits. To measure human mental beliefs around content production, users modify long form AI-generated text articles before publication at the US Open 2024 tennis Grand Slam. Now, an LLMaaJ can solve the Theory of Mind (ToM) alignment problem by anticipating and including human edits within the creation of text from an LLM. Throughout experimentation and by interpreting the results of a live production system, the expectations of human content reviewers had 100% of alignment with AI 53.8% of the time with an average iteration count of 4.38. The geometric interpretation of content traits such as factualness, novelty, repetitiveness, and relevancy over a Hilbert vector space combines spatial volume (all trait importance) with vertices alignment (individual trait relevance) enabled the LLMaaJ to optimize on Human ToM. This resulted in an increase in content quality by extending the coverage of tennis action. Our work that was deployed at the US Open 2024 has been used across other live events within sports and entertainment.

