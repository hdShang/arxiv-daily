---
layout: default
title: "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models"
---

# FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02735" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02735v1</a>
  <a href="https://arxiv.org/pdf/2505.02735.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02735v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02735v1', 'FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhouliang Yu, Ruotian Peng, Keyi Ding, Yizhe Li, Zhongyuan Peng, Minghao Liu, Yifan Zhang, Zheng Yuan, Huajian Xin, Wenhao Huang, Yandong Wen, Ge Zhang, Weiyang Liu

**分类**: cs.AI, cs.LG

**发布日期**: 2025-05-05

**备注**: Technical Report v1 (33 pages, 8 figures, project page: https://sphere-ai-lab.github.io/FormalMATH/)

---

## 💡 一句话要点

**提出FormalMATH以解决形式数学推理的基准测试问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `形式数学推理` `基准测试` `大型语言模型` `自动形式化` `定理证明` `人机协作` `语义验证`

## 📋 核心要点

1. 核心问题：现有的形式数学推理基准在范围和规模上存在显著不足，限制了AI的推理能力。
2. 方法要点：提出FormalMATH基准，结合人机协作的自动形式化流程，提高形式化效率并降低专家注释成本。
3. 实验或效果：评估显示，当前最强的LLM定理证明器在实际应用中成功率仅为16.46%，并存在领域偏见。

## 📝 摘要（中文）

形式数学推理仍然是人工智能面临的重大挑战，现有基准在范围和规模上存在局限。为此，我们提出了FormalMATH，这是一个大规模的Lean4基准，包含5560个形式验证问题，涵盖从高中奥林匹克挑战到本科定理的多样领域（如代数、应用数学、微积分、数论和离散数学）。为提高手动形式化的效率，我们引入了一种新的人机协作自动形式化流程，整合了专用的大型语言模型（LLMs）进行语句自动形式化、多LLM语义验证以及基于否定的反驳过滤策略。我们的评估显示，尽管当前最强模型在实际采样预算下的成功率仅为16.46%，但FormalMATH为形式数学推理提供了一个稳健的基准。

## 🔬 方法详解

**问题定义**：论文要解决的问题是形式数学推理的基准测试不足，现有方法在范围和规模上存在局限，导致AI在推理能力上的挑战。

**核心思路**：论文的核心思路是通过构建FormalMATH基准，利用人机协作的自动形式化流程来提高形式化的效率，降低专家的注释成本。

**技术框架**：整体架构包括三个主要模块：1) 专用大型语言模型进行语句自动形式化；2) 多LLM语义验证；3) 基于否定的反驳过滤策略，使用现成的LLM证明器。

**关键创新**：最重要的技术创新点在于引入人机协作的自动形式化流程，显著提高了形式化效率，并保留了72.09%的语句在手动验证前的有效性。

**关键设计**：关键设计包括选择合适的LLM进行语句自动形式化，采用多模型的语义验证机制，以及设计否定过滤策略以提高推理的准确性。具体参数设置和损失函数的选择在论文中进行了详细讨论。

## 📊 实验亮点

实验结果显示，当前最强的LLM定理证明器在实际采样预算下的成功率仅为16.46%，并且在不同领域（如代数和微积分）表现出明显的领域偏见。这一发现强调了现有模型在处理复杂数学问题时的局限性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动定理证明、数学软件开发等。通过提供一个标准化的基准，FormalMATH可以帮助研究人员和开发者评估和改进形式数学推理模型，推动相关技术的进步与应用。

## 📄 摘要（原文）

> Formal mathematical reasoning remains a critical challenge for artificial intelligence, hindered by limitations of existing benchmarks in scope and scale. To address this, we present FormalMATH, a large-scale Lean4 benchmark comprising 5,560 formally verified problems spanning from high-school Olympiad challenges to undergraduate-level theorems across diverse domains (e.g., algebra, applied mathematics, calculus, number theory, and discrete mathematics). To mitigate the inefficiency of manual formalization, we introduce a novel human-in-the-loop autoformalization pipeline that integrates: (1) specialized large language models (LLMs) for statement autoformalization, (2) multi-LLM semantic verification, and (3) negation-based disproof filtering strategies using off-the-shelf LLM-based provers. This approach reduces expert annotation costs by retaining 72.09% of statements before manual verification while ensuring fidelity to the original natural-language problems. Our evaluation of state-of-the-art LLM-based theorem provers reveals significant limitations: even the strongest models achieve only 16.46% success rate under practical sampling budgets, exhibiting pronounced domain bias (e.g., excelling in algebra but failing in calculus) and over-reliance on simplified automation tactics. Notably, we identify a counterintuitive inverse relationship between natural-language solution guidance and proof success in chain-of-thought reasoning scenarios, suggesting that human-written informal reasoning introduces noise rather than clarity in the formal reasoning settings. We believe that FormalMATH provides a robust benchmark for benchmarking formal mathematical reasoning.

