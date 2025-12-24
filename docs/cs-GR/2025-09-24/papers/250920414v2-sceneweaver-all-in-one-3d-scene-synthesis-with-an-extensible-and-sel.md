---
layout: default
title: "SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent"
---

# SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20414" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20414v2</a>
  <a href="https://arxiv.org/pdf/2509.20414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20414v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20414v2', 'SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yandan Yang, Baoxiong Jia, Shujie Zhang, Siyuan Huang

**分类**: cs.GR, cs.CV, cs.LG, cs.RO

**发布日期**: 2025-09-24 (更新: 2025-10-26)

**备注**: Accepted by NeurIPS 2025, 26 pages

**🔗 代码/项目**: [PROJECT_PAGE](https://scene-weaver.github.io/)

---

## 💡 一句话要点

**SceneWeaver：基于可扩展自反思Agent的All-in-One 3D场景合成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景合成` `具身智能` `语言模型` `Agent框架` `迭代优化` `物理合理性` `视觉真实性`

## 📋 核心要点

1. 现有室内场景合成方法在场景类别、物体细节和物理一致性方面存在局限，难以满足具身智能对多样化3D环境的需求。
2. SceneWeaver采用基于语言模型的规划器，结合多种场景生成工具，通过迭代细化和自我评估，实现更逼真、合理和语义对齐的3D场景。
3. 实验结果表明，SceneWeaver在物理、视觉和语义指标上均优于现有方法，并能有效推广到复杂场景和多样化指令。

## 📝 摘要（中文）

随着具身智能的兴起，室内场景合成变得越来越重要，它需要不仅视觉上逼真，而且物理上合理且功能多样的3D环境。虽然最近的方法提高了视觉逼真度，但它们通常仍局限于固定的场景类别，缺乏足够的物体级细节和物理一致性，并且难以与复杂的用户指令对齐。本文提出了SceneWeaver，一个反思性的Agent框架，通过基于工具的迭代细化统一了各种场景合成范式。SceneWeaver的核心是采用基于语言模型的规划器，从一套可扩展的场景生成工具中进行选择，这些工具包括数据驱动的生成模型以及基于视觉和LLM的方法，并由对物理合理性、视觉真实性和与用户输入的语义对齐的自我评估来指导。这种闭环的reason-act-reflect设计使Agent能够识别语义不一致，调用目标工具，并在连续迭代中更新环境。在常见和开放词汇房间类型上的大量实验表明，SceneWeaver不仅在物理、视觉和语义指标上优于先前的方法，而且有效地推广到具有多样化指令的复杂场景，标志着朝着通用3D环境生成迈出了一步。

## 🔬 方法详解

**问题定义**：论文旨在解决现有3D室内场景合成方法的局限性，包括场景类别固定、物体细节不足、物理一致性差以及难以与复杂用户指令对齐等问题。现有方法难以生成既视觉逼真又物理合理且功能多样的3D环境，无法满足具身智能等应用的需求。

**核心思路**：论文的核心思路是构建一个基于Agent的框架，该Agent能够利用多种工具进行场景生成，并通过自我反思和迭代优化来提升场景的质量。Agent通过语言模型进行规划，选择合适的工具，并根据物理合理性、视觉真实性和语义一致性等指标进行自我评估，从而不断改进场景。

**技术框架**：SceneWeaver的整体架构是一个闭环的reason-act-reflect流程。首先，Agent接收用户指令，并使用语言模型进行规划，选择合适的场景生成工具。然后，Agent执行选定的工具，生成或修改场景。最后，Agent对生成的场景进行自我评估，识别潜在的问题，并根据评估结果调整后续的工具选择和执行。该流程不断迭代，直到场景满足要求。主要模块包括：语言模型规划器、场景生成工具集、自我评估模块。

**关键创新**：SceneWeaver的关键创新在于其Agent框架和闭环的reason-act-reflect流程。该框架能够灵活地组合多种场景生成工具，并利用自我评估来指导场景的迭代优化。这种方法不仅提高了场景的质量，还使其能够适应复杂的用户指令和开放词汇的场景类型。与现有方法相比，SceneWeaver更具通用性和可扩展性。

**关键设计**：SceneWeaver的关键设计包括：1) 可扩展的场景生成工具集，涵盖数据驱动的生成模型和基于视觉/LLM的方法；2) 基于语言模型的规划器，用于选择合适的工具；3) 自我评估模块，用于评估物理合理性、视觉真实性和语义一致性；4) 迭代优化流程，通过不断的反思和调整来提升场景质量。具体的参数设置、损失函数和网络结构等技术细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

SceneWeaver在常见和开放词汇房间类型上的实验结果表明，其在物理、视觉和语义指标上均优于现有方法。具体性能数据和对比基线在论文中进行了详细展示（未知）。该方法能够有效地推广到具有多样化指令的复杂场景，表明其具有良好的泛化能力。实验结果证明了SceneWeaver在3D场景合成方面的优越性和潜力。

## 🎯 应用场景

SceneWeaver具有广泛的应用前景，可用于虚拟现实、游戏开发、机器人导航、室内设计等领域。它可以帮助用户快速生成高质量的3D室内场景，并根据用户需求进行定制。此外，SceneWeaver还可以作为具身智能的训练环境，帮助机器人学习如何在复杂的室内环境中进行导航和交互。未来，该技术有望应用于智能家居、智慧城市等领域。

## 📄 摘要（原文）

> Indoor scene synthesis has become increasingly important with the rise of Embodied AI, which requires 3D environments that are not only visually realistic but also physically plausible and functionally diverse. While recent approaches have advanced visual fidelity, they often remain constrained to fixed scene categories, lack sufficient object-level detail and physical consistency, and struggle to align with complex user instructions. In this work, we present SceneWeaver, a reflective agentic framework that unifies diverse scene synthesis paradigms through tool-based iterative refinement. At its core, SceneWeaver employs a language model-based planner to select from a suite of extensible scene generation tools, ranging from data-driven generative models to visual- and LLM-based methods, guided by self-evaluation of physical plausibility, visual realism, and semantic alignment with user input. This closed-loop reason-act-reflect design enables the agent to identify semantic inconsistencies, invoke targeted tools, and update the environment over successive iterations. Extensive experiments on both common and open-vocabulary room types demonstrate that SceneWeaver not only outperforms prior methods on physical, visual, and semantic metrics, but also generalizes effectively to complex scenes with diverse instructions, marking a step toward general-purpose 3D environment generation. Project website: https://scene-weaver.github.io/.

