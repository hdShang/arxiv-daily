---
layout: default
title: Enhancing Monocular Height Estimation via Sparse LiDAR-Guided Correction
---

# Enhancing Monocular Height Estimation via Sparse LiDAR-Guided Correction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.06905" class="toolbar-btn" target="_blank">📄 arXiv: 2505.06905v3</a>
  <a href="https://arxiv.org/pdf/2505.06905.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.06905v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.06905v3', 'Enhancing Monocular Height Estimation via Sparse LiDAR-Guided Correction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jian Song, Hongruixuan Chen, Naoto Yokoya

**分类**: cs.CV, eess.IV

**发布日期**: 2025-05-11 (更新: 2025-12-08)

**备注**: Accepted for publication in the ISPRS Journal of Photogrammetry and Remote Sensing

**DOI**: [10.1016/j.isprsjprs.2025.12.004](https://doi.org/10.1016/j.isprsjprs.2025.12.004)

---

## 💡 一句话要点

**提出稀疏LiDAR引导修正以提升单目高度估计精度**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `单目高度估计` `LiDAR数据` `深度学习` `自动化修正` `城市规划` `环境监测`

## 📋 核心要点

1. 现有的单目高度估计方法在结构线索不足和环境变化下的鲁棒性较差，限制了其应用。
2. 本文提出了一种自动化的修正管道，结合稀疏的全球LiDAR数据与深度学习预测，提升了高度估计的准确性。
3. 在六个不同区域的实验中，最佳方法显著降低了MHE和MDE模型的误差，验证了修正管道的有效性。

## 📝 摘要（中文）

单目高度估计（MHE）从超高分辨率光学影像中提取高度信息面临挑战，主要由于结构线索有限以及传统高程数据（如机载LiDAR和多视角立体）的高成本和地理限制。尽管近期的MHE和单目深度估计（MDE）模型表现良好，但在不同光照和场景条件下的鲁棒性仍然有限。本文提出了一种完全自动化的修正流程，将来自ICESat-2的稀疏、不完美的全球LiDAR测量与深度学习预测相结合，以提高准确性和稳定性。该工作流程完全依赖于公开可用的模型和数据，仅需一幅地理参考的光学图像即可生成修正后的高度图，具有低成本和全球可扩展的部署能力。我们还建立了该任务的首个基准，评估了两种随机森林方法、四种参数高效微调方法和完全微调。实验结果显示，最佳方法将MHE模型的平均绝对误差（MAE）降低了30.9%，F1HE分数提高了44.2%。

## 🔬 方法详解

**问题定义**：本文旨在解决单目高度估计（MHE）在高分辨率光学影像中因结构线索不足而导致的准确性和稳定性问题。现有方法在不同光照和场景条件下的表现不够鲁棒，限制了其实际应用。

**核心思路**：论文提出的解决方案是通过整合来自ICESat-2的稀疏LiDAR测量与深度学习模型的预测，形成一个自动化的修正流程。这种设计旨在利用全球可用的LiDAR数据来增强单目高度估计的准确性。

**技术框架**：整体架构包括数据输入、深度学习模型预测、LiDAR数据修正和高度图生成四个主要模块。首先，输入一幅地理参考的光学图像，然后通过深度学习模型进行初步的高度估计，接着利用LiDAR数据进行修正，最后输出修正后的高度图。

**关键创新**：最重要的技术创新在于将稀疏的LiDAR数据与深度学习预测相结合，形成了一种新的修正机制。这种方法与传统的依赖于密集LiDAR或多视角立体的方式有本质区别，降低了数据获取的成本和复杂性。

**关键设计**：在技术细节上，论文采用了随机森林和多种参数高效微调方法进行模型训练，优化了损失函数以适应稀疏数据的特性。具体的参数设置和网络结构设计未详细披露，标记为未知。

## 📊 实验亮点

实验结果显示，最佳修正方法将MHE模型的平均绝对误差（MAE）降低了30.9%，F1HE分数提高了44.2%。对于MDE模型，MAE改善了24.1%，F1HE分数提升了25.1%。这些结果验证了修正管道的有效性，表明稀疏LiDAR数据能够系统性地增强高度估计模型的性能。

## 🎯 应用场景

该研究的潜在应用领域包括城市规划、环境监测和灾害管理等。通过提供低成本的3D高度映射，能够为各类应用提供支持，尤其是在资源有限的地区，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Monocular height estimation (MHE) from very-high-resolution (VHR) optical imagery remains challenging due to limited structural cues and the high cost and geographic constraints of conventional elevation data such as airborne LiDAR and multi-view stereo. Although recent MHE and monocular depth estimation (MDE) models show strong performance, their robustness under varied illumination and scene conditions is still limited. We introduce a fully automated correction pipeline that integrates sparse, imperfect global LiDAR measurements from ICESat-2 with deep learning predictions to enhance accuracy and stability. The workflow relies entirely on publicly available models and data and requires only a single georeferenced optical image to produce corrected height maps, enabling low-cost and globally scalable deployment. We also establish the first benchmark for this task, evaluating two random forest based approaches, four parameter efficient fine tuning methods, and full fine tuning. Experiments across six diverse regions at 0.5 m resolution (297 km2), covering the urban cores of Tokyo, Paris, and Sao Paulo as well as suburban and forested areas, show substantial gains. The best method reduces the MHE model's mean absolute error (MAE) by 30.9 percent and improves its F1HE score by 44.2 percent. For the MDE model, MAE improves by 24.1 percent and the F1HE score by 25.1 percent. These results validate the effectiveness of our correction pipeline and demonstrate how sparse global LiDAR can systematically strengthen both MHE and MDE models, enabling scalable and widely accessible 3D height mapping.

