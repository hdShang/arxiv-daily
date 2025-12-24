---
layout: default
title: "BokehFlow: Depth-Free Controllable Bokeh Rendering via Flow Matching"
---

# BokehFlow: Depth-Free Controllable Bokeh Rendering via Flow Matching

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.15066" class="toolbar-btn" target="_blank">📄 arXiv: 2511.15066v1</a>
  <a href="https://arxiv.org/pdf/2511.15066.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.15066v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.15066v1', 'BokehFlow: Depth-Free Controllable Bokeh Rendering via Flow Matching')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yachuan Huang, Xianrui Luo, Qiwen Wang, Liao Shen, Jiaqi Li, Huiqiang Sun, Zihao Huang, Wei Jiang, Zhiguo Cao

**分类**: cs.CV

**发布日期**: 2025-11-19

---

## 💡 一句话要点

**提出BokehFlow，一种基于Flow Matching的无深度信息可控焦外成像方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `焦外成像` `散景` `Flow Matching` `无深度信息` `文本控制`

## 📋 核心要点

1. 现有可控焦外成像方法依赖深度信息，生成式方法可控性和效率不足，限制了应用。
2. BokehFlow基于Flow Matching，直接从全聚焦图像合成焦外成像，无需深度输入。
3. 实验表明，BokehFlow在渲染质量和效率上优于现有方法，并提供精确的语义控制。

## 📝 摘要（中文）

本文提出了一种名为BokehFlow的无深度信息的可控焦外成像框架，旨在模拟摄影中浅景深效果，增强视觉美感并将观众注意力引导至感兴趣的区域。现有可控方法依赖于精确的深度图，而生成式方法在可控性和效率方面存在局限性。BokehFlow直接从全聚焦图像合成逼真的焦外成像效果，无需深度输入。它采用交叉注意力机制，通过文本提示实现对焦点区域和模糊强度的语义控制。为了支持训练和评估，我们收集并合成了四个数据集。大量实验表明，BokehFlow实现了视觉上引人注目的焦外成像效果，并提供了精确的控制，在渲染质量和效率方面均优于现有的深度依赖和生成式方法。

## 🔬 方法详解

**问题定义**：现有可控焦外成像方法主要依赖于精确的深度图，这限制了其在缺乏深度信息的场景中的应用。而基于生成模型的方法虽然可以生成焦外成像效果，但在可控性和生成效率方面存在不足，难以实现对焦点区域和模糊程度的精确控制。因此，如何在没有深度信息的情况下，实现高质量、可控的焦外成像是一个重要的挑战。

**核心思路**：BokehFlow的核心思路是利用Flow Matching技术，直接学习从全聚焦图像到具有特定焦外成像效果图像的映射关系。通过引入文本提示，实现对焦点区域和模糊程度的语义控制。这种方法避免了对深度信息的依赖，并提供了更灵活的控制方式。

**技术框架**：BokehFlow的整体框架包含以下几个主要模块：1) 全聚焦图像输入模块；2) 文本提示输入模块；3) 基于Flow Matching的图像生成模块；4) 交叉注意力机制模块。全聚焦图像和文本提示分别输入到对应的模块中，Flow Matching模块负责生成具有焦外成像效果的图像，交叉注意力机制则用于将文本提示信息融入到图像生成过程中，实现对焦点区域和模糊程度的控制。

**关键创新**：BokehFlow最重要的技术创新点在于其无深度信息的焦外成像方法，以及基于Flow Matching的图像生成框架。与传统的深度依赖方法相比，BokehFlow无需深度信息，适用范围更广。与生成式方法相比，Flow Matching提供了更强的可控性和更高的生成效率。

**关键设计**：BokehFlow的关键设计包括：1) 交叉注意力机制，用于将文本提示信息融入到图像生成过程中，实现对焦点区域和模糊程度的控制；2) Flow Matching的损失函数设计，用于优化图像生成过程，提高生成图像的质量；3) 数据集的构建，为了支持训练和评估，论文收集并合成了四个数据集。

## 📊 实验亮点

实验结果表明，BokehFlow在视觉质量和效率上均优于现有的深度依赖和生成式方法。具体来说，BokehFlow在合成数据集上取得了显著的性能提升，并且在真实图像上也表现出良好的泛化能力。通过文本提示，用户可以精确地控制焦点区域和模糊程度，实现个性化的焦外成像效果。

## 🎯 应用场景

BokehFlow可应用于摄影后期处理、图像编辑、游戏开发等领域。它可以帮助用户在没有深度信息的情况下，轻松地为图像添加逼真的焦外成像效果，突出主体，增强视觉美感。该技术还可以用于虚拟现实和增强现实应用中，提供更具沉浸感的视觉体验。未来，BokehFlow有望成为一种通用的图像处理工具，为用户提供更便捷、更强大的图像编辑功能。

## 📄 摘要（原文）

> Bokeh rendering simulates the shallow depth-of-field effect in photography, enhancing visual aesthetics and guiding viewer attention to regions of interest. Although recent approaches perform well, rendering controllable bokeh without additional depth inputs remains a significant challenge. Existing classical and neural controllable methods rely on accurate depth maps, while generative approaches often struggle with limited controllability and efficiency. In this paper, we propose BokehFlow, a depth-free framework for controllable bokeh rendering based on flow matching. BokehFlow directly synthesizes photorealistic bokeh effects from all-in-focus images, eliminating the need for depth inputs. It employs a cross-attention mechanism to enable semantic control over both focus regions and blur intensity via text prompts. To support training and evaluation, we collect and synthesize four datasets. Extensive experiments demonstrate that BokehFlow achieves visually compelling bokeh effects and offers precise control, outperforming existing depth-dependent and generative methods in both rendering quality and efficiency.

