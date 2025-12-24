---
layout: default
title: "LegalEval-Q: A New Benchmark for The Quality Evaluation of LLM-Generated Legal Text"
---

# LegalEval-Q: A New Benchmark for The Quality Evaluation of LLM-Generated Legal Text

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24826" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24826v2</a>
  <a href="https://arxiv.org/pdf/2505.24826.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24826v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24826v2', 'LegalEval-Q: A New Benchmark for The Quality Evaluation of LLM-Generated Legal Text')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Li yunhan, Wu gengshen

**分类**: cs.CL, cs.CV

**发布日期**: 2025-05-30 (更新: 2025-11-10)

**备注**: 10 pages, 11 figures

**🔗 代码/项目**: [GITHUB](https://github.com/lyxx3rd/LegalEval-Q)

---

## 💡 一句话要点

**提出LegalEval-Q以解决法律文本生成质量评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `法律文本生成` `大型语言模型` `质量评估` `回归模型` `推理模型` `标准化评估` `清晰度` `连贯性`

## 📋 核心要点

1. 现有的法律文本生成评估方法主要关注事实准确性，忽略了语言质量的其他重要方面。
2. 本文提出了一个回归模型来评估法律文本的清晰度、连贯性和术语，同时创建了专门的法律问题集。
3. 通过分析49个LLMs，发现模型参数在140亿时质量趋于平稳，推理模型表现优于基础架构。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在法律应用中的日益普及，现有评估基准主要关注事实准确性，而忽视了清晰度、连贯性和术语等重要语言质量方面。为了解决这一问题，本文提出了三个步骤：首先，开发了一个回归模型以评估法律文本的质量；其次，创建了一套专门的法律问题集；最后，利用该评估框架分析了49个LLMs。研究发现，模型质量在140亿参数时趋于平稳，72亿参数时仅有2.7%的边际提升；工程选择如量化和上下文长度对结果影响微小；推理模型的表现始终优于基础架构。研究的一个重要成果是发布了排名列表和帕累托分析，突出了Qwen3系列在性价比方面的最佳选择。

## 🔬 方法详解

**问题定义**：本文旨在解决当前法律文本生成质量评估中对语言质量方面的忽视，现有方法主要集中在事实准确性上，导致评估不全面。

**核心思路**：论文提出通过回归模型综合评估法律文本的清晰度、连贯性和术语，填补现有评估框架的空白。

**技术框架**：整体架构包括三个主要模块：1) 回归模型用于质量评估；2) 专门的法律问题集；3) 49个LLMs的分析与比较。

**关键创新**：最重要的创新在于建立了一个标准化的评估协议，首次系统性地评估法律文本生成的语言质量，揭示了当前训练数据精炼方法的基本局限性。

**关键设计**：在模型设计中，采用了特定的损失函数和参数设置，以确保评估的准确性和有效性，同时对模型的量化和上下文长度进行了分析，发现其对结果的影响微乎其微。

## 📊 实验亮点

实验结果显示，模型在140亿参数时质量趋于平稳，72亿参数时仅有2.7%的提升，且推理模型在性能上显著优于基础架构。这些发现为法律文本生成模型的选择和优化提供了重要参考。

## 🎯 应用场景

该研究的潜在应用领域包括法律文本生成、法律咨询自动化和法律文书审核等。通过建立标准化的评估协议，可以提升法律领域中LLMs的应用效果，促进法律服务的智能化与高效化，未来可能对法律行业的工作流程产生深远影响。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly used in legal applications, current evaluation benchmarks tend to focus mainly on factual accuracy while largely neglecting important linguistic quality aspects such as clarity, coherence, and terminology. To address this gap, we propose three steps: First, we develop a regression model to evaluate the quality of legal texts based on clarity, coherence, and terminology. Second, we create a specialized set of legal questions. Third, we analyze 49 LLMs using this evaluation framework.
>   Our analysis identifies three key findings: First, model quality levels off at 14 billion parameters, with only a marginal improvement of $2.7\%$ noted at 72 billion parameters. Second, engineering choices such as quantization and context length have a negligible impact, as indicated by statistical significance thresholds above 0.016. Third, reasoning models consistently outperform base architectures. A significant outcome of our research is the release of a ranking list and Pareto analysis, which highlight the Qwen3 series as the optimal choice for cost-performance tradeoffs. This work not only establishes standardized evaluation protocols for legal LLMs but also uncovers fundamental limitations in current training data refinement approaches. Code and models are available at: https://github.com/lyxx3rd/LegalEval-Q.

