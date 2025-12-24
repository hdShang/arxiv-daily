---
layout: default
title: "IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation"
---

# IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26076" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26076v1</a>
  <a href="https://arxiv.org/pdf/2509.26076.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26076v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26076v1', 'IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Johannes Schmitt, Gergely Bérczi, Jasper Dekoninck, Jeremy Feusi, Tim Gehrunger, Raphael Appenzeller, Jim Bryan, Niklas Canova, Timo de Wolff, Filippo Gaia, Michel van Garrel, Baran Hashemi, David Holmes, Aitor Iribar Lopez, Victor Jaeck, Martina Jørgensen, Steven Kelk, Stefan Kuhlmann, Adam Kurpisz, Chiara Meroni, Ingmar Metzler, Martin Möller, Samuel Muñoz-Echániz, Robert Nowak, Georg Oberdieck, Daniel Platt, Dylan Possamaï, Gabriel Ribeiro, Raúl Sánchez Galán, Zheming Sun, Josef Teichmann, Richard P. Thomas, Charles Vial

**分类**: cs.CL

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**IMProofBench：用于评估AI在研究级数学证明生成能力的新基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数学证明生成` `大型语言模型` `AI基准测试` `研究级问题` `数学推理`

## 📋 核心要点

1. 现有数学能力评估基准主要集中于最终答案或高中竞赛题，缺乏对研究级数学证明生成能力的有效评估。
2. IMProofBench提供了一个包含同行评审研究级数学问题的基准，并模拟了真实研究环境，允许模型使用网络搜索和数学软件。
3. 实验结果表明，现有LLM在较简单研究级问题上表现良好，但在更具挑战性的问题上仍存在困难，Grok-4和GPT-5分别在最终答案和证明生成上取得最佳结果。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的数学能力不断提高，评估它们在数学知识前沿的研究级任务中的表现变得越来越重要。然而，现有的基准测试存在局限性，因为它们只关注最终答案问题或高中竞赛问题。为了解决这个问题，我们推出了IMProofBench，这是一个私有基准，包含由数学专家开发的39个经过同行评审的问题。每个问题都需要详细的证明，并配有最终答案的子问题，支持通过人工专家评估数学推理能力，并通过自动评分进行大规模定量分析。此外，与之前的基准测试不同，评估设置模拟了真实的研究环境：模型在具有诸如用于文献综述的网络搜索和诸如SageMath之类的数学软件的代理框架中运行。我们的结果表明，当前的LLM可以成功解决更容易的研究级问题，但在更具挑战性的问题上仍然遇到重大困难。在定量方面，Grok-4在最终答案子问题上实现了52%的最高准确率，而GPT-5在证明生成方面表现最佳，为22%的问题实现了完全正确的解决方案。IMProofBench将继续发展成为与数学界合作的动态基准，确保其与评估下一代LLM的相关性。

## 🔬 方法详解

**问题定义**：论文旨在解决现有数学能力评估基准无法有效评估大型语言模型（LLMs）在研究级数学证明生成能力的问题。现有基准主要集中于最终答案或高中竞赛题，无法反映LLMs在复杂数学推理和证明方面的真实水平。

**核心思路**：论文的核心思路是构建一个更具挑战性和现实性的基准测试，即IMProofBench。该基准包含由数学专家设计的、经过同行评审的研究级数学问题，并模拟了真实的研究环境，允许模型使用网络搜索和数学软件等工具。

**技术框架**：IMProofBench的整体框架包括以下几个关键组成部分：1) 问题集：包含39个研究级数学问题，每个问题都需要详细的证明；2) 子问题：每个问题都配有最终答案的子问题，用于辅助评估；3) 评估环境：模拟真实的研究环境，允许模型使用网络搜索和数学软件；4) 评估指标：包括人工评估和自动评分，用于全面评估模型的数学推理和证明能力。

**关键创新**：IMProofBench的关键创新在于其问题集的难度和真实性。与现有基准相比，IMProofBench的问题更具挑战性，更接近数学研究的前沿。此外，IMProofBench模拟了真实的研究环境，允许模型使用各种工具，这使得评估结果更具参考价值。

**关键设计**：IMProofBench的关键设计包括：1) 问题集的选择：问题由数学专家设计，并经过同行评审，确保其难度和质量；2) 评估环境的构建：评估环境模拟真实的研究环境，允许模型使用网络搜索和数学软件；3) 评估指标的设计：评估指标包括人工评估和自动评分，用于全面评估模型的数学推理和证明能力。

## 📊 实验亮点

实验结果表明，当前LLM在较简单的研究级问题上表现良好，但在更具挑战性的问题上仍存在困难。Grok-4在最终答案子问题上实现了52%的最高准确率，而GPT-5在证明生成方面表现最佳，为22%的问题实现了完全正确的解决方案。这些结果为未来LLM在数学领域的改进方向提供了重要参考。

## 🎯 应用场景

IMProofBench可用于评估和提升AI在数学研究领域的应用能力，例如辅助数学家进行定理证明、发现新的数学规律等。该基准的推出将推动AI在数学领域的进一步发展，并有望在科学研究、工程设计等领域发挥重要作用。

## 📄 摘要（原文）

> As the mathematical capabilities of large language models (LLMs) improve, it becomes increasingly important to evaluate their performance on research-level tasks at the frontier of mathematical knowledge. However, existing benchmarks are limited, as they focus solely on final-answer questions or high-school competition problems. To address this gap, we introduce IMProofBench, a private benchmark consisting of 39 peer-reviewed problems developed by expert mathematicians. Each problem requires a detailed proof and is paired with subproblems that have final answers, supporting both an evaluation of mathematical reasoning capabilities by human experts and a large-scale quantitative analysis through automated grading. Furthermore, unlike prior benchmarks, the evaluation setup simulates a realistic research environment: models operate in an agentic framework with tools like web search for literature review and mathematical software such as SageMath. Our results show that current LLMs can succeed at the more accessible research-level questions, but still encounter significant difficulties on more challenging problems. Quantitatively, Grok-4 achieves the highest accuracy of 52% on final-answer subproblems, while GPT-5 obtains the best performance for proof generation, achieving a fully correct solution for 22% of problems. IMProofBench will continue to evolve as a dynamic benchmark in collaboration with the mathematical community, ensuring its relevance for evaluating the next generation of LLMs.

