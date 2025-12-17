---
layout: default
title: SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing
---

# SketchAssist: A Practical Assistant for Semantic Edits and Precise Local Redrawing

**arXiv**: [2512.14140v1](https://arxiv.org/abs/2512.14140) | [PDF](https://arxiv.org/pdf/2512.14140.pdf)

**作者**: Han Zou, Yan Zhang, Ruiqi Yu, Cong Xie, Jie Huang, Zhenpeng Zhan

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出SketchAssist以解决线稿编辑中语义修改与局部重绘的平衡问题**

🎯 **匹配领域**: **人形机器人** **视觉里程计** **强化学习**

**关键词**: `线稿编辑` `语义编辑` `局部重绘` `可控数据生成` `专家混合` `风格保持` `交互式助手` `数字插画`

## 📋 核心要点

1. 现有图像编辑系统难以在线稿编辑中同时支持高层次语义修改和精确局部重绘，且易破坏线稿的稀疏结构和风格敏感性。
2. SketchAssist通过统一指令引导全局编辑和线条引导区域重绘，结合可控数据生成和任务引导专家混合，提升编辑的语义可控性和结构保真度。
3. 实验表明，SketchAssist在指令遵循和风格/结构保持方面优于基线，实现了线稿编辑任务的最先进性能。

## 📝 摘要（中文）

线稿编辑是数字插画的核心，但现有图像编辑系统难以在支持高层次语义修改和精确局部重绘的同时，保持线稿的稀疏、风格敏感结构。本文提出SketchAssist，一个交互式线稿绘制助手，通过统一指令引导的全局编辑和线条引导的区域重绘来加速创作，同时保持无关区域和整体构图不变。为实现大规模应用，我们引入了一个可控数据生成流程：（i）从无属性基础线稿构建属性添加序列，（ii）通过跨序列采样形成多步编辑链，（iii）应用风格保持的属性移除模型到多样线稿以扩展风格覆盖。基于此数据，SketchAssist采用统一的线稿编辑框架，对基于DiT的编辑器进行最小改动。我们重新利用RGB通道编码输入，实现在单一输入界面中无缝切换指令引导编辑和线条引导重绘。为进一步专业化不同模式的行为，我们在LoRA层中集成任务引导的专家混合，通过文本和视觉线索路由，以提升语义可控性、结构保真度和风格保持。大量实验显示在两个任务上均达到最先进结果，与近期基线相比，在指令遵循和风格/结构保持方面表现更优。我们的数据集和SketchAssist共同为线稿创作和修订提供了一个实用、可控的助手。

## 🔬 方法详解

SketchAssist采用统一的线稿编辑框架，基于DiT编辑器进行最小改动。核心创新包括：重新利用RGB通道编码输入，实现单一界面中指令引导编辑和线条引导重绘的无缝切换；集成任务引导的专家混合到LoRA层，通过文本和视觉线索路由，以提升语义可控性、结构保真度和风格保持。与现有方法相比，其主要区别在于统一了全局语义编辑和局部精确重绘，并通过可控数据生成流程（包括属性添加序列、多步编辑链和风格保持属性移除）支持大规模应用。

## 📊 实验亮点

SketchAssist在指令遵循和风格/结构保持方面优于近期基线，实现了线稿编辑任务的最先进结果，实验显示其在语义编辑和局部重绘中均具有显著性能提升。

## 🎯 应用场景

该研究可应用于数字插画、动画制作、游戏设计和工业设计等领域，为艺术家和设计师提供高效的线稿创作和修订工具，提升创意工作流程的效率和可控性。

## 📄 摘要（原文）

> Sketch editing is central to digital illustration, yet existing image editing systems struggle to preserve the sparse, style-sensitive structure of line art while supporting both high-level semantic changes and precise local redrawing. We present SketchAssist, an interactive sketch drawing assistant that accelerates creation by unifying instruction-guided global edits with line-guided region redrawing, while keeping unrelated regions and overall composition intact. To enable this assistant at scale, we introduce a controllable data generation pipeline that (i) constructs attribute-addition sequences from attribute-free base sketches, (ii) forms multi-step edit chains via cross-sequence sampling, and (iii) expands stylistic coverage with a style-preserving attribute-removal model applied to diverse sketches. Building on this data, SketchAssist employs a unified sketch editing framework with minimal changes to DiT-based editors. We repurpose the RGB channels to encode the inputs, enabling seamless switching between instruction-guided edits and line-guided redrawing within a single input interface. To further specialize behavior across modes, we integrate a task-guided mixture-of-experts into LoRA layers, routing by text and visual cues to improve semantic controllability, structural fidelity, and style preservation. Extensive experiments show state-of-the-art results on both tasks, with superior instruction adherence and style/structure preservation compared to recent baselines. Together, our dataset and SketchAssist provide a practical, controllable assistant for sketch creation and revision.

