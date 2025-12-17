---
layout: default
title: CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer
---

# CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer

**arXiv**: [2512.14560v1](https://arxiv.org/abs/2512.14560) | [PDF](https://arxiv.org/pdf/2512.14560.pdf)

**作者**: Xianwei Cao, Dou Quan, Shuang Wang, Ning Huyan, Wei Wang, Yunan Li, Licheng Jiao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: 16 pages, 6 figures

---

## 💡 一句话要点

**提出CLNet框架，通过显式跨视图对应关系解决图像检索式跨视角地理定位问题。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `跨视角地理定位` `图像检索` `特征对齐` `神经对应图` `非线性嵌入转换` `全局特征重校准` `语义几何对应` `多视图匹配`

## 📋 核心要点

1. 现有方法依赖全局表示或隐式对齐，难以建模跨视图的显式空间对应关系，导致地理定位精度受限。
2. CLNet通过神经对应图、非线性嵌入转换器和全局特征重校准模块，显式学习语义和几何对应，提升特征对齐能力。
3. 在多个基准数据集上，CLNet达到最先进性能，并展现出更好的可解释性和泛化性，验证了其有效性。

## 📝 摘要（中文）

基于图像检索的跨视角地理定位（IRCVGL）旨在匹配从显著不同视角（如卫星和街景图像）捕获的图像。现有方法主要依赖学习鲁棒的全局表示或隐式特征对齐，往往无法建模对精确定位至关重要的显式空间对应关系。本文提出一种新颖的对应感知特征细化框架，称为CLNet，它显式地桥接不同视图之间的语义和几何差距。CLNet将视图对齐过程分解为三个可学习且互补的模块：神经对应图（NCM），通过潜在对应场在空间上对齐跨视图特征；非线性嵌入转换器（NEC），使用基于MLP的变换跨视角重新映射特征；以及全局特征重校准（GFR）模块，通过学习到的空间线索引导重新加权信息丰富的特征通道。所提出的CLNet能够联合捕获高级语义和细粒度对齐。在四个公共基准数据集（CVUSA、CVACT、VIGOR和University-1652）上的广泛实验表明，CLNet实现了最先进的性能，同时提供了更好的可解释性和泛化性。

## 🔬 方法详解

CLNet是一个对应感知特征细化框架，整体架构包括三个核心模块：神经对应图（NCM）通过潜在对应场实现跨视图特征的空间对齐；非线性嵌入转换器（NEC）使用MLP变换跨视角重新映射特征；全局特征重校准（GFR）基于学习到的空间线索重新加权特征通道。关键创新在于显式建模跨视图对应关系，而非依赖隐式对齐。与现有方法的主要区别在于将视图对齐分解为可学习的互补模块，联合捕获高级语义和细粒度几何信息，从而更有效地桥接语义和几何差距。

## 📊 实验亮点

在CVUSA、CVACT、VIGOR和University-1652四个基准数据集上，CLNet均达到最先进性能，显著提升了跨视角地理定位的准确率，同时实验验证了其更好的可解释性和泛化能力。

## 🎯 应用场景

该研究可应用于自动驾驶、无人机导航和增强现实等领域，通过跨视角图像匹配实现精确的地理定位，提升位置感知系统的鲁棒性和准确性。

## 📄 摘要（原文）

> Image retrieval-based cross-view geo-localization (IRCVGL) aims to match images captured from significantly different viewpoints, such as satellite and street-level images. Existing methods predominantly rely on learning robust global representations or implicit feature alignment, which often fail to model explicit spatial correspondences crucial for accurate localization. In this work, we propose a novel correspondence-aware feature refinement framework, termed CLNet, that explicitly bridges the semantic and geometric gaps between different views. CLNet decomposes the view alignment process into three learnable and complementary modules: a Neural Correspondence Map (NCM) that spatially aligns cross-view features via latent correspondence fields; a Nonlinear Embedding Converter (NEC) that remaps features across perspectives using an MLP-based transformation; and a Global Feature Recalibration (GFR) module that reweights informative feature channels guided by learned spatial cues. The proposed CLNet can jointly capture both high-level semantics and fine-grained alignments. Extensive experiments on four public benchmarks, CVUSA, CVACT, VIGOR, and University-1652, demonstrate that our proposed CLNet achieves state-of-the-art performance while offering better interpretability and generalizability.

