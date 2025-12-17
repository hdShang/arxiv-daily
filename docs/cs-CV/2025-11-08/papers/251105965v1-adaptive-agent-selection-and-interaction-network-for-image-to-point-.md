---
layout: default
title: Adaptive Agent Selection and Interaction Network for Image-to-point cloud Registration
---

# Adaptive Agent Selection and Interaction Network for Image-to-point cloud Registration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.05965" class="toolbar-btn" target="_blank">📄 arXiv: 2511.05965v1</a>
  <a href="https://arxiv.org/pdf/2511.05965.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.05965v1" onclick="toggleFavorite(this, '2511.05965v1', 'Adaptive Agent Selection and Interaction Network for Image-to-point cloud Registration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhixin Cheng, Xiaotian Yin, Jiacheng Deng, Bohao Liao, Yujia Chen, Xu Zhou, Baoqun Yin, Tianzhu Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-11-08

**备注**: Accepted by AAAI2026

---

## 💡 一句话要点

**提出自适应Agent选择与交互网络，用于图像到点云的精确配准**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `图像到点云配准` `跨模态学习` `Transformer` `强化学习` `Agent选择` `特征交互` `三维重建`

## 📋 核心要点

1. 现有基于Transformer的图像到点云配准方法易受噪声干扰，导致错误匹配，鲁棒性不足。
2. 提出迭代Agent选择（IAS）和可靠Agent交互（RAI）模块，自适应地选择信息丰富的跨模态特征进行交互。
3. 在RGB-D Scenes v2和7-Scenes数据集上，实验结果表明该方法达到了state-of-the-art的性能。

## 📝 摘要（中文）

本文提出了一种新的跨模态配准框架，用于解决图像到点云配准中噪声干扰和跨模态信息选择困难的问题。该框架包含迭代Agent选择（IAS）模块和可靠Agent交互（RAI）模块。IAS模块利用相位图增强结构特征感知，并采用强化学习原则高效选择可靠的Agent。RAI模块利用这些选定的Agent指导跨模态交互，有效减少错误匹配，提高整体鲁棒性。在RGB-D Scenes v2和7-Scenes基准数据集上的大量实验表明，该方法始终达到最先进的性能。

## 🔬 方法详解

**问题定义**：图像到点云配准旨在建立图像和点云之间的对应关系，是三维重建、定位等任务的关键步骤。现有的基于Transformer的方法在噪声环境下，相似性计算容易出错，导致错误的对应关系。此外，如何有效地选择跨模态中信息量大且相关的特征表示仍然是一个挑战。

**核心思路**：本文的核心思路是通过引入Agent的概念，利用强化学习自适应地选择图像和点云中可靠的、信息量大的特征（即Agent），然后利用这些选定的Agent来指导跨模态特征的交互，从而减少错误匹配，提高配准的鲁棒性和准确性。这种自适应选择和交互的机制能够更好地应对噪声和模态差异带来的挑战。

**技术框架**：该框架主要包含两个模块：迭代Agent选择（IAS）模块和可靠Agent交互（RAI）模块。首先，IAS模块利用相位图增强结构特征的感知能力，并使用强化学习方法选择可靠的Agent。然后，RAI模块利用这些选定的Agent来指导跨模态特征的交互，从而建立更准确的对应关系。整个过程是迭代进行的，不断优化Agent的选择和交互过程。

**关键创新**：该方法最重要的创新点在于提出了自适应的Agent选择和交互机制。与以往方法直接进行跨模态特征融合不同，该方法首先选择可靠的Agent，然后利用这些Agent来指导特征交互，从而减少了噪声和不相关特征的干扰。此外，使用强化学习进行Agent选择也是一个创新点，可以自适应地学习最优的Agent选择策略。

**关键设计**：IAS模块中，相位图用于增强结构特征的感知能力，强化学习算法（具体算法未知）用于学习Agent选择策略。RAI模块的具体交互方式（例如，注意力机制或其他特征融合方法）未知。损失函数的设计也未知，但应该包含配准误差和Agent选择的奖励函数。

## 📊 实验亮点

该方法在RGB-D Scenes v2和7-Scenes数据集上取得了state-of-the-art的性能，表明了其在图像到点云配准任务上的有效性。具体的性能数据和提升幅度未知，但摘要中强调了“consistently achieves state-of-the-art performance”，说明提升是显著且稳定的。

## 🎯 应用场景

该研究成果可应用于机器人导航、三维重建、增强现实等领域。通过更准确的图像到点云配准，机器人可以更好地理解周围环境，实现更精确的定位和导航。在三维重建中，可以提高重建的精度和鲁棒性。在增强现实中，可以实现更逼真的虚拟物体与真实场景的融合。未来，该方法有望扩展到其他跨模态配准任务中。

## 📄 摘要（原文）

> Typical detection-free methods for image-to-point cloud registration leverage transformer-based architectures to aggregate cross-modal features and establish correspondences. However, they often struggle under challenging conditions, where noise disrupts similarity computation and leads to incorrect correspondences. Moreover, without dedicated designs, it remains difficult to effectively select informative and correlated representations across modalities, thereby limiting the robustness and accuracy of registration. To address these challenges, we propose a novel cross-modal registration framework composed of two key modules: the Iterative Agents Selection (IAS) module and the Reliable Agents Interaction (RAI) module. IAS enhances structural feature awareness with phase maps and employs reinforcement learning principles to efficiently select reliable agents. RAI then leverages these selected agents to guide cross-modal interactions, effectively reducing mismatches and improving overall robustness. Extensive experiments on the RGB-D Scenes v2 and 7-Scenes benchmarks demonstrate that our method consistently achieves state-of-the-art performance.

