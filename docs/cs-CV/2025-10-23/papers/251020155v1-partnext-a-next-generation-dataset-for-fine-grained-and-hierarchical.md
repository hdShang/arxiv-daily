---
layout: default
title: PartNeXt: A Next-Generation Dataset for Fine-Grained and Hierarchical 3D Part Understanding
---

# PartNeXt: A Next-Generation Dataset for Fine-Grained and Hierarchical 3D Part Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20155" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20155v1</a>
  <a href="https://arxiv.org/pdf/2510.20155.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20155v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.20155v1', 'PartNeXt: A Next-Generation Dataset for Fine-Grained and Hierarchical 3D Part Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Penghao Wang, Yiyang He, Xin Lv, Yukai Zhou, Lan Xu, Jingyi Yu, Jiayuan Gu

**分类**: cs.CV

**发布日期**: 2025-10-23

**备注**: NeurIPS 2025 DB Track. Project page: https://authoritywang.github.io/partnext

---

## 💡 一句话要点

**提出PartNeXt数据集，用于细粒度分层3D部件理解，提升模型性能。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D部件理解` `细粒度分割` `分层标注` `纹理模型` `3D问答`

## 📋 核心要点

1. 现有3D部件理解数据集依赖无纹理几何体和专家标注，限制了可扩展性和可用性。
2. PartNeXt数据集提供带纹理的3D模型和细粒度分层部件标签，支持多任务评估。
3. 实验表明，PartNeXt能有效提升部件分割和3D部件中心问答等任务的性能。

## 📝 摘要（中文）

本文提出了PartNeXt，一个用于细粒度分层3D部件理解的新一代数据集。该数据集包含超过23,000个高质量、带纹理的3D模型，并标注了50个类别中细粒度、分层结构的部件标签。现有数据集如PartNet依赖于无纹理几何体和专家标注，限制了其可扩展性和可用性。PartNeXt在两个任务上进行了基准测试：(1) 类无关部件分割，现有方法（如PartField、SAMPart3D）难以处理细粒度和叶子级别的部件；(2) 3D部件中心问答，这是一个针对3D-LLM的新基准，揭示了开放词汇部件 grounding 方面的显著差距。此外，在PartNeXt上训练Point-SAM比在PartNet上训练效果更好，突显了该数据集的卓越质量和多样性。PartNeXt结合了可扩展的标注、纹理感知标签和多任务评估，为结构化3D理解的研究开辟了新途径。

## 🔬 方法详解

**问题定义**：现有3D部件理解数据集，如PartNet，主要依赖于无纹理的几何模型，并且标注过程依赖于专家知识，这限制了数据集的规模和泛化能力。此外，现有方法在处理细粒度和叶子级别的部件分割时表现不佳，并且缺乏针对3D部件的开放词汇 grounding 能力的评估。

**核心思路**：PartNeXt的核心思路是通过引入带纹理的3D模型和可扩展的标注方法，构建一个更大、更细粒度、更具多样性的3D部件理解数据集。同时，设计新的基准测试任务，例如3D部件中心问答，来评估模型在开放词汇环境下的部件理解能力。

**技术框架**：PartNeXt数据集包含超过23,000个3D模型，涵盖50个类别。每个模型都带有细粒度的分层部件标签和纹理信息。数据集被用于评估两个任务：类无关部件分割和3D部件中心问答。研究人员使用现有的部件分割方法（如PartField、SAMPart3D）和大型语言模型（LLM）在PartNeXt上进行实验，并分析其性能。

**关键创新**：PartNeXt的关键创新在于其高质量、带纹理的3D模型和细粒度的分层部件标签。与现有数据集相比，PartNeXt提供了更丰富的视觉信息和更精细的部件划分，这有助于提高模型对3D部件的理解能力。此外，3D部件中心问答任务是一个新的基准，用于评估模型在开放词汇环境下的部件 grounding 能力。

**关键设计**：PartNeXt数据集的标注过程采用了可扩展的方法，具体细节未知。在实验中，研究人员使用了Point-SAM模型，并在PartNeXt上进行了训练，以验证数据集的有效性。具体的损失函数和网络结构等技术细节在论文中可能有所描述，但摘要中未提及。

## 📊 实验亮点

实验结果表明，现有方法在PartNeXt数据集上进行类无关部件分割时，难以处理细粒度和叶子级别的部件。在3D部件中心问答任务中，3D-LLM在开放词汇部件 grounding 方面存在显著差距。此外，在PartNeXt上训练Point-SAM比在PartNet上训练效果更好，验证了PartNeXt数据集的优越性。

## 🎯 应用场景

PartNeXt数据集可广泛应用于计算机视觉、机器人和图形学等领域。例如，可用于训练机器人进行精细操作，提升3D场景理解能力，改进CAD模型检索和编辑，以及开发更智能的3D问答系统。该数据集有望推动相关领域的研究进展。

## 📄 摘要（原文）

> Understanding objects at the level of their constituent parts is fundamental to advancing computer vision, graphics, and robotics. While datasets like PartNet have driven progress in 3D part understanding, their reliance on untextured geometries and expert-dependent annotation limits scalability and usability. We introduce PartNeXt, a next-generation dataset addressing these gaps with over 23,000 high-quality, textured 3D models annotated with fine-grained, hierarchical part labels across 50 categories. We benchmark PartNeXt on two tasks: (1) class-agnostic part segmentation, where state-of-the-art methods (e.g., PartField, SAMPart3D) struggle with fine-grained and leaf-level parts, and (2) 3D part-centric question answering, a new benchmark for 3D-LLMs that reveals significant gaps in open-vocabulary part grounding. Additionally, training Point-SAM on PartNeXt yields substantial gains over PartNet, underscoring the dataset's superior quality and diversity. By combining scalable annotation, texture-aware labels, and multi-task evaluation, PartNeXt opens new avenues for research in structured 3D understanding.

