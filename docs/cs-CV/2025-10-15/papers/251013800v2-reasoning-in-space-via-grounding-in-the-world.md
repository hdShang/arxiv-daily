---
layout: default
title: Reasoning in Space via Grounding in the World
---

# Reasoning in Space via Grounding in the World

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.13800" class="toolbar-btn" target="_blank">📄 arXiv: 2510.13800v2</a>
  <a href="https://arxiv.org/pdf/2510.13800.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13800v2" onclick="toggleFavorite(this, '2510.13800v2', 'Reasoning in Space via Grounding in the World')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Chen, Zekun Qi, Wenyao Zhang, Xin Jin, Li Zhang, Peidong Liu

**分类**: cs.CV

**发布日期**: 2025-10-15 (更新: 2025-10-16)

**备注**: 20 pages, 7 figures

---

## 💡 一句话要点

**提出基于世界感知的Grounded-Spatial Reasoner，用于提升3D空间推理能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D视觉感知` `空间推理` `大型语言模型` `双路径池化` `自回归模型` `Grounded Chain-of-Thought` `统一3D表示` `机器人`

## 📋 核心要点

1. 现有3D LLM缺乏统一的3D表示，难以同时捕捉语义和几何信息，导致感知性能不佳。
2. 提出双路径池化机制，将几何特征与语义和位置信息对齐，构建统一的3D表示。
3. GS-Reasoner在3D视觉感知和空间推理上均取得优秀结果，并构建了GCoT数据集。

## 📝 摘要（中文）

本文提出3D视觉感知是空间推理的基石，并引入Grounded-Spatial Reasoner (GS-Reasoner) 来探索有效的空间表示，以弥合两者之间的差距。现有的3D LLM缺乏统一的3D表示，无法同时捕获语义和几何信息。这种缺陷体现在感知性能不佳或过度依赖外部模块，最终阻碍了感知和空间推理的无缝集成。为了解决这个问题，我们提出了一种简单而有效的双路径池化机制，将几何特征与语义和位置线索紧密对齐，构建了一种统一的基于图像块的3D表示，该表示封装了所有必要的信息，而不会增加输入token的数量。利用这种整体表示，GS-Reasoner是第一个完全无需外部模块即可实现自回归感知的3D LLM，同时提供与最先进模型相当的性能，从而建立了一个用于3D空间推理的统一且独立的框架。为了进一步弥合感知和空间推理之间的差距，我们引入了Grounded Chain-of-Thought (GCoT) 数据集。该数据集经过精心策划，包括推理问题中引用的对象的3D bounding box标注，以及将感知作为问题解决过程核心组成部分的逐步推理路径。大量的实验表明，GS-Reasoner在3D视觉感知方面取得了令人印象深刻的结果，这反过来又显著提高了其空间推理能力，从而实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有3D大型语言模型（LLM）在空间推理方面表现不佳，主要原因是缺乏能够同时有效捕捉语义和几何信息的统一3D表示。这导致模型要么在3D视觉感知（grounding）任务上表现不佳，要么需要过度依赖外部模块，从而阻碍了感知和空间推理的无缝集成。现有方法的痛点在于无法在模型内部建立起对3D场景的全面理解，需要借助外部信息才能完成推理任务。

**核心思路**：论文的核心思路是通过构建一种统一的3D表示来弥合3D视觉感知和空间推理之间的差距。这种表示需要能够同时编码语义信息（例如，物体的类别）和几何信息（例如，物体的位置和形状）。通过将感知能力融入到推理过程中，模型可以更好地理解场景，从而提高空间推理的准确性。论文通过提出的双路径池化机制来实现这一目标。

**技术框架**：GS-Reasoner的技术框架主要包含以下几个阶段：1) **特征提取**：使用视觉编码器提取图像的视觉特征。2) **双路径池化**：将提取的视觉特征通过双路径池化机制，分别与语义信息和位置信息对齐，生成统一的3D表示。3) **自回归感知**：利用生成的3D表示，GS-Reasoner以自回归的方式进行3D视觉感知，即逐步预测场景中的物体。4) **空间推理**：基于感知到的3D场景，GS-Reasoner进行空间推理，回答与场景相关的推理问题。

**关键创新**：论文最重要的技术创新点在于提出的双路径池化机制，它能够有效地将几何特征与语义和位置线索对齐，从而构建一种统一的、基于图像块的3D表示。这种表示方法无需增加输入token的数量，即可封装所有必要的信息。与现有方法相比，GS-Reasoner无需依赖外部模块即可实现自回归感知，从而建立了一个统一且独立的3D空间推理框架。

**关键设计**：双路径池化机制是GS-Reasoner的关键设计。具体来说，该机制包含两个路径：一个路径用于将几何特征与语义信息对齐，另一个路径用于将几何特征与位置信息对齐。每个路径都使用一个注意力机制来学习几何特征与语义/位置信息之间的关系。此外，论文还提出了Grounded Chain-of-Thought (GCoT) 数据集，该数据集包含3D bounding box标注和逐步推理路径，有助于训练模型进行更有效的空间推理。

## 📊 实验亮点

GS-Reasoner在3D视觉感知任务上取得了与最先进模型相当的性能，同时无需依赖外部模块。在空间推理任务上，GS-Reasoner也取得了显著的性能提升，证明了其有效性。GCoT数据集的引入也为未来的研究提供了有价值的资源。具体性能数据和对比基线在论文中详细给出，表明GS-Reasoner在多个指标上均优于现有方法。

## 🎯 应用场景

该研究成果可应用于机器人导航、自动驾驶、虚拟现实、增强现实等领域。通过提升机器人对周围环境的理解能力，可以使其更好地完成导航、物体识别、操作等任务。在自动驾驶领域，该技术可以提高车辆对复杂交通场景的感知和推理能力，从而提高驾驶安全性。在VR/AR领域，该技术可以增强用户与虚拟/现实环境的交互体验。

## 📄 摘要（原文）

> In this paper, we claim that 3D visual grounding is the cornerstone of spatial reasoning and introduce the Grounded-Spatial Reasoner (GS-Reasoner) to explore the effective spatial representations that bridge the gap between them. Existing 3D LLMs suffer from the absence of a unified 3D representation capable of jointly capturing semantic and geometric information. This deficiency is manifested either in poor performance on grounding or in an excessive reliance on external modules, ultimately hindering the seamless integration of grounding and spatial reasoning. To address this, we propose a simple yet effective dual-path pooling mechanism that tightly aligns geometric features with both semantic and positional cues, constructing a unified image patch-based 3D representation that encapsulates all essential information without increasing the number of input tokens. Leveraging this holistic representation, GS-Reasoner is the first 3D LLM that achieves autoregressive grounding entirely without external modules while delivering performance comparable to state-of-the-art models, establishing a unified and self-contained framework for 3D spatial reasoning. To further bridge grounding and spatial reasoning, we introduce the Grounded Chain-of-Thought (GCoT) dataset. This dataset is meticulously curated to include both 3D bounding box annotations for objects referenced in reasoning questions and step-by-step reasoning paths that integrate grounding as a core component of the problem-solving process. Extensive experiments demonstrate that GS-Reasoner achieves impressive results on 3D visual grounding, which in turn significantly enhances its spatial reasoning capabilities, leading to state-of-the-art performance.

