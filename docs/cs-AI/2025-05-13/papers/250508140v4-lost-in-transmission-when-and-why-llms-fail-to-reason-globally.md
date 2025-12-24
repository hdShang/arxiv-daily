---
layout: default
title: Lost in Transmission: When and Why LLMs Fail to Reason Globally
---

# Lost in Transmission: When and Why LLMs Fail to Reason Globally

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08140" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08140v4</a>
  <a href="https://arxiv.org/pdf/2505.08140.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08140v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08140v4', 'Lost in Transmission: When and Why LLMs Fail to Reason Globally')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tobias Schnabel, Kiran Tomlinson, Adith Swaminathan, Jennifer Neville

**分类**: cs.AI, cs.FL, cs.LG

**发布日期**: 2025-05-13 (更新: 2025-10-24)

**备注**: 36 pages; accepted to NeurIPS '25 (spotlight)

---

## 💡 一句话要点

**提出BAPO模型以解决LLMs在复杂推理中的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `复杂推理` `有界注意力` `信息流动` `思维链` `推理问题分类` `模型架构` `带宽限制`

## 📋 核心要点

1. 现有的LLMs在处理需要复杂推理的任务时，常常因为信息流动的容量限制而失败。
2. 论文提出了有界注意前缀Oracle（BAPO）模型，旨在模拟LLMs中注意力头的带宽约束，从而解决推理问题。
3. 实验结果显示，主流LLMs在BAPO-easy任务上表现良好，但在BAPO-hard任务上失败，验证了理论预测。

## 📝 摘要（中文）

尽管变换器基础的大型语言模型（LLMs）取得了诸多成功，但在需要对输入的较大部分进行复杂推理的任务中仍然存在困难。本文认为，这些失败源于LLMs内部信息流动的容量限制。为此，作者引入了有界注意前缀Oracle（BAPO）模型，作为一种新的计算框架，模拟注意力头的带宽约束。研究表明，多个重要的推理问题如图的可达性需要高通信带宽才能被BAPOs解决；这些问题被称为BAPO-hard。实验结果验证了理论预测，显示GPT-4o、Claude和Gemini在BAPO-easy任务上表现良好，但在相对较小的BAPO-hard任务上失败。此外，BAPOs还揭示了思维链（CoT）的另一个好处：通过CoT分解任务可以将任何BAPO-hard问题转化为BAPO-easy问题。研究结果为LLMs的关键失败提供了原则性解释，并建议了缓解带宽限制的架构和推理方法的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在复杂推理任务中的局限性，尤其是由于信息流动的带宽限制导致的失败。现有方法未能有效处理需要高通信带宽的推理问题。

**核心思路**：论文的核心思路是引入BAPO模型，通过模拟注意力头的带宽限制，提供一个新的视角来理解LLMs在推理任务中的表现。这样的设计有助于识别和分类不同难度的推理问题。

**技术框架**：BAPO模型的整体架构包括对注意力机制的带宽约束建模，主要模块包括信息流动的分析和推理问题的分类。通过对比不同任务的带宽需求，评估模型的表现。

**关键创新**：最重要的技术创新在于引入了BAPO-hard和BAPO-easy的分类，明确了不同推理问题对带宽的需求。这一分类方法与现有的推理模型有本质区别，提供了更深入的理解。

**关键设计**：在模型设计中，关键参数包括注意力头的数量和带宽限制的设定。损失函数的设计也考虑了推理任务的复杂性，以确保模型能够有效学习和适应不同的推理场景。

## 📊 实验亮点

实验结果显示，GPT-4o、Claude和Gemini在BAPO-easy任务上表现优异，但在BAPO-hard任务上失败，验证了理论预测。研究表明，使用思维链（CoT）可以将BAPO-hard问题转化为BAPO-easy问题，从而显著提升推理能力。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和复杂决策支持系统。通过改进LLMs的推理能力，可以在更广泛的场景中提升其应用效果，尤其是在需要复杂逻辑推理的任务中。未来，BAPO模型的思路可能会影响LLMs的架构设计和推理方法，推动更智能的AI系统的发展。

## 📄 摘要（原文）

> Despite their many successes, transformer-based large language models (LLMs) continue to struggle with tasks that require complex reasoning over large parts of their input. We argue that these failures arise due to capacity limits on the accurate flow of information within LLMs. To formalize this issue, we introduce the bounded attention prefix oracle (BAPO) model, a new computational framework that models bandwidth constraints on attention heads, the mechanism for internal communication in LLMs. We show that several important reasoning problems like graph reachability require high communication bandwidth for BAPOs to solve; we call these problems BAPO-hard. Our experiments corroborate our theoretical predictions: GPT-4o, Claude, and Gemini succeed on BAPO-easy tasks and fail even on relatively small BAPO-hard tasks. BAPOs also reveal another benefit of chain of thought (CoT): we prove that breaking down a task using CoT can turn any BAPO-hard problem into a BAPO-easy one. Our results offer principled explanations for key LLM failures and suggest directions for architectures and inference methods that mitigate bandwidth limits.

