---
layout: default
title: OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving
---

# OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14225" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14225</a>
  <a href="https://arxiv.org/pdf/2512.14225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14225" onclick="toggleFavorite(this, '2512.14225', 'OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Tang, Enhui Ma, xia zhou, Letian Wang, Tianyi Yan, Xueyang Zhang, Kun Zhan, Peng Jia, XianPeng Lang, Jia-Wang Bian, Kaicheng Yu, Xiaodan Liang

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**OmniGen：提出统一的多模态传感器生成框架，用于自动驾驶场景。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `多模态生成` `传感器数据` `鸟瞰图` `扩散模型`

## 📋 核心要点

1. 现有自动驾驶数据采集成本高昂，且难以覆盖所有corner case，单模态生成方法效率低且易导致多模态数据不对齐。
2. OmniGen利用共享BEV空间统一多模态特征，并提出通用多模态重建方法UAE，实现激光雷达和多视角相机数据的联合解码。
3. 通过集成ControlNet分支的Diffusion Transformer，OmniGen实现了可控的多模态传感器数据生成，并保证了多模态一致性。

## 📝 摘要（中文）

自动驾驶的发展很大程度上依赖于大量的真实世界数据。然而，获取多样化和极端情况的数据仍然成本高昂且效率低下。生成模型通过合成逼真的传感器数据提供了一个有前景的解决方案。但是，现有方法主要集中在单模态生成上，导致多模态传感器数据效率低下和不对齐。为了解决这些挑战，我们提出了OmniGen，它在一个统一的框架中生成对齐的多模态传感器数据。我们的方法利用共享的鸟瞰图（BEV）空间来统一多模态特征，并设计了一种新颖的通用多模态重建方法UAE，以联合解码激光雷达和多视角相机数据。UAE通过体渲染实现多模态传感器解码，从而实现准确和灵活的重建。此外，我们结合了带有ControlNet分支的Diffusion Transformer（DiT），以实现可控的多模态传感器生成。我们的综合实验表明，OminiGen在统一的多模态传感器数据生成中实现了期望的性能，具有多模态一致性和灵活的传感器调整。

## 🔬 方法详解

**问题定义**：现有自动驾驶生成模型主要集中于单模态传感器数据的生成，这导致了多模态数据之间缺乏一致性，并且生成效率较低。获取真实世界中多样化的、极端情况下的多模态数据成本高昂，阻碍了自动驾驶系统的发展。因此，如何高效且一致地生成多模态传感器数据是亟待解决的问题。

**核心思路**：OmniGen的核心思路是利用一个统一的框架来生成对齐的多模态传感器数据。具体来说，它首先将不同模态的数据投影到共享的鸟瞰图（BEV）空间中，从而实现多模态特征的统一表示。然后，通过提出的通用多模态重建方法（UAE），联合解码激光雷达和多视角相机数据。这种统一的表示和解码方式能够保证多模态数据之间的一致性，并提高生成效率。

**技术框架**：OmniGen的整体框架包含以下几个主要模块：1) 多模态特征编码器：将不同模态的传感器数据（如激光雷达点云和多视角图像）编码到BEV空间中。2) 通用多模态重建模块（UAE）：基于体渲染技术，从BEV特征中重建出激光雷达点云和多视角图像。3) Diffusion Transformer (DiT) with ControlNet：用于可控的多模态传感器数据生成，ControlNet分支允许用户指定生成数据的属性。

**关键创新**：OmniGen的关键创新点在于：1) 提出了一个统一的多模态传感器生成框架，能够同时生成激光雷达和多视角相机数据，保证了多模态数据之间的一致性。2) 设计了一种通用的多模态重建方法（UAE），通过体渲染技术实现多模态传感器数据的解码，具有较高的重建精度和灵活性。3) 引入了带有ControlNet分支的Diffusion Transformer，实现了可控的多模态传感器数据生成。

**关键设计**：UAE模块的关键设计在于使用体渲染技术进行多模态传感器数据的解码。具体来说，它将BEV特征作为体素的属性，然后通过光线投射算法，将体素属性渲染成激光雷达点云和多视角图像。ControlNet分支的设计允许用户通过控制信号来调整生成数据的属性，例如车辆的位置、速度和朝向。损失函数方面，可能采用了L1损失、L2损失或感知损失等，以保证生成数据的质量和真实感。（具体损失函数细节未知）

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14225/imgs/teaser2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14225/imgs/framework_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14225/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过综合实验验证了OmniGen的有效性。实验结果表明，OmniGen能够在统一的多模态传感器数据生成中实现期望的性能，具有多模态一致性和灵活的传感器调整能力。具体的性能数据和对比基线未知，但摘要强调了OmniGen在多模态一致性和可控性方面的优势。

## 🎯 应用场景

OmniGen在自动驾驶领域具有广泛的应用前景。它可以用于生成大量的训练数据，从而提高自动驾驶系统的性能和鲁棒性。此外，OmniGen还可以用于模拟各种极端情况，例如恶劣天气、复杂交通等，从而帮助自动驾驶系统更好地应对这些挑战。该研究的成果有助于推动自动驾驶技术的进一步发展和应用。

## 📄 摘要（原文）

> Autonomous driving has seen remarkable advancements, largely driven by extensive real-world data collection. However, acquiring diverse and corner-case data remains costly and inefficient. Generative models have emerged as a promising solution by synthesizing realistic sensor data. However, existing approaches primarily focus on single-modality generation, leading to inefficiencies and misalignment in multimodal sensor data. To address these challenges, we propose OminiGen, which generates aligned multimodal sensor data in a unified framework. Our approach leverages a shared Bird\u2019s Eye View (BEV) space to unify multimodal features and designs a novel generalizable multimodal reconstruction method, UAE, to jointly decode LiDAR and multi-view camera data. UAE achieves multimodal sensor decoding through volume rendering, enabling accurate and flexible reconstruction. Furthermore, we incorporate a Diffusion Transformer (DiT) with a ControlNet branch to enable controllable multimodal sensor generation. Our comprehensive experiments demonstrate that OminiGen achieves desired performances in unified multimodal sensor data generation with multimodal consistency and flexible sensor adjustments.

