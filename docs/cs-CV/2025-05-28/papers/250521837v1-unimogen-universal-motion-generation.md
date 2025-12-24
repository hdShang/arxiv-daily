---
layout: default
title: UniMoGen: Universal Motion Generation
---

# UniMoGen: Universal Motion Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21837" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21837v1</a>
  <a href="https://arxiv.org/pdf/2505.21837.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21837v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21837v1', 'UniMoGen: Universal Motion Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aliasghar Khani, Arianna Rampini, Evan Atherton, Bruno Roy

**分类**: cs.CV, cs.LG

**发布日期**: 2025-05-28

---

## 💡 一句话要点

**提出UniMoGen以解决骨架依赖的运动生成问题**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `运动生成` `骨架无关` `UNet` `扩散模型` `计算机图形学` `动画制作` `机器人控制` `多样角色`

## 📋 核心要点

1. 现有的运动生成方法依赖于特定的骨架结构，限制了其在不同角色间的适用性和灵活性。
2. UniMoGen是一种新颖的UNet基础的扩散模型，能够实现骨架无关的运动生成，动态处理所需的关节。
3. 在100style数据集上，UniMoGen的表现超越了现有的最先进方法，展示了其在多样角色运动生成中的有效性。

## 📝 摘要（中文）

运动生成是计算机图形学、动画、游戏和机器人领域的基础，能够创建逼真且多样的角色运动。现有方法的一个显著限制是依赖特定的骨架结构，限制了其在不同角色间的通用性。为此，本文提出了UniMoGen，这是一种基于UNet的扩散模型，旨在实现骨架无关的运动生成。UniMoGen可以在多样角色（如人类和动物）的运动数据上进行训练，而无需预定义最大关节数。通过动态处理每个角色所需的关节，模型实现了骨架无关性和计算效率。UniMoGen的关键特性包括通过风格和轨迹输入进行可控性，以及能够从过去帧继续运动。实验结果表明，UniMoGen在100style数据集上优于现有最先进的方法，并在100style和LAFAN1数据集上表现出高效能和改进的效率，展示了其在角色动画中的广泛应用潜力。

## 🔬 方法详解

**问题定义**：现有的运动生成方法通常依赖于特定的骨架结构，这导致其在不同角色之间的通用性和灵活性受到限制。为了克服这一限制，本文提出了一种新的方法来实现骨架无关的运动生成。

**核心思路**：UniMoGen通过引入基于UNet的扩散模型，能够在没有预定义最大关节数的情况下，处理来自多样角色的运动数据。该模型通过动态选择和处理每个角色所需的关节，确保了骨架无关性和计算效率。

**技术框架**：UniMoGen的整体架构包括数据输入模块、运动生成模块和输出控制模块。数据输入模块负责接收不同角色的运动数据，运动生成模块利用UNet结构生成运动序列，输出控制模块则通过风格和轨迹输入实现对运动的可控性。

**关键创新**：UniMoGen的核心创新在于其骨架无关性和动态关节处理能力，这与传统方法的固定骨架结构形成鲜明对比。该模型的设计使其能够适应多种角色，提升了运动生成的灵活性。

**关键设计**：在网络结构上，UniMoGen采用了UNet架构，结合了扩散模型的优点。损失函数设计上，考虑了运动连续性和风格一致性，以确保生成运动的自然性和多样性。

## 📊 实验亮点

在100style数据集上，UniMoGen的运动生成效果显著优于现有最先进的方法，展示了其在多样角色运动生成中的有效性。通过在100style和LAFAN1数据集上的训练，UniMoGen在不同骨架上均表现出高性能和改进的效率，进一步验证了其灵活性和适应性。

## 🎯 应用场景

UniMoGen在计算机图形学、动画制作、游戏开发和机器人控制等领域具有广泛的应用潜力。其骨架无关的特性使得开发者能够更灵活地创建多样化的角色动画，提升了动画制作的效率和质量。此外，该模型的可控性为用户提供了更多的创作自由，能够满足不同场景的需求。

## 📄 摘要（原文）

> Motion generation is a cornerstone of computer graphics, animation, gaming, and robotics, enabling the creation of realistic and varied character movements. A significant limitation of existing methods is their reliance on specific skeletal structures, which restricts their versatility across different characters. To overcome this, we introduce UniMoGen, a novel UNet-based diffusion model designed for skeleton-agnostic motion generation. UniMoGen can be trained on motion data from diverse characters, such as humans and animals, without the need for a predefined maximum number of joints. By dynamically processing only the necessary joints for each character, our model achieves both skeleton agnosticism and computational efficiency. Key features of UniMoGen include controllability via style and trajectory inputs, and the ability to continue motions from past frames. We demonstrate UniMoGen's effectiveness on the 100style dataset, where it outperforms state-of-the-art methods in diverse character motion generation. Furthermore, when trained on both the 100style and LAFAN1 datasets, which use different skeletons, UniMoGen achieves high performance and improved efficiency across both skeletons. These results highlight UniMoGen's potential to advance motion generation by providing a flexible, efficient, and controllable solution for a wide range of character animations.

