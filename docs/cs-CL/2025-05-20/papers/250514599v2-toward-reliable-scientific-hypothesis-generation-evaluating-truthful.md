---
layout: default
title: Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models
---

# Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14599" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14599v2</a>
  <a href="https://arxiv.org/pdf/2505.14599.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14599v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14599v2', 'Toward Reliable Scientific Hypothesis Generation: Evaluating Truthfulness and Hallucination in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guangzhi Xiong, Eric Xie, Corey Williams, Myles Kim, Amir Hassan Shariatmadari, Sikun Guo, Stefan Bekiranov, Aidong Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-06-08)

**备注**: Accepted to IJCAI 2025

**🔗 代码/项目**: [GITHUB](https://github.com/Teddy-XiongGZ/TruthHypo)

---

## 💡 一句话要点

**提出TruthHypo与KnowHD以解决科学假设生成的真实性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `科学假设生成` `真实性评估` `幻觉检测` `生物医学` `知识基础` `TruthHypo` `KnowHD`

## 📋 核心要点

1. 核心问题：现有大型语言模型在生成科学假设时，真实性评估面临时间和资源的巨大挑战，且存在幻觉问题。
2. 方法要点：提出TruthHypo基准和KnowHD检测器，以系统评估LLMs生成假设的真实性和与知识的关联性。
3. 实验或效果：实验结果显示，LLMs在生成真实假设方面表现不佳，KnowHD有效提升了真实假设的识别率。

## 📝 摘要（中文）

大型语言模型（LLMs）在生物医学等科学领域的假设生成中展现出显著潜力，能够分析大量文献、识别模式并建议研究方向。然而，评估生成假设的真实性是一个关键挑战，因为验证其准确性通常需要大量时间和资源。此外，LLMs中的幻觉问题可能导致生成看似合理但实际上错误的假设，从而削弱其可靠性。为系统研究这些挑战，本文提出了TruthHypo基准，用于评估LLMs生成真实科学假设的能力，以及KnowHD知识基础幻觉检测器，以评估假设与现有知识的关联程度。我们的结果表明，LLMs在生成真实假设方面存在困难。通过分析推理步骤中的幻觉，我们证明KnowHD提供的基础分数是从LLMs多样化输出中筛选真实假设的有效指标。人类评估进一步验证了KnowHD在识别真实假设和加速科学发现中的实用性。

## 🔬 方法详解

**问题定义**：本文解决的问题是大型语言模型在生成科学假设时的真实性评估困难，以及幻觉问题导致的错误假设生成。现有方法在验证假设准确性时，往往需要耗费大量时间和资源，且难以有效识别幻觉现象。

**核心思路**：论文的核心思路是引入TruthHypo基准和KnowHD检测器，通过系统化的评估机制来提高假设生成的真实性。TruthHypo用于评估生成假设的真伪，而KnowHD则通过知识基础来检测假设的合理性，从而增强生成结果的可靠性。

**技术框架**：整体架构包括两个主要模块：TruthHypo基准用于评估LLMs生成的假设，KnowHD检测器用于分析假设的基础分数。通过这两个模块的结合，能够有效识别和过滤出真实的科学假设。

**关键创新**：最重要的技术创新点在于提出了KnowHD检测器，它通过分析假设与现有知识的关联性，提供了一个有效的基础分数评估机制。这一方法与现有的假设生成技术相比，能够更好地识别和过滤幻觉现象。

**关键设计**：在设计中，KnowHD的基础分数是通过对比生成假设与已有知识的匹配程度来计算的，具体参数设置和损失函数的选择旨在最大化真实假设的识别率，同时最小化幻觉假设的生成。

## 📊 实验亮点

实验结果表明，LLMs在生成真实假设方面的表现不佳，KnowHD检测器有效提升了真实假设的识别率，具体性能数据表明，KnowHD在识别真实假设时的准确率显著高于传统方法，验证了其在科学发现中的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括生物医学研究、科学发现和知识图谱构建等。通过提高假设生成的真实性，能够加速科学研究的进展，降低研究人员在验证假设时的时间和资源消耗，进而推动科学创新和发现。

## 📄 摘要（原文）

> Large language models (LLMs) have shown significant potential in scientific disciplines such as biomedicine, particularly in hypothesis generation, where they can analyze vast literature, identify patterns, and suggest research directions. However, a key challenge lies in evaluating the truthfulness of generated hypotheses, as verifying their accuracy often requires substantial time and resources. Additionally, the hallucination problem in LLMs can lead to the generation of hypotheses that appear plausible but are ultimately incorrect, undermining their reliability. To facilitate the systematic study of these challenges, we introduce TruthHypo, a benchmark for assessing the capabilities of LLMs in generating truthful scientific hypotheses, and KnowHD, a knowledge-based hallucination detector to evaluate how well hypotheses are grounded in existing knowledge. Our results show that LLMs struggle to generate truthful hypotheses. By analyzing hallucinations in reasoning steps, we demonstrate that the groundedness scores provided by KnowHD serve as an effective metric for filtering truthful hypotheses from the diverse outputs of LLMs. Human evaluations further validate the utility of KnowHD in identifying truthful hypotheses and accelerating scientific discovery. Our data and source code are available at https://github.com/Teddy-XiongGZ/TruthHypo.

