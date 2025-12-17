---
layout: default
title: UniMo: Unifying 2D Video and 3D Human Motion with an Autoregressive Framework
---

# UniMo: Unifying 2D Video and 3D Human Motion with an Autoregressive Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.03918" class="toolbar-btn" target="_blank">📄 arXiv: 2512.03918v1</a>
  <a href="https://arxiv.org/pdf/2512.03918.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.03918v1" onclick="toggleFavorite(this, '2512.03918v1', 'UniMo: Unifying 2D Video and 3D Human Motion with an Autoregressive Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Youxin Pang, Yong Zhang, Ruizhi Shao, Xiang Deng, Feng Gao, Xu Xiaoming, Xiaoming Wei, Yebin Liu

**分类**: cs.CV

**发布日期**: 2025-12-03

**备注**: https://carlyx.github.io/UniMo/

---

## 💡 一句话要点

**UniMo：提出一个自回归框架，统一建模2D视频和3D人体运动，实现同步生成与理解。**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `2D视频生成` `3D人体运动` `自回归模型` `多模态融合` `统一建模` `运动捕捉` `VQ-VAE`

## 📋 核心要点

1. 现有方法难以同时生成和理解2D视频和3D人体运动，因为它们在结构和分布上存在显著差异。
2. UniMo将2D视频和3D人体运动建模为统一的tokens序列，利用自回归模型实现同步生成和理解。
3. 实验表明，UniMo能够同时生成对应的视频和运动，并执行精确的运动捕捉，验证了统一建模的有效性。

## 📝 摘要（中文）

我们提出了UniMo，一个创新的自回归模型，用于在统一框架内联合建模2D人体视频和3D人体运动，首次实现了这两种模态的同步生成和理解。目前的方法主要集中在以一种模态为条件生成另一种模态，或者将它们与文本和音频等其他模态集成。由于2D视频和3D人体运动在结构和分布上存在显著差异，因此统一它们进行同步优化和生成仍然是一个未被充分探索的领域，面临着巨大的挑战。受LLM统一不同模态能力的启发，我们的方法将视频和3D运动建模为统一的tokens序列，并利用单独的嵌入层来缓解分布差距。此外，我们设计了一种序列建模策略，在一个框架内集成了两个不同的任务，证明了统一建模的有效性。而且，为了有效地与视觉tokens对齐并保留3D空间信息，我们设计了一种具有时间扩展策略的新型3D运动tokenizer，使用单个VQ-VAE来生成量化的运动tokens。它具有多个专家解码器，用于处理身体形状、平移、全局方向和身体姿势，以实现可靠的3D运动重建。大量的实验表明，我们的方法在执行精确的运动捕捉的同时，可以同时生成相应的视频和运动。这项工作挖掘了LLM融合不同数据类型的能力，为将以人为中心的信息集成到现有模型中铺平了道路，并有可能实现人类、物体和场景的多模态、可控的联合建模。

## 🔬 方法详解

**问题定义**：现有方法主要关注单模态生成或将2D/3D人体运动与其他模态融合，缺乏对2D视频和3D人体运动的统一建模和同步生成能力。由于2D视频和3D人体运动在结构和分布上存在巨大差异，直接进行联合建模面临挑战。

**核心思路**：借鉴LLM统一不同模态的能力，将2D视频和3D人体运动视为统一的tokens序列，通过自回归模型学习它们之间的联合分布。通过统一的建模框架，实现2D视频和3D人体运动的同步生成和理解。

**技术框架**：UniMo包含以下主要模块：1) 2D视频编码器：将视频帧编码为视觉tokens序列；2) 3D运动tokenizer：将3D人体运动数据量化为运动tokens序列；3) 统一的自回归模型：以视觉tokens和运动tokens作为输入，学习它们的联合分布，实现同步生成；4) 3D运动解码器：将运动tokens解码为3D人体运动数据。

**关键创新**：1) 统一建模框架：首次将2D视频和3D人体运动统一到同一个自回归模型中，实现同步生成和理解；2) 3D运动tokenizer：设计了一种具有时间扩展策略的新型3D运动tokenizer，使用单个VQ-VAE生成量化的运动tokens，并使用多个专家解码器处理身体形状、平移、全局方向和身体姿势，以实现可靠的3D运动重建。

**关键设计**：1) 使用单独的嵌入层来缓解2D视频和3D人体运动在分布上的差距；2) 设计了一种序列建模策略，在一个框架内集成了视频生成和运动生成两个任务；3) 3D运动tokenizer采用VQ-VAE进行量化，并使用多个专家解码器分别处理身体形状、平移、全局方向和身体姿势。

## 📊 实验亮点

UniMo在同步生成2D视频和3D人体运动方面取得了显著成果。实验结果表明，UniMo能够生成高质量的视频和运动，并且能够准确地捕捉人体运动的细节。与现有方法相比，UniMo在运动捕捉精度和生成视频的真实性方面均有提升。具体性能数据未知。

## 🎯 应用场景

UniMo在虚拟现实、游戏开发、动画制作等领域具有广泛的应用前景。它可以用于生成逼真的人体运动视频，也可以用于根据给定的视频生成相应的3D人体运动。此外，UniMo还可以作为其他多模态模型的组成部分，用于构建更复杂的人机交互系统，例如，可以结合文本或语音输入来控制虚拟角色的运动。

## 📄 摘要（原文）

> We propose UniMo, an innovative autoregressive model for joint modeling of 2D human videos and 3D human motions within a unified framework, enabling simultaneous generation and understanding of these two modalities for the first time. Current methods predominantly focus on generating one modality given another as the condition or integrating either of them with other modalities such as text and audio. Unifying 2D videos and 3D motions for simultaneous optimization and generation remains largely unexplored, presenting significant challenges due to their substantial structural and distributional differences. Inspired by the LLM's ability to unify different modalities, our method models videos and 3D motions as a unified tokens sequence, utilizing separate embedding layers to mitigate distribution gaps. Additionally, we devise a sequence modeling strategy that integrates two distinct tasks within a single framework, proving the effectiveness of unified modeling. Moreover, to efficiently align with visual tokens and preserve 3D spatial information, we design a novel 3D motion tokenizer with a temporal expansion strategy, using a single VQ-VAE to produce quantized motion tokens. It features multiple expert decoders that handle body shapes, translation, global orientation, and body poses for reliable 3D motion reconstruction. Extensive experiments demonstrate that our method simultaneously generates corresponding videos and motions while performing accurate motion capture. This work taps into the capacity of LLMs to fuse diverse data types, paving the way for integrating human-centric information into existing models and potentially enabling multimodal, controllable joint modeling of humans, objects, and scenes.

