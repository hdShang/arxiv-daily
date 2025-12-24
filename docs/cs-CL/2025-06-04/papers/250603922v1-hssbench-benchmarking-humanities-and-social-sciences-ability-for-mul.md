---
layout: default
title: "HSSBench: Benchmarking Humanities and Social Sciences Ability for Multimodal Large Language Models"
---

# HSSBench: Benchmarking Humanities and Social Sciences Ability for Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03922" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03922v1</a>
  <a href="https://arxiv.org/pdf/2506.03922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03922v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03922v1', 'HSSBench: Benchmarking Humanities and Social Sciences Ability for Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaolu Kang, Junhao Gong, Jiaxu Yan, Wanke Xia, Yian Wang, Ziwen Wang, Huaxuan Ding, Zhuo Cheng, Wenhao Cao, Zhiyuan Feng, Siqi He, Shannan Yan, Junzhe Chen, Xiaomin He, Chaoya Jiang, Wei Ye, Kaidong Yu, Xuelong Li

**分类**: cs.CL, cs.AI, cs.CV

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出HSSBench以评估多模态大语言模型在社会科学与人文学科的能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `人文学科` `社会科学` `评估基准` `跨学科思维` `数据生成管道` `联合国官方语言` `知识整合`

## 📋 核心要点

1. 现有的多模态大语言模型评估基准主要集中于STEM领域，忽视了人文学科和社会科学的独特需求与挑战。
2. 本文提出HSSBench，通过多语言评估人文学科和社会科学任务，结合领域专家与自动化生成样本，填补现有评估的空白。
3. 在HSSBench上对20多种主流MLLMs进行基准测试，结果表明即使是最先进的模型在HSS任务中也面临显著挑战。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在多个领域展现出显著潜力。然而，现有的评估基准主要集中于STEM学科的知识和推理，忽视了人文学科和社会科学（HSS）的独特需求。HSS领域的任务需要更为横向的跨学科思维和知识的深度整合。为此，本文提出了HSSBench，一个专门评估MLLMs在HSS任务上能力的基准，涵盖联合国六种官方语言，并引入了一种新颖的数据生成管道，结合领域专家与自动化代理生成和迭代优化样本。HSSBench包含超过13,000个精心设计的样本，涵盖六个关键类别，实验显示即使是最先进的模型在该基准上也面临显著挑战。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大语言模型在评估人文学科和社会科学能力时的不足，现有方法主要关注STEM领域，缺乏对HSS领域的适应性评估。

**核心思路**：HSSBench的核心思路是创建一个专门针对HSS任务的评估基准，强调跨学科的知识整合与抽象概念的视觉表现连接，满足HSS领域的独特需求。

**技术框架**：HSSBench的整体架构包括数据生成管道、样本设计和多语言支持。数据生成管道由领域专家与自动化代理协作生成样本，确保样本的多样性和质量。

**关键创新**：HSSBench的最大创新在于其专注于HSS领域的评估，填补了现有基准的空白，并通过多语言支持提升了评估的广泛性和适用性。

**关键设计**：在样本设计中，采用了多种类别的任务，确保覆盖HSS领域的广泛主题，且每个样本经过多轮迭代优化，以提高其有效性和挑战性。实验中使用的评估指标也经过精心设计，以准确反映模型在HSS任务中的表现。

## 📊 实验亮点

在HSSBench上对20多种主流多模态大语言模型进行评估，结果显示即使是最先进的模型在HSS任务中也面临显著挑战，表明该基准的有效性和必要性。实验结果显示，模型在HSS任务上的表现普遍低于预期，强调了进一步研究的必要性。

## 🎯 应用场景

HSSBench的研究成果可广泛应用于教育、社会科学研究和人工智能领域，特别是在多模态学习和跨学科研究中。它为提升多模态大语言模型在HSS领域的应用能力提供了基础，推动相关技术的发展与应用。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated significant potential to advance a broad range of domains. However, current benchmarks for evaluating MLLMs primarily emphasize general knowledge and vertical step-by-step reasoning typical of STEM disciplines, while overlooking the distinct needs and potential of the Humanities and Social Sciences (HSS). Tasks in the HSS domain require more horizontal, interdisciplinary thinking and a deep integration of knowledge across related fields, which presents unique challenges for MLLMs, particularly in linking abstract concepts with corresponding visual representations. Addressing this gap, we present HSSBench, a dedicated benchmark designed to assess the capabilities of MLLMs on HSS tasks in multiple languages, including the six official languages of the United Nations. We also introduce a novel data generation pipeline tailored for HSS scenarios, in which multiple domain experts and automated agents collaborate to generate and iteratively refine each sample. HSSBench contains over 13,000 meticulously designed samples, covering six key categories. We benchmark more than 20 mainstream MLLMs on HSSBench and demonstrate that it poses significant challenges even for state-of-the-art models. We hope that this benchmark will inspire further research into enhancing the cross-disciplinary reasoning abilities of MLLMs, especially their capacity to internalize and connect knowledge across fields.

