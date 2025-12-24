---
layout: default
title: "DepthGait: Multi-Scale Cross-Level Feature Fusion of RGB-Derived Depth and Silhouette Sequences for Robust Gait Recognition"
---

# DepthGait: Multi-Scale Cross-Level Feature Fusion of RGB-Derived Depth and Silhouette Sequences for Robust Gait Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03397" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03397v1</a>
  <a href="https://arxiv.org/pdf/2508.03397.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03397v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03397v1', 'DepthGait: Multi-Scale Cross-Level Feature Fusion of RGB-Derived Depth and Silhouette Sequences for Robust Gait Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinzhu Li, Juepeng Zheng, Yikun Chen, Xudong Mao, Guanghui Yue, Wei Zhou, Chenlei Lv, Ruomei Wang, Fan Zhou, Baoquan Zhao

**分类**: cs.CV, cs.MM

**发布日期**: 2025-08-05

**DOI**: [10.1145/3746027.3755876](https://doi.org/10.1145/3746027.3755876)

---

## 💡 一句话要点

**提出DepthGait以解决步态识别中的模态融合问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `步态识别` `多模态融合` `深度学习` `特征提取` `计算机视觉`

## 📋 核心要点

1. 现有的步态识别方法主要依赖于二维轮廓和骨架，无法有效应对视角变化和细节捕捉的挑战。
2. 本文提出DepthGait框架，通过结合RGB衍生的深度图和轮廓，增强步态识别的区分能力。
3. 实验结果表明，DepthGait在多个标准数据集上取得了最先进的性能，显著提升了识别准确率。

## 📝 摘要（中文）

步态识别的鲁棒性依赖于高度区分性的表示，这与输入模态密切相关。尽管二进制轮廓和骨架在近期文献中占据主导地位，但这些二维表示无法充分捕捉处理视角变化所需的线索，也无法捕捉步态的细微和有意义的细节。本文提出了一种新颖的框架DepthGait，结合RGB衍生的深度图和轮廓以增强步态识别。该方法不仅利用人体的二维轮廓表示，还从给定的RGB图像序列中显式估计深度图，作为捕捉人类运动固有特征的新模态。此外，开发了一种新颖的多尺度和跨层融合方案，以弥合深度图和轮廓之间的模态差距。大量实验表明，DepthGait在标准基准上实现了与同行方法相比的最先进性能，并在具有挑战性的数据集上达到了令人印象深刻的平均Rank-1准确率。

## 🔬 方法详解

**问题定义**：步态识别面临的主要问题是现有方法依赖于二维轮廓和骨架，无法有效捕捉视角变化和细节信息，导致识别性能受限。

**核心思路**：DepthGait框架通过引入RGB衍生的深度图作为新模态，结合二维轮廓表示，旨在捕捉人类运动的更多区分性特征，从而提高步态识别的鲁棒性。

**技术框架**：该框架包括两个主要模块：首先，从RGB图像序列中估计深度图；其次，采用多尺度和跨层融合策略，将深度图与轮廓信息进行有效结合，以增强特征表示。

**关键创新**：DepthGait的创新之处在于其多尺度和跨层融合方案，能够有效弥合深度图和轮廓之间的模态差距，这在现有方法中尚未得到充分探索。

**关键设计**：在设计中，采用了特定的损失函数以优化模态融合效果，并通过深度学习网络结构来实现深度图和轮廓的特征提取与融合，确保了模型的高效性和准确性。

## 📊 实验亮点

DepthGait在多个标准数据集上实现了最先进的性能，具体表现为在挑战性数据集上达到了令人印象深刻的平均Rank-1准确率，显著优于现有的同行方法，展示了其在步态识别领域的强大能力。

## 🎯 应用场景

该研究在安防监控、智能交通、健康监测等领域具有广泛的应用潜力。通过提高步态识别的准确性，DepthGait可以有效支持人群行为分析、异常检测和个体识别等任务，未来可能推动相关技术的商业化应用。

## 📄 摘要（原文）

> Robust gait recognition requires highly discriminative representations, which are closely tied to input modalities. While binary silhouettes and skeletons have dominated recent literature, these 2D representations fall short of capturing sufficient cues that can be exploited to handle viewpoint variations, and capture finer and meaningful details of gait. In this paper, we introduce a novel framework, termed DepthGait, that incorporates RGB-derived depth maps and silhouettes for enhanced gait recognition. Specifically, apart from the 2D silhouette representation of the human body, the proposed pipeline explicitly estimates depth maps from a given RGB image sequence and uses them as a new modality to capture discriminative features inherent in human locomotion. In addition, a novel multi-scale and cross-level fusion scheme has also been developed to bridge the modality gap between depth maps and silhouettes. Extensive experiments on standard benchmarks demonstrate that the proposed DepthGait achieves state-of-the-art performance compared to peer methods and attains an impressive mean rank-1 accuracy on the challenging datasets.

