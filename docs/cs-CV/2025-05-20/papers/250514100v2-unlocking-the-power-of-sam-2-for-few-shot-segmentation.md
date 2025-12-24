---
layout: default
title: Unlocking the Power of SAM 2 for Few-Shot Segmentation
---

# Unlocking the Power of SAM 2 for Few-Shot Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14100" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14100v2</a>
  <a href="https://arxiv.org/pdf/2505.14100.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14100v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14100v2', 'Unlocking the Power of SAM 2 for Few-Shot Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianxiong Xu, Lanyun Zhu, Xuanyi Liu, Guosheng Lin, Cheng Long, Ziyue Li, Rui Zhao

**分类**: cs.CV

**发布日期**: 2025-05-20 (更新: 2025-05-21)

**备注**: This paper is accepted by ICML'25

---

## 💡 一句话要点

**提出伪提示生成器与迭代记忆精炼以解决少样本分割问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本分割` `伪提示生成器` `迭代记忆精炼` `视频分割` `计算机视觉`

## 📋 核心要点

1. 现有方法在少样本分割中容易出现过拟合，且在视频数据中，前景对象的身份一致性导致匹配步骤不兼容。
2. 本文提出伪提示生成器以编码伪查询记忆，并设计迭代记忆精炼来增强记忆的准确性，抑制意外的背景特征。
3. 在PASCAL-5$^i$和COCO-20$^i$上进行的实验显示，1-shot mIoU比最佳基线提升了4.2%，验证了方法的有效性。

## 📝 摘要（中文）

少样本分割（FSS）旨在通过少量类别学习类无关的分割，但容易导致过拟合。为了解决这一问题，部分方法利用基础模型（如SAM）的知识来简化学习过程。SAM 2扩展了视频分割的支持，其类无关匹配能力对FSS非常有用。本文设计了伪提示生成器以编码伪查询记忆，并通过迭代记忆精炼来增强记忆的准确性，最终在PASCAL-5$^i$和COCO-20$^i$上进行的实验表明，1-shot mIoU比最佳基线提高了4.2%。

## 🔬 方法详解

**问题定义**：本文旨在解决少样本分割中由于前景对象身份一致性导致的匹配不兼容问题。现有方法在处理视频数据时，前景对象的身份始终相同，而在FSS中，前景对象身份却是不同的，这造成了匹配步骤的困难。

**核心思路**：为了解决这一问题，本文设计了伪提示生成器来编码伪查询记忆，使其能够与查询特征以兼容的方式进行匹配。同时，通过迭代记忆精炼来增强记忆的准确性，抑制意外的背景特征。

**技术框架**：整体架构包括伪提示生成器、迭代记忆精炼模块和支持校准记忆注意力机制。伪提示生成器负责生成伪查询记忆，迭代记忆精炼则用于不断优化记忆内容，支持校准记忆注意力机制则用于抑制背景特征。

**关键创新**：本文的主要创新在于提出了伪提示生成器和迭代记忆精炼机制，这与现有方法的设计思路有本质区别，能够有效提高少样本分割的性能。

**关键设计**：在参数设置上，本文对记忆的编码方式进行了优化，损失函数设计上考虑了前景与背景特征的区分，网络结构上则采用了多层次的注意力机制来提升模型的表现。

## 📊 实验亮点

实验结果表明，本文方法在PASCAL-5$^i$和COCO-20$^i$数据集上表现优异，1-shot mIoU比最佳基线提高了4.2%，验证了伪提示生成器和迭代记忆精炼的有效性，显著提升了少样本分割的性能。

## 🎯 应用场景

该研究在计算机视觉领域的少样本分割任务中具有重要应用潜力，能够广泛应用于医疗影像分析、自动驾驶、视频监控等场景。通过提高分割精度，能够有效支持智能系统在复杂环境中的决策与操作，未来可能推动相关领域的技术进步与应用普及。

## 📄 摘要（原文）

> Few-Shot Segmentation (FSS) aims to learn class-agnostic segmentation on few classes to segment arbitrary classes, but at the risk of overfitting. To address this, some methods use the well-learned knowledge of foundation models (e.g., SAM) to simplify the learning process. Recently, SAM 2 has extended SAM by supporting video segmentation, whose class-agnostic matching ability is useful to FSS. A simple idea is to encode support foreground (FG) features as memory, with which query FG features are matched and fused. Unfortunately, the FG objects in different frames of SAM 2's video data are always the same identity, while those in FSS are different identities, i.e., the matching step is incompatible. Therefore, we design Pseudo Prompt Generator to encode pseudo query memory, matching with query features in a compatible way. However, the memories can never be as accurate as the real ones, i.e., they are likely to contain incomplete query FG, and some unexpected query background (BG) features, leading to wrong segmentation. Hence, we further design Iterative Memory Refinement to fuse more query FG features into the memory, and devise a Support-Calibrated Memory Attention to suppress the unexpected query BG features in memory. Extensive experiments have been conducted on PASCAL-5$^i$ and COCO-20$^i$ to validate the effectiveness of our design, e.g., the 1-shot mIoU can be 4.2% better than the best baseline.

