---
layout: default
title: "Learning Yourself: Class-Incremental Semantic Segmentation with Language-Inspired Bootstrapped Disentanglement"
---

# Learning Yourself: Class-Incremental Semantic Segmentation with Language-Inspired Bootstrapped Disentanglement

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.00527" class="toolbar-btn" target="_blank">📄 arXiv: 2509.00527v1</a>
  <a href="https://arxiv.org/pdf/2509.00527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.00527v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.00527v1', 'Learning Yourself: Class-Incremental Semantic Segmentation with Language-Inspired Bootstrapped Disentanglement')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ruitao Wu, Yifan Zhao, Jia Li

**分类**: cs.CV

**发布日期**: 2025-08-30

**备注**: Accepted by ICCV 2025

---

## 💡 一句话要点

**提出语言启发的自我学习框架以解决增量语义分割中的灾难性语义纠缠问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `增量学习` `语义分割` `特征解缠` `视觉-语言模型` `CLIP` `多步学习` `自动驾驶` `机器人视觉`

## 📋 核心要点

1. 现有增量语义分割方法面临灾难性语义纠缠问题，导致新旧类知识难以有效区分。
2. 提出语言启发的自我学习框架（LBD），通过语言引导的解缠方法来改善特征区分能力。
3. 在Pascal VOC和ADE20k数据集上取得了最先进的性能，特别是在多步增量学习场景中表现突出。

## 📝 摘要（中文）

增量语义分割（CISS）需要在持续学习新类的同时保留对过去类的知识。本文识别出一种称为灾难性语义纠缠的根本挑战，主要包括原型特征纠缠和背景增量纠缠。现有技术依赖于视觉特征学习，缺乏足够的目标区分线索，导致显著噪声和错误。为了解决这些问题，本文提出了一种语言启发的自我学习框架（LBD），利用预训练视觉-语言模型的先前类语义，通过语言引导的原型解缠和流形互背景解缠来指导模型自主解缠特征。通过软提示调优和编码器适应性修改，进一步缩小了CLIP在稠密和稀疏任务之间的能力差距，在Pascal VOC和ADE20k数据集上实现了最先进的性能，尤其是在多步场景中。

## 🔬 方法详解

**问题定义**：本文旨在解决增量语义分割中的灾难性语义纠缠问题，现有方法在特征学习中缺乏有效的目标区分线索，导致原型特征和背景特征的混淆。

**核心思路**：提出的LBD框架利用预训练的视觉-语言模型的语义信息，通过语言引导的解缠方法，帮助模型自主区分新旧类特征，减少语义纠缠。

**技术框架**：LBD框架分为两个主要模块：语言引导的原型解缠和流形互背景解缠。前者通过手工文本特征作为拓扑模板指导新原型的解缠，后者则使用多个可学习原型和基于掩膜池的监督进行背景增量类的解缠。

**关键创新**：最重要的创新在于引入了语言引导的解缠机制，利用语言模型的语义信息来解决传统方法中的特征混淆问题，这一方法在增量学习中具有独特的优势。

**关键设计**：在设计中，采用了软提示调优和编码器适应性修改，以缩小CLIP在稠密和稀疏任务之间的能力差距，确保模型在不同任务中的有效性。具体的损失函数和网络结构细节未在摘要中详细说明，需参考原文。

## 📊 实验亮点

在Pascal VOC和ADE20k数据集上，LBD框架实现了最先进的性能，尤其在多步增量学习场景中，相较于基线方法，性能提升显著，具体提升幅度和数值需参考原文。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人视觉和医疗图像分析等需要增量学习的场景。通过有效地处理新旧类之间的知识迁移，LBD框架能够提高模型在动态环境中的适应能力，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Class-Incremental Semantic Segmentation (CISS) requires continuous learning of newly introduced classes while retaining knowledge of past classes. By abstracting mainstream methods into two stages (visual feature extraction and prototype-feature matching), we identify a more fundamental challenge termed catastrophic semantic entanglement. This phenomenon involves Prototype-Feature Entanglement caused by semantic misalignment during the incremental process, and Background-Increment Entanglement due to dynamic data evolution. Existing techniques, which rely on visual feature learning without sufficient cues to distinguish targets, introduce significant noise and errors. To address these issues, we introduce a Language-inspired Bootstrapped Disentanglement framework (LBD). We leverage the prior class semantics of pre-trained visual-language models (e.g., CLIP) to guide the model in autonomously disentangling features through Language-guided Prototypical Disentanglement and Manifold Mutual Background Disentanglement. The former guides the disentangling of new prototypes by treating hand-crafted text features as topological templates, while the latter employs multiple learnable prototypes and mask-pooling-based supervision for background-incremental class disentanglement. By incorporating soft prompt tuning and encoder adaptation modifications, we further bridge the capability gap of CLIP between dense and sparse tasks, achieving state-of-the-art performance on both Pascal VOC and ADE20k, particularly in multi-step scenarios.

