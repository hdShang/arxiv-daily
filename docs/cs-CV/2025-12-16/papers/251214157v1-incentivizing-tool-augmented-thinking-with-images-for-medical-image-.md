---
layout: default
title: Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis
---

# Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis

**arXiv**: [2512.14157v1](https://arxiv.org/abs/2512.14157) | [PDF](https://arxiv.org/pdf/2512.14157.pdf)

**作者**: Yankai Jiang, Yujie Zhang, Peng Zhang, Yichen Li, Jintai Chen, Xiaoming Shi, Shihui Zhen

**分类**: cs.AI, cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Ophiuchus框架，通过工具增强的思维链解决医学图像分析中复杂任务的动态视觉聚焦问题。**

**关键词**: `医学图像分析` `多模态大语言模型` `工具增强推理` `动态视觉聚焦` `三阶段训练策略` `代理强化学习` `医学AI代理`

## 📋 核心要点

1. 现有医学MLLM在复杂任务中难以动态聚焦细粒度视觉区域，导致定位和诊断精度不足。
2. Ophiuchus框架通过工具增强思维链，集成模型能力与外部工具，实现动态视觉证据获取和推理。
3. 实验显示Ophiuchus在VQA、检测和分割等医学基准上超越SOTA方法，验证了其有效性。

## 📝 摘要（中文）

近年来，基于推理的医学多模态大语言模型在生成逐步文本推理链方面取得了进展。然而，它们仍然难以处理需要动态、迭代地关注细粒度视觉区域以实现精确定位和诊断的复杂任务。我们引入了Ophiuchus，这是一个多功能、工具增强的框架，它使MLLM能够：(i)决定何时需要额外的视觉证据，(ii)确定在医学图像中探测和定位的位置，以及(iii)将相关的子图像内容无缝地编织成交错的多模态思维链。与先前受限于专用工具性能上限的方法不同，Ophiuchus将模型固有的定位和感知能力与外部工具相结合，从而促进更高层次的推理。我们方法的核心是一个三阶段训练策略：使用工具集成推理数据进行冷启动训练，以实现对关键区域检查的基本工具选择和适应；自我反思微调，以加强反思性推理并鼓励重新审视工具输出；以及代理工具强化学习，以直接优化特定任务的奖励并模拟类似专家的诊断行为。大量实验表明，Ophiuchus在包括VQA、检测和基于推理的分割在内的多种医学基准测试中，始终优于闭源和开源的最先进方法。我们的方法为医学AI代理指明了一条路径，使其能够通过工具集成推理真正“用图像思考”。数据集、代码和训练模型将公开发布。

## 🔬 方法详解

Ophiuchus是一个工具增强的多模态框架，核心创新在于三阶段训练策略：冷启动训练使用工具集成数据，使模型学会选择和适应工具以检查关键区域；自我反思微调强化反思推理，鼓励模型重新评估工具输出；代理工具强化学习直接优化任务奖励，模拟专家诊断行为。与现有方法相比，它突破了专用工具的性能限制，通过结合模型内在能力与外部工具，实现了更高级的推理和动态视觉聚焦。

## 📊 实验亮点

Ophiuchus在多种医学基准测试中一致优于闭源和开源SOTA方法，包括VQA、检测和基于推理的分割，展示了其在动态视觉聚焦和推理方面的显著性能提升。

## 🎯 应用场景

该研究可应用于医学图像分析领域，如辅助诊断、病灶检测和分割，提升AI在复杂医疗任务中的精确性和可靠性，推动智能医疗代理的发展。

## 📄 摘要（原文）

> Recent reasoning based medical MLLMs have made progress in generating step by step textual reasoning chains. However, they still struggle with complex tasks that necessitate dynamic and iterative focusing on fine-grained visual regions to achieve precise grounding and diagnosis. We introduce Ophiuchus, a versatile, tool-augmented framework that equips an MLLM to (i) decide when additional visual evidence is needed, (ii) determine where to probe and ground within the medical image, and (iii) seamlessly weave the relevant sub-image content back into an interleaved, multimodal chain of thought. In contrast to prior approaches limited by the performance ceiling of specialized tools, Ophiuchus integrates the model's inherent grounding and perception capabilities with external tools, thereby fostering higher-level reasoning. The core of our method is a three-stage training strategy: cold-start training with tool-integrated reasoning data to achieve basic tool selection and adaptation for inspecting key regions; self-reflection fine-tuning to strengthen reflective reasoning and encourage revisiting tool outputs; and Agentic Tool Reinforcement Learning to directly optimize task-specific rewards and emulate expert-like diagnostic behavior. Extensive experiments show that Ophiuchus consistently outperforms both closed-source and open-source SOTA methods across diverse medical benchmarks, including VQA, detection, and reasoning-based segmentation. Our approach illuminates a path toward medical AI agents that can genuinely "think with images" through tool-integrated reasoning. Datasets, codes, and trained models will be released publicly.

