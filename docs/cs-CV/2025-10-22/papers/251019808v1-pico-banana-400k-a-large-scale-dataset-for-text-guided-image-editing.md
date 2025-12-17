---
layout: default
title: Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing
---

# Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.19808" target="_blank" class="toolbar-btn">arXiv: 2510.19808v1</a>
    <a href="https://arxiv.org/pdf/2510.19808.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.19808v1" 
            onclick="toggleFavorite(this, '2510.19808v1', 'Pico-Banana-400K: A Large-Scale Dataset for Text-Guided Image Editing')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yusu Qian, Eli Bocek-Rivele, Liangchen Song, Jialing Tong, Yinfei Yang, Jiasen Lu, Wenze Hu, Zhe Gan

**分类**: cs.CV, cs.CL, cs.LG

**发布日期**: 2025-10-22

---

## 💡 一句话要点

**提出Pico-Banana-400K大规模数据集，促进文本引导图像编辑研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本引导图像编辑` `大规模数据集` `多模态学习` `图像生成` `数据质量评估`

## 📋 核心要点

1. 现有文本引导图像编辑研究缺乏大规模、高质量的真实图像数据集，限制了模型训练和泛化能力。
2. Pico-Banana-400K利用Nano-Banana生成编辑对，并采用细粒度分类和MLLM评分确保数据质量和多样性。
3. 数据集包含多轮编辑、偏好学习和指令重写子集，支持复杂编辑场景的研究和模型能力提升。

## 📝 摘要（中文）

多模态模型的最新进展展示了卓越的文本引导图像编辑能力，例如GPT-4o和Nano-Banana等系统树立了新的基准。然而，由于缺乏基于真实图像构建的大规模、高质量和开放访问的数据集，研究界的进展仍然受到限制。我们推出了Pico-Banana-400K，一个包含40万张图像的综合数据集，用于基于指令的图像编辑。我们的数据集通过利用Nano-Banana从OpenImages集合中的真实照片生成多样化的编辑对来构建。Pico-Banana-400K与以往的合成数据集的区别在于我们系统性的质量和多样性方法。我们采用细粒度的图像编辑分类法，以确保全面覆盖编辑类型，同时通过基于MLLM的质量评分和仔细的策展来保持精确的内容保留和指令忠实性。除了单轮编辑之外，Pico-Banana-400K还支持对复杂编辑场景的研究。该数据集包括三个专门的子集：（1）一个72K示例的多轮集合，用于研究连续修改中的顺序编辑、推理和规划；（2）一个56K示例的偏好子集，用于对齐研究和奖励模型训练；（3）配对的长短编辑指令，用于开发指令重写和总结能力。通过提供这种大规模、高质量和任务丰富的资源，Pico-Banana-400K为训练和基准测试下一代文本引导图像编辑模型奠定了坚实的基础。

## 🔬 方法详解

**问题定义**：现有文本引导图像编辑模型依赖于合成数据或小规模真实数据，难以充分学习真实图像的复杂性和多样性，导致编辑效果不佳或泛化能力不足。缺乏高质量、大规模的真实图像编辑数据集是制约该领域发展的关键瓶颈。

**核心思路**：利用现有的图像编辑模型（Nano-Banana）作为数据生成器，从大规模真实图像数据集（OpenImages）中自动生成编辑对。通过精细的编辑类型分类、基于多模态大语言模型的质量评估和人工筛选，确保生成数据的质量、多样性和指令忠实性。

**技术框架**：Pico-Banana-400K数据集构建流程主要包括以下几个阶段：1) 从OpenImages数据集中选择真实图像；2) 利用Nano-Banana模型生成图像编辑对，包括原始图像和编辑后的图像，以及对应的文本指令；3) 对生成的编辑对进行质量评估，包括内容保留度、指令忠实度等指标，采用基于MLLM的自动评分和人工筛选相结合的方式；4) 根据编辑类型进行分类，确保数据集的多样性；5) 构建三个专门的子集：多轮编辑、偏好学习和指令重写。

**关键创新**：该数据集的关键创新在于其大规模、高质量和多样性。与以往的合成数据集相比，Pico-Banana-400K基于真实图像构建，更贴近实际应用场景。同时，通过精细的质量评估和编辑类型分类，确保了数据的质量和多样性。此外，数据集还包含了多个专门的子集，支持对复杂编辑场景的研究。

**关键设计**：在数据生成阶段，使用了Nano-Banana模型，该模型具有较强的图像编辑能力。在质量评估阶段，使用了基于MLLM的自动评分方法，该方法可以有效地评估图像编辑的质量。在数据集构建过程中，采用了精细的编辑类型分类，包括颜色调整、形状修改、内容添加/删除等，确保数据集的多样性。

## 📊 实验亮点

Pico-Banana-400K包含40万张图像，是目前最大的文本引导图像编辑数据集之一。通过MLLM评估和人工筛选，确保了数据的高质量。数据集包含多轮编辑、偏好学习和指令重写等子集，支持多种研究方向。该数据集为训练和评估下一代文本引导图像编辑模型提供了坚实的基础。

## 🎯 应用场景

Pico-Banana-400K数据集可广泛应用于训练和评估文本引导图像编辑模型，提升模型在真实场景下的编辑效果和泛化能力。该数据集还可用于研究多轮编辑、偏好学习和指令重写等复杂任务，推动图像编辑领域的发展。此外，该数据集可应用于图像生成、图像修复、图像增强等相关领域。

## 📄 摘要（原文）

> Recent advances in multimodal models have demonstrated remarkable text-guided image editing capabilities, with systems like GPT-4o and Nano-Banana setting new benchmarks. However, the research community's progress remains constrained by the absence of large-scale, high-quality, and openly accessible datasets built from real images. We introduce Pico-Banana-400K, a comprehensive 400K-image dataset for instruction-based image editing. Our dataset is constructed by leveraging Nano-Banana to generate diverse edit pairs from real photographs in the OpenImages collection. What distinguishes Pico-Banana-400K from previous synthetic datasets is our systematic approach to quality and diversity. We employ a fine-grained image editing taxonomy to ensure comprehensive coverage of edit types while maintaining precise content preservation and instruction faithfulness through MLLM-based quality scoring and careful curation. Beyond single turn editing, Pico-Banana-400K enables research into complex editing scenarios. The dataset includes three specialized subsets: (1) a 72K-example multi-turn collection for studying sequential editing, reasoning, and planning across consecutive modifications; (2) a 56K-example preference subset for alignment research and reward model training; and (3) paired long-short editing instructions for developing instruction rewriting and summarization capabilities. By providing this large-scale, high-quality, and task-rich resource, Pico-Banana-400K establishes a robust foundation for training and benchmarking the next generation of text-guided image editing models.

