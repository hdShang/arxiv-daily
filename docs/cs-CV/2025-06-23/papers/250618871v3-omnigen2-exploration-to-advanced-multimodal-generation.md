---
layout: default
title: "OmniGen2: Exploration to Advanced Multimodal Generation"
---

# OmniGen2: Exploration to Advanced Multimodal Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18871" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18871v3</a>
  <a href="https://arxiv.org/pdf/2506.18871.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18871v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18871v3', 'OmniGen2: Exploration to Advanced Multimodal Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenyuan Wu, Pengfei Zheng, Ruiran Yan, Shitao Xiao, Xin Luo, Yueze Wang, Wanli Li, Xiyan Jiang, Yexin Liu, Junjie Zhou, Ze Liu, Ziyi Xia, Chaofan Li, Haoge Deng, Jiahao Wang, Kun Luo, Bo Zhang, Defu Lian, Xinlong Wang, Zhongyuan Wang, Tiejun Huang, Zheng Liu

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-23 (更新: 2025-09-27)

**🔗 代码/项目**: [GITHUB](https://github.com/VectorSpaceLab/OmniGen2) | [PROJECT_PAGE](https://vectorspacelab.github.io/OmniGen2)

---

## 💡 一句话要点

**提出OmniGen2以解决多模态生成任务的统一问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态生成` `文本到图像` `图像编辑` `反射机制` `开源模型` `一致性评估` `数据构建管道`

## 📋 核心要点

1. 现有的多模态生成模型在处理不同模态任务时存在统一性不足和适应性差的问题。
2. OmniGen2通过设计独立的文本和图像解码路径，利用不共享的参数和解耦的图像标记器，提升了多模态生成的灵活性和效率。
3. 在多个基准测试中，OmniGen2在文本到图像和图像编辑任务上表现出色，尤其在一致性方面达到了开源模型的最先进水平。

## 📝 摘要（中文）

在本研究中，我们介绍了OmniGen2，一个多功能且开源的生成模型，旨在为文本到图像、图像编辑和上下文生成等多样化生成任务提供统一解决方案。与OmniGen v1不同，OmniGen2为文本和图像模态设计了两个独立的解码路径，利用不共享的参数和解耦的图像标记器。这一设计使OmniGen2能够在不重新适配VAE输入的情况下，基于现有的多模态理解模型进行构建，从而保留原有的文本生成能力。我们还开发了全面的数据构建管道，涵盖图像编辑和上下文生成数据，并引入了针对图像生成任务的反射机制，基于OmniGen2策划了专门的反射数据集。尽管参数规模相对较小，OmniGen2在多个任务基准上取得了竞争力的结果，包括文本到图像和图像编辑。为了进一步评估上下文生成（即主题驱动任务），我们引入了一个新的基准OmniContext。OmniGen2在一致性方面在开源模型中达到了最先进的性能。我们将发布模型、训练代码、数据集和数据构建管道，以支持该领域未来的研究。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有多模态生成模型在处理不同模态任务时的统一性不足和适应性差的问题。现有方法往往需要重新适配输入，导致效率低下和性能损失。

**核心思路**：OmniGen2的核心解决思路是通过设计两个独立的解码路径来处理文本和图像模态，利用不共享的参数和解耦的图像标记器，从而提升生成任务的灵活性和效率。

**技术框架**：OmniGen2的整体架构包括两个主要模块：文本解码器和图像解码器。文本解码器负责处理文本输入，而图像解码器则处理图像生成和编辑任务。此外，论文还开发了全面的数据构建管道，以支持模型的训练。

**关键创新**：OmniGen2的最重要技术创新在于其独立的解码路径设计，这一设计与现有方法的共享参数机制形成了鲜明对比，从而提高了模型在多模态生成任务中的表现。

**关键设计**：在模型设计中，OmniGen2采用了不共享的参数设置，使用了专门的图像标记器，并引入了针对图像生成任务的反射机制。此外，论文还策划了专门的反射数据集，以增强模型的训练效果。

## 📊 实验亮点

在多个任务基准测试中，OmniGen2在文本到图像和图像编辑任务上表现出色，尤其在一致性方面达到了开源模型中的最先进水平。具体而言，OmniGen2在OmniContext基准上取得了显著的性能提升，展示了其在主题驱动任务中的强大能力。

## 🎯 应用场景

OmniGen2的潜在应用领域包括艺术创作、广告设计、虚拟现实和增强现实等多个领域。其统一的多模态生成能力使得用户能够在不同的生成任务中实现更高的效率和更好的效果，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> In this work, we introduce OmniGen2, a versatile and open-source generative model designed to provide a unified solution for diverse generation tasks, including text-to-image, image editing, and in-context generation. Unlike OmniGen v1, OmniGen2 features two distinct decoding pathways for text and image modalities, utilizing unshared parameters and a decoupled image tokenizer. This design enables OmniGen2 to build upon existing multimodal understanding models without the need to re-adapt VAE inputs, thereby preserving the original text generation capabilities. To facilitate the training of OmniGen2, we developed comprehensive data construction pipelines, encompassing image editing and in-context generation data. Additionally, we introduce a reflection mechanism tailored for image generation tasks and curate a dedicated reflection dataset based on OmniGen2. Despite its relatively modest parameter size, OmniGen2 achieves competitive results on multiple task benchmarks, including text-to-image and image editing. To further evaluate in-context generation, also referred to as subject-driven tasks, we introduce a new benchmark named OmniContext. OmniGen2 achieves state-of-the-art performance among open-source models in terms of consistency. We will release our models, training code, datasets, and data construction pipeline to support future research in this field. Project Page: https://vectorspacelab.github.io/OmniGen2; GitHub Link: https://github.com/VectorSpaceLab/OmniGen2

