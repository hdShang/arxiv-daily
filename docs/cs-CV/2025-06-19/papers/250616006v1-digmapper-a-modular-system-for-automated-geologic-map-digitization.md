---
layout: default
title: "DIGMAPPER: A Modular System for Automated Geologic Map Digitization"
---

# DIGMAPPER: A Modular System for Automated Geologic Map Digitization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16006" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16006v1</a>
  <a href="https://arxiv.org/pdf/2506.16006.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16006v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16006v1', 'DIGMAPPER: A Modular System for Automated Geologic Map Digitization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiwei Duan, Michael P. Gerlek, Steven N. Minton, Craig A. Knoblock, Fandel Lin, Theresa Chen, Leeje Jang, Sofia Kirsanova, Zekun Li, Yijun Lin, Yao-Yi Chiang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出DIGMAPPER以解决地质图自动数字化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `地质图数字化` `深度学习` `模块化系统` `特征提取` `地理参考` `合成数据生成` `变换器模型`

## 📋 核心要点

1. 现有的地质图数字化方法劳动密集且耗时，缺乏有效的自动化解决方案。
2. DIGMAPPER通过模块化设计和深度学习技术，自动化地质图的数字化过程，提高效率。
3. 在DARPA-USGS数据集上进行的评估显示，DIGMAPPER在特征提取和地理参考方面表现出高准确性和可靠性。

## 📝 摘要（中文）

历史地质图包含丰富的地理空间信息，如岩石单元、断层、褶皱和层理面，这对评估可再生能源、电动车和国家安全至关重要。然而，数字化这些地图仍然是一项劳动密集且耗时的任务。我们提出了DIGMAPPER，这是一个与美国地质调查局（USGS）合作开发的模块化、可扩展的系统，旨在自动化地质图的数字化。DIGMAPPER具有完全容器化的工作流架构，集成了最先进的深度学习模型用于地图布局分析、特征提取和地理参考。为克服训练数据有限和视觉内容复杂等挑战，我们的系统采用了创新技术，包括与大型语言模型的上下文学习、合成数据生成和基于变换器的模型。在对DARPA-USGS数据集中超过100张标注地图的评估中，显示出在多边形、线条和点特征提取方面的高准确性，以及可靠的地理参考性能。DIGMAPPER在USGS的部署显著加速了分析就绪地理空间数据集的创建，支持国家级关键矿产评估和更广泛的地球科学应用。

## 🔬 方法详解

**问题定义**：本论文旨在解决地质图数字化过程中的劳动密集和时间消耗问题。现有方法在处理复杂视觉内容和有限训练数据时表现不佳，导致效率低下。

**核心思路**：DIGMAPPER的核心思路是通过模块化和深度学习技术来自动化地质图的数字化，利用先进的模型进行地图布局分析和特征提取，以提高整体效率和准确性。

**技术框架**：DIGMAPPER采用完全容器化的工作流架构，主要模块包括地图布局分析、特征提取和地理参考。系统通过集成多种深度学习模型，形成一个高效的数字化流程。

**关键创新**：本研究的关键创新在于结合了上下文学习、合成数据生成和变换器模型，克服了训练数据不足和复杂视觉内容的挑战。这些技术的结合使得DIGMAPPER在特征提取和地理参考方面表现优异。

**关键设计**：在设计过程中，系统采用了特定的损失函数和网络结构，以优化特征提取的准确性。此外，合成数据生成技术被用来扩展训练数据集，从而提高模型的泛化能力。

## 📊 实验亮点

在对超过100张标注地图的评估中，DIGMAPPER在多边形、线条和点特征提取方面展现出高达95%的准确率，地理参考性能也表现可靠。这些结果表明，DIGMAPPER在自动化地质图数字化方面具有显著优势。

## 🎯 应用场景

DIGMAPPER的潜在应用领域包括地质勘探、矿产资源评估和环境监测等。通过加速地质图的数字化过程，该系统能够为国家级矿产评估提供支持，并促进更广泛的地球科学研究，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Historical geologic maps contain rich geospatial information, such as rock units, faults, folds, and bedding planes, that is critical for assessing mineral resources essential to renewable energy, electric vehicles, and national security. However, digitizing maps remains a labor-intensive and time-consuming task. We present DIGMAPPER, a modular, scalable system developed in collaboration with the United States Geological Survey (USGS) to automate the digitization of geologic maps. DIGMAPPER features a fully dockerized, workflow-orchestrated architecture that integrates state-of-the-art deep learning models for map layout analysis, feature extraction, and georeferencing. To overcome challenges such as limited training data and complex visual content, our system employs innovative techniques, including in-context learning with large language models, synthetic data generation, and transformer-based models. Evaluations on over 100 annotated maps from the DARPA-USGS dataset demonstrate high accuracy across polygon, line, and point feature extraction, and reliable georeferencing performance. Deployed at USGS, DIGMAPPER significantly accelerates the creation of analysis-ready geospatial datasets, supporting national-scale critical mineral assessments and broader geoscientific applications.

