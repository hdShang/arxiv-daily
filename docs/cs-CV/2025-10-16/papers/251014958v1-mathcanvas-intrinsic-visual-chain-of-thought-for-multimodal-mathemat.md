---
layout: default
title: MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning
---

# MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.14958" target="_blank" class="toolbar-btn">arXiv: 2510.14958v1</a>
    <a href="https://arxiv.org/pdf/2510.14958.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14958v1" 
            onclick="toggleFavorite(this, '2510.14958v1', 'MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Weikang Shi, Aldrich Yu, Rongyao Fang, Houxing Ren, Ke Wang, Aojun Zhou, Changyao Tian, Xinyu Fu, Yuxuan Hu, Zimu Lu, Linjiang Huang, Si Liu, Rui Liu, Hongsheng Li

**分类**: cs.CV, cs.CL

**发布日期**: 2025-10-16

**备注**: Project Page: https://mathcanvas.github.io/

---

## 💡 一句话要点

**MathCanvas：用于多模态数学推理的内在视觉思维链**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉思维链` `多模态推理` `数学问题求解` `图文生成` `大型多模态模型`

## 📋 核心要点

1. 现有VCoT方法在数学问题中受限于外部工具，难以生成高质量、适时图表，阻碍复杂问题求解。
2. MathCanvas框架通过预训练和微调，使LMM具备内在VCoT能力，学会何时及如何利用视觉辅助进行数学推理。
3. BAGEL-Canvas模型在MathCanvas-Bench上相比LMM基线提升86%，并在其他数学基准上表现出良好的泛化能力。

## 📝 摘要（中文）

大型语言模型(LLMs)在文本推理方面表现出色，但在几何等本质上依赖视觉辅助的数学领域却表现不佳。现有的视觉思维链(VCoT)方法通常受到外部工具的限制，或者无法生成复杂问题求解所需的高保真、策略性定时的图表。为了弥合这一差距，我们引入了MathCanvas，这是一个全面的框架，旨在赋予统一的大型多模态模型(LMMs)内在的数学VCoT能力。我们的方法包括两个阶段。首先，一个视觉操作阶段，在一个新的1520万对语料库上预训练模型，包括1000万个标题到图表的配对(MathCanvas-Imagen)和520万个逐步编辑轨迹(MathCanvas-Edit)，以掌握图表的生成和编辑。其次，一个策略性视觉辅助推理阶段，在MathCanvas-Instruct上微调模型，这是一个新的21.9万个例子的数据集，包含交错的视觉-文本推理路径，教会它何时以及如何利用视觉辅助。为了方便严格的评估，我们引入了MathCanvas-Bench，一个具有3K问题的具有挑战性的基准，要求模型生成交错的视觉-文本解决方案。我们的模型BAGEL-Canvas，在该框架下训练，在MathCanvas-Bench上实现了比强大的LMM基线86%的相对改进，展示了对其他公共数学基准的良好泛化能力。我们的工作提供了一个完整的工具包框架、数据集和基准，以解锁LMM中复杂、类人的视觉辅助推理。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理需要视觉辅助的数学问题，例如几何问题时，表现不佳。现有的视觉思维链方法要么依赖于外部工具，要么无法生成高质量的、策略性定时的图表，这限制了它们解决复杂问题的能力。因此，需要一种能够让模型自主生成和利用视觉信息进行推理的方法。

**核心思路**：MathCanvas的核心思路是赋予大型多模态模型（LMMs）内在的视觉思维链（VCoT）能力。通过预训练和微调，模型能够学习生成、编辑和利用图表进行数学推理，从而克服现有方法对外部工具的依赖和图表质量的限制。这种内在的VCoT能力使得模型能够像人类一样，在解决数学问题时自然地利用视觉信息。

**技术框架**：MathCanvas框架包含两个主要阶段：视觉操作阶段和策略性视觉辅助推理阶段。在视觉操作阶段，模型首先在一个大规模的图文配对数据集（MathCanvas-Imagen）和图表编辑轨迹数据集（MathCanvas-Edit）上进行预训练，以学习图表的生成和编辑能力。然后，在策略性视觉辅助推理阶段，模型在一个包含交错的视觉-文本推理路径的数据集（MathCanvas-Instruct）上进行微调，以学习何时以及如何利用视觉辅助进行推理。为了评估模型的性能，作者还构建了一个新的基准测试集（MathCanvas-Bench）。

**关键创新**：MathCanvas的关键创新在于它赋予了LMM内在的VCoT能力，使其能够自主生成和利用图表进行数学推理。与现有方法相比，MathCanvas不需要依赖外部工具，并且能够生成高质量的、策略性定时的图表。此外，MathCanvas还提出了一个完整的框架，包括数据集、训练方法和评估基准，为研究人员提供了一个全面的工具包。

**关键设计**：MathCanvas-Imagen包含10M caption-to-diagram pairs，用于预训练模型生成图表的能力。MathCanvas-Edit包含5.2M step-by-step editing trajectories，用于预训练模型编辑图表的能力。MathCanvas-Instruct包含219K interleaved visual-textual reasoning paths，用于微调模型学习何时以及如何利用视觉辅助进行推理。BAGEL-Canvas是基于该框架训练的模型，具体参数设置和网络结构细节在论文中未明确给出，属于未知信息。

## 📊 实验亮点

BAGEL-Canvas模型在MathCanvas-Bench基准测试集上取得了显著的性能提升，相比于强大的LMM基线，实现了86%的相对改进。这表明MathCanvas框架能够有效地提升LMM在视觉辅助数学推理方面的能力，并且具有良好的泛化性能，能够在其他公开的数学基准测试集上表现出色。

## 🎯 应用场景

MathCanvas的研究成果可应用于教育领域，例如开发智能辅导系统，帮助学生理解和解决几何问题。此外，该技术还可用于科学研究、工程设计等领域，辅助专业人员进行复杂的视觉推理和问题求解。未来，该技术有望扩展到其他需要视觉辅助的推理任务中。

## 📄 摘要（原文）

> While Large Language Models (LLMs) have excelled in textual reasoning, they struggle with mathematical domains like geometry that intrinsically rely on visual aids. Existing approaches to Visual Chain-of-Thought (VCoT) are often limited by rigid external tools or fail to generate the high-fidelity, strategically-timed diagrams necessary for complex problem-solving. To bridge this gap, we introduce MathCanvas, a comprehensive framework designed to endow unified Large Multimodal Models (LMMs) with intrinsic VCoT capabilities for mathematics. Our approach consists of two phases. First, a Visual Manipulation stage pre-trains the model on a novel 15.2M-pair corpus, comprising 10M caption-to-diagram pairs (MathCanvas-Imagen) and 5.2M step-by-step editing trajectories (MathCanvas-Edit), to master diagram generation and editing. Second, a Strategic Visual-Aided Reasoning stage fine-tunes the model on MathCanvas-Instruct, a new 219K-example dataset of interleaved visual-textual reasoning paths, teaching it when and how to leverage visual aids. To facilitate rigorous evaluation, we introduce MathCanvas-Bench, a challenging benchmark with 3K problems that require models to produce interleaved visual-textual solutions. Our model, BAGEL-Canvas, trained under this framework, achieves an 86% relative improvement over strong LMM baselines on MathCanvas-Bench, demonstrating excellent generalization to other public math benchmarks. Our work provides a complete toolkit-framework, datasets, and benchmark-to unlock complex, human-like visual-aided reasoning in LMMs. Project Page: https://mathcanvas.github.io/

