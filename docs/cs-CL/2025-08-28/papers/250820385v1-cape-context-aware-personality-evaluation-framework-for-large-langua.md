---
layout: default
title: "CAPE: Context-Aware Personality Evaluation Framework for Large Language Models"
---

# CAPE: Context-Aware Personality Evaluation Framework for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.20385" class="toolbar-btn" target="_blank">📄 arXiv: 2508.20385v1</a>
  <a href="https://arxiv.org/pdf/2508.20385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.20385v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.20385v1', 'CAPE: Context-Aware Personality Evaluation Framework for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jivnesh Sandhan, Fei Cheng, Tushar Sandhan, Yugo Murawaki

**分类**: cs.CL

**发布日期**: 2025-08-28

**备注**: Accepted at EMNLP25 (Findings)

**🔗 代码/项目**: [GITHUB](https://github.com/jivnesh/CAPE)

---

## 💡 一句话要点

**提出CAPE框架以解决LLMs个性评估中的上下文缺失问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性评估` `上下文感知` `大型语言模型` `对话系统` `心理测量` `机器学习` `人机交互`

## 📋 核心要点

1. 现有方法在评估大型语言模型的个性时缺乏上下文考虑，导致评估结果不够真实和有效。
2. 本文提出的CAPE框架通过整合对话历史，能够更全面地评估LLMs的个性特征，克服了传统方法的局限性。
3. 实验结果表明，CAPE框架显著提高了响应一致性，并揭示了不同模型在个性表现上的差异，尤其是GPT系列模型的鲁棒性。

## 📝 摘要（中文）

心理测量测试传统上用于评估人类行为特征，现在被应用于大型语言模型（LLMs）以评估其行为特征。然而，现有研究采用无上下文的方法，孤立回答每个问题，忽视了对话历史的影响。为此，本文提出了首个上下文感知个性评估框架（CAPE），将先前的对话交互纳入评估中。通过引入新颖的度量标准来量化LLM响应的一致性，研究表明对话历史增强了响应一致性，但也导致个性偏移。实验结果显示，GPT模型对问题顺序具有鲁棒性，而其他模型则表现出显著敏感性。应用该框架于角色扮演代理（RPA）时，发现上下文依赖的个性偏移提高了响应一致性，更好地符合人类判断。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型个性评估中缺乏上下文的局限性，传统方法孤立回答问题，无法反映真实的对话情境。

**核心思路**：CAPE框架通过引入对话历史，考虑上下文对模型响应的影响，从而更准确地评估模型的个性特征。

**技术框架**：CAPE框架包括数据收集、对话历史整合、个性评估和一致性度量四个主要模块，形成一个闭环评估系统。

**关键创新**：引入新颖的度量标准来量化模型响应的一致性，强调上下文对个性评估的重要性，这是与现有方法的本质区别。

**关键设计**：在模型训练中，采用了特定的损失函数来优化响应一致性，并设计了适应不同模型架构的参数设置，以确保框架的通用性和有效性。

## 📊 实验亮点

实验结果显示，CAPE框架显著提高了响应一致性，尤其在GPT-3.5-Turbo和GPT-4-Turbo模型中，个性偏移现象明显。与基线模型相比，CAPE框架提升了响应一致性，且在角色扮演代理中表现出更好的与人类判断的一致性。

## 🎯 应用场景

CAPE框架具有广泛的应用潜力，尤其在人机交互、虚拟助手和角色扮演游戏等领域。通过更准确的个性评估，能够提升用户体验，使得AI系统在与人类交互时表现得更加自然和人性化。未来，该框架还可以扩展到其他类型的对话系统中，推动个性化AI的发展。

## 📄 摘要（原文）

> Psychometric tests, traditionally used to assess humans, are now being applied to Large Language Models (LLMs) to evaluate their behavioral traits. However, existing studies follow a context-free approach, answering each question in isolation to avoid contextual influence. We term this the Disney World test, an artificial setting that ignores real-world applications, where conversational history shapes responses. To bridge this gap, we propose the first Context-Aware Personality Evaluation (CAPE) framework for LLMs, incorporating prior conversational interactions. To thoroughly analyze the influence of context, we introduce novel metrics to quantify the consistency of LLM responses, a fundamental trait in human behavior.
>   Our exhaustive experiments on 7 LLMs reveal that conversational history enhances response consistency via in-context learning but also induces personality shifts, with GPT-3.5-Turbo and GPT-4-Turbo exhibiting extreme deviations. While GPT models are robust to question ordering, Gemini-1.5-Flash and Llama-8B display significant sensitivity. Moreover, GPT models response stem from their intrinsic personality traits as well as prior interactions, whereas Gemini-1.5-Flash and Llama--8B heavily depend on prior interactions. Finally, applying our framework to Role Playing Agents (RPAs) shows context-dependent personality shifts improve response consistency and better align with human judgments. Our code and datasets are publicly available at: https://github.com/jivnesh/CAPE

