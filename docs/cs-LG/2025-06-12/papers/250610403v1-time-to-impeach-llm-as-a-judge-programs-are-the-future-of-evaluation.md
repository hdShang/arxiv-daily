---
layout: default
title: "Time To Impeach LLM-as-a-Judge: Programs are the Future of Evaluation"
---

# Time To Impeach LLM-as-a-Judge: Programs are the Future of Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.10403" class="toolbar-btn" target="_blank">📄 arXiv: 2506.10403v1</a>
  <a href="https://arxiv.org/pdf/2506.10403.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.10403v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.10403v1', 'Time To Impeach LLM-as-a-Judge: Programs are the Future of Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tzu-Heng Huang, Harit Vishwakarma, Frederic Sala

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-12

---

## 💡 一句话要点

**提出PAJAMA以解决LLM评估中的高成本与偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `模型评估` `程序合成` `偏见消减` `自动化评判`

## 📋 核心要点

1. 现有的LLM评估方法面临高API成本和不可靠性等问题，导致评估过程不灵活且存在偏见。
2. 本文提出PAJAMA，通过合成可执行的评判程序来进行模型评估，降低成本并提高评判的可解释性。
3. 实验结果表明，PAJAMA在判断一致性和偏见响应方面显著优于传统的LLM评判方法，并在多个基准数据集上取得了更好的性能。

## 📝 摘要（中文）

大型语言模型（LLMs）广泛用于评估生成内容的质量，但面临高API成本、可靠性不确定、管道不灵活及固有偏见等挑战。为此，本文提出PAJAMA（Program-As-a-Judge for Automated Model Assessment），通过合成可执行的评判程序来替代直接评分。这些合成程序可本地存储和运行，成本显著降低，同时提供可解释和可审计的评判逻辑，易于适应。与基于Qwen2.5-14B的LLM评判相比，程序评判在判断一致性上提高了15.83%，偏见响应减少了23.7%。当将程序判断蒸馏到模型中时，PAJAMA在RewardBench的CHAT-HARD子集上表现优于LLM评判，Prometheus指标提升2.19%，JudgeLM数据集提升8.67%，且成本降低三个数量级。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM评估方法的高成本、偏见和不可靠性等问题。现有方法依赖于直接评分，导致评估过程不灵活且容易受到偏见影响。

**核心思路**：PAJAMA的核心思路是使用LLMs合成可执行的评判程序，而不是直接对响应进行评分。这种方法不仅降低了成本，还提高了评判的可解释性和适应性。

**技术框架**：PAJAMA的整体架构包括程序合成模块、评判执行模块和结果分析模块。程序合成模块负责生成可执行的评判程序，评判执行模块在本地运行这些程序，结果分析模块则对评判结果进行解释和审计。

**关键创新**：PAJAMA的主要创新在于通过合成程序进行评判，这一方法与传统的LLM评判方法本质上不同，后者直接依赖于模型的评分能力。

**关键设计**：在设计上，PAJAMA关注程序的可执行性和适应性，采用了特定的参数设置和损失函数，以确保合成程序在不同场景下的有效性和稳定性。

## 📊 实验亮点

实验结果显示，PAJAMA在判断一致性上提高了15.83%，偏见响应减少了23.7%。在将程序判断蒸馏到模型后，PAJAMA在CHAT-HARD子集上超越了LLM评判，Prometheus指标提升2.19%，JudgeLM数据集提升8.67%，且成本降低三个数量级，展现了显著的性能优势。

## 🎯 应用场景

PAJAMA的研究成果在多个领域具有潜在应用价值，包括自动化内容审核、在线教育评估和智能客服系统等。通过降低评估成本和提高评判一致性，PAJAMA能够为企业和研究机构提供更高效的模型评估解决方案，推动相关技术的进一步发展。

## 📄 摘要（原文）

> Large language models (LLMs) are widely used to evaluate the quality of LLM generations and responses, but this leads to significant challenges: high API costs, uncertain reliability, inflexible pipelines, and inherent biases. To address these, we introduce PAJAMA (Program-As-a-Judge for Automated Model Assessment), a new alternative that uses LLMs to synthesize executable judging programs instead of directly scoring responses. These synthesized programs can be stored and run locally, costing orders of magnitude less while providing interpretable, and auditable judging logic that can be easily adapted. Program-based judges mitigate biases, improving judgment consistency by 15.83% and reducing biased responses by 23.7% on average compared to a Qwen2.5-14B-based LLM-as-a-judge. When program judgments are distilled into a model, PAJAMA outperforms LLM-as-a-judge on the challenging CHAT-HARD subset of RewardBench, outperforming metrics by 2.19% on Prometheus and 8.67% on the JudgeLM dataset, all at three orders of magnitude lower cost.

