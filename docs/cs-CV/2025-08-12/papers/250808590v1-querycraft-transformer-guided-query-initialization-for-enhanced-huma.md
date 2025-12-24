---
layout: default
title: "QueryCraft: Transformer-Guided Query Initialization for Enhanced Human-Object Interaction Detection"
---

# QueryCraft: Transformer-Guided Query Initialization for Enhanced Human-Object Interaction Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.08590" class="toolbar-btn" target="_blank">📄 arXiv: 2508.08590v1</a>
  <a href="https://arxiv.org/pdf/2508.08590.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.08590v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.08590v1', 'QueryCraft: Transformer-Guided Query Initialization for Enhanced Human-Object Interaction Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxiao Wang, Wolin Liang, Yu Lei, Weiying Xue, Nan Zhuang, Qi Liu

**分类**: cs.CV, cs.HC

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出QueryCraft以解决HOI检测中查询初始化不足问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人-物体交互` `变换器` `查询初始化` `跨模态学习` `深度学习` `特征蒸馏` `智能监控`

## 📋 核心要点

1. 现有DETR基础的HOI检测方法在查询初始化上存在不足，随机初始化的查询缺乏语义信息，导致检测效果不佳。
2. QueryCraft通过引入ACTOR和PDQD模块，利用语义引导的特征学习来优化查询初始化，从而提升HOI检测的准确性。
3. 在HICO-Det和V-COCO数据集上进行的实验表明，QueryCraft在性能上超越了现有的主流方法，展现出良好的泛化能力。

## 📝 摘要（中文）

人-物体交互（HOI）检测旨在定位图像中的人-物体对并识别其交互。尽管基于DETR的方法已成为HOI检测的主流框架，但随机初始化的查询缺乏明确的语义，导致检测性能不佳。为了解决这一挑战，我们提出了QueryCraft，这是一种新颖的可插拔HOI检测框架，通过基于变换器的查询初始化结合语义先验和引导特征学习。我们的方法核心是ACTOR（动作感知跨模态变换器），它共同关注视觉区域和文本提示，以提取与动作相关的特征。为了进一步增强对象级查询质量，我们引入了感知蒸馏查询解码器（PDQD），从预训练检测器中提取对象类别意识，以作为对象查询的初始化。大量实验表明，我们的方法在HICO-Det和V-COCO基准上实现了最先进的性能和强大的泛化能力。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是人-物体交互检测中的查询初始化不足，现有方法随机初始化的查询缺乏明确的语义信息，导致检测性能不理想。

**核心思路**：论文的核心解决思路是通过引入语义先验和引导特征学习，利用变换器进行查询初始化，从而生成更具语义意义的查询表示。

**技术框架**：整体架构包括两个主要模块：ACTOR和PDQD。ACTOR是一个跨模态变换器，负责提取与动作相关的特征；PDQD则从预训练检测器中蒸馏对象类别意识，作为对象查询的初始化。

**关键创新**：最重要的技术创新点在于ACTOR模块的设计，它不仅对视觉区域和文本提示进行对齐，还利用语言引导的注意力推断交互语义，生成更具解释性的查询。

**关键设计**：在设计中，采用了特定的损失函数来优化查询的生成过程，并通过双分支查询初始化策略提升了模型的可解释性和有效性。

## 📊 实验亮点

在HICO-Det和V-COCO基准上，QueryCraft实现了最先进的性能，相较于现有方法，检测精度提升了X%（具体数值待补充），展现出强大的泛化能力和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括智能监控、机器人交互和人机协作等场景。通过提高人-物体交互检测的准确性，QueryCraft能够在实际应用中提升系统的智能化水平，促进更自然的人机交互体验。

## 📄 摘要（原文）

> Human-Object Interaction (HOI) detection aims to localize human-object pairs and recognize their interactions in images. Although DETR-based methods have recently emerged as the mainstream framework for HOI detection, they still suffer from a key limitation: Randomly initialized queries lack explicit semantics, leading to suboptimal detection performance. To address this challenge, we propose QueryCraft, a novel plug-and-play HOI detection framework that incorporates semantic priors and guided feature learning through transformer-based query initialization. Central to our approach is \textbf{ACTOR} (\textbf{A}ction-aware \textbf{C}ross-modal \textbf{T}ransf\textbf{OR}mer), a cross-modal Transformer encoder that jointly attends to visual regions and textual prompts to extract action-relevant features. Rather than merely aligning modalities, ACTOR leverages language-guided attention to infer interaction semantics and produce semantically meaningful query representations. To further enhance object-level query quality, we introduce a \textbf{P}erceptual \textbf{D}istilled \textbf{Q}uery \textbf{D}ecoder (\textbf{PDQD}), which distills object category awareness from a pre-trained detector to serve as object query initiation. This dual-branch query initialization enables the model to generate more interpretable and effective queries for HOI detection. Extensive experiments on HICO-Det and V-COCO benchmarks demonstrate that our method achieves state-of-the-art performance and strong generalization. Code will be released upon publication.

