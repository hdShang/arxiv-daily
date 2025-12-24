---
layout: default
title: "MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning"
---

# MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16792" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16792v3</a>
  <a href="https://arxiv.org/pdf/2506.16792.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16792v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16792v3', 'MIST: Jailbreaking Black-box Large Language Models via Iterative Semantic Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muyang Zheng, Yuanzhi Yao, Changting Lin, Caihong Kai, Yanxiang Chen, Zhiquan Liu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-20 (更新: 2025-09-20)

**备注**: 13 pages, 6 figures

---

## 💡 一句话要点

**提出MIST以解决黑箱大语言模型的越狱问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `黑箱模型` `越狱攻击` `语义调优` `对抗性训练` `大型语言模型` `安全性评估`

## 📋 核心要点

1. 现有的大型语言模型在对抗越狱攻击时存在显著脆弱性，尤其是在输入的离散性和查询预算限制下。
2. MIST方法通过迭代语义调优，允许攻击者在保留语义意图的同时，逐步优化提示以诱导有害内容。
3. 实验结果显示，MIST在多个数据集上实现了竞争性的攻击成功率和较低的查询次数，优于或匹配了现有的越狱方法。

## 📝 摘要（中文）

尽管已有努力使大型语言模型（LLMs）与社会和道德价值观保持一致，这些模型仍然容易受到越狱攻击，即旨在引发有害响应的方法。由于输入的离散性、对目标LLM的限制访问以及有限的查询预算，越狱黑箱LLM被认为是具有挑战性的。为了解决上述问题，本文提出了一种有效的方法，称为MIST，通过迭代语义调优来越狱黑箱大型语言模型。MIST使攻击者能够迭代地优化提示，保留原始语义意图的同时诱导有害内容。具体而言，为了平衡语义相似性与计算效率，MIST结合了两个关键策略：顺序同义词搜索及其高级版本——顺序确定优化。实验结果表明，MIST在攻击成功率、查询次数和可转移性方面表现出色，超越或匹配了现有的最先进越狱方法。

## 🔬 方法详解

**问题定义**：本文旨在解决黑箱大型语言模型的越狱问题，现有方法在输入离散性、访问限制和查询预算方面存在显著挑战。

**核心思路**：MIST的核心思路是通过迭代优化提示，保持原始语义意图的同时诱导有害内容，从而实现有效的越狱。

**技术框架**：MIST的整体架构包括两个主要模块：顺序同义词搜索和顺序确定优化，前者用于初步优化提示，后者则进一步提升优化效果。

**关键创新**：MIST的主要创新在于结合了顺序同义词搜索与顺序确定优化，显著提高了攻击的成功率和效率，与现有方法相比具有本质区别。

**关键设计**：在设计中，MIST采用了特定的参数设置和损失函数，以确保在优化过程中保持语义相似性，同时降低计算复杂度。具体的网络结构和优化策略在实验中得到了验证。

## 📊 实验亮点

实验结果表明，MIST在两个数据集上实现了较高的攻击成功率，查询次数相对较低，且具有良好的可转移性。与现有最先进的越狱方法相比，MIST在多个指标上表现出色，展示了其在实际应用中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括安全性测试、模型鲁棒性评估以及对抗性训练等。通过有效的越狱方法，研究者可以更好地理解和改进大型语言模型的安全性，进而推动更安全的AI系统的开发。未来，MIST可能在对抗性攻击和防御策略的研究中发挥重要作用。

## 📄 摘要（原文）

> Despite efforts to align large language models (LLMs) with societal and moral values, these models remain susceptible to jailbreak attacks -- methods designed to elicit harmful responses. Jailbreaking black-box LLMs is considered challenging due to the discrete nature of token inputs, restricted access to the target LLM, and limited query budget. To address the issues above, we propose an effective method for jailbreaking black-box large language Models via Iterative Semantic Tuning, named MIST. MIST enables attackers to iteratively refine prompts that preserve the original semantic intent while inducing harmful content. Specifically, to balance semantic similarity with computational efficiency, MIST incorporates two key strategies: sequential synonym search, and its advanced version -- order-determining optimization. We conduct extensive experiments on two datasets using two open-source and four closed-source models. Results show that MIST achieves competitive attack success rate, relatively low query count, and fair transferability, outperforming or matching state-of-the-art jailbreak methods. Additionally, we conduct analysis on computational efficiency to validate the practical viability of MIST.

