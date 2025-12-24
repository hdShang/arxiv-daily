---
layout: default
title: "Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?"
---

# Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.17536" class="toolbar-btn" target="_blank">📄 arXiv: 2508.17536v2</a>
  <a href="https://arxiv.org/pdf/2508.17536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.17536v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.17536v2', 'Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li

**分类**: cs.CL, cs.MA

**发布日期**: 2025-08-24 (更新: 2025-10-23)

**备注**: NeurIPS 2025 Spotlight

**🔗 代码/项目**: [GITHUB](https://github.com/deeplearning-wisc/debate-or-vote)

---

## 💡 一句话要点

**提出多代理辩论与投票机制以优化大语言模型决策**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多代理辩论` `大语言模型` `自然语言处理` `决策机制` `性能提升`

## 📋 核心要点

1. 现有的多代理辩论方法在提升大语言模型性能方面的关键因素尚不明确，导致其有效性受到质疑。
2. 本文通过将多代理辩论拆解为多数投票和代理间辩论，提出了一种新的理论框架来分析其贡献。
3. 实验结果表明，多数投票在性能提升中占据主导地位，而辩论本身并未提高预期正确性。

## 📝 摘要（中文）

多代理辩论（MAD）作为一种新兴的协作推理范式，旨在提升大语言模型的性能。尽管取得了一定进展，但MAD的有效性驱动因素尚不明确。本文将MAD拆解为两个关键组成部分——多数投票和代理间辩论，并评估其各自的贡献。通过在七个自然语言处理基准上的广泛实验，发现多数投票单独就能解释大部分性能提升。为此，提出了一个理论框架，将辩论建模为随机过程，证明其不会提升预期正确性。基于这些见解，研究表明，通过偏向修正的信念更新可以显著增强辩论的有效性。整体结果表明，尽管MAD具有潜力，但在许多实际场景中，简单的集成方法仍然是更强大和可靠的替代方案。

## 🔬 方法详解

**问题定义**：本文旨在探讨多代理辩论（MAD）在提升大语言模型性能中的有效性及其驱动因素。现有方法未能明确区分多数投票与辩论的贡献，导致对MAD的理解不够深入。

**核心思路**：通过将MAD拆解为两个组成部分，本文提出了一个理论框架，将辩论视为随机过程，从而分析其对模型性能的影响。

**技术框架**：研究首先定义了MAD的两个核心组件：多数投票和代理间辩论。接着，通过实验验证这两个组件在不同自然语言处理任务中的表现，最后提出针对性干预以优化辩论效果。

**关键创新**：最重要的技术创新在于将辩论建模为随机过程，并证明其不会提升预期正确性。这一发现挑战了传统观点，强调了多数投票的重要性。

**关键设计**：在实验中，采用了七个自然语言处理基准，设计了不同的信念更新策略，以评估辩论和投票的效果。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果显示，单独的多数投票能够解释大部分性能提升，相较于传统的多代理辩论方法，简单的集成方法在许多实际应用中表现出更强的可靠性和效果。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能对话系统和多代理协作任务。通过优化决策机制，能够提升模型在复杂场景下的表现，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Multi-Agent Debate~(MAD) has emerged as a promising paradigm for improving the performance of large language models through collaborative reasoning. Despite recent advances, the key factors driving MAD's effectiveness remain unclear. In this work, we disentangle MAD into two key components--Majority Voting and inter-agent Debate--and assess their respective contributions. Through extensive experiments across seven NLP benchmarks, we find that Majority Voting alone accounts for most of the performance gains typically attributed to MAD. To explain this, we propose a theoretical framework that models debate as a stochastic process. We prove that it induces a martingale over agents' belief trajectories, implying that debate alone does not improve expected correctness. Guided by these insights, we demonstrate that targeted interventions, by biasing the belief update toward correction, can meaningfully enhance debate effectiveness. Overall, our findings suggest that while MAD has potential, simple ensembling methods remain strong and more reliable alternatives in many practical settings. Code is released in https://github.com/deeplearning-wisc/debate-or-vote.

