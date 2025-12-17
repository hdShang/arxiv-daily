---
layout: default
title: Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis
---

# Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14157" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14157</a>
  <a href="https://arxiv.org/pdf/2512.14157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14157" onclick="toggleFavorite(this, '2512.14157', 'Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yankai Jiang, Yujie Zhang, Peng Zhang, Yichen Li, Jintai Chen, Xiaoming Shi, Shihui Zhen

**分类**: cs.AI, cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Ophiuchus：一种工具增强的医学图像分析框架，提升MLLM的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分析` `多模态大语言模型` `工具增强` `推理链` `强化学习`

## 📋 核心要点

1. 现有医学MLLM在复杂任务中，难以动态聚焦细粒度视觉区域，影响定位和诊断精度。
2. Ophiuchus框架通过工具增强，使MLLM具备判断、定位和融合视觉证据的能力，提升推理质量。
3. 三阶段训练策略，包括冷启动、自反思微调和强化学习，使模型能有效利用工具并模拟专家行为。

## 📝 摘要（中文）

本文提出了一种名为Ophiuchus的通用工具增强框架，旨在提升医学多模态大语言模型（MLLM）在复杂任务中的性能。现有方法难以动态地、迭代地聚焦于细粒度的视觉区域，从而影响精确的定位和诊断。Ophiuchus赋予MLLM以下能力：（i）判断何时需要额外的视觉证据；（ii）确定在医学图像中探测和定位的位置；（iii）将相关的子图像内容无缝地融入到交错的多模态思维链中。与受限于专用工具性能上限的先前方法不同，Ophiuchus将模型固有的定位和感知能力与外部工具集成，从而促进更高层次的推理。该方法的核心是三阶段训练策略：使用工具集成推理数据进行冷启动训练，以实现基本的工具选择和关键区域检查适应；自反思微调，以加强反思性推理并鼓励重新审视工具输出；以及Agentic工具强化学习，以直接优化特定于任务的奖励并模拟专家级诊断行为。大量实验表明，Ophiuchus在各种医学基准测试中始终优于闭源和开源的SOTA方法，包括VQA、检测和基于推理的分割。该方法为医学AI智能体开辟了一条新途径，使其能够通过工具集成推理真正地“用图像思考”。数据集、代码和训练模型将公开发布。

## 🔬 方法详解

**问题定义**：现有基于推理的医学多模态大语言模型（MLLM）在处理需要精细视觉区域关注的复杂任务时表现不佳。它们难以动态地、迭代地聚焦于图像的特定区域以进行精确的定位和诊断。现有方法往往受限于特定工具的性能，无法充分利用模型自身的感知和推理能力。

**核心思路**：Ophiuchus的核心思路是将MLLM固有的视觉感知和推理能力与外部工具相结合，形成一个工具增强的推理框架。通过让模型自主决定何时需要额外的视觉证据，并确定在图像中需要探测和定位的关键区域，Ophiuchus能够将相关的子图像信息无缝地融入到多模态的推理链中，从而提升模型的整体推理能力。

**技术框架**：Ophiuchus框架包含三个主要阶段：1) 冷启动训练：使用工具集成推理数据进行训练，使模型能够选择合适的工具并适应关键区域的检查。2) 自反思微调：通过让模型反思自身的推理过程和工具输出，加强反思性推理能力，并鼓励模型重新审视工具的输出结果。3) Agentic工具强化学习：通过直接优化特定任务的奖励，并模拟专家级的诊断行为，进一步提升模型的性能。

**关键创新**：Ophiuchus的关键创新在于其工具增强的推理框架和三阶段训练策略。与以往依赖于特定工具的方法不同，Ophiuchus将模型自身的感知和推理能力与外部工具相结合，从而突破了性能上限。三阶段训练策略则确保模型能够有效地利用工具，并逐步提升推理能力。

**关键设计**：Ophiuchus框架的具体技术细节包括：工具选择模块，用于判断何时需要使用外部工具；区域定位模块，用于确定在图像中需要探测的关键区域；多模态融合模块，用于将工具输出的视觉信息融入到推理链中。在训练过程中，使用了多种损失函数，包括工具选择损失、区域定位损失和推理损失。Agentic工具强化学习阶段，使用了特定于任务的奖励函数，以鼓励模型模拟专家级的诊断行为。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14157/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14157/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14157/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，Ophiuchus在VQA、检测和基于推理的分割等多个医学基准测试中，始终优于当前最先进的闭源和开源方法。具体性能提升数据在论文中给出，证明了Ophiuchus框架的有效性和优越性。该框架为医学AI智能体的发展提供了一条有前景的道路。

## 🎯 应用场景

Ophiuchus框架具有广泛的应用前景，可用于辅助医生进行医学图像分析、疾病诊断和治疗方案制定。该框架能够提升诊断的准确性和效率，减少误诊率，并为患者提供更个性化的医疗服务。未来，Ophiuchus有望成为医学AI领域的重要组成部分，推动医疗智能化发展。

## 📄 摘要（原文）

> Recent reasoning based medical MLLMs have made progress in generating step by step textual reasoning chains. However, they still struggle with complex tasks that necessitate dynamic and iterative focusing on fine-grained visual regions to achieve precise grounding and diagnosis. We introduce Ophiuchus, a versatile, tool-augmented framework that equips an MLLM to (i) decide when additional visual evidence is needed, (ii) determine where to probe and ground within the medical image, and (iii) seamlessly weave the relevant sub-image content back into an interleaved, multimodal chain of thought. In contrast to prior approaches limited by the performance ceiling of specialized tools, Ophiuchus integrates the model's inherent grounding and perception capabilities with external tools, thereby fostering higher-level reasoning. The core of our method is a three-stage training strategy: cold-start training with tool-integrated reasoning data to achieve basic tool selection and adaptation for inspecting key regions; self-reflection fine-tuning to strengthen reflective reasoning and encourage revisiting tool outputs; and Agentic Tool Reinforcement Learning to directly optimize task-specific rewards and emulate expert-like diagnostic behavior. Extensive experiments show that Ophiuchus consistently outperforms both closed-source and open-source SOTA methods across diverse medical benchmarks, including VQA, detection, and reasoning-based segmentation. Our approach illuminates a path toward medical AI agents that can genuinely "think with images" through tool-integrated reasoning. Datasets, codes, and trained models will be released publicly.

