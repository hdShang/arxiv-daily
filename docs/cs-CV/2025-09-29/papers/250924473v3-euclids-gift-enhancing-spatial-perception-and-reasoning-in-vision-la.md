---
layout: default
title: "Euclid's Gift: Enhancing Spatial Perception and Reasoning in Vision-Language Models via Geometric Surrogate Tasks"
---

# Euclid's Gift: Enhancing Spatial Perception and Reasoning in Vision-Language Models via Geometric Surrogate Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24473" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24473v3</a>
  <a href="https://arxiv.org/pdf/2509.24473.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24473v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24473v3', 'Euclid\'s Gift: Enhancing Spatial Perception and Reasoning in Vision-Language Models via Geometric Surrogate Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shijie Lian, Changti Wu, Laurence Tianruo Yang, Hang Yuan, Bin Yu, Lei Zhang, Kai Chen

**分类**: cs.CV, cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-29 (更新: 2025-11-19)

**🔗 代码/项目**: [PROJECT_PAGE](https://zgca-ai4edu.github.io/Euclids_Gift)

---

## 💡 一句话要点

**提出Euclid30K数据集并微调视觉语言模型，显著提升其空间感知与推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `空间推理` `几何学习` `多模态学习` `代理任务`

## 📋 核心要点

1. 多模态大语言模型在空间智能方面存在不足，难以进行形状变换、关系推理等。
2. 将欧几里得几何问题求解作为代理任务，通过构建Euclid30K数据集并进行微调，提升模型空间感知能力。
3. 实验表明，该方法在多个空间推理基准测试中取得了显著的零样本性能提升，验证了其有效性。

## 📝 摘要（中文）

空间智能，包括形状可视化、物体旋转、关系位置判断和数量估计等能力，对多模态大型语言模型（MLLMs）而言仍然是一个关键挑战。为了弥补这一差距，本文提出将欧几里得几何问题求解作为代理任务。具体而言，作者构建了一个名为Euclid30K的多模态数据集，包含约3万个平面和立体几何问题。此外，为了使模型能够学习和应用欧几里得原理，作者使用Group Relative Policy Optimization (GRPO) 对来自Qwen2.5VL、Qwen3VL和RoboBrain2.0系列的七个模型变体（参数范围3-72B）进行了微调，从而激发模型识别形状、计数、关联实体，并使用欧几里得原理执行多步演绎推理。实验表明，由此产生的模型在四个空间推理基准测试（Super-CLEVR、Omni3DBench、VSI-Bench和MindCube）上实现了显著的零样本增益，而无需任何特定于任务的调整。值得注意的是，在Euclid30K上训练后，VSI-Bench的平均准确率从36.6%提高到41.8%（+5.2%），MindCube的平均准确率从31.4%提高到38.1%（+6.7%）。据我们所知，这是第一个系统性研究表明，以几何为中心的微调可以赋予视觉语言模型广泛可迁移的空间技能。

## 🔬 方法详解

**问题定义**：现有的多模态大语言模型在空间感知和推理方面表现不足，难以有效解决涉及几何形状、空间关系等问题。现有方法缺乏对几何知识的有效利用，导致模型在处理空间相关任务时泛化能力较差。

**核心思路**：本文的核心思路是将欧几里得几何问题求解作为一种代理任务，通过让模型学习解决几何问题来提升其空间感知和推理能力。这种方法基于几何知识是空间智能的基础，通过学习几何原理可以提升模型对空间关系的理解和推理能力。

**技术框架**：整体框架包括数据构建和模型微调两个主要阶段。首先，构建包含3万个平面和立体几何问题的Euclid30K数据集。然后，使用Group Relative Policy Optimization (GRPO) 对Qwen2.5VL、Qwen3VL和RoboBrain2.0等模型进行微调，使其学习几何知识并提升空间推理能力。

**关键创新**：最重要的创新点在于将几何问题求解作为视觉语言模型的代理任务，通过学习几何知识来提升模型的空间智能。与以往直接在特定空间推理任务上进行训练的方法不同，本文的方法更注重学习通用的几何原理，从而提升模型的泛化能力。

**关键设计**：Euclid30K数据集包含多种类型的几何问题，涵盖平面和立体几何，旨在全面提升模型的几何知识。GRPO算法用于微调模型，鼓励模型学习识别形状、计数和关联实体，并使用欧几里得原理进行多步演绎推理。具体的参数设置和损失函数细节在论文中未详细说明，属于未知信息。

## 📊 实验亮点

通过在Euclid30K数据集上进行微调，模型在VSI-Bench上的平均准确率提升了5.2%（从36.6%到41.8%），在MindCube上的平均准确率提升了6.7%（从31.4%到38.1%）。这些结果表明，该方法能够显著提升视觉语言模型的空间推理能力，且无需针对特定任务进行额外调整。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、三维场景理解、虚拟现实等领域。通过提升视觉语言模型的空间感知和推理能力，可以使机器人在复杂环境中更好地理解和交互，实现更智能化的应用。

## 📄 摘要（原文）

> Spatial intelligence spans a rich suite of abilities, including visualising and transforming shapes, mentally rotating objects, judging relational positions and containment, and estimating numerosity. However, it still remains a critical unresolved challenge for Multimodal Large Language Models (MLLMs). To fill this gap, we propose to treat Euclidean geometry problem-solving as a surrogate task. Specifically, we meticulously constructed a curated multimodal dataset, called Euclid30K, comprising approximately 30K plane and solid geometry problems. Furthermore, to enable the model to learn and apply Euclidean principles from these geometry problems, we fine-tuned seven model variants (spanning 3--72B parameters) from the Qwen2.5VL, Qwen3VL, and RoboBrain2.0 families using Group Relative Policy Optimization (GRPO), inspiring the models to identify shapes, count, and relate entities, and perform multi-step deductive reasoning using Euclidean principles. Our experiments demonstrate that the resulting models achieve substantial zero-shot gains across four spatial reasoning benchmarks (Super-CLEVR, Omni3DBench, VSI-Bench, and MindCube) without any task-specific adaptations. Notably, after training on the Euclid30K, the mean VSI-Bench accuracy rose from 36.6\% to 41.8\% (+5.2\%), and the mean MindCube accuracy rose from 31.4\% to 38.1\% (+6.7\%). To our knowledge, this is the first systematic study showing that geometry-centric fine-tuning can confer vision-language models with broadly transferable spatial skills. Code and Euclid30K dataset can be found in \href{https://zgca-ai4edu.github.io/Euclids_Gift}{this}.

