---
layout: default
title: "SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations"
---

# SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16437" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16437v1</a>
  <a href="https://arxiv.org/pdf/2509.16437.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16437v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16437v1', 'SENSE-7: Taxonomy and Dataset for Measuring User Perceptions of Empathy in Sustained Human-AI Conversations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jina Suh, Lindy Le, Erfan Shayegani, Gonzalo Ramos, Judith Amores, Desmond C. Ong, Mary Czerwinski, Javier Hernandez

**分类**: cs.HC, cs.AI

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**提出SENSE-7数据集与移情分类器，用于衡量用户在人机对话中对AI移情的感知。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人机交互` `移情` `大型语言模型` `用户感知` `数据集` `情感计算` `对话系统`

## 📋 核心要点

1. 现有“数字移情”方法侧重模拟人类情感，忽略了用户感知的移情的主观性和情境性。
2. 提出以人为中心的移情分类体系，强调可观察行为，并构建包含用户标注的SENSE-7数据集。
3. 实验表明移情判断高度个体化且情境敏感，LLM分类器可识别5个移情级别，Spearman ρ=0.369。

## 📝 摘要（中文）

移情在人机交互中日益重要，但传统的“数字移情”方法侧重于模拟人类的情感状态，忽略了用户感知的移情的主观性、情境性和关系性。本文提出了一个以人为中心的分类体系，强调可观察的移情行为，并引入了一个新的数据集Sense-7，包含信息工作者与大型语言模型（LLM）之间的真实对话，以及用户对每轮对话的移情标注、用户特征和上下文细节，从而更贴近用户地表示移情。对来自109名参与者的695个对话的分析表明，移情判断具有高度的个体化和情境敏感性，并且容易受到对话连续性失败或用户期望未满足的影响。为了促进进一步的研究，我们提供了一个包含672个匿名对话的子集，并进行了探索性分类分析，结果表明基于LLM的分类器可以识别5个移情级别，平均Spearman相关系数ρ=0.369，准确率=0.487。总的来说，我们的研究结果强调了AI设计需要动态地根据用户情境和目标调整移情行为，为未来研究和以人为本的社交AI代理的实际开发提供了路线图。

## 🔬 方法详解

**问题定义**：现有方法在衡量人机对话中的移情时，主要关注AI模拟人类情感，而忽略了用户对AI移情的感知是主观的、情境相关的，并且受到对话关系影响。缺乏一个能够捕捉用户真实感受的数据集和评估框架。

**核心思路**：本文的核心思路是以用户为中心，关注用户在与AI对话过程中对AI表现出的移情行为的感知。通过构建包含用户标注的数据集，并分析用户特征和对话上下文，来理解影响用户移情判断的因素。

**技术框架**：该研究的技术框架主要包括以下几个部分：1) 构建移情分类体系，定义可观察的移情行为；2) 收集真实的人机对话数据，并由用户对每轮对话进行移情标注；3) 分析数据集，研究用户特征、对话上下文与移情判断之间的关系；4) 使用大型语言模型训练移情分类器，并评估其性能。

**关键创新**：该研究的关键创新在于：1) 提出了一个以人为中心的移情分类体系，更贴近用户对移情的真实感知；2) 构建了一个包含用户标注的SENSE-7数据集，为研究人机对话中的移情提供了宝贵资源；3) 揭示了用户特征和对话上下文对移情判断的重要影响。

**关键设计**：SENSE-7数据集包含695个对话，来自109名参与者。每个对话轮次都由用户标注移情等级（5个等级）。分类器使用LLM进行微调，目标是预测用户标注的移情等级。使用Spearman相关系数和准确率作为评估指标。

## 📊 实验亮点

实验结果表明，基于LLM的分类器在SENSE-7数据集上能够识别5个移情级别，平均Spearman相关系数ρ=0.369，准确率=0.487。这表明LLM在理解和预测用户对AI移情的感知方面具有潜力。此外，研究还发现用户特征和对话上下文对移情判断有显著影响，强调了个性化和情境化AI设计的重要性。

## 🎯 应用场景

该研究成果可应用于开发更具同理心的人工智能助手，例如在客户服务、心理咨询、教育等领域。通过理解用户对AI移情的感知，可以设计出能够更好地满足用户需求、建立信任关系的人机交互系统，从而提升用户体验和满意度。未来的研究可以进一步探索如何动态地调整AI的移情行为，以适应不同的用户和情境。

## 📄 摘要（原文）

> Empathy is increasingly recognized as a key factor in human-AI communication, yet conventional approaches to "digital empathy" often focus on simulating internal, human-like emotional states while overlooking the inherently subjective, contextual, and relational facets of empathy as perceived by users. In this work, we propose a human-centered taxonomy that emphasizes observable empathic behaviors and introduce a new dataset, Sense-7, of real-world conversations between information workers and Large Language Models (LLMs), which includes per-turn empathy annotations directly from the users, along with user characteristics, and contextual details, offering a more user-grounded representation of empathy. Analysis of 695 conversations from 109 participants reveals that empathy judgments are highly individualized, context-sensitive, and vulnerable to disruption when conversational continuity fails or user expectations go unmet. To promote further research, we provide a subset of 672 anonymized conversation and provide exploratory classification analysis, showing that an LLM-based classifier can recognize 5 levels of empathy with an encouraging average Spearman $ρ$=0.369 and Accuracy=0.487 over this set. Overall, our findings underscore the need for AI designs that dynamically tailor empathic behaviors to user contexts and goals, offering a roadmap for future research and practical development of socially attuned, human-centered artificial agents.

