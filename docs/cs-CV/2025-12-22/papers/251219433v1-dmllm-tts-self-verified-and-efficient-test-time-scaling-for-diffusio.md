---
layout: default
title: "dMLLM-TTS: Self-Verified and Efficient Test-Time Scaling for Diffusion Multi-Modal Large Language Models"
---

# dMLLM-TTS: Self-Verified and Efficient Test-Time Scaling for Diffusion Multi-Modal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19433" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19433v1</a>
  <a href="https://arxiv.org/pdf/2512.19433.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19433v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19433v1', 'dMLLM-TTS: Self-Verified and Efficient Test-Time Scaling for Diffusion Multi-Modal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Xin, Siqi Luo, Qi Qin, Haoxing Chen, Kaiwen Zhu, Zhiwei Zhang, Yangfan He, Rongchao Zhang, Jinbin Bai, Shuo Cao, Bin Fu, Junjun He, Yihao Liu, Yuewen Cao, Xiaohong Liu

**分类**: cs.CV

**发布日期**: 2025-12-22

**备注**: Project page: https://github.com/Alpha-VLLM/Lumina-DiMOO

**🔗 代码/项目**: [GITHUB](https://github.com/Alpha-VLLM/Lumina-DiMOO)

---

## 💡 一句话要点

**提出dMLLM-TTS，通过自验证和高效测试时缩放提升扩散多模态大语言模型的生成质量和效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `扩散模型` `多模态大语言模型` `测试时缩放` `自验证` `层次搜索` `图像生成` `文本图像对齐`

## 📋 核心要点

1. 现有的扩散多模态大语言模型测试时缩放方法计算成本高昂，依赖外部验证器，限制了生成质量和效率。
2. dMLLM-TTS通过轨迹探索和迭代细化两个维度进行缩放，并引入高效的层次搜索和自验证反馈机制。
3. 实验表明，dMLLM-TTS在GenEval基准测试中，显著提升了生成质量，并实现了高达6倍的效率提升。

## 📝 摘要（中文）

扩散多模态大语言模型(dMLLMs)作为一种统一图像生成和理解的新型架构，近年来备受关注。然而，开发有效且高效的测试时缩放(TTS)方法以充分发挥其生成潜力仍然是一个未被充分探索的挑战。为了解决这个问题，我们提出了dMLLM-TTS，这是一个在两个互补的缩放轴上运行的新框架：(1) 轨迹探索缩放，以增强生成假设的多样性；(2) 迭代细化缩放，以实现稳定的生成。传统的TTS方法通常在这两个维度上执行线性搜索，导致O(NT)的巨大计算成本，并且需要外部验证器来进行最佳N选一。为了克服这些限制，我们提出了两项创新。首先，我们设计了一种高效的层次搜索算法，其复杂度为O(N+T)，能够自适应地扩展和修剪采样轨迹。其次，我们引入了一种自验证反馈机制，该机制利用dMLLMs固有的图像理解能力来评估文本-图像对齐，从而消除了对外部验证器的需求。在GenEval基准上对三个具有代表性的dMLLMs（例如，Lumina-DiMOO、MMaDA、Muddit）进行的大量实验表明，我们的框架在显著提高生成质量的同时，实现了比线性搜索高出6倍的效率。

## 🔬 方法详解

**问题定义**：论文旨在解决扩散多模态大语言模型（dMLLMs）在测试时缩放（TTS）过程中效率低和需要外部验证器的问题。现有的TTS方法通常采用线性搜索，计算复杂度高，难以在生成质量和效率之间取得平衡。此外，依赖外部验证器进行最佳结果选择增加了系统的复杂性和成本。

**核心思路**：论文的核心思路是通过设计一种高效的层次搜索算法和自验证反馈机制来优化TTS过程。层次搜索算法能够自适应地探索和修剪采样轨迹，降低计算复杂度。自验证反馈机制利用dMLLMs自身的图像理解能力来评估文本-图像对齐程度，从而避免使用外部验证器。

**技术框架**：dMLLM-TTS框架包含两个主要的缩放轴：轨迹探索缩放和迭代细化缩放。轨迹探索缩放旨在增加生成假设的多样性，而迭代细化缩放则用于稳定生成过程。框架的核心是层次搜索算法和自验证反馈机制。层次搜索算法在轨迹探索和迭代细化两个维度上进行自适应搜索，并根据自验证反馈机制的评估结果进行剪枝。最终，选择最佳的生成结果。

**关键创新**：论文的关键创新在于：1) 提出了高效的层次搜索算法，将计算复杂度从O(NT)降低到O(N+T)；2) 引入了自验证反馈机制，利用dMLLMs自身的图像理解能力进行文本-图像对齐评估，消除了对外部验证器的依赖。

**关键设计**：层次搜索算法采用分层结构，每一层代表不同的缩放级别。算法首先在较低的缩放级别上进行快速搜索，然后根据自验证反馈机制的评估结果，选择有希望的轨迹进行进一步的探索。自验证反馈机制通过计算生成图像和输入文本之间的相似度来评估文本-图像对齐程度。具体的相似度计算方法可能涉及CLIP等预训练模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19433v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19433v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19433v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，dMLLM-TTS在GenEval基准测试中，相较于传统的线性搜索方法，在生成质量上取得了显著提升，同时实现了高达6倍的效率提升。该方法在Lumina-DiMOO、MMaDA和Muddit等多个代表性dMLLMs上均取得了良好的效果，验证了其通用性和有效性。

## 🎯 应用场景

dMLLM-TTS可应用于各种需要高质量、高效率图像生成的场景，例如：创意设计、内容生成、虚拟现实、游戏开发等。该研究有助于提升多模态大语言模型在实际应用中的性能和用户体验，并降低计算成本，促进相关技术的普及。

## 📄 摘要（原文）

> Diffusion Multi-modal Large Language Models (dMLLMs) have recently emerged as a novel architecture unifying image generation and understanding. However, developing effective and efficient Test-Time Scaling (TTS) methods to unlock their full generative potential remains an underexplored challenge. To address this, we propose dMLLM-TTS, a novel framework operating on two complementary scaling axes: (1) trajectory exploration scaling to enhance the diversity of generated hypotheses, and (2) iterative refinement scaling for stable generation. Conventional TTS approaches typically perform linear search across these two dimensions, incurring substantial computational costs of O(NT) and requiring an external verifier for best-of-N selection. To overcome these limitations, we propose two innovations. First, we design an efficient hierarchical search algorithm with O(N+T) complexity that adaptively expands and prunes sampling trajectories. Second, we introduce a self-verified feedback mechanism that leverages the dMLLMs' intrinsic image understanding capabilities to assess text-image alignment, eliminating the need for external verifier. Extensive experiments on the GenEval benchmark across three representative dMLLMs (e.g., Lumina-DiMOO, MMaDA, Muddit) show that our framework substantially improves generation quality while achieving up to 6x greater efficiency than linear search. Project page: https://github.com/Alpha-VLLM/Lumina-DiMOO.

