---
layout: default
title: Lightweight 3D Gaussian Splatting Compression via Video Codec
---

# Lightweight 3D Gaussian Splatting Compression via Video Codec

**arXiv**: [2512.11186v1](https://arxiv.org/abs/2512.11186) | [PDF](https://arxiv.org/pdf/2512.11186.pdf)

**作者**: Qi Yang, Geert Van Der Auwera, Zhu Li

**分类**: cs.CV

**发布日期**: 2025-12-12

**备注**: Accepted by DCC2026 Oral

**🔗 代码/项目**: [GITHUB](https://github.com/Qi-Yangsjtu/LGSCV)

---

## 💡 一句话要点

**提出基于视频编解码器的轻量级3D高斯溅射压缩方法，适用于轻量级设备。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D高斯溅射` `视频压缩` `Morton扫描` `主成分分析` `率失真优化` `轻量级设备` `视频编码`

## 📋 核心要点

1. 现有基于视频的GS压缩方法依赖于并行线性分配排序（PLAS），计算量大且耗时，限制了GS在轻量级设备上的应用。
2. 提出一种轻量级3D高斯溅射压缩方法，通过两阶段Morton扫描生成块状2D图，并结合PCA降维和MiniPLAS优化中低码率性能。
3. 实验结果表明，该方法在率失真性能上优于现有技术20%以上，同时显著降低了2D图生成和编码时间。

## 📝 摘要（中文）

本文提出了一种基于视频编解码器的轻量级3D高斯溅射（GS）压缩方法（LGSCV）。该方法首先提出了一种两阶段Morton扫描，以生成适用于标准视频编解码器的块状2D图，其中编码单元（CU）是方形块。使用3D Morton扫描来置换GS图元，然后使用2D Morton扫描以块状方式将排序后的GS图元映射到2D图。针对中低码率下质量下降的问题，采用主成分分析（PCA）来降低球谐函数（SH）的维度，并设计了一种灵活快速的MiniPLAS来置换特定块大小内的图元。SH PCA和MiniPLAS的结合显著提高了率失真（RD）性能，尤其是在中低码率下。MiniPLAS还可以指导编解码器CU大小配置，并显著减少编码时间。在MPEG数据集上的实验结果表明，所提出的LGSCV与最先进的方法相比，实现了超过20%的RD增益，同时将2D图生成时间减少到大约1秒，并将编码时间减少了50%。

## 🔬 方法详解

**问题定义**：现有基于视频的3D高斯溅射（GS）压缩方法，如基于并行线性分配排序（PLAS）的方法，计算复杂度高，耗时较长，难以在轻量级设备上部署。因此，需要一种计算效率更高、更轻量级的GS压缩方法。

**核心思路**：论文的核心思路是利用标准视频编解码器对3D GS数据进行压缩。为了更好地适应视频编解码器的块状编码结构，论文设计了一种两阶段Morton扫描方法，将3D GS图元映射到块状2D图。同时，为了解决中低码率下的性能下降问题，引入了PCA降维和MiniPLAS优化。

**技术框架**：该方法主要包含以下几个阶段：1) 3D Morton扫描：对GS图元进行排序。2) 2D Morton扫描：将排序后的GS图元映射到块状2D图。3) SH PCA：对球谐函数进行主成分分析，降低维度。4) MiniPLAS：在块内进行图元置换优化。5) 视频编码：使用标准视频编解码器对2D图进行编码。

**关键创新**：该方法的主要创新点在于：1) 提出了两阶段Morton扫描方法，生成适用于视频编解码器的块状2D图。2) 结合PCA降维和MiniPLAS优化，显著提高了中低码率下的率失真性能。3) MiniPLAS可以指导编解码器CU大小配置，从而减少编码时间。与现有方法相比，该方法计算复杂度更低，更适合在轻量级设备上部署。

**关键设计**：两阶段Morton扫描的具体实现细节，包括3D和2D Morton码的生成方式。PCA降维中保留的主成分数量。MiniPLAS的块大小设置和置换策略。编解码器CU大小的配置策略，以及如何利用MiniPLAS指导CU大小的设置。

## 📊 实验亮点

实验结果表明，所提出的LGSCV方法与最先进的方法相比，实现了超过20%的率失真（RD）增益。同时，该方法将2D图生成时间减少到大约1秒，并将编码时间减少了50%。这些结果表明，该方法在性能和效率方面都具有显著优势。

## 🎯 应用场景

该研究成果可应用于各种需要高效3D高斯溅射压缩的场景，例如移动端的3D场景渲染、VR/AR应用、以及低带宽网络环境下的3D内容传输。通过降低计算复杂度和提高压缩效率，该方法有望推动3D高斯溅射技术在轻量级设备和资源受限环境中的普及。

## 📄 摘要（原文）

> Current video-based GS compression methods rely on using Parallel Linear Assignment Sorting (PLAS) to convert 3D GS into smooth 2D maps, which are computationally expensive and time-consuming, limiting the application of GS on lightweight devices. In this paper, we propose a Lightweight 3D Gaussian Splatting (GS) Compression method based on Video codec (LGSCV). First, a two-stage Morton scan is proposed to generate blockwise 2D maps that are friendly for canonical video codecs in which the coding units (CU) are square blocks. A 3D Morton scan is used to permute GS primitives, followed by a 2D Morton scan to map the ordered GS primitives to 2D maps in a blockwise style. However, although the blockwise 2D maps report close performance to the PLAS map in high-bitrate regions, they show a quality collapse at medium-to-low bitrates. Therefore, a principal component analysis (PCA) is used to reduce the dimensionality of spherical harmonics (SH), and a MiniPLAS, which is flexible and fast, is designed to permute the primitives within certain block sizes. Incorporating SH PCA and MiniPLAS leads to a significant gain in rate-distortion (RD) performance, especially at medium and low bitrates. MiniPLAS can also guide the setting of the codec CU size configuration and significantly reduce encoding time. Experimental results on the MPEG dataset demonstrate that the proposed LGSCV achieves over 20% RD gain compared with state-of-the-art methods, while reducing 2D map generation time to approximately 1 second and cutting encoding time by 50%. The code is available at https://github.com/Qi-Yangsjtu/LGSCV .

