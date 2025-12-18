---
layout: default
title: Unified Semantic Transformer for 3D Scene Understanding
---

# Unified Semantic Transformer for 3D Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14364" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14364v1</a>
  <a href="https://arxiv.org/pdf/2512.14364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14364v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14364v1', 'Unified Semantic Transformer for 3D Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sebastian Koch, Johanna Wald, Hide Matsuki, Pedro Hermosilla, Timo Ropinski, Federico Tombari

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://unite-page.github.io/

---

## 💡 一句话要点

**提出UNITE：用于3D场景理解的统一语义Transformer模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景理解` `语义分割` `实例分割` `Transformer` `知识蒸馏` `多视角学习` `自监督学习`

## 📋 核心要点

1. 现有3D场景理解模型通常是任务特定的，难以处理真实世界复杂性。
2. UNITE通过统一的Transformer架构，从RGB图像直接预测多种语义属性。
3. UNITE在多个语义任务上达到SOTA，甚至超越了使用3D几何信息的模型。

## 📝 摘要（中文）

本文提出了一种用于3D场景理解的统一语义Transformer模型UNITE，它是一个新颖的前馈神经网络，可以在单个模型中统一处理各种3D语义任务。该模型以完全端到端的方式处理未见过的场景，只需几秒钟即可推断出完整的3D语义几何结构。该方法能够直接从RGB图像预测多个语义属性，包括3D场景分割、实例嵌入、开放词汇特征以及可供性和关节。该方法采用2D知识蒸馏进行训练，大量依赖自监督，并利用新颖的多视角损失来确保3D视角一致性。实验表明，UNITE在多个不同的语义任务上实现了最先进的性能，甚至优于特定任务的模型，在许多情况下，超过了使用真实3D几何数据的方法。

## 🔬 方法详解

**问题定义**：现有的3D场景理解模型通常是针对特定任务设计的，例如场景分割、实例分割或可供性预测。这些模型无法在一个统一的框架下处理多种语义任务，并且通常需要大量的标注数据。此外，许多方法依赖于3D几何信息，限制了它们在只有RGB图像可用的场景中的应用。

**核心思路**：UNITE的核心思路是利用Transformer架构的强大表示能力，将不同的3D语义任务统一到一个模型中。通过使用2D知识蒸馏和多视角一致性损失，UNITE可以从RGB图像中学习到丰富的3D语义信息，而无需依赖大量的3D标注数据。这种统一的方法使得UNITE能够同时预测多个语义属性，并且在不同的任务上都表现出色。

**技术框架**：UNITE的整体架构是一个基于Transformer的编码器-解码器结构。编码器负责从RGB图像中提取特征，解码器负责预测各种语义属性，包括3D场景分割、实例嵌入、开放词汇特征以及可供性和关节。该模型采用多头注意力机制来捕捉图像中的长程依赖关系，并使用前馈神经网络来处理每个位置的特征。

**关键创新**：UNITE的关键创新在于其统一的架构和训练方法。通过将不同的3D语义任务统一到一个模型中，UNITE可以共享特征表示，从而提高整体性能。此外，UNITE使用2D知识蒸馏和多视角一致性损失来利用未标注的数据，从而减少了对3D标注数据的依赖。

**关键设计**：UNITE的关键设计包括以下几个方面：1) 使用ResNet作为图像编码器的骨干网络。2) 使用Transformer编码器-解码器结构来预测语义属性。3) 使用2D知识蒸馏来从预训练的2D模型中转移知识。4) 使用多视角一致性损失来确保3D视角的一致性。5) 使用Adam优化器进行训练，并采用学习率衰减策略。

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

UNITE在ScanNet、Matterport3D等数据集上进行了评估，并在多个语义任务上取得了最先进的性能。例如，在3D语义分割任务上，UNITE的性能优于现有的基于点云的方法。在实例分割任务上，UNITE的性能也优于现有的方法。此外，UNITE还展示了其在开放词汇特征预测和可供性预测方面的能力。

## 🎯 应用场景

UNITE在机器人导航、自动驾驶、增强现实等领域具有广泛的应用前景。它可以帮助机器人理解周围环境，从而更好地进行导航和交互。在自动驾驶领域，UNITE可以用于场景理解和障碍物检测。在增强现实领域，UNITE可以用于场景重建和虚拟对象放置。此外，UNITE还可以用于3D场景编辑和生成等任务。

## 📄 摘要（原文）

> Holistic 3D scene understanding involves capturing and parsing unstructured 3D environments. Due to the inherent complexity of the real world, existing models have predominantly been developed and limited to be task-specific. We introduce UNITE, a Unified Semantic Transformer for 3D scene understanding, a novel feed-forward neural network that unifies a diverse set of 3D semantic tasks within a single model. Our model operates on unseen scenes in a fully end-to-end manner and only takes a few seconds to infer the full 3D semantic geometry. Our approach is capable of directly predicting multiple semantic attributes, including 3D scene segmentation, instance embeddings, open-vocabulary features, as well as affordance and articulations, solely from RGB images. The method is trained using a combination of 2D distillation, heavily relying on self-supervision and leverages novel multi-view losses designed to ensure 3D view consistency. We demonstrate that UNITE achieves state-of-the-art performance on several different semantic tasks and even outperforms task-specific models, in many cases, surpassing methods that operate on ground truth 3D geometry. See the project website at unite-page.github.io

