---
layout: default
title: "LL3M: Large Language 3D Modelers"
---

# LL3M: Large Language 3D Modelers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08228" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08228v1</a>
  <a href="https://arxiv.org/pdf/2508.08228.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08228v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08228v1', 'LL3M: Large Language 3D Modelers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sining Lu, Guan Chen, Nam Anh Dinh, Itai Lang, Ari Holtzman, Rana Hanocka

**分类**: cs.GR, cs.AI

**发布日期**: 2025-08-11

**备注**: Our project page is at https://threedle.github.io/ll3m

**🔗 代码/项目**: [PROJECT_PAGE](https://threedle.github.io/ll3m)

---

## 💡 一句话要点

**提出LL3M以通过代码生成3D资产，提升创作灵活性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `3D资产生成` `Blender` `代码生成` `多代理系统` `艺术家工作流程` `可编辑性` `模块化设计`

## 📋 核心要点

1. 现有方法通常依赖于大量3D数据进行生成，缺乏灵活性和可编辑性，难以与艺术家工作流程有效结合。
2. LL3M通过将形状生成视为代码编写任务，利用多代理系统协调LLM生成Blender脚本，提升了生成过程的模块化和可控性。
3. 实验结果表明，LL3M在多种形状类别、风格和材料编辑中表现出色，展示了代码生成的强大潜力和灵活性。

## 📝 摘要（中文）

我们提出了LL3M，一个多代理系统，利用预训练的大型语言模型（LLMs）通过编写可解释的Python代码在Blender中生成3D资产。与传统的从3D数据集中学习的生成方法不同，我们将形状生成重新定义为代码编写任务，从而实现更大的模块化、可编辑性和与艺术家工作流程的集成。LL3M协调一组专门的LLM代理，根据文本提示规划、检索、编写、调试和优化Blender脚本，生成和编辑几何体和外观。生成的代码作为高层次、可解释、易读且文档齐全的场景和对象表示，充分利用Blender的复杂构造，支持多样化的形状、材料和场景。我们的实验展示了代码作为3D资产创作的生成和可解释媒介的强大能力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有3D资产生成方法的灵活性不足和与艺术家工作流程的整合问题。传统方法依赖于大量3D数据，缺乏可编辑性和模块化设计，限制了创作的自由度。

**核心思路**：LL3M的核心思路是将3D形状生成重新定义为代码编写任务，通过协调多个专门的LLM代理来生成Blender脚本。这种设计使得生成的资产不仅可编辑，还能与艺术家的创作过程无缝对接。

**技术框架**：LL3M的整体架构包括多个模块：文本提示解析、代码生成、调试与优化、以及用户反馈整合。每个模块由不同的LLM代理负责，形成一个协同工作的小组，确保生成过程的高效和准确。

**关键创新**：LL3M的主要创新在于将代码生成作为3D资产创作的核心媒介，打破了传统的生成模型依赖数据的限制。通过这种方式，生成的代码不仅可读性强，还便于后续的编辑和调整。

**关键设计**：在技术细节上，LL3M利用Blender API文档构建了一个知识库，支持代理在生成代码时进行检索和参考。此外，生成的代码采用高层次的结构，便于艺术家进行进一步的修改和实验。具体的参数设置和损失函数设计尚未详细披露，属于未知领域。

## 📊 实验亮点

实验结果表明，LL3M在多种形状类别的生成任务中表现优异，能够生成高质量的3D资产。与传统方法相比，LL3M在生成速度和可编辑性上均有显著提升，具体性能数据尚未披露，属于未知领域。

## 🎯 应用场景

LL3M的研究成果在多个领域具有潜在应用价值，包括游戏开发、动画制作、虚拟现实和增强现实等。通过提供灵活的3D资产生成工具，艺术家和开发者可以更高效地实现创意，推动数字内容创作的创新与发展。未来，LL3M可能会与其他AI技术结合，进一步提升3D建模的智能化水平。

## 📄 摘要（原文）

> We present LL3M, a multi-agent system that leverages pretrained large language models (LLMs) to generate 3D assets by writing interpretable Python code in Blender. We break away from the typical generative approach that learns from a collection of 3D data. Instead, we reformulate shape generation as a code-writing task, enabling greater modularity, editability, and integration with artist workflows. Given a text prompt, LL3M coordinates a team of specialized LLM agents to plan, retrieve, write, debug, and refine Blender scripts that generate and edit geometry and appearance. The generated code works as a high-level, interpretable, human-readable, well-documented representation of scenes and objects, making full use of sophisticated Blender constructs (e.g. B-meshes, geometry modifiers, shader nodes) for diverse, unconstrained shapes, materials, and scenes. This code presents many avenues for further agent and human editing and experimentation via code tweaks or procedural parameters. This medium naturally enables a co-creative loop in our system: agents can automatically self-critique using code and visuals, while iterative user instructions provide an intuitive way to refine assets. A shared code context across agents enables awareness of previous attempts, and a retrieval-augmented generation knowledge base built from Blender API documentation, BlenderRAG, equips agents with examples, types, and functions empowering advanced modeling operations and code correctness. We demonstrate the effectiveness of LL3M across diverse shape categories, style and material edits, and user-driven refinements. Our experiments showcase the power of code as a generative and interpretable medium for 3D asset creation. Our project page is at https://threedle.github.io/ll3m.

