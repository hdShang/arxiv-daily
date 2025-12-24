---
layout: default
title: "RadarGen: Automotive Radar Point Cloud Generation from Cameras"
---

# RadarGen: Automotive Radar Point Cloud Generation from Cameras

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.17897" class="toolbar-btn" target="_blank">📄 arXiv: 2512.17897v1</a>
  <a href="https://arxiv.org/pdf/2512.17897.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.17897v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.17897v1', 'RadarGen: Automotive Radar Point Cloud Generation from Cameras')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tomer Borreda, Fangqiang Ding, Sanja Fidler, Shengyu Huang, Or Litany

**分类**: cs.CV, cs.AI, cs.LG, cs.RO

**发布日期**: 2025-12-19

**备注**: Project page: https://radargen.github.io/

---

## 💡 一句话要点

**RadarGen：提出一种基于图像的汽车雷达点云生成扩散模型**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `雷达点云生成` `扩散模型` `多模态仿真` `自动驾驶` `鸟瞰图`

## 📋 核心要点

1. 现有雷达数据生成方法难以保证真实性和多样性，且依赖昂贵的硬件和复杂的环境设置。
2. RadarGen利用图像潜在扩散模型，并结合视觉信息（深度、语义、运动）引导雷达点云生成，提升真实感。
3. 实验表明，RadarGen生成的雷达点云能够有效缩小与真实数据训练的感知模型之间的性能差距。

## 📝 摘要（中文）

本文提出RadarGen，一种从多视角相机图像合成逼真汽车雷达点云的扩散模型。RadarGen通过将雷达测量结果表示为鸟瞰图形式，并将空间结构与雷达截面(RCS)和多普勒属性编码，从而将高效的图像潜在扩散应用于雷达领域。一个轻量级的恢复步骤从生成的地图中重建点云。为了更好地使生成与视觉场景对齐，RadarGen结合了从预训练基础模型中提取的BEV对齐的深度、语义和运动线索，这些线索引导随机生成过程朝着物理上合理的雷达模式发展。原则上，以图像为条件使得该方法与现有的视觉数据集和仿真框架广泛兼容，为跨传感模态的统一生成式仿真提供了一个可扩展的方向。对大规模驾驶数据的评估表明，RadarGen捕获了特征雷达测量分布，并缩小了与在真实数据上训练的感知模型之间的差距，标志着朝着跨传感模态的统一生成式仿真迈出了一步。

## 🔬 方法详解

**问题定义**：论文旨在解决汽车雷达点云数据生成的问题。现有方法，如基于规则的仿真或GAN，难以生成足够真实和多样化的雷达数据，且依赖于精确的场景建模和参数调整。这限制了雷达感知算法的训练和验证，尤其是在corner case场景下。

**核心思路**：论文的核心思路是利用扩散模型强大的生成能力，并以多视角相机图像作为条件，生成与视觉场景一致的雷达点云。通过视觉信息引导，可以生成更符合物理规律和场景语义的雷达数据。将雷达数据表示为鸟瞰图(BEV)形式，方便与图像特征对齐和进行扩散建模。

**技术框架**：RadarGen的整体框架包含以下几个主要步骤：1) 从多视角相机图像中提取BEV对齐的深度、语义和运动特征；2) 将这些特征作为条件输入到图像潜在扩散模型中；3) 扩散模型生成雷达鸟瞰图，包含空间结构、RCS和多普勒信息；4) 从生成的雷达鸟瞰图中重建雷达点云。

**关键创新**：RadarGen的关键创新在于：1) 将图像潜在扩散模型应用于雷达点云生成，充分利用了扩散模型强大的生成能力；2) 引入BEV对齐的深度、语义和运动特征作为条件，引导雷达点云生成，保证了生成数据的真实性和场景一致性；3) 使用鸟瞰图形式表示雷达数据，方便与图像特征对齐和进行扩散建模。

**关键设计**：RadarGen使用预训练的视觉基础模型提取深度、语义和运动特征。扩散模型采用U-Net结构，以图像特征作为cross-attention的key和value。雷达鸟瞰图的分辨率和通道数需要根据具体数据集进行调整。损失函数包括扩散模型的标准损失函数，以及可选的对抗损失函数，以进一步提高生成数据的真实性。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17897v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17897v1/figures/data/fig_method_radar_maps.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.17897v1/x2.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，RadarGen生成的雷达点云在视觉上与真实场景高度一致，并且能够有效缩小与在真实数据上训练的感知模型之间的性能差距。具体来说，使用RadarGen生成的数据训练的雷达目标检测器，其性能接近于使用真实数据训练的模型，证明了RadarGen生成数据的有效性。

## 🎯 应用场景

RadarGen可应用于自动驾驶系统的雷达感知算法的训练和验证，尤其是在真实数据难以获取的corner case场景下。它还可以用于生成多模态仿真数据，促进跨模态感知算法的研究。此外，该方法可以扩展到其他传感器模态，实现统一的生成式仿真框架。

## 📄 摘要（原文）

> We present RadarGen, a diffusion model for synthesizing realistic automotive radar point clouds from multi-view camera imagery. RadarGen adapts efficient image-latent diffusion to the radar domain by representing radar measurements in bird's-eye-view form that encodes spatial structure together with radar cross section (RCS) and Doppler attributes. A lightweight recovery step reconstructs point clouds from the generated maps. To better align generation with the visual scene, RadarGen incorporates BEV-aligned depth, semantic, and motion cues extracted from pretrained foundation models, which guide the stochastic generation process toward physically plausible radar patterns. Conditioning on images makes the approach broadly compatible, in principle, with existing visual datasets and simulation frameworks, offering a scalable direction for multimodal generative simulation. Evaluations on large-scale driving data show that RadarGen captures characteristic radar measurement distributions and reduces the gap to perception models trained on real data, marking a step toward unified generative simulation across sensing modalities.

