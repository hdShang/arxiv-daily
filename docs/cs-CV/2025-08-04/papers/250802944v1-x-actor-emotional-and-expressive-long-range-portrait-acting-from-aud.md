---
layout: default
title: "X-Actor: Emotional and Expressive Long-Range Portrait Acting from Audio"
---

# X-Actor: Emotional and Expressive Long-Range Portrait Acting from Audio

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.02944" class="toolbar-btn" target="_blank">📄 arXiv: 2508.02944v1</a>
  <a href="https://arxiv.org/pdf/2508.02944.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.02944v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.02944v1', 'X-Actor: Emotional and Expressive Long-Range Portrait Acting from Audio')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenxu Zhang, Zenan Li, Hongyi Xu, You Xie, Xiaochen Zhao, Tianpei Gu, Guoxian Song, Xin Chen, Chao Liang, Jianwen Jiang, Linjie Luo

**分类**: cs.CV

**发布日期**: 2025-08-04

**备注**: Project Page at https://byteaigc.github.io/X-Actor/

---

## 💡 一句话要点

**提出X-Actor以解决长视频情感表达问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `音频驱动动画` `情感表达` `长视频生成` `自回归模型` `扩散模型` `面部运动` `虚拟角色` `计算机视觉`

## 📋 核心要点

1. 现有方法主要集中在短期口型同步，难以捕捉长时间的情感变化和动态演绎。
2. X-Actor通过音频条件自回归扩散模型和视频合成模块，解耦面部运动与身份信息，实现长篇情感表达。
3. 实验结果显示，X-Actor在长程音频驱动的情感肖像表演中表现优异，超越了现有技术，达到了新的性能标准。

## 📝 摘要（中文）

我们提出了X-Actor，这是一种新颖的音频驱动肖像动画框架，能够从单一参考图像和输入音频片段生成栩栩如生、情感丰富的对话视频。与以往强调口型同步和短期视觉保真的方法不同，X-Actor能够实现演员级的长篇肖像表演，捕捉与语音节奏和内容一致的细腻、动态变化的情感。我们的方法核心是一个两阶段的解耦生成管道：一个音频条件自回归扩散模型在长时间上下文窗口内预测富有表现力但与身份无关的面部运动潜在标记，随后是一个基于扩散的视频合成模块，将这些运动转化为高保真视频动画。通过在与视觉和身份线索解耦的紧凑面部运动潜在空间中操作，我们的自回归扩散模型有效捕捉音频与面部动态之间的长程相关性，实现了无误差累积的情感丰富运动预测。大量实验表明，X-Actor生成的表演超越了标准的对话头动画，并在长程音频驱动的情感肖像表演中达到了最先进的结果。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有音频驱动肖像动画方法在长时间情感表达上的不足，现有方法往往无法有效捕捉和表达复杂的情感变化，且容易在长时间生成中出现误差累积的问题。

**核心思路**：X-Actor的核心思路是通过音频条件自回归扩散模型来预测面部运动，并将其与视频合成模块结合，从而实现高保真、情感丰富的长篇肖像动画。此设计使得模型能够在长时间上下文中捕捉音频与面部动态之间的相关性。

**技术框架**：整体架构分为两个主要阶段：第一阶段是音频条件自回归扩散模型，负责生成面部运动潜在标记；第二阶段是扩散视频合成模块，将这些运动转化为高质量的视频动画。

**关键创新**：最重要的技术创新在于解耦面部运动与身份信息，使得模型能够在一个紧凑的潜在空间中操作，捕捉长程音频与面部动态之间的关系，从而避免了误差累积。

**关键设计**：在模型设计中，采用了特定的损失函数来优化生成的面部运动与音频的匹配度，并在网络结构上进行了优化，以提高生成视频的质量和流畅性。具体的参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

实验结果表明，X-Actor在长程音频驱动的情感肖像表演中达到了最先进的性能，相较于基线方法，生成的视频在情感表达和视觉质量上均有显著提升，具体性能数据未在摘要中提供。

## 🎯 应用场景

X-Actor的潜在应用场景包括影视制作、虚拟现实、游戏开发等领域，能够为角色动画提供更自然、情感丰富的表现，提升用户体验。此外，该技术还可用于教育、培训等需要情感表达的场景，具有广泛的实际价值和影响力。

## 📄 摘要（原文）

> We present X-Actor, a novel audio-driven portrait animation framework that generates lifelike, emotionally expressive talking head videos from a single reference image and an input audio clip. Unlike prior methods that emphasize lip synchronization and short-range visual fidelity in constrained speaking scenarios, X-Actor enables actor-quality, long-form portrait performance capturing nuanced, dynamically evolving emotions that flow coherently with the rhythm and content of speech. Central to our approach is a two-stage decoupled generation pipeline: an audio-conditioned autoregressive diffusion model that predicts expressive yet identity-agnostic facial motion latent tokens within a long temporal context window, followed by a diffusion-based video synthesis module that translates these motions into high-fidelity video animations. By operating in a compact facial motion latent space decoupled from visual and identity cues, our autoregressive diffusion model effectively captures long-range correlations between audio and facial dynamics through a diffusion-forcing training paradigm, enabling infinite-length emotionally-rich motion prediction without error accumulation. Extensive experiments demonstrate that X-Actor produces compelling, cinematic-style performances that go beyond standard talking head animations and achieves state-of-the-art results in long-range, audio-driven emotional portrait acting.

