---
layout: default
title: AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models
---

# AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.10017" class="toolbar-btn" target="_blank">📄 arXiv: 2511.10017v1</a>
  <a href="https://arxiv.org/pdf/2511.10017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.10017v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.10017v1', 'AffordBot: 3D Fine-grained Embodied Reasoning via Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyi Wang, Xun Yang, Yanlong Xu, Yuchen Wu, Zhen Li, Na Zhao

**分类**: cs.CV

**发布日期**: 2025-11-13

**备注**: NeurIPS 2025

---

## 💡 一句话要点

**AffordBot：利用多模态大语言模型实现细粒度3D具身推理**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `具身智能` `多模态大语言模型` `3D场景理解` `可供性推理` `思维链` `机器人操作` `主动感知`

## 📋 核心要点

1. 现有方法在物理环境中进行人机协作时，缺乏对可交互元素精细位置和交互方式的理解，通常在对象级别操作或孤立地处理可供性推理。
2. AffordBot通过渲染环绕视图图像并结合多模态大语言模型，实现指令驱动的细粒度3D具身推理，预测可供性元素的位置、运动类型和运动轴。
3. 在SceneFun3D数据集上，AffordBot取得了state-of-the-art的性能，验证了其在3D点云输入下的泛化能力和物理基础推理能力。

## 📝 摘要（中文）

本文提出了一种新的任务：细粒度3D具身推理，要求智能体根据任务指令，预测3D场景中每个被引用的可供性元素的三元组，包括空间位置、运动类型和运动轴。为了解决这个问题，我们提出了AffordBot，一个集成了多模态大语言模型（MLLM）和定制的思维链（CoT）推理范式的框架。为了弥合3D输入和2D兼容MLLM之间的差距，我们渲染场景的环绕视图图像，并将3D元素候选投影到这些视图中，形成与场景几何对齐的丰富视觉表示。我们的CoT流程从主动感知阶段开始，提示MLLM根据指令选择信息量最大的视点，然后逐步推理以定位可供性元素并推断合理的交互运动。在SceneFun3D数据集上的评估表明，AffordBot实现了最先进的性能，展示了强大的泛化能力和基于3D点云输入和MLLM的物理基础推理。

## 🔬 方法详解

**问题定义**：现有方法在具身环境中进行推理时，通常只关注物体级别的操作，或者将细粒度的可供性推理孤立地处理，缺乏连贯的、指令驱动的定位和推理能力。这使得智能体难以理解如何与环境中的特定元素进行交互，例如，如何打开一个抽屉，而不仅仅是识别抽屉这个物体。

**核心思路**：AffordBot的核心思路是将3D场景信息转换为2D图像，利用多模态大语言模型（MLLM）强大的视觉理解和推理能力，结合思维链（CoT）方法，逐步推理出可供性元素的位置、运动类型和运动轴。通过主动感知选择最佳视点，提高推理的准确性。

**技术框架**：AffordBot框架主要包含以下几个阶段：1) **3D场景表示**：将3D点云场景渲染成多视角的2D图像，形成环绕视图。2) **候选元素投影**：将3D场景中的候选可供性元素投影到2D图像中，建立3D几何与2D视觉信息的对应关系。3) **主动感知**：利用MLLM根据指令选择信息量最大的视点。4) **思维链推理**：通过CoT方法，MLLM逐步推理出可供性元素的位置、运动类型和运动轴。

**关键创新**：AffordBot的关键创新在于：1) 提出了细粒度3D具身推理任务，填补了现有方法在可供性推理方面的不足。2) 将3D场景信息转换为2D图像，使得MLLM能够直接处理3D场景信息。3) 结合主动感知和思维链推理，提高了推理的准确性和效率。

**关键设计**：在主动感知阶段，MLLM被提示选择最能提供关于可供性元素信息的视点。在思维链推理阶段，MLLM被提示逐步推理，首先定位可供性元素，然后推断其可能的运动类型和运动轴。具体参数设置和网络结构细节在论文中未明确给出，属于未知信息。

## 📊 实验亮点

AffordBot在SceneFun3D数据集上取得了state-of-the-art的性能，证明了其在细粒度3D具身推理方面的有效性。具体性能数据和对比基线在论文中给出，展示了AffordBot相对于现有方法的显著提升。该模型仅使用3D点云输入和MLLM，展示了强大的泛化能力和物理基础推理能力。

## 🎯 应用场景

AffordBot在机器人操作、虚拟助手、增强现实等领域具有广泛的应用前景。例如，它可以帮助机器人理解如何与各种物体进行交互，从而实现更智能、更自主的操作。在虚拟助手领域，它可以帮助用户更自然地与虚拟环境进行交互。在增强现实领域，它可以为用户提供更丰富的交互体验。

## 📄 摘要（原文）

> Effective human-agent collaboration in physical environments requires understanding not only what to act upon, but also where the actionable elements are and how to interact with them. Existing approaches often operate at the object level or disjointedly handle fine-grained affordance reasoning, lacking coherent, instruction-driven grounding and reasoning. In this work, we introduce a new task: Fine-grained 3D Embodied Reasoning, which requires an agent to predict, for each referenced affordance element in a 3D scene, a structured triplet comprising its spatial location, motion type, and motion axis, based on a task instruction. To solve this task, we propose AffordBot, a novel framework that integrates Multimodal Large Language Models (MLLMs) with a tailored chain-of-thought (CoT) reasoning paradigm. To bridge the gap between 3D input and 2D-compatible MLLMs, we render surround-view images of the scene and project 3D element candidates into these views, forming a rich visual representation aligned with the scene geometry. Our CoT pipeline begins with an active perception stage, prompting the MLLM to select the most informative viewpoint based on the instruction, before proceeding with step-by-step reasoning to localize affordance elements and infer plausible interaction motions. Evaluated on the SceneFun3D dataset, AffordBot achieves state-of-the-art performance, demonstrating strong generalization and physically grounded reasoning with only 3D point cloud input and MLLMs.

