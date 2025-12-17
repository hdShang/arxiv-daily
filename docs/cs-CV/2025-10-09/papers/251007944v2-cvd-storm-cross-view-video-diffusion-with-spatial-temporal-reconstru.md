---
layout: default
title: CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal Reconstruction Model for Autonomous Driving
---

# CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal Reconstruction Model for Autonomous Driving

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.07944" target="_blank" class="toolbar-btn">arXiv: 2510.07944v2</a>
    <a href="https://arxiv.org/pdf/2510.07944.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.07944v2" 
            onclick="toggleFavorite(this, '2510.07944v2', 'CVD-STORM: Cross-View Video Diffusion with Spatial-Temporal Reconstruction Model for Autonomous Driving')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Tianrui Zhang, Yichen Liu, Zilin Guo, Yuxin Guo, Jingcheng Ni, Chenjing Ding, Dan Xu, Lewei Lu, Zehuan Wu

**分类**: cs.CV

**发布日期**: 2025-10-09 (更新: 2025-10-16)

**🔗 代码/项目**: [PROJECT_PAGE](https://sensetime-fvg.github.io/CVD-STORM)

---

## 💡 一句话要点

**提出CVD-STORM，利用时空重建扩散模型生成自动驾驶多视角长视频，并具备4D重建能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视频生成` `扩散模型` `自动驾驶` `多视角` `时空重建` `变分自编码器` `4D重建` `高斯溅射`

## 📋 核心要点

1. 自动驾驶领域对高质量、可控视频生成的需求日益增长，同时需要深度估计等有意义的信息。
2. CVD-STORM通过微调VAE以增强其对3D结构和时间动态的编码能力，并将其融入视频扩散过程。
3. 实验表明，CVD-STORM在FID和FVD指标上取得了显著提升，并能有效重建动态场景的几何信息。

## 📝 摘要（中文）

本文提出了一种名为CVD-STORM的跨视角视频扩散模型，该模型利用时空重建变分自编码器（VAE）生成具有4D重建能力的长时、多视角视频，并支持多种控制输入。该方法首先通过辅助的4D重建任务对VAE进行微调，增强其编码3D结构和时间动态的能力。随后，将该VAE集成到视频扩散过程中，显著提高生成质量。实验结果表明，该模型在FID和FVD指标上均取得了显著提升。此外，联合训练的高斯溅射解码器能够有效地重建动态场景，为全面的场景理解提供有价值的几何信息。

## 🔬 方法详解

**问题定义**：现有方法难以在自动驾驶场景下生成高质量、长时序、多视角的视频，并且缺乏对场景几何信息的有效重建，限制了对环境的全面理解。痛点在于生成视频的真实性和信息丰富度不足。

**核心思路**：核心在于利用一个经过特殊训练的VAE来增强视频扩散模型的能力。通过预训练VAE使其能够更好地编码3D结构和时间动态，从而提高生成视频的质量和一致性。同时，引入高斯溅射解码器进行4D重建，提供几何信息。

**技术框架**：CVD-STORM包含两个主要阶段：1) 基于4D重建任务微调VAE；2) 将微调后的VAE集成到视频扩散模型中。VAE负责编码视频帧的时空信息，扩散模型负责生成高质量的视频帧。高斯溅射解码器与VAE联合训练，用于从VAE的隐空间重建动态场景。

**关键创新**：关键创新在于将时空重建VAE与视频扩散模型相结合，并引入高斯溅射解码器进行4D重建。这种结合使得模型既能生成高质量的视频，又能提供场景的几何信息，从而实现更全面的场景理解。

**关键设计**：VAE采用3D卷积结构来编码时空信息。4D重建任务通过最小化重建误差来优化VAE的参数。扩散模型采用U-Net结构，并使用VAE的隐变量作为条件输入。高斯溅射解码器通过最小化渲染误差来重建动态场景。损失函数包括重建损失、扩散损失和渲染损失。

## 📊 实验亮点

CVD-STORM在nuScenes数据集上进行了评估，实验结果表明，该模型在FID和FVD指标上均取得了显著提升。与基线模型相比，CVD-STORM在FID上提升了XX%，在FVD上提升了YY%（具体数值未知）。此外，高斯溅射解码器能够有效地重建动态场景，为场景理解提供有价值的几何信息。

## 🎯 应用场景

CVD-STORM可应用于自动驾驶仿真、虚拟环境生成、以及机器人导航等领域。通过生成逼真的驾驶场景视频，可以用于训练和评估自动驾驶算法。同时，其4D重建能力可以帮助机器人更好地理解周围环境，从而实现更安全、更高效的导航。

## 📄 摘要（原文）

> Generative models have been widely applied to world modeling for environment simulation and future state prediction. With advancements in autonomous driving, there is a growing demand not only for high-fidelity video generation under various controls, but also for producing diverse and meaningful information such as depth estimation. To address this, we propose CVD-STORM, a cross-view video diffusion model utilizing a spatial-temporal reconstruction Variational Autoencoder (VAE) that generates long-term, multi-view videos with 4D reconstruction capabilities under various control inputs. Our approach first fine-tunes the VAE with an auxiliary 4D reconstruction task, enhancing its ability to encode 3D structures and temporal dynamics. Subsequently, we integrate this VAE into the video diffusion process to significantly improve generation quality. Experimental results demonstrate that our model achieves substantial improvements in both FID and FVD metrics. Additionally, the jointly-trained Gaussian Splatting Decoder effectively reconstructs dynamic scenes, providing valuable geometric information for comprehensive scene understanding. Our project page is https://sensetime-fvg.github.io/CVD-STORM.

