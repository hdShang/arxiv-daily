---
layout: default
title: FLaTEC: Frequency-Disentangled Latent Triplanes for Efficient Compression of LiDAR Point Clouds
---

# FLaTEC: Frequency-Disentangled Latent Triplanes for Efficient Compression of LiDAR Point Clouds

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20065" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20065v1</a>
  <a href="https://arxiv.org/pdf/2511.20065.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20065v1" onclick="toggleFavorite(this, '2511.20065v1', 'FLaTEC: Frequency-Disentangled Latent Triplanes for Efficient Compression of LiDAR Point Clouds')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoge Zhang, Zijie Wu, Mingtao Feng, Zichen Geng, Mehwish Nasim, Saeed Anwar, Ajmal Mian

**分类**: cs.CV

**发布日期**: 2025-11-25

---

## 💡 一句话要点

**FLaTEC：提出频率解耦的隐式三平面表示，高效压缩LiDAR点云。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `点云压缩` `LiDAR` `频率解耦` `隐式表示` `三平面`

## 📋 核心要点

1. 现有点云压缩方法难以平衡压缩率和重建质量，因为低频和高频分量在相同分辨率下的贡献不同。
2. FLaTEC通过频率解耦机制分离低频结构和高频纹理，并使用隐式三平面作为点云的紧凑表示。
3. 实验结果表明，FLaTEC在SemanticKITTI和Ford数据集上显著优于现有方法，BD-rate分别提升78%和94%。

## 📝 摘要（中文）

本文提出了一种频率感知的点云压缩模型FLaTEC，旨在实现高压缩率下的全扫描点云压缩。该模型通过频率感知机制解耦低频结构和高频纹理，并利用隐式三平面作为点云的紧凑代理。具体而言，首先将体素化嵌入转换为三平面表示，以降低稀疏性、计算成本和存储需求。然后，设计了一种频率解耦技术，提取紧凑的低频内容，同时收集跨尺度的高频细节。解耦后的低频和高频分量以二进制格式存储。在解码过程中，通过调制块逐步恢复全频谱信号。此外，为了弥补3D相关性的损失，引入了一种高效的基于频率的注意力机制，以促进局部连通性并输出任意分辨率的点。在SemanticKITTI和Ford数据集上，该方法在BD-rate指标上分别优于标准编解码器78%和94%，实现了最先进的率失真性能。

## 🔬 方法详解

**问题定义**：现有点云压缩方法在压缩率和重建质量之间难以取得平衡。这是因为点云中的低频结构和高频纹理对重建的贡献不同，但在传统方法中往往被同等对待。此外，直接处理稀疏点云数据会导致较高的计算成本和存储需求。

**核心思路**：FLaTEC的核心思路是将点云数据分解为低频和高频分量，并分别进行压缩。低频分量主要包含点云的整体结构信息，高频分量则包含细节纹理信息。通过对不同频率分量进行差异化处理，可以在保证重建质量的同时提高压缩率。此外，使用隐式三平面表示可以有效地降低点云的稀疏性，减少计算和存储开销。

**技术框架**：FLaTEC的整体框架包括以下几个主要阶段：1) 体素化嵌入：将原始点云数据转换为体素化表示。2) 三平面转换：将体素化嵌入转换为三平面表示，降低稀疏性。3) 频率解耦：使用频率解耦模块将三平面表示分解为低频和高频分量。4) 压缩编码：对解耦后的低频和高频分量进行压缩编码。5) 解码与重建：解码压缩后的数据，并通过调制块逐步恢复全频谱信号，最后通过频率注意力机制重建点云。

**关键创新**：FLaTEC的关键创新在于频率解耦机制和隐式三平面表示的结合。频率解耦机制能够有效地分离点云中的低频和高频信息，从而实现更高效的压缩。隐式三平面表示则能够降低点云的稀疏性，减少计算和存储开销。此外，频率注意力机制能够增强局部连通性，提高重建质量。

**关键设计**：频率解耦模块采用多尺度卷积和池化操作，提取不同频率的特征。隐式三平面表示通过将三维空间中的点映射到三个二维平面上，从而降低数据的维度和稀疏性。频率注意力机制通过计算不同频率分量之间的相关性，自适应地调整权重，从而增强局部连通性。损失函数包括率失真损失，用于平衡压缩率和重建质量。

## 📊 实验亮点

FLaTEC在SemanticKITTI和Ford数据集上取得了显著的性能提升。在SemanticKITTI数据集上，FLaTEC的BD-rate比标准编解码器降低了78%。在Ford数据集上，BD-rate降低了94%。这些结果表明，FLaTEC在点云压缩方面具有显著的优势，能够实现更高的压缩率和更好的重建质量。

## 🎯 应用场景

FLaTEC可应用于自动驾驶、机器人导航、三维地图构建等领域。通过高效压缩LiDAR点云数据，可以降低存储和传输成本，提高系统的实时性和效率。该研究的成果有助于推动三维视觉技术在实际场景中的应用，并为未来的三维数据处理和分析提供新的思路。

## 📄 摘要（原文）

> Point cloud compression methods jointly optimize bitrates and reconstruction distortion. However, balancing compression ratio and reconstruction quality is difficult because low-frequency and high-frequency components contribute differently at the same resolution. To address this, we propose FLaTEC, a frequency-aware compression model that enables the compression of a full scan with high compression ratios. Our approach introduces a frequency-aware mechanism that decouples low-frequency structures and high-frequency textures, while hybridizing latent triplanes as a compact proxy for point cloud. Specifically, we convert voxelized embeddings into triplane representations to reduce sparsity, computational cost, and storage requirements. We then devise a frequency-disentangling technique that extracts compact low-frequency content while collecting high-frequency details across scales. The decoupled low-frequency and high-frequency components are stored in binary format. During decoding, full-spectrum signals are progressively recovered via a modulation block. Additionally, to compensate for the loss of 3D correlation, we introduce an efficient frequency-based attention mechanism that fosters local connectivity and outputs arbitrary resolution points. Our method achieves state-of-the-art rate-distortion performance and outperforms the standard codecs by 78\% and 94\% in BD-rate on both SemanticKITTI and Ford datasets.

