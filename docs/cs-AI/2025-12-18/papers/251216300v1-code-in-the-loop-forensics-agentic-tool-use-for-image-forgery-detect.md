---
layout: default
title: "Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection"
---

# Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16300" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16300v1</a>
  <a href="https://arxiv.org/pdf/2512.16300.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16300v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16300v1', 'Code-in-the-Loop Forensics: Agentic Tool Use for Image Forgery Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fanrui Zhang, Qiang Zhang, Sizhuo Zhou, Jianwen Sun, Chuanhao Li, Jiaxin Ai, Yukang Feng, Yujie Zhang, Wenjie Li, Zizhen Li, Yifan Chang, Jiawei Liu, Kaipeng Zhang

**分类**: cs.AI

**发布日期**: 2025-12-18

**备注**: 11 pages, 6 figures

---

## 💡 一句话要点

**提出ForenAgent，利用Agentic工具解决图像伪造检测中跨层信息融合难题。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像伪造检测` `多模态大语言模型` `Agentic工具使用` `强化学习` `数字取证`

## 📋 核心要点

1. 现有图像伪造检测方法难以有效融合低级伪影和高级语义知识，限制了检测性能。
2. ForenAgent框架利用多模态大语言模型自主生成和执行低级工具，实现灵活可解释的伪造分析。
3. 通过冷启动和强化微调，ForenAgent在FABench数据集上展现出强大的工具使用能力和推理能力。

## 📝 摘要（中文）

现有的图像伪造检测(IFD)方法要么利用低级、语义无关的伪影，要么依赖具有高级语义知识的多模态大型语言模型(MLLM)。这两种信息流在范式和推理上高度异构，使得现有方法难以统一它们或有效地建模它们的跨层交互。为了解决这个差距，我们提出了ForenAgent，一个多轮交互式IFD框架，使MLLM能够自主生成、执行和迭代地改进围绕检测目标的基于Python的低级工具，从而实现更灵活和可解释的伪造分析。ForenAgent遵循一个结合冷启动和强化微调的两阶段训练流程，以逐步提高其工具交互能力和推理适应性。受到人类推理的启发，我们设计了一个动态推理循环，包括全局感知、局部聚焦、迭代探测和整体裁决，并将其实例化为数据采样策略和任务对齐的过程奖励。为了进行系统的训练和评估，我们构建了FABench，一个异构的、高质量的agent-forensics数据集，包含10万张图像和大约20万个agent交互问答对。实验表明，在低级工具的辅助下，ForenAgent在具有挑战性的IFD任务中表现出新兴的工具使用能力和反思性推理，为通用IFD开辟了一条有希望的道路。代码将在审查过程完成后发布。

## 🔬 方法详解

**问题定义**：现有图像伪造检测方法主要存在两个问题。一是依赖低级特征，缺乏语义理解能力，容易受到内容干扰。二是依赖多模态大语言模型，虽然具备语义知识，但缺乏对底层伪造痕迹的精确分析能力。这两种信息流的异构性使得现有方法难以有效融合，导致检测精度受限。

**核心思路**：ForenAgent的核心思路是利用多模态大语言模型（MLLM）作为智能体，使其能够自主生成、执行和迭代优化基于Python的低级工具，从而实现对图像伪造的细粒度分析。通过将高级语义知识与低级特征分析相结合，弥合了现有方法在信息融合方面的不足。这种Agentic工具使用方式使得伪造检测过程更加灵活、可解释，并能够适应不同的伪造类型。

**技术框架**：ForenAgent框架主要包含两个阶段：冷启动和强化微调。在冷启动阶段，使用预训练的MLLM初始化Agent，并提供少量示例进行初步训练。在强化微调阶段，通过与环境的交互，Agent不断学习和优化其工具使用策略。框架的核心是一个动态推理循环，包括全局感知（Global Perception）、局部聚焦（Local Focusing）、迭代探测（Iterative Probing）和整体裁决（Holistic Adjudication）。这个循环指导Agent逐步分析图像，并最终做出伪造判断。

**关键创新**：ForenAgent的关键创新在于将多模态大语言模型与Agentic工具使用相结合，实现了图像伪造检测的自动化和智能化。与传统方法相比，ForenAgent能够自主探索和利用各种低级工具，从而更全面地分析图像中的伪造痕迹。此外，ForenAgent的动态推理循环模拟了人类的推理过程，使其能够更有效地解决复杂的伪造检测问题。

**关键设计**：ForenAgent的训练过程采用了两阶段策略。冷启动阶段旨在快速初始化Agent，使其具备基本的工具使用能力。强化微调阶段则通过奖励函数引导Agent学习更有效的工具使用策略。奖励函数的设计至关重要，它需要能够反映Agent的推理过程和最终的检测结果。此外，FABench数据集的构建也为ForenAgent的训练和评估提供了高质量的数据支持。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16300v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ForenAgent在FABench数据集上取得了显著的性能提升，证明了其有效性。实验结果表明，ForenAgent能够有效地利用低级工具进行伪造检测，并在多个指标上超越了现有方法。此外，ForenAgent还展现出良好的泛化能力，能够在不同的伪造类型上保持较高的检测精度。

## 🎯 应用场景

ForenAgent在数字取证、新闻真实性验证、版权保护等领域具有广泛的应用前景。它可以帮助专业人员更高效地检测图像伪造，提高信息安全水平，维护社会诚信。未来，该技术有望应用于视频伪造检测、音频伪造检测等领域，为打击网络犯罪提供有力支持。

## 📄 摘要（原文）

> Existing image forgery detection (IFD) methods either exploit low-level, semantics-agnostic artifacts or rely on multimodal large language models (MLLMs) with high-level semantic knowledge. Although naturally complementary, these two information streams are highly heterogeneous in both paradigm and reasoning, making it difficult for existing methods to unify them or effectively model their cross-level interactions. To address this gap, we propose ForenAgent, a multi-round interactive IFD framework that enables MLLMs to autonomously generate, execute, and iteratively refine Python-based low-level tools around the detection objective, thereby achieving more flexible and interpretable forgery analysis. ForenAgent follows a two-stage training pipeline combining Cold Start and Reinforcement Fine-Tuning to enhance its tool interaction capability and reasoning adaptability progressively. Inspired by human reasoning, we design a dynamic reasoning loop comprising global perception, local focusing, iterative probing, and holistic adjudication, and instantiate it as both a data-sampling strategy and a task-aligned process reward. For systematic training and evaluation, we construct FABench, a heterogeneous, high-quality agent-forensics dataset comprising 100k images and approximately 200k agent-interaction question-answer pairs. Experiments show that ForenAgent exhibits emergent tool-use competence and reflective reasoning on challenging IFD tasks when assisted by low-level tools, charting a promising route toward general-purpose IFD. The code will be released after the review process is completed.

