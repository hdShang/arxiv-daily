---
layout: default
title: "PromptEnhancer: A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting"
---

# PromptEnhancer: A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04545" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04545v5</a>
  <a href="https://arxiv.org/pdf/2509.04545.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04545v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04545v5', 'PromptEnhancer: A Simple Approach to Enhance Text-to-Image Models via Chain-of-Thought Prompt Rewriting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Linqing Wang, Ximing Xing, Yiji Cheng, Zhiyuan Zhao, Donghao Li, Tiankai Hang, Jiale Tao, Qixun Wang, Ruihuang Li, Comi Chen, Xin Li, Mingrui Wu, Xinchi Deng, Shuyang Gu, Chunyu Wang, Qinglin Lu

**分类**: cs.CV

**发布日期**: 2025-09-04 (更新: 2025-09-23)

**备注**: Technical Report. Project Page: https://hunyuan-promptenhancer.github.io/

---

## 💡 一句话要点

**提出PromptEnhancer，通过思维链提示重写增强文本到图像生成模型。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `提示工程` `思维链` `强化学习` `图像-文本对齐`

## 📋 核心要点

1. 现有的文本到图像模型在处理复杂提示时，难以准确呈现属性绑定、否定和组合关系等，导致用户意图与生成结果不匹配。
2. PromptEnhancer通过训练一个思维链（CoT）重写器，利用强化学习和专门设计的奖励模型AlignEvaluator，生成更精确的提示。
3. 实验表明，PromptEnhancer显著提高了图像-文本对齐，并提供了一个新的高质量人类偏好基准，促进未来研究。

## 📝 摘要（中文）

本文提出PromptEnhancer，一种新颖且通用的提示重写框架，用于增强预训练的文本到图像（T2I）模型，无需修改模型权重。与依赖于模型特定微调或隐式奖励信号（如图像奖励分数）的现有方法不同，该框架将重写器与生成器解耦。通过强化学习训练一个思维链（CoT）重写器，并由一个名为AlignEvaluator的专用奖励模型指导。AlignEvaluator基于对常见T2I失败模式的全面分析，从24个关键点的系统分类中提取，提供显式和细粒度的反馈。通过优化CoT重写器以最大化来自AlignEvaluator的奖励，该框架学习生成能够被T2I模型更精确地解释的提示。在HunyuanImage 2.1模型上的大量实验表明，PromptEnhancer显著提高了各种语义和组合挑战中的图像-文本对齐。此外，本文还引入了一个新的高质量人类偏好基准，以促进未来在该方向的研究。

## 🔬 方法详解

**问题定义**：文本到图像生成模型在处理复杂的用户提示时，经常出现图像与文本描述不一致的问题，尤其是在属性绑定、否定和组合关系等方面。现有的方法通常需要对模型进行微调或者依赖隐式的奖励信号，计算成本高昂且缺乏明确的指导。

**核心思路**：PromptEnhancer的核心思路是将提示重写器与图像生成器解耦，通过强化学习训练一个思维链（CoT）重写器，使其能够生成更符合图像生成器理解的提示。通过显式的奖励模型AlignEvaluator，为重写器提供细粒度的反馈，从而优化重写过程。

**技术框架**：PromptEnhancer框架主要包含三个模块：文本到图像生成模型（T2I Model）、思维链提示重写器（CoT Rewriter）和对齐评估器（AlignEvaluator）。首先，用户输入原始提示，CoT Rewriter根据原始提示生成新的提示。然后，T2I Model根据新的提示生成图像。最后，AlignEvaluator评估生成图像与原始提示的对齐程度，并将评估结果作为奖励信号反馈给CoT Rewriter，用于优化重写策略。

**关键创新**：PromptEnhancer的关键创新在于将提示重写过程与图像生成过程解耦，并引入了显式的对齐评估器AlignEvaluator。AlignEvaluator基于对T2I模型常见失败模式的分析，提供细粒度的反馈，从而更有效地指导提示重写器的训练。与现有方法相比，PromptEnhancer无需修改图像生成模型的权重，具有更好的通用性和可扩展性。

**关键设计**：AlignEvaluator的设计是关键。它基于对T2I模型常见失败模式的系统分类，定义了24个关键点，用于评估生成图像与原始提示的对齐程度。CoT Rewriter使用强化学习进行训练，目标是最大化来自AlignEvaluator的奖励。具体的强化学习算法和奖励函数的设计对最终效果有重要影响。论文中使用了HunyuanImage 2.1模型进行实验，并构建了一个新的高质量人类偏好基准。

## 📊 实验亮点

在HunyuanImage 2.1模型上的实验表明，PromptEnhancer显著提高了图像-文本对齐，尤其是在处理复杂提示时。此外，该论文还构建了一个新的高质量人类偏好基准，为未来的研究提供了有价值的资源。具体的性能提升数据需要在论文中查找。

## 🎯 应用场景

PromptEnhancer可应用于各种文本到图像生成场景，例如艺术创作、产品设计、虚拟现实等。通过提高生成图像与用户意图的对齐程度，可以提升用户体验，并促进文本到图像生成技术在更广泛领域的应用。该研究也有助于提升AI模型的可控性和可靠性。

## 📄 摘要（原文）

> Recent advancements in text-to-image (T2I) diffusion models have demonstrated remarkable capabilities in generating high-fidelity images. However, these models often struggle to faithfully render complex user prompts, particularly in aspects like attribute binding, negation, and compositional relationships. This leads to a significant mismatch between user intent and the generated output. To address this challenge, we introduce PromptEnhancer, a novel and universal prompt rewriting framework that enhances any pretrained T2I model without requiring modifications to its weights. Unlike prior methods that rely on model-specific fine-tuning or implicit reward signals like image-reward scores, our framework decouples the rewriter from the generator. We achieve this by training a Chain-of-Thought (CoT) rewriter through reinforcement learning, guided by a dedicated reward model we term the AlignEvaluator. The AlignEvaluator is trained to provide explicit and fine-grained feedback based on a systematic taxonomy of 24 key points, which are derived from a comprehensive analysis of common T2I failure modes. By optimizing the CoT rewriter to maximize the reward from our AlignEvaluator, our framework learns to generate prompts that are more precisely interpreted by T2I models. Extensive experiments on the HunyuanImage 2.1 model demonstrate that PromptEnhancer significantly improves image-text alignment across a wide range of semantic and compositional challenges. Furthermore, we introduce a new, high-quality human preference benchmark to facilitate future research in this direction.

