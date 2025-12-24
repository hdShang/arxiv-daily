---
layout: default
title: "MF-LPR$^2$: Multi-Frame License Plate Image Restoration and Recognition using Optical Flow"
---

# MF-LPR$^2$: Multi-Frame License Plate Image Restoration and Recognition using Optical Flow

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14797" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14797v1</a>
  <a href="https://arxiv.org/pdf/2508.14797.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14797v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14797v1', 'MF-LPR$^2$: Multi-Frame License Plate Image Restoration and Recognition using Optical Flow')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kihyun Na, Junseok Oh, Youngkwan Cho, Bumjin Kim, Sungmin Cho, Jinyoung Choi, Injung Kim

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-19

**备注**: Accepted for publication in Computer Vision and Image Understanding (CVIU), 2025

**期刊**: Computer Vision and Image Understanding, Vol. 256, May 2025, 104361

**DOI**: [10.1016/j.cviu.2025.104361](https://doi.org/10.1016/j.cviu.2025.104361)

---

## 💡 一句话要点

**提出MF-LPR$^2$以解决低质量车牌图像恢复与识别问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `车牌识别` `图像恢复` `光流估计` `多帧处理` `深度学习`

## 📋 核心要点

1. 现有的车牌识别方法在处理低质量图像时存在显著不足，尤其是在运动模糊和光照变化下，识别准确率低。
2. MF-LPR$^2$通过对齐和聚合相邻帧，利用光流估计来恢复和识别车牌图像，避免了依赖预训练模型的局限性。
3. 实验结果显示，MF-LPR$^2$在多个指标上超越了现有模型，识别准确率达到86.44%，显著提升了识别性能。

## 📝 摘要（中文）

车牌识别（LPR）在交通执法、犯罪调查和监控中至关重要。然而，行车记录仪图像中的车牌区域常常受到低分辨率、运动模糊和眩光的影响，导致准确识别变得困难。现有的生成模型依赖于预训练的先验知识，无法可靠地恢复这些低质量图像，常常引入严重的伪影和失真。为了解决这个问题，本文提出了一种新颖的多帧车牌恢复与识别框架MF-LPR$^2$，通过对齐和聚合相邻帧来解决低质量图像中的模糊性，而不是依赖预训练知识。我们采用了先进的光流估计器，并设计了精确的算法来检测和纠正错误的光流估计，从而提高图像质量和识别准确性，同时保留输入图像的证据内容。此外，我们构建了一个新的真实车牌识别（RLPR）数据集来评估MF-LPR$^2$。实验结果表明，MF-LPR$^2$在PSNR、SSIM和LPIPS等指标上显著优于八个最新的恢复模型，识别准确率达到86.44%。

## 🔬 方法详解

**问题定义**：本文旨在解决低质量车牌图像的恢复与识别问题，现有方法在处理低分辨率、运动模糊和眩光等情况下表现不佳，常常导致识别错误和图像失真。

**核心思路**：MF-LPR$^2$的核心思路是通过对齐和聚合相邻帧来恢复车牌图像，而不是依赖于预训练的生成模型，从而有效减少伪影和失真。

**技术框架**：该框架包括光流估计模块、图像对齐模块和图像恢复模块。光流估计模块负责计算相邻帧之间的运动信息，图像对齐模块则利用光流信息对图像进行对齐，最后通过恢复模块生成高质量的车牌图像。

**关键创新**：MF-LPR$^2$的创新在于其通过光流估计实现的帧间对齐和聚合，克服了传统方法对预训练模型的依赖，显著提高了恢复效果和识别准确率。

**关键设计**：在技术细节上，论文设计了精确的光流估计算法，并结合时空一致性来检测和纠正错误的光流估计。此外，损失函数的设计也考虑了图像质量和识别准确性之间的平衡。

## 📊 实验亮点

实验结果显示，MF-LPR$^2$在PSNR、SSIM和LPIPS等指标上显著优于八个最新的恢复模型，识别准确率达到86.44%，远超最佳单帧LPR（14.04%）和多帧LPR（82.55%），展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能交通系统、自动停车管理、公共安全监控等。通过提高车牌识别的准确性，MF-LPR$^2$能够有效支持交通执法和犯罪调查，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> License plate recognition (LPR) is important for traffic law enforcement, crime investigation, and surveillance. However, license plate areas in dash cam images often suffer from low resolution, motion blur, and glare, which make accurate recognition challenging. Existing generative models that rely on pretrained priors cannot reliably restore such poor-quality images, frequently introducing severe artifacts and distortions. To address this issue, we propose a novel multi-frame license plate restoration and recognition framework, MF-LPR$^2$, which addresses ambiguities in poor-quality images by aligning and aggregating neighboring frames instead of relying on pretrained knowledge. To achieve accurate frame alignment, we employ a state-of-the-art optical flow estimator in conjunction with carefully designed algorithms that detect and correct erroneous optical flow estimations by leveraging the spatio-temporal consistency inherent in license plate image sequences. Our approach enhances both image quality and recognition accuracy while preserving the evidential content of the input images. In addition, we constructed a novel Realistic LPR (RLPR) dataset to evaluate MF-LPR$^2$. The RLPR dataset contains 200 pairs of low-quality license plate image sequences and high-quality pseudo ground-truth images, reflecting the complexities of real-world scenarios. In experiments, MF-LPR$^2$ outperformed eight recent restoration models in terms of PSNR, SSIM, and LPIPS by significant margins. In recognition, MF-LPR$^2$ achieved an accuracy of 86.44%, outperforming both the best single-frame LPR (14.04%) and the multi-frame LPR (82.55%) among the eleven baseline models. The results of ablation studies confirm that our filtering and refinement algorithms significantly contribute to these improvements.

