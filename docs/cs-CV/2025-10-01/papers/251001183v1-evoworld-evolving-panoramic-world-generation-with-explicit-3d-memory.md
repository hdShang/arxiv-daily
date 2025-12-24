---
layout: default
title: "EvoWorld: Evolving Panoramic World Generation with Explicit 3D Memory"
---

# EvoWorld: Evolving Panoramic World Generation with Explicit 3D Memory

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.01183" class="toolbar-btn" target="_blank">📄 arXiv: 2510.01183v1</a>
  <a href="https://arxiv.org/pdf/2510.01183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01183v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.01183v1', 'EvoWorld: Evolving Panoramic World Generation with Explicit 3D Memory')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Wang, Luoxin Ye, TaiMing Lu, Junfei Xiao, Jiahan Zhang, Yuxiang Guo, Xijun Liu, Rama Chellappa, Cheng Peng, Alan Yuille, Jieneng Chen

**分类**: cs.CV

**发布日期**: 2025-10-01

**备注**: Code available at: https://github.com/JiahaoPlus/EvoWorld

---

## 💡 一句话要点

**EvoWorld：利用显式3D记忆演化的全景世界生成模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `世界模型` `全景视频生成` `3D重建` `长时程探索` `空间一致性` `几何重投影` `Transformer`

## 📋 核心要点

1. 现有视频生成方法难以保证长时程探索中的空间一致性，尤其是在复杂场景中。
2. EvoWorld通过演化的3D记忆来指导视频生成，利用几何重投影提供丰富的空间线索，提升视觉真实感和几何一致性。
3. 在合成、室内和真实世界数据集上的实验表明，EvoWorld在视觉保真度和空间连贯性方面优于现有方法。

## 📝 摘要（中文）

本文提出EvoWorld，一个将全景视频生成与演化3D记忆相结合的世界模型，旨在实现空间一致的长时程探索。给定单个全景图像作为输入，EvoWorld首先利用具有精细视角控制的视频生成器生成未来视频帧，然后使用前馈即插即用Transformer演化场景的3D重建，最后通过以来自该演化显式3D记忆的几何重投影为条件来合成未来帧。与仅合成视频的现有技术不同，本文的关键在于利用这种演化的3D重建作为视频生成过程的显式空间指导，将重建的几何体投影到目标视点，以提供丰富的空间线索，从而显著提高视觉真实感和几何一致性。为了评估长距离探索能力，本文引入了首个综合基准，涵盖合成户外环境、Habitat室内场景和具有挑战性的真实世界场景，特别强调了循环闭合检测和扩展轨迹上的空间连贯性。大量实验表明，与现有方法相比，EvoWorld的演化3D记忆显著提高了视觉保真度并保持了空间场景连贯性，代表了在长时程空间一致世界建模方面的重要进展。

## 🔬 方法详解

**问题定义**：现有视频生成方法，尤其是在长时程探索场景下，难以维持生成视频的空间一致性。它们通常缺乏对场景几何结构的显式建模，导致生成的视频在视角变化时出现不自然的扭曲或不连贯的现象。尤其是在循环闭合等任务中，这种不一致性会严重影响性能。

**核心思路**：EvoWorld的核心思路是利用一个演化的3D记忆来显式地建模场景的几何结构，并将其作为视频生成过程中的空间指导。通过将重建的3D几何体投影到目标视点，可以为视频生成器提供丰富的空间线索，从而提高生成视频的视觉真实感和几何一致性。这种显式的3D建模能够更好地处理视角变化和遮挡等问题，从而实现更稳定的长时程探索。

**技术框架**：EvoWorld的整体框架包含三个主要模块：1) 视频生成器：用于生成未来视频帧，具有精细的视角控制能力。2) 3D重建演化模块：使用前馈即插即用Transformer来演化场景的3D重建。3) 几何重投影模块：将演化的3D记忆投影到目标视点，为视频生成器提供空间指导。整个流程是：给定一个全景图像，视频生成器生成初步的未来帧，然后3D重建演化模块更新场景的3D表示，最后几何重投影模块将3D信息融入到视频生成过程中，生成最终的视频帧。

**关键创新**：EvoWorld的关键创新在于将演化的3D重建作为视频生成过程的显式空间指导。与以往仅依赖于图像或视频信息的生成方法不同，EvoWorld通过显式地建模场景的几何结构，并将其融入到生成过程中，从而显著提高了生成视频的空间一致性。这种显式的3D建模使得EvoWorld能够更好地处理视角变化和遮挡等问题，从而实现更稳定的长时程探索。

**关键设计**：3D重建演化模块使用前馈Transformer来更新3D表示，允许快速和可扩展的3D场景演化。几何重投影模块使用可微渲染技术，将3D几何体投影到目标视点，并生成深度图和法线图等空间信息，这些信息被用作视频生成器的额外输入。损失函数包括图像重建损失、深度一致性损失和法线一致性损失，以确保生成视频的视觉真实感和几何一致性。具体参数设置和网络结构细节在论文中有详细描述（未知）。

## 📊 实验亮点

EvoWorld在合成户外环境、Habitat室内场景和真实世界场景等多个数据集上进行了评估。实验结果表明，与现有方法相比，EvoWorld在视觉保真度和空间连贯性方面均有显著提升。特别是在循环闭合检测任务中，EvoWorld的性能优于现有方法，证明了其在长时程探索方面的优势。具体性能数据和提升幅度在论文中有详细描述（未知）。

## 🎯 应用场景

EvoWorld具有广泛的应用前景，包括虚拟现实、增强现实、机器人导航、自动驾驶等领域。它可以用于创建更逼真和空间一致的虚拟环境，帮助机器人更好地理解和探索周围环境，并提高自动驾驶系统的安全性。此外，EvoWorld还可以用于视频游戏开发、电影制作等创意产业，为用户提供更沉浸式的体验。

## 📄 摘要（原文）

> Humans possess a remarkable ability to mentally explore and replay 3D environments they have previously experienced. Inspired by this mental process, we present EvoWorld: a world model that bridges panoramic video generation with evolving 3D memory to enable spatially consistent long-horizon exploration. Given a single panoramic image as input, EvoWorld first generates future video frames by leveraging a video generator with fine-grained view control, then evolves the scene's 3D reconstruction using a feedforward plug-and-play transformer, and finally synthesizes futures by conditioning on geometric reprojections from this evolving explicit 3D memory. Unlike prior state-of-the-arts that synthesize videos only, our key insight lies in exploiting this evolving 3D reconstruction as explicit spatial guidance for the video generation process, projecting the reconstructed geometry onto target viewpoints to provide rich spatial cues that significantly enhance both visual realism and geometric consistency. To evaluate long-range exploration capabilities, we introduce the first comprehensive benchmark spanning synthetic outdoor environments, Habitat indoor scenes, and challenging real-world scenarios, with particular emphasis on loop-closure detection and spatial coherence over extended trajectories. Extensive experiments demonstrate that our evolving 3D memory substantially improves visual fidelity and maintains spatial scene coherence compared to existing approaches, representing a significant advance toward long-horizon spatially consistent world modeling.

