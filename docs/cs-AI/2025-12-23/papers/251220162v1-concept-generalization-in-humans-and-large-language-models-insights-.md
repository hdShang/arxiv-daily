---
layout: default
title: Concept Generalization in Humans and Large Language Models: Insights from the Number Game
---

# Concept Generalization in Humans and Large Language Models: Insights from the Number Game

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20162" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20162v1</a>
  <a href="https://arxiv.org/pdf/2512.20162.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20162v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20162v1', 'Concept Generalization in Humans and Large Language Models: Insights from the Number Game')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Arghavan Bazigaran, Hansem Sohn

**分类**: cs.AI

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**通过数字游戏对比人类与大语言模型在概念泛化上的差异**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `概念泛化` `大语言模型` `贝叶斯模型` `数字游戏` `归纳偏置`

## 📋 核心要点

1. 现有方法难以解释人类与大语言模型在概念泛化上的差异，尤其是在数学概念方面。
2. 论文采用贝叶斯模型作为分析框架，研究人类和LLM在数字游戏中的归纳偏置和推理策略。
3. 实验表明，人类能灵活推断规则和相似性概念，且具有更强的小样本泛化能力，而LLM更依赖数学规则。

## 📝 摘要（中文）

本文对比了人类和大语言模型（LLM）在数字游戏（一种概念推断任务）中的泛化能力。我们使用贝叶斯模型作为分析框架，研究了人类和LLM的归纳偏置和推理策略。贝叶斯模型能更好地捕捉人类行为，因为人类可以灵活地推断基于规则和基于相似性的概念，而LLM更依赖于数学规则。人类还表现出小样本泛化能力，即使只有一个例子也能泛化，而LLM需要更多的样本才能泛化。这些对比突出了人类和LLM在推断和泛化数学概念方面的根本差异。

## 🔬 方法详解

**问题定义**：论文旨在研究人类和大语言模型在概念泛化能力上的差异，特别是在数学概念领域。现有方法未能充分解释两者在归纳偏置和推理策略上的不同，也未能揭示LLM在小样本学习方面的局限性。数字游戏提供了一个受控的环境，用于量化和比较人类和LLM在概念学习和泛化方面的表现。

**核心思路**：论文的核心思路是使用贝叶斯模型作为分析框架，将人类和LLM的行为建模为概率推理过程。通过比较模型参数和预测结果，可以揭示人类和LLM在归纳偏置和推理策略上的差异。同时，通过改变训练样本的数量，可以评估两者的小样本泛化能力。

**技术框架**：整体框架包括三个主要部分：1) 数字游戏环境的构建，用于生成训练和测试数据；2) 人类行为数据的收集，通过实验获取人类在数字游戏中的决策；3) LLM的训练和评估，使用不同的LLM架构和训练策略，评估其在数字游戏中的表现。贝叶斯模型用于对人类和LLM的行为进行建模和分析。

**关键创新**：论文的关键创新在于将贝叶斯模型应用于分析人类和LLM在概念泛化上的差异。通过这种方法，可以量化两者在归纳偏置和推理策略上的不同，并揭示LLM在小样本学习方面的局限性。此外，论文还提出了一个数字游戏环境，为研究概念学习和泛化提供了一个新的平台。

**关键设计**：在贝叶斯模型中，需要定义先验概率分布，用于表示对不同概念的初始信念。似然函数用于表示给定概念下观察到数据的概率。后验概率分布用于表示在观察到数据后对概念的更新信念。通过比较人类和LLM的后验概率分布，可以揭示两者在归纳偏置和推理策略上的差异。实验中使用了不同规模的LLM，并采用了不同的训练策略，例如微调和提示学习。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20162v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20162v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20162v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，贝叶斯模型能更好地捕捉人类行为，人类在数字游戏中表现出更强的灵活性和泛化能力，能够灵活地推断基于规则和基于相似性的概念，并且具有更强的小样本泛化能力。相比之下，LLM更依赖于数学规则，且需要更多的样本才能泛化。这些发现揭示了人类和LLM在概念学习和泛化方面的根本差异。

## 🎯 应用场景

该研究成果可应用于提升大语言模型的推理能力和泛化能力，使其更接近人类的认知水平。例如，可以借鉴人类的归纳偏置和推理策略，设计更有效的LLM训练方法。此外，该研究还可以应用于教育领域，帮助人们更好地理解数学概念，并提高解决问题的能力。

## 📄 摘要（原文）

> We compare human and large language model (LLM) generalization in the number game, a concept inference task. Using a Bayesian model as an analytical framework, we examined the inductive biases and inference strategies of humans and LLMs. The Bayesian model captured human behavior better than LLMs in that humans flexibly infer rule-based and similarity-based concepts, whereas LLMs rely more on mathematical rules. Humans also demonstrated a few-shot generalization, even from a single example, while LLMs required more samples to generalize. These contrasts highlight the fundamental differences in how humans and LLMs infer and generalize mathematical concepts.

