---
layout: default
title: "CloseUpShot: Close-up Novel View Synthesis from Sparse-views via Point-conditioned Diffusion Model"
---

# CloseUpShot: Close-up Novel View Synthesis from Sparse-views via Point-conditioned Diffusion Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13121" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13121v1</a>
  <a href="https://arxiv.org/pdf/2511.13121.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13121v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.13121v1', 'CloseUpShot: Close-up Novel View Synthesis from Sparse-views via Point-conditioned Diffusion Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuqi Zhang, Guanying Chen, Jiaxing Chen, Chuanyu Fu, Chuan Huang, Shuguang Cui

**分类**: cs.CV

**发布日期**: 2025-11-17

**备注**: Project Link: https://zyqz97.github.io/CloseUpShot/

---

## 💡 一句话要点

**提出CloseUpShot，通过点云条件扩散模型实现稀疏视角下的近距离新视角合成**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `新视角合成` `扩散模型` `三维重建` `点云` `近距离场景`

## 📋 核心要点

1. 现有方法在稀疏视角下进行3D重建和新视角合成时，难以捕捉近距离场景中的精细细节，面临信息严重受限的挑战。
2. CloseUpShot通过点云条件视频扩散，利用分层扭曲、遮挡感知噪声抑制和全局结构引导，提升近距离新视角合成的质量。
3. 实验结果表明，CloseUpShot在近距离新视角合成任务上显著优于现有方法，验证了所提出设计的有效性。

## 📝 摘要（中文）

本文提出了一种名为CloseUpShot的基于扩散模型的框架，用于从稀疏输入视角合成近距离的新视角。针对近距离场景下像素扭曲条件化存在的稀疏性和背景泄露问题，提出了分层扭曲和遮挡感知噪声抑制，以提高视频扩散模型条件化图像的质量和完整性。此外，引入全局结构引导，利用密集融合点云为扩散过程提供一致的几何上下文，以弥补稀疏条件化输入中缺乏全局一致的3D约束。在多个数据集上的大量实验表明，该方法优于现有方法，尤其是在近距离新视角合成方面，验证了设计的有效性。

## 🔬 方法详解

**问题定义**：论文旨在解决从稀疏视角输入重建3D场景并合成新视角的问题，尤其关注近距离场景。现有方法在处理近距离场景时，由于输入信息极度有限，难以捕捉到精细的细节，导致重建质量下降。像素扭曲条件化方法在近距离场景下会面临严重的稀疏性和背景泄露问题，进一步加剧了这一挑战。

**核心思路**：论文的核心思路是利用视频扩散模型强大的时序推理能力，并结合点云提供的几何信息，来提升稀疏视角下的近距离新视角合成质量。通过改进条件化方式，减少稀疏性和背景泄露，并引入全局结构引导，弥补3D约束的不足。

**技术框架**：CloseUpShot框架主要包含以下几个模块：1) 分层扭曲和遮挡感知噪声抑制模块，用于生成高质量的条件化图像；2) 全局结构引导模块，利用密集融合点云提供几何上下文；3) 基于视频扩散模型的生成模块，根据条件化图像和几何上下文生成新视角图像。整体流程是先对输入图像进行预处理，然后通过分层扭曲和噪声抑制生成条件化图像，同时构建全局点云，最后将条件化图像和点云信息输入到视频扩散模型中进行新视角合成。

**关键创新**：论文的关键创新在于：1) 提出了分层扭曲和遮挡感知噪声抑制方法，有效缓解了近距离场景下像素扭曲条件化的稀疏性和背景泄露问题；2) 引入了全局结构引导，利用点云提供全局一致的几何约束，弥补了稀疏视角下3D信息不足的问题。

**关键设计**：分层扭曲的具体实现方式未知。遮挡感知噪声抑制可能通过学习一个mask来区分前景和背景，从而抑制背景噪声。全局结构引导可能通过将点云特征与图像特征进行融合，或者直接将点云作为扩散模型的输入。视频扩散模型可能采用U-Net结构，并使用特定的损失函数进行训练，例如L1损失或感知损失。

## 📊 实验亮点

实验结果表明，CloseUpShot在多个数据集上优于现有方法，尤其是在近距离新视角合成方面表现突出。具体性能提升数据未知，但论文强调该方法在处理近距离场景时，能够生成更清晰、更完整的图像，有效缓解了稀疏性和背景泄露问题，验证了所提出设计的有效性。

## 🎯 应用场景

该研究成果可应用于增强现实、虚拟现实、机器人导航、三维重建、游戏开发等领域。例如，在AR/VR应用中，可以利用少量图像快速生成高质量的近距离场景新视角，提升用户体验。在机器人导航中，可以利用稀疏的视觉信息重建周围环境，辅助机器人进行路径规划和避障。此外，该技术还可用于文物保护，通过少量照片重建文物的三维模型。

## 📄 摘要（原文）

> Reconstructing 3D scenes and synthesizing novel views from sparse input views is a highly challenging task. Recent advances in video diffusion models have demonstrated strong temporal reasoning capabilities, making them a promising tool for enhancing reconstruction quality under sparse-view settings. However, existing approaches are primarily designed for modest viewpoint variations, which struggle in capturing fine-grained details in close-up scenarios since input information is severely limited. In this paper, we present a diffusion-based framework, called CloseUpShot, for close-up novel view synthesis from sparse inputs via point-conditioned video diffusion. Specifically, we observe that pixel-warping conditioning suffers from severe sparsity and background leakage in close-up settings. To address this, we propose hierarchical warping and occlusion-aware noise suppression, enhancing the quality and completeness of the conditioning images for the video diffusion model. Furthermore, we introduce global structure guidance, which leverages a dense fused point cloud to provide consistent geometric context to the diffusion process, to compensate for the lack of globally consistent 3D constraints in sparse conditioning inputs. Extensive experiments on multiple datasets demonstrate that our method outperforms existing approaches, especially in close-up novel view synthesis, clearly validating the effectiveness of our design.

