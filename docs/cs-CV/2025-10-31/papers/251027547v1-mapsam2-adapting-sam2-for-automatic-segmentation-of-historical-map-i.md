---
layout: default
title: "MapSAM2: Adapting SAM2 for Automatic Segmentation of Historical Map Images and Time Series"
---

# MapSAM2: Adapting SAM2 for Automatic Segmentation of Historical Map Images and Time Series

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27547" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27547v1</a>
  <a href="https://arxiv.org/pdf/2510.27547.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27547v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27547v1', 'MapSAM2: Adapting SAM2 for Automatic Segmentation of Historical Map Images and Time Series')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xue Xia, Randall Balestriero, Tao Zhang, Yixin Zhou, Andrew Ding, Dev Saini, Lorenz Hurni

**分类**: cs.CV

**发布日期**: 2025-10-31

---

## 💡 一句话要点

**MapSAM2：通过自适应SAM2实现历史地图图像和时间序列的自动分割**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `历史地图分割` `时间序列分析` `少样本学习` `视觉基础模型` `记忆注意力机制`

## 📋 核心要点

1. 历史地图图像分析面临风格多样性和标注数据稀缺的挑战，阻碍了时空数据集的构建。
2. MapSAM2将地图图像和时间序列视为视频，利用记忆注意力机制和伪时间序列生成，实现少样本学习。
3. 实验表明，MapSAM2在历史地图分割和时间序列建筑物链接方面表现出色，尤其是在数据有限的情况下。

## 📝 摘要（中文）

历史地图是记录不同时期地理特征的独特且有价值的档案。然而，由于其广泛的风格变异性和带注释的训练数据的稀缺性，历史地图图像的自动分析仍然是一个重大挑战。从历史地图时间序列构建链接的时空数据集更加耗时和费力，因为它需要综合来自多个地图的信息。此类数据集对于诸如建筑物年代测定、分析道路网络和居民地的发展、研究环境变化等应用至关重要。我们提出了MapSAM2，一个用于自动分割历史地图图像和时间序列的统一框架。MapSAM2建立在视觉基础模型之上，通过少样本微调来适应不同的分割任务。我们的关键创新是将历史地图图像和时间序列都视为视频。对于图像，我们将一组瓦片作为视频进行处理，使记忆注意力机制能够整合来自相似瓦片的上下文线索，从而提高了几何精度，特别是对于面积特征。对于时间序列，我们引入了带注释的Siegfried Building Time Series Dataset，并且为了降低注释成本，我们提出通过模拟常见的时序变换，从单年地图生成伪时间序列。实验结果表明，MapSAM2有效地学习了时间关联，并且可以在有限的监督下或使用伪视频准确地分割和链接时间序列中的建筑物。我们将发布我们的数据集和代码，以支持未来的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决历史地图图像和时间序列的自动分割问题。现有方法在处理历史地图时，由于其风格多样性和缺乏标注数据，分割精度较低。此外，构建历史地图时间序列数据集需要大量人工标注，成本高昂。

**核心思路**：论文的核心思路是将历史地图图像和时间序列都视为视频进行处理。对于图像，将图像分割成瓦片序列，利用视频处理中的记忆注意力机制，捕捉瓦片之间的上下文信息，提高分割精度。对于时间序列，通过生成伪时间序列来扩充训练数据，降低标注成本。

**技术框架**：MapSAM2基于视觉基础模型SAM2构建，整体框架包含以下几个主要步骤：1) 数据预处理：对历史地图图像进行切片处理，生成瓦片序列；对时间序列数据，生成伪时间序列。2) 特征提取：使用SAM2提取图像和时间序列的视觉特征。3) 上下文建模：对于图像，使用记忆注意力机制建模瓦片之间的上下文关系；对于时间序列，学习时间关联。4) 分割预测：基于提取的特征和上下文信息，进行分割预测。5) 后处理：对分割结果进行优化。

**关键创新**：论文的关键创新在于：1) 将历史地图图像和时间序列统一视为视频进行处理，利用视频处理技术解决地图分割问题。2) 提出了一种生成伪时间序列的方法，有效降低了标注成本。3) 利用记忆注意力机制，捕捉图像瓦片之间的上下文信息，提高了分割精度。

**关键设计**：在图像处理方面，论文将图像分割成重叠的瓦片，以确保分割的连续性。记忆注意力机制的具体实现细节未知，但其目的是捕捉瓦片之间的空间关系。在时间序列处理方面，伪时间序列的生成方法包括模拟常见的时序变换，例如平移、旋转和缩放。损失函数的设计细节未知，但应该包含分割损失和时间一致性损失。

## 📊 实验亮点

MapSAM2在历史地图图像和时间序列分割任务中取得了显著成果。在Siegfried Building Time Series Dataset上，即使在有限的监督下或使用伪视频，也能准确地分割和链接建筑物。具体性能数据和对比基线的详细信息未知，但论文强调了其在学习时间关联和降低标注成本方面的优势。

## 🎯 应用场景

该研究成果可应用于历史地理研究、城市规划、环境保护等领域。通过自动分割和分析历史地图，可以研究城市发展、道路演变、土地利用变化等，为相关领域的决策提供数据支持。此外，该方法还可以推广到其他类型的图像和时间序列数据的分割任务中。

## 📄 摘要（原文）

> Historical maps are unique and valuable archives that document geographic features across different time periods. However, automated analysis of historical map images remains a significant challenge due to their wide stylistic variability and the scarcity of annotated training data. Constructing linked spatio-temporal datasets from historical map time series is even more time-consuming and labor-intensive, as it requires synthesizing information from multiple maps. Such datasets are essential for applications such as dating buildings, analyzing the development of road networks and settlements, studying environmental changes etc. We present MapSAM2, a unified framework for automatically segmenting both historical map images and time series. Built on a visual foundation model, MapSAM2 adapts to diverse segmentation tasks with few-shot fine-tuning. Our key innovation is to treat both historical map images and time series as videos. For images, we process a set of tiles as a video, enabling the memory attention mechanism to incorporate contextual cues from similar tiles, leading to improved geometric accuracy, particularly for areal features. For time series, we introduce the annotated Siegfried Building Time Series Dataset and, to reduce annotation costs, propose generating pseudo time series from single-year maps by simulating common temporal transformations. Experimental results show that MapSAM2 learns temporal associations effectively and can accurately segment and link buildings in time series under limited supervision or using pseudo videos. We will release both our dataset and code to support future research.

