---
layout: default
title: PFAvatar: Pose-Fusion 3D Personalized Avatar Reconstruction from Real-World Outfit-of-the-Day Photos
---

# PFAvatar: Pose-Fusion 3D Personalized Avatar Reconstruction from Real-World Outfit-of-the-Day Photos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12935" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12935v2</a>
  <a href="https://arxiv.org/pdf/2511.12935.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12935v2" onclick="toggleFavorite(this, '2511.12935v2', 'PFAvatar: Pose-Fusion 3D Personalized Avatar Reconstruction from Real-World Outfit-of-the-Day Photos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dianbing Xi, Guoyuan An, Jingsen Zhu, Zhijian Liu, Yuan Liu, Ruiyuan Zhang, Jiayuan Lu, Yuchi Huo, Rui Wang

**分类**: cs.CV, cs.AI, cs.GR

**发布日期**: 2025-11-17 (更新: 2025-11-18)

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**PFAvatar：从日常照片中进行姿态融合的个性化3D头像重建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)** **支柱六：视频提取与匹配 (Video Extraction & Matching)**

**关键词**: `3D头像重建` `神经辐射场` `扩散模型` `姿态估计` `少量样本学习` `个性化建模` `虚拟试穿`

## 📋 核心要点

1. 现有方法在从OOTD照片重建3D头像时，通常依赖于图像分割和3D资产组装，容易导致不一致和细节丢失。
2. PFAvatar通过姿态感知的扩散模型直接对全身外观进行建模，避免了图像分割，并引入条件先验保持损失以提升少量样本学习效果。
3. 实验表明，PFAvatar在重建质量、细节保留和遮挡处理方面优于现有方法，并且个性化速度提升了48倍。

## 📝 摘要（中文）

本文提出了一种名为PFAvatar（Pose-Fusion Avatar）的新方法，该方法可以从日常穿搭（OOTD）照片中重建高质量的3D头像，这些照片通常具有不同的姿势、遮挡和复杂的背景。该方法包括两个阶段：（1）从少量OOTD示例中微调一个姿态感知的扩散模型；（2）提炼一个由神经辐射场（NeRF）表示的3D头像。在第一阶段，与之前将图像分割成资产（例如，服装、配饰）以进行3D组装的方法不同（这种方法容易出现不一致），我们避免了分解，而是直接对全身外观进行建模。通过集成用于姿态估计的预训练ControlNet和一个新颖的条件先验保持损失（CPPL），我们的方法能够实现端到端学习精细细节，同时减轻少量样本训练中的语言漂移。我们的方法仅需5分钟即可完成个性化，与以前的方法相比，速度提高了48倍。在第二阶段，我们引入了一种基于NeRF的头像表示，该表示通过规范的SMPL-X空间采样和多分辨率3D-SDS进行优化。与基于网格的表示相比，我们的连续辐射场可以保留高频纹理（例如，头发），并通过透射率正确处理遮挡。实验表明，PFAvatar在重建保真度、细节保留以及对遮挡/截断的鲁棒性方面优于最先进的方法，从而推进了从真实世界OOTD相册中生成实用3D头像的技术。此外，重建的3D头像支持虚拟试穿、动画和人体视频重演等下游应用，进一步证明了我们方法的多功能性和实用价值。

## 🔬 方法详解

**问题定义**：从日常穿搭照片（OOTD）中重建高质量的个性化3D头像。现有方法通常将图像分割成不同的服装和配饰，然后进行3D组装，这种方法容易产生不一致性，并且难以捕捉精细的细节，尤其是在存在遮挡的情况下。此外，现有方法通常需要大量的训练数据和较长的训练时间。

**核心思路**：PFAvatar的核心思路是避免图像分割，直接对全身外观进行建模，并利用姿态信息来指导3D重建。通过姿态感知的扩散模型，可以学习到不同姿势下的全身外观分布。同时，引入条件先验保持损失（CPPL）来缓解少量样本训练中的语言漂移问题，从而提高重建质量。

**技术框架**：PFAvatar包含两个主要阶段：（1）姿态感知扩散模型微调阶段：利用少量OOTD照片，微调一个预训练的姿态感知扩散模型，使其能够生成特定个体的全身外观图像。（2）NeRF头像提炼阶段：将微调后的扩散模型作为教师模型，利用多分辨率3D-SDS损失，训练一个基于NeRF的3D头像模型。该NeRF模型以规范的SMPL-X空间进行采样，从而更好地处理姿态变化。

**关键创新**：PFAvatar的关键创新在于：（1）避免了图像分割，直接对全身外观进行建模，从而避免了不一致性问题。（2）引入了条件先验保持损失（CPPL），缓解了少量样本训练中的语言漂移问题。（3）利用多分辨率3D-SDS损失，优化基于NeRF的3D头像，从而更好地保留高频纹理和处理遮挡。

**关键设计**：在姿态感知扩散模型微调阶段，使用了预训练的ControlNet进行姿态估计，并将姿态信息作为条件输入到扩散模型中。条件先验保持损失（CPPL）的设计旨在保持微调后的扩散模型与预训练模型之间的语义一致性，从而避免语言漂移。在NeRF头像提炼阶段，使用了SMPL-X模型作为规范空间，并采用多分辨率3D-SDS损失来优化NeRF模型，从而更好地保留高频纹理和处理遮挡。

## 📊 实验亮点

实验结果表明，PFAvatar在重建保真度、细节保留以及对遮挡/截断的鲁棒性方面优于现有方法。与现有方法相比，PFAvatar的个性化速度提高了48倍，仅需5分钟即可完成。在细节保留方面，PFAvatar能够更好地重建头发等高频纹理。在遮挡处理方面，PFAvatar能够更准确地重建被遮挡的区域。

## 🎯 应用场景

PFAvatar重建的3D头像具有广泛的应用前景，包括虚拟试穿、游戏角色定制、虚拟社交、动画制作和人体视频重演等。该技术可以帮助用户创建个性化的虚拟形象，并在各种虚拟环境中进行互动和体验。此外，该技术还可以应用于电商领域，帮助用户在线试穿服装，提高购物体验。

## 📄 摘要（原文）

> We propose PFAvatar (Pose-Fusion Avatar), a new method that reconstructs high-quality 3D avatars from Outfit of the Day(OOTD) photos, which exhibit diverse poses, occlusions, and complex backgrounds. Our method consists of two stages: (1) fine-tuning a pose-aware diffusion model from few-shot OOTD examples and (2) distilling a 3D avatar represented by a neural radiance field (NeRF). In the first stage, unlike previous methods that segment images into assets (e.g., garments, accessories) for 3D assembly, which is prone to inconsistency, we avoid decomposition and directly model the full-body appearance. By integrating a pre-trained ControlNet for pose estimation and a novel Condition Prior Preservation Loss (CPPL), our method enables end-to-end learning of fine details while mitigating language drift in few-shot training. Our method completes personalization in just 5 minutes, achieving a 48x speed-up compared to previous approaches. In the second stage, we introduce a NeRF-based avatar representation optimized by canonical SMPL-X space sampling and Multi-Resolution 3D-SDS. Compared to mesh-based representations that suffer from resolution-dependent discretization and erroneous occluded geometry, our continuous radiance field can preserve high-frequency textures (e.g., hair) and handle occlusions correctly through transmittance. Experiments demonstrate that PFAvatar outperforms state-of-the-art methods in terms of reconstruction fidelity, detail preservation, and robustness to occlusions/truncations, advancing practical 3D avatar generation from real-world OOTD albums. In addition, the reconstructed 3D avatar supports downstream applications such as virtual try-on, animation, and human video reenactment, further demonstrating the versatility and practical value of our approach.

