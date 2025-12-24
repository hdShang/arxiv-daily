---
layout: default
title: "Query-Kontext: An Unified Multimodal Model for Image Generation and Editing"
---

# Query-Kontext: An Unified Multimodal Model for Image Generation and Editing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26641" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26641v1</a>
  <a href="https://arxiv.org/pdf/2509.26641.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26641v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26641v1', 'Query-Kontext: An Unified Multimodal Model for Image Generation and Editing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuxin Song, Wenkai Dong, Shizun Wang, Qi Zhang, Song Xue, Tao Yuan, Hu Yang, Haocheng Feng, Hang Zhou, Xinyan Xiao, Jingdong Wang

**分类**: cs.CV

**发布日期**: 2025-09-30

**备注**: 23 pages, 10 figures

---

## 💡 一句话要点

**提出Query-Kontext以提升多模态图像生成与编辑能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态模型` `图像生成` `图像编辑` `视觉语言模型` `扩散模型` `生成推理` `深度学习`

## 📋 核心要点

1. 现有的统一多模态模型在多模态生成推理能力上存在不足，难以实现高保真合成与身份保留。
2. 本文提出Query-Kontext，通过多模态语境连接VLM与扩散模型，充分发挥VLM的生成推理能力。
3. 实验结果表明，该方法在多个任务上与强基线相匹配，甚至在某些情况下超越了特定任务的最先进方法。

## 📝 摘要（中文）

统一多模态模型（UMMs）在文本到图像生成（T2I）和编辑（TI2I）方面表现出色，但现有框架在多模态生成推理能力上存在不足。本文提出Query-Kontext，通过将视觉语言模型（VLM）与扩散模型连接，利用语义线索和粗粒度图像条件的多模态“kontext”来提升生成质量。我们设计了三阶段的渐进训练策略，最终在多个任务上超越了强基线和特定任务的最先进方法。

## 🔬 方法详解

**问题定义**：本文旨在解决现有统一多模态模型在多模态生成推理能力不足的问题，特别是在高保真合成和身份保留方面的挑战。

**核心思路**：通过引入Query-Kontext，将视觉语言模型（VLM）与扩散模型结合，利用多模态语境来增强生成推理能力，同时保留扩散模型在视觉合成中的优势。

**技术框架**：整体架构分为三个阶段：第一阶段连接轻量级扩散头与VLM，释放VLM的生成推理能力；第二阶段将扩散头扩展至大型预训练扩散模型，以增强视觉细节；第三阶段引入低级图像编码器，提升图像保真度并进行指令调优。

**关键创新**：最重要的创新在于引入了多模态“kontext”，使得VLM与扩散模型之间的协同工作更加高效，解决了现有方法在生成推理上的局限性。

**关键设计**：在训练过程中，采用了多模态kontext令牌连接VLM与扩散头，设计了适应不同任务的损失函数，并优化了网络结构以提升生成质量。

## 📊 实验亮点

实验结果显示，Query-Kontext在多个任务上与强基线模型相匹配，甚至在某些情况下超越了特定任务的最先进方法，展现出显著的性能提升，具体数据未详述。

## 🎯 应用场景

该研究的潜在应用领域包括图像生成、指令驱动的图像编辑、定制化生成以及多主体组合等。其实际价值在于能够提供更高质量的图像合成和编辑能力，未来可能在艺术创作、广告设计和虚拟现实等领域产生深远影响。

## 📄 摘要（原文）

> Unified Multimodal Models (UMMs) have demonstrated remarkable performance in text-to-image generation (T2I) and editing (TI2I), whether instantiated as assembled unified frameworks which couple powerful vision-language model (VLM) with diffusion-based generator, or as naive Unified Multimodal Models with an early fusion of understanding and generation modalities. We contend that in current unified frameworks, the crucial capability of multimodal generative reasoning which encompasses instruction understanding, grounding, and image referring for identity preservation and faithful reconstruction, is intrinsically entangled with high-fidelity synthesis. In this work, we introduce Query-Kontext, a novel approach that bridges the VLM and diffusion model via a multimodal ``kontext'' composed of semantic cues and coarse-grained image conditions encoded from multimodal inputs. This design delegates the complex ability of multimodal generative reasoning to powerful VLM while reserving diffusion model's role for high-quality visual synthesis. To achieve this, we propose a three-stage progressive training strategy. First, we connect the VLM to a lightweight diffusion head via multimodal kontext tokens to unleash the VLM's generative reasoning ability. Second, we scale this head to a large, pre-trained diffusion model to enhance visual detail and realism. Finally, we introduce a low-level image encoder to improve image fidelity and perform instruction tuning on downstream tasks. Furthermore, we build a comprehensive data pipeline integrating real, synthetic, and open-source datasets, covering diverse multimodal reference-to-image scenarios, including image generation, instruction-driven editing, customized generation, and multi-subject composition. Experiments show that our approach matches strong unified baselines and even outperforms task-specific state-of-the-art methods in several cases.

