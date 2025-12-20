---
layout: default
title: Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning
---

# Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16698" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16698v1</a>
  <a href="https://arxiv.org/pdf/2512.16698.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16698v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16698v1', 'Do Multi-Agents Solve Better Than Single? Evaluating Agentic Frameworks for Diagram-Grounded Geometry Problem Solving and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahbub E Sobhani, Md. Faiyaz Abdullah Sayeedi, Mohammad Nehad Alam, Proma Hossain Progga, Swakkhar Shatabda

**分类**: cs.AI, cs.CG

**发布日期**: 2025-12-18

**备注**: Accepted to the ARR October 2025 cycle

**🔗 代码/项目**: [GITHUB](https://github.com/faiyazabdullah/Interpreter-Solver)

---

## 💡 一句话要点

**对比单智能体与多智能体框架，评估其在图解几何问题求解中的表现。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多智能体系统` `图解几何问题求解` `多模态大语言模型` `视觉推理` `智能体分解`

## 📋 核心要点

1. 现有的多模态大语言模型在图解几何问题求解中面临挑战，尤其是在复杂推理和视觉信息利用方面。
2. 论文对比单智能体和多智能体框架，探索智能体分解是否能有效提升模型在此任务上的性能。
3. 实验结果表明，多智能体框架对开源模型有显著提升，对闭源模型在新数据集上有一定帮助。

## 📝 摘要（中文）

图解几何问题求解是多模态大型语言模型（MLLM）的关键基准，但多智能体设计相对于单智能体的优势尚不明确。本文系统地比较了单智能体和多智能体流程在四个视觉数学基准（Geometry3K、MathVerse、OlympiadBench 和 We-Math）上的表现。对于开源模型，多智能体方法始终能提高性能。例如，Qwen-2.5-VL (7B) 在 Geometry3K 上获得了 +6.8 的提升，Qwen-2.5-VL (32B) 获得了 +3.3 的提升，并且两个 Qwen-2.5-VL 变体在 OlympiadBench 和 We-Math 上都获得了进一步的提升。相比之下，闭源模型 Gemini-2.0-Flash 在经典基准测试中通常在单智能体模式下表现更好，而多智能体仅在新数据集 We-Math 上产生了适度的改进。这些发现表明，多智能体流程为开源模型提供了明显的优势，并且可以帮助强大的专有系统处理更新、不太熟悉的基准，但智能体分解并非普遍最佳。

## 🔬 方法详解

**问题定义**：论文旨在研究在图解几何问题求解任务中，多智能体框架是否优于单智能体框架。现有的单智能体方法可能在处理复杂几何问题时，由于缺乏有效的分解和协同机制，导致推理能力不足，难以充分利用图中的视觉信息。

**核心思路**：论文的核心思路是通过将复杂的几何问题分解为多个子任务，并分配给不同的智能体协同完成，从而提高问题求解的效率和准确性。多智能体框架能够模拟人类解决复杂问题的过程，通过分工合作，更好地利用各种信息源。

**技术框架**：论文构建了单智能体和多智能体两种流程。单智能体流程直接使用MLLM对问题进行求解。多智能体流程则包含问题分解、子任务分配、智能体执行和结果整合等阶段。具体来说，可能包括一个负责理解问题和图表的智能体，一个负责进行几何推理的智能体，以及一个负责生成最终答案的智能体。

**关键创新**：论文的关键创新在于系统性地对比了单智能体和多智能体框架在图解几何问题求解任务中的性能差异，并针对不同类型的模型（开源和闭源）进行了深入分析。此外，论文还探讨了多智能体框架在处理不同难度和类型的几何问题时的表现。

**关键设计**：论文可能采用了特定的智能体间通信机制，例如消息传递或共享知识库，以实现智能体之间的协同。此外，论文可能还设计了特定的损失函数或奖励机制，以鼓励智能体更好地完成子任务并提高整体性能。具体的参数设置和网络结构取决于所使用的MLLM和智能体架构，论文中应该有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16698v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16698v1/figures/diagram.png" alt="fig_1" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，对于开源模型，多智能体框架在Geometry3K、OlympiadBench和We-Math等基准测试中均能显著提升性能。例如，Qwen-2.5-VL (7B) 在 Geometry3K 上获得了 +6.8 的提升。然而，对于闭源模型 Gemini-2.0-Flash，单智能体模式在经典基准上表现更好，多智能体仅在We-Math数据集上略有提升。

## 🎯 应用场景

该研究成果可应用于教育领域，例如开发智能几何辅导系统，帮助学生理解和解决几何问题。此外，该研究对于提升多模态大语言模型在复杂推理和视觉理解任务中的能力具有重要意义，可应用于机器人导航、图像识别等领域。

## 📄 摘要（原文）

> Diagram-grounded geometry problem solving is a critical benchmark for multimodal large language models (MLLMs), yet the benefits of multi-agent design over single-agent remain unclear. We systematically compare single-agent and multi-agent pipelines on four visual math benchmarks: Geometry3K, MathVerse, OlympiadBench, and We-Math. For open-source models, multi-agent consistently improves performance. For example, Qwen-2.5-VL (7B) gains +6.8 points and Qwen-2.5-VL (32B) gains +3.3 on Geometry3K, and both Qwen-2.5-VL variants see further gains on OlympiadBench and We-Math. In contrast, the closed-source Gemini-2.0-Flash generally performs better in single-agent mode on classic benchmarks, while multi-agent yields only modest improvements on the newer We-Math dataset. These findings show that multi-agent pipelines provide clear benefits for open-source models and can assist strong proprietary systems on newer, less familiar benchmarks, but agentic decomposition is not universally optimal. All code, data, and reasoning files are available at https://github.com/faiyazabdullah/Interpreter-Solver

