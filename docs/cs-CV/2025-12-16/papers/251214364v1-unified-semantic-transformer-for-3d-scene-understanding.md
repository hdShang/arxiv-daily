---
layout: default
title: Unified Semantic Transformer for 3D Scene Understanding
---

# Unified Semantic Transformer for 3D Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14364" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14364v1</a>
  <a href="https://arxiv.org/pdf/2512.14364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14364v1" onclick="toggleFavorite(this, '2512.14364v1', 'Unified Semantic Transformer for 3D Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sebastian Koch, Johanna Wald, Hide Matsuki, Pedro Hermosilla, Timo Ropinski, Federico Tombari

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://unite-page.github.io/

---

## 💡 一句话要点

**提出UNITE：用于3D场景理解的统一语义Transformer模型**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D场景理解` `语义分割` `Transformer` `知识蒸馏` `多视角学习` `机器人` `计算机视觉`

## 📋 核心要点

1. 现有3D场景理解模型通常是任务特定的，难以处理真实世界环境的复杂性。
2. UNITE通过统一的Transformer架构，从RGB图像直接预测多种语义属性，实现端到端的3D场景理解。
3. UNITE在多个语义任务上取得了SOTA性能，甚至超越了使用ground truth 3D几何的方法。

## 📝 摘要（中文）

本文提出UNITE，一个用于3D场景理解的统一语义Transformer模型，这是一个新颖的前馈神经网络，可在单个模型中统一各种3D语义任务。该模型以完全端到端的方式处理未见过的场景，只需几秒钟即可推断完整的3D语义几何。该方法能够直接预测多个语义属性，包括3D场景分割、实例嵌入、开放词汇特征以及可供性和关节，仅需RGB图像。该方法采用2D知识蒸馏进行训练，严重依赖自监督，并利用新颖的多视角损失，旨在确保3D视角一致性。实验表明，UNITE在多个不同的语义任务上实现了最先进的性能，甚至优于特定于任务的模型，在许多情况下，超过了在真实3D几何上运行的方法。

## 🔬 方法详解

**问题定义**：现有的3D场景理解模型通常是针对特定任务设计的，例如场景分割、目标检测或可供性预测。这些模型无法在一个统一的框架下处理多种语义任务，并且通常需要ground truth 3D几何信息，限制了其在真实世界场景中的应用。因此，如何设计一个能够从RGB图像直接推断多种语义属性，并且能够处理复杂场景的统一模型是一个关键问题。

**核心思路**：UNITE的核心思路是利用Transformer架构的强大表示能力，将不同的3D语义任务统一到一个模型中。通过学习图像的全局上下文信息，UNITE能够预测多种语义属性，例如3D场景分割、实例嵌入、开放词汇特征以及可供性和关节。此外，UNITE还采用了2D知识蒸馏和多视角损失，以提高模型的性能和泛化能力。

**技术框架**：UNITE的整体架构是一个前馈神经网络，它以RGB图像作为输入，并输出多种语义属性。该模型主要包含以下几个模块：1) 图像编码器：用于提取图像的特征表示。2) Transformer编码器：用于学习图像的全局上下文信息。3) 语义解码器：用于预测不同的语义属性。UNITE使用2D图像作为输入，通过知识蒸馏的方式，将2D图像的语义信息迁移到3D场景理解任务中。

**关键创新**：UNITE最重要的技术创新点在于其统一的Transformer架构，它能够在一个模型中处理多种3D语义任务。与现有的任务特定模型相比，UNITE具有更强的泛化能力和更高的效率。此外，UNITE还采用了2D知识蒸馏和多视角损失，以提高模型的性能和鲁棒性。

**关键设计**：UNITE的关键设计包括：1) Transformer编码器的结构和参数设置。2) 语义解码器的设计，包括不同的损失函数和网络结构。3) 2D知识蒸馏的策略，包括如何选择合适的教师模型和如何设计蒸馏损失。4) 多视角损失的设计，包括如何选择不同的视角和如何计算视角一致性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14364v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14364v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14364v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

UNITE在多个3D语义任务上取得了最先进的性能。例如，在3D场景分割任务上，UNITE的性能超过了现有的SOTA模型。在实例嵌入任务上，UNITE能够生成高质量的实例嵌入，用于目标检测和跟踪。更重要的是，UNITE在许多情况下，甚至超越了在真实3D几何上运行的方法，证明了其强大的表示能力和泛化能力。

## 🎯 应用场景

UNITE具有广泛的应用前景，例如机器人导航、自动驾驶、虚拟现实和增强现实等领域。它可以帮助机器人理解周围环境，从而实现更智能的交互和导航。在自动驾驶领域，UNITE可以用于场景理解和行为预测，提高驾驶安全性。在虚拟现实和增强现实领域，UNITE可以用于创建更逼真的3D场景和更自然的交互体验。

## 📄 摘要（原文）

> Holistic 3D scene understanding involves capturing and parsing unstructured 3D environments. Due to the inherent complexity of the real world, existing models have predominantly been developed and limited to be task-specific. We introduce UNITE, a Unified Semantic Transformer for 3D scene understanding, a novel feed-forward neural network that unifies a diverse set of 3D semantic tasks within a single model. Our model operates on unseen scenes in a fully end-to-end manner and only takes a few seconds to infer the full 3D semantic geometry. Our approach is capable of directly predicting multiple semantic attributes, including 3D scene segmentation, instance embeddings, open-vocabulary features, as well as affordance and articulations, solely from RGB images. The method is trained using a combination of 2D distillation, heavily relying on self-supervision and leverages novel multi-view losses designed to ensure 3D view consistency. We demonstrate that UNITE achieves state-of-the-art performance on several different semantic tasks and even outperforms task-specific models, in many cases, surpassing methods that operate on ground truth 3D geometry. See the project website at unite-page.github.io

