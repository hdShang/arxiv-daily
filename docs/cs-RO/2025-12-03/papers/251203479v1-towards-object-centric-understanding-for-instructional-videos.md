---
layout: default
title: Towards Object-centric Understanding for Instructional Videos
---

# Towards Object-centric Understanding for Instructional Videos

**arXiv**: [2512.03479v1](https://arxiv.org/abs/2512.03479) | [PDF](https://arxiv.org/pdf/2512.03479.pdf)

**作者**: Wenliang Guo, Yu Kong

---

## 💡 一句话要点

**提出对象中心范式与Object-IVQA基准，以提升教学视频中基于对象状态的理解能力。**

**关键词**: `教学视频理解` `对象中心推理` `长视频基准` `状态转换` `多跳推理` `开放问答`

## 📋 核心要点

1. 核心问题：现有动作中心方法难以处理真实教学视频中步骤顺序随对象状态变化的灵活性。
2. 方法要点：将动作视为驱动状态转换的机制，并引入对象中心规划、感知、分析和生成工具框架。
3. 实验或效果：在Object-IVQA基准上，现有大视觉语言模型表现不佳，而所提框架显著提升对象级识别与推理能力。

## 📄 摘要（原文）

> Understanding procedural activities is crucial for developing future assistive AI that can reason about complex real-world tasks. Existing action-centric methods struggle with the flexibility of real procedures, where step order varies depending on object states. In this work, we propose to shift the focus to an object-centric paradigm by regarding actions as mechanisms that drive state transitions. To advance this direction, we introduce Object-IVQA, a long-form instructional video benchmark with 107 videos and 514 open-ended question-answer pairs annotated with temporally grounded evidence. The benchmark evaluates four dimensions of object-centric reasoning, including state evolution, precondition verification, counterfactual reasoning and mistake recognition. We further propose an agent framework that orchestrates object-centric planning, perception, analysis and generation tools, enabling explicit evidence retrieval and multi-hop reasoning across disjoint segments. Experiments show that existing large vision-language models struggle in object-level recognition and reasoning, whereas our framework achieves substantially improvement.

