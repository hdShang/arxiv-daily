---
layout: default
title: CRAFT-E: A Neuro-Symbolic Framework for Embodied Affordance Grounding
---

# CRAFT-E: A Neuro-Symbolic Framework for Embodied Affordance Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.04231" class="toolbar-btn" target="_blank">📄 arXiv: 2512.04231v1</a>
  <a href="https://arxiv.org/pdf/2512.04231.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.04231v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.04231v1', 'CRAFT-E: A Neuro-Symbolic Framework for Embodied Affordance Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhou Chen, Joe Lin, Carson Bulgin, Sathyanarayanan N. Aakur

**分类**: cs.RO, cs.AI

**发布日期**: 2025-12-03

**备注**: 20 pages. 3 figures, 4 tables. Under Review

---

## 💡 一句话要点

**CRAFT-E：用于具身可供性接地的神经符号框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `具身智能` `可供性` `神经符号` `知识图谱` `机器人` `视觉语言对齐` `抓取推理`

## 📋 核心要点

1. 现有方法依赖黑盒模型或固定标签，缺乏透明性和可控性，难以满足人机交互应用的需求。
2. CRAFT-E结合知识图谱、视觉语言对齐和能量模型，生成可解释的推理路径，并考虑抓取可行性。
3. CRAFT-E在静态场景和真实机器人实验中表现出色，且在感知噪声下保持鲁棒性，提供组件级诊断。

## 📝 摘要（中文）

在非结构化环境中运行的辅助机器人不仅需要理解物体是什么，还需要理解它们可以用来做什么。这需要将基于语言的动作查询与既能提供所需功能又能被物理检索的物体进行关联。现有方法通常依赖于黑盒模型或固定的可供性标签，限制了面向人类应用的透明性、可控性和可靠性。我们引入了CRAFT-E，一个模块化的神经符号框架，它将结构化的动词-属性-对象知识图与视觉-语言对齐和基于能量的抓取推理相结合。该系统生成可解释的接地路径，揭示影响物体选择的因素，并将抓取可行性作为可供性推理的一个组成部分。我们进一步构建了一个基准数据集，其中包含动词-对象兼容性、分割和抓取候选的统一注释，并在物理机器人上部署了完整的pipeline。CRAFT-E在静态场景、基于ImageNet的功能检索以及涉及20个动词和39个物体的真实世界试验中取得了有竞争力的性能。该框架在感知噪声下保持稳健，并提供透明的组件级诊断。通过将符号推理与具身感知相结合，CRAFT-E为可供性接地的物体选择提供了一种可解释和可定制的替代方案，支持辅助机器人系统中值得信赖的决策。

## 🔬 方法详解

**问题定义**：论文旨在解决辅助机器人如何在非结构化环境中理解物体的功能（可供性），并根据语言指令选择合适的物体进行操作的问题。现有方法的痛点在于依赖黑盒模型或预定义的可供性标签，缺乏透明性和可解释性，难以调试和信任。

**核心思路**：论文的核心思路是将神经方法和符号推理相结合，构建一个模块化的神经符号框架。通过知识图谱来表示物体、属性和动作之间的关系，利用视觉语言模型将语言指令与视觉信息对齐，并使用能量模型来评估抓取的可行性。这样可以生成可解释的推理路径，从而提高系统的透明性和可控性。

**技术框架**：CRAFT-E框架包含以下主要模块：1) 知识图谱：存储动词、属性和对象之间的关系。2) 视觉语言对齐模块：将语言指令中的动词和对象与图像中的视觉信息对齐。3) 能量模型：评估抓取候选的质量和可行性。4) 推理引擎：根据知识图谱、视觉语言对齐结果和抓取可行性，生成可解释的接地路径，选择最佳物体。

**关键创新**：CRAFT-E的关键创新在于将符号推理与具身感知相结合，构建了一个可解释的神经符号框架。与端到端模型相比，CRAFT-E的推理过程更加透明，可以进行组件级的诊断和调试。此外，CRAFT-E将抓取可行性作为可供性推理的一个组成部分，提高了物体选择的准确性和可靠性。

**关键设计**：CRAFT-E使用预训练的视觉语言模型（如CLIP）进行视觉语言对齐。能量模型采用基于能量的框架，通过学习能量函数来评估抓取候选的质量。知识图谱采用人工构建的方式，并根据具体任务进行扩展。损失函数包括视觉语言对齐损失和抓取能量损失。

## 📊 实验亮点

CRAFT-E在静态场景、ImageNet-based功能检索和真实世界机器人实验中取得了有竞争力的性能。实验结果表明，CRAFT-E在感知噪声下保持鲁棒性，并能够提供透明的组件级诊断。在真实机器人实验中，CRAFT-E成功地完成了涉及20个动词和39个物体的任务。

## 🎯 应用场景

CRAFT-E可应用于辅助机器人、智能家居、工业自动化等领域。它可以帮助机器人理解人类的指令，选择合适的工具和物体进行操作，从而提高机器人的自主性和智能化水平。该研究有助于构建更值得信赖、更易于理解和控制的机器人系统，促进人机协作。

## 📄 摘要（原文）

> Assistive robots operating in unstructured environments must understand not only what objects are, but what they can be used for. This requires grounding language-based action queries to objects that both afford the requested function and can be physically retrieved. Existing approaches often rely on black-box models or fixed affordance labels, limiting transparency, controllability, and reliability for human-facing applications. We introduce CRAFT-E, a modular neuro-symbolic framework that composes a structured verb-property-object knowledge graph with visual-language alignment and energy-based grasp reasoning. The system generates interpretable grounding paths that expose the factors influencing object selection and incorporates grasp feasibility as an integral part of affordance inference. We further construct a benchmark dataset with unified annotations for verb-object compatibility, segmentation, and grasp candidates, and deploy the full pipeline on a physical robot. CRAFT-E achieves competitive performance in static scenes, ImageNet-based functional retrieval, and real-world trials involving 20 verbs and 39 objects. The framework remains robust under perceptual noise and provides transparent, component-level diagnostics. By coupling symbolic reasoning with embodied perception, CRAFT-E offers an interpretable and customizable alternative to end-to-end models for affordance-grounded object selection, supporting trustworthy decision-making in assistive robotic systems.

