---
layout: default
title: CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning
---

# CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00750" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00750v2</a>
  <a href="https://arxiv.org/pdf/2506.00750.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00750v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00750v2', 'CodeSense: a Real-World Benchmark and Dataset for Code Semantic Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Monoshi Kumar Roy, Simin Chen, Benjamin Steenhoek, Jinjun Peng, Gail Kaiser, Baishakhi Ray, Wei Le

**分类**: cs.SE, cs.AI

**发布日期**: 2025-05-31 (更新: 2025-10-02)

**🔗 代码/项目**: [PROJECT_PAGE](https://codesense-bench.github.io/)

---

## 💡 一句话要点

**提出CodeSense以解决代码语义推理基准不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码语义推理` `基准测试` `真实数据集` `软件工程` `大语言模型` `细粒度推理` `执行追踪` `模型评估`

## 📋 核心要点

1. 现有的代码推理基准多依赖合成数据集，缺乏真实世界软件工程任务的有效评估。
2. 提出CodeSense基准，提供真实代码的细粒度推理任务，构建真实数据集以支持评估。
3. 实验结果显示，当前LLMs在细粒度推理任务上存在明显性能差距，提示技术虽有帮助但仍受限于代码语义理解。

## 📝 摘要（中文）

理解和推理代码语义对于提升代码大语言模型（LLMs）在实际软件工程任务中的能力至关重要。现有的代码推理基准大多依赖于合成数据集或教育编码问题，且主要关注粗粒度推理任务，如输入/输出预测，限制了其在实际软件工程背景下评估LLMs的有效性。为此，本文提出了CodeSense，这是第一个提供一系列与真实代码的软件工程相关的细粒度代码推理任务的基准。我们从真实的代码库中收集了Python、C和Java软件项目，执行测试并收集执行轨迹，构建了细粒度语义推理任务的真实数据集。综合评估显示，当前模型在处理细粒度推理任务时存在明显的性能差距，尽管链式思维和上下文学习等提示技术有所帮助，但LLMs在代码语义方面的缺乏根本限制了其推理能力。

## 🔬 方法详解

**问题定义**：本文旨在解决现有代码推理基准在真实软件工程任务中的不足，尤其是缺乏细粒度推理任务的评估。现有方法多依赖合成数据集，无法有效反映实际应用中的挑战。

**核心思路**：论文提出CodeSense基准，通过收集真实代码库中的项目，构建细粒度语义推理任务的数据集，旨在提升LLMs在实际软件工程中的推理能力。

**技术框架**：整体架构包括数据收集、执行测试、轨迹收集和数据集构建四个主要模块。首先从真实代码库中提取项目，然后执行相关测试以获取执行轨迹，最后构建出用于细粒度推理的真实数据集。

**关键创新**：最重要的创新点在于首次提供了针对真实世界代码的细粒度推理任务基准，填补了现有基准的空白，推动了LLMs在实际应用中的评估和改进。

**关键设计**：在数据集构建过程中，采用了多种编程语言（Python、C、Java），并设计了执行追踪框架和工具集，以便于收集真实的执行轨迹和构建高质量的基准数据集。实验中使用了多种提示技术来评估其对模型性能的影响。

## 📊 实验亮点

实验结果表明，当前的LLMs在细粒度推理任务上存在明显的性能差距，尽管采用了链式思维和上下文学习等提示技术，模型的表现仍然受到代码语义理解的限制。具体性能数据未提供，但结果显示了模型在处理复杂代码推理任务时的不足。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、代码审查和自动化测试等。通过提供真实世界的代码推理基准，CodeSense可以帮助开发者和研究者更好地评估和改进代码大语言模型的能力，推动智能编程助手的发展，提升软件工程的效率和质量。

## 📄 摘要（原文）

> Understanding and reasoning about code semantics is essential for enhancing code LLMs' abilities to solve real-world software engineering (SE) tasks. Although several code reasoning benchmarks exist, most rely on synthetic datasets or educational coding problems and focus on coarse-grained reasoning tasks such as input/output prediction, limiting their effectiveness in evaluating LLMs in practical SE contexts. To bridge this gap, we propose CodeSense, the first benchmark that makes available a spectrum of fine-grained code reasoning tasks concerned with the software engineering of real-world code. We collected Python, C and Java software projects from real-world repositories. We executed tests from these repositories, collected their execution traces, and constructed a ground truth dataset for fine-grained semantic reasoning tasks. We then performed comprehensive evaluations on state-of-the-art LLMs. Our results show a clear performance gap for the models to handle fine-grained reasoning tasks. Although prompting techniques such as chain-of-thought and in-context learning helped, the lack of code semantics in LLMs fundamentally limit models' capabilities of code reasoning. Besides dataset, benchmark and evaluation, our work produced an execution tracing framework and tool set that make it easy to collect ground truth for fine-grained SE reasoning tasks, offering a strong basis for future benchmark construction and model post training. Our code and data are located at https://codesense-bench.github.io/.

