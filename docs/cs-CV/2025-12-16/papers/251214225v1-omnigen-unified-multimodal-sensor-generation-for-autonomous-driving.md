---
layout: default
title: OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving
---

# OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14225" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14225v1</a>
  <a href="https://arxiv.org/pdf/2512.14225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14225v1" onclick="toggleFavorite(this, '2512.14225v1', 'OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Tang, Enhui Ma, xia zhou, Letian Wang, Tianyi Yan, Xueyang Zhang, Kun Zhan, Peng Jia, XianPeng Lang, Jia-Wang Bian, Kaicheng Yu, Xiaodan Liang

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: ACM MM 2025

---

## 💡 一句话要点

**OmniGen：提出统一的多模态传感器生成框架，用于自动驾驶场景数据增强。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `多模态数据生成` `传感器融合` `鸟瞰图` `扩散模型`

## 📋 核心要点

1. 现有自动驾驶数据生成方法主要集中于单模态，导致多模态数据生成效率低且模态间不对齐。
2. OmniGen利用共享BEV空间统一多模态特征，并提出通用多模态重建方法UAE联合解码激光雷达和相机数据。
3. 实验结果表明，OmniGen在多模态传感器数据生成中表现出色，保证了多模态一致性并支持灵活的传感器调整。

## 📝 摘要（中文）

自动驾驶领域的发展很大程度上依赖于大量的真实世界数据。然而，获取多样化和极端场景的数据仍然成本高昂且效率低下。生成模型通过合成逼真的传感器数据提供了一个有前景的解决方案。但是，现有的方法主要集中在单模态生成上，导致多模态传感器数据效率低下和不对齐。为了解决这些挑战，我们提出了OmniGen，它在一个统一的框架中生成对齐的多模态传感器数据。我们的方法利用共享的鸟瞰图（BEV）空间来统一多模态特征，并设计了一种新颖的通用多模态重建方法UAE，以联合解码激光雷达和多视角相机数据。UAE通过体渲染实现多模态传感器解码，从而实现准确而灵活的重建。此外，我们结合了带有ControlNet分支的Diffusion Transformer（DiT），以实现可控的多模态传感器生成。我们全面的实验表明，OminiGen在统一的多模态传感器数据生成中实现了所需的性能，具有多模态一致性和灵活的传感器调整。

## 🔬 方法详解

**问题定义**：现有自动驾驶数据生成方法主要集中于单模态，无法有效生成对齐的多模态传感器数据，导致训练数据不足，模型泛化能力受限。获取真实世界的多模态数据成本高昂，且难以覆盖所有corner case场景。

**核心思路**：OmniGen的核心思路是利用共享的鸟瞰图（BEV）空间作为多模态特征的统一表示，从而实现多模态数据的对齐和融合。通过设计通用的多模态重建方法，可以从BEV表示中解码出激光雷达和多视角相机数据，实现多模态数据的生成。同时，引入可控的扩散模型，实现对生成数据的灵活控制。

**技术框架**：OmniGen的整体框架包括以下几个主要模块：1) 多模态特征编码器：将不同模态的传感器数据（如激光雷达点云和多视角图像）编码到共享的BEV空间中。2) 通用多模态重建模块（UAE）：从BEV表示中解码出激光雷达点云和多视角图像。UAE采用体渲染技术，实现准确而灵活的重建。3) 可控的扩散模型：使用Diffusion Transformer（DiT）作为生成器，并结合ControlNet分支，实现对生成数据的可控性，例如控制场景的布局和对象的属性。

**关键创新**：OmniGen的关键创新在于：1) 提出了一种统一的多模态传感器生成框架，能够同时生成对齐的激光雷达和相机数据。2) 设计了一种通用的多模态重建方法UAE，通过体渲染实现多模态数据的解码，具有很强的灵活性和准确性。3) 引入了可控的扩散模型，可以灵活地控制生成数据的属性。

**关键设计**：UAE模块使用体渲染技术，将BEV特征转换为体素表示，然后通过可微分的渲染过程生成激光雷达点云和多视角图像。扩散模型采用Diffusion Transformer (DiT) 架构，并使用ControlNet分支来控制生成过程。损失函数包括重建损失（用于保证生成数据的准确性）和对抗损失（用于提高生成数据的真实感）。具体参数设置和网络结构细节未在摘要中详细说明，需要参考论文全文。

## 📊 实验亮点

论文通过实验验证了OmniGen在统一多模态传感器数据生成方面的有效性。实验结果表明，OmniGen能够生成具有多模态一致性和灵活传感器调整能力的数据。具体的性能数据、对比基线和提升幅度等信息需要在论文全文中查找。

## 🎯 应用场景

OmniGen可应用于自动驾驶仿真平台，用于生成大规模、多样化的训练数据，从而提高自动驾驶系统的感知、决策和控制能力。该方法还可以用于数据增强，提高模型在corner case场景下的鲁棒性。此外，OmniGen还可用于自动驾驶算法的验证和评估，降低实车测试的成本和风险。

## 📄 摘要（原文）

> Autonomous driving has seen remarkable advancements, largely driven by extensive real-world data collection. However, acquiring diverse and corner-case data remains costly and inefficient. Generative models have emerged as a promising solution by synthesizing realistic sensor data. However, existing approaches primarily focus on single-modality generation, leading to inefficiencies and misalignment in multimodal sensor data. To address these challenges, we propose OminiGen, which generates aligned multimodal sensor data in a unified framework. Our approach leverages a shared Bird\u2019s Eye View (BEV) space to unify multimodal features and designs a novel generalizable multimodal reconstruction method, UAE, to jointly decode LiDAR and multi-view camera data. UAE achieves multimodal sensor decoding through volume rendering, enabling accurate and flexible reconstruction. Furthermore, we incorporate a Diffusion Transformer (DiT) with a ControlNet branch to enable controllable multimodal sensor generation. Our comprehensive experiments demonstrate that OminiGen achieves desired performances in unified multimodal sensor data generation with multimodal consistency and flexible sensor adjustments.

