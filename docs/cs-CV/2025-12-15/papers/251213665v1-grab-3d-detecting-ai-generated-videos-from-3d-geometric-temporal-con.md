---
layout: default
title: "Grab-3D: Detecting AI-Generated Videos from 3D Geometric Temporal Consistency"
---

# Grab-3D: Detecting AI-Generated Videos from 3D Geometric Temporal Consistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13665" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13665v1</a>
  <a href="https://arxiv.org/pdf/2512.13665.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13665v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.13665v1', 'Grab-3D: Detecting AI-Generated Videos from 3D Geometric Temporal Consistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhan Chen, Sezer Karaoglu, Theo Gevers

**分类**: cs.CV

**发布日期**: 2025-12-15

---

## 💡 一句话要点

**提出Grab-3D，利用3D几何时序一致性检测AI生成视频**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `AI生成视频检测` `3D几何一致性` `Transformer` `消失点` `时序建模`

## 📋 核心要点

1. 现有AI生成视频检测方法对视频中蕴含的3D几何信息利用不足，导致检测性能受限。
2. Grab-3D通过显式建模视频中的3D几何信息（消失点），并结合Transformer架构进行时序建模，从而区分真实视频和AI生成视频。
3. 实验结果表明，Grab-3D在AI生成视频检测任务上显著优于现有方法，并具有良好的跨域泛化能力。

## 📝 摘要（中文）

扩散模型生成技术的发展使得AI模型能够生成高度逼真的视频，因此需要可靠的检测机制。然而，现有的检测方法对生成视频中存在的3D几何模式的探索有限。本文利用消失点作为3D几何模式的显式表示，揭示了真实视频和AI生成视频在几何一致性方面的根本差异。我们提出了Grab-3D，一个基于3D几何时序一致性的几何感知Transformer框架，用于检测AI生成的视频。为了实现可靠的评估，我们构建了一个静态场景的AI生成视频数据集，从而能够稳定地提取3D几何特征。我们提出了一个配备了几何位置编码、时序几何注意力和基于EMA的几何分类器头的几何感知Transformer，以将3D几何感知显式地注入到时间建模中。实验表明，Grab-3D显著优于最先进的检测器，实现了对未见过的生成器的鲁棒的跨域泛化。

## 🔬 方法详解

**问题定义**：当前AI生成视频技术快速发展，但缺乏有效的检测方法。现有方法对视频中的3D几何信息利用不足，难以有效区分真实视频和AI生成视频，尤其是在面对未知的生成器时，泛化能力较差。

**核心思路**：论文的核心思路是利用3D几何时序一致性作为区分真实视频和AI生成视频的关键特征。真实视频通常具有稳定的3D几何结构，而AI生成视频可能存在几何上的不一致性。通过显式地建模和分析视频中的3D几何信息，可以更有效地检测AI生成视频。

**技术框架**：Grab-3D框架主要包含以下几个模块：1) 3D几何特征提取模块：利用消失点作为3D几何信息的显式表示，提取视频帧中的几何特征。2) 几何感知Transformer：该Transformer配备了几何位置编码，用于将几何信息融入到Transformer的输入中；同时，采用时序几何注意力机制，用于建模几何特征的时序关系。3) 基于EMA的几何分类器头：利用指数移动平均（EMA）来提高分类器的鲁棒性和泛化能力。

**关键创新**：论文的关键创新在于：1) 显式地利用3D几何信息进行AI生成视频检测，这与现有方法主要关注图像层面的特征不同。2) 提出了几何感知Transformer，能够有效地建模几何特征的时序关系，并提高检测性能。3) 构建了一个静态场景的AI生成视频数据集，用于评估算法的性能。

**关键设计**：几何位置编码用于将3D几何信息（消失点坐标）嵌入到Transformer的输入中。时序几何注意力机制通过计算不同帧之间几何特征的相似度来建模时序关系。基于EMA的几何分类器头通过对模型参数进行指数移动平均，来提高模型的泛化能力。损失函数采用交叉熵损失函数。

## 📊 实验亮点

Grab-3D在AI生成视频检测任务上取得了显著的性能提升，超越了现有的最先进方法。实验结果表明，Grab-3D不仅在已知生成器上表现出色，而且在未见过的生成器上也具有很强的泛化能力。具体性能数据在论文中给出，表明该方法在跨域泛化方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于内容安全领域，用于检测和识别AI生成的虚假视频，防止恶意传播和信息操纵。此外，该技术还可以应用于视频内容审核、版权保护等领域，具有重要的社会价值和应用前景。

## 📄 摘要（原文）

> Recent advances in diffusion-based generation techniques enable AI models to produce highly realistic videos, heightening the need for reliable detection mechanisms. However, existing detection methods provide only limited exploration of the 3D geometric patterns present in generated videos. In this paper, we use vanishing points as an explicit representation of 3D geometry patterns, revealing fundamental discrepancies in geometric consistency between real and AI-generated videos. We introduce Grab-3D, a geometry-aware transformer framework for detecting AI-generated videos based on 3D geometric temporal consistency. To enable reliable evaluation, we construct an AI-generated video dataset of static scenes, allowing stable 3D geometric feature extraction. We propose a geometry-aware transformer equipped with geometric positional encoding, temporal-geometric attention, and an EMA-based geometric classifier head to explicitly inject 3D geometric awareness into temporal modeling. Experiments demonstrate that Grab-3D significantly outperforms state-of-the-art detectors, achieving robust cross-domain generalization to unseen generators.

