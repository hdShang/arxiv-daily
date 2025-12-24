---
layout: default
title: Do We Know What LLMs Don't Know? A Study of Consistency in Knowledge Probing
---

# Do We Know What LLMs Don't Know? A Study of Consistency in Knowledge Probing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21701" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21701v2</a>
  <a href="https://arxiv.org/pdf/2505.21701.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21701v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21701v2', 'Do We Know What LLMs Don\'t Know? A Study of Consistency in Knowledge Probing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raoyuan Zhao, Abdullatif Köksal, Ali Modarressi, Michael A. Hedderich, Hinrich Schütze

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-05-30)

---

## 💡 一句话要点

**提出新方法识别大型语言模型知识盲区的一致性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `知识探测` `一致性评估` `输入扰动` `人工智能可靠性`

## 📋 核心要点

1. 现有知识探测方法存在显著的不一致性，导致对大型语言模型知识盲区的识别不可靠。
2. 论文提出了一种基于输入变体和定量指标的新评估过程，以揭示知识探测中的不一致性。
3. 实验结果显示，同一方法内和不同方法间的知识探测一致性均很低，强调了改进探测框架的必要性。

## 📝 摘要（中文）

大型语言模型（LLMs）的可靠性受到其幻觉倾向的严重影响，因此需要精确识别其知识盲区。本文提出了一种基于输入变体和定量指标的新过程来评估现有的知识探测方法。研究揭示了知识探测中的两种不一致性维度：同一方法内的不一致性和不同方法间的不一致性。具体而言，微小的非语义扰动会导致同一探测方法中检测到的知识盲区出现显著差异，而不同探测方法之间的决策一致性低至7%。这些发现挑战了现有的探测方法，强调了对抗扰动的稳健探测框架的迫切需求。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型知识探测方法的不一致性问题。现有方法在不同输入和探测手段下，往往无法稳定地识别模型的知识盲区，导致结果不可靠。

**核心思路**：论文的核心思路是通过引入输入变体和定量评估指标，系统性地分析知识探测方法的一致性问题。这种设计旨在揭示探测过程中的潜在不稳定性。

**技术框架**：整体架构包括输入变体生成、知识探测执行和一致性评估三个主要模块。首先，通过对输入进行微小扰动生成变体；然后，应用不同的探测方法进行知识评估；最后，利用定量指标分析探测结果的一致性。

**关键创新**：最重要的技术创新点在于系统性地揭示了同一方法内和不同方法间的知识探测不一致性，特别是通过简单的输入扰动可以显著影响探测结果。这一发现与现有方法的本质区别在于强调了输入对探测结果的敏感性。

**关键设计**：在实验中，采用了多种输入扰动方式，如选项洗牌等，并设计了相应的定量评估指标，以衡量探测结果的一致性。具体的参数设置和损失函数设计则依赖于所选的探测方法。实验结果表明，决策一致性在不同方法间低至7%。

## 📊 实验亮点

实验结果显示，同一探测方法内的知识盲区一致性低至40%，而不同探测方法间的决策一致性仅为7%。这些数据突显了现有探测方法的局限性，并强调了对抗扰动的稳健探测框架的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的开发与评估、人工智能系统的可靠性测试以及教育领域的智能辅导系统。通过识别和修复知识盲区，可以提升模型的实际应用价值和用户信任度，推动更安全的AI技术发展。

## 📄 摘要（原文）

> The reliability of large language models (LLMs) is greatly compromised by their tendency to hallucinate, underscoring the need for precise identification of knowledge gaps within LLMs. Various methods for probing such gaps exist, ranging from calibration-based to prompting-based methods. To evaluate these probing methods, in this paper, we propose a new process based on using input variations and quantitative metrics. Through this, we expose two dimensions of inconsistency in knowledge gap probing. (1) Intra-method inconsistency: Minimal non-semantic perturbations in prompts lead to considerable variance in detected knowledge gaps within the same probing method; e.g., the simple variation of shuffling answer options can decrease agreement to around 40%. (2) Cross-method inconsistency: Probing methods contradict each other on whether a model knows the answer. Methods are highly inconsistent -- with decision consistency across methods being as low as 7% -- even though the model, dataset, and prompt are all the same. These findings challenge existing probing methods and highlight the urgent need for perturbation-robust probing frameworks.

