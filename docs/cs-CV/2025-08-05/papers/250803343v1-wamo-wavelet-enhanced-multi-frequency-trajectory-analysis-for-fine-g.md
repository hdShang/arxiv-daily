---
layout: default
title: "WaMo: Wavelet-Enhanced Multi-Frequency Trajectory Analysis for Fine-Grained Text-Motion Retrieval"
---

# WaMo: Wavelet-Enhanced Multi-Frequency Trajectory Analysis for Fine-Grained Text-Motion Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.03343" class="toolbar-btn" target="_blank">📄 arXiv: 2508.03343v1</a>
  <a href="https://arxiv.org/pdf/2508.03343.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.03343v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.03343v1', 'WaMo: Wavelet-Enhanced Multi-Frequency Trajectory Analysis for Fine-Grained Text-Motion Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junlong Ren, Gangjian Zhang, Honghao Fu, Pengcheng Wu, Hao Wang

**分类**: cs.CV

**发布日期**: 2025-08-05

---

## 💡 一句话要点

**提出WaMo框架以解决文本与3D动作序列匹配问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `文本-动作检索` `小波变换` `多频特征提取` `时空动态` `运动序列预测`

## 📋 核心要点

1. 现有文本-动作检索方法未能有效处理人体复杂结构和时空动态，导致语义对齐不准确。
2. WaMo框架通过小波变换提取多频特征，捕捉部位特定的运动细节，实现精确的文本与动作对齐。
3. 实验结果显示，WaMo在HumanML3D和KIT-ML数据集上分别提升了17.0%和18.2%的性能，优于现有方法。

## 📝 摘要（中文）

文本-动作检索（TMR）旨在检索与文本描述语义相关的3D动作序列。然而，由于人体结构复杂及其时空动态，匹配3D动作与文本仍然具有高度挑战性。现有方法往往忽视这些复杂性，依赖于通用编码方法，未能区分不同身体部位及其动态，限制了精确的语义对齐。为此，本文提出了WaMo，一个基于小波的多频特征提取框架，能够全面捕捉身体关节在多个分辨率下的部位特定和时变运动细节，从而提取出具有区分性的运动特征，实现与文本的细粒度对齐。WaMo的三个关键组件包括：轨迹小波分解、轨迹小波重构和无序运动序列预测。大量实验表明，WaMo在HumanML3D和KIT-ML数据集上分别提升了17.0%和18.2%的$Rsum$，超越了现有的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决文本与3D动作序列之间的匹配问题，现有方法由于忽视人体结构复杂性和动态特征，导致语义对齐效果不佳。

**核心思路**：WaMo框架通过小波变换实现多频特征提取，能够捕捉到不同身体部位的运动细节和时变特征，从而提高文本与动作的对齐精度。

**技术框架**：WaMo的整体架构包括三个主要模块：轨迹小波分解、轨迹小波重构和无序运动序列预测。轨迹小波分解将运动信号分解为频率成分，轨迹小波重构则通过可学习的逆小波变换重建原始关节轨迹，而无序运动序列预测则通过重新排序运动序列来增强时序一致性学习。

**关键创新**：WaMo的核心创新在于其小波基础的多频特征提取方法，能够有效捕捉局部运动细节和全局运动语义，这与现有方法的通用编码方式有本质区别。

**关键设计**：在设计中，WaMo采用了可学习的逆小波变换以确保重建过程中保留重要的时空信息，同时在无序运动序列预测中引入了序列重排序机制，以提升模型对时序一致性的学习能力。

## 📊 实验亮点

WaMo在HumanML3D和KIT-ML数据集上分别实现了17.0%和18.2%的$Rsum$性能提升，显著超越了现有的最先进方法，证明了其在文本-动作检索任务中的有效性和优越性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在虚拟现实、动画制作和人机交互等领域。通过实现更精确的文本与动作匹配，WaMo能够提升用户体验，推动相关技术的发展。此外，未来可能在其他多模态检索任务中得到应用，进一步拓展其影响力。

## 📄 摘要（原文）

> Text-Motion Retrieval (TMR) aims to retrieve 3D motion sequences semantically relevant to text descriptions. However, matching 3D motions with text remains highly challenging, primarily due to the intricate structure of human body and its spatial-temporal dynamics. Existing approaches often overlook these complexities, relying on general encoding methods that fail to distinguish different body parts and their dynamics, limiting precise semantic alignment. To address this, we propose WaMo, a novel wavelet-based multi-frequency feature extraction framework. It fully captures part-specific and time-varying motion details across multiple resolutions on body joints, extracting discriminative motion features to achieve fine-grained alignment with texts. WaMo has three key components: (1) Trajectory Wavelet Decomposition decomposes motion signals into frequency components that preserve both local kinematic details and global motion semantics. (2) Trajectory Wavelet Reconstruction uses learnable inverse wavelet transforms to reconstruct original joint trajectories from extracted features, ensuring the preservation of essential spatial-temporal information. (3) Disordered Motion Sequence Prediction reorders shuffled motion sequences to improve the learning of inherent temporal coherence, enhancing motion-text alignment. Extensive experiments demonstrate WaMo's superiority, achieving 17.0\% and 18.2\% improvements in $Rsum$ on HumanML3D and KIT-ML datasets, respectively, outperforming existing state-of-the-art (SOTA) methods.

