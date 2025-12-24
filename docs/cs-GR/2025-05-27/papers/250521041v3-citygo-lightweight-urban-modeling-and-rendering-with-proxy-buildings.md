---
layout: default
title: CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians
---

# CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21041" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21041v3</a>
  <a href="https://arxiv.org/pdf/2505.21041.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21041v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21041v3', 'CityGo: Lightweight Urban Modeling and Rendering with Proxy Buildings and Residual Gaussians')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weihang Liu, Yuhui Zhong, Yuke Li, Xi Chen, Jiadi Cui, Honglong Zhang, Lan Xu, Xin Lou, Yujiao Shi, Jingyi Yu, Yingliang Zhang

**分类**: cs.GR, cs.CV

**发布日期**: 2025-05-27 (更新: 2025-06-09)

---

## 💡 一句话要点

**提出CityGo以解决大规模城市场景建模与渲染问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `城市建模` `渲染技术` `高斯体` `增强现实` `无人机检查` `智能城市` `实时渲染`

## 📋 核心要点

1. 现有方法在城市场景建模中面临遮挡、不完整几何和高内存需求等挑战，限制了其在移动设备上的应用。
2. 论文提出的CityGo框架结合了纹理代理几何体与残差高斯体，通过优化策略实现轻量级的城市场景渲染。
3. 实验结果显示，CityGo在真实世界的航空数据集上实现了1.4倍的训练时间加速，并在视觉保真度上与3D高斯散射方法相当。

## 📝 摘要（中文）

大规模城市场景的准确高效建模对增强现实导航、无人机检查和智能城市数字双胞胎等应用至关重要。尽管航空影像提供了广泛的覆盖，但从这些视角重建城市环境仍面临遮挡、不完整几何和高内存需求等挑战。CityGo是一个混合框架，结合了纹理代理几何体与残差高斯体，旨在实现轻量级、真实感的城市场景渲染。该方法提取紧凑的建筑代理网格，并利用零阶SH高斯生成无遮挡纹理，进一步通过残差高斯捕捉高频细节。实验表明，CityGo显著减少了训练时间，平均加速1.4倍，同时在移动GPU上实现了实时渲染。

## 🔬 方法详解

**问题定义**：本论文旨在解决大规模城市场景的建模与渲染问题，现有方法在处理遮挡和高内存需求时表现不佳，尤其在移动设备上难以实现实时渲染。

**核心思路**：CityGo框架通过结合纹理代理几何体与残差高斯体，利用图像渲染和反投影技术生成无遮挡纹理，从而实现轻量级的真实感渲染。

**技术框架**：该方法首先从多视角立体（MVS）点云中提取建筑代理网格，然后使用零阶SH高斯生成纹理，接着引入残差高斯以捕捉高频细节，最后通过重要性感知下采样减少冗余。

**关键创新**：最重要的创新在于引入了残差高斯体和周围高斯体的结合，显著提高了渲染效率和视觉质量，同时减少了对密集原始体的依赖。

**关键设计**：在参数设置上，采用了优化策略共同调整代理纹理和高斯参数，确保在移动GPU上实现实时渲染，且显著降低了训练和内存需求。

## 📊 实验亮点

实验结果表明，CityGo在真实世界的航空数据集上实现了1.4倍的训练时间加速，同时在视觉保真度上与传统的3D高斯散射方法相当。此外，该方法在移动消费级GPU上实现了实时渲染，显著降低了内存使用和能耗。

## 🎯 应用场景

CityGo的研究成果在增强现实导航、无人机检查和智能城市数字双胞胎等领域具有广泛的应用潜力。通过实现轻量级的城市场景渲染，该方法能够在资源受限的设备上提供高质量的视觉体验，推动相关技术的普及与发展。

## 📄 摘要（原文）

> Accurate and efficient modeling of large-scale urban scenes is critical for applications such as AR navigation, UAV based inspection, and smart city digital twins. While aerial imagery offers broad coverage and complements limitations of ground-based data, reconstructing city-scale environments from such views remains challenging due to occlusions, incomplete geometry, and high memory demands. Recent advances like 3D Gaussian Splatting (3DGS) improve scalability and visual quality but remain limited by dense primitive usage, long training times, and poor suit ability for edge devices. We propose CityGo, a hybrid framework that combines textured proxy geometry with residual and surrounding 3D Gaussians for lightweight, photorealistic rendering of urban scenes from aerial perspectives. Our approach first extracts compact building proxy meshes from MVS point clouds, then uses zero order SH Gaussians to generate occlusion-free textures via image-based rendering and back-projection. To capture high-frequency details, we introduce residual Gaussians placed based on proxy-photo discrepancies and guided by depth priors. Broader urban context is represented by surrounding Gaussians, with importance-aware downsampling applied to non-critical regions to reduce redundancy. A tailored optimization strategy jointly refines proxy textures and Gaussian parameters, enabling real-time rendering of complex urban scenes on mobile GPUs with significantly reduced training and memory requirements. Extensive experiments on real-world aerial datasets demonstrate that our hybrid representation significantly reduces training time, achieving on average 1.4x speedup, while delivering comparable visual fidelity to pure 3D Gaussian Splatting approaches. Furthermore, CityGo enables real-time rendering of large-scale urban scenes on mobile consumer GPUs, with substantially reduced memory usage and energy consumption.

