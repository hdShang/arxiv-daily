---
layout: default
title: SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models
---

# SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08559" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08559v1</a>
  <a href="https://arxiv.org/pdf/2510.08559.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08559v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08559v1', 'SciVideoBench: Benchmarking Scientific Video Reasoning in Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andong Deng, Taojiannan Yang, Shoubin Yu, Lincoln Spencer, Mohit Bansal, Chen Chen, Serena Yeung-Levy, Xiaohan Wang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**SciVideoBench：提出科学视频推理基准，评估大型多模态模型在科学领域的认知能力。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `科学视频推理` `大型多模态模型` `基准数据集` `认知能力评估` `领域知识` `时空感知` `逻辑推理`

## 📋 核心要点

1. 现有视频基准侧重通用场景，推理任务简单，无法有效评估多模态模型在科学领域的认知能力。
2. SciVideoBench通过构建科学实验视频推理数据集，包含领域知识、时空感知和逻辑推理等多重挑战。
3. 实验结果表明，现有LMMs在SciVideoBench上表现不佳，揭示了科学视频推理能力的巨大提升空间。

## 📝 摘要（中文）

大型多模态模型(LMMs)在各种能力上取得了显著进展；然而，科学领域中复杂的视频推理仍然是一个重要且具有挑战性的前沿。当前的视频基准主要针对通用场景，这些场景严重依赖感知/识别，而推理任务相对简单，导致饱和，因此无法有效评估高级多模态认知技能。为了解决这个关键差距，我们引入了SciVideoBench，这是一个专门设计的严格基准，用于评估科学背景下的高级视频推理。SciVideoBench包含1000个精心设计的选择题，这些问题源于涵盖超过25个专业学术科目的前沿科学实验视频，并由半自动系统验证。每个问题都需要复杂的领域特定知识、精确的时空感知和复杂的逻辑推理，有效地挑战了模型的高阶认知能力。我们的评估突出了最先进的专有和开源LMM（包括Gemini 2.5 Pro和Qwen2.5-VL）的显著性能缺陷，表明视频推理能力有很大的提升空间。对推理复杂性和视觉基础等关键因素的详细分析为LMM的未来发展提供了宝贵的见解和明确的方向，推动了真正有能力的多模态AI共同科学家的发展。我们希望SciVideoBench能够符合社区的兴趣，并帮助推动前沿AI在边界科学中的发展。

## 🔬 方法详解

**问题定义**：现有视频基准数据集主要集中在通用场景，依赖于感知和识别，推理难度较低，无法有效评估LMMs在科学领域的复杂推理能力。因此，需要一个更具挑战性的基准来推动LMMs在科学领域的应用。

**核心思路**：构建一个高质量的科学视频推理数据集，该数据集需要涵盖多个科学领域，并包含需要领域知识、时空感知和逻辑推理才能解决的问题。通过在该数据集上评估LMMs的性能，可以更准确地了解LMMs在科学领域的推理能力，并为未来的研究提供指导。

**技术框架**：SciVideoBench数据集的构建流程包括以下几个阶段：1) 从科学实验视频中提取关键帧和视频片段；2) 设计需要领域知识、时空感知和逻辑推理才能解决的多选题；3) 使用半自动系统验证问题的正确性和难度；4) 对数据集进行清洗和标注。

**关键创新**：SciVideoBench的关键创新在于其专注于科学视频推理，并设计了需要复杂认知能力才能解决的问题。与现有视频基准相比，SciVideoBench更具挑战性，可以更有效地评估LMMs在科学领域的推理能力。

**关键设计**：SciVideoBench包含1000个选择题，涵盖超过25个专业学术科目。每个问题都经过精心设计，需要模型具备领域特定知识、精确的时空感知和复杂的逻辑推理能力。数据集还提供了详细的标注信息，包括问题的类型、难度和答案的解释。

## 📊 实验亮点

在SciVideoBench上的实验结果表明，包括Gemini 2.5 Pro和Qwen2.5-VL在内的最先进LMMs表现出显著的性能缺陷，表明在科学视频推理方面仍有很大的改进空间。详细的分析揭示了推理复杂性和视觉基础等关键因素对性能的影响。

## 🎯 应用场景

SciVideoBench可用于评估和提升LMMs在科学领域的应用能力，例如辅助科研人员进行实验设计、数据分析和结果解释。未来，更强大的LMMs有望成为AI Co-scientist，加速科学发现的进程。

## 📄 摘要（原文）

> Large Multimodal Models (LMMs) have achieved remarkable progress across various capabilities; however, complex video reasoning in the scientific domain remains a significant and challenging frontier. Current video benchmarks predominantly target general scenarios where perception/recognition is heavily relied on, while with relatively simple reasoning tasks, leading to saturation and thus failing to effectively evaluate advanced multimodal cognitive skills. To address this critical gap, we introduce SciVideoBench, a rigorous benchmark specifically designed to assess advanced video reasoning in scientific contexts. SciVideoBench consists of 1,000 carefully crafted multiple-choice questions derived from cutting-edge scientific experimental videos spanning over 25 specialized academic subjects and verified by a semi-automatic system. Each question demands sophisticated domain-specific knowledge, precise spatiotemporal perception, and intricate logical reasoning, effectively challenging models' higher-order cognitive abilities. Our evaluation highlights significant performance deficits in state-of-the-art proprietary and open-source LMMs, including Gemini 2.5 Pro and Qwen2.5-VL, indicating substantial room for advancement in video reasoning capabilities. Detailed analyses of critical factors such as reasoning complexity and visual grounding provide valuable insights and clear direction for future developments in LMMs, driving the evolution of truly capable multimodal AI co-scientists. We hope SciVideoBench could fit the interests of the community and help to push the boundary of cutting-edge AI for border science.

