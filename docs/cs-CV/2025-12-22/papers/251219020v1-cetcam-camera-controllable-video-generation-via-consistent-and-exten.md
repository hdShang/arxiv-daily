---
layout: default
title: "CETCAM: Camera-Controllable Video Generation via Consistent and Extensible Tokenization"
---

# CETCAM: Camera-Controllable Video Generation via Consistent and Extensible Tokenization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19020" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19020v1</a>
  <a href="https://arxiv.org/pdf/2512.19020.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19020v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19020v1', 'CETCAM: Camera-Controllable Video Generation via Consistent and Extensible Tokenization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zelin Zhao, Xinyu Gong, Bangya Liu, Ziyang Song, Jun Zhang, Suhui Wu, Yongxin Chen, Hao Zhang

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-22

**🔗 代码/项目**: [PROJECT_PAGE](https://sjtuytc.github.io/CETCam_project_page.github.io/)

---

## 💡 一句话要点

**CETCAM：通过一致且可扩展的Token化实现相机可控的视频生成**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `相机可控视频生成` `视频扩散模型` `几何感知Token化` `深度估计` `几何一致性`

## 📋 核心要点

1. 现有相机可控视频生成方法依赖相机位姿标注，难以扩展到大型动态数据集，且与深度估计不一致，导致训练-测试差异。
2. CETCAM通过一致且可扩展的Token化方案，将深度和相机参数转换为几何感知的Token，无需相机标注即可实现相机控制。
3. 实验表明，CETCAM在几何一致性、时间稳定性和视觉真实感方面均达到SOTA，并能适应图像修复和布局控制等额外模态。

## 📝 摘要（中文）

本文提出了一种相机可控的视频生成框架CETCAM，该框架通过一致且可扩展的Token化方案消除了对相机标注的需求。CETCAM利用几何基础模型（如VGGT）估计深度和相机参数，并将它们转换为统一的、几何感知的Token。这些Token通过轻量级的上下文块无缝集成到预训练的视频扩散骨干网络中。CETCAM分两个阶段进行训练，首先从各种原始视频数据中学习鲁棒的相机可控性，然后使用精心策划的高保真数据集细化精细的视觉质量。大量实验表明，CETCAM在多个基准测试中表现出最先进的几何一致性、时间稳定性和视觉真实感。此外，CETCAM对额外的控制模态（包括图像修复和布局控制）表现出强大的适应性，突出了其在相机控制之外的灵活性。

## 🔬 方法详解

**问题定义**：现有的相机可控视频生成方法主要依赖于带有相机位姿标注的数据集进行训练。然而，获取大规模、高质量的相机位姿标注非常困难，尤其是在动态场景中。此外，这些标注通常与深度估计不一致，导致训练和测试阶段存在差异，影响生成视频的质量和可控性。

**核心思路**：CETCAM的核心思路是利用几何基础模型（如VGGT）来估计视频中的深度和相机参数，并将这些几何信息转换为统一的、几何感知的Token。通过这种方式，模型可以在没有显式相机标注的情况下学习相机控制，从而避免了对大规模标注数据的依赖，并提高了模型的泛化能力。

**技术框架**：CETCAM的整体框架包含以下几个主要模块：1) 几何信息提取模块：使用VGGT等几何基础模型估计视频的深度和相机参数。2) Token化模块：将提取的几何信息转换为统一的、几何感知的Token。3) 上下文融合模块：使用轻量级的上下文块将几何Token集成到预训练的视频扩散骨干网络中。4) 视频生成模块：利用扩散模型生成最终的视频。CETCAM采用两阶段训练策略：首先，在大量未标注的原始视频数据上训练模型，使其学习鲁棒的相机可控性；然后，使用高质量的标注数据集对模型进行微调，以提高生成视频的视觉质量。

**关键创新**：CETCAM的关键创新在于提出了一种一致且可扩展的Token化方案，该方案能够将深度和相机参数等几何信息有效地编码为Token，并无缝集成到预训练的视频扩散模型中。这种方法避免了对相机标注的依赖，提高了模型的泛化能力和可控性。与现有方法相比，CETCAM能够生成具有更高几何一致性和时间稳定性的视频。

**关键设计**：CETCAM的关键设计包括：1) 使用VGGT作为几何信息提取器，以获得准确的深度和相机参数估计。2) 设计了一种几何感知的Token化方案，该方案能够有效地编码深度和相机参数。3) 使用轻量级的上下文块将几何Token集成到视频扩散骨干网络中，以避免引入过多的计算开销。4) 采用两阶段训练策略，以提高模型的鲁棒性和视觉质量。损失函数方面，采用了标准的扩散模型损失函数，并根据需要添加了正则化项，以提高生成视频的几何一致性和时间稳定性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19020v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19020v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19020v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

CETCAM在多个基准测试中取得了最先进的结果，证明了其在几何一致性、时间稳定性和视觉真实感方面的优越性。例如，在相机轨迹控制任务中，CETCAM生成的视频与目标相机轨迹的偏差显著小于现有方法。此外，CETCAM还展示了对图像修复和布局控制等额外模态的强大适应性，进一步证明了其灵活性和通用性。

## 🎯 应用场景

CETCAM具有广泛的应用前景，例如电影制作、游戏开发、虚拟现实和增强现实等领域。它可以用于生成具有精确相机控制的逼真视频内容，从而为用户提供更加沉浸式的体验。此外，CETCAM还可以用于数据增强，生成更多样化的训练数据，以提高其他计算机视觉模型的性能。未来，该技术有望应用于自动驾驶、机器人导航等领域。

## 📄 摘要（原文）

> Achieving precise camera control in video generation remains challenging, as existing methods often rely on camera pose annotations that are difficult to scale to large and dynamic datasets and are frequently inconsistent with depth estimation, leading to train-test discrepancies. We introduce CETCAM, a camera-controllable video generation framework that eliminates the need for camera annotations through a consistent and extensible tokenization scheme. CETCAM leverages recent advances in geometry foundation models, such as VGGT, to estimate depth and camera parameters and converts them into unified, geometry-aware tokens. These tokens are seamlessly integrated into a pretrained video diffusion backbone via lightweight context blocks. Trained in two progressive stages, CETCAM first learns robust camera controllability from diverse raw video data and then refines fine-grained visual quality using curated high-fidelity datasets. Extensive experiments across multiple benchmarks demonstrate state-of-the-art geometric consistency, temporal stability, and visual realism. Moreover, CETCAM exhibits strong adaptability to additional control modalities, including inpainting and layout control, highlighting its flexibility beyond camera control. The project page is available at https://sjtuytc.github.io/CETCam_project_page.github.io/.

