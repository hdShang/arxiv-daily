---
layout: default
title: Hybrid-Domain Adaptative Representation Learning for Gaze Estimation
---

# Hybrid-Domain Adaptative Representation Learning for Gaze Estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.13222" class="toolbar-btn" target="_blank">📄 arXiv: 2511.13222v1</a>
  <a href="https://arxiv.org/pdf/2511.13222.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.13222v1" onclick="toggleFavorite(this, '2511.13222v1', 'Hybrid-Domain Adaptative Representation Learning for Gaze Estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qida Tan, Hongyu Yang, Wenchao Du

**分类**: cs.CV

**发布日期**: 2025-11-17

**备注**: AAAI2026

**🔗 代码/项目**: [GITHUB](https://github.com/da60266/HARL)

---

## 💡 一句话要点

**提出混合领域自适应表示学习以解决注视估计中的跨域问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `注视估计` `领域适应` `表示学习` `图像处理` `深度学习`

## 📋 核心要点

1. 现有的注视估计方法在跨域评估中表现不佳，受到表情、佩戴物和图像质量等因素的干扰。
2. 本文提出的HARL框架通过无监督领域适应，从低质量面部图像中提取注视相关表示，减少了计算和推理成本。
3. 在EyeDiap、MPIIFaceGaze和Gaze360数据集上的实验结果显示，我们的方法分别达到了5.02°、3.36°和9.26°的准确性，表现优异。

## 📝 摘要（中文）

基于外观的注视估计旨在从单张面部图像中预测准确的3D注视方向，近年来取得了显著进展。然而，大多数方法在跨域评估中表现不佳，受到与注视无关因素的干扰，如表情、佩戴物和图像质量。为了解决这一问题，本文提出了一种新颖的混合领域自适应表示学习框架（HARL），利用多源混合数据集学习稳健的注视表示。具体而言，我们通过无监督领域适应方式对齐从高质量近眼图像提取的特征，以从低质量面部图像中解耦注视相关表示。此外，我们分析了头部姿态的影响，并设计了一个简单而高效的稀疏图融合模块，以探索注视方向与头部姿态之间的几何约束，从而获得密集且稳健的注视表示。大量实验表明，我们的方法在多个数据集上达到了最先进的准确性。

## 🔬 方法详解

**问题定义**：本文旨在解决基于外观的注视估计在跨域评估中性能下降的问题，现有方法在面对不同环境和条件时，容易受到与注视无关因素的干扰。

**核心思路**：我们提出的HARL框架通过利用多源混合数据集，采用无监督领域适应的方法，从低质量图像中提取出注视相关的特征表示，旨在增强模型的鲁棒性。

**技术框架**：HARL框架主要包括两个模块：特征对齐模块和稀疏图融合模块。特征对齐模块负责从高质量图像中提取特征并与低质量图像进行对齐，而稀疏图融合模块则用于探索注视方向与头部姿态之间的几何关系。

**关键创新**：本文的主要创新在于通过无监督方式实现低质量图像与高质量图像特征的对齐，显著降低了对标注数据的依赖，同时引入稀疏图融合模块来增强注视表示的几何约束。

**关键设计**：我们在模型中采用了特定的损失函数来优化特征对齐过程，并设计了稀疏图融合的结构，以有效捕捉注视方向与头部姿态之间的关系。

## 📊 实验亮点

实验结果表明，HARL框架在EyeDiap、MPIIFaceGaze和Gaze360数据集上分别达到了5.02°、3.36°和9.26°的注视估计准确性，显著优于现有方法，展示了在跨数据集评估中的竞争力。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、虚拟现实和增强现实等场景，能够提升系统对用户注视行为的理解和响应能力。随着技术的进步，HARL框架有望在智能设备和辅助技术中发挥重要作用，推动注视估计技术的广泛应用。

## 📄 摘要（原文）

> Appearance-based gaze estimation, aiming to predict accurate 3D gaze direction from a single facial image, has made promising progress in recent years. However, most methods suffer significant performance degradation in cross-domain evaluation due to interference from gaze-irrelevant factors, such as expressions, wearables, and image quality. To alleviate this problem, we present a novel Hybrid-domain Adaptative Representation Learning (shorted by HARL) framework that exploits multi-source hybrid datasets to learn robust gaze representation. More specifically, we propose to disentangle gaze-relevant representation from low-quality facial images by aligning features extracted from high-quality near-eye images in an unsupervised domain-adaptation manner, which hardly requires any computational or inference costs. Additionally, we analyze the effect of head-pose and design a simple yet efficient sparse graph fusion module to explore the geometric constraint between gaze direction and head-pose, leading to a dense and robust gaze representation. Extensive experiments on EyeDiap, MPIIFaceGaze, and Gaze360 datasets demonstrate that our approach achieves state-of-the-art accuracy of $\textbf{5.02}^{\circ}$ and $\textbf{3.36}^{\circ}$, and $\textbf{9.26}^{\circ}$ respectively, and present competitive performances through cross-dataset evaluation. The code is available at https://github.com/da60266/HARL.

