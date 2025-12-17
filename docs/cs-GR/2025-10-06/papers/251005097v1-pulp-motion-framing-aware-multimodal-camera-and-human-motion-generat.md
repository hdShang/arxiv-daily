---
layout: default
title: Pulp Motion: Framing-aware multimodal camera and human motion generation
---

# Pulp Motion: Framing-aware multimodal camera and human motion generation

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.05097" target="_blank" class="toolbar-btn">arXiv: 2510.05097v1</a>
    <a href="https://arxiv.org/pdf/2510.05097.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.05097v1" 
            onclick="toggleFavorite(this, '2510.05097v1', 'Pulp Motion: Framing-aware multimodal camera and human motion generation')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Robin Courant, Xi Wang, David Loiseaux, Marc Christie, Vicky Kalogeiton

**分类**: cs.GR, cs.CV

**发布日期**: 2025-10-06

**备注**: Project page: https://www.lix.polytechnique.fr/vista/projects/2025_pulpmotion_courant/

---

## 💡 一句话要点

**提出多模态联合生成方法以解决人类动作与摄像机轨迹生成问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态生成` `人类动作` `摄像机轨迹` `联合生成` `计算机视觉` `影视制作` `文本对齐`

## 📋 核心要点

1. 现有方法将人类动作与摄像机轨迹生成分开处理，忽视了两者之间的内在联系，导致生成结果缺乏一致性。
2. 本研究提出了一种模型无关的框架，通过引入屏幕框架作为辅助模态，实现人类动作与摄像机轨迹的联合生成。
3. 实验结果表明，该方法在生成一致的摄像机与人类动作方面表现优异，并在文本对齐方面也取得了显著的提升。

## 📝 摘要（中文）

在本论文中，我们首次将人类动作与摄像机轨迹生成任务视为文本条件下的联合生成，强调演员表演与摄像机工作之间的紧密互动。我们提出了一种简单的模型无关框架，通过引入辅助模态——在屏幕上投影人类关节所诱导的框架，来强制实现多模态一致性。我们设计了一个联合自编码器，学习共享潜在空间，并通过轻量线性变换将人类和摄像机潜在空间映射到框架潜在空间。此外，我们引入了辅助采样，利用线性变换引导生成一致的框架模态。实验结果表明，我们的方法在生成框架一致的人类与摄像机动作方面表现出色，并在文本对齐上也取得了显著提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决人类动作与摄像机轨迹生成的联合问题。现有方法往往将这两者分开处理，导致生成结果缺乏一致性，无法充分体现电影摄影的核心原则。

**核心思路**：我们提出了一种新的框架，将人类动作与摄像机轨迹的生成视为一个文本条件下的联合生成任务。通过引入屏幕框架作为辅助模态，促进了两者之间的多模态一致性。

**技术框架**：整体架构包括一个联合自编码器，该自编码器学习共享潜在空间，并通过轻量级线性变换将人类和摄像机的潜在空间映射到框架潜在空间。此外，采用辅助采样方法来引导生成过程。

**关键创新**：最重要的创新点在于引入了屏幕框架作为辅助模态，形成了人类动作与摄像机轨迹之间的自然桥梁，从而提升了生成的一致性和精确度。

**关键设计**：在设计中，我们设置了共享潜在空间的结构，并采用了轻量级线性变换来实现模态间的映射。损失函数的设计也考虑了多模态一致性，确保生成结果在视觉上具有连贯性。

## 📊 实验亮点

实验结果显示，我们的方法在生成框架一致的人类与摄像机动作方面达到了新的技术水平，尤其在文本对齐方面，相较于基线方法有显著提升，具体性能数据未详述，但整体效果优于现有技术。

## 🎯 应用场景

该研究的潜在应用领域包括电影制作、虚拟现实和游戏开发等。通过实现人类动作与摄像机轨迹的高效生成，可以显著提升影视作品的制作效率和质量，推动相关领域的技术进步与创新。

## 📄 摘要（原文）

> Treating human motion and camera trajectory generation separately overlooks a core principle of cinematography: the tight interplay between actor performance and camera work in the screen space. In this paper, we are the first to cast this task as a text-conditioned joint generation, aiming to maintain consistent on-screen framing while producing two heterogeneous, yet intrinsically linked, modalities: human motion and camera trajectories. We propose a simple, model-agnostic framework that enforces multimodal coherence via an auxiliary modality: the on-screen framing induced by projecting human joints onto the camera. This on-screen framing provides a natural and effective bridge between modalities, promoting consistency and leading to more precise joint distribution. We first design a joint autoencoder that learns a shared latent space, together with a lightweight linear transform from the human and camera latents to a framing latent. We then introduce auxiliary sampling, which exploits this linear transform to steer generation toward a coherent framing modality. To support this task, we also introduce the PulpMotion dataset, a human-motion and camera-trajectory dataset with rich captions, and high-quality human motions. Extensive experiments across DiT- and MAR-based architectures show the generality and effectiveness of our method in generating on-frame coherent human-camera motions, while also achieving gains on textual alignment for both modalities. Our qualitative results yield more cinematographically meaningful framings setting the new state of the art for this task. Code, models and data are available in our \href{https://www.lix.polytechnique.fr/vista/projects/2025_pulpmotion_courant/}{project page}.

