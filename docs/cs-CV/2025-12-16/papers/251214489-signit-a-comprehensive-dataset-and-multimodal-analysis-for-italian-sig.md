---
layout: default
title: SignIT: A Comprehensive Dataset and Multimodal Analysis for Italian Sign Language Recognition
---

# SignIT: A Comprehensive Dataset and Multimodal Analysis for Italian Sign Language Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14489" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14489</a>
  <a href="https://arxiv.org/pdf/2512.14489.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14489" onclick="toggleFavorite(this, '2512.14489', 'SignIT: A Comprehensive Dataset and Multimodal Analysis for Italian Sign Language Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alessia Micieli, Giovanni Maria Farinella, Francesco Ragusa

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**SignIT：一个用于意大利手语识别的综合数据集与多模态分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意大利手语识别` `手语数据集` `多模态分析` `2D关键点` `视频理解`

## 📋 核心要点

1. 现有的意大利手语识别数据集规模有限，难以充分训练和评估复杂模型。
2. SignIT数据集包含大量视频和细粒度的手语类别标注，并提供2D关键点信息，支持多模态分析。
3. 论文通过实验评估了现有模型在SignIT数据集上的性能，揭示了现有方法在意大利手语识别上的挑战。

## 📝 摘要（中文）

本文提出了SignIT，一个新的用于研究意大利手语（LIS）识别任务的数据集。该数据集包含644个视频，总时长3.33小时。我们手动标注了这些视频，涵盖了94个不同的手语类别，这些类别属于5个宏观类别：动物、食物、颜色、情感和家庭。我们还提取了用户的手、面部和身体相关的2D关键点。基于该数据集，我们提出了一个手语识别任务的基准，采用了几种最先进的模型，展示了时间信息、2D关键点和RGB帧如何影响这些模型的性能。结果表明，这些模型在这个具有挑战性的LIS数据集上存在局限性。我们公开了数据和标注。

## 🔬 方法详解

**问题定义**：论文旨在解决意大利手语（LIS）识别问题。现有手语识别数据集，特别是针对意大利手语的数据集，规模较小，标注信息不足，难以支持复杂模型的训练和评估。这限制了意大利手语识别技术的发展。

**核心思路**：论文的核心思路是构建一个大规模、高质量的意大利手语数据集SignIT，并利用该数据集对现有手语识别模型进行基准测试。通过多模态数据（RGB视频和2D关键点）的结合，探索不同模态信息对手语识别性能的影响。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据采集：收集包含多种手语类别的大量意大利手语视频。2) 数据标注：手动标注视频中的手语类别，并提取手、面部和身体的2D关键点。3) 模型评估：选择几种最先进的手语识别模型，在SignIT数据集上进行训练和测试。4) 性能分析：分析不同模型在不同模态数据下的性能表现，找出模型的优势和不足。

**关键创新**：该论文的关键创新在于构建了一个新的、大规模的意大利手语数据集SignIT，该数据集不仅包含RGB视频，还提供了2D关键点信息，为多模态手语识别研究提供了基础。此外，论文还对现有手语识别模型在SignIT数据集上进行了全面的基准测试，为后续研究提供了参考。

**关键设计**：SignIT数据集包含644个视频，涵盖94个不同的手语类别。这些类别被划分为5个宏观类别：动物、食物、颜色、情感和家庭。论文采用了常见的关键点检测方法提取手、面部和身体的2D关键点。在模型评估方面，论文选择了多种最先进的手语识别模型，并针对不同模态的数据进行了实验。具体的参数设置和网络结构等技术细节取决于所选用的具体模型。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14489/Image/grid_name.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14489/Image/verdeGreen.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14489/Image/pre.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建的SignIT数据集包含644个视频，覆盖94个手语类别，是目前最大的意大利手语数据集之一。实验结果表明，现有手语识别模型在SignIT数据集上表现出一定的局限性，这突显了意大利手语识别任务的挑战性，并为未来的研究方向提供了指导。

## 🎯 应用场景

该研究成果可应用于开发意大利手语翻译系统，帮助听力障碍人士进行交流。此外，该数据集和基准测试结果可以促进手语识别领域的研究进展，推动更准确、更鲁棒的手语识别技术的开发。未来，该技术有望应用于智能助手、教育、医疗等领域。

## 📄 摘要（原文）

> In this work we present SignIT, a new dataset to study the task of Italian Sign Language (LIS) recognition. The dataset is composed of 644 videos covering 3.33 hours. We manually annotated videos considering a taxonomy of 94 distinct sign classes belonging to 5 macro-categories: Animals, Food, Colors, Emotions and Family. We also extracted 2D keypoints related to the hands, face and body of the users. With the dataset, we propose a benchmark for the sign recognition task, adopting several state-of-the-art models showing how temporal information, 2D keypoints and RGB frames can be influence the performance of these models. Results show the limitations of these models on this challenging LIS dataset. We release data and annotations at the following link:this https URL.

