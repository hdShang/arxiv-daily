---
layout: default
title: Rewriting Pre-Training Data Boosts LLM Performance in Math and Code
---

# Rewriting Pre-Training Data Boosts LLM Performance in Math and Code

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02881" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02881v3</a>
  <a href="https://arxiv.org/pdf/2505.02881.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02881v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02881v3', 'Rewriting Pre-Training Data Boosts LLM Performance in Math and Code')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kazuki Fujii, Yukito Tajima, Sakae Mizuki, Hinari Shimada, Taihei Shiotani, Koshiro Saito, Masanari Ohi, Masaki Kawamura, Taishi Nakamura, Takumi Okamoto, Shigeki Ishida, Kakeru Hattori, Youmi Ma, Hiroya Takamura, Rio Yokota, Naoaki Okazaki

**分类**: cs.LG, cs.AI

**发布日期**: 2025-05-05 (更新: 2025-07-04)

---

## 💡 一句话要点

**通过重写预训练数据提升大语言模型在数学和代码生成中的表现**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `程序合成` `数学推理` `数据集重写` `预训练优化`

## 📋 核心要点

1. 现有方法在程序合成和数学推理中受限于预训练数据的质量，导致性能不足。
2. 本文提出的SwallowCode和SwallowMath数据集，通过重写公共数据，系统性提升了LLM的性能。
3. 实验结果显示，使用新数据集进行预训练，LLM在多个基准测试中显著提高了准确率。

## 📝 摘要（中文）

大型语言模型（LLMs）在程序合成和数学推理中的性能受到预训练语料质量的根本限制。本文介绍了两个开放许可的数据集，通过系统性重写公共数据显著提升LLM性能。SwallowCode（约161亿个标记）通过四阶段流程精炼Python代码片段，SwallowMath（约23亿个标记）则通过去除冗余、恢复上下文和重新格式化解决方案来增强数学数据。在固定的500亿标记训练预算内，使用SwallowCode进行Llama-3.1-8B的持续预训练，在HumanEval和HumanEval+上分别提升了17.0和17.7的通过率，超越了基线模型的代码生成能力。所有数据集、提示和检查点均公开可用，促进可重复研究并推动LLM在专业领域的预训练进展。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在程序合成和数学推理中因预训练数据质量不足而导致的性能限制。现有方法通常依赖排除性过滤或有限的转换，未能有效利用低质量代码。

**核心思路**：提出的重写和保留方法通过系统性重写公共数据，提升了数据的实用性，最大化了低质量代码的利用率，从而增强了模型的学习效果。

**技术框架**：整体流程分为两个主要数据集：SwallowCode和SwallowMath。SwallowCode经过语法验证、基于pylint的风格过滤和两阶段的LLM重写，确保代码片段的风格一致性和算法效率；SwallowMath则通过去除冗余、恢复上下文和逐步解释格式化解决方案来提升数学数据质量。

**关键创新**：最重要的创新在于重写和保留方法的引入，与现有方法相比，能够有效提升低质量代码的质量，而不仅仅是排除不合格数据。

**关键设计**：在SwallowCode中，采用了四阶段的处理流程，确保每个阶段都能提升代码质量；在SwallowMath中，重写过程强调了上下文的恢复和解决方案的清晰表达。

## 📊 实验亮点

实验结果显示，使用SwallowCode进行Llama-3.1-8B的持续预训练，在HumanEval上提升了17.0的通过率，在HumanEval+上提升了17.7；使用SwallowMath则在GSM8K和MATH上分别提升了12.4和7.6的准确率，显著超越了基线模型。

## 🎯 应用场景

该研究的潜在应用领域包括教育、编程辅助工具和自动化代码生成等。通过提升LLM在数学和代码生成方面的能力，可以为开发更智能的编程助手、教育工具和自动化系统提供支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> The performance of large language models (LLMs) in program synthesis and mathematical reasoning is fundamentally limited by the quality of their pre-training corpora. We introduce two openly licensed datasets, released under the Llama 3.3 Community License, that significantly enhance LLM performance by systematically rewriting public data. SwallowCode (approximately 16.1 billion tokens) refines Python snippets from The-Stack-v2 through a novel four-stage pipeline: syntax validation, pylint-based style filtering, and a two-stage LLM rewriting process that enforces style conformity and transforms snippets into self-contained, algorithmically efficient examples. Unlike prior methods that rely on exclusionary filtering or limited transformations, our transform-and-retain approach upgrades low-quality code, maximizing data utility. SwallowMath (approximately 2.3 billion tokens) enhances Finemath-4+ by removing boilerplate, restoring context, and reformatting solutions into concise, step-by-step explanations. Within a fixed 50 billion token training budget, continual pre-training of Llama-3.1-8B with SwallowCode boosts pass@1 by +17.0 on HumanEval and +17.7 on HumanEval+ compared to Stack-Edu, surpassing the baseline model's code generation capabilities. Similarly, substituting SwallowMath yields +12.4 accuracy on GSM8K and +7.6 on MATH. Ablation studies confirm that each pipeline stage contributes incrementally, with rewriting delivering the largest gains. All datasets, prompts, and checkpoints are publicly available, enabling reproducible research and advancing LLM pre-training for specialized domains.

