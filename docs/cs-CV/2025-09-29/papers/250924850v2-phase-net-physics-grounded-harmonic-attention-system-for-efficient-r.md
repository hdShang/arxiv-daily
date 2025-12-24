---
layout: default
title: "PHASE-Net: Physics-Grounded Harmonic Attention System for Efficient Remote Photoplethysmography Measurement"
---

# PHASE-Net: Physics-Grounded Harmonic Attention System for Efficient Remote Photoplethysmography Measurement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.24850" class="toolbar-btn" target="_blank">📄 arXiv: 2509.24850v2</a>
  <a href="https://arxiv.org/pdf/2509.24850.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.24850v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.24850v2', 'PHASE-Net: Physics-Grounded Harmonic Attention System for Efficient Remote Photoplethysmography Measurement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Zhao, Dan Guo, Junzhe Cao, Yong Xu, Tao Tan, Yue Sun, Bochao Zou, Jie Zhang, Zitong Yu

**分类**: cs.CV

**发布日期**: 2025-09-29 (更新: 2025-09-30)

---

## 💡 一句话要点

**提出PHASE-Net，通过物理驱动的谐波注意力机制实现高效的远程光电容积脉搏波测量。**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `远程光电容积脉搏波` `rPPG` `生理信号监测` `时间卷积网络` `物理信息建模`

## 📋 核心要点

1. 现有rPPG深度学习方法缺乏理论基础，导致在头部运动和光照变化下鲁棒性和可解释性不足。
2. 论文提出基于血液动力学方程的物理信息rPPG范式，并以此为基础设计轻量级PHASE-Net模型。
3. 实验结果表明，PHASE-Net在rPPG测量中实现了最先进的性能，并具有很高的效率。

## 📝 摘要（中文）

远程光电容积脉搏波(rPPG)测量能够实现非接触式生理监测，但易受头部运动和光照变化的影响，导致精度下降。现有的深度学习方法大多是启发式的，缺乏理论基础，限制了鲁棒性和可解释性。本文提出了一种基于血液动力学Navier-Stokes方程的物理信息rPPG范式，表明脉搏信号遵循二阶动力系统，其离散解自然地导出了因果卷积。这为使用时间卷积网络(TCN)提供了理论依据。基于此，我们设计了PHASE-Net，一个轻量级模型，包含三个关键组件：(1)零FLOPs轴向交换模块，它交换或转置几个空间通道，以混合远距离面部区域，并在不破坏时间顺序的情况下增强跨区域特征交互；(2)自适应空间滤波器，它学习每个帧的软空间掩码，以突出显示信号丰富的区域并抑制噪声；(3)门控TCN，一种带有门控的因果扩张TCN，用于建模长程时间动态以实现精确的脉搏恢复。大量实验表明，PHASE-Net以强大的效率实现了最先进的性能，提供了一种理论上可靠且可部署的rPPG解决方案。

## 🔬 方法详解

**问题定义**：论文旨在解决远程光电容积脉搏波(rPPG)测量中，由于头部运动和光照变化导致的精度下降问题。现有深度学习方法通常是启发式的，缺乏理论基础，导致模型鲁棒性和可解释性较差，难以应对复杂场景。

**核心思路**：论文的核心思路是将rPPG信号的产生过程与血液动力学的Navier-Stokes方程联系起来，推导出脉搏信号遵循二阶动力系统，其离散解与因果卷积相对应。因此，可以使用时间卷积网络(TCN)来建模脉搏信号的时序动态，并从理论上解释了TCN在rPPG信号处理中的有效性。

**技术框架**：PHASE-Net的整体架构包含三个主要模块：(1)零FLOPs轴向交换模块，用于增强跨区域特征交互；(2)自适应空间滤波器，用于突出信号丰富的区域并抑制噪声；(3)门控TCN，用于建模长程时间动态以实现精确的脉搏恢复。整个流程是：首先，通过轴向交换模块混合空间信息，然后使用自适应空间滤波器提取关键区域，最后通过门控TCN进行时序建模，得到最终的脉搏信号。

**关键创新**：论文最重要的技术创新点在于将物理模型引入到rPPG信号处理中，通过Navier-Stokes方程推导出脉搏信号的动力学特性，为TCN的使用提供了理论依据。此外，零FLOPs轴向交换模块和自适应空间滤波器也有效地提升了模型的性能和效率。

**关键设计**：零FLOPs轴向交换模块通过交换或转置少量空间通道来实现跨区域特征混合，避免了额外的计算开销。自适应空间滤波器通过学习每个帧的软空间掩码来动态地调整不同区域的权重。门控TCN使用因果扩张卷积来建模长程时间依赖关系，并使用门控机制来控制信息的流动。

## 📊 实验亮点

实验结果表明，PHASE-Net在多个公开rPPG数据集上取得了state-of-the-art的性能，并且具有很高的计算效率。例如，在XXX数据集上，PHASE-Net的性能超过了现有最佳方法X%，同时模型参数量和计算量也显著降低，使其更易于部署。

## 🎯 应用场景

该研究成果可应用于非接触式生理监测领域，例如远程医疗、智能家居健康监测、驾驶员疲劳检测等。通过摄像头即可实现对人体心率等生理指标的监测，具有重要的实际应用价值和广阔的市场前景。未来，该技术有望进一步扩展到其他生理信号的监测，实现更全面的健康管理。

## 📄 摘要（原文）

> Remote photoplethysmography (rPPG) measurement enables non-contact physiological monitoring but suffers from accuracy degradation under head motion and illumination changes. Existing deep learning methods are mostly heuristic and lack theoretical grounding, which limits robustness and interpretability. In this work, we propose a physics-informed rPPG paradigm derived from the Navier-Stokes equations of hemodynamics, showing that the pulse signal follows a second-order dynamical system whose discrete solution naturally leads to a causal convolution. This provides a theoretical justification for using a Temporal Convolutional Network (TCN). Based on this principle, we design PHASE-Net, a lightweight model with three key components: (1) Zero-FLOPs Axial Swapper module, which swaps or transposes a few spatial channels to mix distant facial regions and enhance cross-region feature interaction without breaking temporal order; (2) Adaptive Spatial Filter, which learns a soft spatial mask per frame to highlight signal-rich areas and suppress noise; and (3) Gated TCN, a causal dilated TCN with gating that models long-range temporal dynamics for accurate pulse recovery. Extensive experiments demonstrate that PHASE-Net achieves state-of-the-art performance with strong efficiency, offering a theoretically grounded and deployment-ready rPPG solution.

