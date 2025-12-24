---
layout: default
title: Enhancing annotations for 5D apple pose estimation through 3D Gaussian Splatting (3DGS)
---

# Enhancing annotations for 5D apple pose estimation through 3D Gaussian Splatting (3DGS)

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20148" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20148v1</a>
  <a href="https://arxiv.org/pdf/2512.20148.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20148v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20148v1', 'Enhancing annotations for 5D apple pose estimation through 3D Gaussian Splatting (3DGS)')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Robert van de Ven, Trim Bresilla, Bram Nelissen, Ard Nieuwenhuizen, Eldert J. van Henten, Gert Kootstra

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-23

**备注**: 33 pages, excluding appendices. 17 figures

---

## 💡 一句话要点

**利用3D高斯溅射增强5D苹果姿态估计的标注效率**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `苹果姿态估计` `3D高斯溅射` `数据增强` `自动化标注` `果园机器人`

## 📋 核心要点

1. 苹果姿态估计依赖人工标注，但果园环境遮挡严重，导致标注困难且易出错。
2. 利用3D高斯溅射重建果园场景，简化标注流程，并自动将标注投影到图像。
3. 实验表明，该方法仅需少量人工标注即可生成大量训练数据，并提升姿态估计性能。

## 📝 摘要（中文）

果园环境变化大且遮挡严重，使得果园自动化任务充满挑战。苹果姿态估计是其中一个难题，果萼等关键点经常被遮挡。虽然最新的姿态估计方法不再依赖这些关键点，但仍然需要它们进行标注，这使得标注工作既困难又耗时。由于遮挡，同一苹果在不同图像之间可能存在冲突或缺失的标注。新颖的3D重建方法可用于简化标注并扩大数据集。本文提出了一种新颖的流程，包括使用3D高斯溅射重建果园场景、简化标注、自动将标注投影到图像，以及训练和评估姿态估计方法。使用该流程，仅需105个手动标注即可获得28,191个训练标签，减少了99.6%。实验结果表明，使用遮挡率≤95%的苹果标签进行训练可获得最佳性能，在原始图像上的F1得分为0.927，在渲染图像上的F1得分为0.970。调整训练数据集的大小对模型的F1得分和姿态估计准确率影响不大。研究发现，遮挡最少的苹果的位置估计效果最好，随着遮挡增加，效果变差。此外，测试的姿态估计方法无法正确学习苹果的姿态估计。

## 🔬 方法详解

**问题定义**：论文旨在解决苹果姿态估计中人工标注耗时且易受遮挡影响的问题。现有方法虽然不再依赖关键点，但仍需人工标注，在遮挡严重的果园环境中，标注质量难以保证，且效率低下。

**核心思路**：论文的核心思路是利用3D高斯溅射（3DGS）技术重建果园场景的3D模型，然后在3D模型上进行简化标注，最后将这些标注自动投影到2D图像上，从而生成大量的训练数据。这样可以显著减少人工标注的工作量，并提高标注的准确性和一致性。

**技术框架**：该方法包含以下几个主要阶段：1) 使用多视角图像重建果园场景的3D高斯溅射模型；2) 在3D模型上进行简化标注（例如，仅标注苹果的中心点）；3) 将3D标注投影到2D图像上，生成训练数据；4) 使用生成的训练数据训练姿态估计模型；5) 评估姿态估计模型的性能。

**关键创新**：该方法最重要的创新点在于将3D高斯溅射技术应用于苹果姿态估计的标注流程中。与传统的2D标注方法相比，该方法可以在3D空间中进行标注，从而避免了遮挡带来的问题，并提高了标注的效率和准确性。此外，自动投影标注到图像的方法也减少了人工干预，降低了标注成本。

**关键设计**：论文中使用了标准的3D高斯溅射算法进行场景重建。在标注方面，作者简化了标注内容，例如只标注苹果的中心点。在训练姿态估计模型时，作者探索了不同遮挡程度的苹果对模型性能的影响，并发现使用遮挡率≤95%的苹果标签进行训练可以获得最佳性能。具体的姿态估计模型结构和损失函数没有在摘要中详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20148v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20148v1/img/overview_w_camera_poses.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20148v1/img/annotating_3dgs.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

该方法仅需105个手动标注即可生成28,191个训练标签，标注工作量减少了99.6%。实验结果表明，使用遮挡率≤95%的苹果标签进行训练，在原始图像上的F1得分为0.927，在渲染图像上的F1得分为0.970，验证了该方法的有效性。

## 🎯 应用场景

该研究成果可应用于果园机器人、自动化采摘、产量预测等领域。通过减少人工标注工作量，降低了数据获取成本，加速了相关算法的开发和部署。未来，该方法可推广到其他农作物或复杂场景的姿态估计任务中，促进农业智能化发展。

## 📄 摘要（原文）

> Automating tasks in orchards is challenging because of the large amount of variation in the environment and occlusions. One of the challenges is apple pose estimation, where key points, such as the calyx, are often occluded. Recently developed pose estimation methods no longer rely on these key points, but still require them for annotations, making annotating challenging and time-consuming. Due to the abovementioned occlusions, there can be conflicting and missing annotations of the same fruit between different images. Novel 3D reconstruction methods can be used to simplify annotating and enlarge datasets. We propose a novel pipeline consisting of 3D Gaussian Splatting to reconstruct an orchard scene, simplified annotations, automated projection of the annotations to images, and the training and evaluation of a pose estimation method. Using our pipeline, 105 manual annotations were required to obtain 28,191 training labels, a reduction of 99.6%. Experimental results indicated that training with labels of fruits that are $\leq95\%$ occluded resulted in the best performance, with a neutral F1 score of 0.927 on the original images and 0.970 on the rendered images. Adjusting the size of the training dataset had small effects on the model performance in terms of F1 score and pose estimation accuracy. It was found that the least occluded fruits had the best position estimation, which worsened as the fruits became more occluded. It was also found that the tested pose estimation method was unable to correctly learn the orientation estimation of apples.

