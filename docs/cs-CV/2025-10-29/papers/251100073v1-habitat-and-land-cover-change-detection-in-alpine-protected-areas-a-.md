---
layout: default
title: "Habitat and Land Cover Change Detection in Alpine Protected Areas: A Comparison of AI Architectures"
---

# Habitat and Land Cover Change Detection in Alpine Protected Areas: A Comparison of AI Architectures

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.00073" class="toolbar-btn" target="_blank">📄 arXiv: 2511.00073v1</a>
  <a href="https://arxiv.org/pdf/2511.00073.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.00073v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.00073v1', 'Habitat and Land Cover Change Detection in Alpine Protected Areas: A Comparison of AI Architectures')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harald Kristen, Daniel Kulmer, Manuela Hirschmugl

**分类**: cs.CV

**发布日期**: 2025-10-29

---

## 💡 一句话要点

**对比AI架构，解决高山保护区生境和土地覆盖变化检测难题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `高山生态系统` `变化检测` `深度学习` `地理空间基础模型` `多模态数据融合` `遥感图像处理` `土地覆盖变化`

## 📋 核心要点

1. 现有高山生境监测依赖人工测绘，成本高昂且难以满足频繁监测的需求，限制了对快速气候变化的响应。
2. 论文对比后分类变化检测和直接变化检测两种范式，并评估了地理空间基础模型和传统深度学习模型在高山环境中的性能。
3. 实验结果表明，地理空间基础模型Clay v1.0在多类生境变化检测中优于U-Net，且集成LiDAR数据能显著提升语义分割准确率。

## 📝 摘要（中文）

气候变化和干扰对高山生态系统造成影响，需要频繁的生境监测，但人工测绘成本过高。本文利用深度学习进行变化检测，使用奥地利Gesaeuse国家公园的长期高山生境数据，填补了地理空间基础模型（GFM）在复杂自然环境中应用的主要空白，这些环境具有模糊的类别边界和高度不平衡的类别。我们比较了两种范式：后分类变化检测（CD）与直接CD。对于后分类CD，我们评估了GFM Prithvi-EO-2.0和Clay v1.0与U-Net CNN的性能；对于直接CD，我们测试了transformer ChangeViT与U-Net基线。使用覆盖15.3平方公里、包含4480个记录变化的高分辨率多模态数据（RGB、NIR、LiDAR、地形属性），结果表明，Clay v1.0在多类生境变化检测中实现了51%的总体准确率，而U-Net为41%，两者在二元变化检测中均达到67%。直接CD在二元检测中产生更高的IoU（0.53 vs 0.35），但在多类检测中仅达到28%的准确率。跨时间评估显示了GFM的鲁棒性，Clay在2020年数据上保持了33%的准确率，而U-Net为23%。集成LiDAR将语义分割的准确率从30%提高到50%。虽然总体准确率低于更均匀的景观，但反映了复杂高山生境的实际性能。未来的工作将整合基于对象的后处理和物理约束，以增强适用性。

## 🔬 方法详解

**问题定义**：论文旨在解决高山保护区生境和土地覆盖变化检测问题。现有方法，特别是人工测绘，成本高昂且效率低下，无法满足频繁监测的需求。此外，高山环境的复杂性，如模糊的类别边界和高度不平衡的类别，对传统的遥感图像处理方法提出了挑战。

**核心思路**：论文的核心思路是利用深度学习技术，特别是地理空间基础模型（GFM）和卷积神经网络（CNN），实现自动化、高效的变化检测。通过比较后分类变化检测和直接变化检测两种范式，探索适用于复杂高山环境的最佳方法。同时，利用多模态数据（RGB、NIR、LiDAR、地形属性）提升模型的性能和鲁棒性。

**技术框架**：论文采用两种主要的变化检测框架：后分类变化检测和直接变化检测。后分类变化检测首先对不同时期的图像进行独立的语义分割，然后比较分割结果以检测变化。该框架评估了GFM（Prithvi-EO-2.0和Clay v1.0）和U-Net CNN。直接变化检测直接输入不同时期的图像对，输出变化区域。该框架测试了transformer ChangeViT和U-Net基线。整体流程包括数据预处理、模型训练、模型评估和结果分析。

**关键创新**：论文的关键创新在于将地理空间基础模型（GFM）应用于复杂的高山环境中进行生境和土地覆盖变化检测。与传统的深度学习模型相比，GFM具有更强的泛化能力和鲁棒性，能够更好地处理高山环境中的复杂性和不确定性。此外，论文还探索了多模态数据融合的方法，利用LiDAR数据提升语义分割的准确率。

**关键设计**：论文使用了多种深度学习模型，包括U-Net、ChangeViT、Prithvi-EO-2.0和Clay v1.0。U-Net作为基线模型，采用标准的卷积神经网络结构。ChangeViT是一种基于transformer的变化检测模型，能够捕捉图像中的长程依赖关系。Prithvi-EO-2.0和Clay v1.0是预训练的地理空间基础模型，具有强大的特征提取能力。论文使用了交叉熵损失函数进行模型训练，并采用总体准确率和IoU等指标进行模型评估。LiDAR数据通过与RGB、NIR图像进行通道拼接的方式进行融合。

## 📊 实验亮点

实验结果表明，地理空间基础模型Clay v1.0在多类生境变化检测中取得了51%的总体准确率，优于U-Net的41%。在二元变化检测中，两者均达到67%的准确率。直接变化检测方法ChangeViT在二元检测中取得了更高的IoU（0.53 vs 0.35）。集成LiDAR数据后，语义分割的准确率从30%提高到50%。跨时间评估显示，Clay在2020年数据上保持了33%的准确率，优于U-Net的23%。

## 🎯 应用场景

该研究成果可应用于高山保护区的生态环境监测、土地利用规划和气候变化影响评估。通过自动化、高效的变化检测，可以及时发现和应对生态环境问题，为保护高山生态系统的生物多样性和生态功能提供科学依据。此外，该方法还可以推广到其他复杂自然环境的变化检测应用中。

## 📄 摘要（原文）

> Rapid climate change and other disturbances in alpine ecosystems demand frequent habitat monitoring, yet manual mapping remains prohibitively expensive for the required temporal resolution. We employ deep learning for change detection using long-term alpine habitat data from Gesaeuse National Park, Austria, addressing a major gap in applying geospatial foundation models (GFMs) to complex natural environments with fuzzy class boundaries and highly imbalanced classes. We compare two paradigms: post-classification change detection (CD) versus direct CD. For post-classification CD, we evaluate GFMs Prithvi-EO-2.0 and Clay v1.0 against U-Net CNNs; for direct CD, we test the transformer ChangeViT against U-Net baselines. Using high-resolution multimodal data (RGB, NIR, LiDAR, terrain attributes) covering 4,480 documented changes over 15.3 km2, results show Clay v1.0 achieves 51% overall accuracy versus U-Net's 41% for multi-class habitat change, while both reach 67% for binary change detection. Direct CD yields superior IoU (0.53 vs 0.35) for binary but only 28% accuracy for multi-class detection. Cross-temporal evaluation reveals GFM robustness, with Clay maintaining 33% accuracy on 2020 data versus U-Net's 23%. Integrating LiDAR improves semantic segmentation from 30% to 50% accuracy. Although overall accuracies are lower than in more homogeneous landscapes, they reflect realistic performance for complex alpine habitats. Future work will integrate object-based post-processing and physical constraints to enhance applicability.

