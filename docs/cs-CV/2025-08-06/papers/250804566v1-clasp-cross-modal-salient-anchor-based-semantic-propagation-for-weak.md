---
layout: default
title: "CLASP: Cross-modal Salient Anchor-based Semantic Propagation for Weakly-supervised Dense Audio-Visual Event Localization"
---

# CLASP: Cross-modal Salient Anchor-based Semantic Propagation for Weakly-supervised Dense Audio-Visual Event Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04566" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04566v1</a>
  <a href="https://arxiv.org/pdf/2508.04566.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04566v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04566v1', 'CLASP: Cross-modal Salient Anchor-based Semantic Propagation for Weakly-supervised Dense Audio-Visual Event Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jinxing Zhou, Ziheng Zhou, Yanghao Zhou, Yuxin Mao, Zhangling Duan, Dan Guo

**分类**: cs.CV, cs.AI, cs.MM

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出基于跨模态显著锚点的语义传播方法以解决弱监督密集音视频事件定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `弱监督学习` `音视频事件定位` `跨模态学习` `显著锚点` `语义传播` `多模态融合` `时间定位` `深度学习`

## 📋 核心要点

1. 现有方法在弱监督条件下难以准确定位音视频事件的时间边界，导致性能受限。
2. 提出利用跨模态显著锚点，通过互事件一致性评估和锚点识别模块来增强事件语义编码。
3. 在UnAV-100和ActivityNet1.3数据集上进行的实验显示，方法实现了最先进的性能，显著提升了定位准确性。

## 📝 摘要（中文）

密集音视频事件定位（DAVEL）任务旨在对未剪辑视频中同时发生的音频和视觉事件进行时间定位。本文在新的弱监督设置（W-DAVEL任务）下探讨DAVEL，其中仅提供视频级事件标签，且每个事件的时间边界未知。我们通过利用跨模态显著锚点来解决W-DAVEL问题，这些锚点是指在弱监督下可靠预测的时间戳，并在音频和视觉模态中展现出高度一致的事件语义。具体而言，我们提出了一种互事件一致性评估模块，通过测量预测的音频和视觉事件类别之间的差异生成一致性评分。然后，该评分用于跨模态显著锚点识别模块，通过全局视频和局部时间窗口识别机制识别音频和视觉锚点特征。经过多模态集成后的锚点特征被输入到基于锚点的时间传播模块，以增强原始时间音频和视觉特征中的事件语义编码，从而在弱监督下促进更好的时间定位。我们在UnAV-100和ActivityNet1.3数据集上建立了W-DAVEL的基准。大量实验表明，我们的方法达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决在弱监督条件下进行密集音视频事件定位的问题。现有方法在仅提供视频级标签的情况下，难以准确识别事件的时间边界，导致定位效果不佳。

**核心思路**：我们提出了一种基于跨模态显著锚点的语义传播方法，通过识别在音频和视觉模态中一致的时间戳来增强事件的语义表示，从而改善定位性能。

**技术框架**：整体架构包括三个主要模块：互事件一致性评估模块、跨模态显著锚点识别模块和基于锚点的时间传播模块。首先，通过一致性评估生成评分，然后识别显著锚点，最后进行时间传播以增强语义编码。

**关键创新**：最重要的创新在于引入了跨模态显著锚点的概念，并通过互事件一致性评估来提高音频和视觉模态之间的语义一致性，这与现有方法的单一模态处理形成了鲜明对比。

**关键设计**：在设计中，我们使用了全局视频和局部时间窗口识别机制来提取锚点特征，并通过特定的损失函数来优化一致性评分，确保模型在弱监督条件下的鲁棒性。

## 📊 实验亮点

实验结果表明，所提方法在UnAV-100和ActivityNet1.3数据集上均达到了最先进的性能，具体提升幅度超过了现有基线，尤其在事件定位准确性上有显著改善，验证了方法的有效性和优越性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在视频监控、自动视频摘要和多媒体检索等领域。通过提高音视频事件的定位精度，可以显著提升这些应用的智能化水平，推动相关技术的发展与应用。未来，该方法也可能扩展到其他模态融合任务中，进一步提升多模态学习的效果。

## 📄 摘要（原文）

> The Dense Audio-Visual Event Localization (DAVEL) task aims to temporally localize events in untrimmed videos that occur simultaneously in both the audio and visual modalities. This paper explores DAVEL under a new and more challenging weakly-supervised setting (W-DAVEL task), where only video-level event labels are provided and the temporal boundaries of each event are unknown. We address W-DAVEL by exploiting \textit{cross-modal salient anchors}, which are defined as reliable timestamps that are well predicted under weak supervision and exhibit highly consistent event semantics across audio and visual modalities. Specifically, we propose a \textit{Mutual Event Agreement Evaluation} module, which generates an agreement score by measuring the discrepancy between the predicted audio and visual event classes. Then, the agreement score is utilized in a \textit{Cross-modal Salient Anchor Identification} module, which identifies the audio and visual anchor features through global-video and local temporal window identification mechanisms. The anchor features after multimodal integration are fed into an \textit{Anchor-based Temporal Propagation} module to enhance event semantic encoding in the original temporal audio and visual features, facilitating better temporal localization under weak supervision. We establish benchmarks for W-DAVEL on both the UnAV-100 and ActivityNet1.3 datasets. Extensive experiments demonstrate that our method achieves state-of-the-art performance.

