---
layout: default
title: EmoCaliber: Advancing Reliable Visual Emotion Comprehension via Confidence Verbalization and Calibration
---

# EmoCaliber: Advancing Reliable Visual Emotion Comprehension via Confidence Verbalization and Calibration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15528" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15528v1</a>
  <a href="https://arxiv.org/pdf/2512.15528.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15528v1" onclick="toggleFavorite(this, '2512.15528v1', 'EmoCaliber: Advancing Reliable Visual Emotion Comprehension via Confidence Verbalization and Calibration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daiqing Wu, Dongbao Yang, Can Ma. Yu Zhou

**分类**: cs.CV

**发布日期**: 2025-12-17

**🔗 代码/项目**: [GITHUB](https://github.com/wdqqdw/EmoCaliber)

---

## 💡 一句话要点

**EmoCaliber：通过置信度表达与校准，提升视觉情感理解的可靠性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉情感理解` `多模态大语言模型` `置信度估计` `置信度校准` `情感分析` `人机交互` `VECBench`

## 📋 核心要点

1. 现有VEC方法通常将情感理解视为确定性任务，忽略了情感感知的主观性和多种合理的情感解释。
2. EmoCaliber的核心在于赋予MLLM表达情感预测置信度的能力，从而提供对模型能力和替代解释的估计。
3. EmoCaliber在VECBench上取得了优异的性能，验证了其在情感预测和置信度估计方面的有效性。

## 📝 摘要（中文）

视觉情感理解(VEC)旨在从图像中蕴含的情感线索推断情感极性或类别。近年来，多模态大型语言模型(MLLM)已成为VEC领域的热门范式，利用其泛化能力统一不同情感分类体系下的VEC任务。然而，这种范式通常将VEC视为确定性任务，要求模型为每张图像输出一个明确的情感标签。这种方式未能充分考虑情感感知的主观性，忽略了不同观看者可能存在的其他合理解释。为了解决这一局限性，我们提出赋予MLLM表达情感预测置信度的能力。这种附加信号为用户提供了对替代解释合理性和MLLM自身能力的估计，从而提高了实际应用中的可靠性。基于此，我们引入了一个三阶段训练框架，逐步赋予模型结构化推理能力，教会模型表达置信度，并校准置信度表达，最终得到EmoCaliber，一个用于VEC的置信度感知MLLM。通过在统一基准VECBench上的公平和全面评估，EmoCaliber在情感预测和置信度估计方面均优于现有方法。这些结果验证了我们方法的有效性，并标志着朝着更可靠的VEC系统迈出了可行的一步。

## 🔬 方法详解

**问题定义**：视觉情感理解（VEC）旨在从图像中推断情感。现有方法，特别是基于多模态大型语言模型（MLLM）的方法，通常将VEC视为一个确定性任务，即为每个图像输出一个单一的情感标签。这种方法忽略了情感感知的主观性，以及不同人对同一图像可能存在多种合理情感解释的情况。因此，现有方法的痛点在于缺乏对模型预测不确定性的建模和表达，导致可靠性不足。

**核心思路**：EmoCaliber的核心思路是让MLLM能够表达其对情感预测的置信度。通过让模型输出置信度信息，用户可以更好地理解模型预测的可靠性，并考虑其他可能的情感解释。这种设计旨在解决VEC任务中情感主观性和不确定性的问题，提高VEC系统的实用性和可靠性。

**技术框架**：EmoCaliber采用一个三阶段训练框架：
1. **结构化推理**：赋予模型进行结构化推理的能力，理解情感的复杂性。
2. **置信度表达**：训练模型 verbalize 其对情感预测的置信度，例如使用自然语言描述。
3. **置信度校准**：校准模型的置信度表达，使其与实际预测准确率相匹配。

**关键创新**：EmoCaliber的关键创新在于：
1. **置信度 verbalization**：让MLLM能够以自然语言表达其对情感预测的置信度，这与传统的输出单一标签的方法不同。
2. **三阶段训练框架**：该框架逐步赋予模型结构化推理、置信度表达和校准能力，确保模型能够准确地表达其预测的不确定性。
3. **置信度校准**：通过校准，模型的置信度表达能够更准确地反映其预测的可靠性。

**关键设计**：论文中没有详细说明具体的参数设置、损失函数、网络结构等技术细节。但是，三阶段训练框架是关键设计，每个阶段都针对特定的目标进行优化。置信度校准阶段可能涉及到使用校准损失函数，例如温度缩放或直方图均衡化等方法，以确保模型的置信度表达与实际预测准确率相匹配。具体实现细节需要在论文的补充材料或代码中查找。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15528v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15528v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15528v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

EmoCaliber在VECBench基准测试中取得了显著的性能提升，在情感预测和置信度估计方面均优于现有方法。具体性能数据需要在论文中查找。实验结果验证了EmoCaliber三阶段训练框架的有效性，以及置信度表达和校准对提高VEC系统可靠性的重要作用。项目代码已开源，方便研究人员复现和进一步研究。

## 🎯 应用场景

EmoCaliber在情感分析、人机交互、心理健康评估等领域具有广泛的应用前景。例如，在社交媒体情感分析中，EmoCaliber可以提供更可靠的情感判断，帮助识别网络欺凌和仇恨言论。在人机交互中，EmoCaliber可以使机器更好地理解人类情感，从而提供更自然和个性化的服务。在心理健康评估中，EmoCaliber可以辅助医生进行情感诊断，提高诊断的准确性和效率。

## 📄 摘要（原文）

> Visual Emotion Comprehension (VEC) aims to infer sentiment polarities or emotion categories from affective cues embedded in images. In recent years, Multimodal Large Language Models (MLLMs) have established a popular paradigm in VEC, leveraging their generalizability to unify VEC tasks defined under diverse emotion taxonomies. While this paradigm achieves notable success, it typically formulates VEC as a deterministic task, requiring the model to output a single, definitive emotion label for each image. Such a formulation insufficiently accounts for the inherent subjectivity of emotion perception, overlooking alternative interpretations that may be equally plausible to different viewers. To address this limitation, we propose equipping MLLMs with capabilities to verbalize their confidence in emotion predictions. This additional signal provides users with an estimate of both the plausibility of alternative interpretations and the MLLMs' self-assessed competence, thereby enhancing reliability in practice. Building on this insight, we introduce a three-stage training framework that progressively endows with structured reasoning, teaches to verbalize confidence, and calibrates confidence expression, culminating in EmoCaliber, a confidence-aware MLLM for VEC. Through fair and comprehensive evaluations on the unified benchmark VECBench, EmoCaliber demonstrates overall superiority against existing methods in both emotion prediction and confidence estimation. These results validate the effectiveness of our approach and mark a feasible step toward more reliable VEC systems. Project page: https://github.com/wdqqdw/EmoCaliber.

