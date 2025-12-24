---
layout: default
title: Cube Bench: A Benchmark for Spatial Visual Reasoning in MLLMs
---

# Cube Bench: A Benchmark for Spatial Visual Reasoning in MLLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20595" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20595v1</a>
  <a href="https://arxiv.org/pdf/2512.20595.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20595v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20595v1', 'Cube Bench: A Benchmark for Spatial Visual Reasoning in MLLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dhruv Anand, Ehsan Shareghi

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-12-23

**备注**: 27 pages, 5 figures, 9 tables. Cube available at https://github.com/dana-23/cube-bench

---

## 💡 一句话要点

**提出Cube Bench：用于评估多模态大语言模型空间视觉推理能力的魔方基准测试。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `空间推理` `视觉推理` `魔方` `基准测试`

## 📋 核心要点

1. 现有的多模态大语言模型在空间和序列推理方面存在不足，尤其是在复杂任务中。
2. Cube Bench通过魔方任务，将空间推理分解为面重建、动作选择、结果预测、多步执行和错误纠正五个技能。
3. 实验表明，模型性能随魔方复杂度急剧下降，且闭源模型优于开源模型，自我纠正策略效果有限。

## 📝 摘要（中文）

本文提出了Cube Bench，一个用于评估多模态大语言模型（MLLM）在空间和序列推理能力的魔方基准测试。该基准将性能分解为五个技能：（i）从图像和文本重建魔方的面，（ii）选择最佳的下一步动作，（iii）在不应用候选动作的情况下预测其结果，（iv）执行多步计划并在错误中恢复，以及（v）检测和修改自己的错误。使用一组共享的打乱魔方状态、相同的提示和解析器以及单一的距离解决度量，本文比较了七个MLLM在不同打乱深度下的性能。结果表明，准确率随着深度急剧下降；一旦轨迹停滞或发散，模型很少恢复，并且高的面重建准确率并不能保证有效的动作选择或多步执行。闭源模型和开源模型之间存在明显的差距：最强的闭源模型在单步感知任务和多步控制任务中都处于领先地位，而开源模型在最困难的设置中接近随机水平；然而，即使是最好的MLLM也会在更高的魔方复杂度下性能下降。通过反思性思维进行简单的自我纠正可以产生适度的收益，但也可能导致过度思考。Cube Bench 为 MLLM 中的序列空间推理提供了一个紧凑、可复现的探针。

## 🔬 方法详解

**问题定义**：论文旨在评估多模态大语言模型（MLLM）在空间和序列推理方面的能力，特别是在解决魔方这类复杂任务中的表现。现有方法缺乏一个专门针对空间推理的基准测试，难以系统性地评估和比较不同MLLM的性能。此外，现有方法难以深入分析模型在解决复杂问题时的具体瓶颈，例如感知、决策和执行等环节的错误。

**核心思路**：论文的核心思路是利用魔方作为评估MLLM空间推理能力的代理任务。魔方具有明确的状态空间和动作空间，可以通过一系列操作来改变其状态。通过设计不同的魔方任务，可以考察MLLM在感知、推理、规划和执行等方面的能力。此外，论文还设计了统一的评估指标和实验流程，以便公平地比较不同MLLM的性能。

**技术框架**：Cube Bench的整体框架包括以下几个主要模块：
1. **魔方状态表示**：使用图像和文本两种方式来表示魔方的状态。
2. **任务设计**：设计了五个不同的魔方任务，分别考察MLLM的面重建、动作选择、结果预测、多步执行和错误纠正能力。
3. **提示工程**：设计了一致的提示模板，用于引导MLLM完成不同的任务。
4. **评估指标**：使用距离解决度量（distance-to-solved metric）来评估MLLM的性能。
5. **实验流程**：使用一组共享的打乱魔方状态、相同的提示和解析器，对不同的MLLM进行评估。

**关键创新**：Cube Bench的关键创新在于：
1. **魔方任务的分解**：将魔方任务分解为五个不同的技能，可以更细粒度地评估MLLM的空间推理能力。
2. **统一的评估框架**：提供了一个统一的评估框架，可以公平地比较不同MLLM的性能。
3. **错误分析**：可以分析MLLM在解决魔方任务时的具体错误，例如感知错误、决策错误和执行错误。

**关键设计**：
* **提示模板**：论文使用了精心设计的提示模板，以确保MLLM能够理解任务要求并生成有效的输出。
* **距离解决度量**：使用距离解决度量来评估MLLM的性能，该指标可以反映MLLM距离解决魔方的程度。
* **自我纠正机制**：论文尝试使用反思性思维进行自我纠正，但效果有限，表明MLLM在复杂任务中的自我纠正能力仍有待提高。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20595v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20595v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20595v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，MLLM在Cube Bench上的性能随着魔方复杂度的增加而急剧下降。闭源模型（如GPT-4V）在单步感知和多步控制任务中优于开源模型，但即使是最强的模型在更高复杂度下也会退化。简单的自我纠正策略虽然能带来一些提升，但效果有限。开源模型在最困难的设置中接近随机水平。

## 🎯 应用场景

Cube Bench为评估和提升多模态大语言模型的空间视觉推理能力提供了一个有价值的工具。该基准测试可以应用于机器人导航、自动驾驶、游戏AI等领域，帮助开发更智能、更可靠的AI系统。未来，可以扩展Cube Bench，增加任务的复杂性和多样性，以更好地评估MLLM的泛化能力。

## 📄 摘要（原文）

> We introduce Cube Bench, a Rubik's-cube benchmark for evaluating spatial and sequential reasoning in multimodal large language models (MLLMs). The benchmark decomposes performance into five skills: (i) reconstructing cube faces from images and text, (ii) choosing the optimal next move, (iii) predicting the outcome of a candidate move without applying it, (iv) executing multi-step plans while recovering from mistakes, and (v) detecting and revising one's own errors. Using a shared set of scrambled cube states, identical prompts and parsers, and a single distance-to-solved metric, we compare recent MLLMs side by side as a function of scramble depth. Across seven MLLMs, accuracy drops sharply with depth; once a trajectory stalls or diverges, models rarely recover, and high face-reconstruction accuracy does not guarantee competent action selection or multi-step execution. A pronounced closed- vs open-source gap emerges: the strongest closed model leads on both single-step perception tasks and multi-step control tasks, while open-weight models cluster near chance on the hardest settings; yet even the best MLLM degrades at higher cube complexity. A simple self-correction via reflective thinking yields modest gains but can also introduce overthinking. Cube Bench offers a compact, reproducible probe of sequential spatial reasoning in MLLMs.

