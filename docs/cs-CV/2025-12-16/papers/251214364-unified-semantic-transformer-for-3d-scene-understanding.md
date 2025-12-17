---
layout: default
title: Unified Semantic Transformer for 3D Scene Understanding
---

# Unified Semantic Transformer for 3D Scene Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14364" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14364</a>
  <a href="https://arxiv.org/pdf/2512.14364.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14364" onclick="toggleFavorite(this, '2512.14364', 'Unified Semantic Transformer for 3D Scene Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sebastian Koch, Johanna Wald, Hide Matsuki, Pedro Hermosilla, Timo Ropinski, Federico Tombari

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出UNITE：用于3D场景理解的统一语义Transformer模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景理解` `语义分割` `Transformer` `知识蒸馏` `自监督学习` `多视角学习` `机器人视觉`

## 📋 核心要点

1. 现有3D场景理解模型通常是任务特定的，难以处理真实世界环境的复杂性。
2. UNITE通过统一的Transformer架构，从RGB图像直接预测多种语义属性，实现端到端的3D场景理解。
3. UNITE在多个语义任务上取得了SOTA性能，甚至超越了使用真实3D几何信息的特定任务模型。

## 📝 摘要（中文）

本文提出UNITE，一种用于3D场景理解的统一语义Transformer模型。该模型是一个新颖的前馈神经网络，它在一个单一模型中统一了多种3D语义任务。UNITE以完全端到端的方式处理未见过的场景，只需几秒钟即可推断出完整的3D语义几何结构。该方法能够仅从RGB图像直接预测多个语义属性，包括3D场景分割、实例嵌入、开放词汇特征以及可供性和关节。该模型采用2D知识蒸馏进行训练，大量依赖自监督，并利用新颖的多视角损失来确保3D视角一致性。实验表明，UNITE在多个不同的语义任务上实现了最先进的性能，甚至优于特定任务的模型，在许多情况下，超过了在真实3D几何上运行的方法。

## 🔬 方法详解

**问题定义**：现有的3D场景理解模型通常是针对特定任务设计的，例如场景分割、实例分割或可供性预测。这些模型无法在一个统一的框架下处理多种语义任务，并且通常需要ground truth 3D几何信息。因此，如何设计一个能够从RGB图像中直接预测多种语义属性，并且能够处理未见过的场景的统一模型是一个挑战。

**核心思路**：UNITE的核心思路是利用Transformer架构的强大表示能力，将不同的3D语义任务统一到一个模型中。通过共享的特征表示，模型可以学习不同任务之间的关联性，从而提高整体性能。此外，模型采用2D知识蒸馏和自监督学习，以减少对ground truth 3D几何信息的依赖。

**技术框架**：UNITE的整体架构是一个前馈神经网络，它以RGB图像作为输入，并输出多个语义属性，包括3D场景分割、实例嵌入、开放词汇特征、可供性和关节。该模型包含一个图像编码器，用于提取图像特征；一个Transformer编码器，用于学习特征之间的关系；以及多个解码器，用于预测不同的语义属性。模型采用多视角损失函数，以确保3D视角一致性。

**关键创新**：UNITE的关键创新在于它是一个统一的3D场景理解模型，能够在一个单一框架下处理多种语义任务。与现有的特定任务模型相比，UNITE具有更强的泛化能力和更高的效率。此外，UNITE采用2D知识蒸馏和自监督学习，减少了对ground truth 3D几何信息的依赖。

**关键设计**：UNITE的关键设计包括：1) 使用Transformer编码器来学习特征之间的关系；2) 采用多视角损失函数来确保3D视角一致性；3) 使用2D知识蒸馏和自监督学习来减少对ground truth 3D几何信息的依赖。具体的损失函数包括分割损失、实例嵌入损失、开放词汇特征损失、可供性损失和关节损失。网络结构细节未在摘要中详细说明，具体实现可能参考了Transformer相关的经典设计。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14364/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14364/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14364/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

UNITE在多个3D语义任务上取得了state-of-the-art的性能，包括3D场景分割、实例嵌入、开放词汇特征、可供性和关节预测。在许多情况下，UNITE甚至超过了使用ground truth 3D几何信息的特定任务模型。具体的性能数据未在摘要中给出，需要在论文正文中查找。

## 🎯 应用场景

UNITE具有广泛的应用前景，例如机器人导航、自动驾驶、增强现实和虚拟现实。它可以帮助机器人理解周围环境，从而实现更智能的交互。在自动驾驶领域，UNITE可以用于识别道路上的物体和场景，从而提高驾驶安全性。在AR/VR领域，UNITE可以用于创建更逼真的虚拟环境，并实现更自然的交互。

## 📄 摘要（原文）

> Holistic 3D scene understanding involves capturing and parsing unstructured 3D environments. Due to the inherent complexity of the real world, existing models have predominantly been developed and limited to be task-specific. We introduce UNITE, a Unified Semantic Transformer for 3D scene understanding, a novel feed-forward neural network that unifies a diverse set of 3D semantic tasks within a single model. Our model operates on unseen scenes in a fully end-to-end manner and only takes a few seconds to infer the full 3D semantic geometry. Our approach is capable of directly predicting multiple semantic attributes, including 3D scene segmentation, instance embeddings, open-vocabulary features, as well as affordance and articulations, solely from RGB images. The method is trained using a combination of 2D distillation, heavily relying on self-supervision and leverages novel multi-view losses designed to ensure 3D view consistency. We demonstrate that UNITE achieves state-of-the-art performance on several different semantic tasks and even outperforms task-specific models, in many cases, surpassing methods that operate on ground truth 3D geometry. See the project website atthis http URL

