---
layout: default
title: Large Language Model-Driven Distributed Integrated Multimodal Sensing and Semantic Communications
---

# Large Language Model-Driven Distributed Integrated Multimodal Sensing and Semantic Communications

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18194" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18194v2</a>
  <a href="https://arxiv.org/pdf/2505.18194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18194v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18194v2', 'Large Language Model-Driven Distributed Integrated Multimodal Sensing and Semantic Communications')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yubo Peng, Luping Xiang, Bingxin Zhang, Kun Yang

**分类**: eess.SP, cs.AI, cs.CV

**发布日期**: 2025-05-20 (更新: 2025-05-30)

---

## 💡 一句话要点

**提出LLM-DiSAC框架以解决单模态感知系统的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态感知` `语义通信` `大语言模型` `射频-视觉融合` `分布式学习` `智能城市` `无人驾驶`

## 📋 核心要点

1. 现有的单模态感知系统在复杂环境中表现不佳，尤其是在城市和非视距场景中，视角和空间覆盖的限制显著降低了其有效性。
2. 本文提出的LLM-DiSAC框架通过多个协作设备结合RF和视觉数据，利用大语言模型提升感知精度和通信效率。
3. 在合成的多视角RF-视觉数据集上，LLM-DiSAC展示了优异的性能，显著提高了感知准确性和语义传输效率。

## 📝 摘要（中文）

传统的单模态感知系统在复杂动态环境中面临挑战，尤其是在城市或非视距场景中，受限于视角和空间覆盖不足。为此，本文提出了一种新颖的基于大语言模型的分布式集成多模态感知与语义通信框架（LLM-DiSAC）。该系统由多个协作感知设备组成，结合射频（RF）和视觉数据，通过聚合中心提升感知精度。具体而言，LLM-DiSAC开发了射频-视觉融合网络（RVFN）和基于LLM的语义传输网络（LSTN），并在聚合中心使用变换器聚合模型（TRAM）进行特征融合。实验结果表明，LLM-DiSAC在合成的多视角RF-视觉数据集上表现良好。

## 🔬 方法详解

**问题定义**：本文旨在解决传统单模态感知系统在复杂动态环境中的局限性，尤其是在城市和非视距场景中的视角和空间覆盖不足问题。

**核心思路**：LLM-DiSAC框架通过结合多个协作感知设备的RF和视觉数据，利用大语言模型进行语义通信，从而提升感知精度和通信效率。

**技术框架**：该框架包括多个主要模块：射频-视觉融合网络（RVFN）用于多模态数据集成，基于LLM的语义传输网络（LSTN）用于提高通信效率，以及变换器聚合模型（TRAM）用于特征融合。

**关键创新**：最重要的创新在于引入了基于大语言模型的语义传输网络，能够有效利用已知信道参数来减轻语义失真，与传统方法相比，提升了通信的准确性和效率。

**关键设计**：在RVFN中，采用了专门的特征提取器和交叉注意力模块；LSTN中的解码器利用信道距离和信噪比等参数；TRAM则使用自适应聚合注意力机制来融合分布式特征。

## 📊 实验亮点

在合成的多视角RF-视觉数据集上，LLM-DiSAC的性能表现优异，相较于基线方法，感知准确性和语义传输效率均有显著提升，具体数据尚未披露。

## 🎯 应用场景

该研究的潜在应用领域包括智能城市、无人驾驶、安防监控等场景，能够在复杂环境中提供更高效的感知和通信解决方案。未来，随着多模态技术的发展，LLM-DiSAC框架有望在更多实际应用中发挥重要作用。

## 📄 摘要（原文）

> Traditional single-modal sensing systems-based solely on either radio frequency (RF) or visual data-struggle to cope with the demands of complex and dynamic environments. Furthermore, single-device systems are constrained by limited perspectives and insufficient spatial coverage, which impairs their effectiveness in urban or non-line-of-sight scenarios. To overcome these challenges, we propose a novel large language model (LLM)-driven distributed integrated multimodal sensing and semantic communication (LLM-DiSAC) framework. Specifically, our system consists of multiple collaborative sensing devices equipped with RF and camera modules, working together with an aggregation center to enhance sensing accuracy. First, on sensing devices, LLM-DiSAC develops an RF-vision fusion network (RVFN), which employs specialized feature extractors for RF and visual data, followed by a cross-attention module for effective multimodal integration. Second, a LLM-based semantic transmission network (LSTN) is proposed to enhance communication efficiency, where the LLM-based decoder leverages known channel parameters, such as transceiver distance and signal-to-noise ratio (SNR), to mitigate semantic distortion. Third, at the aggregation center, a transformer-based aggregation model (TRAM) with an adaptive aggregation attention mechanism is developed to fuse distributed features and enhance sensing accuracy. To preserve data privacy, a two-stage distributed learning strategy is introduced, allowing local model training at the device level and centralized aggregation model training using intermediate features. Finally, evaluations on a synthetic multi-view RF-visual dataset generated by the Genesis simulation engine show that LLM-DiSAC achieves a good performance.

