---
layout: default
title: "SoM-1K: A Thousand-Problem Benchmark Dataset for Strength of Materials"
---

# SoM-1K: A Thousand-Problem Benchmark Dataset for Strength of Materials

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21079" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21079v1</a>
  <a href="https://arxiv.org/pdf/2509.21079.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21079v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21079v1', 'SoM-1K: A Thousand-Problem Benchmark Dataset for Strength of Materials')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qixin Wan, Zilong Wang, Jingwen Zhou, Wanting Wang, Ziheng Geng, Jiachen Liu, Ran Cao, Minghui Cheng, Lu Cheng

**分类**: cs.CL

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**提出SoM-1K材料力学基准数据集，评估并提升多模态工程问题中大模型的性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `材料力学` `基准数据集` `多模态学习` `图像描述` `大型语言模型`

## 📋 核心要点

1. 现有基础模型在复杂、多模态工程问题上的性能仍有待探索，缺乏专门的评估基准。
2. 提出SoM-1K数据集和DoI提示策略，利用专家生成的图像描述增强模型对视觉信息的理解。
3. 实验表明，现有模型在SoM问题上表现不佳，DoI提示能有效提升LLM的性能，优于直接使用图像的VLM。

## 📝 摘要（中文）

本文提出了SoM-1K，首个大规模多模态基准数据集，用于评估基础模型在材料力学（SoM）问题上的性能。该数据集包含1065个带标注的SoM问题，通过包含文本问题描述和示意图来模拟真实的工程任务。针对当前基础模型在理解复杂视觉信息方面的局限性，提出了一种名为图像描述（DoI）的新型提示策略，该策略提供由专家生成的对视觉图的严格文本描述作为上下文。评估了八个具有代表性的基础模型，包括大型语言模型（LLM）和视觉语言模型（VLM）。结果表明，当前的基础模型在这些工程问题上表现不佳，性能最佳的模型仅达到56.6%的准确率。有趣的是，当提供DoI时，LLM通常优于提供视觉图的VLM。详细的错误分析表明，DoI在减轻视觉误解错误方面起着关键作用，这表明对于当前的基础模型，准确的基于文本的描述可能比直接图像输入更有效。这项工作为工程AI建立了一个严格的基准，并强调了在基础模型中开发更强大的多模态推理能力（尤其是在科学和工程环境中）的关键需求。

## 🔬 方法详解

**问题定义**：论文旨在解决基础模型在材料力学（SoM）问题上的性能评估问题。现有方法缺乏专门针对工程领域、包含多模态信息的基准数据集，导致无法有效评估和提升模型在复杂工程问题上的能力。现有模型难以准确理解复杂的视觉信息，容易产生误解。

**核心思路**：论文的核心思路是构建一个大规模、多模态的SoM数据集，并提出一种新型的提示策略（DoI）来弥补模型在视觉理解方面的不足。通过提供专家生成的图像描述，将视觉信息转化为文本信息，从而帮助模型更好地理解问题。

**技术框架**：整体框架包含两个主要部分：SoM-1K数据集的构建和DoI提示策略的应用。SoM-1K数据集包含文本问题描述和示意图，并进行了人工标注。DoI提示策略则是在输入模型时，除了文本问题描述外，还提供专家生成的示意图文本描述。然后，使用各种LLM和VLM模型进行评估，并分析结果。

**关键创新**：论文的关键创新在于：1) 构建了首个大规模多模态SoM基准数据集SoM-1K；2) 提出了DoI提示策略，利用文本描述增强模型对视觉信息的理解，尤其是在模型视觉理解能力不足的情况下，该策略能够有效提升性能。

**关键设计**：DoI提示策略的关键在于生成高质量的图像描述。这些描述需要准确、详细地描述示意图中的关键信息，例如几何形状、材料属性、载荷情况等。论文中使用了专家来生成这些描述，保证了描述的准确性和完整性。此外，在实验中，论文还探索了不同模型的性能，并分析了DoI提示策略对不同模型的影响。

## 📊 实验亮点

实验结果表明，当前基础模型在SoM问题上表现不佳，最佳模型准确率仅为56.6%。但当使用DoI提示策略时，LLM的性能显著提升，甚至优于直接使用图像的VLM。错误分析表明，DoI能有效减轻视觉误解错误，证明了准确的文本描述在多模态工程问题中的重要性。

## 🎯 应用场景

该研究成果可应用于工程教育、智能设计、故障诊断等领域。通过提升AI模型在材料力学问题上的解决能力，可以辅助工程师进行设计优化、提高工作效率，并为自动化工程分析提供技术支持。未来，该研究可扩展到其他工程领域，推动工程AI的发展。

## 📄 摘要（原文）

> Foundation models have shown remarkable capabilities in various domains, but their performance on complex, multimodal engineering problems remains largely unexplored. We introduce SoM-1K, the first large-scale multimodal benchmark dataset dedicated to evaluating foundation models on problems in the strength of materials (SoM). The dataset, which contains 1,065 annotated SoM problems, mirrors real-world engineering tasks by including both textual problem statements and schematic diagrams. Due to the limited capabilities of current foundation models in understanding complicated visual information, we propose a novel prompting strategy called Descriptions of Images (DoI), which provides rigorous expert-generated text descriptions of the visual diagrams as the context. We evaluate eight representative foundation models, including both large language models (LLMs) and vision language models (VLMs). Our results show that current foundation models struggle significantly with these engineering problems, with the best-performing model achieving only 56.6% accuracy. Interestingly, we found that LLMs, when provided with DoI, often outperform VLMs provided with visual diagrams. A detailed error analysis reveals that DoI plays a crucial role in mitigating visual misinterpretation errors, suggesting that accurate text-based descriptions can be more effective than direct image input for current foundation models. This work establishes a rigorous benchmark for engineering AI and highlights a critical need for developing more robust multimodal reasoning capabilities in foundation models, particularly in scientific and engineering contexts.

