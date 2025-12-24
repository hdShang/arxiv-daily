---
layout: default
title: "TerraFM: A Scalable Foundation Model for Unified Multisensor Earth Observation"
---

# TerraFM: A Scalable Foundation Model for Unified Multisensor Earth Observation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06281" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06281v1</a>
  <a href="https://arxiv.org/pdf/2506.06281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06281v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06281v1', 'TerraFM: A Scalable Foundation Model for Unified Multisensor Earth Observation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Sohail Danish, Muhammad Akhtar Munir, Syed Roshaan Ali Shah, Muhammad Haris Khan, Rao Muhammad Anwer, Jorma Laaksonen, Fahad Shahbaz Khan, Salman Khan

**分类**: cs.CV

**发布日期**: 2025-06-06

**🔗 代码/项目**: [GITHUB](https://github.com/mbzuai-oryx/TerraFM)

---

## 💡 一句话要点

**提出TerraFM以解决多传感器地球观测数据的统一学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `地球观测` `自监督学习` `多模态融合` `深度学习` `遥感技术`

## 📋 核心要点

1. 现有的地球观测模型在规模、地理覆盖和光谱多样性上存在局限，影响了其泛化能力。
2. TerraFM通过自监督学习结合多种传感器影像，采用模态特定补丁嵌入和交叉注意力机制来统一不同输入。
3. 实验结果显示，TerraFM在分类和分割任务上超越了现有模型，尤其在GEO-Bench和Copernicus-Bench上表现优异。

## 📝 摘要（中文）

现代地球观测（EO）越来越依赖深度学习来利用跨传感器和区域的卫星影像的规模和多样性。尽管近期的基础模型在EO任务上展现了良好的泛化能力，但许多模型仍受限于训练数据的规模、地理覆盖和光谱多样性，这些因素对学习全球可迁移的表示至关重要。本研究提出了TerraFM，一个可扩展的自监督学习模型，利用全球分布的Sentinel-1和Sentinel-2影像，结合大空间块和土地覆盖感知采样，以丰富空间和语义覆盖。通过将感知模态视为自监督方法中的自然增强，我们通过模态特定的补丁嵌入和自适应交叉注意力融合来统一雷达和光学输入。TerraFM在分类和分割任务上表现出强大的泛化能力，在GEO-Bench和Copernicus-Bench上超越了先前的模型。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有地球观测模型在训练数据规模和多样性上的不足，特别是如何有效利用多种传感器数据进行统一学习。

**核心思路**：论文提出的核心思路是通过自监督学习结合不同传感器的影像数据，利用模态特定的补丁嵌入和自适应交叉注意力机制来增强模型的泛化能力。

**技术框架**：TerraFM的整体架构包括数据预处理、模态嵌入、交叉注意力融合和对比学习等主要模块。首先，利用Sentinel-1和Sentinel-2影像进行数据采样，然后通过补丁嵌入将不同模态数据统一表示，最后通过对比学习进行模型训练。

**关键创新**：最重要的技术创新在于引入了双中心机制和类频感知正则化，以应对土地覆盖的长尾分布问题，这在现有模型中尚未得到有效解决。

**关键设计**：在参数设置上，采用了大空间块和土地覆盖感知采样，损失函数结合了对比损失和类频正则化，网络结构则通过交叉注意力机制实现模态融合。

## 📊 实验亮点

TerraFM在分类和分割任务上表现出色，尤其在GEO-Bench和Copernicus-Bench上，超越了先前的模型，显示出显著的性能提升。具体而言，模型在多个基准测试中实现了更高的准确率和更好的泛化能力，验证了其在多模态学习中的有效性。

## 🎯 应用场景

TerraFM的研究成果在多个领域具有潜在应用价值，包括环境监测、城市规划、农业管理等。通过统一处理多种传感器数据，能够更准确地进行土地覆盖分类和变化检测，从而为决策提供科学依据。未来，该模型有望推动地球观测技术的进一步发展，提升数据利用效率。

## 📄 摘要（原文）

> Modern Earth observation (EO) increasingly leverages deep learning to harness the scale and diversity of satellite imagery across sensors and regions. While recent foundation models have demonstrated promising generalization across EO tasks, many remain limited by the scale, geographical coverage, and spectral diversity of their training data, factors critical for learning globally transferable representations. In this work, we introduce TerraFM, a scalable self-supervised learning model that leverages globally distributed Sentinel-1 and Sentinel-2 imagery, combined with large spatial tiles and land-cover aware sampling to enrich spatial and semantic coverage. By treating sensing modalities as natural augmentations in our self-supervised approach, we unify radar and optical inputs via modality-specific patch embeddings and adaptive cross-attention fusion. Our training strategy integrates local-global contrastive learning and introduces a dual-centering mechanism that incorporates class-frequency-aware regularization to address long-tailed distributions in land cover.TerraFM achieves strong generalization on both classification and segmentation tasks, outperforming prior models on GEO-Bench and Copernicus-Bench. Our code and pretrained models are publicly available at: https://github.com/mbzuai-oryx/TerraFM .

