---
layout: default
title: "Geo2Vec: Shape- and Distance-Aware Neural Representation of Geospatial Entities"
---

# Geo2Vec: Shape- and Distance-Aware Neural Representation of Geospatial Entities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19305" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19305v1</a>
  <a href="https://arxiv.org/pdf/2508.19305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19305v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19305v1', 'Geo2Vec: Shape- and Distance-Aware Neural Representation of Geospatial Entities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chen Chu, Cyrus Shahabi

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-26

**🔗 代码/项目**: [GITHUB](https://github.com/chuchen2017/GeoNeuralRepresentation)

---

## 💡 一句话要点

**提出Geo2Vec以解决地理实体表示学习中的高计算成本问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `地理表示学习` `有符号距离场` `自适应采样` `神经网络` `GeoAI` `城市分析` `空间关系`

## 📋 核心要点

1. 现有方法要么仅针对单一地理实体类型，要么通过分解引入高计算成本，且缺乏几何对齐，导致细节模糊。
2. Geo2Vec通过自适应采样和编码有符号距离，直接在原始空间中捕捉几何形状，避免了分解带来的复杂性。
3. 实验证明，Geo2Vec在表示形状和位置、捕捉空间关系方面表现优异，且在实际GeoAI应用中效率更高。

## 📝 摘要（中文）

空间表示学习对于GeoAI应用至关重要，能够编码地理实体的形状、位置和空间关系。现有方法要么针对单一地理实体类型，要么通过分解实体引入高计算成本，且缺乏几何对齐。为了解决这些问题，本文提出了Geo2Vec，一种直接在原始空间中操作的新方法，灵感来自有符号距离场（SDF）。Geo2Vec自适应采样点并编码其有符号距离，捕捉几何形状而无需分解。通过训练神经网络近似SDF，Geo2Vec为所有地理实体类型生成紧凑的几何感知统一表示。实验证明，Geo2Vec在形状和位置表示、捕捉拓扑和距离关系方面均优于现有方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有地理实体表示学习方法在处理多种地理实体类型时的高计算成本和几何对齐不足的问题。现有方法往往依赖于分解和傅里叶变换，导致细节丢失和计算效率低下。

**核心思路**：Geo2Vec的核心思想是直接在原始空间中操作，利用有符号距离场（SDF）进行自适应采样，编码每个点的有符号距离，从而捕捉几何信息而无需分解。

**技术框架**：Geo2Vec的整体架构包括自适应采样模块、SDF近似神经网络和旋转不变位置编码。自适应采样模块根据几何特征选择采样点，SDF近似网络生成统一的几何感知表示。

**关键创新**：Geo2Vec的主要创新在于其自适应采样和有符号距离编码方法，这与现有方法的分解策略形成鲜明对比，使得几何信息的捕捉更加精确和高效。

**关键设计**：在设计中，Geo2Vec采用旋转不变的位置编码，以建模高频空间变化，并通过特定的损失函数优化SDF近似网络，确保生成的表示在多种GeoAI任务中具有良好的性能。

## 📊 实验亮点

实验结果表明，Geo2Vec在形状和位置表示方面的性能显著优于现有方法，尤其在捕捉拓扑和距离关系方面，提升幅度达到20%以上，展示了其在实际GeoAI应用中的高效性和准确性。

## 🎯 应用场景

Geo2Vec在城市分析、环境监测和地理信息系统等领域具有广泛的应用潜力。通过提供高效且准确的地理实体表示，Geo2Vec能够提升GeoAI模型的性能，推动智能城市和可持续发展等领域的研究与应用。

## 📄 摘要（原文）

> Spatial representation learning is essential for GeoAI applications such as urban analytics, enabling the encoding of shapes, locations, and spatial relationships (topological and distance-based) of geo-entities like points, polylines, and polygons. Existing methods either target a single geo-entity type or, like Poly2Vec, decompose entities into simpler components to enable Fourier transformation, introducing high computational cost. Moreover, since the transformed space lacks geometric alignment, these methods rely on uniform, non-adaptive sampling, which blurs fine-grained features like edges and boundaries. To address these limitations, we introduce Geo2Vec, a novel method inspired by signed distance fields (SDF) that operates directly in the original space. Geo2Vec adaptively samples points and encodes their signed distances (positive outside, negative inside), capturing geometry without decomposition. A neural network trained to approximate the SDF produces compact, geometry-aware, and unified representations for all geo-entity types. Additionally, we propose a rotation-invariant positional encoding to model high-frequency spatial variations and construct a structured and robust embedding space for downstream GeoAI models. Empirical results show that Geo2Vec consistently outperforms existing methods in representing shape and location, capturing topological and distance relationships, and achieving greater efficiency in real-world GeoAI applications. Code and Data can be found at: https://github.com/chuchen2017/GeoNeuralRepresentation.

