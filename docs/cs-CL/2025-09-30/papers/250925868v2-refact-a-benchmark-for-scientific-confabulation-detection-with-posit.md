---
layout: default
title: "ReFACT: A Benchmark for Scientific Confabulation Detection with Positional Error Annotations"
---

# ReFACT: A Benchmark for Scientific Confabulation Detection with Positional Error Annotations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25868" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25868v2</a>
  <a href="https://arxiv.org/pdf/2509.25868.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25868v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25868v2', 'ReFACT: A Benchmark for Scientific Confabulation Detection with Positional Error Annotations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yindong Wang, Martin Preiß, Margarita Bugueño, Jan Vincent Hoffbauer, Abdullatif Ghajar, Tolga Buz, Gerard de Melo

**分类**: cs.CL

**发布日期**: 2025-09-30 (更新: 2025-10-01)

**🔗 代码/项目**: [GITHUB](https://github.com/ddz5431/ReFACT)

---

## 💡 一句话要点

**ReFACT：提出一个科学知识捏造检测基准，包含位置错误标注。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `科学知识` `捏造检测` `基准测试` `错误定位`

## 📋 核心要点

1. 现有大型语言模型在科学领域容易捏造事实，缺乏细粒度的评估和纠正机制。
2. ReFACT基准提供专家标注的科学问答对，包含正确答案和错误答案，并标注错误位置和类型。
3. 实验表明，即使是GPT-4o等先进模型在ReFACT上的表现也有限，凸显了基准的价值。

## 📝 摘要（中文）

大型语言模型（LLMs）经常捏造科学事实，严重损害了其可信度。为了应对这一挑战，需要超越二元事实性判断的基准，并实现细粒度的评估。我们推出了ReFACT（Reddit False And Correct Texts），这是一个包含1001个由专家标注的问答对的基准，涵盖了不同的科学领域，用于检测科学知识捏造。每个实例都包含一个科学上正确的答案和一个非事实的对应答案，并标注了精确的错误范围和错误类型。ReFACT支持多阶段评估：（1）捏造检测，（2）细粒度的错误定位，以及（3）纠正。我们对9个最先进的LLM进行了基准测试，发现性能有限（约50%的准确率）。即使是GPT-4o等顶级模型也无法区分事实性和捏造的科学答案，这引发了对LLM作为评判标准的可靠性的担忧。我们的研究结果强调，需要细粒度的、经过人工验证的基准来检测和纠正特定领域背景下的科学知识捏造。该数据集可在https://github.com/ddz5431/ReFACT 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLMs）在科学领域中捏造事实的问题。现有方法通常只关注二元的事实性判断（正确或错误），缺乏对错误位置和类型的细粒度分析，难以有效评估和纠正LLMs的科学知识捏造行为。

**核心思路**：论文的核心思路是构建一个高质量的、细粒度标注的科学知识捏造检测基准ReFACT。通过提供包含错误位置和类型的标注数据，ReFACT能够支持多阶段的评估，包括捏造检测、错误定位和纠正。这种细粒度的评估方式能够更全面地了解LLMs在科学领域的知识缺陷。

**技术框架**：ReFACT基准的构建流程主要包括以下几个阶段：1) 数据收集：从Reddit等平台收集科学相关的问答对；2) 专家标注：由领域专家对每个问答对进行标注，包括提供一个科学上正确的答案和一个非事实的对应答案，并标注非事实答案中的错误范围和错误类型；3) 数据集发布：将标注好的数据整理成ReFACT基准，并公开发布。

**关键创新**：ReFACT的关键创新在于其细粒度的错误标注。与以往的二元事实性判断基准不同，ReFACT不仅标注了答案是否正确，还标注了错误答案中的错误位置和错误类型。这种细粒度的标注方式使得ReFACT能够支持更深入的分析和评估，例如错误定位和纠正。

**关键设计**：ReFACT基准包含1001个专家标注的问答对，涵盖了不同的科学领域。每个实例都包含一个科学上正确的答案和一个非事实的对应答案，并标注了精确的错误范围和错误类型。错误类型包括但不限于概念错误、数值错误和关系错误。论文没有涉及特定的模型结构或损失函数的设计，而是侧重于基准的构建和评估。

## 📊 实验亮点

对9个最先进的LLM进行了基准测试，结果显示，即使是GPT-4o等顶级模型在ReFACT上的准确率也仅为50%左右。这表明，现有LLM在科学知识捏造检测方面仍存在显著不足，凸显了ReFACT基准的价值和意义。该结果也对LLM作为评判标准的可靠性提出了质疑。

## 🎯 应用场景

ReFACT基准可用于评估和改进大型语言模型在科学领域的知识准确性。通过ReFACT，研究人员可以开发更有效的科学知识捏造检测和纠正方法，提高LLMs在科学研究、教育和信息检索等领域的可靠性。未来，ReFACT可以扩展到更多领域，并与其他知识库相结合，构建更强大的科学知识服务。

## 📄 摘要（原文）

> Large Language Models (LLMs) frequently confabulate scientific facts, severely undermining their trustworthiness. Addressing this challenge requires benchmarks that go beyond binary factuality and enable fine-grained evaluation. We introduce ReFACT (Reddit False And Correct Texts), a benchmark of 1,001 expert-annotated question-answer pairs spanning diverse scientific domains for the detection of scientific confabulation. Each instance includes both a scientifically correct answer and a non-factual counterpart annotated with precise error spans and error types. ReFACT enables multi-stage evaluation: (1) confabulation detection, (2) fine-grained error localization, and (3) correction. We benchmark 9 state-of-the-art LLMs, revealing limited performance (about 50 percent accuracy). Even top models such as GPT-4o fail to distinguish factual from confabulated scientific answers, raising concerns about the reliability of LLM-as-judge evaluation paradigms. Our findings highlight the need for fine-grained, human-validated benchmarks to detect and correct scientific confabulation in domain-specific contexts. The dataset is available at: https://github.com/ddz5431/ReFACT

