---
layout: default
title: MapRF: Weakly Supervised Online HD Map Construction via NeRF-Guided Self-Training
---

# MapRF: Weakly Supervised Online HD Map Construction via NeRF-Guided Self-Training

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19527" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19527v1</a>
  <a href="https://arxiv.org/pdf/2511.19527.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19527v1" onclick="toggleFavorite(this, '2511.19527v1', 'MapRF: Weakly Supervised Online HD Map Construction via NeRF-Guided Self-Training')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongyu Lyu, Thomas Monninger, Julie Stephany Berrio Perez, Mao Shan, Zhenxing Ming, Stewart Worrall

**分类**: cs.CV

**发布日期**: 2025-11-24

---

## 💡 一句话要点

**MapRF：基于NeRF引导自训练的弱监督在线高清地图构建**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `高清地图构建` `弱监督学习` `神经辐射场` `自训练` `自动驾驶`

## 📋 核心要点

1. 现有在线高清地图构建方法依赖昂贵的3D地图标注进行训练，限制了其在不同驾驶环境中的泛化能力和可扩展性。
2. MapRF利用2D图像标签，通过NeRF生成高质量伪标签，并以自训练方式迭代优化地图网络，实现弱监督学习。
3. 实验表明，MapRF在Argoverse 2和nuScenes数据集上取得了与全监督方法接近的性能，验证了其有效性。

## 📝 摘要（中文）

本文提出MapRF，一个弱监督框架，仅使用2D图像标签学习构建3D地图。为了生成高质量的伪标签，引入了一个以地图预测为条件的神经辐射场（NeRF）模块，该模块重建视角一致的3D几何和语义信息。这些伪标签随后以自训练的方式迭代地用于细化地图网络，从而在没有额外监督的情况下实现渐进式改进。此外，为了减轻自训练期间的误差累积，提出了一种地图到射线匹配策略，该策略将地图预测与源自2D标签的相机射线对齐。在Argoverse 2和nuScenes数据集上的大量实验表明，MapRF实现了与全监督方法相当的性能，达到了基线的约75%，同时超过了几种仅使用2D标签的方法。这突显了MapRF在为自动驾驶实现可扩展且经济高效的在线高清地图构建方面的潜力。

## 🔬 方法详解

**问题定义**：现有在线高清地图构建方法需要大量的3D标注数据，成本高昂且难以扩展到新的场景。缺乏标注数据成为制约在线高清地图构建的关键瓶颈。

**核心思路**：利用易于获取的2D图像标签作为监督信号，通过NeRF生成高质量的3D伪标签，并采用自训练的方式迭代优化地图网络。核心在于利用NeRF的视角一致性约束，从2D标签中推断出可靠的3D信息。

**技术框架**：MapRF包含以下主要模块：1) 地图预测网络：用于从图像中预测初始的3D地图；2) NeRF模块：以地图预测为条件，重建视角一致的3D几何和语义信息，生成伪标签；3) 自训练模块：使用NeRF生成的伪标签训练地图预测网络；4) 地图到射线匹配模块：将地图预测与2D标签对应的相机射线对齐，减少误差累积。整个流程是一个迭代的自训练过程，不断提升地图预测的精度。

**关键创新**：1) 基于NeRF的伪标签生成：利用NeRF的视角一致性约束，从2D标签中生成高质量的3D伪标签，克服了弱监督学习中标签质量差的问题。2) 地图到射线匹配：通过将地图预测与相机射线对齐，有效缓解了自训练过程中误差累积的问题。

**关键设计**：NeRF模块以地图预测网络的输出作为条件输入，指导NeRF重建3D场景。地图到射线匹配模块使用Huber损失函数来衡量地图预测与相机射线之间的距离，并将其作为正则化项加入到总损失函数中。自训练过程迭代多次，每次迭代都使用更新后的地图预测网络生成新的伪标签。

## 📊 实验亮点

MapRF在Argoverse 2和nuScenes数据集上取得了显著成果，性能接近全监督方法，达到约75%的基线水平，并超越了其他仅使用2D标签的方法。这表明MapRF能够有效利用弱监督信息构建高质量的3D地图，具有很强的实用价值。

## 🎯 应用场景

MapRF可应用于自动驾驶领域，实现低成本、可扩展的在线高清地图构建。该方法降低了对3D标注数据的依赖，使得自动驾驶系统能够快速适应新的驾驶环境，提升感知和决策能力。此外，该技术也可应用于机器人导航、城市建模等领域。

## 📄 摘要（原文）

> Autonomous driving systems benefit from high-definition (HD) maps that provide critical information about road infrastructure. The online construction of HD maps offers a scalable approach to generate local maps from on-board sensors. However, existing methods typically rely on costly 3D map annotations for training, which limits their generalization and scalability across diverse driving environments. In this work, we propose MapRF, a weakly supervised framework that learns to construct 3D maps using only 2D image labels. To generate high-quality pseudo labels, we introduce a novel Neural Radiance Fields (NeRF) module conditioned on map predictions, which reconstructs view-consistent 3D geometry and semantics. These pseudo labels are then iteratively used to refine the map network in a self-training manner, enabling progressive improvement without additional supervision. Furthermore, to mitigate error accumulation during self-training, we propose a Map-to-Ray Matching strategy that aligns map predictions with camera rays derived from 2D labels. Extensive experiments on the Argoverse 2 and nuScenes datasets demonstrate that MapRF achieves performance comparable to fully supervised methods, attaining around 75% of the baseline while surpassing several approaches using only 2D labels. This highlights the potential of MapRF to enable scalable and cost-effective online HD map construction for autonomous driving.

