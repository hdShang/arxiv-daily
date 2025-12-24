---
layout: default
title: "VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results"
---

# VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09190" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09190v1</a>
  <a href="https://arxiv.org/pdf/2509.09190.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09190v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09190v1', 'VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hanwei Zhu, Haoning Wu, Zicheng Zhang, Lingyu Zhu, Yixuan Li, Peilin Chen, Shiqi Wang, Chris Wei Zhou, Linhan Cao, Wei Sun, Xiangyang Zhu, Weixia Zhang, Yucheng Zhu, Jing Liu, Dandan Zhu, Guangtao Zhai, Xiongkuo Min, Zhichao Zhang, Xinyue Li, Shubo Xu, Anh Dao, Yifan Li, Hongyuan Yu, Jiaojiao Yi, Yiding Tian, Yupeng Wu, Feiran Sun, Lijuan Liao, Song Jiang

**分类**: cs.CV

**发布日期**: 2025-09-11

**备注**: ICCV VQualA Workshop 2025

---

## 💡 一句话要点

**VQualA 2025挑战赛：评估并提升大型多模态模型在视觉质量比较方面的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉质量评估` `大型多模态模型` `视觉质量比较` `基准数据集` `指令调整`

## 📋 核心要点

1. 现有LMM在视觉质量比较方面缺乏细粒度和开放域的评估基准，限制了其在该领域的应用。
2. VQualA 2025挑战赛构建了包含多种视觉质量比较任务的新基准，旨在全面评估LMM的质量判断能力。
3. 挑战赛吸引了约100名参与者，结果表明指令调整的LMM在质量评估方面展现出潜力，但仍有提升空间。

## 📝 摘要（中文）

本文总结了作为ICCV 2025视觉质量评估研讨会一部分的VQualA 2025大型多模态模型视觉质量比较挑战赛。该挑战赛旨在评估和提升最先进的大型多模态模型（LMMs）在执行关于多个图像之间视觉质量差异的开放式和详细推理方面的能力。为此，比赛引入了一个新颖的基准，包含数千个由粗到细粒度的视觉质量比较任务，涵盖单个图像、图像对和多图像组。每个任务都要求模型提供准确的质量判断。比赛强调整体评估协议，包括基于2AFC的二元偏好和多项选择题（MCQs）。大约100名参与者提交了参赛作品，其中五个模型展示了指令调整LMMs在质量评估方面的新兴能力。这项挑战标志着朝着开放域视觉质量推理和比较迈出的重要一步，并为未来可解释和人类对齐的质量评估系统的研究提供了催化剂。

## 🔬 方法详解

**问题定义**：论文旨在解决大型多模态模型（LMMs）在视觉质量比较任务中缺乏有效评估和提升的问题。现有方法在开放域和细粒度视觉质量比较方面存在不足，缺乏统一的基准和评估协议，难以全面衡量LMM的性能。

**核心思路**：论文的核心思路是通过构建一个包含多种视觉质量比较任务的新基准，并设计相应的评估协议，来促进LMM在视觉质量比较方面的研究。该基准涵盖了单张图像、图像对和多张图像组的比较，并要求模型提供准确的质量判断。

**技术框架**：VQualA 2025挑战赛的技术框架主要包括以下几个部分：1) 构建包含数千个视觉质量比较任务的新基准；2) 设计基于2AFC的二元偏好和多项选择题（MCQs）的评估协议；3) 组织比赛，吸引研究人员提交LMM模型进行评估；4) 分析比赛结果，总结LMM在视觉质量比较方面的优势和不足。

**关键创新**：论文的关键创新在于构建了一个新颖的、由粗到细粒度的视觉质量比较基准，该基准涵盖了多种类型的视觉质量比较任务，能够更全面地评估LMM的性能。此外，论文还设计了基于2AFC和MCQs的评估协议，能够更准确地衡量LMM的质量判断能力。

**关键设计**：基准数据集包含单张图像、图像对和多张图像组的比较任务，涵盖了多种视觉质量属性，如清晰度、对比度、色彩等。评估协议采用2AFC和MCQs两种形式，能够从不同角度评估LMM的性能。比赛鼓励参与者使用各种LMM模型，并根据评估结果进行排名。

## 📊 实验亮点

VQualA 2025挑战赛吸引了约100名参与者，提交了多种LMM模型。结果表明，经过指令调整的LMM在视觉质量比较方面展现出潜力，但仍有提升空间。例如，部分模型在2AFC任务中取得了较好的结果，但在MCQs任务中表现相对较弱，表明LMM在细粒度视觉质量推理方面仍存在挑战。

## 🎯 应用场景

该研究成果可应用于图像/视频质量评估、图像增强、图像修复等领域。通过提升LMM在视觉质量比较方面的能力，可以开发更智能的图像处理算法，提高用户体验，并为内容创作和编辑提供更有效的工具。未来，该研究有望推动可解释和人类对齐的质量评估系统的发展。

## 📄 摘要（原文）

> This paper presents a summary of the VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models (LMMs), hosted as part of the ICCV 2025 Workshop on Visual Quality Assessment. The challenge aims to evaluate and enhance the ability of state-of-the-art LMMs to perform open-ended and detailed reasoning about visual quality differences across multiple images. To this end, the competition introduces a novel benchmark comprising thousands of coarse-to-fine grained visual quality comparison tasks, spanning single images, pairs, and multi-image groups. Each task requires models to provide accurate quality judgments. The competition emphasizes holistic evaluation protocols, including 2AFC-based binary preference and multi-choice questions (MCQs). Around 100 participants submitted entries, with five models demonstrating the emerging capabilities of instruction-tuned LMMs on quality assessment. This challenge marks a significant step toward open-domain visual quality reasoning and comparison and serves as a catalyst for future research on interpretable and human-aligned quality evaluation systems.

