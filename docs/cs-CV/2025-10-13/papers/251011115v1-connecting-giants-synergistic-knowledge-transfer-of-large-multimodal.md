---
layout: default
title: Connecting Giants: Synergistic Knowledge Transfer of Large Multimodal Models for Few-Shot Learning
---

# Connecting Giants: Synergistic Knowledge Transfer of Large Multimodal Models for Few-Shot Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11115" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11115v1</a>
  <a href="https://arxiv.org/pdf/2510.11115.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11115v1" onclick="toggleFavorite(this, '2510.11115v1', 'Connecting Giants: Synergistic Knowledge Transfer of Large Multimodal Models for Few-Shot Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Tang, Shengfeng He, Jing Qin

**分类**: cs.CV, cs.MM

**发布日期**: 2025-10-13

**备注**: Accepted by IJCAI 2025

---

## 💡 一句话要点

**提出SynTrans框架，利用大型多模态模型协同知识迁移提升少样本学习性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `少样本学习` `知识迁移` `多模态学习` `协同学习` `视觉语义桥接` `知识蒸馏` `CLIP`

## 📋 核心要点

1. 少样本学习面临数据稀缺的挑战，现有方法利用小规模模型的语义知识，但易引入噪声和偏差。
2. SynTrans框架通过知识蒸馏、协同知识挖掘和视觉-语义桥接，实现大型多模态模型知识的有效迁移。
3. 实验表明，SynTrans即使搭配简单的视觉编码器，也能显著超越现有少样本学习方法。

## 📝 摘要（中文）

本文提出了一种新颖的协同知识迁移（SynTrans）框架，旨在有效迁移大型多模态模型中多样且互补的知识，从而增强现有少样本学习器的能力。SynTrans采用CLIP作为强大的教师模型，并使用少样本视觉编码器作为弱学生模型，通过无监督代理任务提炼语义对齐的视觉知识。随后，一个无需训练的协同知识挖掘模块促进大型多模态模型之间的协作，以提取高质量的语义知识。在此基础上，视觉-语义桥接模块实现了视觉和语义空间之间的双向知识迁移，将显式的视觉知识和隐式的语义知识转化为特定类别的分类器权重。最后，SynTrans引入了视觉权重生成器和语义权重重构器，以自适应地构建最优的多模态少样本学习分类器。在四个少样本学习数据集上的实验结果表明，即使与简单的少样本视觉编码器配对，SynTrans也显著优于当前最先进的方法。

## 🔬 方法详解

**问题定义**：少样本学习旨在仅利用少量样本对新类别进行分类。现有方法尝试利用外部知识，但通常依赖于规模较小的模型，这些模型提供的语义知识可能不够丰富，并且容易引入噪声和偏差，限制了少样本学习的性能。

**核心思路**：SynTrans的核心思路是利用大型多模态模型（如CLIP）中蕴含的丰富视觉和语义知识，通过知识迁移的方式提升少样本学习器的性能。该方法通过协同多个大型模型，提取互补的知识，并设计模块实现视觉和语义知识的有效融合，从而克服了传统方法中知识来源单一和易引入噪声的问题。

**技术框架**：SynTrans框架包含以下几个主要模块：1) **知识蒸馏模块**：使用CLIP作为教师模型，将语义对齐的视觉知识蒸馏到少样本视觉编码器中。2) **协同知识挖掘模块**：促进多个大型多模态模型之间的协作，提取高质量的语义知识。3) **视觉-语义桥接模块**：实现视觉和语义空间之间的双向知识迁移，将视觉和语义知识转化为分类器权重。4) **权重生成与重构模块**：自适应地生成视觉权重和重构语义权重，构建最优的多模态少样本学习分类器。

**关键创新**：SynTrans的关键创新在于：1) **协同知识迁移**：通过协同多个大型多模态模型，提取互补的知识，避免了单一知识来源的局限性。2) **视觉-语义桥接**：实现了视觉和语义空间之间的双向知识迁移，充分利用了视觉和语义信息。3) **自适应权重生成与重构**：能够根据不同类别的特点，自适应地生成视觉权重和重构语义权重，提升了分类器的性能。

**关键设计**：在知识蒸馏模块中，使用无监督代理任务来对齐视觉和语义空间。在协同知识挖掘模块中，设计特定的策略来促进不同模型之间的知识共享。在视觉-语义桥接模块中，使用线性变换将视觉和语义特征映射到同一空间。在权重生成与重构模块中，使用神经网络来生成视觉权重和重构语义权重，并使用损失函数来优化这些权重。

## 📊 实验亮点

SynTrans在四个少样本学习数据集上取得了显著的性能提升，超越了当前最先进的方法。即使与简单的少样本视觉编码器搭配使用，SynTrans也能取得优异的性能，证明了其知识迁移策略的有效性。具体实验数据在论文中有详细展示，表明SynTrans在少样本学习领域具有强大的竞争力。

## 🎯 应用场景

SynTrans框架可应用于图像分类、目标检测等多种计算机视觉任务，尤其适用于数据标注成本高昂的场景，例如医学图像分析、遥感图像解译等。通过利用大型多模态模型的知识，该方法能够显著降低对标注数据的需求，提高模型的泛化能力和实用性，具有重要的实际应用价值。

## 📄 摘要（原文）

> Few-shot learning (FSL) addresses the challenge of classifying novel classes with limited training samples. While some methods leverage semantic knowledge from smaller-scale models to mitigate data scarcity, these approaches often introduce noise and bias due to the data's inherent simplicity. In this paper, we propose a novel framework, Synergistic Knowledge Transfer (SynTrans), which effectively transfers diverse and complementary knowledge from large multimodal models to empower the off-the-shelf few-shot learner. Specifically, SynTrans employs CLIP as a robust teacher and uses a few-shot vision encoder as a weak student, distilling semantic-aligned visual knowledge via an unsupervised proxy task. Subsequently, a training-free synergistic knowledge mining module facilitates collaboration among large multimodal models to extract high-quality semantic knowledge. Building upon this, a visual-semantic bridging module enables bi-directional knowledge transfer between visual and semantic spaces, transforming explicit visual and implicit semantic knowledge into category-specific classifier weights. Finally, SynTrans introduces a visual weight generator and a semantic weight reconstructor to adaptively construct optimal multimodal FSL classifiers. Experimental results on four FSL datasets demonstrate that SynTrans, even when paired with a simple few-shot vision encoder, significantly outperforms current state-of-the-art methods.

