---
layout: default
title: Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks
---

# Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.24010" class="toolbar-btn" target="_blank">📄 arXiv: 2510.24010v1</a>
  <a href="https://arxiv.org/pdf/2510.24010.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.24010v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.24010v1', 'Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mirali Purohit, Bimal Gajera, Vatsal Malaviya, Irish Mehta, Kunal Kasodekar, Jacob Adler, Steven Lu, Umaa Rebbapragada, Hannah Kerner

**分类**: cs.CV, cs.AI, cs.LG

**发布日期**: 2025-10-28

**备注**: Accepted at NeurIPS 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://mars-bench.github.io/)

---

## 💡 一句话要点

**Mars-Bench：火星科学任务的深度学习基础模型评估基准**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `火星科学` `机器学习` `基准数据集` `图像分类` `目标检测` `图像分割` `深度学习` `地质特征`

## 📋 核心要点

1. 火星科学缺乏标准化的评估基准，阻碍了适用于火星任务的深度学习基础模型的发展。
2. Mars-Bench提供了一系列火星相关的图像数据集，涵盖多种任务，用于系统评估机器学习模型。
3. 实验结果表明，针对火星数据进行预训练的模型可能优于通用模型，值得进一步研究。

## 📝 摘要（中文）

本文提出了Mars-Bench，这是一个用于系统评估火星科学相关任务中机器学习模型的基准。该基准旨在解决火星科学领域缺乏标准化评估框架的问题，从而促进适用于火星任务的基础模型发展。Mars-Bench包含20个数据集，涵盖分类、分割和目标检测等任务，专注于陨石坑、锥体、巨石和霜等关键地质特征。论文提供了标准化的、即用型数据集，并使用在自然图像、地球卫星数据和先进视觉-语言模型上预训练的模型进行了基线评估。分析结果表明，特定于火星的基础模型可能优于通用领域模型，激发了对领域自适应预训练的进一步探索。Mars-Bench旨在为开发和比较火星科学机器学习模型建立一个标准化的基础。

## 🔬 方法详解

**问题定义**：目前，火星科学领域缺乏统一的、标准化的基准数据集和评估框架，这使得研究人员难以系统地评估和比较不同的机器学习模型在火星探测任务上的性能。现有的模型通常在通用数据集上预训练，然后直接应用于火星图像，忽略了火星地貌的独特性，导致性能受限。

**核心思路**：Mars-Bench的核心思路是构建一个全面的、标准化的火星科学数据集，涵盖多种任务和地质特征，为研究人员提供一个公平、可重复的评估平台。通过在这个基准上评估不同的模型，可以更好地了解哪些模型更适合处理火星数据，并促进针对火星任务的专用模型的开发。

**技术框架**：Mars-Bench包含20个数据集，涵盖分类、分割和目标检测三种任务类型。数据集来源于火星轨道和表面图像，包含了陨石坑、锥体、巨石和霜等关键地质特征。论文提供了标准化的数据格式和评估指标，方便研究人员使用。此外，论文还提供了基于现有模型的基线评估结果，作为比较的参考。

**关键创新**：Mars-Bench的主要创新在于它是第一个专门为火星科学任务设计的综合性基准。它填补了该领域缺乏标准化评估框架的空白，为研究人员提供了一个统一的平台来开发和比较模型。通过提供多样化的数据集和基线结果，Mars-Bench促进了火星科学领域机器学习研究的进展。

**关键设计**：Mars-Bench的数据集涵盖了多种地质特征和任务类型，以确保评估的全面性。论文使用了常用的图像处理和机器学习技术，如卷积神经网络（CNN）和视觉-语言模型，作为基线模型进行评估。数据集被划分为训练集、验证集和测试集，以确保评估的公平性。论文还定义了标准的评估指标，如准确率、召回率和F1分数，用于衡量模型的性能。

## 📊 实验亮点

Mars-Bench的实验结果表明，在自然图像和地球卫星数据上预训练的模型在火星数据集上的表现相对较弱，这突显了领域自适应预训练的重要性。初步实验结果表明，针对火星数据进行预训练的模型可能优于通用模型，这为未来研究方向提供了有价值的参考。

## 🎯 应用场景

Mars-Bench的潜在应用领域包括火星地质特征的自动识别与分类、火星探测车导航、资源勘探以及潜在的生命迹象检测。该基准的实际价值在于加速火星科学研究的进展，提高火星探测任务的效率和准确性。未来，基于Mars-Bench开发的模型可以用于自动化分析大量的火星图像数据，从而帮助科学家更好地了解火星的地质历史和演化过程。

## 📄 摘要（原文）

> Foundation models have enabled rapid progress across many specialized domains by leveraging large-scale pre-training on unlabeled data, demonstrating strong generalization to a variety of downstream tasks. While such models have gained significant attention in fields like Earth Observation, their application to Mars science remains limited. A key enabler of progress in other domains has been the availability of standardized benchmarks that support systematic evaluation. In contrast, Mars science lacks such benchmarks and standardized evaluation frameworks, which have limited progress toward developing foundation models for Martian tasks. To address this gap, we introduce Mars-Bench, the first benchmark designed to systematically evaluate models across a broad range of Mars-related tasks using both orbital and surface imagery. Mars-Bench comprises 20 datasets spanning classification, segmentation, and object detection, focused on key geologic features such as craters, cones, boulders, and frost. We provide standardized, ready-to-use datasets and baseline evaluations using models pre-trained on natural images, Earth satellite data, and state-of-the-art vision-language models. Results from all analyses suggest that Mars-specific foundation models may offer advantages over general-domain counterparts, motivating further exploration of domain-adapted pre-training. Mars-Bench aims to establish a standardized foundation for developing and comparing machine learning models for Mars science. Our data, models, and code are available at: https://mars-bench.github.io/.

