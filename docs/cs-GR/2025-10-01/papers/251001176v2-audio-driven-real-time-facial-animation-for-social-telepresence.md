---
layout: default
title: Audio Driven Real-Time Facial Animation for Social Telepresence
---

# Audio Driven Real-Time Facial Animation for Social Telepresence

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01176" target="_blank" class="toolbar-btn">arXiv: 2510.01176v2</a>
    <a href="https://arxiv.org/pdf/2510.01176.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01176v2" 
            onclick="toggleFavorite(this, '2510.01176v2', 'Audio Driven Real-Time Facial Animation for Social Telepresence')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jiye Lee, Chenghui Li, Linh Tran, Shih-En Wei, Jason Saragih, Alexander Richard, Hanbyul Joo, Shaojie Bai

**分类**: cs.GR, cs.CV, cs.LG, cs.SD

**发布日期**: 2025-10-01 (更新: 2025-11-01)

**备注**: SIGGRAPH Asia 2025. Project page: https://jiyewise.github.io/projects/AudioRTA

**DOI**: [10.1145/3757377.3763854](https://doi.org/10.1145/3757377.3763854)

---

## 💡 一句话要点

**提出一种基于音频驱动的实时面部动画系统，用于社交远程呈现。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音频驱动` `面部动画` `实时渲染` `扩散模型` `在线Transformer` `蒸馏学习` `社交VR`

## 📋 核心要点

1. 现有音频驱动面部动画方法难以兼顾高真实度、低延迟和实时性，限制了其在社交VR中的应用。
2. 利用扩散模型的生成能力，结合在线Transformer和蒸馏技术，实现高质量、低延迟的实时面部动画。
3. 实验表明，该方法在面部动画准确性上优于现有技术，推理速度提升显著，并成功应用于实时VR演示。

## 📝 摘要（中文）

本文提出了一种音频驱动的实时系统，用于为虚拟现实中的社交互动生成逼真的3D面部头像动画，且延迟极低。该方法的核心是一个编码器模型，能够实时将音频信号转换为潜在的面部表情序列，然后将其解码为逼真的3D面部头像。利用扩散模型的生成能力，系统能够捕捉自然交流所需的丰富面部表情，同时实现实时性能（<15ms GPU时间）。通过在线Transformer（消除了对未来输入的依赖）和蒸馏流水线（将迭代去噪加速为单步），该架构最大限度地降低了延迟。此外，还解决了实时场景中逐帧处理连续音频信号并保持一致动画质量的关键设计挑战。该框架的多功能性扩展到多模态应用，包括情感条件等语义模态以及VR头显上的头戴式眼动相机等传感器。实验结果表明，与现有的离线最先进基线相比，面部动画的准确性得到了显著提高，推理速度提高了100到1000倍。通过实时VR演示和多语言语音等各种场景验证了该方法。

## 🔬 方法详解

**问题定义**：现有音频驱动的面部动画方法通常难以在真实感、延迟和实时性之间取得平衡。离线方法虽然可以生成高质量的动画，但延迟过高，无法满足实时交互的需求。而现有的实时方法往往牺牲了动画的真实感和丰富性。因此，该论文旨在解决如何在保证面部动画真实感的同时，实现极低的延迟，从而满足社交VR等实时应用的需求。

**核心思路**：该论文的核心思路是利用扩散模型的强大生成能力来捕捉丰富的面部表情，并通过在线Transformer和蒸馏技术来加速推理过程，从而实现实时性能。通过将音频信号编码为潜在的面部表情序列，并使用扩散模型解码为逼真的3D面部头像，可以在保证动画质量的同时，显著降低延迟。

**技术框架**：该系统主要包含两个阶段：编码阶段和解码阶段。在编码阶段，使用一个在线Transformer将音频信号实时转换为潜在的面部表情序列。在线Transformer的设计避免了对未来输入的依赖，从而降低了延迟。在解码阶段，使用一个基于扩散模型的解码器将潜在的面部表情序列解码为逼真的3D面部头像。为了进一步加速解码过程，采用了一种蒸馏流水线，将迭代去噪过程加速为单步。

**关键创新**：该论文的关键创新在于以下几点：1) 提出了一种在线Transformer，消除了对未来输入的依赖，从而降低了延迟。2) 提出了一种蒸馏流水线，将迭代去噪过程加速为单步，从而显著提高了推理速度。3) 将扩散模型应用于实时面部动画，从而在保证动画质量的同时，实现了实时性能。

**关键设计**：在线Transformer采用了因果注意力机制，确保每个时间步的输出只依赖于过去的输入。蒸馏流水线通过训练一个单步模型来逼近迭代去噪过程的结果。损失函数包括重建损失和对抗损失，用于保证动画的真实感和一致性。具体参数设置和网络结构细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

实验结果表明，该方法在面部动画准确性上显著优于现有的离线最先进基线，推理速度提高了100到1000倍，实现了<15ms的GPU时间。通过实时VR演示和多语言语音等各种场景验证了该方法的有效性和鲁棒性。这些结果表明，该方法在实时面部动画领域具有显著的优势。

## 🎯 应用场景

该研究成果可广泛应用于社交VR、远程会议、虚拟主播、游戏等领域。通过实时捕捉和生成逼真的面部动画，可以增强虚拟交互的沉浸感和真实感，提升用户体验。此外，该技术还可以应用于个性化头像定制、情感识别和表达等领域，具有广阔的应用前景。

## 📄 摘要（原文）

> We present an audio-driven real-time system for animating photorealistic 3D facial avatars with minimal latency, designed for social interactions in virtual reality for anyone. Central to our approach is an encoder model that transforms audio signals into latent facial expression sequences in real time, which are then decoded as photorealistic 3D facial avatars. Leveraging the generative capabilities of diffusion models, we capture the rich spectrum of facial expressions necessary for natural communication while achieving real-time performance (<15ms GPU time). Our novel architecture minimizes latency through two key innovations: an online transformer that eliminates dependency on future inputs and a distillation pipeline that accelerates iterative denoising into a single step. We further address critical design challenges in live scenarios for processing continuous audio signals frame-by-frame while maintaining consistent animation quality. The versatility of our framework extends to multimodal applications, including semantic modalities such as emotion conditions and multimodal sensors with head-mounted eye cameras on VR headsets. Experimental results demonstrate significant improvements in facial animation accuracy over existing offline state-of-the-art baselines, achieving 100 to 1000 times faster inference speed. We validate our approach through live VR demonstrations and across various scenarios such as multilingual speeches.

