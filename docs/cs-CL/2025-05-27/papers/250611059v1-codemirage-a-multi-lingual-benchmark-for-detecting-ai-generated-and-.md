---
layout: default
title: "CodeMirage: A Multi-Lingual Benchmark for Detecting AI-Generated and Paraphrased Source Code from Production-Level LLMs"
---

# CodeMirage: A Multi-Lingual Benchmark for Detecting AI-Generated and Paraphrased Source Code from Production-Level LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11059" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11059v1</a>
  <a href="https://arxiv.org/pdf/2506.11059.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11059v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11059v1', 'CodeMirage: A Multi-Lingual Benchmark for Detecting AI-Generated and Paraphrased Source Code from Production-Level LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanxi Guo, Siyuan Cheng, Kaiyuan Zhang, Guangyu Shen, Xiangyu Zhang

**分类**: cs.SE, cs.CL, cs.CY, cs.LG

**发布日期**: 2025-05-27

---

## 💡 一句话要点

**提出CodeMirage以解决AI生成代码检测的基准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI生成代码` `代码检测` `基准测试` `多语言支持` `软件安全` `大型语言模型` `代码审查`

## 📋 核心要点

1. 现有的AI生成代码检测基准测试覆盖的编程语言有限，且依赖于能力较弱的生成模型，无法反映真实世界的复杂性。
2. CodeMirage通过涵盖十种编程语言、提供原始和改写代码样本，以及整合多个顶尖LLMs的输出，解决了现有基准的不足。
3. 通过对十个检测器的评估，发现了当前检测器的优缺点，并提出了未来研究的关键挑战，推动了检测技术的发展。

## 📝 摘要（中文）

大型语言模型（LLMs）已成为现代软件开发的重要组成部分，生成大量AI生成的源代码。尽管这些模型提高了编程生产力，但其误用带来了代码抄袭、许可证违规和不安全程序传播等重大风险。因此，强有力的AI生成代码检测至关重要。现有基准测试存在不足，主要覆盖的编程语言有限，且依赖于能力较弱的生成模型。本文提出了CodeMirage，一个全面的基准测试，涵盖十种广泛使用的编程语言，包含原始和改写的代码样本，并整合了来自十个顶尖生产级LLMs的输出。通过CodeMirage，我们评估了十个代表性检测器在四种方法论范式下的表现，揭示了当前检测器的优缺点，并识别了未来工作的关键挑战。我们相信CodeMirage为开发稳健且具有普适性的AI生成代码检测器提供了严格且实用的测试平台。

## 🔬 方法详解

**问题定义**：本文旨在解决AI生成代码的检测问题，现有方法在编程语言覆盖和生成模型能力上存在明显不足，无法满足实际应用需求。

**核心思路**：论文提出CodeMirage基准，通过多语言支持和多样化的代码样本，提升检测器的评估标准和实用性。

**技术框架**：整体架构包括数据收集、样本生成、检测器评估和结果分析四个主要模块，确保全面覆盖和准确评估。

**关键创新**：CodeMirage的最大创新在于其多语言支持和对多种生成模型的整合，显著提高了检测的全面性和准确性。

**关键设计**：在参数设置上，使用了多种评估指标，并设计了适应不同检测器的评估配置，确保结果的可靠性和可比性。

## 📊 实验亮点

实验结果显示，使用CodeMirage评估的检测器在多种配置下表现出色，揭示了当前检测器在不同编程语言和代码样本类型上的优缺点，推动了检测技术的进一步研究和改进。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、代码审查和安全性检测等，能够帮助开发者识别和防止AI生成代码中的潜在风险，提升软件质量和安全性。未来，CodeMirage有望成为AI生成代码检测领域的标准基准，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Large language models (LLMs) have become integral to modern software development, producing vast amounts of AI-generated source code. While these models boost programming productivity, their misuse introduces critical risks, including code plagiarism, license violations, and the propagation of insecure programs. As a result, robust detection of AI-generated code is essential. To support the development of such detectors, a comprehensive benchmark that reflects real-world conditions is crucial. However, existing benchmarks fall short -- most cover only a limited set of programming languages and rely on less capable generative models. In this paper, we present CodeMirage, a comprehensive benchmark that addresses these limitations through three major advancements: (1) it spans ten widely used programming languages, (2) includes both original and paraphrased code samples, and (3) incorporates outputs from ten state-of-the-art production-level LLMs, including both reasoning and non-reasoning models from six major providers. Using CodeMirage, we evaluate ten representative detectors across four methodological paradigms under four realistic evaluation configurations, reporting results using three complementary metrics. Our analysis reveals nine key findings that uncover the strengths and weaknesses of current detectors, and identify critical challenges for future work. We believe CodeMirage offers a rigorous and practical testbed to advance the development of robust and generalizable AI-generated code detectors.

