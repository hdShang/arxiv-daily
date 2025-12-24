---
layout: default
title: "TalkingMachines: Real-Time Audio-Driven FaceTime-Style Video via Autoregressive Diffusion Models"
---

# TalkingMachines: Real-Time Audio-Driven FaceTime-Style Video via Autoregressive Diffusion Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03099" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03099v1</a>
  <a href="https://arxiv.org/pdf/2506.03099.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03099v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03099v1', 'TalkingMachines: Real-Time Audio-Driven FaceTime-Style Video via Autoregressive Diffusion Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chetwin Low, Weimin Wang

**分类**: cs.SD, cs.AI, cs.GR

**发布日期**: 2025-06-03

**🔗 代码/项目**: [PROJECT_PAGE](https://aaxwaz.github.io/TalkingMachines/)

---

## 💡 一句话要点

**提出TalkingMachines以实现实时音频驱动的视频生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频驱动生成` `实时视频生成` `知识蒸馏` `多模态融合` `角色动画`

## 📋 核心要点

1. 现有的视频生成方法在实时性和音频驱动的角色动画方面存在显著不足，难以实现自然的对话体验。
2. 论文提出了一种将音频大型语言模型与视频生成模型结合的方法，利用知识蒸馏技术提升生成效率。
3. 实验结果表明，TalkingMachines在视频生成的延迟和吞吐量上有显著提升，能够实现高效的实时视频流传输。

## 📝 摘要（中文）

本文提出了TalkingMachines，一个高效框架，将预训练的视频生成模型转化为实时音频驱动的角色动画生成器。通过将音频大型语言模型与视频生成基础模型相结合，TalkingMachines实现了自然的对话体验。主要贡献包括：将预训练的最先进图像到视频模型DiT适配为具有180亿参数的音频驱动头像生成模型；通过从双向教师模型到稀疏因果自回归学生模型的不对称知识蒸馏，实现无限视频流传输而不发生错误累积；设计了高吞吐量、低延迟的推理管道，包含多个关键工程优化。

## 🔬 方法详解

**问题定义**：本文旨在解决现有音频驱动视频生成方法在实时性和生成质量上的不足，尤其是在自然对话场景中的应用挑战。

**核心思路**：通过将预训练的图像到视频生成模型DiT进行适配，并结合音频大型语言模型，设计出高效的实时生成框架。采用不对称知识蒸馏技术，避免了错误累积问题。

**技术框架**：整体架构包括音频输入处理模块、视频生成模型和推理管道。音频输入通过大型语言模型处理后，驱动视频生成模型生成相应的角色动画。

**关键创新**：最重要的创新在于将知识蒸馏应用于音频驱动视频生成，利用双向教师模型与稀疏因果自回归学生模型的结合，实现了高效的实时生成。

**关键设计**：在设计中，采用了分离的DiT和VAE解码器，优化了设备间的通信与计算重叠，消除了冗余的重计算，以最大化帧生成的吞吐量。具体参数设置和损失函数的选择也经过精心调整，以确保生成质量。

## 📊 实验亮点

实验结果显示，TalkingMachines在视频生成的延迟上显著降低，吞吐量提升至每秒生成多个高质量帧，且在与现有基线模型的对比中，生成质量和实时性均有明显改善，展示了其在实际应用中的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、在线教育、游戏开发及社交媒体等，能够为用户提供更为自然和沉浸的交互体验。未来，随着技术的进一步发展，可能会在远程沟通和在线娱乐等领域产生深远影响。

## 📄 摘要（原文）

> In this paper, we present TalkingMachines -- an efficient framework that transforms pretrained video generation models into real-time, audio-driven character animators. TalkingMachines enables natural conversational experiences by integrating an audio large language model (LLM) with our video generation foundation model. Our primary contributions include: (1) We adapt a pretrained SOTA image-to-video DiT into an audio-driven avatar generation model of 18 billion parameters; (2) We enable infinite video streaming without error accumulation through asymmetric knowledge distillation from a bidirectional teacher model into a sparse causal, autoregressive student model; (3) We design a high-throughput, low-latency inference pipeline incorporating several key engineering optimizations such as: (a) disaggregation of the DiT and VAE decoder across separate devices, (b) efficient overlap of inter-device communication and computation using CUDA streams, (c) elimination of redundant recomputations to maximize frame-generation throughput. Please see demo videos here - https://aaxwaz.github.io/TalkingMachines/

