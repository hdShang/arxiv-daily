---
layout: default
title: FaithFusion: Harmonizing Reconstruction and Generation via Pixel-wise Information Gain
---

# FaithFusion: Harmonizing Reconstruction and Generation via Pixel-wise Information Gain

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21113" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21113v1</a>
  <a href="https://arxiv.org/pdf/2511.21113.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21113v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21113v1', 'FaithFusion: Harmonizing Reconstruction and Generation via Pixel-wise Information Gain')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: YuAn Wang, Xiaofan Li, Chi Huang, Wenhao Zhang, Hao Li, Bosheng Wang, Xun Sun, Jun Wang

**分类**: cs.CV

**发布日期**: 2025-11-26

**备注**: 16 pages, 10 figures

**🔗 代码/项目**: [GITHUB](https://github.com/wangyuanbiubiubiu/FaithFusion)

---

## 💡 一句话要点

**FaithFusion：提出基于像素级信息增益的3DGS-扩散融合框架，解决可控驾驶场景重建与生成问题。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `3D场景重建` `3D场景生成` `扩散模型` `3DGS` `信息增益` `自动驾驶` `可控生成`

## 📋 核心要点

1. 现有方法在融合3DGS和扩散模型时，缺乏像素级的3D一致性编辑标准，导致过度修复和几何漂移。
2. FaithFusion利用像素级期望信息增益（EIG）作为统一策略，指导扩散模型并提炼编辑结果到3DGS。
3. 实验表明，FaithFusion在Waymo数据集上取得了SOTA性能，即使在较大车道偏移下也能保持良好的FID。

## 📝 摘要（中文）

在可控驾驶场景重建和3D场景生成中，保持几何保真度并在大视角变换下合成视觉上合理的表观至关重要。然而，基于几何的3DGS和表观驱动的扩散模型的有效融合面临着内在的挑战，因为缺乏像素级的、3D一致的编辑标准通常会导致过度恢复和几何漂移。为了解决这些问题，我们引入了FaithFusion，这是一个由像素级期望信息增益（EIG）驱动的3DGS-扩散融合框架。EIG作为连贯时空合成的统一策略：它引导扩散作为空间先验来细化高不确定性区域，同时其像素级权重将编辑结果提炼回3DGS。由此产生的即插即用系统无需额外的先验条件和结构修改。在Waymo数据集上的大量实验表明，我们的方法在NTA-IoU、NTL-IoU和FID方面都达到了SOTA性能，即使在6米的车道偏移下也能保持107.47的FID。

## 🔬 方法详解

**问题定义**：论文旨在解决可控驾驶场景重建和3D场景生成中，几何保真度和视觉逼真度难以兼顾的问题。现有方法在融合3DGS（3D Gaussian Splatting）和扩散模型时，缺乏像素级别的、3D一致的编辑标准，容易导致过度修复，引入伪影，甚至造成几何结构的漂移，影响最终重建或生成结果的质量。

**核心思路**：论文的核心思路是利用像素级的期望信息增益（Expected Information Gain, EIG）作为桥梁，将3DGS和扩散模型进行有效融合。EIG能够量化每个像素的不确定性，并指导扩散模型优先修复不确定性高的区域，同时将扩散模型的编辑结果以像素级权重的方式反向提炼到3DGS中，从而实现几何和外观的协同优化。

**技术框架**：FaithFusion框架主要包含以下几个阶段：1) 初始化3DGS场景；2) 使用扩散模型生成图像，并计算每个像素的EIG；3) 基于EIG指导扩散模型进行图像修复，提高不确定性区域的质量；4) 将修复后的图像信息反向传播到3DGS，更新3DGS的参数，从而优化场景的几何和外观。这个过程迭代进行，直到场景达到期望的质量。

**关键创新**：论文最重要的创新在于提出了使用像素级EIG作为3DGS和扩散模型融合的统一标准。与现有方法相比，FaithFusion能够更精细地控制扩散模型的编辑过程，避免过度修复和几何漂移，从而提高重建和生成结果的质量。此外，该方法是一个即插即用的系统，无需额外的先验条件和结构修改，具有良好的通用性。

**关键设计**：EIG的计算方式未知，论文中可能使用了某种特定的计算方法来估计每个像素的不确定性。此外，如何将扩散模型的编辑结果有效地反向传播到3DGS，可能涉及到特定的损失函数设计和优化策略。具体的网络结构和参数设置未知，但可以推测使用了标准的3DGS和扩散模型架构。

## 📊 实验亮点

FaithFusion在Waymo数据集上进行了广泛的实验，结果表明其在NTA-IoU、NTL-IoU和FID等指标上均达到了SOTA性能。即使在6米的车道偏移下，FaithFusion仍然能够保持107.47的FID，表明其具有很强的鲁棒性和泛化能力。这些实验结果充分证明了FaithFusion的有效性和优越性。

## 🎯 应用场景

FaithFusion在自动驾驶、虚拟现实、游戏开发等领域具有广泛的应用前景。它可以用于生成逼真的驾驶场景，训练自动驾驶系统，也可以用于创建沉浸式的虚拟环境和游戏世界。该研究的实际价值在于提高了3D场景重建和生成质量，为相关应用提供了更可靠的数据基础。未来，该技术有望进一步发展，实现更高效、更智能的3D内容创作。

## 📄 摘要（原文）

> In controllable driving-scene reconstruction and 3D scene generation, maintaining geometric fidelity while synthesizing visually plausible appearance under large viewpoint shifts is crucial. However, effective fusion of geometry-based 3DGS and appearance-driven diffusion models faces inherent challenges, as the absence of pixel-wise, 3D-consistent editing criteria often leads to over-restoration and geometric drift. To address these issues, we introduce \textbf{FaithFusion}, a 3DGS-diffusion fusion framework driven by pixel-wise Expected Information Gain (EIG). EIG acts as a unified policy for coherent spatio-temporal synthesis: it guides diffusion as a spatial prior to refine high-uncertainty regions, while its pixel-level weighting distills the edits back into 3DGS. The resulting plug-and-play system is free from extra prior conditions and structural modifications.Extensive experiments on the Waymo dataset demonstrate that our approach attains SOTA performance across NTA-IoU, NTL-IoU, and FID, maintaining an FID of 107.47 even at 6 meters lane shift. Our code is available at https://github.com/wangyuanbiubiubiu/FaithFusion.

