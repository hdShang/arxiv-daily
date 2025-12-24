---
layout: default
title: "No More Sibling Rivalry: Debiasing Human-Object Interaction Detection"
---

# No More Sibling Rivalry: Debiasing Human-Object Interaction Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00760" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00760v1</a>
  <a href="https://arxiv.org/pdf/2509.00760.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00760v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00760v1', 'No More Sibling Rivalry: Debiasing Human-Object Interaction Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bin Yang, Yulin Zhang, Hong-Yu Zhou, Sibei Yang

**分类**: cs.CV

**发布日期**: 2025-08-31

**备注**: Accept to ICCV2025

---

## 💡 一句话要点

**提出新方法以解决人机交互检测中的偏见问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人机交互` `去偏见` `检测变换器` `深度学习` `计算机视觉` `特征学习` `模型优化`

## 📋 核心要点

1. 现有的HOI检测方法在处理相似的HOI三元组时存在“有毒兄弟”偏见，导致模型学习效果受损。
2. 论文提出的“对比后校准”和“合并后拆分”方法，分别从输入和输出角度去除偏见，提高模型的区分能力。
3. 实验结果表明，所提方法在HICO-Det数据集上较基线提升了9.18%的mAP，相较于最先进方法提升了3.59%。

## 📝 摘要（中文）

本研究针对人机交互（HOI）检测中的“有毒兄弟”偏见问题，提出了两种新的去偏见学习目标——“对比后校准”和“合并后拆分”。该偏见源于相似但不同的HOI三元组之间的干扰，导致模型学习效果下降。通过对输入和输出的不同处理，显著提升了检测精度，实验结果显示在HICO-Det数据集上，mAP提升了9.18%。

## 🔬 方法详解

**问题定义**：本研究旨在解决人机交互检测中的“有毒兄弟”偏见问题。现有方法在处理相似的HOI三元组时，因相互干扰导致模型学习效果下降，影响检测精度。

**核心思路**：论文提出了两种新的去偏见学习目标，分别针对输入和输出进行优化。通过对相似三元组的处理，增强模型的区分能力，从而提高检测精度。

**技术框架**：整体方法包括两个主要模块：对比后校准模块和合并后拆分模块。前者通过样本重构来纠正错误的HOI三元组，后者则通过学习共享特征来增强类别间的区分。

**关键创新**：最重要的技术创新在于提出了“对比后校准”和“合并后拆分”两种去偏见策略，显著改善了模型在相似HOI三元组上的学习效果，与现有方法相比，提供了更有效的解决方案。

**关键设计**：在对比后校准中，利用强位置先验对相似三元组进行重构；在合并后拆分中，首先学习兄弟类别的共享特征，然后细化组内差异以保持独特性。

## 📊 实验亮点

实验结果显示，所提方法在HICO-Det数据集上实现了9.18%的mAP提升，相较于最先进的技术提升了3.59%。这些结果表明，新的去偏见策略显著增强了模型的性能，具有重要的实际应用价值。

## 🎯 应用场景

该研究的成果可广泛应用于智能监控、机器人交互和人机协作等领域，提升机器对人类行为的理解能力，进而改善人机交互的自然性和准确性。未来，随着技术的进一步发展，可能会推动更复杂场景下的HOI检测应用。

## 📄 摘要（原文）

> Detection transformers have been applied to human-object interaction (HOI) detection, enhancing the localization and recognition of human-action-object triplets in images. Despite remarkable progress, this study identifies a critical issue-"Toxic Siblings" bias-which hinders the interaction decoder's learning, as numerous similar yet distinct HOI triplets interfere with and even compete against each other both input side and output side to the interaction decoder. This bias arises from high confusion among sibling triplets/categories, where increased similarity paradoxically reduces precision, as one's gain comes at the expense of its toxic sibling's decline. To address this, we propose two novel debiasing learning objectives-"contrastive-then-calibration" and "merge-then-split"-targeting the input and output perspectives, respectively. The former samples sibling-like incorrect HOI triplets and reconstructs them into correct ones, guided by strong positional priors. The latter first learns shared features among sibling categories to distinguish them from other groups, then explicitly refines intra-group differentiation to preserve uniqueness. Experiments show that we significantly outperform both the baseline (+9.18% mAP on HICO-Det) and the state-of-the-art (+3.59% mAP) across various settings.

