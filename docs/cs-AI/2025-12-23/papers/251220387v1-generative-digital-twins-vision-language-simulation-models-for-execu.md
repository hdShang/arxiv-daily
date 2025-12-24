---
layout: default
title: Generative Digital Twins: Vision-Language Simulation Models for Executable Industrial Systems
---

# Generative Digital Twins: Vision-Language Simulation Models for Executable Industrial Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20387" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20387v1</a>
  <a href="https://arxiv.org/pdf/2512.20387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20387v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20387v1', 'Generative Digital Twins: Vision-Language Simulation Models for Executable Industrial Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: YuChe Hsu, AnJui Wang, TsaiChing Ni, YuanFu Yang

**分类**: cs.AI, cs.CL, cs.CV

**发布日期**: 2025-12-23

**备注**: 10 pages, 9 figures

---

## 💡 一句话要点

**提出视觉-语言模拟模型，从草图和文本生成可执行的工业系统数字孪生。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数字孪生` `视觉-语言模型` `工业仿真` `跨模态学习` `代码生成`

## 📋 核心要点

1. 现有工业仿真系统缺乏从视觉和语言信息直接生成可执行代码的能力，限制了其易用性和智能化水平。
2. 提出视觉-语言模拟模型（VLSM），利用草图和自然语言提示生成可执行的FlexScript代码，实现跨模态的工业仿真。
3. 构建大规模数据集，并提出结构有效率、参数匹配率和执行成功率等新指标，实验结果表明模型具有高精度和鲁棒性。

## 📝 摘要（中文）

本文提出了一种视觉-语言模拟模型（VLSM），它统一了视觉和文本理解，能够从布局草图和自然语言提示中合成可执行的FlexScript代码，从而实现工业仿真系统的跨模态推理。为了支持这种新范式，本研究构建了首个用于生成数字孪生的大规模数据集，包含超过12万个提示-草图-代码三元组，从而实现文本描述、空间结构和仿真逻辑之间的多模态学习。同时，针对该任务专门提出了三个新的评估指标：结构有效率（SVR）、参数匹配率（PMR）和执行成功率（ESR），以全面评估结构完整性、参数保真度和仿真器的可执行性。通过对视觉编码器、连接器和代码预训练语言骨干网络的系统性消融研究，所提出的模型实现了近乎完美的结构精度和高执行鲁棒性。这项工作为将视觉推理和语言理解集成到可执行的工业仿真系统中的生成数字孪生奠定了基础。

## 🔬 方法详解

**问题定义**：现有工业仿真系统通常需要人工编写复杂的代码来描述系统行为，这既耗时又需要专业的编程知识。缺乏一种能够直接从视觉布局和自然语言描述生成可执行代码的方法，使得仿真系统的构建和修改变得困难，阻碍了其广泛应用。

**核心思路**：本文的核心思路是利用视觉和语言的互补信息，通过一个统一的模型将布局草图和自然语言提示转化为可执行的仿真代码。这种方法旨在降低仿真系统的构建门槛，提高其智能化水平，使得用户可以通过更直观的方式来创建和修改仿真模型。

**技术框架**：该方法的核心是视觉-语言模拟模型（VLSM），它包含以下几个主要模块：1) 视觉编码器：用于提取布局草图的视觉特征；2) 文本编码器：用于提取自然语言提示的语义特征；3) 连接器：用于融合视觉和文本特征，实现跨模态的信息交互；4) 代码生成器：用于将融合后的特征转化为可执行的FlexScript代码。整个流程是从输入草图和文本开始，经过编码、融合，最终生成代码。

**关键创新**：该方法最重要的创新点在于它将视觉和语言信息融合到一个统一的模型中，实现了从草图和文本到可执行代码的直接生成。此外，构建的大规模数据集和提出的新评估指标也为该领域的研究提供了重要的资源和工具。与现有方法相比，该方法无需人工编写代码，大大简化了仿真系统的构建过程。

**关键设计**：视觉编码器可以采用卷积神经网络（CNN）或Transformer等结构，文本编码器可以采用预训练的语言模型（如BERT或GPT）。连接器可以使用注意力机制或跨模态Transformer等方法来实现视觉和文本特征的融合。代码生成器可以使用序列到序列（Seq2Seq）模型或Transformer等结构。损失函数可以包括代码生成损失、结构有效性损失和参数匹配损失等。具体参数设置需要根据实验结果进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20387v1/figures/dataset_pipeline.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20387v1/figures/layout_type.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20387v1/figures/level_of_automation.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，提出的VLSM模型在结构有效率（SVR）上接近完美，在参数匹配率（PMR）和执行成功率（ESR）上也取得了显著的成果。通过消融实验，验证了各个模块的有效性，并证明了该模型在生成可执行工业仿真代码方面的优越性。

## 🎯 应用场景

该研究成果可应用于智能制造、物流仓储、交通运输等领域，实现快速构建和修改工业仿真系统，优化生产流程、提高资源利用率、降低运营成本。未来可进一步扩展到更复杂的工业场景，例如智能工厂的自动化设计和优化。

## 📄 摘要（原文）

> We propose a Vision-Language Simulation Model (VLSM) that unifies visual and textual understanding to synthesize executable FlexScript from layout sketches and natural-language prompts, enabling cross-modal reasoning for industrial simulation systems. To support this new paradigm, the study constructs the first large-scale dataset for generative digital twins, comprising over 120,000 prompt-sketch-code triplets that enable multimodal learning between textual descriptions, spatial structures, and simulation logic. In parallel, three novel evaluation metrics, Structural Validity Rate (SVR), Parameter Match Rate (PMR), and Execution Success Rate (ESR), are proposed specifically for this task to comprehensively evaluate structural integrity, parameter fidelity, and simulator executability. Through systematic ablation across vision encoders, connectors, and code-pretrained language backbones, the proposed models achieve near-perfect structural accuracy and high execution robustness. This work establishes a foundation for generative digital twins that integrate visual reasoning and language understanding into executable industrial simulation systems.

