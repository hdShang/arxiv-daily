---
layout: default
title: "OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving"
---

# OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14225" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14225v1</a>
  <a href="https://arxiv.org/pdf/2512.14225.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14225v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14225v1', 'OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tao Tang, Enhui Ma, xia zhou, Letian Wang, Tianyi Yan, Xueyang Zhang, Kun Zhan, Peng Jia, XianPeng Lang, Jia-Wang Bian, Kaicheng Yu, Xiaodan Liang

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: ACM MM 2025

---

## 💡 一句话要点

**OmniGen：提出统一多模态传感器生成框架，用于自动驾驶场景数据增强。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `多模态生成` `传感器仿真` `鸟瞰图` `扩散模型` `体渲染` `数据增强`

## 📋 核心要点

1. 现有自动驾驶数据采集成本高昂，且难以覆盖所有corner case，单模态生成方法效率低且易造成多模态数据不对齐。
2. OmniGen利用共享BEV空间统一多模态特征，并提出通用多模态重建方法UAE，通过体渲染联合解码激光雷达和多视角相机数据。
3. 实验结果表明，OmniGen在统一多模态传感器数据生成中表现出色，实现了多模态一致性和灵活的传感器调整。

## 📝 摘要（中文）

自动驾驶领域的发展很大程度上依赖于大量的真实世界数据。然而，获取多样化和极端场景数据仍然成本高昂且效率低下。生成模型通过合成逼真的传感器数据，为解决这一问题提供了有希望的方案。然而，现有的方法主要集中在单模态生成上，导致多模态传感器数据的不一致和效率低下。为了解决这些挑战，我们提出了OmniGen，它在一个统一的框架中生成对齐的多模态传感器数据。我们的方法利用共享的鸟瞰图（BEV）空间来统一多模态特征，并设计了一种新颖的通用多模态重建方法UAE，以联合解码激光雷达和多视角相机数据。UAE通过体渲染实现多模态传感器解码，从而实现准确而灵活的重建。此外，我们还结合了带有ControlNet分支的Diffusion Transformer（DiT），以实现可控的多模态传感器生成。全面的实验表明，OminiGen在统一的多模态传感器数据生成中实现了理想的性能，具有多模态一致性和灵活的传感器调整能力。

## 🔬 方法详解

**问题定义**：现有自动驾驶数据生成方法主要集中于单模态，导致多模态数据之间缺乏一致性，并且生成效率较低。获取足够数量的、具有多样性和覆盖极端场景的数据仍然是一个挑战。因此，需要一种能够高效生成对齐的多模态传感器数据的方法，以支持自动驾驶系统的训练和验证。

**核心思路**：OmniGen的核心思路是利用共享的鸟瞰图（BEV）空间作为多模态特征的统一表示，从而实现多模态数据之间的对齐。通过设计一种通用的多模态重建方法（UAE），可以联合解码激光雷达和多视角相机数据，实现准确且灵活的多模态传感器数据生成。此外，引入可控的扩散模型，允许用户控制生成过程，从而生成特定场景和条件下的数据。

**技术框架**：OmniGen的整体框架包括以下几个主要模块：1) 多模态特征编码器：将来自不同传感器（如激光雷达和多视角相机）的数据编码到共享的BEV空间中。2) 通用多模态重建模块（UAE）：利用体渲染技术，从BEV特征中解码出多模态传感器数据。3) 可控的扩散模型（DiT + ControlNet）：用于生成BEV特征，并允许用户通过ControlNet控制生成过程。整个流程首先将多模态数据编码到BEV空间，然后使用扩散模型生成BEV特征，最后通过UAE解码生成多模态传感器数据。

**关键创新**：OmniGen的关键创新在于：1) 统一的多模态表示：通过共享的BEV空间，实现了多模态特征的对齐和融合。2) 通用多模态重建方法（UAE）：利用体渲染技术，实现了从BEV特征到多模态传感器数据的准确重建，避免了传统方法中对每个模态单独建模的复杂性。3) 可控的扩散模型：允许用户控制生成过程，从而生成特定场景和条件下的数据。

**关键设计**：UAE模块使用体渲染技术，通过学习一个体密度场来表示场景，然后通过光线投射算法将BEV特征渲染成多模态传感器数据。扩散模型采用Diffusion Transformer (DiT) 架构，并引入ControlNet分支，允许用户通过输入控制信号（如场景布局、目标位置等）来控制生成过程。损失函数包括重建损失（用于保证生成数据的准确性）和对抗损失（用于提高生成数据的真实感）。具体的参数设置和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14225v1/imgs/teaser2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14225v1/imgs/framework_2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14225v1/x1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了OmniGen在多模态传感器数据生成方面的有效性。实验结果表明，OmniGen能够生成具有多模态一致性和高真实感的传感器数据，并且可以通过ControlNet实现对生成过程的灵活控制。具体的性能数据和对比基线在论文中有详细描述，证明了OmniGen相比于现有方法的优越性。

## 🎯 应用场景

OmniGen可应用于自动驾驶系统的仿真测试、数据增强和模型训练。通过生成多样化的、具有多模态一致性的传感器数据，可以有效提高自动驾驶系统在各种复杂场景下的鲁棒性和安全性。此外，该方法还可以用于自动驾驶算法的验证和评估，加速自动驾驶技术的研发进程。

## 📄 摘要（原文）

> Autonomous driving has seen remarkable advancements, largely driven by extensive real-world data collection. However, acquiring diverse and corner-case data remains costly and inefficient. Generative models have emerged as a promising solution by synthesizing realistic sensor data. However, existing approaches primarily focus on single-modality generation, leading to inefficiencies and misalignment in multimodal sensor data. To address these challenges, we propose OminiGen, which generates aligned multimodal sensor data in a unified framework. Our approach leverages a shared Bird\u2019s Eye View (BEV) space to unify multimodal features and designs a novel generalizable multimodal reconstruction method, UAE, to jointly decode LiDAR and multi-view camera data. UAE achieves multimodal sensor decoding through volume rendering, enabling accurate and flexible reconstruction. Furthermore, we incorporate a Diffusion Transformer (DiT) with a ControlNet branch to enable controllable multimodal sensor generation. Our comprehensive experiments demonstrate that OminiGen achieves desired performances in unified multimodal sensor data generation with multimodal consistency and flexible sensor adjustments.

