---
layout: default
title: "UI2V-Bench: An Understanding-based Image-to-video Generation Benchmark"
---

# UI2V-Bench: An Understanding-based Image-to-video Generation Benchmark

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24427" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24427v1</a>
  <a href="https://arxiv.org/pdf/2509.24427.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24427v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24427v1', 'UI2V-Bench: An Understanding-based Image-to-video Generation Benchmark')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ailing Zhang, Lina Lei, Dehong Kong, Zhixin Wang, Jiaqi Xu, Fenglong Song, Chun-Le Guo, Chang Liu, Fan Li, Jie Chen

**分类**: cs.CV

**发布日期**: 2025-09-29

---

## 💡 一句话要点

**UI2V-Bench：提出一个基于理解的图生视频生成评测基准，关注语义理解与推理能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图生视频` `视频生成` `语义理解` `常识推理` `多模态学习`

## 📋 核心要点

1. 现有I2V评估基准侧重视频质量和时间一致性，忽略了模型对图像语义的理解和常识推理能力。
2. UI2V-Bench通过引入空间理解、属性绑定、类别理解和推理四个维度，评估I2V模型的语义理解能力。
3. 该基准包含500个文本-图像对，并使用基于MLLM的评估方法，与人工评估结果高度一致。

## 📝 摘要（中文）

生成扩散模型发展迅速，并在图像到视频（I2V）生成领域引起了广泛关注。然而，现有的评估基准主要关注视频质量和时间一致性，而忽略了模型理解输入图像中特定对象语义以及确保生成的视频符合物理规律和人类常识的能力。为了解决这个问题，我们提出了UI2V-Bench，这是一个新的基准，用于评估I2V模型，重点关注语义理解和推理。它引入了四个主要的评估维度：空间理解、属性绑定、类别理解和推理。为了评估这些维度，我们设计了两种基于多模态大型语言模型（MLLM）的评估方法：用于细粒度语义理解的实例级pipeline，以及用于逐步因果评估的基于反馈的推理pipeline，以实现更准确的评估。UI2V-Bench包括大约500个精心构建的文本-图像对，并评估了一系列开源和闭源I2V模型。我们进一步纳入了人工评估，结果表明与我们提出的基于MLLM的指标高度一致。总的来说，UI2V-Bench通过强调语义理解和推理能力，填补了I2V评估中的一个关键空白，提供了一个强大的框架和数据集，以支持该领域未来的研究和模型开发。

## 🔬 方法详解

**问题定义**：现有图像到视频（I2V）生成模型的评估主要集中在视频质量和时间一致性上，缺乏对模型理解输入图像语义以及进行常识推理能力的有效评估。这导致模型可能生成视觉上流畅但语义上不合理或违反物理规律的视频，限制了I2V技术在实际应用中的可靠性。

**核心思路**：UI2V-Bench的核心思路是构建一个能够全面评估I2V模型语义理解和推理能力的基准。通过定义四个关键维度（空间理解、属性绑定、类别理解和推理），并设计基于多模态大型语言模型（MLLM）的评估方法，该基准旨在更准确地衡量模型对图像内容的理解程度以及生成符合常识和物理规律视频的能力。

**技术框架**：UI2V-Bench的评估框架主要包含以下几个阶段：1) 数据集构建：包含500个精心设计的文本-图像对，涵盖各种场景和对象。2) 特征提取：使用I2V模型生成视频。3) 维度评估：针对空间理解、属性绑定、类别理解和推理四个维度，分别设计评估方法。4) MLLM评估：利用MLLM进行自动评估，包括实例级pipeline和反馈式推理pipeline。5) 人工评估：进行人工评估，验证MLLM评估的有效性。

**关键创新**：UI2V-Bench的关键创新在于其评估维度和评估方法。它首次将语义理解和推理能力作为I2V模型评估的重要指标，并设计了基于MLLM的自动评估方法，能够更细粒度地评估模型的语义理解能力。反馈式推理pipeline通过逐步因果评估，提高了评估的准确性。

**关键设计**：UI2V-Bench的关键设计包括：1) 四个评估维度的定义，确保全面覆盖语义理解和推理能力。2) 基于MLLM的实例级pipeline，用于细粒度语义理解。3) 基于MLLM的反馈式推理pipeline，用于逐步因果评估。4) 数据集的构建，包含多样化的场景和对象，以提高评估的泛化能力。5) MLLM的选择和prompt的设计，确保评估的准确性和可靠性。

## 📊 实验亮点

UI2V-Bench对多个开源和闭源I2V模型进行了评估，结果表明现有模型在语义理解和推理方面存在明显不足。人工评估结果与MLLM评估结果高度一致，验证了UI2V-Bench的有效性。该基准为未来的I2V模型研究提供了一个可靠的评估平台。

## 🎯 应用场景

UI2V-Bench可应用于评估和改进图像到视频生成模型，尤其是在需要高度语义一致性和常识推理的场景中，例如：自动驾驶模拟、游戏开发、虚拟现实内容生成、教育视频制作等。该基准能够推动I2V技术的发展，使其生成的视频更符合人类的预期和理解，从而提高用户体验和应用价值。

## 📄 摘要（原文）

> Generative diffusion models are developing rapidly and attracting increasing attention due to their wide range of applications. Image-to-Video (I2V) generation has become a major focus in the field of video synthesis. However, existing evaluation benchmarks primarily focus on aspects such as video quality and temporal consistency, while largely overlooking the model's ability to understand the semantics of specific subjects in the input image or to ensure that the generated video aligns with physical laws and human commonsense. To address this gap, we propose UI2V-Bench, a novel benchmark for evaluating I2V models with a focus on semantic understanding and reasoning. It introduces four primary evaluation dimensions: spatial understanding, attribute binding, category understanding, and reasoning. To assess these dimensions, we design two evaluation methods based on Multimodal Large Language Models (MLLMs): an instance-level pipeline for fine-grained semantic understanding, and a feedback-based reasoning pipeline that enables step-by-step causal assessment for more accurate evaluation. UI2V-Bench includes approximately 500 carefully constructed text-image pairs and evaluates a range of both open source and closed-source I2V models across all defined dimensions. We further incorporate human evaluations, which show strong alignment with the proposed MLLM-based metrics. Overall, UI2V-Bench fills a critical gap in I2V evaluation by emphasizing semantic comprehension and reasoning ability, offering a robust framework and dataset to support future research and model development in the field.

