---
layout: default
title: "HERO-VQL: Hierarchical, Egocentric and Robust Visual Query Localization"
---

# HERO-VQL: Hierarchical, Egocentric and Robust Visual Query Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00385" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00385v1</a>
  <a href="https://arxiv.org/pdf/2509.00385.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00385v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00385v1', 'HERO-VQL: Hierarchical, Egocentric and Robust Visual Query Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Joohyun Chang, Soyeon Hong, Hyogun Lee, Seong Jong Ha, Dongho Lee, Seong Tae Kim, Jinwoo Choi

**分类**: cs.CV

**发布日期**: 2025-08-30

**备注**: Accepted to BMVC 2025 (Oral), 23 pages with supplementary material

---

## 💡 一句话要点

**提出HERO-VQL以解决自我中心视频中的视觉查询定位问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `自我中心视频` `视觉查询定位` `注意力机制` `一致性训练` `物体识别` `深度学习` `计算机视觉`

## 📋 核心要点

1. 自我中心视频中的频繁视角变化导致对象外观变化和遮挡，现有方法难以实现准确定位。
2. HERO-VQL通过自上而下的注意力引导和自我中心增强训练来提高查询对象的定位精度。
3. 在VQ2D数据集上的实验结果表明，HERO-VQL显著优于现有基线，提升了定位的准确性和稳定性。

## 📝 摘要（中文）

本研究针对自我中心视觉查询定位（VQL）问题，提出了一种新方法HERO-VQL，该方法旨在处理长时间自我中心视频中的查询对象定位。由于自我中心视频中频繁且突发的视角变化，导致对象外观的显著变化和部分遮挡，使得现有方法难以实现准确定位。HERO-VQL受人类物体识别的认知过程启发，提出了自上而下的注意力引导（TAG）和基于自我中心增强的一致性训练（EgoACT）。通过这些创新，HERO-VQL在VQ2D数据集上的实验结果显示，能够有效应对自我中心视频中的挑战，显著优于基线方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决自我中心视频中的视觉查询定位问题。现有方法在处理频繁视角变化和对象遮挡时表现不佳，导致定位精度不足。

**核心思路**：HERO-VQL的核心思路是模拟人类的物体识别过程，通过引入自上而下的注意力引导和自我中心增强训练来提高模型的定位能力。这样的设计旨在增强模型对复杂场景的适应性。

**技术框架**：HERO-VQL的整体架构包括两个主要模块：自上而下的注意力引导（TAG）和基于自我中心增强的一致性训练（EgoACT）。TAG利用类别标记和主成分得分图进行高层次上下文的提炼，而EgoACT则通过替换查询对象和重新排序视频帧来增强查询的多样性。

**关键创新**：HERO-VQL的主要创新在于结合了TAG和EgoACT两种机制，显著提升了模型在自我中心视频中的定位能力。这种方法与现有技术的本质区别在于其对视角变化的鲁棒性和对查询对象多样性的处理。

**关键设计**：在模型设计中，TAG模块通过类别标记和主成分得分图进行注意力机制的优化，同时EgoACT通过随机选择对应对象和极端视角变化模拟来增强训练。此外，CT损失函数确保了在不同增强场景下的稳定定位。

## 📊 实验亮点

在VQ2D数据集上的实验结果显示，HERO-VQL在自我中心视觉查询定位任务中显著优于基线方法，定位准确率提升幅度达到XX%。该方法有效应对了自我中心视频中的视角变化和遮挡问题，展示了其在复杂场景下的鲁棒性。

## 🎯 应用场景

HERO-VQL的研究成果在多个领域具有潜在应用价值，尤其是在虚拟现实、增强现实和自动驾驶等需要实时物体识别和定位的场景中。通过提高自我中心视频的理解能力，该方法能够为智能系统提供更准确的环境感知，进而提升用户体验和安全性。

## 📄 摘要（原文）

> In this work, we tackle the egocentric visual query localization (VQL), where a model should localize the query object in a long-form egocentric video. Frequent and abrupt viewpoint changes in egocentric videos cause significant object appearance variations and partial occlusions, making it difficult for existing methods to achieve accurate localization. To tackle these challenges, we introduce Hierarchical, Egocentric and RObust Visual Query Localization (HERO-VQL), a novel method inspired by human cognitive process in object recognition. We propose i) Top-down Attention Guidance (TAG) and ii) Egocentric Augmentation based Consistency Training (EgoACT). Top-down Attention Guidance refines the attention mechanism by leveraging the class token for high-level context and principal component score maps for fine-grained localization. To enhance learning in diverse and challenging matching scenarios, EgoAug enhances query diversity by replacing the query with a randomly selected corresponding object from groundtruth annotations and simulates extreme viewpoint changes by reordering video frames. Additionally, CT loss enforces stable object localization across different augmentation scenarios. Extensive experiments on VQ2D dataset validate that HERO-VQL effectively handles egocentric challenges, significantly outperforming baselines.

