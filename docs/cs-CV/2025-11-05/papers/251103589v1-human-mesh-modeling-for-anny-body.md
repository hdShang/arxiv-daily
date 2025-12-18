---
layout: default
title: Human Mesh Modeling for Anny Body
---

# Human Mesh Modeling for Anny Body

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.03589" class="toolbar-btn" target="_blank">📄 arXiv: 2511.03589v1</a>
  <a href="https://arxiv.org/pdf/2511.03589.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.03589v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.03589v1', 'Human Mesh Modeling for Anny Body')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Romain Brégier, Guénolé Fiche, Laura Bravo-Sánchez, Thomas Lucas, Matthieu Armando, Philippe Weinzaepfel, Grégory Rogez, Fabien Baradel

**分类**: cs.CV

**发布日期**: 2025-11-05

**备注**: We release our model and code at https://github.com/naver/anny

---

## 💡 一句话要点

**提出Anny：一个基于人体测量学知识的可微、无扫描的人体网格建模方法**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `人体建模` `参数化模型` `人体网格恢复` `合成数据生成` `人体测量学` `可微渲染` `无扫描建模`

## 📋 核心要点

1. 现有参数化人体模型依赖昂贵的3D扫描和受限的形状空间，缺乏开放性和广泛代表性。
2. Anny模型基于人体测量学知识，构建可微、可解释的形状空间，通过表型参数控制人体形态。
3. Anny在HMR任务中表现与扫描模型相当，同时保持可解释性和广泛代表性，并开源代码。

## 📝 摘要（中文）

参数化人体模型在许多以人为中心的任务中至关重要，但现有模型通常依赖于昂贵的3D扫描和专有的、人口统计学上狭隘的学习形状空间。我们提出了Anny，一个简单、完全可微且无扫描的人体模型，它基于MakeHuman社区的人体测量学知识。Anny定义了一个连续的、可解释的形状空间，其中表型参数（例如性别、年龄、身高、体重）控制着跨越广泛人体形态的混合形状——涵盖年龄（从婴儿到老人）、体型和比例。通过使用世界卫生组织（WHO）的人口统计数据进行校准，它在单个统一模型中提供了现实且具有人口统计学基础的人体形状变化。由于其开放性和语义控制，Anny可以作为3D人体建模的通用基础——支持毫米级精度的扫描拟合、可控的合成数据生成和人体网格恢复（HMR）。我们进一步介绍了Anny-One，一个包含80万个由Anny生成的逼真人体的集合，表明尽管Anny很简单，但使用Anny训练的HMR模型可以与使用基于扫描的身体模型训练的模型相匹配，同时保持可解释性和广泛的代表性。Anny身体模型及其代码在Apache 2.0许可下发布，使Anny成为以人为中心的3D建模的可访问基础。

## 🔬 方法详解

**问题定义**：现有参数化人体模型依赖于昂贵的3D扫描数据，且学习到的形状空间通常是专有的，并且在人口统计学上存在偏差，缺乏开放性和广泛的代表性。这限制了其在各种应用中的适用性，例如合成数据生成和人体网格恢复。

**核心思路**：Anny的核心思路是构建一个基于人体测量学知识的、完全可微的参数化人体模型，该模型不需要3D扫描数据，而是利用MakeHuman社区的知识，通过表型参数（如性别、年龄、身高、体重）来控制blendshapes，从而生成各种人体形态。这种方法旨在创建一个开放、可解释且具有广泛代表性的人体模型。

**技术框架**：Anny模型的技术框架主要包括以下几个部分：1) 基于MakeHuman社区的人体测量学知识构建基础模型；2) 定义一个连续的、可解释的形状空间，其中表型参数作为控制变量；3) 使用blendshapes来表示不同的人体形态，并通过表型参数进行控制；4) 使用WHO的人口统计数据对模型进行校准，以确保其具有现实的人体形状变化；5) 提供一个完全可微的框架，方便进行优化和学习。

**关键创新**：Anny的关键创新在于其无扫描的建模方法和基于人体测量学知识的形状空间。与传统的基于扫描的模型相比，Anny不需要昂贵的3D扫描数据，并且可以生成具有广泛代表性的人体形态。此外，Anny的形状空间是连续且可解释的，这使得用户可以方便地控制和修改人体形态。

**关键设计**：Anny的关键设计包括：1) 使用blendshapes来表示不同的人体形态，并使用表型参数作为控制变量；2) 使用WHO的人口统计数据对模型进行校准，以确保其具有现实的人体形状变化；3) 提供一个完全可微的框架，方便进行优化和学习；4) 开源模型和代码，使其易于访问和使用。

## 📊 实验亮点

Anny-One数据集包含80万个由Anny生成的逼真人像，实验表明，使用Anny训练的HMR模型性能与使用基于扫描的身体模型训练的模型相当，同时保持了模型的可解释性和广泛代表性。这证明了Anny在人体网格恢复任务中的有效性。

## 🎯 应用场景

Anny模型可广泛应用于3D人体建模、合成数据生成、人体网格恢复（HMR）、虚拟现实/增强现实、游戏开发、服装设计等领域。其开放性和可解释性使其成为研究和工业应用的理想选择，有助于推动以人为中心的AI技术发展。

## 📄 摘要（原文）

> Parametric body models are central to many human-centric tasks, yet existing models often rely on costly 3D scans and learned shape spaces that are proprietary and demographically narrow. We introduce Anny, a simple, fully differentiable, and scan-free human body model grounded in anthropometric knowledge from the MakeHuman community. Anny defines a continuous, interpretable shape space, where phenotype parameters (e.g. gender, age, height, weight) control blendshapes spanning a wide range of human forms -- across ages (from infants to elders), body types, and proportions. Calibrated using WHO population statistics, it provides realistic and demographically grounded human shape variation within a single unified model. Thanks to its openness and semantic control, Anny serves as a versatile foundation for 3D human modeling -- supporting millimeter-accurate scan fitting, controlled synthetic data generation, and Human Mesh Recovery (HMR). We further introduce Anny-One, a collection of 800k photorealistic humans generated with Anny, showing that despite its simplicity, HMR models trained with Anny can match the performance of those trained with scan-based body models, while remaining interpretable and broadly representative. The Anny body model and its code are released under the Apache 2.0 license, making Anny an accessible foundation for human-centric 3D modeling.

