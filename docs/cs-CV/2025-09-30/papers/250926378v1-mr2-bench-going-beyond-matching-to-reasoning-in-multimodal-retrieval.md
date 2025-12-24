---
layout: default
title: "MR$^2$-Bench: Going Beyond Matching to Reasoning in Multimodal Retrieval"
---

# MR$^2$-Bench: Going Beyond Matching to Reasoning in Multimodal Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26378" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26378v1</a>
  <a href="https://arxiv.org/pdf/2509.26378.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26378v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26378v1', 'MR$^2$-Bench: Going Beyond Matching to Reasoning in Multimodal Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Zhou, Ze Liu, Lei Xiong, Jin-Ge Yao, Yueze Wang, Shitao Xiao, Fenfen Lin, Miguel Hu Chen, Zhicheng Dou, Siqi Bao, Defu Lian, Yongping Xiong, Zheng Liu

**分类**: cs.IR, cs.CV

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/VectorSpaceLab/MR2-Bench)

---

## 💡 一句话要点

**提出MR$^2$-Bench，一个面向多模态检索推理能力的综合性评测基准。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态检索` `推理能力` `评测基准` `数据集` `视觉推理`

## 📋 核心要点

1. 现有基准侧重于浅层语义匹配，无法有效评估模型在多模态检索中进行深层推理的能力。
2. MR$^2$-Bench通过推理驱动的任务、多样化的多模态数据和复杂的查询文档，全面评估模型的推理能力。
3. 实验表明，现有SOTA模型在MR$^2$-Bench上的性能显著下降，突显了该基准的挑战性和进一步研究的必要性。

## 📝 摘要（中文）

多模态检索正成为现代人工智能应用的关键组成部分，但其评估滞后于更真实和更具挑战性的场景需求。现有的基准主要探测表面语义对应（例如，对象-文本匹配），而未能评估捕获视觉和文本信息之间复杂关系所需的更深层次的推理能力。为了解决这一差距，我们引入了MR$^2$-Bench，这是一个推理密集型的多模态检索基准。MR$^2$-Bench 具有以下关键价值：1) 所有任务都是推理驱动的，超越了浅层匹配，有效地评估了模型进行逻辑、空间和因果推理的能力；2) 它具有多样化的多模态数据，例如自然图像、图表和视觉谜题，从而能够跨内容类型进行全面评估；3) 它支持包含多个图像的复杂查询和文档，并涵盖多样化的检索场景，更准确地反映了真实世界的应用。我们的基准包含 1,309 个精心策划的查询，这些查询来自手动收集和注释或选择性地整合公共数据集。尽管在现有基准上取得了优异的成绩，但当前最先进的模型在 MR$^2$-Bench 上仍然表现不佳：例如，领先的 Seed1.6-Embedding 模型在 MMEB 上的 Recall@1 为 77.78，但在 MR$^2$-Bench 上仅为 9.91。这种巨大的性能差距凸显了我们的基准带来的更大挑战，以及对推理密集型多模态检索的进一步发展的迫切需求。数据集和评估代码将在 https://github.com/VectorSpaceLab/MR2-Bench 上公开。

## 🔬 方法详解

**问题定义**：论文旨在解决现有基准在多模态检索评估中无法有效衡量模型深层推理能力的问题。现有方法主要关注对象-文本匹配等浅层语义对应，忽略了逻辑、空间和因果推理等高级认知能力，导致模型在更复杂的真实场景中表现不佳。

**核心思路**：论文的核心思路是构建一个推理密集型的多模态检索基准，即MR$^2$-Bench。该基准通过设计需要逻辑、空间和因果推理的任务，以及包含多样化多模态数据和复杂查询文档的场景，来全面评估模型的推理能力。这样设计的目的是为了更真实地反映实际应用中多模态检索的需求，并推动相关技术的发展。

**技术框架**：MR$^2$-Bench的整体框架包括以下几个关键组成部分：1) 数据集构建：通过手动收集、注释和整合公共数据集，构建包含1309个查询的数据集，涵盖自然图像、图表和视觉谜题等多种模态数据。2) 任务设计：设计需要逻辑、空间和因果推理的多模态检索任务，例如根据图像推理文本描述，或根据文本描述检索相关图像。3) 评估指标：采用Recall@K等指标评估模型在不同任务上的性能，并分析模型的推理能力。

**关键创新**：MR$^2$-Bench的最重要的技术创新点在于其推理密集型的任务设计。与现有基准主要关注浅层语义匹配不同，MR$^2$-Bench的任务需要模型进行深层的逻辑、空间和因果推理，从而更全面地评估模型的认知能力。此外，MR$^2$-Bench还包含了多样化的多模态数据和复杂的查询文档，更真实地反映了实际应用场景。

**关键设计**：MR$^2$-Bench的关键设计包括：1) 数据集的选择和标注：选择包含丰富推理信息的图像、图表和视觉谜题，并进行精细的标注，以确保任务的难度和准确性。2) 任务的设计：设计需要逻辑、空间和因果推理的任务，例如根据图像推理文本描述，或根据文本描述检索相关图像。3) 评估指标的选择：采用Recall@K等指标评估模型在不同任务上的性能，并分析模型的推理能力。

## 📊 实验亮点

实验结果表明，现有最先进的模型在MR$^2$-Bench上的性能显著下降。例如，领先的Seed1.6-Embedding模型在MMEB上的Recall@1为77.78，但在MR$^2$-Bench上仅为9.91。这一结果表明，现有模型在推理密集型的多模态检索任务中仍然存在很大的提升空间，MR$^2$-Bench能够有效区分模型的推理能力。

## 🎯 应用场景

MR$^2$-Bench可应用于开发更智能的多模态检索系统，例如智能搜索引擎、图像理解系统和机器人导航等。通过提高模型在复杂场景下的推理能力，可以提升用户体验，并为人工智能在实际应用中发挥更大的作用奠定基础。未来，该基准可以扩展到更多领域，例如医疗诊断和教育等。

## 📄 摘要（原文）

> Multimodal retrieval is becoming a crucial component of modern AI applications, yet its evaluation lags behind the demands of more realistic and challenging scenarios. Existing benchmarks primarily probe surface-level semantic correspondence (e.g., object-text matching) while failing to assess the deeper reasoning required to capture complex relationships between visual and textual information. To address this gap, we introduce MR$^2$-Bench, a reasoning-intensive benchmark for multimodal retrieval. MR$^2$-Bench presents the following critical values: 1) all tasks are reasoning-driven, going beyond shallow matching to effectively assess models' capacity for logical, spatial, and causal inference; 2) it features diverse multimodal data, such as natural images, diagrams, and visual puzzles, enabling comprehensive evaluation across content types; 3) it supports complex queries and documents containing multiple images and covers diverse retrieval scenarios, more accurately reflecting real-world applications. Our benchmark contains 1,309 curated queries, derived either from manual collection and annotation or from selective consolidation of public datasets. Despite achieving strong results on existing benchmarks, current state-of-the-art models still struggle on MR$^2$-Bench: for example, the leading Seed1.6-Embedding model attains a Recall@1 of 77.78 on MMEB, but only 9.91 on MR$^2$-Bench. This substantial performance gap highlights both the increased challenge posed by our benchmark and the pressing need for further advances in reasoning-intensive multimodal retrieval. The dataset and evaluation code will be made publicly available at https://github.com/VectorSpaceLab/MR2-Bench.

