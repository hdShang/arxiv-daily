---
layout: default
title: "CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts"
---

# CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05063" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05063v1</a>
  <a href="https://arxiv.org/pdf/2505.05063.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05063v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05063v1', 'CodeMixBench: Evaluating Large Language Models on Code Generation with Code-Mixed Prompts')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Manik Sheokand, Parth Sawant

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-08

---

## 💡 一句话要点

**提出CodeMixBench以解决多语言代码生成评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码生成` `多语言处理` `大型语言模型` `评估基准` `代码混合语言`

## 📋 核心要点

1. 现有评估基准主要集中在英语提示，忽视了多语言开发者的实际需求，导致评估结果不够全面。
2. 提出CodeMixBench，通过引入控制代码混合（CMD）来评估LLMs在多语言环境下的代码生成能力。
3. 实验结果表明，代码混合提示的Pass@1性能显著低于英语提示，尤其是小模型在高CMD水平下表现更差。

## 📝 摘要（中文）

大型语言模型（LLMs）在代码生成任务中取得了显著成功，广泛应用于代码补全、调试和编程辅助等场景。然而，现有的评估基准如HumanEval、MBPP和BigCodeBench主要集中在英语提示上，忽视了多语言开发者在与LLMs交互时常用的代码混合语言。为了解决这一问题，本文提出了CodeMixBench，一个旨在评估LLMs在代码混合提示下的生成能力的新基准。CodeMixBench基于BigCodeBench构建，引入了控制代码混合（CMD），涵盖了三种语言对：Hinglish（印地语-英语）、西班牙语-英语和汉语拼音-英语。我们的评估结果显示，与仅使用英语的提示相比，代码混合提示在Pass@1性能上持续下降，且在较高的CMD水平下，小模型的性能下降幅度更大。CodeMixBench为研究多语言代码生成提供了现实的评估框架，并突出了构建能够在多样语言环境中良好泛化的稳健代码生成模型的新挑战和方向。

## 🔬 方法详解

**问题定义**：本文旨在解决现有代码生成评估基准对多语言提示的忽视，特别是代码混合语言的使用。现有方法未能反映真实开发环境中的多样性，导致评估结果的局限性。

**核心思路**：通过引入控制代码混合（CMD），本文设计了CodeMixBench，以评估LLMs在处理多语言提示时的生成能力。这种设计旨在更好地模拟多语言开发者的实际使用场景。

**技术框架**：CodeMixBench基于BigCodeBench构建，涵盖三种语言对的代码混合提示。评估流程包括生成代码、计算性能指标（如Pass@1）以及对比不同模型在不同CMD水平下的表现。

**关键创新**：最重要的创新在于引入了控制代码混合的机制，使得评估不仅限于单一语言提示，能够更全面地反映模型在多语言环境下的表现。与现有方法相比，CodeMixBench提供了更具现实意义的评估标准。

**关键设计**：在实验中，设置了不同的CMD水平，并评估了1.5B到15B参数的多种开源代码生成模型。损失函数和网络结构的具体细节在论文中进行了详细描述，以确保评估的准确性和可靠性。

## 📊 实验亮点

实验结果显示，代码混合提示的Pass@1性能普遍低于英语提示，尤其是在高CMD水平下，小模型的性能下降幅度更大。这一发现强调了多语言环境下代码生成模型的挑战，为未来的研究提供了重要的方向。

## 🎯 应用场景

该研究的潜在应用领域包括多语言编程环境中的代码生成、智能编程助手和自动化调试工具。通过提供更真实的评估框架，CodeMixBench能够帮助开发者和研究人员理解和改进LLMs在多语言场景下的表现，从而推动相关技术的发展和应用。

## 📄 摘要（原文）

> Large Language Models (LLMs) have achieved remarkable success in code generation tasks, powering various applications like code completion, debugging, and programming assistance. However, existing benchmarks such as HumanEval, MBPP, and BigCodeBench primarily evaluate LLMs on English-only prompts, overlooking the real-world scenario where multilingual developers often use code-mixed language while interacting with LLMs. To address this gap, we introduce CodeMixBench, a novel benchmark designed to evaluate the robustness of LLMs on code generation from code-mixed prompts. Built upon BigCodeBench, CodeMixBench introduces controlled code-mixing (CMD) into the natural language parts of prompts across three language pairs: Hinglish (Hindi-English), Spanish-English, and Chinese Pinyin-English. We comprehensively evaluate a diverse set of open-source code generation models ranging from 1.5B to 15B parameters. Our results show that code-mixed prompts consistently degrade Pass@1 performance compared to their English-only counterparts, with performance drops increasing under higher CMD levels for smaller models. CodeMixBench provides a realistic evaluation framework for studying multilingual code generation and highlights new challenges and directions for building robust code generation models that generalize well across diverse linguistic settings.

