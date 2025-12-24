---
layout: default
title: "GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM Reconstruction"
---

# GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25075" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25075v2</a>
  <a href="https://arxiv.org/pdf/2509.25075.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25075v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25075v2', 'GEM: 3D Gaussian Splatting for Efficient and Accurate Cryo-EM Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Huaizhi Qu, Xiao Wang, Gengwei Zhang, Jie Peng, Tianlong Chen

**分类**: cs.CV, cs.CE

**发布日期**: 2025-09-29 (更新: 2025-10-02)

**🔗 代码/项目**: [GITHUB](https://github.com/UNITES-Lab/GEM)

---

## 💡 一句话要点

**GEM：基于3D高斯溅射的冷冻电镜高效精确重建框架**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `冷冻电镜` `三维重建` `3D高斯溅射` `结构生物学` `计算效率` `内存优化`

## 📋 核心要点

1. 冷冻电镜3D重建面临大数据集带来的计算和内存瓶颈，传统方法精度不足，NeRF方法开销过大。
2. GEM利用3D高斯溅射直接在实空间表示蛋白质结构，仅用少量参数即可实现高效重建。
3. GEM在标准数据集上实现了更快的训练速度、更低的内存占用和更高的局部重建分辨率。

## 📝 摘要（中文）

冷冻电镜(cryo-EM)已成为高分辨率结构生物学的核心工具，但大规模数据集（通常超过10万张粒子图像）使得3D重建在计算和内存上都非常昂贵。传统的傅里叶空间方法效率高，但由于重复变换而损失了保真度；而最近基于神经辐射场(NeRFs)的实空间方法提高了精度，但导致立方级的内存和计算开销。因此，我们引入了GEM，这是一种基于3D高斯溅射(3DGS)的新型cryo-EM重建框架，它直接在实空间中运行，同时保持了高效率。GEM没有对整个密度体积进行建模，而是用紧凑的3D高斯函数来表示蛋白质，每个高斯函数仅由11个值参数化。为了进一步提高训练效率，我们设计了一种新的梯度计算方法，用于计算对每个体素有贡献的3D高斯函数。这种设计大大减少了内存占用和训练成本。在标准的cryo-EM基准测试中，GEM的训练速度比最先进的方法快48%，内存使用量降低12%，同时局部分辨率提高了38.8%。这些结果表明，GEM是cryo-EM重建的一种实用且可扩展的范例，统一了速度、效率和高分辨率精度。

## 🔬 方法详解

**问题定义**：冷冻电镜三维重建旨在从大量二维投影图像中恢复蛋白质的三维结构。现有方法，如基于傅里叶变换的方法，虽然计算效率高，但在处理复杂结构时精度受限。基于NeRF的方法虽然精度有所提升，但计算和内存开销呈立方级增长，难以处理大规模数据集。

**核心思路**：GEM的核心思路是利用3D高斯溅射（3DGS）来表示蛋白质的三维结构。与体素或NeRF不同，3DGS使用一组参数化的3D高斯函数来近似蛋白质密度，每个高斯函数仅需少量参数即可表示，从而大大降低了内存占用和计算复杂度。

**技术框架**：GEM框架主要包含以下几个阶段：1) 初始化：使用一组随机初始化的3D高斯函数来表示蛋白质结构。2) 投影：将3D高斯函数投影到2D图像平面，模拟冷冻电镜的成像过程。3) 损失计算：计算投影图像与真实图像之间的差异，作为损失函数。4) 优化：使用梯度下降法优化3D高斯函数的参数，使其更好地拟合真实数据。GEM的关键在于高效的梯度计算方法，能够快速计算每个高斯函数对体素的贡献。

**关键创新**：GEM的关键创新在于使用3D高斯溅射来表示蛋白质结构，并设计了高效的梯度计算方法。与传统的体素表示相比，3DGS更加紧凑，能够显著降低内存占用。与NeRF相比，3DGS的渲染过程更加高效，能够实现更快的训练速度。

**关键设计**：每个3D高斯函数由11个参数表示，包括位置、协方差矩阵（表示形状和方向）和颜色。损失函数采用L1损失和SSIM损失的加权组合，以提高重建质量。梯度计算方法利用了3DGS的可微性，能够高效地计算每个高斯函数对体素的贡献，从而加速训练过程。

## 📊 实验亮点

GEM在标准冷冻电镜基准数据集上取得了显著的性能提升。与最先进的方法相比，GEM的训练速度提高了高达48%，内存使用量降低了12%，同时局部分辨率提高了38.8%。这些结果表明，GEM在效率、内存占用和重建精度方面都具有显著优势。

## 🎯 应用场景

GEM为冷冻电镜三维重建提供了一种高效且精确的解决方案，可广泛应用于结构生物学领域，加速蛋白质结构解析，促进药物发现和疾病研究。该方法有望应用于更大规模、更高分辨率的冷冻电镜数据处理，为理解生命过程提供更深入的见解，并推动相关技术在其他三维重建领域的应用。

## 📄 摘要（原文）

> Cryo-electron microscopy (cryo-EM) has become a central tool for high-resolution structural biology, yet the massive scale of datasets (often exceeding 100k particle images) renders 3D reconstruction both computationally expensive and memory intensive. Traditional Fourier-space methods are efficient but lose fidelity due to repeated transforms, while recent real-space approaches based on neural radiance fields (NeRFs) improve accuracy but incur cubic memory and computation overhead. Therefore, we introduce GEM, a novel cryo-EM reconstruction framework built on 3D Gaussian Splatting (3DGS) that operates directly in real-space while maintaining high efficiency. Instead of modeling the entire density volume, GEM represents proteins with compact 3D Gaussians, each parameterized by only 11 values. To further improve the training efficiency, we designed a novel gradient computation to 3D Gaussians that contribute to each voxel. This design substantially reduced both memory footprint and training cost. On standard cryo-EM benchmarks, GEM achieves up to 48% faster training and 12% lower memory usage compared to state-of-the-art methods, while improving local resolution by as much as 38.8%. These results establish GEM as a practical and scalable paradigm for cryo-EM reconstruction, unifying speed, efficiency, and high-resolution accuracy. Our code is available at https://github.com/UNITES-Lab/GEM.

