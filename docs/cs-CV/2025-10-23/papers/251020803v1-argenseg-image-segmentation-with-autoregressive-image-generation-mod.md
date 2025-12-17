---
layout: default
title: ARGenSeg: Image Segmentation with Autoregressive Image Generation Model
---

# ARGenSeg: Image Segmentation with Autoregressive Image Generation Model

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.20803" target="_blank" class="toolbar-btn">arXiv: 2510.20803v1</a>
    <a href="https://arxiv.org/pdf/2510.20803.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.20803v1" 
            onclick="toggleFavorite(this, '2510.20803v1', 'ARGenSeg: Image Segmentation with Autoregressive Image Generation Model')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Xiaolong Wang, Lixiang Ru, Ziyuan Huang, Kaixiang Ji, Dandan Zheng, Jingdong Chen, Jun Zhou

**分类**: cs.CV

**发布日期**: 2025-10-23

**备注**: Accepted to NeurIPS 2025, 18 pages

---

## 💡 一句话要点

**ARGenSeg：提出基于自回归图像生成模型的图像分割方法**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像分割` `自回归生成模型` `多模态大型语言模型` `VQ-VAE` `像素级理解`

## 📋 核心要点

1. 现有方法依赖离散表示或语义提示，限制了多模态大型语言模型（MLLM）捕获细粒度视觉细节的能力。
2. ARGenSeg利用MLLM生成视觉tokens，并通过VQ-VAE将其转换为图像，实现像素级的分割理解。
3. 通过下一尺度预测策略并行生成视觉tokens，显著降低了推理延迟，并在多个数据集上超越了现有方法。

## 📝 摘要（中文）

本文提出了一种新颖的基于自回归生成模型的图像分割范式（ARGenSeg），在统一框架内实现多模态理解和像素级感知。现有将图像分割集成到多模态大型语言模型（MLLM）中的工作通常采用边界点表示或专用分割头。这些方法依赖于离散表示或输入到特定任务解码器的语义提示，限制了MLLM捕获细粒度视觉细节的能力。为了解决这些挑战，我们引入了一种基于图像生成的MLLM分割框架，该框架自然地为目标对象生成密集掩码。我们利用MLLM输出视觉tokens，并使用通用VQ-VAE将其解token化为图像，使分割完全依赖于MLLM的像素级理解。为了减少推理延迟，我们采用下一尺度预测策略来并行生成所需的视觉tokens。大量实验表明，我们的方法在多个分割数据集上超越了先前的最先进方法，推理速度显著提高，同时保持了强大的理解能力。

## 🔬 方法详解

**问题定义**：现有将图像分割集成到多模态大型语言模型（MLLM）的方法，如基于边界点表示或专用分割头的方法，依赖于离散表示或语义提示，无法充分利用MLLM的像素级理解能力，限制了模型捕获细粒度视觉细节的能力。这些方法在分割精度和效率上存在瓶颈。

**核心思路**：ARGenSeg的核心思路是将图像分割问题转化为图像生成问题。通过让MLLM生成视觉tokens，然后使用VQ-VAE将这些tokens解码为图像，从而直接生成密集的分割掩码。这种方法充分利用了MLLM的生成能力和像素级理解能力，避免了对离散表示的依赖。

**技术框架**：ARGenSeg的整体框架包括以下几个主要模块：1) 多模态大型语言模型（MLLM）：负责接收输入图像和文本提示，并生成视觉tokens。2) VQ-VAE：用于将MLLM生成的视觉tokens解码为图像，从而得到分割掩码。3) 下一尺度预测策略：用于并行生成视觉tokens，以减少推理延迟。整个流程是，输入图像和文本提示到MLLM，MLLM输出视觉tokens，VQ-VAE解码tokens生成分割图像。

**关键创新**：ARGenSeg的关键创新在于将图像分割问题转化为图像生成问题，并利用MLLM的生成能力直接生成密集的分割掩码。与现有方法相比，ARGenSeg避免了对离散表示的依赖，能够更好地利用MLLM的像素级理解能力。此外，下一尺度预测策略的引入显著降低了推理延迟。

**关键设计**：ARGenSeg的关键设计包括：1) 使用通用的VQ-VAE进行视觉tokens的解码，保证了模型的通用性。2) 采用下一尺度预测策略，通过并行生成视觉tokens来减少推理延迟。3) 损失函数的设计需要考虑分割精度和生成质量，可能包括交叉熵损失和生成对抗损失等。具体的网络结构细节和参数设置在论文中应该有更详细的描述。

## 📊 实验亮点

ARGenSeg在多个分割数据集上取得了显著的性能提升，超越了现有的最先进方法。同时，通过下一尺度预测策略，推理速度得到了显著提高。具体的性能数据和对比基线需要在论文中查找，例如在某个数据集上mIOU提升了X%，推理速度提升了Y倍等。

## 🎯 应用场景

ARGenSeg在多个领域具有广泛的应用前景，包括自动驾驶、医学图像分析、遥感图像处理等。该方法可以用于目标检测、语义分割、实例分割等任务，提高图像理解和分析的精度和效率。未来，ARGenSeg可以进一步扩展到视频分割、三维重建等领域，为人工智能应用提供更强大的支持。

## 📄 摘要（原文）

> We propose a novel AutoRegressive Generation-based paradigm for image Segmentation (ARGenSeg), achieving multimodal understanding and pixel-level perception within a unified framework. Prior works integrating image segmentation into multimodal large language models (MLLMs) typically employ either boundary points representation or dedicated segmentation heads. These methods rely on discrete representations or semantic prompts fed into task-specific decoders, which limits the ability of the MLLM to capture fine-grained visual details. To address these challenges, we introduce a segmentation framework for MLLM based on image generation, which naturally produces dense masks for target objects. We leverage MLLM to output visual tokens and detokenize them into images using an universal VQ-VAE, making the segmentation fully dependent on the pixel-level understanding of the MLLM. To reduce inference latency, we employ a next-scale-prediction strategy to generate required visual tokens in parallel. Extensive experiments demonstrate that our method surpasses prior state-of-the-art approaches on multiple segmentation datasets with a remarkable boost in inference speed, while maintaining strong understanding capabilities.

