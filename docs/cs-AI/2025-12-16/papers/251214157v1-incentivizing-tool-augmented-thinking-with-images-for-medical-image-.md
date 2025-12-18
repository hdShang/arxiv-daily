---
layout: default
title: Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis
---

# Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14157" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14157v1</a>
  <a href="https://arxiv.org/pdf/2512.14157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14157v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14157v1', 'Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yankai Jiang, Yujie Zhang, Peng Zhang, Yichen Li, Jintai Chen, Xiaoming Shi, Shihui Zhen

**分类**: cs.AI, cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**Ophiuchus：一种工具增强的医学图像分析框架，提升MLLM的细粒度推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分析` `多模态大语言模型` `工具增强` `推理链` `强化学习` `自反思学习` `智能医疗`

## 📋 核心要点

1. 现有医学MLLM在复杂任务中，难以动态聚焦细粒度视觉区域，影响了精确定位和诊断。
2. Ophiuchus框架通过工具增强，使MLLM能够自主决定何时、何地探测图像，并将信息融入推理链。
3. Ophiuchus在VQA、检测和分割等医学基准测试中，显著优于现有SOTA方法，展现了强大的性能。

## 📝 摘要（中文）

本文提出了一种名为Ophiuchus的通用工具增强框架，旨在提升医学多模态大语言模型（MLLM）在复杂任务中的性能。现有方法难以动态、迭代地聚焦于细粒度的视觉区域，从而影响精确的定位和诊断。Ophiuchus赋予MLLM以下能力：（i）判断何时需要额外的视觉证据；（ii）确定在医学图像中探测和定位的位置；（iii）无缝地将相关的子图像内容融入到交错的多模态推理链中。与受限于专用工具性能上限的先前方法不同，Ophiuchus将模型固有的定位和感知能力与外部工具集成，从而促进更高层次的推理。该方法的核心是三阶段训练策略：使用工具集成推理数据进行冷启动训练，以实现基本的工具选择和关键区域检查适应；自反思微调，以加强反思性推理并鼓励重新审视工具输出；以及Agentic工具强化学习，以直接优化特定于任务的奖励并模拟专家级诊断行为。大量实验表明，Ophiuchus在各种医学基准测试中始终优于闭源和开源的SOTA方法，包括VQA、检测和基于推理的分割。该方法为医学AI智能体开辟了一条新途径，使其能够通过工具集成推理真正地“用图像思考”。数据集、代码和训练模型将公开发布。

## 🔬 方法详解

**问题定义**：现有基于推理的医学多模态大语言模型（MLLM）在处理需要精确定位和诊断的复杂任务时，面临着挑战。这些模型难以动态且迭代地聚焦于细粒度的视觉区域，导致无法充分利用图像中的关键信息。现有方法通常依赖于预定义的工具或模块，其性能上限受限于这些工具的能力，无法充分发挥MLLM自身的感知和推理潜力。

**核心思路**：Ophiuchus的核心思路是将MLLM固有的感知和推理能力与外部工具相结合，构建一个能够自主决定何时、何地使用工具来增强视觉理解的框架。通过这种方式，模型可以动态地探索图像，提取相关的子图像内容，并将其无缝地融入到多模态推理链中，从而实现更高层次的推理。这种设计旨在克服现有方法中工具性能的限制，充分发挥MLLM的潜力。

**技术框架**：Ophiuchus框架包含三个主要的训练阶段：1) 冷启动训练：使用工具集成推理数据，使模型学习基本的工具选择和关键区域检查适应能力。2) 自反思微调：通过强化反思性推理，鼓励模型重新审视工具输出，提高推理的准确性。3) Agentic工具强化学习：直接优化特定于任务的奖励，使模型能够模拟专家级的诊断行为。整个框架通过这三个阶段的训练，逐步提升模型在医学图像分析任务中的性能。

**关键创新**：Ophiuchus的关键创新在于其工具增强的推理框架，该框架允许MLLM自主地决定何时以及如何使用外部工具来增强其视觉理解。与现有方法不同，Ophiuchus不是简单地将工具作为预定义的模块集成到模型中，而是将工具视为一种可以动态调用的资源，从而使模型能够更灵活地适应不同的任务和场景。此外，三阶段训练策略也是一个重要的创新点，它能够逐步提升模型在工具使用、推理和诊断方面的能力。

**关键设计**：在冷启动训练阶段，使用了大量的工具集成推理数据，这些数据包含了图像、问题、工具选择和推理步骤等信息。在自反思微调阶段，设计了特定的损失函数来鼓励模型进行反思性推理。在Agentic工具强化学习阶段，定义了特定于任务的奖励函数，以引导模型学习专家级的诊断行为。具体的网络结构和参数设置在论文中进行了详细描述，但摘要中未提供具体数值。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14157v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14157v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14157v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

Ophiuchus在多个医学基准测试中取得了显著的性能提升，包括VQA、检测和基于推理的分割任务。实验结果表明，Ophiuchus始终优于闭源和开源的SOTA方法，证明了其有效性和优越性。具体的性能数据和提升幅度将在论文中详细展示。

## 🎯 应用场景

Ophiuchus框架具有广泛的应用前景，可用于辅助医生进行疾病诊断、病灶检测、影像报告生成等任务。该研究有望提升医学影像分析的效率和准确性，降低误诊率，并为远程医疗和智能化医疗提供技术支持。未来，该框架可以扩展到其他医学影像模态，如CT、MRI等，并与其他医疗AI技术相结合，构建更强大的智能医疗系统。

## 📄 摘要（原文）

> Recent reasoning based medical MLLMs have made progress in generating step by step textual reasoning chains. However, they still struggle with complex tasks that necessitate dynamic and iterative focusing on fine-grained visual regions to achieve precise grounding and diagnosis. We introduce Ophiuchus, a versatile, tool-augmented framework that equips an MLLM to (i) decide when additional visual evidence is needed, (ii) determine where to probe and ground within the medical image, and (iii) seamlessly weave the relevant sub-image content back into an interleaved, multimodal chain of thought. In contrast to prior approaches limited by the performance ceiling of specialized tools, Ophiuchus integrates the model's inherent grounding and perception capabilities with external tools, thereby fostering higher-level reasoning. The core of our method is a three-stage training strategy: cold-start training with tool-integrated reasoning data to achieve basic tool selection and adaptation for inspecting key regions; self-reflection fine-tuning to strengthen reflective reasoning and encourage revisiting tool outputs; and Agentic Tool Reinforcement Learning to directly optimize task-specific rewards and emulate expert-like diagnostic behavior. Extensive experiments show that Ophiuchus consistently outperforms both closed-source and open-source SOTA methods across diverse medical benchmarks, including VQA, detection, and reasoning-based segmentation. Our approach illuminates a path toward medical AI agents that can genuinely "think with images" through tool-integrated reasoning. Datasets, codes, and trained models will be released publicly.

