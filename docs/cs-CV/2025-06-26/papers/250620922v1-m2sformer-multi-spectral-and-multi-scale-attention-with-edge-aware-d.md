---
layout: default
title: "M2SFormer: Multi-Spectral and Multi-Scale Attention with Edge-Aware Difficulty Guidance for Image Forgery Localization"
---

# M2SFormer: Multi-Spectral and Multi-Scale Attention with Edge-Aware Difficulty Guidance for Image Forgery Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.20922" class="toolbar-btn" target="_blank">📄 arXiv: 2506.20922v1</a>
  <a href="https://arxiv.org/pdf/2506.20922.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.20922v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.20922v1', 'M2SFormer: Multi-Spectral and Multi-Scale Attention with Edge-Aware Difficulty Guidance for Image Forgery Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ju-Hyeon Nam, Dong-Hyun Moon, Sang-Chul Lee

**分类**: cs.CV

**发布日期**: 2025-06-26

**备注**: Accepted in International Conference on Computer Vision (ICCV) 2025

---

## 💡 一句话要点

**提出M2SFormer以解决图像伪造定位中的细节损失问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `图像伪造` `深度学习` `Transformer` `多尺度注意力` `图像处理` `数字取证` `伪造检测`

## 📋 核心要点

1. 现有的深度学习方法在图像伪造定位中存在计算开销大和表示能力有限的问题，尤其对于细微篡改的处理。
2. M2SFormer通过统一多频率和多尺度的注意力机制，结合全局上下文信息，提升了伪造伪影的捕捉能力。
3. 实验结果显示，M2SFormer在多个基准数据集上表现优异，超越了现有模型，尤其在未见领域的检测和定位能力上有显著提升。

## 📝 摘要（中文）

随着图像编辑技术的迅速发展，数字图像的创新应用与恶意操控并存。尽管基于深度学习的方法在像素级伪造定位中取得了高准确率，但在计算开销和表示能力方面仍面临挑战，尤其是对于细微或复杂的篡改。本文提出了M2SFormer，这是一种新颖的基于Transformer的编码器框架，旨在克服这些挑战。M2SFormer通过在跳跃连接中统一多频率和多尺度注意力，利用全局上下文更好地捕捉多样的伪造伪影。此外，框架通过利用全局先验图和曲率度量来引导难度引导注意力模块，从而更有效地保留细微的操控。大量实验表明，M2SFormer在多个基准数据集上超越了现有的最先进模型，在未见领域中检测和定位伪造的泛化能力更强。

## 🔬 方法详解

**问题定义**：本文旨在解决图像伪造定位中细节损失和计算开销大的问题。现有方法在处理复杂或细微篡改时表现不佳，难以有效捕捉伪造特征。

**核心思路**：M2SFormer通过在跳跃连接中整合多频率和多尺度的注意力机制，利用全局上下文信息来增强伪造特征的捕捉能力。此外，采用全局先验图和曲率度量来引导注意力模块，有效保留细微操控。

**技术框架**：M2SFormer的整体架构包括多个模块：首先是多频率和多尺度的注意力机制，然后是全局先验图的生成，最后是难度引导的注意力模块。这些模块协同工作，以提升伪造定位的精度和效率。

**关键创新**：M2SFormer的主要创新在于将多频率和多尺度注意力机制结合在一起，并通过全局先验图引导注意力模块，从而有效解决了细节损失的问题。这一设计与传统方法的分离处理方式形成鲜明对比。

**关键设计**：在网络结构上，M2SFormer采用了Transformer编码器架构，结合了跳跃连接和全局上下文信息。损失函数设计上，考虑了细节保留和伪造定位的综合效果，以优化模型性能。具体参数设置和超参数调优在实验中进行了详细探讨。

## 📊 实验亮点

在多个基准数据集上的实验结果显示，M2SFormer在伪造检测和定位任务中超越了现有最先进模型，尤其在未见领域的泛化能力上提升显著，具体性能提升幅度达到了XX%（具体数据未知）。

## 🎯 应用场景

M2SFormer在图像伪造检测和定位领域具有广泛的应用潜力，尤其适用于数字取证、社交媒体内容审核和新闻真实性验证等场景。随着图像编辑技术的不断发展，该研究的成果将为打击恶意操控提供有效工具，提升公众对数字内容的信任度。

## 📄 摘要（原文）

> Image editing techniques have rapidly advanced, facilitating both innovative use cases and malicious manipulation of digital images. Deep learning-based methods have recently achieved high accuracy in pixel-level forgery localization, yet they frequently struggle with computational overhead and limited representation power, particularly for subtle or complex tampering. In this paper, we propose M2SFormer, a novel Transformer encoder-based framework designed to overcome these challenges. Unlike approaches that process spatial and frequency cues separately, M2SFormer unifies multi-frequency and multi-scale attentions in the skip connection, harnessing global context to better capture diverse forgery artifacts. Additionally, our framework addresses the loss of fine detail during upsampling by utilizing a global prior map, a curvature metric indicating the difficulty of forgery localization, which then guides a difficulty-guided attention module to preserve subtle manipulations more effectively. Extensive experiments on multiple benchmark datasets demonstrate that M2SFormer outperforms existing state-of-the-art models, offering superior generalization in detecting and localizing forgeries across unseen domains.

