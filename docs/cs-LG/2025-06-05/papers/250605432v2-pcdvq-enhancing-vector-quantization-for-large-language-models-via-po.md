---
layout: default
title: "PCDVQ: Enhancing Vector Quantization for Large Language Models via Polar Coordinate Decoupling"
---

# PCDVQ: Enhancing Vector Quantization for Large Language Models via Polar Coordinate Decoupling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05432" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05432v2</a>
  <a href="https://arxiv.org/pdf/2506.05432.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05432v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05432v2', 'PCDVQ: Enhancing Vector Quantization for Large Language Models via Polar Coordinate Decoupling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxuan Yue, Zukang Xu, Zhihang Yuan, Dawei Yang, Jianlong Wu, Liqiang Nie

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-05 (更新: 2025-06-26)

---

## 💡 一句话要点

**提出PCDVQ以解决大语言模型量化精度不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `向量量化` `极坐标解耦` `大语言模型` `边缘计算` `模型压缩` `零-shot学习` `分布对齐`

## 📋 核心要点

1. 现有的向量量化方法在处理大语言模型时，往往无法有效平衡方向和幅度的量化精度，导致性能下降。
2. 本文提出的PCDVQ方法通过极坐标解耦，将向量的方向和幅度进行独立量化，从而提高量化精度。
3. 实验结果显示，PCDVQ在2比特量化下的零-shot任务准确率比基线方法提高了至少1.5%，展现了其有效性。

## 📝 摘要（中文）

大语言模型（LLMs）在边缘部署中面临参数规模庞大的挑战。向量量化（VQ）作为一种聚类基础的量化方法，因其极低的比特数（甚至可达2比特）和较高的准确性而广泛应用。现有VQ方法通常以耦合的方式对向量进行量化，但研究发现，方向对量化的敏感性显著高于幅度。本文提出了极坐标解耦向量量化（PCDVQ），通过极坐标解耦和分布对齐码本构建两个关键模块，实现方向和幅度的独立量化。实验结果表明，PCDVQ在2比特水平下的零-shot准确率至少提高了1.5%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有向量量化方法在大语言模型中量化精度不足的问题，尤其是方向和幅度耦合量化导致的性能下降。

**核心思路**：提出极坐标解耦的思想，将向量转换为极坐标表示，分别对方向和幅度进行独立量化，以减少量化误差。

**技术框架**：PCDVQ框架包含两个主要模块：极坐标解耦（PCD）和分布对齐码本构建（DACC）。PCD模块负责将向量转换为极坐标形式并进行独立量化，DACC模块则优化方向和幅度的码本以符合源分布。

**关键创新**：最重要的创新在于提出了极坐标解耦的量化方法，突破了传统VQ方法的耦合限制，显著提高了量化精度。

**关键设计**：在设计中，采用了适应性聚类中心设置，确保方向和幅度的量化能够有效反映源数据的分布特征，同时优化了损失函数以平衡方向和幅度的量化误差。

## 📊 实验亮点

实验结果表明，PCDVQ在2比特量化下的零-shot任务准确率比基线方法提高了至少1.5%。这一提升不仅验证了方法的有效性，也为大语言模型的高效部署提供了新的思路。

## 🎯 应用场景

该研究的潜在应用领域包括边缘计算、移动设备上的大语言模型部署以及实时自然语言处理任务。通过提高量化精度，PCDVQ能够在资源受限的环境中实现高效的模型推理，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Large Language Models (LLMs) face significant challenges in edge deployment due to their massive parameter scale. Vector Quantization (VQ), a clustering-based quantization method, serves as a prevalent solution to this issue for its extremely low-bit (even at 2-bit) and considerable accuracy. Since a vector is a quantity in mathematics and physics that has both direction and magnitude, existing VQ works typically quantize them in a coupled manner. However, we find that direction exhibits significantly greater sensitivity to quantization compared to the magnitude. For instance, when separately clustering the directions and magnitudes of weight vectors in LLaMA-2-7B, the accuracy drop of zero-shot tasks are 46.5\% and 2.3\%, respectively. This gap even increases with the reduction of clustering centers. Further, Euclidean distance, a common metric to access vector similarities in current VQ works, places greater emphasis on reducing the magnitude error. This property is contrary to the above finding, unavoidably leading to larger quantization errors. To these ends, this paper proposes Polar Coordinate Decoupled Vector Quantization (PCDVQ), an effective and efficient VQ framework consisting of two key modules: 1) Polar Coordinate Decoupling (PCD), which transforms vectors into their polar coordinate representations and perform independent quantization of the direction and magnitude parameters.2) Distribution Aligned Codebook Construction (DACC), which optimizes the direction and magnitude codebooks in accordance with the source distribution. Experimental results show that PCDVQ outperforms baseline methods at 2-bit level by at least 1.5\% zero-shot accuracy, establishing a novel paradigm for accurate and highly compressed LLMs.

