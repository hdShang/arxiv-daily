---
layout: default
title: "Unlearning vs. Obfuscation: Are We Truly Removing Knowledge?"
---

# Unlearning vs. Obfuscation: Are We Truly Removing Knowledge?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02884" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02884v2</a>
  <a href="https://arxiv.org/pdf/2505.02884.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02884v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02884v2', 'Unlearning vs. Obfuscation: Are We Truly Removing Knowledge?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangzhi Sun, Potsawee Manakul, Xiao Zhan, Mark Gales

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-05 (更新: 2025-09-08)

**备注**: To Appear in EMNLP 2025 main conference

---

## 💡 一句话要点

**提出DF-MCQ以解决知识移除的有效性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识移除` `模糊处理` `大型语言模型` `数据隐私` `KL散度` `探测评估` `多项选择题`

## 📋 核心要点

1. 现有的知识移除方法多依赖模糊处理，未能有效去除模型中的敏感信息，导致隐私风险。
2. 本文提出DF-MCQ，通过KL散度优化模型预测分布，旨在实现真正的知识移除。
3. 实验结果显示，DF-MCQ在拒绝率和不确定性方面显著优于传统模糊处理方法。

## 📝 摘要（中文）

知识移除已成为大型语言模型（LLMs）支持数据隐私和合规性的重要能力。现有技术往往依赖于模糊处理，通过注入错误或无关信息来抑制知识，这实际上构成了知识的添加而非真正的移除，导致模型在探测时仍然脆弱。本文正式区分了知识移除与模糊处理，并引入了一种基于探测的评估框架，以评估现有方法是否真正移除了目标信息。此外，我们提出了DF-MCQ，这是一种新颖的知识移除方法，通过使用KL散度平坦化模型对自动生成的多项选择题的预测分布，有效移除关于目标个体的知识，并触发适当的拒绝行为。实验结果表明，DF-MCQ在探测问题上的拒绝率超过90%，且随机选择水平的不确定性显著高于模糊处理。

## 🔬 方法详解

**问题定义**：本文旨在解决现有知识移除方法的不足，尤其是模糊处理未能真正去除敏感信息的问题。现有方法往往通过注入无关信息来掩盖知识，但这并不等同于真正的知识移除，导致模型在探测时仍然存在风险。

**核心思路**：DF-MCQ的核心思路是通过KL散度来平坦化模型对多项选择题的预测分布，从而实现对目标个体知识的有效移除。该方法不仅关注知识的抑制，更强调知识的真正消除，确保模型在面对探测时能够做出适当的拒绝反应。

**技术框架**：DF-MCQ的整体架构包括数据预处理、模型训练和评估三个主要模块。首先，自动生成多项选择题作为输入数据；其次，利用KL散度优化模型的预测分布；最后，通过探测框架评估知识移除的有效性。

**关键创新**：DF-MCQ的主要创新在于其通过KL散度实现知识移除的机制，与传统的模糊处理方法本质上不同，后者仅仅是通过添加噪声来掩盖知识，而DF-MCQ则是通过优化模型的输出分布来实现真正的知识消除。

**关键设计**：在DF-MCQ中，关键的参数设置包括KL散度的权重、模型的学习率以及多项选择题的生成策略。损失函数设计上，强调了对目标知识的移除效果，同时确保模型在探测时的拒绝行为符合预期。

## 📊 实验亮点

实验结果表明，DF-MCQ在知识移除方面的拒绝率超过90%，而在探测问题上的随机选择水平的不确定性显著高于传统的模糊处理方法。这一结果表明DF-MCQ在有效性和安全性方面的显著提升，展示了其在知识移除领域的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括数据隐私保护、合规性要求的AI系统以及需要处理敏感信息的智能助手。DF-MCQ的有效性为开发更安全的AI模型提供了新的思路，能够在保护用户隐私的同时，满足法律和伦理要求，未来可能对AI的广泛应用产生深远影响。

## 📄 摘要（原文）

> Unlearning has emerged as a critical capability for large language models (LLMs) to support data privacy, regulatory compliance, and ethical AI deployment. Recent techniques often rely on obfuscation by injecting incorrect or irrelevant information to suppress knowledge. Such methods effectively constitute knowledge addition rather than true removal, often leaving models vulnerable to probing. In this paper, we formally distinguish unlearning from obfuscation and introduce a probing-based evaluation framework to assess whether existing approaches genuinely remove targeted information. Moreover, we propose DF-MCQ, a novel unlearning method that flattens the model predictive distribution over automatically generated multiple-choice questions using KL-divergence, effectively removing knowledge about target individuals and triggering appropriate refusal behaviour. Experimental results demonstrate that DF-MCQ achieves unlearning with over 90% refusal rate and a random choice-level uncertainty that is much higher than obfuscation on probing questions.

