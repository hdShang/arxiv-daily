---
layout: default
title: "HunyuanVideo-Avatar: High-Fidelity Audio-Driven Human Animation for Multiple Characters"
---

# HunyuanVideo-Avatar: High-Fidelity Audio-Driven Human Animation for Multiple Characters

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20156" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20156v2</a>
  <a href="https://arxiv.org/pdf/2505.20156.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20156v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20156v2', 'HunyuanVideo-Avatar: High-Fidelity Audio-Driven Human Animation for Multiple Characters')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi Chen, Sen Liang, Zixiang Zhou, Ziyao Huang, Yifeng Ma, Junshu Tang, Qin Lin, Yuan Zhou, Qinglin Lu

**分类**: cs.CV

**发布日期**: 2025-05-26 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出HunyuanVideo-Avatar以解决多角色音频驱动人类动画问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频驱动动画` `多模态扩散变换器` `角色一致性` `情感对齐` `多角色动画`

## 📋 核心要点

1. 现有音频驱动人类动画方法在生成动态视频时难以保持角色一致性，且情感对齐精度不足。
2. HunyuanVideo-Avatar通过引入角色图像注入模块和音频情感模块，解决了角色一致性和情感控制的问题。
3. 该模型在多个基准数据集上表现优异，超越了现有方法，生成的动画在动态场景中更加真实和沉浸。

## 📝 摘要（中文）

近年来，音频驱动的人类动画取得了显著进展，但仍面临生成动态视频时保持角色一致性、实现角色与音频之间情感精确对齐以及支持多角色动画等挑战。为此，本文提出了HunyuanVideo-Avatar，这是一种基于多模态扩散变换器（MM-DiT）的模型，能够同时生成动态、可控情感和多角色对话视频。HunyuanVideo-Avatar引入了三个关键创新：角色图像注入模块、音频情感模块（AEM）和面部感知音频适配器（FAA），这些创新使得该模型在基准数据集和新提出的野外数据集上超越了现有的最先进方法，能够在动态、沉浸的场景中生成逼真的虚拟角色。

## 🔬 方法详解

**问题定义**：本文旨在解决音频驱动人类动画中的三个核心问题：生成动态视频时的角色一致性、角色与音频之间的情感对齐精度，以及多角色动画的实现。现有方法在这些方面存在显著不足。

**核心思路**：HunyuanVideo-Avatar通过多模态扩散变换器（MM-DiT）架构，结合角色图像注入和音频情感模块，提供了一种新的解决方案，以确保生成视频的动态性和情感一致性。

**技术框架**：该模型的整体架构包括三个主要模块：角色图像注入模块、音频情感模块（AEM）和面部感知音频适配器（FAA），这些模块协同工作以实现高保真度的多角色动画生成。

**关键创新**：HunyuanVideo-Avatar的主要创新在于角色图像注入模块的设计，替代了传统的基于加法的角色条件方案，消除了训练与推理之间的条件不匹配，从而确保了动态运动和角色一致性。

**关键设计**：在技术细节上，AEM模块提取情感线索并将其转移到目标生成视频中，而FAA模块则通过潜在级面具隔离音频驱动角色，允许在多角色场景中独立注入音频。

## 📊 实验亮点

在实验中，HunyuanVideo-Avatar在多个基准数据集上超越了现有的最先进方法，生成的动画在动态场景中表现出更高的真实感和情感一致性，具体性能提升幅度达到XX%（具体数据未知）。

## 🎯 应用场景

HunyuanVideo-Avatar在动画制作、游戏开发和虚拟现实等领域具有广泛的应用潜力。其高保真度的多角色动画生成能力，可以为用户提供更加沉浸和互动的体验，推动相关行业的发展。

## 📄 摘要（原文）

> Recent years have witnessed significant progress in audio-driven human animation. However, critical challenges remain in (i) generating highly dynamic videos while preserving character consistency, (ii) achieving precise emotion alignment between characters and audio, and (iii) enabling multi-character audio-driven animation. To address these challenges, we propose HunyuanVideo-Avatar, a multimodal diffusion transformer (MM-DiT)-based model capable of simultaneously generating dynamic, emotion-controllable, and multi-character dialogue videos. Concretely, HunyuanVideo-Avatar introduces three key innovations: (i) A character image injection module is designed to replace the conventional addition-based character conditioning scheme, eliminating the inherent condition mismatch between training and inference. This ensures the dynamic motion and strong character consistency; (ii) An Audio Emotion Module (AEM) is introduced to extract and transfer the emotional cues from an emotion reference image to the target generated video, enabling fine-grained and accurate emotion style control; (iii) A Face-Aware Audio Adapter (FAA) is proposed to isolate the audio-driven character with latent-level face mask, enabling independent audio injection via cross-attention for multi-character scenarios. These innovations empower HunyuanVideo-Avatar to surpass state-of-the-art methods on benchmark datasets and a newly proposed wild dataset, generating realistic avatars in dynamic, immersive scenarios.

