---
layout: default
title: "DMS:Diffusion-Based Multi-Baseline Stereo Generation for Improving Self-Supervised Depth Estimation"
---

# DMS:Diffusion-Based Multi-Baseline Stereo Generation for Improving Self-Supervised Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13091" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13091v1</a>
  <a href="https://arxiv.org/pdf/2508.13091.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13091v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13091v1', 'DMS:Diffusion-Based Multi-Baseline Stereo Generation for Improving Self-Supervised Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zihua Liu, Yizhou Li, Songyan Zhang, Masatoshi Okutomi

**分类**: cs.CV

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出DMS以解决自监督深度估计中的视差模糊问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `自监督学习` `深度估计` `立体匹配` `扩散模型` `光度重建` `计算机视觉` `机器人技术`

## 📋 核心要点

1. 自监督深度估计面临光度重建中的模糊性问题，尤其是在遮挡和框外区域缺失对应像素。
2. 提出DMS方法，通过扩散模型合成新视图，补充缺失像素，增强光度重建的准确性。
3. 实验结果显示，DMS方法在多个基准数据集上实现了最先进的性能，异常值减少高达35%。

## 📝 摘要（中文）

尽管基于学习的监督立体匹配和单目深度估计取得了显著进展，但自监督方法在使用立体图像作为监督信号方面仍然相对较少关注，亟需进一步研究。主要挑战来自于光度重建过程中引入的模糊性，特别是在目标视图的欠定区域（如遮挡和框外区域）中缺失对应像素。为了解决这一问题并建立明确的光度对应关系，本文提出了一种模型无关的方法DMS，该方法利用扩散模型中的几何先验，沿着极线方向合成新视图，并通过方向提示进行引导。我们对稳定扩散模型进行了微调，以模拟关键位置的视角：从左摄像头偏移的左-左视图、从右摄像头偏移的右-右视图，以及左摄像头和右摄像头之间的额外新视图。这些合成视图补充了被遮挡的像素，从而实现了明确的光度重建。DMS是一种无成本的“即插即用”方法，能够无缝增强自监督立体匹配和单目深度估计，仅依赖于未标记的立体图像对进行训练和合成。大量实验表明，该方法有效性显著，能够减少多达35%的异常值，并在多个基准数据集上实现了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决自监督深度估计中由于光度重建引入的模糊性问题，尤其是在遮挡和框外区域缺失对应像素的情况下，现有方法在这些情况下表现不佳。

**核心思路**：DMS方法的核心思路是利用扩散模型的几何先验，通过合成新视图来补充缺失的像素，从而实现更准确的光度重建。该方法通过方向提示引导合成过程，确保生成的视图在几何上合理。

**技术框架**：DMS的整体架构包括对稳定扩散模型的微调，以生成左-左视图、右-右视图和左、右摄像头之间的新视图。合成的视图用于补充原始图像中的缺失像素，形成完整的光度重建。

**关键创新**：DMS的主要创新在于其模型无关性和“即插即用”的特性，使其能够在不需要额外标注数据的情况下，显著提升自监督深度估计的性能。与现有方法相比，DMS能够有效减少因遮挡引起的模糊性。

**关键设计**：在DMS中，关键的参数设置包括扩散模型的微调策略和合成视图的生成过程。损失函数设计上，强调了光度一致性和几何一致性，以确保合成视图的质量和准确性。

## 📊 实验亮点

实验结果表明，DMS方法在多个基准数据集上实现了最先进的性能，异常值减少高达35%。与现有的自监督深度估计方法相比，DMS显著提升了光度重建的准确性，展示了其在实际应用中的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和虚拟现实等，能够在缺乏标注数据的情况下，提升深度估计的准确性和鲁棒性。未来，DMS方法有望在更多实际场景中得到应用，推动自监督学习的发展。

## 📄 摘要（原文）

> While supervised stereo matching and monocular depth estimation have advanced significantly with learning-based algorithms, self-supervised methods using stereo images as supervision signals have received relatively less focus and require further investigation. A primary challenge arises from ambiguity introduced during photometric reconstruction, particularly due to missing corresponding pixels in ill-posed regions of the target view, such as occlusions and out-of-frame areas. To address this and establish explicit photometric correspondences, we propose DMS, a model-agnostic approach that utilizes geometric priors from diffusion models to synthesize novel views along the epipolar direction, guided by directional prompts. Specifically, we finetune a Stable Diffusion model to simulate perspectives at key positions: left-left view shifted from the left camera, right-right view shifted from the right camera, along with an additional novel view between the left and right cameras. These synthesized views supplement occluded pixels, enabling explicit photometric reconstruction. Our proposed DMS is a cost-free, ''plug-and-play'' method that seamlessly enhances self-supervised stereo matching and monocular depth estimation, and relies solely on unlabeled stereo image pairs for both training and synthesizing. Extensive experiments demonstrate the effectiveness of our approach, with up to 35% outlier reduction and state-of-the-art performance across multiple benchmark datasets.

