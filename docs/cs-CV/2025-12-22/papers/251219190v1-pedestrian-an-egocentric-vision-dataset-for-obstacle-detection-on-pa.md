---
layout: default
title: "PEDESTRIAN: An Egocentric Vision Dataset for Obstacle Detection on Pavements"
---

# PEDESTRIAN: An Egocentric Vision Dataset for Obstacle Detection on Pavements

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19190" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19190v1</a>
  <a href="https://arxiv.org/pdf/2512.19190.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19190v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19190v1', 'PEDESTRIAN: An Egocentric Vision Dataset for Obstacle Detection on Pavements')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Marios Thoma, Zenonas Theodosiou, Harris Partaourides, Vassilis Vassiliades, Loizos Michael, Andreas Lanitis

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-22

**备注**: 24 pages, 7 figures, 9 tables, Dataset: https://doi.org/10.5281/zenodo.10907945, Code: https://github.com/CYENS/PEDESTRIAN

---

## 💡 一句话要点

**提出行人视角障碍物检测数据集PEDESTRIAN，用于提升城市人行道安全。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `行人安全` `障碍物检测` `第一人称视角` `数据集` `深度学习`

## 📋 核心要点

1. 城市人行道障碍物阻碍行人通行，存在安全隐患，但缺乏有效的第一人称视角障碍物检测方法。
2. 论文构建了包含29种常见障碍物的PEDESTRIAN数据集，利用行人视角视频数据进行障碍物检测。
3. 实验结果表明，该数据集可用于训练深度学习算法，为行人安全提供基准。

## 📝 摘要（中文）

步行是主要的交通方式，对保持健康至关重要。然而，城市人行道经常被各种障碍物阻碍，影响行人自由通行，构成安全隐患。普适计算和第一人称视角技术的发展为设计能够自动实时检测这些障碍物的系统提供了可能，从而提高行人安全。有效识别算法的开发依赖于全面且均衡的第一人称视角数据集。本文介绍了PEDESTRIAN数据集，其中包含29种城市人行道上常见的障碍物的第一人称视角数据。使用手机摄像头收集了总共340个视频，捕捉了行人的视角。此外，我们还展示了一系列实验的结果，这些实验使用提出的数据集训练了几种最先进的深度学习算法，这些算法可以用作障碍物检测和识别任务的基准。

## 🔬 方法详解

**问题定义**：论文旨在解决城市人行道上行人面临的障碍物检测问题。现有方法缺乏针对行人第一人称视角的有效数据集，难以训练出鲁棒的障碍物检测模型。这些障碍物可能对行人安全构成威胁，尤其对于弱势群体，如老年人和残疾人。

**核心思路**：论文的核心思路是构建一个大规模、多样化的行人第一人称视角数据集，用于训练和评估障碍物检测算法。通过提供真实场景下的行人视角数据，可以使模型更好地学习到障碍物的特征，从而提高检测的准确性和鲁棒性。

**技术框架**：该研究主要围绕数据集的构建和实验展开。首先，使用手机摄像头采集了340个视频，覆盖29种常见的城市人行道障碍物。然后，使用这些数据训练了多种最先进的深度学习算法，并评估了它们的性能。整个流程包括数据采集、数据标注、模型训练和性能评估四个主要阶段。

**关键创新**：该论文的关键创新在于构建了PEDESTRIAN数据集，这是一个专门针对行人第一人称视角障碍物检测的数据集。与现有的通用目标检测数据集不同，PEDESTRIAN数据集更加关注行人视角下的障碍物，并且包含了多种常见的城市人行道障碍物，更贴合实际应用场景。

**关键设计**：数据集包含了340个视频，覆盖了29种不同的障碍物。视频数据使用手机摄像头采集，模拟了真实的行人视角。论文没有详细说明具体的模型参数设置、损失函数或网络结构，而是将数据集作为基准，供研究者使用不同的模型进行训练和评估。未来的研究可以探索不同的模型结构和训练策略，以进一步提高障碍物检测的性能。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19190v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19190v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19190v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文通过实验验证了PEDESTRIAN数据集的有效性，使用该数据集训练的深度学习算法可以实现较好的障碍物检测性能。虽然论文没有给出具体的性能指标，但强调了该数据集可以作为障碍物检测和识别任务的基准。未来的研究可以基于该数据集，进一步优化模型结构和训练策略，以提高检测精度和鲁棒性。

## 🎯 应用场景

该研究成果可应用于开发智能辅助系统，例如为视力障碍人士提供导航辅助，或为自动驾驶轮椅提供障碍物规避功能。通过实时检测人行道上的障碍物，可以显著提高行人的安全性，尤其是在城市环境中。未来，结合可穿戴设备和边缘计算技术，可以实现更加便捷和高效的行人安全保障系统。

## 📄 摘要（原文）

> Walking has always been a primary mode of transportation and is recognized as an essential activity for maintaining good health. Despite the need for safe walking conditions in urban environments, sidewalks are frequently obstructed by various obstacles that hinder free pedestrian movement. Any object obstructing a pedestrian's path can pose a safety hazard. The advancement of pervasive computing and egocentric vision techniques offers the potential to design systems that can automatically detect such obstacles in real time, thereby enhancing pedestrian safety. The development of effective and efficient identification algorithms relies on the availability of comprehensive and well-balanced datasets of egocentric data. In this work, we introduce the PEDESTRIAN dataset, comprising egocentric data for 29 different obstacles commonly found on urban sidewalks. A total of 340 videos were collected using mobile phone cameras, capturing a pedestrian's point of view. Additionally, we present the results of a series of experiments that involved training several state-of-the-art deep learning algorithms using the proposed dataset, which can be used as a benchmark for obstacle detection and recognition tasks. The dataset can be used for training pavement obstacle detectors to enhance the safety of pedestrians in urban areas.

