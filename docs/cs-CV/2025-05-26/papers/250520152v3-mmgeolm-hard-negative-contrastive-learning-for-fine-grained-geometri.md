---
layout: default
title: "MMGeoLM: Hard Negative Contrastive Learning for Fine-Grained Geometric Understanding in Large Multimodal Models"
---

# MMGeoLM: Hard Negative Contrastive Learning for Fine-Grained Geometric Understanding in Large Multimodal Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20152" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20152v3</a>
  <a href="https://arxiv.org/pdf/2505.20152.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20152v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20152v3', 'MMGeoLM: Hard Negative Contrastive Learning for Fine-Grained Geometric Understanding in Large Multimodal Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kai Sun, Yushi Bai, Zhen Yang, Jiajie Zhang, Ji Qi, Lei Hou, Juanzi Li

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-05-26 (更新: 2025-10-01)

**🔗 代码/项目**: [GITHUB](https://github.com/THU-KEG/MMGeoLM)

---

## 💡 一句话要点

**提出MMGeoLM以解决大规模多模态模型的几何理解问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `几何理解` `对比学习` `硬负样本` `视觉编码器` `细粒度差异` `模型优化`

## 📋 核心要点

1. 现有的多模态模型在几何理解任务中表现不足，尤其是在捕捉细粒度视觉差异方面，限制了其应用效果。
2. 本文提出了一种硬负样本对比学习框架，通过生成和选择负样本来增强视觉编码器的训练效果，从而提升几何理解能力。
3. 实验结果显示，MMGeoLM在多个几何推理基准上表现优异，超越了其他开源模型，展示了其在大规模模型中的潜力。

## 📝 摘要（中文）

大规模多模态模型（LMMs）通常基于视觉变换器（如CLIP），但使用简单的随机批内负样本限制了其捕捉细粒度视觉差异的能力，尤其是在几何场景中。为了解决这一挑战，本文提出了一种新颖的硬负样本对比学习框架，结合了基于图像的对比学习和基于文本的对比学习。通过生成扰动图示生成代码创建的硬负样本以及基于修改几何描述和检索相似性选择的负样本，训练了视觉编码器CLIP，并进一步训练了用于几何问题求解的LMM。实验表明，训练出的模型MMGeoLM在三个几何推理基准上显著优于其他开源模型，甚至在7B参数规模下也能与强大的闭源模型如GPT-4o相媲美。

## 🔬 方法详解

**问题定义**：本文旨在解决大规模多模态模型在几何理解任务中对细粒度视觉差异捕捉能力不足的问题。现有方法使用简单的随机批内负样本，导致模型在复杂几何场景中的表现不佳。

**核心思路**：提出了一种硬负样本对比学习框架，结合图像生成的硬负样本和基于文本的规则负样本，以增强视觉编码器的训练效果，从而提升几何理解能力。

**技术框架**：整体架构包括两个主要阶段：首先，使用生成扰动的图示生成代码创建硬负样本进行图像对比学习；其次，基于修改的几何描述和检索相似性选择负样本进行文本对比学习。

**关键创新**：最重要的技术创新在于引入了生成和选择的硬负样本，显著提升了模型在细粒度几何理解任务中的表现，与传统方法相比，能够更有效地捕捉视觉差异。

**关键设计**：在训练过程中，采用了特定的损失函数来平衡正负样本的影响，同时对网络结构进行了优化，以适应多模态输入的特性。

## 📊 实验亮点

实验结果表明，MMGeoLM在三个几何推理基准上显著优于其他开源模型，尤其是在7B参数规模下，其性能接近于强大的闭源模型GPT-4o，展示了硬负样本对比学习的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化设计和机器人视觉等，能够为几何问题求解提供更为精确的支持。未来，随着模型的进一步优化，MMGeoLM有望在更广泛的多模态任务中发挥重要作用。

## 📄 摘要（原文）

> Large Multimodal Models (LMMs) typically build on ViTs (e.g., CLIP), yet their training with simple random in-batch negatives limits the ability to capture fine-grained visual differences, particularly in geometric scenarios. To address this challenge, we propose a novel hard negative contrastive learning framework for the vision encoder, which combines image-based contrastive learning using generation-based hard negatives created by perturbing diagram generation code, and text-based contrastive learning using rule-based negatives derived from modified geometric descriptions and retrieval-based negatives selected based on caption similarity. We train a vision encoder (CLIP) using our hard negative training method, namely MMCLIP (Multimodal Math CLIP), and subsequently train an LMM for geometric problem-solving. Experiments show that our trained model, MMGeoLM, significantly outperforms other open-source models on three geometric reasoning benchmarks. Even with a size of 7B, it can rival powerful closed-source models like GPT-4o. We further conduct ablation studies to analyze three key factors: hard negative types, the efficiency of image-based negatives, and training configurations. These analyses yield important insights into optimizing the training pipeline of vision encoder for fine-grained geometric reasoning tasks. https://github.com/THU-KEG/MMGeoLM.

