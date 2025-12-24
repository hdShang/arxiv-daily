---
layout: default
title: AgriFM: A Multi-source Temporal Remote Sensing Foundation Model for Crop Mapping
---

# AgriFM: A Multi-source Temporal Remote Sensing Foundation Model for Crop Mapping

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21357" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21357v2</a>
  <a href="https://arxiv.org/pdf/2505.21357.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21357v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21357v2', 'AgriFM: A Multi-source Temporal Remote Sensing Foundation Model for Crop Mapping')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenyuan Li, Shunlin Liang, Keyan Chen, Yongzhe Chen, Han Ma, Jianglei Xu, Yichuan Ma, Shikang Guan, Husheng Fang, Zhenwei Shi

**分类**: cs.CV, cs.LG

**发布日期**: 2025-05-27 (更新: 2025-05-28)

**🔗 代码/项目**: [GITHUB](https://github.com/flyakon/AgriFM)

---

## 💡 一句话要点

**提出AgriFM以解决农业作物映射中的时空特征提取问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `遥感技术` `作物映射` `时空特征提取` `Transformer模型` `深度学习` `农业应用` `多源数据`

## 📋 核心要点

1. 现有的遥感基础模型在作物映射中未能有效处理多尺度时空特征，导致性能不足。
2. AgriFM通过同步时空特征提取，采用修改后的Video Swin Transformer架构，提升了作物映射的准确性。
3. 实验结果表明，AgriFM在所有下游任务中均优于传统深度学习方法和现有的通用遥感基础模型。

## 📝 摘要（中文）

准确的作物映射依赖于对多尺度时空模式的建模，现有的基于Transformer的遥感基础模型在作物映射中表现不佳，主要是因为它们要么使用固定的时空窗口，忽视了作物系统的多尺度特性，要么完全忽略时间信息。为了解决这些问题，本文提出了AgriFM，一个专门为农业作物映射设计的多源遥感基础模型。AgriFM通过修改Video Swin Transformer架构，实现了时空特征的层次提取，并利用来自MODIS、Landsat-8/9和Sentinel-2的丰富时序数据进行预训练，最终在各项下游任务中表现优越。

## 🔬 方法详解

**问题定义**：本文旨在解决现有遥感基础模型在作物映射中对多尺度时空特征提取不足的问题。现有方法往往使用固定的时空窗口，无法适应作物系统的复杂性，或仅关注空间模式，忽略了时间信息的重要性。

**核心思路**：AgriFM的核心思路是实现层次化的时空特征提取，采用修改后的Video Swin Transformer架构，使得时空下采样与空间缩放操作同步进行，从而有效处理长时间序列的卫星输入。

**技术框架**：AgriFM的整体架构包括多个模块：首先是数据输入模块，接收来自不同卫星源的时序数据；接着是特征提取模块，利用修改后的Transformer架构提取时空特征；最后是解码器模块，动态融合这些特征以支持多种下游任务。

**关键创新**：AgriFM的主要创新在于其同步的时空特征提取机制，解决了传统模型在处理多尺度时空数据时的局限性。与现有方法相比，AgriFM能够更全面地捕捉作物生长的动态变化。

**关键设计**：在设计上，AgriFM采用了多源数据输入，结合了MODIS、Landsat-8/9和Sentinel-2的丰富信息，并在全球代表性数据集上进行预训练，确保模型的泛化能力。

## 📊 实验亮点

在综合评估中，AgriFM在所有下游任务上均表现出色，相较于传统深度学习方法和现有的通用遥感基础模型，性能提升显著，具体提升幅度未知，显示了其在作物映射中的优越性。

## 🎯 应用场景

AgriFM在农业作物映射中的应用潜力巨大，可以用于精准农业、土地利用监测和环境变化分析等领域。通过提高作物映射的准确性，AgriFM能够为农业管理决策提供更可靠的数据支持，促进可持续发展。

## 📄 摘要（原文）

> Accurate crop mapping fundamentally relies on modeling multi-scale spatiotemporal patterns, where spatial scales range from individual field textures to landscape-level context, and temporal scales capture both short-term phenological transitions and full growing-season dynamics. Transformer-based remote sensing foundation models (RSFMs) offer promising potential for crop mapping due to their innate ability for unified spatiotemporal processing. However, current RSFMs remain suboptimal for crop mapping: they either employ fixed spatiotemporal windows that ignore the multi-scale nature of crop systems or completely disregard temporal information by focusing solely on spatial patterns. To bridge these gaps, we present AgriFM, a multi-source remote sensing foundation model specifically designed for agricultural crop mapping. Our approach begins by establishing the necessity of simultaneous hierarchical spatiotemporal feature extraction, leading to the development of a modified Video Swin Transformer architecture where temporal down-sampling is synchronized with spatial scaling operations. This modified backbone enables efficient unified processing of long time-series satellite inputs. AgriFM leverages temporally rich data streams from three satellite sources including MODIS, Landsat-8/9 and Sentinel-2, and is pre-trained on a global representative dataset comprising over 25 million image samples supervised by land cover products. The resulting framework incorporates a versatile decoder architecture that dynamically fuses these learned spatiotemporal representations, supporting diverse downstream tasks. Comprehensive evaluations demonstrate AgriFM's superior performance over conventional deep learning approaches and state-of-the-art general-purpose RSFMs across all downstream tasks. Codes will be available at https://github.com/flyakon/AgriFM.

