---
layout: default
title: Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis
---

# Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14157" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14157v1</a>
  <a href="https://arxiv.org/pdf/2512.14157.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14157v1" onclick="toggleFavorite(this, '2512.14157v1', 'Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yankai Jiang, Yujie Zhang, Peng Zhang, Yichen Li, Jintai Chen, Xiaoming Shi, Shihui Zhen

**分类**: cs.AI, cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**Ophiuchus：一种工具增强的医学图像分析框架，提升MLLM的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学图像分析` `多模态大语言模型` `工具增强` `推理链` `强化学习` `自反思学习` `视觉定位`

## 📋 核心要点

1. 现有医学MLLM在复杂任务中，难以动态聚焦细粒度视觉区域，导致定位和诊断精度不足。
2. Ophiuchus框架通过工具增强，使MLLM具备自主决定何时、何地探测图像，并将信息融入推理链的能力。
3. Ophiuchus在VQA、检测和分割等医学基准测试中，显著超越了现有最优的闭源和开源方法。

## 📝 摘要（中文）

本文提出了一种名为Ophiuchus的通用工具增强框架，旨在提升医学多模态大语言模型（MLLM）在复杂任务中的性能。现有方法难以动态地、迭代地聚焦于细粒度的视觉区域，从而难以实现精确的定位和诊断。Ophiuchus赋予MLLM以下能力：（i）决定何时需要额外的视觉证据；（ii）确定在医学图像中何处进行探测和定位；（iii）无缝地将相关的子图像内容编织回交错的多模态思维链中。与受限于专用工具性能上限的先前方法不同，Ophiuchus将模型固有的定位和感知能力与外部工具集成，从而促进了更高层次的推理。该方法的核心是三阶段训练策略：使用工具集成推理数据进行冷启动训练，以实现基本的工具选择和关键区域检查适应；自反思微调，以加强反思性推理并鼓励重新审视工具输出；以及Agentic工具强化学习，以直接优化特定于任务的奖励并模拟专家级诊断行为。大量实验表明，Ophiuchus在各种医学基准测试中始终优于闭源和开源的SOTA方法，包括VQA、检测和基于推理的分割。该方法为医学AI智能体开辟了一条新途径，使其能够通过工具集成推理真正地“用图像思考”。数据集、代码和训练模型将公开发布。

## 🔬 方法详解

**问题定义**：现有基于推理的医学多模态大语言模型（MLLM）在处理复杂任务时，面临着难以动态和迭代地聚焦于细粒度视觉区域的挑战。这导致模型在精确的定位和诊断方面表现不佳。现有方法往往依赖于预定义的工具，限制了模型利用自身感知能力进行更高级推理的潜力。

**核心思路**：Ophiuchus的核心思路是将MLLM固有的定位和感知能力与外部工具相结合，从而实现更高级别的推理。通过赋予模型自主决定何时需要额外视觉证据、确定在图像中何处进行探测的能力，并无缝地将相关信息融入推理链中，Ophiuchus旨在克服现有方法的局限性。这种设计允许模型动态地调整其推理过程，并利用外部工具来增强其自身的感知能力。

**技术框架**：Ophiuchus框架包含三个主要的训练阶段：1) 冷启动训练：使用工具集成推理数据进行训练，使模型能够选择合适的工具并适应关键区域的检查。2) 自反思微调：通过强化反思性推理，鼓励模型重新审视工具的输出，从而提高推理的准确性。3) Agentic工具强化学习：直接优化特定于任务的奖励，并模拟专家级的诊断行为，进一步提升模型的性能。整个框架旨在创建一个能够自主进行工具选择和利用的智能体。

**关键创新**：Ophiuchus的关键创新在于其工具增强的推理框架，该框架允许MLLM动态地与外部工具交互，并将其输出集成到推理过程中。与现有方法不同，Ophiuchus强调模型自身的感知能力与外部工具的协同作用，从而实现了更高级别的推理。此外，三阶段训练策略也是一个重要的创新点，它逐步地提升了模型在工具选择、反思性推理和任务特定优化方面的能力。

**关键设计**：Ophiuchus框架的具体技术细节包括：工具集成推理数据的构建方式，自反思微调的具体实现方法（例如，使用的损失函数和训练策略），以及Agentic工具强化学习的奖励函数设计。此外，模型架构的选择和参数设置，以及如何将外部工具的输出无缝地集成到MLLM的推理链中，也是关键的设计考虑因素。具体的网络结构和损失函数等细节在论文中应该有更详细的描述（未知）。

## 📊 实验亮点

Ophiuchus在多个医学基准测试中取得了显著的性能提升，包括VQA、检测和基于推理的分割任务。实验结果表明，Ophiuchus始终优于现有的闭源和开源SOTA方法。具体的性能数据和提升幅度需要在论文中查找（未知），但摘要强调了其一致性的优越性，表明该方法具有较强的泛化能力。

## 🎯 应用场景

Ophiuchus框架在医学图像分析领域具有广泛的应用前景，例如辅助医生进行疾病诊断、病灶定位、治疗方案制定等。该框架可以应用于各种医学影像模态，如X光、CT、MRI等。通过提升MLLM的推理能力，Ophiuchus有望提高诊断的准确性和效率，减轻医生的工作负担，并最终改善患者的治疗效果。未来，该框架还可以扩展到其他需要精细视觉推理的领域，如遥感图像分析、工业质检等。

## 📄 摘要（原文）

> Recent reasoning based medical MLLMs have made progress in generating step by step textual reasoning chains. However, they still struggle with complex tasks that necessitate dynamic and iterative focusing on fine-grained visual regions to achieve precise grounding and diagnosis. We introduce Ophiuchus, a versatile, tool-augmented framework that equips an MLLM to (i) decide when additional visual evidence is needed, (ii) determine where to probe and ground within the medical image, and (iii) seamlessly weave the relevant sub-image content back into an interleaved, multimodal chain of thought. In contrast to prior approaches limited by the performance ceiling of specialized tools, Ophiuchus integrates the model's inherent grounding and perception capabilities with external tools, thereby fostering higher-level reasoning. The core of our method is a three-stage training strategy: cold-start training with tool-integrated reasoning data to achieve basic tool selection and adaptation for inspecting key regions; self-reflection fine-tuning to strengthen reflective reasoning and encourage revisiting tool outputs; and Agentic Tool Reinforcement Learning to directly optimize task-specific rewards and emulate expert-like diagnostic behavior. Extensive experiments show that Ophiuchus consistently outperforms both closed-source and open-source SOTA methods across diverse medical benchmarks, including VQA, detection, and reasoning-based segmentation. Our approach illuminates a path toward medical AI agents that can genuinely "think with images" through tool-integrated reasoning. Datasets, codes, and trained models will be released publicly.

