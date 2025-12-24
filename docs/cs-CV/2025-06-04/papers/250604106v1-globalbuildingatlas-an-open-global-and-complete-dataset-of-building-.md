---
layout: default
title: "GlobalBuildingAtlas: An Open Global and Complete Dataset of Building Polygons, Heights and LoD1 3D Models"
---

# GlobalBuildingAtlas: An Open Global and Complete Dataset of Building Polygons, Heights and LoD1 3D Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04106" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04106v1</a>
  <a href="https://arxiv.org/pdf/2506.04106.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04106v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04106v1', 'GlobalBuildingAtlas: An Open Global and Complete Dataset of Building Polygons, Heights and LoD1 3D Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiao Xiang Zhu, Sining Chen, Fahong Zhang, Yilei Shi, Yuanyuan Wang

**分类**: cs.CV

**发布日期**: 2025-06-04

---

## 💡 一句话要点

**提出GlobalBuildingAtlas以解决全球建筑数据缺乏问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `建筑数据集` `机器学习` `卫星数据` `3D模型` `城市规划` `可持续发展` `高分辨率`

## 📋 核心要点

1. 现有建筑数据集缺乏全球范围内的高质量和完整性，限制了建筑分析和城市规划的研究。
2. 论文提出了GlobalBuildingAtlas，通过机器学习从卫星数据中提取建筑多边形和高度，提供全球建筑的完整数据。
3. 实验结果显示，GBA.Polygon和GBA.Height分别超越了现有数据库，提供了更高的空间分辨率和准确性。

## 📝 摘要（中文）

我们介绍了GlobalBuildingAtlas，这是一个公开可用的数据集，提供全球建筑多边形、高度和等级1（LoD1）3D建筑模型的完整覆盖。这是第一个在全球范围内以个体建筑级别提供高质量、一致且完整的2D和3D建筑数据的开放数据集。为此，我们开发了基于机器学习的管道，从全球PlanetScope卫星数据中提取建筑多边形和高度。此外，采用基于质量的融合策略生成更高质量的多边形。GBA.Polygon包含超过27.5亿个建筑，超越了现有最全面数据库。GBA.Height提供了最详细和准确的全球3D建筑高度图，空间分辨率为3x3米，远高于以往产品。最终，我们生成了全球LoD1建筑模型，包含2.68亿个建筑实例，预测高度完整性超过97%。

## 🔬 方法详解

**问题定义**：本论文旨在解决全球建筑数据缺乏的问题，现有方法在建筑多边形和高度的提取上存在准确性和覆盖范围不足的痛点。

**核心思路**：论文的核心思路是利用机器学习技术从PlanetScope卫星数据中提取建筑信息，并通过质量融合策略提升数据的准确性和完整性。

**技术框架**：整体架构包括数据采集、建筑多边形提取（GBA.Polygon）、建筑高度提取（GBA.Height）和LoD1模型生成（GBA.LoD1）四个主要模块。

**关键创新**：最重要的技术创新在于首次提供全球范围内的完整建筑数据集，尤其是高分辨率的建筑高度图，显著提升了建筑分析的精度。

**关键设计**：在多边形提取中，采用了基于质量的融合策略，结合已有的建筑多边形数据和新提取的数据，确保生成的多边形质量更高。高度提取则实现了3x3米的空间分辨率，远超以往的90米分辨率。

## 📊 实验亮点

实验结果表明，GBA.Polygon包含超过27.5亿个建筑实例，超越了现有数据库1亿个建筑，GBA.Height的空间分辨率为3x3米，相较于以往产品提升了30倍，LoD1模型的高度完整性超过97%，RMSE在1.5米到8.9米之间，显示出显著的准确性。

## 🎯 应用场景

该研究的潜在应用领域包括城市规划、建筑监测、环境评估等。通过提供高质量的建筑数据，GlobalBuildingAtlas能够支持更精确的城市发展分析和可持续发展目标的监测，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We introduce GlobalBuildingAtlas, a publicly available dataset providing global and complete coverage of building polygons, heights and Level of Detail 1 (LoD1) 3D building models. This is the first open dataset to offer high quality, consistent, and complete building data in 2D and 3D form at the individual building level on a global scale. Towards this dataset, we developed machine learning-based pipelines to derive building polygons and heights (called GBA.Height) from global PlanetScope satellite data, respectively. Also a quality-based fusion strategy was employed to generate higher-quality polygons (called GBA.Polygon) based on existing open building polygons, including our own derived one. With more than 2.75 billion buildings worldwide, GBA.Polygon surpasses the most comprehensive database to date by more than 1 billion buildings. GBA.Height offers the most detailed and accurate global 3D building height maps to date, achieving a spatial resolution of 3x3 meters-30 times finer than previous global products (90 m), enabling a high-resolution and reliable analysis of building volumes at both local and global scales. Finally, we generated a global LoD1 building model (called GBA.LoD1) from the resulting GBA.Polygon and GBA.Height. GBA.LoD1 represents the first complete global LoD1 building models, including 2.68 billion building instances with predicted heights, i.e., with a height completeness of more than 97%, achieving RMSEs ranging from 1.5 m to 8.9 m across different continents. With its height accuracy, comprehensive global coverage and rich spatial details, GlobalBuildingAltas offers novel insights on the status quo of global buildings, which unlocks unprecedented geospatial analysis possibilities, as showcased by a better illustration of where people live and a more comprehensive monitoring of the progress on the 11th Sustainable Development Goal of the United Nations.

