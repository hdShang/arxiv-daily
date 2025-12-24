---
layout: default
title: "Depth Any Panoramas: A Foundation Model for Panoramic Depth Estimation"
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

**提出全景深度估计基础模型DAP，提升跨场景距离的泛化能力。**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱七：动作重定向 (Motion Retargeting)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `全景深度估计` `深度学习` `基础模型` `数据闭环` `伪标签`

## 📋 核心要点

1. 现有全景深度估计方法在处理不同场景距离和领域泛化性方面存在不足，尤其是在真实场景中。
2. 论文提出一种数据闭环范式，结合多种数据源并使用伪标签方法缩小领域差距，提升模型泛化能力。
3. 实验结果表明，该模型在多个基准测试中表现出色，并在真实场景中实现了鲁棒和稳定的深度预测。

## 📝 摘要（中文）

本文提出了一种全景度量深度基础模型，该模型能够泛化到各种场景距离。我们探索了一种数据闭环范式，从数据构建和框架设计的角度出发。我们通过结合公共数据集、来自UE5模拟器的高质量合成数据、文本到图像模型以及来自网络的真实全景图像，收集了一个大规模数据集。为了减少室内/室外和合成/真实数据之间的领域差距，我们引入了一个三阶段伪标签生成流程，为未标记图像生成可靠的ground truth。在模型方面，我们采用DINOv3-Large作为骨干网络，因为它具有强大的预训练泛化能力，并引入了一个即插即用的范围掩码头、以清晰度为中心的优化和以几何为中心的优化，以提高对不同距离的鲁棒性并加强跨视图的几何一致性。在多个基准测试（例如，Stanford2D3D、Matterport3D和Deep360）上的实验表明，该模型具有强大的性能和零样本泛化能力，尤其是在各种真实场景中具有鲁棒和稳定的度量预测。

## 🔬 方法详解

**问题定义**：全景深度估计旨在从单张全景图像中预测场景的深度信息。现有方法在处理不同场景距离（近距离、远距离）以及室内外场景的泛化能力上存在挑战。此外，合成数据与真实数据之间的领域差距也是一个重要问题，限制了模型在真实场景中的应用效果。

**核心思路**：论文的核心思路是构建一个大规模、多样化的全景数据集，并设计一个能够有效利用这些数据的深度估计模型。通过数据闭环的方式，不断迭代优化数据集和模型，从而提升模型的泛化能力和鲁棒性。具体来说，利用伪标签技术来弥合合成数据和真实数据之间的差距，并采用几何一致性约束来提高深度预测的准确性。

**技术框架**：整体框架包含三个主要阶段：数据收集与增强、伪标签生成和模型训练。数据收集阶段结合了公共数据集、UE5合成数据和网络爬取的真实全景图像。伪标签生成阶段采用三阶段流程，逐步为未标记图像生成可靠的深度标签。模型训练阶段使用DINOv3-Large作为骨干网络，并添加了范围掩码头、清晰度优化和几何优化模块。

**关键创新**：论文的关键创新在于数据闭环范式和伪标签生成流程。数据闭环范式强调数据集和模型之间的相互促进，通过不断迭代优化来提升性能。伪标签生成流程能够有效利用未标记的真实数据，缩小领域差距，从而提高模型的泛化能力。此外，范围掩码头和几何优化模块也进一步提升了深度预测的准确性和一致性。

**关键设计**：在数据方面，UE5合成数据生成使用了随机纹理和光照，增加了数据的多样性。伪标签生成流程包括初始预测、置信度过滤和几何一致性优化三个阶段。模型方面，范围掩码头用于区分不同距离的物体，清晰度优化用于提高深度图的清晰度，几何优化则通过最小化相邻像素深度差异来保证几何一致性。损失函数包括深度损失、梯度损失和几何一致性损失。

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

实验结果表明，该模型在Stanford2D3D、Matterport3D和Deep360等多个基准测试中取得了优异的性能，尤其是在真实场景中表现出强大的鲁棒性和稳定性。与现有方法相比，该模型在零样本泛化能力方面有显著提升，能够直接应用于未见过的场景。

## 🎯 应用场景

该研究成果可广泛应用于机器人导航、虚拟现实、增强现实、自动驾驶等领域。高质量的全景深度估计能够为这些应用提供更准确的环境感知信息，从而提升系统的性能和用户体验。未来，该模型可以进一步扩展到其他模态数据，例如RGB-D全景图像，以实现更全面的场景理解。

## 📄 摘要（原文）

> In this work, we present a panoramic metric depth foundation model that generalizes across diverse scene distances. We explore a data-in-the-loop paradigm from the view of both data construction and framework design. We collect a large-scale dataset by combining public datasets, high-quality synthetic data from our UE5 simulator and text-to-image models, and real panoramic images from the web. To reduce domain gaps between indoor/outdoor and synthetic/real data, we introduce a three-stage pseudo-label curation pipeline to generate reliable ground truth for unlabeled images. For the model, we adopt DINOv3-Large as the backbone for its strong pre-trained generalization, and introduce a plug-and-play range mask head, sharpness-centric optimization, and geometry-centric optimization to improve robustness to varying distances and enforce geometric consistency across views. Experiments on multiple benchmarks (e.g., Stanford2D3D, Matterport3D, and Deep360) demonstrate strong performance and zero-shot generalization, with particularly robust and stable metric predictions in diverse real-world scenes. The project page can be found at: \href{https://insta360-research-team.github.io/DAP_website/} {https://insta360-research-team.github.io/DAP\_website/}

