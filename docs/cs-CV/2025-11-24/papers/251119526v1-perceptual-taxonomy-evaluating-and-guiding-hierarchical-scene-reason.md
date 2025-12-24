---
layout: default
title: "Perceptual Taxonomy: Evaluating and Guiding Hierarchical Scene Reasoning in Vision-Language Models"
---

# Perceptual Taxonomy: Evaluating and Guiding Hierarchical Scene Reasoning in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19526" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19526v1</a>
  <a href="https://arxiv.org/pdf/2511.19526.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19526v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.19526v1', 'Perceptual Taxonomy: Evaluating and Guiding Hierarchical Scene Reasoning in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jonathan Lee, Xingrui Wang, Jiawei Peng, Luoxin Ye, Zehan Zheng, Tiezheng Zhang, Tao Wang, Wufei Ma, Siyi Chen, Yu-Cheng Chou, Prakhar Kaushik, Alan Yuille

**分类**: cs.CV

**发布日期**: 2025-11-24

---

## 💡 一句话要点

**提出感知分类法，用于评估和指导视觉-语言模型中的分层场景推理**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `视觉-语言模型` `场景理解` `物理推理` `分层推理` `基准测试` `属性推断` `感知分类法`

## 📋 核心要点

1. 现有视觉-语言基准测试缺乏对物理基础视觉推理的全面评估，主要集中于表面识别或图像-文本对齐。
2. 论文提出Perceptual Taxonomy，通过识别物体、空间配置并推断属性来支持目标导向的推理。
3. 实验结果表明，现有模型在属性驱动问题上性能下降，但通过感知分类法引导提示可以有效提升性能。

## 📝 摘要（中文）

本文提出了一种结构化的场景理解过程，称为感知分类法。该方法首先识别物体及其空间配置，然后推断任务相关的属性，如材料、可供性、功能和物理属性，以支持目标导向的推理。为了弥补现有视觉-语言基准测试在全面评估这种能力方面的不足，本文引入了Perceptual Taxonomy，一个用于物理基础视觉推理的基准。该基准使用四个属性族覆盖的84个细粒度属性标注了3173个对象。利用这些标注，构建了一个包含5802张图像的多项选择题基准，涵盖合成和真实领域。该基准包含28033个基于模板的问题，跨越四种类型（对象描述、空间推理、属性匹配和分类推理），以及50个专家精心设计的问题，旨在评估模型在感知分类推理的各个方面的能力。实验结果表明，领先的视觉-语言模型在识别任务上表现良好，但在属性驱动的问题上性能下降10%到20%，尤其是在需要对结构化属性进行多步推理的问题上。这些发现突出了结构化视觉理解方面存在的差距，以及当前严重依赖模式匹配的模型的局限性。此外，研究表明，提供来自模拟场景的上下文推理示例可以提高模型在真实世界和专家策划问题上的性能，证明了感知分类法引导提示的有效性。

## 🔬 方法详解

**问题定义**：现有视觉-语言模型在场景理解方面存在不足，尤其是在需要进行多步骤推理和理解物体属性（如材质、功能等）的任务中表现不佳。现有的基准测试主要关注表面识别和图像-文本对齐，缺乏对物理基础视觉推理的全面评估。

**核心思路**：论文的核心思路是构建一个结构化的场景理解过程，即Perceptual Taxonomy。该方法模拟人类的感知过程，首先识别场景中的物体及其空间关系，然后推断这些物体的属性，从而支持更高级别的推理任务。通过这种分层推理，模型可以更好地理解场景的物理属性和功能。

**技术框架**：Perceptual Taxonomy包含以下几个主要组成部分：1) 对象识别模块，用于识别场景中的物体；2) 空间关系推理模块，用于理解物体之间的空间配置；3) 属性推断模块，用于推断物体的属性，如材料、可供性、功能和物理属性；4) 基于模板的问题生成模块，用于生成多项选择题，涵盖对象描述、空间推理、属性匹配和分类推理等类型；5) 专家策划问题集，用于评估模型在复杂场景下的推理能力。

**关键创新**：该论文的关键创新在于提出了Perceptual Taxonomy这一结构化的场景理解过程，并构建了一个相应的基准测试。与以往的基准测试相比，Perceptual Taxonomy更注重对模型物理基础视觉推理能力的评估，而不仅仅是表面识别。此外，论文还提出了使用感知分类法引导提示的方法，通过提供来自模拟场景的上下文推理示例来提高模型在真实世界和专家策划问题上的性能。

**关键设计**：Perceptual Taxonomy基准测试包含3173个对象，并使用四个属性族覆盖的84个细粒度属性进行标注。基准测试包含5802张图像，涵盖合成和真实领域。问题生成采用基于模板的方法，生成28033个问题，并辅以50个专家策划的问题。在实验中，论文使用了多种领先的视觉-语言模型，并评估了它们在不同类型问题上的性能。此外，论文还研究了不同提示策略对模型性能的影响。

## 📊 实验亮点

实验结果表明，领先的视觉-语言模型在识别任务上表现良好，但在属性驱动的问题上性能下降10%到20%。通过提供来自模拟场景的上下文推理示例，模型在真实世界和专家策划问题上的性能得到显著提升，证明了感知分类法引导提示的有效性。例如，在专家策划问题上，性能提升幅度超过5%。

## 🎯 应用场景

该研究成果可应用于机器人导航、智能家居、自动驾驶等领域。通过提升视觉-语言模型对场景的结构化理解能力，可以使机器人更好地理解周围环境，从而实现更智能的交互和决策。此外，该研究也有助于开发更强大的视觉辅助工具，帮助视障人士更好地理解周围世界。

## 📄 摘要（原文）

> We propose Perceptual Taxonomy, a structured process of scene understanding that first recognizes objects and their spatial configurations, then infers task-relevant properties such as material, affordance, function, and physical attributes to support goal-directed reasoning. While this form of reasoning is fundamental to human cognition, current vision-language benchmarks lack comprehensive evaluation of this ability and instead focus on surface-level recognition or image-text alignment.
>   To address this gap, we introduce Perceptual Taxonomy, a benchmark for physically grounded visual reasoning. We annotate 3173 objects with four property families covering 84 fine-grained attributes. Using these annotations, we construct a multiple-choice question benchmark with 5802 images across both synthetic and real domains. The benchmark contains 28033 template-based questions spanning four types (object description, spatial reasoning, property matching, and taxonomy reasoning), along with 50 expert-crafted questions designed to evaluate models across the full spectrum of perceptual taxonomy reasoning.
>   Experimental results show that leading vision-language models perform well on recognition tasks but degrade by 10 to 20 percent on property-driven questions, especially those requiring multi-step reasoning over structured attributes. These findings highlight a persistent gap in structured visual understanding and the limitations of current models that rely heavily on pattern matching. We also show that providing in-context reasoning examples from simulated scenes improves performance on real-world and expert-curated questions, demonstrating the effectiveness of perceptual-taxonomy-guided prompting.

