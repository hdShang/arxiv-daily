---
layout: default
title: Monocular Depth Guided Occlusion-Aware Disparity Refinement via Semi-supervised Learning in Laparoscopic Images
---

# Monocular Depth Guided Occlusion-Aware Disparity Refinement via Semi-supervised Learning in Laparoscopic Images

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08178" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08178v1</a>
  <a href="https://arxiv.org/pdf/2505.08178.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08178v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08178v1', 'Monocular Depth Guided Occlusion-Aware Disparity Refinement via Semi-supervised Learning in Laparoscopic Images')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziteng Liu, Dongdong He, Chenghong Zhang, Wenpeng Gao, Yili Fu

**分类**: cs.CV

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出深度引导的遮挡感知视差精炼网络以解决腹腔镜图像中的视差估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视差估计` `深度学习` `腹腔镜图像` `遮挡感知` `光流分析` `半监督学习` `医疗图像处理`

## 📋 核心要点

1. 现有方法在腹腔镜图像的视差估计中面临遮挡和标注数据稀缺的挑战，影响了精度和鲁棒性。
2. 本研究提出DGORNet，通过单目深度信息和位置嵌入模块来精炼视差图，并引入光流差异损失以增强动态场景的鲁棒性。
3. 实验结果显示，DGORNet在SCARED数据集上显著降低了EPE和RMSE，尤其在复杂的遮挡和无纹理区域表现优异。

## 📝 摘要（中文）

遮挡和标注手术数据的稀缺是立体腹腔镜图像视差估计中的重大挑战。为了解决这些问题，本研究提出了一种深度引导的遮挡感知视差精炼网络（DGORNet），通过利用不受遮挡影响的单目深度信息来精炼视差图。引入了位置嵌入模块（PE），提供明确的空间上下文，增强了网络定位和精炼特征的能力。此外，提出了一种光流差异损失（OFDLoss），利用视频帧间的时间连续性来提高动态手术场景中的鲁棒性。实验结果表明，DGORNet在SCARED数据集上在端点误差（EPE）和均方根误差（RMSE）方面优于现有最先进的方法，尤其是在遮挡和无纹理区域。消融研究确认了位置嵌入和光流差异损失的贡献，突显了它们在提高空间和时间一致性方面的作用。

## 🔬 方法详解

**问题定义**：本论文旨在解决腹腔镜图像中视差估计的遮挡问题和标注数据稀缺的问题。现有方法在处理这些挑战时，往往无法提供足够的精度和鲁棒性。

**核心思路**：论文提出的DGORNet通过引入单目深度信息来指导视差图的精炼，同时利用位置嵌入模块增强空间上下文信息，从而提高特征的定位和精炼能力。

**技术框架**：DGORNet的整体架构包括多个模块，主要包括位置嵌入模块、视差精炼模块和光流差异损失模块。位置嵌入模块提供空间上下文，视差精炼模块负责生成精炼的视差图，而光流差异损失模块则利用时间连续性来处理未标注数据。

**关键创新**：本研究的关键创新在于引入了位置嵌入模块和光流差异损失，这两者共同提升了网络在动态手术场景中的空间和时间一致性，与现有方法相比，显著提高了视差估计的准确性。

**关键设计**：在网络设计中，位置嵌入模块通过显式的空间信息增强特征表示，光流差异损失则通过计算视频帧间的光流差异来优化未标注数据的学习过程。这些设计使得DGORNet在处理复杂场景时表现出更高的鲁棒性和准确性。

## 📊 实验亮点

实验结果表明，DGORNet在SCARED数据集上相较于最先进的方法，EPE和RMSE分别降低了XX%和YY%。尤其在遮挡和无纹理区域，DGORNet的表现显著优于对比基线，验证了其在复杂场景中的有效性。

## 🎯 应用场景

该研究的潜在应用领域主要集中在医疗图像处理，尤其是腹腔镜手术中的视差估计。通过提高视差估计的准确性，DGORNet能够为手术导航、三维重建和机器人手术提供更可靠的支持，进而提升手术的安全性和有效性。未来，该技术有望扩展到其他类型的医疗影像分析和计算机视觉任务中。

## 📄 摘要（原文）

> Occlusion and the scarcity of labeled surgical data are significant challenges in disparity estimation for stereo laparoscopic images. To address these issues, this study proposes a Depth Guided Occlusion-Aware Disparity Refinement Network (DGORNet), which refines disparity maps by leveraging monocular depth information unaffected by occlusion. A Position Embedding (PE) module is introduced to provide explicit spatial context, enhancing the network's ability to localize and refine features. Furthermore, we introduce an Optical Flow Difference Loss (OFDLoss) for unlabeled data, leveraging temporal continuity across video frames to improve robustness in dynamic surgical scenes. Experiments on the SCARED dataset demonstrate that DGORNet outperforms state-of-the-art methods in terms of End-Point Error (EPE) and Root Mean Squared Error (RMSE), particularly in occlusion and texture-less regions. Ablation studies confirm the contributions of the Position Embedding and Optical Flow Difference Loss, highlighting their roles in improving spatial and temporal consistency. These results underscore DGORNet's effectiveness in enhancing disparity estimation for laparoscopic surgery, offering a practical solution to challenges in disparity estimation and data limitations.

