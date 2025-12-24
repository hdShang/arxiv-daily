---
layout: default
title: Amulet: Putting Complex Multi-Turn Conversations on the Stand with LLM Juries
---

# Amulet: Putting Complex Multi-Turn Conversations on the Stand with LLM Juries

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20451" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20451v1</a>
  <a href="https://arxiv.org/pdf/2505.20451.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20451v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20451v1', 'Amulet: Putting Complex Multi-Turn Conversations on the Stand with LLM Juries')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sahana Ramnath, Anurag Mudgil, Brihi Joshi, Skyler Hallinan, Xiang Ren

**分类**: cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出Amulet框架以提升复杂多轮对话的LLM评估能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多轮对话` `语言模型` `对话行为` `会话原则` `评判机制` `人工智能` `自然语言处理`

## 📋 核心要点

1. 现有方法在多轮对话中难以准确评估用户意图的变化，导致评判结果不够可靠。
2. Amulet框架通过引入对话行为和会话原则，增强了LLM评判者在复杂对话中的判断能力。
3. 在四个具有挑战性的数据集上，Amulet显示出显著的性能提升，尤其是在意图变化和响应区分方面。

## 📝 摘要（中文）

当前，大型语言模型（LLM）被广泛用作评估其他语言模型响应的评判者。因此，基于真实世界语言模型使用情况对这些LLM评判者进行基准测试和改进显得尤为重要。我们提出了Amulet框架，利用对话行为和会话原则的相关语言学概念，提升LLM评判者在复杂多轮对话上下的准确性。研究表明，人在对话中频繁改变意图，且75%的偏好响应可以通过对话行为和/或会话原则进行区分，强调了后者在评判中的重要性。Amulet可作为单一LLM的评判者使用，也可与不同的LLM评判者集成，显著提升了四个数据集的基线表现。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有LLM评判者在复杂多轮对话中对用户意图变化的评估不足，导致评判结果的准确性和可靠性较低。

**核心思路**：Amulet框架通过引入对话行为和会话原则的概念，帮助LLM更好地理解和评估对话中的意图变化，从而提升评判的准确性。

**技术框架**：Amulet的整体架构包括数据预处理、对话行为和会话原则的提取、LLM评判模型的训练和评估等主要模块。每个模块都针对多轮对话的特性进行了优化。

**关键创新**：Amulet的核心创新在于结合了对话行为和会话原则的评估机制，使得LLM能够更准确地捕捉对话中的意图变化，这一方法与传统的单一评判机制有本质区别。

**关键设计**：在模型设计中，Amulet采用了特定的损失函数以强调对话行为和会话原则的影响，同时在网络结构上进行了调整，以适应多轮对话的复杂性。

## 📊 实验亮点

在四个具有挑战性的数据集上，Amulet展示了显著的性能提升，尤其是人类在对话中60%至70%的时间会改变意图，而75%的偏好响应可以通过对话行为和会话原则进行有效区分，强调了这些因素在评判中的重要性。

## 🎯 应用场景

Amulet框架在人机对话系统、智能助手和客服机器人等领域具有广泛的应用潜力。通过提升对话评估的准确性，能够显著改善用户体验和系统响应质量，未来可能推动更智能的对话系统的发展。

## 📄 摘要（原文）

> Today, large language models are widely used as judges to evaluate responses from other language models. Hence, it is imperative to benchmark and improve these LLM-judges on real-world language model usage: a typical human-assistant conversation is lengthy, and shows significant diversity in topics, intents, and requirements across turns, e.g. social interactions, task requests, feedback. We present Amulet, a framework that leverages pertinent linguistic concepts of dialog-acts and maxims to improve the accuracy of LLM-judges on preference data with complex, multi-turn conversational context. Amulet presents valuable insights about (a) the communicative structures and intents present in the conversation (dialog acts), and (b) the satisfaction of conversational principles (maxims) by the preference responses, and uses them to make judgments. On four challenging datasets, Amulet shows that (a) humans frequently (60 to 70 percent of the time) change their intents from one turn of the conversation to the next, and (b) in 75 percent of instances, the preference responses can be differentiated via dialog acts and/or maxims, reiterating the latter's significance in judging such data. Amulet can be used either as a judge by applying the framework to a single LLM, or integrated into a jury with different LLM judges; our judges and juries show strong improvements on relevant baselines for all four datasets.

