---
layout: default
title: Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation
---

# Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16913" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16913v1</a>
  <a href="https://arxiv.org/pdf/2512.16913.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16913v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16913v1', 'Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xin Lin, Meixi Song, Dizhe Zhang, Wenxuan Lu, Haodong Li, Bo Du, Ming-Hsuan Yang, Truong Nguyen, Lu Qi

**分类**: cs.CV

**发布日期**: 2025-12-18

**备注**: Project Page: https://insta360-research-team.github.io/DAP_website/

**🔗 代码/项目**: [PROJECT_PAGE](https://insta360-research-team.github.io/DAP_website/) | [PROJECT_PAGE](https://insta360-research-team.github.io/DAP)

---

## 💡 一句话要点

**提出全景深度基础模型以解决多场景深度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全景深度估计` `深度学习` `伪标签整理` `几何一致性` `数据驱动`

## 📋 核心要点

1. 现有的深度估计方法在处理多样化场景和不同距离时存在泛化能力不足的问题。
2. 论文提出了一种基于DINOv3-Large的全景深度估计模型，结合伪标签整理和优化策略以提升鲁棒性。
3. 在多个基准测试上，模型展示了强大的性能，尤其在真实场景中实现了稳定的度量预测。

## 📝 摘要（中文）

本研究提出了一种全景度量深度基础模型，能够在多样化场景距离下进行泛化。我们从数据构建和框架设计的角度探索了数据循环的范式。通过结合公共数据集、来自UE5模拟器的高质量合成数据、文本到图像模型以及网络上的真实全景图像，收集了大规模数据集。为减少室内/室外和合成/真实数据之间的领域差距，我们引入了三阶段伪标签整理管道，以生成可靠的无标签图像的真实标签。我们采用DINOv3-Large作为主干网络，并引入了即插即用的范围掩码头、以清晰度为中心的优化和以几何为中心的优化，以提高对不同距离的鲁棒性，并在视图之间强制几何一致性。实验结果表明，在多个基准测试上表现出强大的性能和零-shot泛化能力，尤其是在多样化的真实场景中，度量预测表现出特别的鲁棒性和稳定性。

## 🔬 方法详解

**问题定义**：本论文旨在解决全景深度估计中的泛化能力不足问题，现有方法在不同场景和距离下的表现不够稳定，导致深度估计的准确性下降。

**核心思路**：论文提出了一种数据驱动的循环范式，通过构建大规模数据集和引入伪标签整理管道，增强模型对不同场景的适应性和鲁棒性。

**技术框架**：整体架构包括数据收集、伪标签生成和模型训练三个主要阶段。数据收集阶段结合了公共数据集和合成数据，伪标签生成阶段通过三阶段管道确保标签的可靠性，模型训练阶段则采用DINOv3-Large作为主干网络。

**关键创新**：最重要的创新在于引入了即插即用的范围掩码头和优化策略，增强了模型对不同距离的适应性，并确保了几何一致性，这在现有方法中较为少见。

**关键设计**：在模型设计中，采用了清晰度和几何一致性为中心的优化策略，确保了在多样化场景下的鲁棒性，同时通过伪标签整理管道生成高质量的训练数据。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16913v1/x2.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16913v1/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16913v1/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在多个基准测试（如Stanford2D3D、Matterport3D和Deep360）中，模型展示了优异的性能，特别是在真实场景中的度量预测表现出强大的鲁棒性和稳定性，零-shot泛化能力显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和机器人导航等场景，能够为这些领域提供高精度的深度信息，提升用户体验和系统性能。未来，该模型的应用可能推动全景图像处理和三维重建技术的发展。

## 📄 摘要（原文）

> In this work, we present a panoramic metric depth foundation model that generalizes across diverse scene distances. We explore a data-in-the-loop paradigm from the view of both data construction and framework design. We collect a large-scale dataset by combining public datasets, high-quality synthetic data from our UE5 simulator and text-to-image models, and real panoramic images from the web. To reduce domain gaps between indoor/outdoor and synthetic/real data, we introduce a three-stage pseudo-label curation pipeline to generate reliable ground truth for unlabeled images. For the model, we adopt DINOv3-Large as the backbone for its strong pre-trained generalization, and introduce a plug-and-play range mask head, sharpness-centric optimization, and geometry-centric optimization to improve robustness to varying distances and enforce geometric consistency across views. Experiments on multiple benchmarks (e.g., Stanford2D3D, Matterport3D, and Deep360) demonstrate strong performance and zero-shot generalization, with particularly robust and stable metric predictions in diverse real-world scenes. The project page can be found at: \href{https://insta360-research-team.github.io/DAP_website/} {https://insta360-research-team.github.io/DAP\_website/}

