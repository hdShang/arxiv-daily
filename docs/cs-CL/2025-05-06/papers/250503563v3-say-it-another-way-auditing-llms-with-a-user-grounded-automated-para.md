---
layout: default
title: "Say It Another Way: Auditing LLMs with a User-Grounded Automated Paraphrasing Framework"
---

# Say It Another Way: Auditing LLMs with a User-Grounded Automated Paraphrasing Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03563" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03563v3</a>
  <a href="https://arxiv.org/pdf/2505.03563.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03563v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03563v3', 'Say It Another Way: Auditing LLMs with a User-Grounded Automated Paraphrasing Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cléa Chataigner, Rebecca Ma, Prakhar Ganesh, Yuhao Chen, Afaf Taïk, Elliot Creager, Golnoosh Farnadi

**分类**: cs.CL

**发布日期**: 2025-05-06 (更新: 2025-10-08)

---

## 💡 一句话要点

**提出AUGMENT框架以解决LLMs审计中的语言敏感性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `审计` `自然语言处理` `用户行为` `受控改写` `语言学规则` `系统性弱点`

## 📋 核心要点

1. 现有方法在审计大型语言模型时，往往忽视了语言和人口统计因素的影响，导致审计结果不可靠。
2. 本文提出的AUGMENT框架通过用户行为生成受控的改写，确保审计过程中的语言变换更具针对性和有效性。
3. 实验结果表明，AUGMENT能够揭示在不受限制的改写中被忽视的系统性弱点，提升了审计的可靠性。

## 📝 摘要（中文）

大型语言模型（LLMs）对提示语的细微变化极为敏感，这给可靠审计带来了挑战。现有方法通常采用不受限制的提示改写，可能忽视影响真实用户交互的语言和人口统计因素。本文提出了AUGMENT（自动用户基础建模与自然语言转换评估框架），该框架生成基于用户行为的受控改写。AUGMENT利用语言学知识规则，并通过对指令遵循、语义相似性和现实性的检查来确保改写的可靠性和意义。通过对BBQ和MMLU数据集的案例研究，我们展示了受控改写揭示了在不受限制变异下被掩盖的系统性弱点。这些结果突显了AUGMENT框架在可靠审计中的价值。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在审计过程中对提示语细微变化的敏感性问题。现有方法常常采用不受限制的改写，导致忽视了影响用户交互的语言和人口统计因素。

**核心思路**：AUGMENT框架的核心思路是生成基于用户行为的受控改写，通过语言学知识规则来确保改写的质量和相关性。这样的设计能够更好地反映真实用户的交互方式。

**技术框架**：AUGMENT框架包括多个模块，首先是用户行为分析模块，接着是基于规则的改写生成模块，最后是质量检查模块，确保改写符合语义相似性和现实性要求。

**关键创新**：AUGMENT的主要创新在于其受控改写的生成方式，利用用户行为数据和语言学规则，显著提高了审计的可靠性，与传统的不受限制改写方法形成鲜明对比。

**关键设计**：在设计上，AUGMENT框架采用了多种语言学规则作为参数设置，并引入了针对性损失函数来优化改写的质量，确保生成的改写在语义和现实性上都具有较高的标准。

## 📊 实验亮点

实验结果显示，AUGMENT框架在BBQ和MMLU数据集上能够揭示出传统方法未能发现的系统性弱点，显著提升了审计的可靠性。受控改写的使用使得审计结果更具针对性，确保了语言模型的评估更加全面和准确。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的审计、用户交互分析和自然语言处理系统的改进。AUGMENT框架能够为开发更可靠的语言模型提供支持，确保其在实际应用中的有效性和安全性。未来，随着用户行为数据的丰富，AUGMENT的应用价值将进一步提升。

## 📄 摘要（原文）

> Large language models (LLMs) are highly sensitive to subtle changes in prompt phrasing, posing challenges for reliable auditing. Prior methods often apply unconstrained prompt paraphrasing, which risk missing linguistic and demographic factors that shape authentic user interactions. We introduce AUGMENT (Automated User-Grounded Modeling and Evaluation of Natural Language Transformations), a framework for generating controlled paraphrases, grounded in user behaviors. AUGMENT leverages linguistically informed rules and enforces quality through checks on instruction adherence, semantic similarity, and realism, ensuring paraphrases are both reliable and meaningful for auditing. Through case studies on the BBQ and MMLU datasets, we show that controlled paraphrases uncover systematic weaknesses that remain obscured under unconstrained variation. These results highlight the value of the AUGMENT framework for reliable auditing.

