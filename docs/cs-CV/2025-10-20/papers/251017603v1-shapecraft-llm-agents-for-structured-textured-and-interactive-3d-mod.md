---
layout: default
title: "ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling"
---

# ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.17603" class="toolbar-btn" target="_blank">📄 arXiv: 2510.17603v1</a>
  <a href="https://arxiv.org/pdf/2510.17603.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.17603v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.17603v1', 'ShapeCraft: LLM Agents for Structured, Textured and Interactive 3D Modeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuyuan Zhang, Chenhan Jiang, Zuoou Li, Jiankang Deng

**分类**: cs.CV

**发布日期**: 2025-10-20

**备注**: NeurIPS 2025 Poster

---

## 💡 一句话要点

**ShapeCraft：利用LLM Agent生成结构化、纹理化和交互式3D模型**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `文本到3D生成` `LLM Agent` `程序化建模` `图表示` `交互式编辑`

## 📋 核心要点

1. 现有文本到3D生成方法生成的网格结构性差，交互性不足，限制了其在艺术创作中的应用。
2. ShapeCraft提出基于图的程序化形状（GPS）表示，并利用多Agent框架迭代优化3D模型，实现结构化生成。
3. 实验表明，ShapeCraft在几何精度和语义丰富度上优于现有方法，并支持动画和用户自定义编辑等交互功能。

## 📝 摘要（中文）

本文提出ShapeCraft，一种新颖的多Agent框架，用于从文本生成3D模型。现有方法生成的3D模型通常是非结构化的网格，且交互性差，难以应用于艺术工作流程。ShapeCraft将3D资产表示为形状程序，并提出基于图的程序化形状（GPS）表示，将复杂的自然语言分解为子任务的结构化图，从而促进LLM对空间关系和语义形状细节的准确理解和解释。LLM Agent分层解析用户输入以初始化GPS，然后迭代地细化程序建模和绘制，以生成结构化、纹理化和交互式的3D资产。实验结果表明，与现有的基于LLM的Agent相比，ShapeCraft在生成几何精确和语义丰富的3D资产方面表现出优越的性能。此外，通过动画和用户自定义编辑的例子，展示了ShapeCraft的多功能性及其在更广泛的交互式应用中的潜力。

## 🔬 方法详解

**问题定义**：现有文本到3D生成方法主要存在两个痛点：一是生成的3D模型通常是非结构化的网格，难以进行后续编辑和控制；二是交互性差，用户难以对生成的模型进行定制和修改，限制了其在实际应用中的价值。

**核心思路**：ShapeCraft的核心思路是将3D模型表示为形状程序，通过程序化的方式生成和编辑3D模型。这种方法可以保证模型的结构化，并方便用户通过修改程序来定制模型。同时，利用LLM Agent来理解自然语言描述，并将其转化为形状程序，从而实现文本到3D模型的自动生成。

**技术框架**：ShapeCraft的整体框架是一个多Agent系统，包括以下几个主要模块：1) GPS初始化Agent：负责将用户输入的自然语言描述解析为基于图的程序化形状（GPS）表示。2) 程序建模Agent：根据GPS表示，生成3D模型的几何结构。3) 纹理绘制Agent：为3D模型添加纹理和材质。4) 迭代优化模块：通过迭代地调整GPS表示和模型参数，优化模型的质量和逼真度。

**关键创新**：ShapeCraft的关键创新在于提出了基于图的程序化形状（GPS）表示。GPS是一种结构化的表示方法，可以将复杂的3D模型分解为一系列简单的几何操作和参数。这种表示方法不仅方便LLM理解和处理，而且可以保证生成的3D模型的结构化和可编辑性。

**关键设计**：GPS表示包含节点和边，节点表示几何操作（如拉伸、旋转、缩放），边表示操作之间的依赖关系。LLM Agent使用分层解析策略，将用户输入分解为子任务，并为每个子任务生成相应的GPS节点。程序建模Agent使用预定义的几何操作库，根据GPS节点生成3D模型的几何结构。纹理绘制Agent使用扩散模型，根据GPS节点和用户描述生成纹理图像。

## 📊 实验亮点

实验结果表明，ShapeCraft在生成几何精确和语义丰富的3D资产方面优于现有的基于LLM的Agent。定性结果展示了ShapeCraft生成复杂场景的能力，定量指标（如FID和CLIP score）也表明ShapeCraft生成的模型在视觉质量和文本一致性方面具有显著优势。此外，ShapeCraft还支持动画和用户自定义编辑等交互功能，展示了其在实际应用中的潜力。

## 🎯 应用场景

ShapeCraft具有广泛的应用前景，包括游戏开发、动画制作、工业设计、建筑可视化等领域。它可以帮助用户快速生成高质量的3D模型，降低建模成本，提高创作效率。此外，ShapeCraft的交互式编辑功能也为用户提供了更大的创作自由，可以根据自己的需求定制3D模型。

## 📄 摘要（原文）

> 3D generation from natural language offers significant potential to reduce expert manual modeling efforts and enhance accessibility to 3D assets. However, existing methods often yield unstructured meshes and exhibit poor interactivity, making them impractical for artistic workflows. To address these limitations, we represent 3D assets as shape programs and introduce ShapeCraft, a novel multi-agent framework for text-to-3D generation. At its core, we propose a Graph-based Procedural Shape (GPS) representation that decomposes complex natural language into a structured graph of sub-tasks, thereby facilitating accurate LLM comprehension and interpretation of spatial relationships and semantic shape details. Specifically, LLM agents hierarchically parse user input to initialize GPS, then iteratively refine procedural modeling and painting to produce structured, textured, and interactive 3D assets. Qualitative and quantitative experiments demonstrate ShapeCraft's superior performance in generating geometrically accurate and semantically rich 3D assets compared to existing LLM-based agents. We further show the versatility of ShapeCraft through examples of animated and user-customized editing, highlighting its potential for broader interactive applications.

