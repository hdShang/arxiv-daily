---
layout: default
title: "DEL: Dense Event Localization for Multi-modal Audio-Visual Understanding"
---

# DEL: Dense Event Localization for Multi-modal Audio-Visual Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23196" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23196v1</a>
  <a href="https://arxiv.org/pdf/2506.23196.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23196v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23196v1', 'DEL: Dense Event Localization for Multi-modal Audio-Visual Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mona Ahmadian, Amir Shirian, Frank Guerin, Andrew Gilbert

**分类**: cs.CV

**发布日期**: 2025-06-29

---

## 💡 一句话要点

**提出DEL框架以解决多模态视频中的密集事件定位问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `密集事件定位` `多模态融合` `自注意力机制` `动作识别`

## 📋 核心要点

1. 现有方法在处理长视频中的重叠事件和复杂时间依赖时存在显著不足，导致多模态交互建模困难。
2. DEL框架通过音频与视觉特征的对齐和多模态交互细化模块，增强了跨模态依赖建模能力，提升了动作定位精度。
3. 在UnAV-100、THUMOS14、ActivityNet 1.3和EPIC-Kitchens-100等数据集上，DEL框架的mAP平均提升显著，显示出其优越性。

## 📝 摘要（中文）

现实世界的视频通常包含重叠事件和复杂的时间依赖关系，使得多模态交互建模变得尤为困难。我们提出了DEL，一个用于密集语义动作定位的框架，旨在以细粒度的时间分辨率准确检测和分类长未修剪视频中的多个动作。DEL由两个关键模块组成：音频与视觉特征的对齐，利用掩蔽自注意力增强内部模式一致性，以及多模态交互细化模块，建模跨模态依赖关系，支持高层语义与细粒度细节。我们的方法在多个真实世界的时间动作定位数据集上取得了最先进的性能，显著超越了之前的方法，平均mAP提升分别为+3.3%、+2.6%、+1.2%、+1.7%（动词）和+1.4%（名词）。

## 🔬 方法详解

**问题定义**：本论文旨在解决长视频中重叠事件的密集语义动作定位问题。现有方法在处理复杂时间依赖和多模态交互时效果不佳，难以准确检测和分类多个动作。

**核心思路**：DEL框架的核心思路是通过音频与视觉特征的对齐，利用掩蔽自注意力机制增强内部模式的一致性，同时通过多模态交互细化模块建模跨模态依赖关系，以实现高层语义与细粒度细节的结合。

**技术框架**：DEL框架主要包括两个模块：1) 音频与视觉特征对齐模块，利用掩蔽自注意力增强特征一致性；2) 多模态交互细化模块，建模不同尺度的跨模态依赖关系，提升动作定位的准确性。

**关键创新**：DEL的主要创新在于引入了掩蔽自注意力机制来增强音频和视觉特征的对齐效果，并通过多模态交互细化模块有效建模跨模态依赖，这与传统方法的处理方式有本质区别。

**关键设计**：在DEL中，特征对齐模块的设计采用了多层自注意力结构，损失函数结合了分类损失与定位损失，以确保模型在多模态特征学习中的有效性。

## 📊 实验亮点

DEL框架在多个真实世界的时间动作定位数据集上表现出色，平均mAP提升分别为+3.3%、+2.6%、+1.2%、+1.7%（动词）和+1.4%（名词），显著超越了现有方法，展示了其在多模态理解中的有效性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在视频监控、智能家居、自动驾驶等领域，能够有效提升对复杂场景中多重事件的理解与分析能力。未来，DEL框架还可以扩展到其他多模态数据处理任务中，推动相关技术的发展。

## 📄 摘要（原文）

> Real-world videos often contain overlapping events and complex temporal dependencies, making multimodal interaction modeling particularly challenging. We introduce DEL, a framework for dense semantic action localization, aiming to accurately detect and classify multiple actions at fine-grained temporal resolutions in long untrimmed videos. DEL consists of two key modules: the alignment of audio and visual features that leverage masked self-attention to enhance intra-mode consistency and a multimodal interaction refinement module that models cross-modal dependencies across multiple scales, enabling high-level semantics and fine-grained details. Our method achieves state-of-the-art performance on multiple real-world Temporal Action Localization (TAL) datasets, UnAV-100, THUMOS14, ActivityNet 1.3, and EPIC-Kitchens-100, surpassing previous approaches with notable average mAP gains of +3.3%, +2.6%, +1.2%, +1.7% (verb), and +1.4% (noun), respectively.

