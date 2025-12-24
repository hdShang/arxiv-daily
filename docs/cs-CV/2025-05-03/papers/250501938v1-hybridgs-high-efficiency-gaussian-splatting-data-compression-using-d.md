---
layout: default
title: HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder
---

# HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01938" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01938v1</a>
  <a href="https://arxiv.org/pdf/2505.01938.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01938v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01938v1', 'HybridGS: High-Efficiency Gaussian Splatting Data Compression using Dual-Channel Sparse Representation and Point Cloud Encoder')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qi Yang, Le Yang, Geert Van Der Auwera, Zhu Li

**分类**: cs.CV, eess.IV

**发布日期**: 2025-05-03

**备注**: Accepted by ICML2025

**🔗 代码/项目**: [GITHUB](https://github.com/Qi-Yangsjtu/HybridGS)

---

## 💡 一句话要点

**提出HybridGS以解决3D高斯点云压缩效率低的问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D高斯点云` `数据压缩` `稀疏表示` `点云编码` `速率控制` `虚拟现实` `增强现实`

## 📋 核心要点

1. 现有的3D高斯点云压缩方法编码时间长且格式定制，限制了其应用。
2. HybridGS框架通过双通道稀疏表示和标准点云编码实现高效压缩。
3. 实验显示HybridGS在编码速度上显著提升，同时重建性能与先进方法相当。

## 📝 摘要（中文）

现有的3D高斯点云压缩方案主要依赖隐式数据嵌入，导致编码时间长且数据格式高度定制，限制了其广泛应用。本文提出了一种新的3D高斯点云压缩框架HybridGS，结合了紧凑生成和标准化点云数据编码。HybridGS首先生成紧凑且明确的3D高斯点云数据，采用双通道稀疏表示来监督原始位置和特征位深。接着，利用规范的点云编码器进一步压缩数据并形成标准输出比特流。实验结果表明，HybridGS在编码和解码速度上显著提高，同时在重建性能上与现有最先进的方法相当。

## 🔬 方法详解

**问题定义**：现有的3D高斯点云压缩方法往往依赖隐式数据嵌入，导致编码时间较长且数据格式高度定制，难以实现广泛部署。

**核心思路**：HybridGS框架通过生成紧凑且明确的3D高斯点云数据，结合双通道稀疏表示和标准化编码，旨在提高压缩效率和解码速度。

**技术框架**：该框架主要分为两个阶段：首先生成紧凑的3D高斯点云数据，然后利用规范的点云编码器进行进一步压缩，最终形成标准输出比特流。

**关键创新**：HybridGS的核心创新在于引入双通道稀疏表示来监督原始位置和特征位深，这一设计显著提高了数据压缩的效率。

**关键设计**：在参数设置上，HybridGS采用了简单有效的速率控制方案，确保数据压缩的可解释性，同时未引入提升3D高斯点云质量的模块。

## 📊 实验亮点

实验结果表明，HybridGS在编码和解码速度上显著提高，编码速度比现有方法快，且重建性能与最先进的方法相当，展示了其在实际应用中的有效性。

## 🎯 应用场景

HybridGS在3D点云数据压缩领域具有广泛的应用潜力，适用于虚拟现实、增强现实和自动驾驶等场景。其高效的编码和解码速度将促进实时3D数据处理的实现，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Most existing 3D Gaussian Splatting (3DGS) compression schemes focus on producing compact 3DGS representation via implicit data embedding. They have long coding times and highly customized data format, making it difficult for widespread deployment. This paper presents a new 3DGS compression framework called HybridGS, which takes advantage of both compact generation and standardized point cloud data encoding. HybridGS first generates compact and explicit 3DGS data. A dual-channel sparse representation is introduced to supervise the primitive position and feature bit depth. It then utilizes a canonical point cloud encoder to perform further data compression and form standard output bitstreams. A simple and effective rate control scheme is proposed to pivot the interpretable data compression scheme. At the current stage, HybridGS does not include any modules aimed at improving 3DGS quality during generation. But experiment results show that it still provides comparable reconstruction performance against state-of-the-art methods, with evidently higher encoding and decoding speed. The code is publicly available at https://github.com/Qi-Yangsjtu/HybridGS.

