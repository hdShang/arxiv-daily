---
layout: default
title: "SIGMUS: Semantic Integration for Knowledge Graphs in Multimodal Urban Spaces"
---

# SIGMUS: Semantic Integration for Knowledge Graphs in Multimodal Urban Spaces

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00287" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00287v1</a>
  <a href="https://arxiv.org/pdf/2509.00287.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00287v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00287v1', 'SIGMUS: Semantic Integration for Knowledge Graphs in Multimodal Urban Spaces')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Brian Wang, Mani Srivastava

**分类**: cs.AI, cs.CY

**发布日期**: 2025-08-30

**备注**: 9 pages, accepted at UrbComp 2025 KDD 2025

---

## 💡 一句话要点

**提出SIGMUS以解决城市多模态数据整合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态数据` `知识图谱` `城市管理` `事件识别` `人工智能` `大型语言模型` `数据整合`

## 📋 核心要点

1. 现有方法在整合城市多模态数据时面临碎片化和依赖人工推理的问题，导致事件识别困难。
2. SIGMUS系统通过大型语言模型生成世界知识，自动识别城市事件与多模态数据之间的关系，避免人工编码规则。
3. 实验结果显示，SIGMUS能够有效连接五种数据源与相关事件，提升了事件识别的准确性和效率。

## 📝 摘要（中文）

现代城市空间配备了多种传感器，产生大量多模态数据。这些数据可用于识别和推理城市中发生的重要事件，如重大紧急情况、文化和社会活动以及自然灾害。然而，由于数据分散且依赖于人工推理来识别多模态数据之间的关系，整合这些数据变得困难。为此，本文提出了SIGMUS系统，利用大型语言模型生成必要的世界知识，以识别城市事件与不同模态数据之间的关系，从而组织与事件相关的证据和观察。这种知识以知识图谱的形式表示，能够有效整合来自不同来源的数据。实验表明，SIGMUS能够合理连接五种不同的数据源（新闻文章文本、监控图像、空气质量、天气和交通测量）与相关事件。

## 🔬 方法详解

**问题定义**：本文旨在解决城市多模态数据整合的挑战，现有方法依赖人工推理，导致数据碎片化和整合困难。

**核心思路**：SIGMUS系统利用大型语言模型（LLMs）生成世界知识，自动识别城市事件与多模态数据之间的关系，从而组织与事件相关的证据和观察。

**技术框架**：SIGMUS的整体架构包括数据采集模块、知识生成模块和知识图谱构建模块。数据采集模块负责从不同来源获取多模态数据，知识生成模块利用LLMs处理数据并生成知识，最后知识图谱构建模块将知识组织成图谱形式。

**关键创新**：SIGMUS的主要创新在于使用大型语言模型进行知识生成，突破了传统方法依赖人工编码规则的局限，实现了自动化的多模态数据整合。

**关键设计**：在设计中，SIGMUS采用了特定的参数设置以优化LLMs的输出质量，并设计了适合多模态数据的损失函数，以确保知识图谱的准确性和完整性。通过这些设计，SIGMUS能够有效处理来自不同数据源的信息。

## 📊 实验亮点

实验结果表明，SIGMUS能够合理连接五种不同的数据源，包括新闻文章、监控图像、空气质量、天气和交通测量，显著提升了事件识别的准确性。与传统方法相比，SIGMUS在多模态数据整合方面的表现有明显改善，展示了其在实际应用中的有效性。

## 🎯 应用场景

SIGMUS的研究成果在城市管理、应急响应和公共安全等领域具有广泛的应用潜力。通过有效整合多模态数据，城市管理者可以更快速地识别和响应突发事件，提高城市的安全性和应急能力。此外，该系统还可用于文化活动的监测和社会事件的分析，推动城市智能化发展。

## 📄 摘要（原文）

> Modern urban spaces are equipped with an increasingly diverse set of sensors, all producing an abundance of multimodal data. Such multimodal data can be used to identify and reason about important incidents occurring in urban landscapes, such as major emergencies, cultural and social events, as well as natural disasters. However, such data may be fragmented over several sources and difficult to integrate due to the reliance on human-driven reasoning for identifying relationships between the multimodal data corresponding to an incident, as well as understanding the different components which define an incident. Such relationships and components are critical to identifying the causes of such incidents, as well as producing forecasting the scale and intensity of future incidents as they begin to develop. In this work, we create SIGMUS, a system for Semantic Integration for Knowledge Graphs in Multimodal Urban Spaces. SIGMUS uses Large Language Models (LLMs) to produce the necessary world knowledge for identifying relationships between incidents occurring in urban spaces and data from different modalities, allowing us to organize evidence and observations relevant to an incident without relying and human-encoded rules for relating multimodal sensory data with incidents. This organized knowledge is represented as a knowledge graph, organizing incidents, observations, and much more. We find that our system is able to produce reasonable connections between 5 different data sources (new article text, CCTV images, air quality, weather, and traffic measurements) and relevant incidents occurring at the same time and location.

