---
layout: default
title: "KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation"
---

# KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00366" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00366v1</a>
  <a href="https://arxiv.org/pdf/2509.00366.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00366v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00366v1', 'KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyi Guan, Jason Chun Lok Li, Zhijian Hou, Pingping Zhang, Donglai Xu, Yuzhi Zhao, Mengyang Wu, Jinpeng Chen, Thanh-Toan Nguyen, Pengfei Xian, Wenao Ma, Shengchao Qin, Graziano Chesi, Ngai Wong

**分类**: cs.MA, cs.CL, cs.MM

**发布日期**: 2025-08-30

**备注**: Accepted by the EMNLP 2025

---

## 💡 一句话要点

**提出KG-RAG框架以提升GUI代理的决策能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `检索增强生成` `图形用户界面` `移动应用` `决策支持` `意图引导` `用户界面转换图`

## 📋 核心要点

1. 现有的GUI代理在处理复杂移动任务时，由于缺乏应用特定知识，导致决策能力不足。
2. KG-RAG框架通过知识图谱驱动的检索增强生成方法，将UTGs转化为结构化向量数据库，从而实现高效检索。
3. 实验结果显示，KG-RAG在成功率、决策准确率和任务步骤上均显著优于现有方法，具有良好的应用前景。

## 📝 摘要（中文）

尽管近年来取得了进展，基于大型语言模型的图形用户界面（GUI）代理在复杂移动任务中仍面临应用特定知识不足的问题。虽然用户界面转换图（UTGs）提供了结构化的导航表示，但由于提取不佳和整合效率低下，未得到充分利用。我们提出KG-RAG，一个知识图谱驱动的检索增强生成框架，将碎片化的UTGs转化为结构化的向量数据库，以实现高效的实时检索。通过利用意图引导的LLM搜索方法，KG-RAG生成可操作的导航路径，增强代理的决策能力。实验表明，KG-RAG在多种移动应用中表现优异，成功率达到75.8%（比AutoDroid提高8.9%），决策准确率为84.6%（提高8.1%），平均任务步骤从4.5减少到4.1。此外，我们还提出了KG-Android-Bench和KG-Harmony-Bench两个基准，专为中国移动生态系统设计，以促进未来研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决基于大型语言模型的GUI代理在复杂移动任务中因缺乏应用特定知识而导致的决策能力不足的问题。现有方法在提取和整合用户界面转换图（UTGs）方面存在效率低下和准确性不足的痛点。

**核心思路**：KG-RAG框架的核心思路是利用知识图谱驱动的检索增强生成方法，将碎片化的UTGs转化为结构化的向量数据库，以实现高效的实时检索和生成可操作的导航路径。通过意图引导的搜索方法，KG-RAG能够更好地理解用户意图，从而提升决策能力。

**技术框架**：KG-RAG的整体架构包括数据预处理、UTG转化为向量数据库、意图引导的检索模块和生成模块。首先，对UTGs进行结构化处理，然后通过知识图谱构建向量数据库，最后利用LLM生成导航路径。

**关键创新**：KG-RAG的主要创新在于将知识图谱与检索增强生成相结合，形成了一种新的决策支持框架。这一方法与传统的单一生成或检索方法相比，能够更有效地整合应用特定知识，提高决策的准确性和效率。

**关键设计**：在KG-RAG中，关键设计包括向量数据库的构建方式、意图引导的检索算法以及生成模块的网络结构。具体的参数设置和损失函数设计也经过精心调整，以确保模型在复杂任务中的表现最优。

## 📊 实验亮点

KG-RAG在多种移动应用中的实验结果显示，成功率达到75.8%，比AutoDroid提高8.9%；决策准确率为84.6%，提高8.1%；平均任务步骤从4.5减少到4.1。此外，该框架在Web和桌面应用中的迁移表现也显著，分别在微博和QQ音乐上成功率提高40%和20%。

## 🎯 应用场景

KG-RAG框架具有广泛的应用潜力，特别是在移动应用程序的导航和决策支持系统中。通过提升GUI代理的决策能力，该框架可以为用户提供更流畅的操作体验。此外，KG-RAG的设计理念也可以扩展到其他领域，如智能家居、自动驾驶等，未来可能对人机交互和智能系统的设计产生深远影响。

## 📄 摘要（原文）

> Despite recent progress, Graphic User Interface (GUI) agents powered by Large Language Models (LLMs) struggle with complex mobile tasks due to limited app-specific knowledge. While UI Transition Graphs (UTGs) offer structured navigation representations, they are underutilized due to poor extraction and inefficient integration. We introduce KG-RAG, a Knowledge Graph-driven Retrieval-Augmented Generation framework that transforms fragmented UTGs into structured vector databases for efficient real-time retrieval. By leveraging an intent-guided LLM search method, KG-RAG generates actionable navigation paths, enhancing agent decision-making. Experiments across diverse mobile apps show that KG-RAG outperforms existing methods, achieving a 75.8% success rate (8.9% improvement over AutoDroid), 84.6% decision accuracy (8.1% improvement), and reducing average task steps from 4.5 to 4.1. Additionally, we present KG-Android-Bench and KG-Harmony-Bench, two benchmarks tailored to the Chinese mobile ecosystem for future research. Finally, KG-RAG transfers to web/desktop (+40% SR on Weibo-web; +20% on QQ Music-desktop), and a UTG cost ablation shows accuracy saturates at ~4h per complex app, enabling practical deployment trade-offs.

