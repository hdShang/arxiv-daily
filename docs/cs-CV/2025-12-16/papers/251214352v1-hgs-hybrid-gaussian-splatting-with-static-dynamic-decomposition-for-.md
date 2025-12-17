---
layout: default
title: HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis
---

# HGS: Hybrid Gaussian Splatting with Static-Dynamic Decomposition for Compact Dynamic View Synthesis

**arXiv**: [2512.14352v1](https://arxiv.org/abs/2512.14352) | [PDF](https://arxiv.org/pdf/2512.14352.pdf)

**作者**: Kaizhe Zhang, Yijie Zhou, Weizhan Zhang, Caixia Yan, Haipeng Du, yugui xie, Yu-Hui Wen, Yong-Jin Liu

**分类**: cs.CV, cs.CG

**发布日期**: 2025-12-16

**备注**: 11 pages, 9 figures

---

## 💡 一句话要点

**提出混合高斯溅射框架，通过静态-动态分解策略解决动态新视角合成中模型冗余和效率低下的问题。**

**关键词**: `动态新视角合成` `3D高斯溅射` `静态-动态分解` `径向基函数` `实时渲染` `模型压缩` `虚拟现实` `高效计算`

## 📋 核心要点

1. 现有动态新视角合成方法因模型复杂和参数冗余，导致模型体积大、渲染慢，难以实时应用。
2. 提出混合高斯溅射框架，通过静态-动态分解策略，使用径向基函数分别建模动态和静态区域。
3. 实验显示模型大小减少高达98%，渲染速度达125 FPS，在VR系统中实现高效集成。

## 📝 摘要（中文）

动态新视角合成对于创造沉浸式体验至关重要。现有方法通过引入带有隐式变形场或非区分性时变参数的3D高斯溅射，超越了基于NeRF的方法。然而，由于模型复杂度过高和参数冗余，它们导致模型体积庞大、渲染速度缓慢，在资源受限设备上效率低下。为获得更高效、参数冗余更少的模型，本文提出混合高斯溅射，这是一个紧凑高效的框架，旨在在统一表示中显式解耦场景的静态和动态区域。HGS的核心创新在于静态-动态分解策略，该策略利用径向基函数对高斯基元进行建模。具体而言，对于动态区域，我们使用时变RBF有效捕捉时间变化并处理场景突变；对于静态区域，我们通过共享时间不变参数减少冗余。此外，我们引入针对显式模型的两阶段训练策略，以增强静态-动态边界的时间一致性。实验结果表明，我们的方法将模型大小减少了高达98%，在单个RTX 3090 GPU上以4K分辨率实现高达125 FPS的实时渲染。在RTX 3050上，它还能在1352*1014分辨率下维持160 FPS，并已集成到VR系统中。此外，HGS在渲染质量上与最先进方法相当，同时在高频细节和场景突变方面显著提高了视觉保真度。

## 🔬 方法详解

HGS的整体框架是一个基于3D高斯溅射的紧凑动态新视角合成系统。关键技术创新包括静态-动态分解策略，该策略利用径向基函数对高斯基元进行建模：动态区域使用时变RBF捕捉时间变化，静态区域共享时间不变参数以减少冗余。此外，引入两阶段训练策略以增强静态-动态边界的时间一致性。与现有方法的主要区别在于显式解耦静态和动态区域，避免了隐式变形场或非区分性时变参数带来的过度复杂性和参数冗余，从而实现了更高效的模型表示。

## 📊 实验亮点

模型大小减少高达98%，在RTX 3090上以4K分辨率实现125 FPS实时渲染，RTX 3050上维持160 FPS，已集成到VR系统，渲染质量与最先进方法相当。

## 🎯 应用场景

该研究在虚拟现实、增强现实和沉浸式媒体中具有广泛应用潜力，特别是在资源受限设备上实现实时动态场景渲染，提升用户体验和系统效率。

## 📄 摘要（原文）

> Dynamic novel view synthesis (NVS) is essential for creating immersive experiences. Existing approaches have advanced dynamic NVS by introducing 3D Gaussian Splatting (3DGS) with implicit deformation fields or indiscriminately assigned time-varying parameters, surpassing NeRF-based methods. However, due to excessive model complexity and parameter redundancy, they incur large model sizes and slow rendering speeds, making them inefficient for real-time applications, particularly on resource-constrained devices. To obtain a more efficient model with fewer redundant parameters, in this paper, we propose Hybrid Gaussian Splatting (HGS), a compact and efficient framework explicitly designed to disentangle static and dynamic regions of a scene within a unified representation. The core innovation of HGS lies in our Static-Dynamic Decomposition (SDD) strategy, which leverages Radial Basis Function (RBF) modeling for Gaussian primitives. Specifically, for dynamic regions, we employ time-dependent RBFs to effectively capture temporal variations and handle abrupt scene changes, while for static regions, we reduce redundancy by sharing temporally invariant parameters. Additionally, we introduce a two-stage training strategy tailored for explicit models to enhance temporal coherence at static-dynamic boundaries. Experimental results demonstrate that our method reduces model size by up to 98% and achieves real-time rendering at up to 125 FPS at 4K resolution on a single RTX 3090 GPU. It further sustains 160 FPS at 1352 * 1014 on an RTX 3050 and has been integrated into the VR system. Moreover, HGS achieves comparable rendering quality to state-of-the-art methods while providing significantly improved visual fidelity for high-frequency details and abrupt scene changes.

