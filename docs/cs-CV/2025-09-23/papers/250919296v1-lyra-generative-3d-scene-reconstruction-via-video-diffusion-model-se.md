---
layout: default
title: "Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation"
---

# Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.19296" class="toolbar-btn" target="_blank">📄 arXiv: 2509.19296v1</a>
  <a href="https://arxiv.org/pdf/2509.19296.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.19296v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.19296v1', 'Lyra: Generative 3D Scene Reconstruction via Video Diffusion Model Self-Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sherwin Bahmani, Tianchang Shen, Jiawei Ren, Jiahui Huang, Yifeng Jiang, Haithem Turki, Andrea Tagliasacchi, David B. Lindell, Zan Gojcic, Sanja Fidler, Huan Ling, Jun Gao, Xuanchi Ren

**分类**: cs.CV, cs.GR

**发布日期**: 2025-09-23

**备注**: Project Page: https://research.nvidia.com/labs/toronto-ai/lyra/

---

## 💡 一句话要点

**Lyra：通过视频扩散模型自蒸馏实现生成式3D场景重建**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `3D场景重建` `视频扩散模型` `自蒸馏` `3D高斯溅射` `生成模型` `单目视觉` `虚拟环境生成`

## 📋 核心要点

1. 现有3D重建方法依赖多视角数据，获取困难，限制了应用场景。
2. Lyra通过自蒸馏框架，将视频扩散模型的隐式3D知识提炼为显式3DGS表示。
3. 实验表明，该框架在静态和动态3D场景生成方面均达到SOTA性能。

## 📝 摘要（中文）

生成虚拟环境的能力对于游戏、机器人、自动驾驶和工业AI等应用至关重要。现有的基于学习的3D重建方法依赖于捕获的真实世界多视角数据，而这些数据并非总是容易获得。最近视频扩散模型的进步展示了卓越的想象能力，但其2D性质限制了在机器人需要导航和与环境交互的模拟中的应用。本文提出了一种自蒸馏框架，旨在将视频扩散模型中的隐式3D知识提炼成显式的3D高斯溅射(3DGS)表示，从而消除了对多视角训练数据的需求。具体来说，我们用3DGS解码器增强了典型的RGB解码器，该解码器由RGB解码器的输出监督。在这种方法中，3DGS解码器可以完全用视频扩散模型生成的合成数据进行训练。在推理时，我们的模型可以从文本提示或单个图像合成3D场景以进行实时渲染。我们的框架进一步扩展到从单目输入视频生成动态3D场景。实验结果表明，我们的框架在静态和动态3D场景生成方面实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有基于学习的3D重建方法严重依赖于多视角图像数据，而获取高质量、多视角的真实世界数据成本高昂且不总是可行。此外，现有的视频扩散模型虽然具有强大的生成能力，但其本质是2D的，无法直接用于需要3D信息的任务，例如机器人导航和交互。

**核心思路**：Lyra的核心思想是利用视频扩散模型强大的2D生成能力，通过自蒸馏的方式，将其中蕴含的隐式3D知识提取出来，并将其转化为显式的3D表示。这样，就可以在不需要多视角数据的情况下，仅通过视频扩散模型生成的合成数据来训练3D重建模型。

**技术框架**：Lyra框架主要包含一个视频扩散模型（作为教师网络）和一个3DGS解码器（作为学生网络）。首先，使用视频扩散模型生成RGB图像。然后，将生成的RGB图像作为监督信号，训练3DGS解码器。3DGS解码器将图像解码为3D高斯溅射表示，该表示可以用于实时渲染和3D场景重建。整个训练过程是一个自蒸馏的过程，学生网络学习模仿教师网络的输出，从而获得3D场景的生成能力。

**关键创新**：Lyra的关键创新在于使用自蒸馏的方式，将2D视频扩散模型的知识迁移到3D表示学习中。这种方法避免了对多视角数据的依赖，使得3D场景重建可以在仅有单视角图像或文本提示的情况下进行。此外，使用3DGS作为3D表示，可以实现实时渲染。

**关键设计**：Lyra的关键设计包括：1) 使用预训练的视频扩散模型作为教师网络，提供高质量的监督信号；2) 使用3DGS作为3D表示，实现实时渲染；3) 设计合适的损失函数，使得3DGS解码器能够有效地学习视频扩散模型的知识。具体的损失函数包括RGB重建损失、深度一致性损失等。网络结构方面，3DGS解码器通常采用MLP结构，将图像特征映射到3D高斯分布的参数。

## 📊 实验亮点

Lyra在静态和动态3D场景生成方面均取得了SOTA性能。与现有方法相比，Lyra无需多视角训练数据，仅使用视频扩散模型生成的合成数据即可训练。实验结果表明，Lyra生成的3D场景具有更高的质量和更强的真实感。具体性能数据未知，但论文强调了其在主观视觉效果上的优越性。

## 🎯 应用场景

Lyra的应用场景广泛，包括游戏开发、机器人仿真、自动驾驶、工业AI等。它可以用于快速生成虚拟环境，为机器人提供训练数据，或者用于创建逼真的游戏场景。此外，Lyra还可以用于从单张图像或文本描述中重建3D场景，为用户提供更加沉浸式的体验。未来，Lyra有望成为虚拟现实和增强现实领域的重要工具。

## 📄 摘要（原文）

> The ability to generate virtual environments is crucial for applications ranging from gaming to physical AI domains such as robotics, autonomous driving, and industrial AI. Current learning-based 3D reconstruction methods rely on the availability of captured real-world multi-view data, which is not always readily available. Recent advancements in video diffusion models have shown remarkable imagination capabilities, yet their 2D nature limits the applications to simulation where a robot needs to navigate and interact with the environment. In this paper, we propose a self-distillation framework that aims to distill the implicit 3D knowledge in the video diffusion models into an explicit 3D Gaussian Splatting (3DGS) representation, eliminating the need for multi-view training data. Specifically, we augment the typical RGB decoder with a 3DGS decoder, which is supervised by the output of the RGB decoder. In this approach, the 3DGS decoder can be purely trained with synthetic data generated by video diffusion models. At inference time, our model can synthesize 3D scenes from either a text prompt or a single image for real-time rendering. Our framework further extends to dynamic 3D scene generation from a monocular input video. Experimental results show that our framework achieves state-of-the-art performance in static and dynamic 3D scene generation.

