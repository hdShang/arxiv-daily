---
layout: default
title: Hybrid Convolution and Frequency State Space Network for Image Compression
---

# Hybrid Convolution and Frequency State Space Network for Image Compression

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.20151" class="toolbar-btn" target="_blank">📄 arXiv: 2511.20151v1</a>
  <a href="https://arxiv.org/pdf/2511.20151.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.20151v1" onclick="toggleFavorite(this, '2511.20151v1', 'Hybrid Convolution and Frequency State Space Network for Image Compression')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haodong Pan, Hao Wei, Yusong Wang, Nanning Zheng, Caigui Jiang

**分类**: cs.CV

**发布日期**: 2025-11-25

**备注**: 36 pages, 8 figures

---

## 💡 一句话要点

**提出HCFSSNet，一种混合卷积和频率状态空间网络的图像压缩方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `图像压缩` `卷积神经网络` `状态空间模型` `频率调制` `自适应比特分配`

## 📋 核心要点

1. 现有基于Transformer和SSM的图像压缩方法，虽然具有长程建模能力，但可能丢失结构信息或忽略频率特征。
2. HCFSSNet结合CNN提取高频信息，并提出VFSS块建模低频信息，利用AFMM进行频率调制，实现高效比特分配。
3. 实验表明，HCFSSNet在Kodak等数据集上，相比VTM锚点显著降低BD率，且参数量更少，性能优于现有SSM方法。

## 📝 摘要（中文）

本文提出了一种混合卷积和频率状态空间网络（HCFSSNet）用于学习图像压缩。卷积神经网络（CNN）能够有效捕获局部高频细节，而Transformer和状态空间模型（SSM）提供强大的长程建模能力，但可能导致结构信息丢失或忽略对压缩至关重要的频率特征。HCFSSNet利用CNN提取局部高频结构，并引入视觉频率状态空间（VFSS）块来建模长程低频信息。VFSS块结合了全向邻域状态空间（VONSS）模块（水平、垂直和对角扫描特征）以及自适应频率调制模块（AFMM）（对离散余弦变换频率分量进行内容自适应加权，以实现更有效的比特分配）。为了进一步减少熵模型中的冗余，我们将AFMM与Swin Transformer集成，形成频率感知的Swin Transformer注意力模块（FSTAM），用于频率感知的边信息建模。在Kodak、Tecnick和CLIC Professional Validation数据集上的实验表明，与最近基于SSM的编解码器（如MambaIC）相比，HCFSSNet实现了具有竞争力的率失真性能，同时使用的参数明显更少。在Kodak、Tecnick和CLIC上，HCFSSNet相对于VTM锚点分别降低了18.06%、24.56%和22.44%的BD率，为未来的学习图像压缩系统提供了一种高效且可解释的混合架构。

## 🔬 方法详解

**问题定义**：现有的基于Transformer和SSM的图像压缩方法在建模长程依赖关系方面表现出色，但它们在捕获局部高频细节和保持图像的结构信息方面存在不足。此外，这些方法通常忽略了图像压缩中至关重要的频率特征，导致压缩效率降低。

**核心思路**：HCFSSNet的核心思路是将CNN的局部高频特征提取能力与状态空间模型（SSM）的长程依赖建模能力相结合，并引入频率调制机制，以实现更高效的图像压缩。通过这种混合架构，模型可以同时捕获图像的局部细节和全局结构，并根据内容自适应地分配比特，从而提高压缩效率。

**技术框架**：HCFSSNet的整体架构包括以下几个主要模块：1) CNN模块：用于提取图像的局部高频特征。2) 视觉频率状态空间（VFSS）块：用于建模长程低频信息，VFSS块由全向邻域状态空间（VONSS）模块和自适应频率调制模块（AFMM）组成。3) 频率感知的Swin Transformer注意力模块（FSTAM）：用于频率感知的边信息建模，进一步减少熵模型中的冗余。

**关键创新**：HCFSSNet的关键创新在于VFSS块的设计，它将VONSS模块和AFMM模块相结合，实现了对图像频率特征的自适应建模。VONSS模块通过水平、垂直和对角扫描特征，捕捉图像的全局结构信息。AFMM模块则通过对离散余弦变换（DCT）频率分量进行内容自适应加权，实现了更有效的比特分配。此外，FSTAM模块通过将AFMM与Swin Transformer集成，进一步提高了边信息建模的效率。

**关键设计**：AFMM模块的关键设计在于内容自适应的频率权重计算。该模块首先对输入特征进行DCT变换，然后根据输入内容计算每个频率分量的权重。这些权重用于调整DCT系数，从而实现对频率分量的自适应调制。VONSS模块采用了一种全向扫描策略，通过水平、垂直和对角三个方向扫描特征，捕捉图像的全局结构信息。损失函数方面，采用了率失真优化目标，平衡压缩率和图像质量。

## 📊 实验亮点

实验结果表明，HCFSSNet在Kodak、Tecnick和CLIC Professional Validation数据集上取得了显著的性能提升。与VTM锚点相比，HCFSSNet分别降低了18.06%、24.56%和22.44%的BD率。此外，与最近基于SSM的编解码器（如MambaIC）相比，HCFSSNet实现了具有竞争力的率失真性能，同时使用的参数明显更少，表明该方法在效率和性能方面都具有优势。

## 🎯 应用场景

HCFSSNet在图像压缩领域具有广泛的应用前景，可应用于图像存储、图像传输、视频会议、流媒体服务等场景。该方法能够有效降低图像的存储空间和传输带宽，提高用户体验。未来，该研究可以扩展到视频压缩领域，为视频应用提供更高效的压缩方案。

## 📄 摘要（原文）

> Learned image compression (LIC) has recently benefited from Transformer based and state space model (SSM) based architectures. Convolutional neural networks (CNNs) effectively capture local high frequency details, whereas Transformers and SSMs provide strong long range modeling capabilities but may cause structural information loss or ignore frequency characteristics that are crucial for compression. In this work we propose HCFSSNet, a Hybrid Convolution and Frequency State Space Network for LIC. HCFSSNet uses CNNs to extract local high frequency structures and introduces a Vision Frequency State Space (VFSS) block that models long range low frequency information. The VFSS block combines an Omni directional Neighborhood State Space (VONSS) module, which scans features horizontally, vertically and diagonally, with an Adaptive Frequency Modulation Module (AFMM) that applies content adaptive weighting of discrete cosine transform frequency components for more efficient bit allocation. To further reduce redundancy in the entropy model, we integrate AFMM with a Swin Transformer to form a Frequency Swin Transformer Attention Module (FSTAM) for frequency aware side information modeling. Experiments on the Kodak, Tecnick and CLIC Professional Validation datasets show that HCFSSNet achieves competitive rate distortion performance compared with recent SSM based codecs such as MambaIC, while using significantly fewer parameters. On Kodak, Tecnick and CLIC, HCFSSNet reduces BD rate over the VTM anchor by 18.06, 24.56 and 22.44 percent, respectively, providing an efficient and interpretable hybrid architecture for future learned image compression systems.

