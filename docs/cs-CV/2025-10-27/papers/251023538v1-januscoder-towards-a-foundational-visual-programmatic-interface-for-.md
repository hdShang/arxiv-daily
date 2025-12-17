---
layout: default
title: JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence
---

# JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23538" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23538v1</a>
  <a href="https://arxiv.org/pdf/2510.23538.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23538v1" onclick="toggleFavorite(this, '2510.23538v1', 'JanusCoder: Towards a Foundational Visual-Programmatic Interface for Code Intelligence')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qiushi Sun, Jingyang Gong, Yang Liu, Qiaosheng Chen, Lei Li, Kai Chen, Qipeng Guo, Ben Kao, Fei Yuan

**分类**: cs.AI, cs.CL, cs.CV, cs.SE

**发布日期**: 2025-10-27

**备注**: Work in progress

**🔗 代码/项目**: [GITHUB](https://github.com/InternLM/JanusCoder)

---

## 💡 一句话要点

**JanusCoder：构建用于代码智能的基础视觉-程序化接口**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `代码智能` `多模态学习` `视觉-程序化接口` `代码生成` `数据合成` `Transformer模型` `神经网络`

## 📋 核心要点

1. 现有神经代码智能方法在处理视觉输出方面存在不足，缺乏高质量多模态代码数据是主要瓶颈。
2. 论文提出JanusCoder，通过构建大规模多模态代码语料库和统一模型，实现文本、视觉到代码的转换。
3. 实验表明，JanusCoder在文本和视觉编码任务上表现出色，性能接近甚至超过商业模型。

## 📝 摘要（中文）

神经代码智能的范围正迅速扩展，超越了基于文本的源代码，涵盖了程序生成的丰富视觉输出。这种视觉维度对于灵活的内容生成以及精确的、程序驱动的可视化编辑等高级应用至关重要。然而，高质量多模态代码数据的稀缺阻碍了进展，这是由于合成和质量评估方面的挑战造成的。为了应对这些挑战，我们从数据和建模的角度做出了贡献。我们首先引入了一个完整的合成工具包，该工具包利用数据模态之间的互惠协同作用，有效地生成大规模、高质量的语料库，涵盖从标准图表到复杂的交互式Web UI和代码驱动的动画。利用这个工具包，我们构建了迄今为止最大的多模态代码语料库JanusCode-800K。这为我们的模型JanusCoder和JanusCoderV的训练提供了支持，这些模型建立了一个视觉-程序化接口，用于从文本指令、视觉输入或两者的组合生成代码。我们的统一模型与为孤立任务构建专用模型的现有方法不同。在以文本为中心和以视觉为中心的编码任务上进行的大量实验表明，JanusCoder系列的性能优越，我们的7B到14B规模的模型接近甚至超过了商业模型的性能。此外，广泛的分析提供了关于协调程序逻辑与其视觉表达的关键见解。我们的代码和检查点可在https://github.com/InternLM/JanusCoder获得。

## 🔬 方法详解

**问题定义**：现有神经代码智能方法主要集中于文本代码的处理，忽略了程序生成的视觉输出，如图表、UI界面等。缺乏大规模、高质量的多模态代码数据，阻碍了视觉-程序化接口的发展。现有方法通常为特定任务构建专用模型，缺乏通用性。

**核心思路**：论文的核心思路是构建一个统一的视觉-程序化接口，能够根据文本指令、视觉输入或两者的结合生成代码。通过大规模多模态代码语料库的训练，使模型能够理解和生成程序逻辑及其视觉表达。这种统一模型避免了为每个任务构建专用模型的需要。

**技术框架**：JanusCoder的技术框架主要包括两个部分：一是数据合成工具包，用于生成大规模多模态代码语料库JanusCode-800K；二是统一的JanusCoder模型，该模型基于Transformer架构，能够接收文本、视觉输入，并生成代码。整个流程包括数据收集与合成、模型训练和评估。

**关键创新**：论文的关键创新在于：1) 提出了一个完整的合成工具包，能够高效生成大规模、高质量的多模态代码数据；2) 构建了迄今为止最大的多模态代码语料库JanusCode-800K；3) 提出了统一的JanusCoder模型，能够处理文本和视觉输入，并生成代码，避免了为特定任务构建专用模型。

**关键设计**：JanusCoder模型基于Transformer架构，具体结构未知。数据合成工具包的设计细节未知。损失函数和训练策略等细节未知。模型规模包括7B和14B两种。

## 📊 实验亮点

JanusCoder在文本和视觉编码任务上表现出色，7B到14B规模的模型性能接近甚至超过了商业模型。论文构建了迄今为止最大的多模态代码语料库JanusCode-800K，为模型训练提供了有力支持。实验结果表明，JanusCoder能够有效协调程序逻辑与其视觉表达。

## 🎯 应用场景

JanusCoder具有广泛的应用前景，包括自动化UI生成、数据可视化、代码驱动的动画生成等。它可以帮助开发者更高效地创建和编辑可视化内容，降低开发成本。未来，JanusCoder有望成为构建通用人工智能的重要组成部分，实现更智能的人机交互。

## 📄 摘要（原文）

> The scope of neural code intelligence is rapidly expanding beyond text-based source code to encompass the rich visual outputs that programs generate. This visual dimension is critical for advanced applications like flexible content generation and precise, program-driven editing of visualizations. However, progress has been impeded by the scarcity of high-quality multimodal code data, a bottleneck stemming from challenges in synthesis and quality assessment. To address these challenges, we make contributions from both a data and modeling perspective. We first introduce a complete synthesis toolkit that leverages reciprocal synergies between data modalities to efficiently produce a large-scale, high-quality corpus spanning from standard charts to complex interactive web UIs and code-driven animations. Leveraging this toolkit, we construct JanusCode-800K, the largest multimodal code corpus to date. This powers the training of our models, JanusCoder and JanusCoderV, which establish a visual-programmatic interface for generating code from textual instructions, visual inputs, or a combination of both. Our unified model is a departure from existing approaches that build specialized models for isolated tasks. Extensive experiments on both text-centric and vision-centric coding tasks demonstrate the superior performance of the JanusCoder series, with our 7B to 14B scale models approaching or even exceeding the performance of commercial models. Furthermore, extensive analysis provides key insights into harmonizing programmatic logic with its visual expression. Our code and checkpoints will are available at https://github.com/InternLM/JanusCoder.

