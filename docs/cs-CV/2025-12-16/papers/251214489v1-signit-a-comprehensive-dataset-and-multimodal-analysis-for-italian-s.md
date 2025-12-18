---
layout: default
title: SignIT: A Comprehensive Dataset and Multimodal Analysis for Italian Sign Language Recognition
---

# SignIT: A Comprehensive Dataset and Multimodal Analysis for Italian Sign Language Recognition

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14489" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14489v1</a>
  <a href="https://arxiv.org/pdf/2512.14489.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14489v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14489v1', 'SignIT: A Comprehensive Dataset and Multimodal Analysis for Italian Sign Language Recognition')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alessia Micieli, Giovanni Maria Farinella, Francesco Ragusa

**分类**: cs.CV

**发布日期**: 2025-12-16

**🔗 代码/项目**: [PROJECT_PAGE](https://fpv-iplab.github.io/SignIT/)

---

## 💡 一句话要点

**发布SignIT意大利手语数据集，并进行多模态手语识别基准分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `意大利手语识别` `多模态数据集` `2D关键点` `手语识别基准` `SignIT数据集`

## 📋 核心要点

1. 现有的意大利手语识别数据集不足，限制了相关算法的研究和发展。
2. 构建包含RGB视频和2D关键点信息的SignIT数据集，为意大利手语识别提供新的资源。
3. 通过在SignIT数据集上评估现有模型，揭示了现有方法在意大利手语识别任务中的局限性。

## 📝 摘要（中文）

本文介绍了SignIT，一个新的用于研究意大利手语（LIS）识别任务的数据集。该数据集包含644个视频，总时长3.33小时。我们手动标注了视频，涵盖94个不同的手语类别，这些类别属于5个宏观类别：动物、食物、颜色、情感和家庭。我们还提取了用户的手部、面部和身体相关的2D关键点。基于该数据集，我们提出了一个手语识别任务的基准，采用了几种最先进的模型，展示了时间信息、2D关键点和RGB帧如何影响这些模型的性能。结果表明，这些模型在这个具有挑战性的LIS数据集上存在局限性。我们在以下链接发布数据和注释：https://fpv-iplab.github.io/SignIT/。

## 🔬 方法详解

**问题定义**：论文旨在解决意大利手语（LIS）识别问题。现有方法在意大利手语数据集上的表现不佳，缺乏专门针对意大利手语的数据集是主要痛点。已有的手语识别模型在处理意大利手语时，由于数据集的差异和复杂性，泛化能力受到限制。

**核心思路**：论文的核心思路是构建一个高质量的意大利手语数据集SignIT，并利用该数据集评估现有手语识别模型，从而为未来的研究提供基准和方向。通过提供包含RGB视频和2D关键点信息的多模态数据，可以更全面地捕捉手语的特征。

**技术框架**：该研究的技术框架主要包含两个部分：数据集构建和基准模型评估。数据集构建包括视频采集、手动标注和2D关键点提取。基准模型评估部分，作者选择了多个state-of-the-art的手语识别模型，并在SignIT数据集上进行训练和测试。评估过程中，作者分析了不同模态（RGB, 2D关键点）对模型性能的影响。

**关键创新**：该论文的关键创新在于构建了专门针对意大利手语的SignIT数据集。该数据集不仅包含RGB视频，还提供了手部、面部和身体的2D关键点信息，为多模态手语识别研究提供了可能。此外，论文还通过实验分析了现有模型在SignIT数据集上的性能，为未来的研究提供了有价值的参考。

**关键设计**：数据集包含644个视频，涵盖94个不同的手语类别，这些类别属于5个宏观类别。视频通过人工标注，确保标注的准确性。2D关键点使用现有的姿态估计模型提取。在基准模型评估中，作者选择了多个常用的手语识别模型，并使用标准的评估指标（如准确率）来衡量模型的性能。具体的模型参数设置和训练策略在论文中没有详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14489v1/Image/grid_name.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14489v1/Image/verdeGreen.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14489v1/Image/pre.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

论文构建的SignIT数据集包含644个视频，涵盖94个手语类别，为意大利手语识别研究提供了宝贵资源。通过在SignIT数据集上评估现有模型，作者发现现有模型在意大利手语识别任务中存在局限性，这为未来的研究指明了方向。具体的性能数据和提升幅度在摘要中没有明确给出，属于未知信息。

## 🎯 应用场景

该研究成果可应用于手语翻译、手语教学、聋哑人辅助交流等领域。SignIT数据集的发布将促进意大利手语识别技术的发展，为聋哑人提供更便捷的交流方式。未来，可以将该技术应用于智能家居、虚拟助手等场景，提升用户体验。

## 📄 摘要（原文）

> In this work we present SignIT, a new dataset to study the task of Italian Sign Language (LIS) recognition. The dataset is composed of 644 videos covering 3.33 hours. We manually annotated videos considering a taxonomy of 94 distinct sign classes belonging to 5 macro-categories: Animals, Food, Colors, Emotions and Family. We also extracted 2D keypoints related to the hands, face and body of the users. With the dataset, we propose a benchmark for the sign recognition task, adopting several state-of-the-art models showing how temporal information, 2D keypoints and RGB frames can be influence the performance of these models. Results show the limitations of these models on this challenging LIS dataset. We release data and annotations at the following link: https://fpv-iplab.github.io/SignIT/.

