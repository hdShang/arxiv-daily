---
layout: default
title: "Point-It-Out: Benchmarking Embodied Reasoning for Vision Language Models in Multi-Stage Visual Grounding"
---

# Point-It-Out: Benchmarking Embodied Reasoning for Vision Language Models in Multi-Stage Visual Grounding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.25794" class="toolbar-btn" target="_blank">📄 arXiv: 2509.25794v1</a>
  <a href="https://arxiv.org/pdf/2509.25794.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.25794v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.25794v1', 'Point-It-Out: Benchmarking Embodied Reasoning for Vision Language Models in Multi-Stage Visual Grounding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Xue, Yunhao Ge, Yu Zeng, Zhaoshuo Li, Ming-Yu Liu, Yongxin Chen, Jiaojiao Fan

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-30

---

## 💡 一句话要点

**提出Point-It-Out基准，评估视觉语言模型在多阶段视觉定位中的具身推理能力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `具身推理` `视觉定位` `基准测试` `多阶段评估`

## 📋 核心要点

1. 现有具身推理基准主要依赖图像标注和选择题，无法精确评估视觉语言模型(VLM)的视觉定位能力。
2. Point-It-Out (PIO)基准通过多阶段视觉定位任务，系统评估VLM在具身智能场景下的推理能力。
3. 实验表明，通用VLM在视觉定位方面表现不如特定开源模型，且模型在不同阶段表现差异显著。

## 📝 摘要（中文）

视觉语言模型(VLM)在各种任务中展现了令人印象深刻的世界知识，使其成为具身推理应用的有希望的候选者。然而，现有的基准主要通过基于图像注释的多项选择题来评估VLM的具身推理能力，例如，选择哪个轨迹更好地描述了图像中的事件。本文提出了Point-It-Out (PIO)基准，这是一个新颖的基准，旨在通过精确的视觉定位系统地评估VLM的具身推理能力。我们提出了一个分层评估协议，跨越三个阶段(S1:参考对象定位，S2:任务驱动的指向，S3:视觉轨迹预测)，数据收集自具身智能的关键领域，包括室内、厨房、驾驶和机器人操作场景。对十多个最先进的VLM的广泛实验揭示了一些有趣的发现。例如，像GPT-4o这样强大的通用模型，虽然在许多基准测试(例如，语言、感知和推理)中表现出色，但在精确的视觉定位方面，其性能不如一些开源模型;像MoLMO这样的模型在S1和S2中表现良好，但在S3中表现不佳，S3需要将定位与视觉轨迹规划相结合。

## 🔬 方法详解

**问题定义**：现有具身推理评估方法主要依赖于图像标注和选择题，缺乏对视觉语言模型(VLM)精确视觉定位能力的有效评估。这使得我们难以了解VLM在真实具身智能任务中的表现，例如机器人操作和导航等。

**核心思路**：Point-It-Out (PIO)基准的核心思路是通过构建一个多阶段的视觉定位任务，系统地评估VLM的具身推理能力。该基准模拟了真实世界中具身智能体需要执行的各种任务，例如寻找特定物体、根据指令指向目标位置以及预测视觉轨迹。

**技术框架**：PIO基准包含三个阶段：S1（参考对象定位）：VLM需要根据文本描述在图像中定位目标对象；S2（任务驱动的指向）：VLM需要根据任务指令指向图像中的特定位置；S3（视觉轨迹预测）：VLM需要预测完成任务所需的视觉轨迹。数据收集自室内、厨房、驾驶和机器人操作等多个具身智能关键领域。

**关键创新**：PIO基准的关键创新在于其多阶段的评估协议，能够更全面地评估VLM的具身推理能力。与现有基准相比，PIO更加关注VLM的视觉定位精度，并引入了视觉轨迹预测任务，更贴近真实世界的具身智能应用。

**关键设计**：PIO基准的数据集包含各种具身智能场景，例如室内环境、厨房环境、驾驶场景和机器人操作场景。每个场景都包含多个视觉定位任务，每个任务都包含文本描述、图像和目标位置的标注。评估指标包括定位精度、指向精度和轨迹预测精度。具体参数设置和网络结构取决于所评估的VLM模型。

## 📊 实验亮点

实验结果表明，GPT-4o等通用VLM在视觉定位方面表现不如MoLMO等开源模型。MoLMO在S1和S2阶段表现良好，但在S3阶段表现不佳，表明视觉轨迹预测对VLM提出了更高的要求。这些发现有助于指导VLM在具身智能领域的进一步研究和应用。

## 🎯 应用场景

该研究成果可应用于机器人导航、智能家居、自动驾驶等领域。通过精确评估和提升视觉语言模型的具身推理能力，可以使智能体更好地理解环境、执行任务，从而实现更智能、更高效的人机交互和自动化。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have demonstrated impressive world knowledge across a wide range of tasks, making them promising candidates for embodied reasoning applications. However, existing benchmarks primarily evaluate the embodied reasoning ability of VLMs through multiple-choice questions based on image annotations -- for example, selecting which trajectory better describes an event in the image. In this work, we introduce the Point-It-Out (PIO) benchmark, a novel benchmark designed to systematically assess the embodied reasoning abilities of VLMs through precise visual grounding. We propose a hierarchical evaluation protocol spanning three stages (S1: referred-object localization, S2: task-driven pointing, and S3: visual trace prediction), with data collected from critical domains for embodied intelligence, including indoor, kitchen, driving, and robotic manipulation scenarios. Extensive experiments with over ten state-of-the-art VLMs reveal several interesting findings. For example, strong general-purpose models such as GPT-4o, while excelling on many benchmarks (e.g., language, perception, and reasoning), underperform compared to some open-source models in precise visual grounding; models such as MoLMO perform well in S1 and S2 but struggle in S3, where requires grounding combined with visual trace planning.

