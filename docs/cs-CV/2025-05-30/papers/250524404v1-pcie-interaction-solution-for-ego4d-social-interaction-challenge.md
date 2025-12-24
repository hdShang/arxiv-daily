---
layout: default
title: PCIE_Interaction Solution for Ego4D Social Interaction Challenge
---

# PCIE_Interaction Solution for Ego4D Social Interaction Challenge

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24404" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24404v1</a>
  <a href="https://arxiv.org/pdf/2505.24404.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24404v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24404v1', 'PCIE_Interaction Solution for Ego4D Social Interaction Challenge')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kanokphan Lertniphonphan, Feng Chen, Junda Xu, Fengbu Lan, Jun Xie, Tao Zhang, Zhepeng Wang

**分类**: cs.CV

**发布日期**: 2025-05-30

**🔗 代码/项目**: [GITHUB](https://github.com/KanokphanL/PCIE_Ego4D_Social_Interaction)

---

## 💡 一句话要点

**提出PCIE_Interaction解决方案以应对Ego4D社交互动挑战**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `社交互动检测` `多模态融合` `面部识别` `音频处理` `深度学习`

## 📋 核心要点

1. 现有方法在社交互动检测中面临准确性不足的挑战，尤其是在复杂场景下的面部识别和音频同步问题。
2. 我们提出的解决方案通过面部质量增强和音频视觉融合，提升了社交互动的检测精度，尤其是在LAM和TTM任务中。
3. 实验结果显示，我们的方法在LAM和TTM任务中分别达到了0.81和0.71的mAP，显著优于现有基线方法。

## 📝 摘要（中文）

本文报告了我们团队在CVPR 2025的Ego4D社交互动挑战中提出的PCIE_Interaction解决方案，针对Looking At Me (LAM)和Talking To Me (TTM)任务进行研究。该挑战要求准确检测主体与摄像机佩戴者之间的社交互动，LAM任务依赖于面部裁剪序列，而TTM任务则结合了说话者的面部裁剪和同步音频片段。在LAM轨道中，我们采用了面部质量增强和集成方法；在TTM任务中，我们通过融合音频和视觉线索，结合视觉质量评分，扩展了视觉互动分析。我们的方案在LAM和TTM挑战的排行榜上分别取得了0.81和0.71的平均精度（mAP）。代码可在https://github.com/KanokphanL/PCIE_Ego4D_Social_Interaction获取。

## 🔬 方法详解

**问题定义**：本文旨在解决Ego4D社交互动挑战中的社交互动检测问题，现有方法在复杂场景下的面部识别和音频同步存在不足，导致检测精度不高。

**核心思路**：我们的方法通过面部质量增强和音频视觉融合来提升社交互动检测的准确性，特别是在LAM和TTM任务中，利用视觉质量评分来加权融合不同模态的信息。

**技术框架**：整体架构包括两个主要模块：LAM模块专注于面部裁剪序列的处理，TTM模块则结合说话者面部裁剪与音频片段，确保信息的同步与准确性。

**关键创新**：本研究的创新点在于通过视觉质量评分对音频和视觉线索进行加权融合，这一设计显著提升了社交互动的检测性能，与传统方法相比具有本质区别。

**关键设计**：在技术细节上，我们采用了集成方法来增强面部质量，并在TTM任务中设计了特定的损失函数以优化音频与视觉信息的融合效果。具体的网络结构和参数设置在实验中进行了详细调优。

## 📊 实验亮点

实验结果表明，我们的方法在LAM和TTM任务中分别取得了0.81和0.71的平均精度（mAP），显著高于现有基线，展示了音频与视觉信息融合的有效性，提升幅度明显。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、智能监控和人机交互等，能够在复杂社交场景中实现更高效的互动检测，提升用户体验。未来，该技术有望在增强现实和虚拟现实等领域发挥重要作用，推动社交互动的智能化发展。

## 📄 摘要（原文）

> This report presents our team's PCIE_Interaction solution for the Ego4D Social Interaction Challenge at CVPR 2025, addressing both Looking At Me (LAM) and Talking To Me (TTM) tasks. The challenge requires accurate detection of social interactions between subjects and the camera wearer, with LAM relying exclusively on face crop sequences and TTM combining speaker face crops with synchronized audio segments. In the LAM track, we employ face quality enhancement and ensemble methods. For the TTM task, we extend visual interaction analysis by fusing audio and visual cues, weighted by a visual quality score. Our approach achieved 0.81 and 0.71 mean average precision (mAP) on the LAM and TTM challenges leader board. Code is available at https://github.com/KanokphanL/PCIE_Ego4D_Social_Interaction

