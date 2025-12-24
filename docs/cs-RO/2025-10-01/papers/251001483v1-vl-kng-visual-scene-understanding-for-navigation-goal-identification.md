---
layout: default
title: "VL-KnG: Visual Scene Understanding for Navigation Goal Identification using Spatiotemporal Knowledge Graphs"
---

# VL-KnG: Visual Scene Understanding for Navigation Goal Identification using Spatiotemporal Knowledge Graphs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01483" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01483v1</a>
  <a href="https://arxiv.org/pdf/2510.01483.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01483v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01483v1', 'VL-KnG: Visual Scene Understanding for Navigation Goal Identification using Spatiotemporal Knowledge Graphs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohamad Al Mdfaa, Svetlana Lukina, Timur Akhtyamov, Arthur Nigmatzyanov, Dmitrii Nalberskii, Sergey Zagoruyko, Gonzalo Ferrer

**分类**: cs.RO, cs.AI

**发布日期**: 2025-10-01

**备注**: This work has been submitted to the IEEE for possible publication

---

## 💡 一句话要点

**VL-KnG：利用时空知识图谱进行视觉场景理解，实现导航目标识别**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视觉场景理解` `知识图谱` `机器人导航` `视觉-语言模型` `空间推理` `时空推理` `可解释性`

## 📋 核心要点

1. 现有视觉-语言模型在机器人导航中存在场景记忆不足、空间推理有限和实时性差等问题。
2. VL-KnG通过构建时空知识图谱，维护对象身份信息，并支持可查询的图结构，实现可解释的空间推理。
3. 在WalkieKnowledge基准测试和真实机器人实验中，VL-KnG在导航目标识别方面取得了与Gemini 2.5 Pro相当的性能，并具备实时性和可解释性。

## 📝 摘要（中文）

视觉-语言模型(VLMs)在机器人导航方面展现了潜力，但存在局限性：缺乏持久的场景记忆，空间推理能力有限，且无法有效扩展到长时间视频以满足实时应用需求。我们提出了VL-KnG，一个视觉场景理解系统，通过构建时空知识图谱和高效的查询处理来解决这些挑战，用于导航目标识别。该方法分块处理视频序列，利用现代VLMs创建持久的知识图谱，维护对象随时间推移的身份信息，并通过可查询的图结构实现可解释的空间推理。我们还引入了WalkieKnowledge，一个新的基准测试，包含约200个手动标注的问题，涵盖8条不同的轨迹，视频数据约100分钟，以便在结构化方法和通用VLMs之间进行公平比较。在差速驱动机器人上的实际部署表明了其应用性，我们的方法实现了77.27%的成功率和76.92%的答案准确率，与Gemini 2.5 Pro的性能相匹配，同时提供了由知识图谱支持的可解释推理，以及在定位、导航和规划等不同任务中进行实时部署的计算效率。代码和数据集将在接收后发布。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人导航中，视觉-语言模型（VLMs）在理解复杂场景和进行有效空间推理方面的局限性。现有VLMs缺乏持久的场景记忆，难以处理长时间视频，并且空间推理能力不足，导致无法准确识别导航目标。这些问题限制了VLMs在实际机器人导航中的应用。

**核心思路**：论文的核心思路是构建一个时空知识图谱（Spatiotemporal Knowledge Graph, KnG），用于表示和维护场景中的对象、关系以及它们随时间的变化。通过将视频信息转化为结构化的知识图谱，可以实现持久的场景记忆和可解释的空间推理，从而提高导航目标识别的准确性和效率。

**技术框架**：VL-KnG系统的整体架构包括以下几个主要模块：1) 视频分块处理：将长视频分割成较小的块，以便于处理。2) 视觉-语言模型（VLM）：利用现代VLMs提取视频块中的对象和关系信息。3) 知识图谱构建：将VLM提取的信息整合到时空知识图谱中，维护对象身份和关系随时间的变化。4) 查询处理：通过查询知识图谱，进行空间推理和导航目标识别。整个流程旨在将非结构化的视频数据转化为结构化的知识表示，并利用该知识进行有效的推理。

**关键创新**：该论文的关键创新在于将时空知识图谱应用于机器人导航中的视觉场景理解。与传统的VLMs相比，VL-KnG能够维护持久的场景记忆，进行可解释的空间推理，并且能够有效处理长时间视频。此外，WalkieKnowledge基准测试的引入也为结构化方法和通用VLMs的公平比较提供了平台。

**关键设计**：论文中关于知识图谱的构建和查询处理是关键设计。具体来说，知识图谱的节点表示场景中的对象，边表示对象之间的关系（例如，空间关系、时间关系）。在查询处理方面，论文设计了高效的图查询算法，用于从知识图谱中提取相关信息，并进行空间推理。此外，视频分块的大小和VLM的选择也会影响系统的性能，但论文中未提供具体的参数设置细节。

## 📊 实验亮点

VL-KnG在真实机器人实验中取得了显著成果，成功率达到77.27%，答案准确率达到76.92%，与Gemini 2.5 Pro的性能相匹配。更重要的是，VL-KnG提供了可解释的推理过程，并具备实时部署的计算效率。此外，新提出的WalkieKnowledge基准测试为评估视觉场景理解系统提供了有价值的资源。

## 🎯 应用场景

VL-KnG具有广泛的应用前景，包括但不限于：机器人导航、智能监控、自动驾驶、增强现实等领域。通过提供持久的场景记忆和可解释的空间推理，该技术可以提高机器人在复杂环境中的感知和决策能力，从而实现更安全、更高效的自主操作。未来，该技术有望应用于更广泛的场景，例如家庭服务机器人、工业自动化和智能交通系统。

## 📄 摘要（原文）

> Vision-language models (VLMs) have shown potential for robot navigation but encounter fundamental limitations: they lack persistent scene memory, offer limited spatial reasoning, and do not scale effectively with video duration for real-time application. We present VL-KnG, a Visual Scene Understanding system that tackles these challenges using spatiotemporal knowledge graph construction and computationally efficient query processing for navigation goal identification. Our approach processes video sequences in chunks utilizing modern VLMs, creates persistent knowledge graphs that maintain object identity over time, and enables explainable spatial reasoning through queryable graph structures. We also introduce WalkieKnowledge, a new benchmark with about 200 manually annotated questions across 8 diverse trajectories spanning approximately 100 minutes of video data, enabling fair comparison between structured approaches and general-purpose VLMs. Real-world deployment on a differential drive robot demonstrates practical applicability, with our method achieving 77.27% success rate and 76.92% answer accuracy, matching Gemini 2.5 Pro performance while providing explainable reasoning supported by the knowledge graph, computational efficiency for real-time deployment across different tasks, such as localization, navigation and planning. Code and dataset will be released after acceptance.

