---
layout: default
title: SutureBot: A Precision Framework & Benchmark For Autonomous End-to-End Suturing
---

# SutureBot: A Precision Framework & Benchmark For Autonomous End-to-End Suturing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.20965" class="toolbar-btn" target="_blank">📄 arXiv: 2510.20965v1</a>
  <a href="https://arxiv.org/pdf/2510.20965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20965v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.20965v1', 'SutureBot: A Precision Framework & Benchmark For Autonomous End-to-End Suturing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jesse Haworth, Juo-Tung Chen, Nigel Nelson, Ji Woong Kim, Masoud Moghani, Chelsea Finn, Axel Krieger

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-23

**备注**: 10 pages, 5 figures, 4 tables, NeurIPS 2025

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/jchen396)

---

## 💡 一句话要点

**SutureBot：用于自主端到端缝合的精准框架与基准测试**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `机器人缝合` `自主操作` `目标条件学习` `视觉-语言-动作模型` `达芬奇研究套件`

## 📋 核心要点

1. 现有机器人缝合方法在端到端自主性方面存在挑战，尤其是在物理硬件上的完全自主流程。
2. 论文提出了一种以目标为条件的框架，显式优化插入点精度，以提高缝合的准确性。
3. 通过在dVRK上构建SutureBot基准，并发布包含1890个演示的数据集，促进了可重复的评估和开发。

## 📝 摘要（中文）

机器人缝合是一项典型的长时程灵巧操作任务，需要协调的持针、精确的组织穿透和牢固的结扎。尽管在端到端自主性方面做出了诸多努力，但尚未在物理硬件上演示完全自主的缝合流程。我们推出了SutureBot：一个在达芬奇研究套件（dVRK）上的自主缝合基准，涵盖了持针、组织插入和结扎。为了确保可重复性，我们发布了一个包含1890个缝合演示的高保真数据集。此外，我们提出了一个以目标为条件的框架，该框架显式地优化了插入点精度，与仅任务基线相比，目标精度提高了59%-74%。为了将此任务确立为灵巧模仿学习的基准，我们评估了最先进的视觉-语言-动作（VLA）模型，包括$π_0$、GR00T N1、OpenVLA-OFT和多任务ACT，每个模型都通过高级任务预测策略进行了增强。自主缝合是实现手术机器人自主性的一个关键里程碑。这些贡献支持对端到端缝合所需的、以精度为中心的长时程灵巧操作策略进行可重复的评估和开发。数据集可在以下网址获得：https://huggingface.co/datasets/jchen396/suturebot

## 🔬 方法详解

**问题定义**：论文旨在解决机器人自主缝合中精度不足的问题，特别是在长时程操作中，如何实现端到端的自主缝合，包括持针、组织穿透和结扎等步骤。现有方法难以在真实物理环境中达到足够的精度和鲁棒性，限制了其在实际手术中的应用。

**核心思路**：论文的核心思路是以目标为条件，显式地优化插入点精度。通过预测和优化缝合针的插入位置，提高缝合的准确性和可靠性。这种方法将缝合任务分解为多个子任务，并针对每个子任务进行优化，从而实现更精确的控制。

**技术框架**：SutureBot框架主要包含以下几个模块：1) 数据采集模块，用于收集dVRK上的缝合演示数据；2) 目标条件策略模块，用于预测和优化插入点；3) 视觉-语言-动作（VLA）模型，用于学习缝合策略；4) 任务预测策略模块，用于增强VLA模型。整体流程是从数据集中学习缝合策略，然后使用目标条件策略优化插入点，最后通过VLA模型执行缝合操作。

**关键创新**：论文最重要的技术创新点在于提出了目标条件策略，显式地优化插入点精度。与传统的仅任务学习方法相比，该方法能够更有效地学习缝合策略，并提高缝合的准确性。此外，论文还构建了一个高保真数据集，为机器人缝合的研究提供了重要的资源。

**关键设计**：目标条件策略的关键设计在于使用一个神经网络来预测插入点，并使用一个损失函数来优化插入点的位置。损失函数包括一个目标损失和一个正则化损失，目标损失用于衡量预测的插入点与目标插入点之间的距离，正则化损失用于防止插入点过于偏离。VLA模型使用了Transformer架构，并结合了视觉、语言和动作信息。

## 📊 实验亮点

实验结果表明，论文提出的目标条件框架在插入点精度方面比仅任务基线提高了59%-74%。通过在SutureBot基准上评估多种VLA模型，验证了该框架的有效性。此外，发布的高保真数据集为机器人缝合领域的研究提供了重要的资源，促进了相关技术的发展。

## 🎯 应用场景

该研究成果可应用于微创手术、远程手术等领域，提高手术的精度和效率，降低手术风险。通过自主缝合，可以减轻医生的工作负担，并为缺乏专业医生的地区提供医疗服务。未来，该技术有望应用于更复杂的手术操作，实现手术机器人的完全自主化。

## 📄 摘要（原文）

> Robotic suturing is a prototypical long-horizon dexterous manipulation task, requiring coordinated needle grasping, precise tissue penetration, and secure knot tying. Despite numerous efforts toward end-to-end autonomy, a fully autonomous suturing pipeline has yet to be demonstrated on physical hardware. We introduce SutureBot: an autonomous suturing benchmark on the da Vinci Research Kit (dVRK), spanning needle pickup, tissue insertion, and knot tying. To ensure repeatability, we release a high-fidelity dataset comprising 1,890 suturing demonstrations. Furthermore, we propose a goal-conditioned framework that explicitly optimizes insertion-point precision, improving targeting accuracy by 59\%-74\% over a task-only baseline. To establish this task as a benchmark for dexterous imitation learning, we evaluate state-of-the-art vision-language-action (VLA) models, including $π_0$, GR00T N1, OpenVLA-OFT, and multitask ACT, each augmented with a high-level task-prediction policy. Autonomous suturing is a key milestone toward achieving robotic autonomy in surgery. These contributions support reproducible evaluation and development of precision-focused, long-horizon dexterous manipulation policies necessary for end-to-end suturing. Dataset is available at: https://huggingface.co/datasets/jchen396/suturebot

