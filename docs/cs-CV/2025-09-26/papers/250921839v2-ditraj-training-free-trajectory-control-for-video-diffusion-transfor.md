---
layout: default
title: "DiTraj: training-free trajectory control for video diffusion transformer"
---

# DiTraj: training-free trajectory control for video diffusion transformer

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21839" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21839v2</a>
  <a href="https://arxiv.org/pdf/2509.21839.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21839v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21839v2', 'DiTraj: training-free trajectory control for video diffusion transformer')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheng Lei, Jiayu Zhang, Yue Ma, Xinyu Wang, Long Chen, Liang Tang, Yiqiang Yan, Fei Su, Zhicheng Zhao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-26 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出DiTraj，一种面向视频扩散Transformer的免训练轨迹控制框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视频生成` `轨迹控制` `扩散模型` `Transformer` `位置编码` `免训练方法`

## 📋 核心要点

1. 现有轨迹控制方法需要大量训练资源或专为U-Net设计，无法充分利用DiT的卓越性能。
2. DiTraj通过前景-背景分离引导和帧间时空解耦的3D-RoPE，实现免训练的轨迹控制。
3. 实验结果表明，DiTraj在视频质量和轨迹可控性上均优于现有方法，展现了其有效性。

## 📝 摘要（中文）

本文提出DiTraj，一个简单而有效的免训练框架，用于文本到视频生成中的轨迹控制，专门为Diffusion Transformers (DiT)设计。首先，为了注入对象的轨迹，我们提出了前景-背景分离引导：使用大型语言模型（LLM）将用户提供的提示转换为前景和背景提示，分别指导视频中前景和背景区域的生成。然后，我们分析了3D全注意力机制，并探索了token间注意力分数与位置嵌入之间的紧密相关性。基于此，我们提出了帧间时空解耦的3D-RoPE（STD-RoPE）。通过仅修改前景token的位置嵌入，STD-RoPE消除了它们之间的跨帧空间差异，加强了它们之间的跨帧注意力，从而增强了轨迹控制。此外，我们通过调节位置嵌入的密度来实现3D感知的轨迹控制。大量实验表明，我们的方法在视频质量和轨迹可控性方面均优于现有方法。

## 🔬 方法详解

**问题定义**：现有视频生成模型，特别是基于Diffusion Transformer (DiT) 的模型，在生成高质量视频方面表现出色。然而，如何有效地控制视频中特定物体的运动轨迹仍然是一个挑战。现有的轨迹控制方法通常需要大量的训练数据和计算资源，或者专门为U-Net架构设计，无法直接应用于DiT模型，限制了DiT在可控视频生成方面的应用。

**核心思路**：DiTraj的核心思路是通过解耦前景和背景的生成过程，并利用改进的旋转位置编码（RoPE）来精确控制前景物体的运动轨迹。具体来说，首先使用大型语言模型将用户提示分解为前景和背景提示，分别指导相应区域的生成。然后，通过修改前景token的位置嵌入，增强它们之间的跨帧注意力，从而实现对轨迹的精确控制。

**技术框架**：DiTraj框架主要包含两个关键模块：1) 前景-背景分离引导模块：利用大型语言模型将用户输入的文本提示分解为前景提示和背景提示，分别用于指导视频中前景和背景区域的生成。2) 帧间时空解耦的3D-RoPE（STD-RoPE）模块：通过修改前景token的位置嵌入，消除它们之间的跨帧空间差异，增强跨帧注意力，从而实现对轨迹的精确控制。整个流程无需额外的训练。

**关键创新**：DiTraj的关键创新在于提出了帧间时空解耦的3D-RoPE（STD-RoPE）。与传统的RoPE相比，STD-RoPE能够更有效地控制前景token的运动轨迹，因为它只修改前景token的位置嵌入，从而避免了对背景区域的影响。此外，通过调节位置嵌入的密度，DiTraj还可以实现3D感知的轨迹控制。

**关键设计**：在前景-背景分离引导模块中，使用了特定的prompt工程技术，以确保LLM能够准确地提取前景和背景信息。在STD-RoPE模块中，关键在于如何确定哪些token属于前景，这可以通过注意力机制或语义分割等方法来实现。此外，位置嵌入密度的调节策略也需要根据具体的应用场景进行调整。

## 📊 实验亮点

实验结果表明，DiTraj在视频质量和轨迹可控性方面均优于现有方法。与基线方法相比，DiTraj能够生成更清晰、更逼真的视频，并且能够更精确地控制前景物体的运动轨迹。定量评估指标显示，DiTraj在轨迹误差方面显著降低，同时保持了较高的视频质量评分。

## 🎯 应用场景

DiTraj在视频编辑、游戏开发、电影制作等领域具有广泛的应用前景。例如，用户可以使用DiTraj轻松地控制视频中角色的运动轨迹，或者创建具有特定运动模式的特效。此外，DiTraj还可以用于生成具有特定故事情节的动画视频，从而降低动画制作的成本和难度。该研究为可控视频生成提供了一种新的思路，有望推动相关技术的发展。

## 📄 摘要（原文）

> Diffusion Transformers (DiT)-based video generation models with 3D full attention exhibit strong generative capabilities. Trajectory control represents a user-friendly task in the field of controllable video generation. However, existing methods either require substantial training resources or are specifically designed for U-Net, do not take advantage of the superior performance of DiT. To address these issues, we propose DiTraj, a simple but effective training-free framework for trajectory control in text-to-video generation, tailored for DiT. Specifically, first, to inject the object's trajectory, we propose foreground-background separation guidance: we use the Large Language Model (LLM) to convert user-provided prompts into foreground and background prompts, which respectively guide the generation of foreground and background regions in the video. Then, we analyze 3D full attention and explore the tight correlation between inter-token attention scores and position embedding. Based on this, we propose inter-frame Spatial-Temporal Decoupled 3D-RoPE (STD-RoPE). By modifying only foreground tokens' position embedding, STD-RoPE eliminates their cross-frame spatial discrepancies, strengthening cross-frame attention among them and thus enhancing trajectory control. Additionally, we achieve 3D-aware trajectory control by regulating the density of position embedding. Extensive experiments demonstrate that our method outperforms previous methods in both video quality and trajectory controllability.

