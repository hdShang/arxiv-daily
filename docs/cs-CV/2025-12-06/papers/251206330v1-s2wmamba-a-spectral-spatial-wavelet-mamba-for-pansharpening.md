---
layout: default
title: S2WMamba: A Spectral-Spatial Wavelet Mamba for Pansharpening
---

# S2WMamba: A Spectral-Spatial Wavelet Mamba for Pansharpening

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.06330" class="toolbar-btn" target="_blank">📄 arXiv: 2512.06330v1</a>
  <a href="https://arxiv.org/pdf/2512.06330.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.06330v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.06330v1', 'S2WMamba: A Spectral-Spatial Wavelet Mamba for Pansharpening')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoyu Zhang, Junhan Luo, Yugang Cao, Siran Peng, Jie Huang, Liangjian-Deng

**分类**: cs.CV

**发布日期**: 2025-12-06

**🔗 代码/项目**: [GITHUB](https://github.com/KagUYa66/S2WMamba)

---

## 💡 一句话要点

**提出S2WMamba，通过谱-空域小波变换和Mamba模块实现高效遥感图像融合**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `遥感图像融合` `Pansharpening` `小波变换` `Mamba` `谱空域处理`

## 📋 核心要点

1. 遥感图像融合的关键挑战在于如何有效分离和处理空间细节与光谱信息，现有方法常常难以避免二者之间的相互干扰。
2. S2WMamba的核心思想是利用小波变换在谱域和空域分别解耦信息，并通过Mamba模块进行跨模态特征交互，实现高效融合。
3. 实验结果表明，S2WMamba在多个遥感数据集上取得了优异的性能，相较于现有方法，在PSNR和HQNR等指标上均有提升。

## 📝 摘要（中文）

本文提出了一种名为S2WMamba的新型遥感图像融合（Pansharpening）方法，旨在将高分辨率全色（PAN）图像与低分辨率多光谱（LRMS）图像融合，生成高分辨率多光谱（HRMS）图像。该方法的核心在于解耦空间细节和光谱信息，并进行轻量级的跨模态交互。具体而言，对PAN图像应用2D Haar离散小波变换（DWT）以提取空间边缘和纹理，同时将每个像素的光谱视为1D信号，应用通道级的1D Haar DWT来分离低/高频分量，从而限制光谱失真。该方法包含谱分支和空域分支，通过基于Mamba的跨模态调制进行信息交换，并使用多尺度动态门控自适应地融合分支输出。在WV3、GF2和QB数据集上的实验结果表明，S2WMamba与最新的基线方法（FusionMamba、CANNet、U2Net、ARConv）相比，性能相当或更优，在全分辨率WV3数据集上PSNR提高了0.23 dB，HQNR达到了0.956。消融实验验证了2D/1D DWT放置、并行双分支以及融合门控选择的合理性。

## 🔬 方法详解

**问题定义**：遥感图像融合（Pansharpening）旨在将高分辨率的全色（PAN）图像和低分辨率的多光谱（LRMS）图像融合，生成高分辨率的多光谱（HRMS）图像。现有的方法通常难以有效地分离和处理空间细节和光谱信息，导致融合后的图像在空间细节增强的同时，光谱信息出现失真。

**核心思路**：S2WMamba的核心思路是利用小波变换在谱域和空域分别解耦空间细节和光谱信息。具体来说，对PAN图像进行2D Haar DWT提取空间细节，对LRMS图像的光谱进行1D Haar DWT提取光谱信息。然后，通过双分支结构分别处理空间和光谱信息，并使用Mamba模块进行跨模态交互。这种设计旨在减少空间细节和光谱信息之间的干扰，从而提高融合图像的质量。

**技术框架**：S2WMamba的整体架构包含以下几个主要模块：1) 2D Haar DWT模块，用于提取PAN图像的空间细节；2) 1D Haar DWT模块，用于提取LRMS图像的光谱信息；3) 谱分支，将小波提取的空间细节注入到MS特征中；4) 空域分支，使用来自1D金字塔的光谱信息细化PAN特征；5) 基于Mamba的跨模态调制模块，用于在谱分支和空域分支之间交换信息；6) 多尺度动态门控模块，用于自适应地融合两个分支的输出。

**关键创新**：S2WMamba最重要的技术创新点在于：1) 采用2D和1D Haar DWT分别处理空间和光谱信息，实现了空间细节和光谱信息的有效解耦；2) 使用Mamba模块进行跨模态交互，能够有效地建模长距离依赖关系，并具有线性复杂度；3) 采用多尺度动态门控机制，能够自适应地融合不同分支的输出。与现有方法相比，S2WMamba能够更好地平衡空间细节增强和光谱信息保持。

**关键设计**：在S2WMamba中，2D Haar DWT和1D Haar DWT的分解层数是一个关键参数，需要根据具体的数据集进行调整。Mamba模块的配置，如状态空间模型的维度，也会影响模型的性能。多尺度动态门控模块的权重初始化方式也会影响融合效果。损失函数通常采用L1损失或L2损失，也可以结合感知损失来进一步提高图像质量。

## 📊 实验亮点

S2WMamba在WV3、GF2和QB等多个遥感数据集上进行了实验验证。在WV3数据集上，S2WMamba的PSNR指标最高提升了0.23 dB，HQNR指标达到了0.956，超过了FusionMamba、CANNet、U2Net和ARConv等先进的基线方法。消融实验验证了2D/1D DWT放置、并行双分支以及融合门控选择的有效性。

## 🎯 应用场景

S2WMamba在遥感图像处理领域具有广泛的应用前景，例如城市规划、环境监测、灾害评估和农业资源调查等。通过提高遥感图像的空间分辨率和光谱保真度，可以为相关领域的决策提供更准确、更可靠的数据支持，具有重要的实际应用价值和未来发展潜力。

## 📄 摘要（原文）

> Pansharpening fuses a high-resolution PAN image with a low-resolution multispectral (LRMS) image to produce an HRMS image. A key difficulty is that jointly processing PAN and MS often entangles spatial detail with spectral fidelity. We propose S2WMamba, which explicitly disentangles frequency information and then performs lightweight cross-modal interaction. Concretely, a 2D Haar DWT is applied to PAN to localize spatial edges and textures, while a channel-wise 1D Haar DWT treats each pixel's spectrum as a 1D signal to separate low/high-frequency components and limit spectral distortion. The resulting Spectral branch injects wavelet-extracted spatial details into MS features, and the Spatial branch refines PAN features using spectra from the 1D pyramid; the two branches exchange information through Mamba-based cross-modulation that models long-range dependencies with linear complexity. A multi-scale dynamic gate (multiplicative + additive) then adaptively fuses branch outputs.On WV3, GF2, and QB, S2WMamba matches or surpasses recent strong baselines (FusionMamba, CANNet, U2Net, ARConv), improving PSNR by up to 0.23 dB and reaching HQNR 0.956 on full-resolution WV3. Ablations justify the choice of 2D/1D DWT placement, parallel dual branches, and the fusion gate. Our code is available at https://github.com/KagUYa66/S2WMamba.

