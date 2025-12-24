---
layout: default
title: "WeatherPrompt: Multi-modality Representation Learning for All-Weather Drone Visual Geo-Localization"
---

# WeatherPrompt: Multi-modality Representation Learning for All-Weather Drone Visual Geo-Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.09560" class="toolbar-btn" target="_blank">📄 arXiv: 2508.09560v3</a>
  <a href="https://arxiv.org/pdf/2508.09560.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.09560v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.09560v3', 'WeatherPrompt: Multi-modality Representation Learning for All-Weather Drone Visual Geo-Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Wen, Hang Yu, Zhedong Zheng

**分类**: cs.CV, cs.RO

**发布日期**: 2025-08-13 (更新: 2025-12-04)

---

## 💡 一句话要点

**提出WeatherPrompt以解决无人机视觉地理定位中的天气干扰问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态学习` `视觉地理定位` `天气推理` `动态门控机制` `无人机技术`

## 📋 核心要点

1. 现有无人机视觉地理定位方法在复杂天气条件下表现不佳，主要受限于天气类别的局限性和特征解耦的不足。
2. 提出WeatherPrompt，通过多模态学习融合图像和文本信息，建立天气不变的表示，提升模型的泛化能力。
3. 实验结果显示，WeatherPrompt在不同天气条件下的召回率显著提升，尤其在夜间和恶劣天气下表现优异。

## 📝 摘要（中文）

无人机的视觉地理定位在天气扰动（如雨和雾）下面临严重退化，现有方法存在两个固有的局限性：一是过度依赖有限的天气类别，限制了模型的泛化能力；二是通过伪天气类别对纠缠的场景-天气特征的解耦效果不佳。为此，本文提出WeatherPrompt，一个多模态学习范式，通过将图像嵌入与文本上下文融合，建立天气不变的表示。该框架的两个关键贡献是：首先，提出了一种无训练的天气推理机制，利用现成的大型多模态模型合成多天气文本描述，提升了对未见或复杂天气的可扩展性；其次，提出了一个动态门控机制的多模态框架，通过文本嵌入自适应地重新加权和融合视觉特征。大量实验验证了该方法在多种天气条件下的竞争性召回率，尤其在夜间、雾和雪条件下分别提高了13.37%和18.69%。

## 🔬 方法详解

**问题定义**：本文旨在解决无人机视觉地理定位在复杂天气条件下的性能退化问题。现有方法过于依赖有限的天气类别，导致泛化能力不足，同时对场景与天气特征的解耦效果不佳。

**核心思路**：WeatherPrompt通过多模态学习，结合图像嵌入与文本上下文，建立天气不变的特征表示。采用无训练的天气推理机制，利用大型多模态模型生成多种天气描述，增强模型对复杂天气的适应能力。

**技术框架**：该框架包括两个主要模块：天气推理模块和动态门控融合模块。天气推理模块负责生成多天气文本描述，而动态门控模块则根据文本嵌入自适应调整视觉特征的权重，确保场景与天气特征的有效解耦。

**关键创新**：提出的无训练天气推理机制和动态门控融合方法是本研究的核心创新，与现有方法相比，显著提升了对复杂天气的适应能力和特征解耦效果。

**关键设计**：在模型设计中，采用了图像-文本对比学习和图像-文本匹配的交叉模态目标，确保在表示空间中将同一场景在不同天气条件下的特征尽可能靠近。

## 📊 实验亮点

在多种天气条件下，WeatherPrompt的实验结果显示出显著的性能提升，特别是在夜间条件下召回率提高了13.37%，在雾和雪条件下提高了18.69%。这些结果表明，该方法在无人机视觉地理定位领域的有效性和优越性，超越了现有的最先进技术。

## 🎯 应用场景

WeatherPrompt的研究成果在无人机导航、环境监测和灾害响应等领域具有广泛的应用潜力。通过提升无人机在各种天气条件下的定位精度，该技术可以增强无人机在复杂环境中的自主决策能力，推动智能交通和无人机配送等行业的发展。

## 📄 摘要（原文）

> Visual geo-localization for drones faces critical degradation under weather perturbations, \eg, rain and fog, where existing methods struggle with two inherent limitations: 1) Heavy reliance on limited weather categories that constrain generalization, and 2) Suboptimal disentanglement of entangled scene-weather features through pseudo weather categories. We present WeatherPrompt, a multi-modality learning paradigm that establishes weather-invariant representations through fusing the image embedding with the text context. Our framework introduces two key contributions: First, a Training-free Weather Reasoning mechanism that employs off-the-shelf large multi-modality models to synthesize multi-weather textual descriptions through human-like reasoning. It improves the scalability to unseen or complex weather, and could reflect different weather strength. Second, to better disentangle the scene and weather feature, we propose a multi-modality framework with the dynamic gating mechanism driven by the text embedding to adaptively reweight and fuse visual features across modalities. The framework is further optimized by the cross-modal objectives, including image-text contrastive learning and image-text matching, which maps the same scene with different weather conditions closer in the respresentation space. Extensive experiments validate that, under diverse weather conditions, our method achieves competitive recall rates compared to state-of-the-art drone geo-localization methods. Notably, it improves Recall@1 by +13.37\% under night conditions and by 18.69\% under fog and snow conditions.

