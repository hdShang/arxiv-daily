---
layout: default
title: "InterAct: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation"
---

# InterAct: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09555" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09555v1</a>
  <a href="https://arxiv.org/pdf/2509.09555.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09555v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09555v1', 'InterAct: Advancing Large-Scale Versatile 3D Human-Object Interaction Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sirui Xu, Dongting Li, Yucheng Zhang, Xiyan Xu, Qi Long, Ziyin Wang, Yunzhi Lu, Shuchang Dong, Hezi Jiang, Akshat Gupta, Yu-Xiong Wang, Liang-Yan Gui

**分类**: cs.CV

**发布日期**: 2025-09-11

**备注**: CVPR 2025

**🔗 代码/项目**: [GITHUB](https://github.com/wzyabcas/InterAct)

---

## 💡 一句话要点

**InterAct：提出大规模通用3D人-物交互生成数据集与方法**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人-物交互` `3D生成` `数据集` `动作捕捉` `数据增强`

## 📋 核心要点

1. 现有HOI数据集规模小、质量低，存在伪影和标注不足，限制了3D人-物交互生成模型的发展。
2. InterAct通过整合多源数据、优化数据质量和利用接触不变性进行数据增强，构建了大规模高质量的HOI数据集。
3. 论文定义了六个HOI生成任务，并提出了统一的生成模型，在InterAct数据集上取得了SOTA性能，验证了数据集的有效性。

## 📝 摘要（中文）

由于数据集的限制，建模和生成动态3D人-物交互（HOI）仍然具有挑战性。现有的数据集通常缺乏广泛、高质量的运动和标注，并且存在接触穿透、漂浮和不正确的手部运动等伪影。为了解决这些问题，我们推出了InterAct，这是一个大规模的3D HOI基准，具有数据集和方法上的进步。首先，我们整合和标准化了来自不同来源的21.81小时的HOI数据，并用详细的文本注释丰富了它。其次，我们提出了一个统一的优化框架，通过减少伪影和纠正手部运动来提高数据质量。利用接触不变性原则，我们在保持人-物关系的同时引入运动变化，将数据集扩展到30.70小时。第三，我们定义了六个基准测试任务，并开发了一个统一的HOI生成建模视角，实现了最先进的性能。大量的实验验证了我们的数据集作为推进3D人-物交互生成的基础资源的效用。为了支持该领域的持续研究，该数据集可在https://github.com/wzyabcas/InterAct公开获取，并将得到积极维护。

## 🔬 方法详解

**问题定义**：现有3D人-物交互（HOI）数据集规模有限，数据质量不高，存在接触穿透、漂浮等伪影，手部动作不准确，缺乏详细的文本标注。这些问题严重阻碍了HOI生成模型的发展，使其难以学习到真实、自然的交互模式。

**核心思路**：论文的核心思路是构建一个大规模、高质量的HOI数据集，并提出一个统一的生成模型。通过整合多源数据，利用优化框架减少伪影，并利用接触不变性进行数据增强，从而提高数据集的规模和质量。同时，设计一个统一的生成模型，能够处理不同的HOI生成任务。

**技术框架**：InterAct的整体框架包含三个主要部分：数据收集与整合、数据优化与增强、HOI生成模型。首先，从多个来源收集HOI数据，并进行标准化处理。然后，利用优化框架减少伪影，并利用接触不变性进行数据增强。最后，提出了一个统一的HOI生成模型，用于处理不同的HOI生成任务。

**关键创新**：论文的关键创新点在于：1) 构建了一个大规模、高质量的HOI数据集InterAct，解决了现有数据集规模小、质量低的问题。2) 提出了一个统一的优化框架，能够有效减少HOI数据中的伪影。3) 利用接触不变性进行数据增强，在保持人-物关系的同时引入运动变化，进一步扩大了数据集的规模。4) 提出了一个统一的HOI生成模型，能够处理不同的HOI生成任务。

**关键设计**：在数据优化阶段，论文设计了一个基于优化的框架，通过最小化接触穿透、漂浮等伪影的能量函数来提高数据质量。在数据增强阶段，论文利用接触不变性原则，在保持人-物接触关系的同时，对人体运动进行微调，从而生成新的HOI数据。在HOI生成模型中，论文采用Transformer架构，并设计了专门的损失函数来鼓励生成真实、自然的HOI序列。

## 📊 实验亮点

InterAct数据集包含21.81小时的原始HOI数据，经过优化和增强后达到30.70小时。在六个HOI生成任务上，论文提出的统一生成模型均取得了SOTA性能，显著优于现有方法，验证了InterAct数据集的有效性和模型的优越性。具体性能数据在论文中有详细展示。

## 🎯 应用场景

InterAct数据集和相关技术可广泛应用于虚拟现实、增强现实、游戏开发、机器人控制等领域。例如，可以用于生成逼真的人与虚拟物体的交互动画，提高VR/AR体验的沉浸感；可以用于训练机器人学习如何与物体进行交互，从而实现更智能的机器人控制。

## 📄 摘要（原文）

> While large-scale human motion capture datasets have advanced human motion generation, modeling and generating dynamic 3D human-object interactions (HOIs) remain challenging due to dataset limitations. Existing datasets often lack extensive, high-quality motion and annotation and exhibit artifacts such as contact penetration, floating, and incorrect hand motions. To address these issues, we introduce InterAct, a large-scale 3D HOI benchmark featuring dataset and methodological advancements. First, we consolidate and standardize 21.81 hours of HOI data from diverse sources, enriching it with detailed textual annotations. Second, we propose a unified optimization framework to enhance data quality by reducing artifacts and correcting hand motions. Leveraging the principle of contact invariance, we maintain human-object relationships while introducing motion variations, expanding the dataset to 30.70 hours. Third, we define six benchmarking tasks and develop a unified HOI generative modeling perspective, achieving state-of-the-art performance. Extensive experiments validate the utility of our dataset as a foundational resource for advancing 3D human-object interaction generation. To support continued research in this area, the dataset is publicly available at https://github.com/wzyabcas/InterAct, and will be actively maintained.

