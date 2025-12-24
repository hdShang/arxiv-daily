---
layout: default
title: "MCTED: A Machine-Learning-Ready Dataset for Digital Elevation Model Generation From Mars Imagery"
---

# MCTED: A Machine-Learning-Ready Dataset for Digital Elevation Model Generation From Mars Imagery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08027" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08027v2</a>
  <a href="https://arxiv.org/pdf/2509.08027.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08027v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08027v2', 'MCTED: A Machine-Learning-Ready Dataset for Digital Elevation Model Generation From Mars Imagery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rafał Osadnik, Pablo Gómez, Eleni Bohacek, Rickbir Bahia

**分类**: cs.CV, cs.LG

**发布日期**: 2025-09-09 (更新: 2025-11-06)

**备注**: 22 pages, 21 figures

---

## 💡 一句话要点

**MCTED：一个为火星图像数字高程模型生成任务设计的机器学习数据集**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `火星` `数字高程模型` `数据集` `机器学习` `深度学习`

## 📋 核心要点

1. 现有火星DEM生成流程复杂，易产生伪影和数据缺失，影响后续机器学习模型的训练。
2. 论文构建了MCTED数据集，包含火星图像、DEM以及掩码，用于指示缺失或修改的数据，方便用户灵活处理。
3. 实验表明，在MCTED上训练的小型U-Net模型，性能优于零样本的深度估计基础模型DepthAnythingV2。

## 📝 摘要（中文）

本研究提出了一个名为MCTED的火星数字高程模型预测任务的新数据集，专为机器学习应用设计。该数据集通过一个综合流程生成，该流程处理了Day等人提供的高分辨率火星正射影像和DEM对，最终生成包含80,898个数据样本的数据集。源图像由火星勘测轨道飞行器使用CTX仪器收集，提供了对火星表面的非常多样化和全面的覆盖。考虑到大规模DEM中使用处理流程的复杂性，原始数据中经常存在伪影和缺失数据点，为此我们开发了工具来解决或减轻它们的影响。我们将处理后的样本分为训练集和验证集，确保两个集合中的样本不覆盖相互区域，以避免数据泄漏。数据集中的每个样本都由光学图像块、DEM块和两个掩码块表示，指示原始缺失或被我们更改的值。这允许数据集的未来用户随意处理更改后的高程区域。我们提供了生成的统计数据，包括样本的空间分布、高程值、坡度等的分布。最后，我们在MCTED数据集上训练了一个小型U-Net架构，并将其性能与单目深度估计基础模型DepthAnythingV2在高度预测任务上进行了比较。我们发现，即使是在该数据集上专门训练的非常小的架构，也胜过了像DepthAnythingV2这样的深度估计基础模型的零样本性能。我们将用于生成数据集和代码完全开源在公共存储库中。

## 🔬 方法详解

**问题定义**：论文旨在解决火星数字高程模型（DEM）生成任务中，现有数据集质量不高的问题。具体来说，现有DEM数据集中存在由于处理流程复杂而导致的伪影和缺失数据点，这些问题会影响机器学习模型的训练效果和泛化能力。因此，需要一个高质量、大规模、易于机器学习模型使用的数据集来提升火星DEM生成的精度和效率。

**核心思路**：论文的核心思路是构建一个高质量的火星DEM数据集，并通过精心设计的处理流程来解决原始数据中的伪影和缺失问题。该数据集不仅包含光学图像和DEM数据，还包含指示数据质量的掩码，允许用户灵活处理。此外，论文还通过划分训练集和验证集来避免数据泄露，保证模型的泛化能力。

**技术框架**：MCTED数据集的生成流程主要包括以下几个阶段：1) 数据源选择：使用火星勘测轨道飞行器（MRO）的CTX仪器获取的高分辨率火星正射影像和DEM数据。2) 数据预处理：开发工具来解决或减轻原始数据中的伪影和缺失数据点。3) 数据分割：将处理后的数据分割成80,898个样本，每个样本包含光学图像块、DEM块和两个掩码块。4) 数据划分：将样本划分为训练集和验证集，确保两个集合不覆盖相互区域。5) 数据统计：对生成的数据集进行统计分析，包括样本的空间分布、高程值、坡度等的分布。

**关键创新**：MCTED数据集的关键创新在于：1) 数据质量控制：通过开发工具来解决或减轻原始数据中的伪影和缺失数据点，提高了数据集的质量。2) 数据掩码：为每个样本提供指示数据质量的掩码，允许用户灵活处理。3) 数据划分：通过划分训练集和验证集来避免数据泄露，保证模型的泛化能力。

**关键设计**：在数据预处理阶段，论文开发了专门的工具来检测和修复原始数据中的伪影和缺失数据点。具体的技术细节未知，但掩码的设计允许用户在训练模型时灵活地处理这些区域，例如，可以忽略这些区域的损失，或者使用特定的方法来填充这些区域。此外，训练集和验证集的划分方式也保证了模型在未见过的数据上的泛化能力。

## 📊 实验亮点

实验结果表明，在MCTED数据集上训练的小型U-Net模型，在火星高程预测任务上，性能优于零样本的深度估计基础模型DepthAnythingV2。这表明，针对特定任务训练的小型模型，在高质量数据集的支持下，可以超越通用的大型模型。

## 🎯 应用场景

该数据集可广泛应用于火星地貌分析、地形重建、机器人导航、资源勘探等领域。高质量的DEM数据能够提升火星探测任务的安全性与效率，并为未来的火星殖民计划提供重要的数据支撑。此外，该数据集的构建方法也可推广到其他行星或卫星的DEM生成任务中。

## 📄 摘要（原文）

> This work presents a new dataset for the Martian digital elevation model prediction task, ready for machine learning applications called MCTED. The dataset has been generated using a comprehensive pipeline designed to process high-resolution Mars orthoimage and DEM pairs from Day et al., yielding a dataset consisting of 80,898 data samples. The source images are data gathered by the Mars Reconnaissance Orbiter using the CTX instrument, providing a very diverse and comprehensive coverage of the Martian surface. Given the complexity of the processing pipelines used in large-scale DEMs, there are often artefacts and missing data points in the original data, for which we developed tools to solve or mitigate their impact. We divide the processed samples into training and validation splits, ensuring samples in both splits cover no mutual areas to avoid data leakage. Every sample in the dataset is represented by the optical image patch, DEM patch, and two mask patches, indicating values that were originally missing or were altered by us. This allows future users of the dataset to handle altered elevation regions as they please. We provide statistical insights of the generated dataset, including the spatial distribution of samples, the distributions of elevation values, slopes and more. Finally, we train a small U-Net architecture on the MCTED dataset and compare its performance to a monocular depth estimation foundation model, DepthAnythingV2, on the task of elevation prediction. We find that even a very small architecture trained on this dataset specifically, beats a zero-shot performance of a depth estimation foundation model like DepthAnythingV2. We make the dataset and code used for its generation completely open source in public repositories.

