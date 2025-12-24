---
layout: default
title: "M3Depth: Wavelet-Enhanced Depth Estimation on Mars via Mutual Boosting of Dual-Modal Data"
---

# M3Depth: Wavelet-Enhanced Depth Estimation on Mars via Mutual Boosting of Dual-Modal Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14159" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14159v2</a>
  <a href="https://arxiv.org/pdf/2505.14159.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14159v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14159v2', 'M3Depth: Wavelet-Enhanced Depth Estimation on Mars via Mutual Boosting of Dual-Modal Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junjie Li, Jiawei Wang, Miyu Li, Yu Liu, Yumei Wang, Haitao Xu

**分类**: cs.CV, cs.RO

**发布日期**: 2025-05-20 (更新: 2025-06-14)

---

## 💡 一句话要点

**提出M3Depth以解决火星环境下深度估计问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `深度估计` `火星探测` `小波变换` `多模态数据` `一致性损失` `互助机制` `机器人导航`

## 📋 核心要点

1. 现有的深度估计方法在火星稀疏纹理和缺乏几何约束的环境中表现不佳，导致深度图精度不足。
2. M3Depth模型结合小波变换卷积核和一致性损失，旨在提高火星地形的深度估计准确性。
3. 在合成火星数据集上，M3Depth的深度估计准确性比其他先进方法提高了16%，显示出良好的应用前景。

## 📝 摘要（中文）

深度估计在火星探测任务中的障碍规避和导航中具有重要潜力。与传统的立体匹配方法相比，基于学习的立体深度估计提供了一种数据驱动的方法，可以从立体图像对中推断出密集且精确的深度图。然而，这些方法在稀疏纹理和缺乏几何约束的环境中（如火星的非结构化地形）表现不佳。为了解决这些挑战，我们提出了M3Depth，这是一种专为火星探测车设计的深度估计模型。该模型结合了基于小波变换的卷积核，有效捕捉低频响应，并扩展感受野。此外，我们引入了一种一致性损失，明确建模深度图与表面法线图之间的互补关系，利用表面法线作为几何约束以提高深度估计的准确性。实验结果表明，M3Depth在合成火星数据集上的深度估计准确性比其他先进方法提高了16%。

## 🔬 方法详解

**问题定义**：论文要解决火星探测环境中深度估计的准确性问题，现有方法在稀疏纹理和缺乏几何约束的情况下表现不佳，导致深度图的精度不足。

**核心思路**：M3Depth模型通过引入基于小波变换的卷积核，专注于捕捉低频特征，并结合一致性损失来增强深度图与表面法线图之间的关系，从而提高深度估计的准确性。

**技术框架**：M3Depth的整体架构包括三个主要模块：小波变换卷积模块、表面法线一致性损失模块和像素级细化模块。小波模块用于捕捉低频特征，一致性损失模块用于建模深度与法线之间的关系，而细化模块则通过互助机制迭代优化深度和法线预测。

**关键创新**：最重要的技术创新点在于引入了小波变换卷积核和一致性损失，这使得模型能够有效应对火星环境的挑战，与现有方法相比，能够更好地捕捉低频特征并利用几何约束。

**关键设计**：模型设计中，损失函数包括深度损失和一致性损失，网络结构采用了多层卷积以增强特征提取能力，细化模块则通过互助机制实现深度和法线的共同优化。

## 📊 实验亮点

实验结果显示，M3Depth在合成火星数据集上的深度估计准确性比其他先进方法提高了16%，这表明该模型在处理火星特有的稀疏纹理环境中具有显著优势，展现出强大的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括火星探测任务中的自动导航和障碍物规避，能够为未来的火星探测车提供更精确的环境感知能力，提升探测效率和安全性。随着火星探索任务的不断推进，M3Depth模型的实际价值和影响将愈加显著。

## 📄 摘要（原文）

> Depth estimation plays a great potential role in obstacle avoidance and navigation for further Mars exploration missions. Compared to traditional stereo matching, learning-based stereo depth estimation provides a data-driven approach to infer dense and precise depth maps from stereo image pairs. However, these methods always suffer performance degradation in environments with sparse textures and lacking geometric constraints, such as the unstructured terrain of Mars. To address these challenges, we propose M3Depth, a depth estimation model tailored for Mars rovers. Considering the sparse and smooth texture of Martian terrain, which is primarily composed of low-frequency features, our model incorporates a convolutional kernel based on wavelet transform that effectively captures low-frequency response and expands the receptive field. Additionally, we introduce a consistency loss that explicitly models the complementary relationship between depth map and surface normal map, utilizing the surface normal as a geometric constraint to enhance the accuracy of depth estimation. Besides, a pixel-wise refinement module with mutual boosting mechanism is designed to iteratively refine both depth and surface normal predictions. Experimental results on synthetic Mars datasets with depth annotations show that M3Depth achieves a 16% improvement in depth estimation accuracy compared to other state-of-the-art methods in depth estimation. Furthermore, the model demonstrates strong applicability in real-world Martian scenarios, offering a promising solution for future Mars exploration missions.

