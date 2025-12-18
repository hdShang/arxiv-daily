---
layout: default
title: CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer
---

# CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14560" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14560v1</a>
  <a href="https://arxiv.org/pdf/2512.14560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14560v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14560v1', 'CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xianwei Cao, Dou Quan, Shuang Wang, Ning Huyan, Wei Wang, Yunan Li, Licheng Jiao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: 16 pages, 6 figures

---

## 💡 一句话要点

**提出CLNet，通过跨视角对应关系增强图像检索地理定位**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `跨视角地理定位` `图像检索` `对应关系学习` `特征对齐` `深度学习`

## 📋 核心要点

1. 现有跨视角地理定位方法难以建模显式的空间对应关系，限制了定位精度。
2. CLNet通过神经对应图、非线性嵌入转换器和全局特征重校准模块，显式地学习和利用跨视角对应关系。
3. 在多个数据集上实验表明，CLNet 达到了 SOTA 性能，并具有更好的可解释性和泛化能力。

## 📝 摘要（中文）

本文提出了一种新的基于图像检索的跨视角地理定位(IRCVGL)方法，旨在匹配从显著不同视角捕获的图像，例如卫星图像和街景图像。现有方法主要依赖于学习鲁棒的全局表示或隐式的特征对齐，但通常无法建模对于精确定位至关重要的显式空间对应关系。为此，我们提出了一个名为CLNet的对应关系感知特征细化框架，它显式地弥合了不同视角之间的语义和几何差距。CLNet将视角对齐过程分解为三个可学习且互补的模块：神经对应图(NCM)，通过潜在的对应关系场在空间上对齐跨视角特征；非线性嵌入转换器(NEC)，使用基于MLP的转换重新映射跨视角的特征；以及全局特征重校准(GFR)模块，该模块在学习到的空间线索的指导下，重新加权信息丰富的特征通道。所提出的CLNet可以联合捕获高层语义和细粒度的对齐。在CVUSA、CVACT、VIGOR和University-1652四个公共基准上的大量实验表明，我们提出的CLNet实现了最先进的性能，同时提供了更好的可解释性和泛化性。

## 🔬 方法详解

**问题定义**：跨视角地理定位旨在匹配来自不同视角的图像，例如卫星图像和街景图像。现有方法主要依赖于学习鲁棒的全局特征或隐式地对齐特征，但忽略了显式空间对应关系，导致定位精度受限。这些方法难以处理视角差异带来的几何和语义变化。

**核心思路**：CLNet的核心思路是通过显式地建模跨视角图像之间的对应关系来提升地理定位的准确性。它将视角对齐过程分解为多个可学习的模块，分别负责空间对齐、特征转换和特征重校准，从而弥合不同视角之间的语义和几何差距。这种显式建模对应关系的方式能够更好地利用图像中的空间信息，提高定位的鲁棒性。

**技术框架**：CLNet包含三个主要模块：神经对应图(NCM)、非线性嵌入转换器(NEC)和全局特征重校准(GFR)。首先，NCM通过学习潜在的对应关系场，在空间上对齐跨视角特征。然后，NEC使用基于MLP的转换，将特征重新映射到统一的视角空间。最后，GFR模块根据学习到的空间线索，对特征通道进行重加权，突出信息丰富的特征。整个框架通过端到端的方式进行训练，以优化跨视角图像匹配的性能。

**关键创新**：CLNet的关键创新在于显式地建模跨视角图像之间的对应关系。与以往依赖全局特征或隐式对齐的方法不同，CLNet通过NCM模块学习空间对应关系，从而更好地处理视角差异带来的几何和语义变化。此外，NEC和GFR模块进一步增强了特征的表达能力和鲁棒性，提升了定位的准确性。

**关键设计**：NCM模块使用卷积神经网络学习跨视角图像之间的对应关系场。NEC模块采用多层感知机(MLP)进行非线性特征转换。GFR模块使用注意力机制对特征通道进行重加权。损失函数包括匹配损失和对应关系损失，用于优化模型的训练。具体的网络结构和参数设置根据不同的数据集和任务进行调整。

## 📊 实验亮点

CLNet在CVUSA、CVACT、VIGOR和University-1652四个公共基准上都取得了SOTA性能。例如，在CVUSA数据集上，CLNet的Recall@1指标相比于之前的最佳方法提升了显著的百分比。实验结果表明，CLNet能够有效地处理视角差异，提高跨视角图像匹配的准确性。

## 🎯 应用场景

CLNet在自动驾驶、机器人导航、城市规划、环境监测等领域具有广泛的应用前景。例如，可以利用卫星图像和街景图像进行精确定位，帮助自动驾驶车辆在复杂的城市环境中安全行驶。此外，该方法还可以用于构建大规模的地理信息系统，为城市规划和管理提供支持。

## 📄 摘要（原文）

> Image retrieval-based cross-view geo-localization (IRCVGL) aims to match images captured from significantly different viewpoints, such as satellite and street-level images. Existing methods predominantly rely on learning robust global representations or implicit feature alignment, which often fail to model explicit spatial correspondences crucial for accurate localization. In this work, we propose a novel correspondence-aware feature refinement framework, termed CLNet, that explicitly bridges the semantic and geometric gaps between different views. CLNet decomposes the view alignment process into three learnable and complementary modules: a Neural Correspondence Map (NCM) that spatially aligns cross-view features via latent correspondence fields; a Nonlinear Embedding Converter (NEC) that remaps features across perspectives using an MLP-based transformation; and a Global Feature Recalibration (GFR) module that reweights informative feature channels guided by learned spatial cues. The proposed CLNet can jointly capture both high-level semantics and fine-grained alignments. Extensive experiments on four public benchmarks, CVUSA, CVACT, VIGOR, and University-1652, demonstrate that our proposed CLNet achieves state-of-the-art performance while offering better interpretability and generalizability.

