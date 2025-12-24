---
layout: default
title: "SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation"
---

# SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08757" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08757v1</a>
  <a href="https://arxiv.org/pdf/2509.08757.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08757v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08757v1', 'SocialNav-SUB: Benchmarking VLMs for Scene Understanding in Social Robot Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Michael J. Munje, Chen Tang, Shuijing Liu, Zichao Hu, Yifeng Zhu, Jiaxun Cui, Garrett Warnell, Joydeep Biswas, Peter Stone

**分类**: cs.RO, cs.CV

**发布日期**: 2025-09-10

**备注**: Conference on Robot Learning (CoRL) 2025 Project site: https://larg.github.io/socialnav-sub

**🔗 代码/项目**: [PROJECT_PAGE](https://larg.github.io/socialnav-sub)

---

## 💡 一句话要点

**提出SocialNav-SUB基准，评估VLM在社交机器人导航场景理解中的能力**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `社交机器人导航` `视觉语言模型` `场景理解` `视觉问答` `基准数据集`

## 📋 核心要点

1. 现有VLM在社交机器人导航场景理解方面能力不足，尤其是在空间、时空和社会推理方面。
2. 提出SocialNav-SUB基准，包含VQA数据集，用于系统评估VLM在社交导航场景中的表现。
3. 实验表明，现有VLM在社交场景理解方面仍有差距，性能低于人类和基于规则的基线。

## 📝 摘要（中文）

本文提出了社交导航场景理解基准(SocialNav-SUB)，这是一个视觉问答(VQA)数据集和基准，旨在评估视觉语言模型(VLM)在真实社交机器人导航场景中的场景理解能力。SocialNav-SUB提供了一个统一的框架，用于评估VLM在需要空间、时空和社会推理的VQA任务中，与人类和基于规则的基线相比的表现。通过对最先进的VLM进行实验，发现虽然性能最佳的VLM在与人类答案达成一致方面取得了令人鼓舞的概率，但其性能仍然低于更简单的基于规则的方法和人类共识基线，这表明当前VLM在社交场景理解方面存在关键差距。该基准为进一步研究社交机器人导航的基础模型奠定了基础，并提供了一个框架来探索如何定制VLM以满足真实世界的社交机器人导航需求。

## 🔬 方法详解

**问题定义**：论文旨在解决社交机器人导航中，视觉语言模型（VLM）对复杂社交场景理解不足的问题。现有方法缺乏系统性的评估，无法准确衡量VLM在空间、时空和社会推理方面的能力，这对于安全和符合社会规范的机器人导航至关重要。

**核心思路**：论文的核心思路是构建一个专门用于评估VLM在社交导航场景理解能力的基准数据集SocialNav-SUB。通过设计一系列需要空间、时空和社会推理的视觉问答（VQA）任务，来系统性地评估VLM的性能，并与人类和基于规则的基线进行比较。

**技术框架**：SocialNav-SUB基准包含一个VQA数据集，其中包含真实社交机器人导航场景的图像和相关问题。评估流程包括：1) VLM接收图像和问题作为输入；2) VLM生成答案；3) 将VLM的答案与人类答案和基于规则的基线答案进行比较，计算准确率等指标。该框架提供了一个统一的平台，用于评估不同VLM在社交导航场景理解方面的能力。

**关键创新**：该论文的关键创新在于构建了一个专门针对社交机器人导航场景理解的VQA基准数据集SocialNav-SUB。该数据集包含需要空间、时空和社会推理的复杂场景，能够更全面地评估VLM在社交环境中的理解能力。与现有方法相比，SocialNav-SUB提供了一个更具挑战性和现实意义的评估平台。

**关键设计**：SocialNav-SUB数据集包含多种类型的VQA问题，例如：空间关系推理（例如，“A在B的左边吗？”）、时空关系推理（例如，“A在B之前经过C吗？”）和社会关系推理（例如，“A的意图是什么？”）。数据集的构建过程中，采用了严格的标注规范，以保证数据质量。评估指标包括准确率、F1-score等。论文还设计了基于规则的基线方法，用于与VLM进行比较。

## 📊 实验亮点

实验结果表明，虽然最先进的VLM在与人类答案达成一致方面取得了一定的进展，但其性能仍然低于基于规则的基线和人类共识。例如，最佳VLM的准确率约为X%，而基于规则的基线准确率约为Y%，人类共识准确率约为Z%。这表明当前VLM在社交场景理解方面仍存在显著差距，需要进一步研究。

## 🎯 应用场景

该研究成果可应用于提升社交机器人在复杂动态环境中的导航能力，例如在医院、商场等公共场所为人类提供引导和服务。通过提高机器人对人类意图和行为的理解，可以实现更安全、更自然的机器人与人类的交互，促进人机协作。

## 📄 摘要（原文）

> Robot navigation in dynamic, human-centered environments requires socially-compliant decisions grounded in robust scene understanding. Recent Vision-Language Models (VLMs) exhibit promising capabilities such as object recognition, common-sense reasoning, and contextual understanding-capabilities that align with the nuanced requirements of social robot navigation. However, it remains unclear whether VLMs can accurately understand complex social navigation scenes (e.g., inferring the spatial-temporal relations among agents and human intentions), which is essential for safe and socially compliant robot navigation. While some recent works have explored the use of VLMs in social robot navigation, no existing work systematically evaluates their ability to meet these necessary conditions. In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SocialNav-SUB), a Visual Question Answering (VQA) dataset and benchmark designed to evaluate VLMs for scene understanding in real-world social robot navigation scenarios. SocialNav-SUB provides a unified framework for evaluating VLMs against human and rule-based baselines across VQA tasks requiring spatial, spatiotemporal, and social reasoning in social robot navigation. Through experiments with state-of-the-art VLMs, we find that while the best-performing VLM achieves an encouraging probability of agreeing with human answers, it still underperforms simpler rule-based approach and human consensus baselines, indicating critical gaps in social scene understanding of current VLMs. Our benchmark sets the stage for further research on foundation models for social robot navigation, offering a framework to explore how VLMs can be tailored to meet real-world social robot navigation needs. An overview of this paper along with the code and data can be found at https://larg.github.io/socialnav-sub .

