---
layout: default
title: "SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction"
---

# SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14633" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14633v1</a>
  <a href="https://arxiv.org/pdf/2511.14633.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14633v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14633v1', 'SparseSurf: Sparse-View 3D Gaussian Splatting for Surface Reconstruction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Meiying Gu, Jiawei Zhang, Jiahe Li, Xiaohan Yu, Haonan Luo, Jin Zheng, Xiao Bai

**分类**: cs.CV

**发布日期**: 2025-11-18

**备注**: Accepted at AAAI 2026. Project page: https://miya-oi.github.io/SparseSurf-project

---

## 💡 一句话要点

**SparseSurf：稀疏视图下基于3D高斯溅射的表面重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `三维重建` `高斯溅射` `稀疏视图` `表面重建` `几何一致性` `立体视觉` `新视角合成`

## 📋 核心要点

1. 现有方法在稀疏视图下进行3D高斯溅射表面重建时，容易发生过拟合，导致重建质量不佳，这是核心挑战。
2. SparseSurf的核心思想是引入立体几何-纹理对齐，将渲染质量与几何估计联系起来，从而共同优化表面重建和视角合成。
3. 实验结果表明，SparseSurf在DTU、BlendedMVS和Mip-NeRF360数据集上均取得了state-of-the-art的性能。

## 📝 摘要（中文）

本文提出了一种名为SparseSurf的方法，旨在解决从稀疏视图图像中重建高质量、细节丰富的表面几何结构的问题。现有方法在稀疏视图下容易过拟合，导致重建质量下降。虽然使用扁平高斯基元和深度正则化可以缓解几何歧义，但扁平高斯带来的各向异性会加剧过拟合，影响表面拟合和新视角合成。SparseSurf通过引入立体几何-纹理对齐，将渲染质量与几何估计联系起来，从而共同提升表面重建和视角合成质量。此外，提出了伪特征增强几何一致性，通过结合训练视图和未见视图来增强多视图几何一致性，有效缓解稀疏监督导致的过拟合。在DTU、BlendedMVS和Mip-NeRF360数据集上的实验表明，该方法达到了最先进的性能。

## 🔬 方法详解

**问题定义**：论文旨在解决在稀疏视图条件下，利用3D高斯溅射进行精确表面重建的问题。现有方法，如直接优化高斯参数或使用扁平高斯，在稀疏视图下容易过拟合，导致几何形状不准确，新视角渲染质量下降。现有方法在稀疏视图下几何信息不足，易受噪声干扰，难以保证重建的几何一致性。

**核心思路**：SparseSurf的核心思路是建立渲染质量和几何估计之间的桥梁，通过立体几何-纹理对齐，将渲染损失反向传播到几何优化中，从而提高重建精度。同时，利用伪特征增强几何一致性，引入未见视图的信息，增强多视图几何一致性，缓解过拟合。

**技术框架**：SparseSurf包含两个主要模块：立体几何-纹理对齐和伪特征增强几何一致性。首先，通过立体几何-纹理对齐模块，利用渲染损失优化高斯参数，实现几何和纹理的协同优化。然后，通过伪特征增强几何一致性模块，利用训练视图和未见视图的伪特征，约束高斯参数，增强多视图几何一致性。整体流程是迭代优化高斯参数，直至收敛。

**关键创新**：SparseSurf的关键创新在于立体几何-纹理对齐和伪特征增强几何一致性。立体几何-纹理对齐将渲染质量直接反馈到几何优化中，避免了单独优化几何形状导致的偏差。伪特征增强几何一致性利用未见视图的信息，有效缓解了稀疏视图下的过拟合问题。与现有方法相比，SparseSurf更有效地利用了稀疏视图的信息，实现了更精确的表面重建。

**关键设计**：立体几何-纹理对齐模块使用渲染损失（如L1损失、SSIM损失）作为优化目标，指导高斯参数的更新。伪特征增强几何一致性模块首先提取训练视图和未见视图的伪特征，然后利用这些伪特征计算几何一致性损失，约束高斯参数。具体实现中，可以使用预训练的深度估计网络提取伪特征，并使用Huber损失等鲁棒损失函数计算几何一致性损失。

## 📊 实验亮点

SparseSurf在DTU、BlendedMVS和Mip-NeRF360数据集上进行了广泛的实验，结果表明该方法在表面重建质量和新视角渲染质量方面均优于现有方法。例如，在DTU数据集上，SparseSurf在L1误差和PSNR指标上均取得了显著提升，证明了其在稀疏视图下的优越性能。

## 🎯 应用场景

SparseSurf在三维重建领域具有广泛的应用前景，例如：逆向工程、文物数字化、虚拟现实、增强现实、机器人导航等。该方法能够从有限的图像中重建出高质量的三维模型，降低了数据采集的成本和难度，为相关应用提供了更便捷的解决方案。未来，该技术有望应用于自动驾驶、城市建模等领域。

## 📄 摘要（原文）

> Recent advances in optimizing Gaussian Splatting for scene geometry have enabled efficient reconstruction of detailed surfaces from images. However, when input views are sparse, such optimization is prone to overfitting, leading to suboptimal reconstruction quality. Existing approaches address this challenge by employing flattened Gaussian primitives to better fit surface geometry, combined with depth regularization to alleviate geometric ambiguities under limited viewpoints. Nevertheless, the increased anisotropy inherent in flattened Gaussians exacerbates overfitting in sparse-view scenarios, hindering accurate surface fitting and degrading novel view synthesis performance. In this paper, we propose \net{}, a method that reconstructs more accurate and detailed surfaces while preserving high-quality novel view rendering. Our key insight is to introduce Stereo Geometry-Texture Alignment, which bridges rendering quality and geometry estimation, thereby jointly enhancing both surface reconstruction and view synthesis. In addition, we present a Pseudo-Feature Enhanced Geometry Consistency that enforces multi-view geometric consistency by incorporating both training and unseen views, effectively mitigating overfitting caused by sparse supervision. Extensive experiments on the DTU, BlendedMVS, and Mip-NeRF360 datasets demonstrate that our method achieves the state-of-the-art performance.

