---
layout: default
title: OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation
---

# OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02015" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02015v2</a>
  <a href="https://arxiv.org/pdf/2506.02015.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02015v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02015v2', 'OSPO: Object-centric Self-improving Preference Optimization for Text-to-Image Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yoonjin Oh, Yongjin Kim, Hyomin Kim, Donghwan Chi, Sungwoong Kim

**分类**: cs.CV

**发布日期**: 2025-05-28 (更新: 2025-09-19)

---

## 💡 一句话要点

**提出OSPO框架以解决文本到图像生成中的对象对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `文本到图像生成` `对象中心优化` `自我改进机制` `多模态学习` `图像生成` `深度学习`

## 📋 核心要点

1. 现有的自我改进方法未能有效解决文本到图像生成中的对象幻觉问题，尤其是在细粒度视觉细节方面。
2. 本文提出了对象中心自我改进偏好优化（OSPO）框架，通过构建对象级硬负样本数据来提升对象级别的文本-图像对齐。
3. 实验结果表明，OSPO在组合图像生成基准上显著提高了细粒度对齐，超越了以往的自我改进方法和基于扩散的图像生成模型。

## 📝 摘要（中文）

近年来，多模态大语言模型（MLLMs）的进展使得模型能够以统一的方式理解和生成多模态数据。然而，在文本到图像生成中，实现输入提示与生成图像之间的细粒度对齐仍然是一个主要挑战。为此，近期研究引入了基于自生成数据和自反馈的自我改进机制，以高效缓解这一挑战，而无需依赖外部大规模数据或模型。然而，现有的自我改进方法未能关注生成训练数据或提供反馈时的细粒度视觉细节，尤其是在对象层面，因此在解决对象幻觉问题上仍然存在困难。为了解决这一问题，本文提出了对象中心自我改进偏好优化（OSPO）框架，旨在增强对象级文本-图像对齐。OSPO明确构建和利用对象级硬负样本数据，并通过对象中心优化来提高对象特定的保真度。

## 🔬 方法详解

**问题定义**：本文旨在解决文本到图像生成中的对象幻觉问题，现有方法在生成训练数据和反馈时未能关注细粒度的视觉细节，导致对齐效果不佳。

**核心思路**：OSPO框架通过构建和利用对象级硬负样本数据，结合对象中心优化，旨在提升对象特定的保真度，从而改善文本与图像之间的对齐。

**技术框架**：OSPO框架包括四个主要模块：初始提示生成、硬偏好对生成、过滤与选择、以及基于条件偏好损失的对象中心偏好优化。

**关键创新**：OSPO的创新之处在于其专注于对象级别的细节，通过硬负样本的构建和对象中心优化，显著提升了生成图像的质量和对齐精度。

**关键设计**：在设计中，使用了条件偏好损失作为优化目标，确保生成的图像在对象层面上具有更高的保真度，同时通过精细的过滤与选择机制来提升训练数据的质量。

## 📊 实验亮点

实验结果显示，OSPO在组合图像生成基准上显著提高了细粒度对齐，超越了以往的自我改进方法，性能提升幅度达到XX%（具体数据待补充），并在与基于扩散的图像生成模型的对比中表现出更优的效果。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、图像生成、虚拟现实和增强现实等。通过提升文本与图像之间的对齐精度，OSPO框架能够为多模态内容生成提供更高质量的解决方案，推动相关领域的发展与应用。未来，OSPO可能在艺术创作、游戏设计和教育等多个领域产生深远影响。

## 📄 摘要（原文）

> Recent advances in Multimodal Large Language Models (MLLMs) have enabled models to perform both understanding and generation of multimodal data in a unified manner. However, achieving a fine-grained alignment between input prompts and generated images remains a major challenge especially in text-to-image generation. Therefore, recent works have introduced self-improving mechanisms based on self-generated data and self-feedback to efficiently mitigate this challenge without relying on external large-scale data or models. However, existing self-improving approaches have not focused on fine-grained visual details especially at the object level in generating training data or providing a feedback, and thus they still struggle to resolve the object hallucination problem in text-to-image generation. To tackle this problem, we propose an Object-centric Self-improving Preference Optimization (OSPO), a self-improving framework for enhancing object-level text-image alignment. OSPO is designed to explicitly address the need for constructing and leveraging object-level hard negative data and an object-centric optimization in improving object-specific fidelity. In specific, OSPO consists of: (1) Initial Prompt Generation (2) Hard Preference Pair Generation (3) Filtering and Selection (4) Object-centric Preference Optimization with Conditional Preference Loss. Extensive experiments on compositional image generation benchmarks demonstrate that OSPO significantly improves fine-grained alignment in text-to-image generation, surpassing not only prior self-improving methods but also diffusion-based specialized image generation models.

