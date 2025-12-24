---
layout: default
title: "STROKEVISION-BENCH: A Multimodal Video And 2D Pose Benchmark For Tracking Stroke Recovery"
---

# STROKEVISION-BENCH: A Multimodal Video And 2D Pose Benchmark For Tracking Stroke Recovery

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07994" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07994v1</a>
  <a href="https://arxiv.org/pdf/2509.07994.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07994v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07994v1', 'STROKEVISION-BENCH: A Multimodal Video And 2D Pose Benchmark For Tracking Stroke Recovery')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: David Robinson, Animesh Gupta, Rizwan Quershi, Qiushi Fu, Mubarak Shah

**分类**: eess.IV, cs.CV, cs.LG

**发布日期**: 2025-09-02

**备注**: 6 pages

---

## 💡 一句话要点

**StrokeVision-Bench：用于跟踪中风恢复的多模态视频和2D姿态基准数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `中风康复` `数据集` `视频动作识别` `2D姿态估计` `临床评估`

## 📋 核心要点

1. 现有中风康复数据集缺乏临床结构化评估，且常混合健康与患病个体，限制了临床应用。
2. StrokeVision-Bench数据集专注于中风患者的方块转移任务，提供视频和2D骨骼关键点两种模态。
3. 论文对现有动作识别方法进行基准测试，为自动化中风康复评估研究奠定基础。

## 📝 摘要（中文）

尽管康复方案取得了进展，但中风后上肢(UE)功能的临床评估在很大程度上仍然是主观的，严重依赖治疗师的观察和粗略的评分系统。这种主观性限制了评估检测细微运动改善的敏感性，而这对于个性化康复计划至关重要。计算机视觉的最新进展为实现客观、定量和可扩展的UE运动功能评估提供了有希望的途径。在标准化测试中，Box and Block Test (BBT)被广泛用于测量手的灵活性和跟踪中风恢复，提供了一个适合计算分析的结构化环境。然而，现有的针对中风康复的数据集主要集中在日常生活活动上，并且通常无法捕捉到临床结构化评估，例如方块转移任务。此外，许多可用的数据集包括健康人和受中风影响的人的混合，限制了它们的特异性和临床效用。为了解决这些关键差距，我们推出了StrokeVision-Bench，这是第一个专门针对中风患者执行临床结构化方块转移任务的数据集。StrokeVision-Bench包含1,000个带注释的视频，分为四个临床上有意义的动作类别，每个样本以两种模态表示：原始视频帧和2D骨骼关键点。我们对几种最先进的视频动作识别和基于骨骼的动作分类方法进行了基准测试，以建立该领域的性能基线，并促进未来在自动化中风康复评估方面的研究。

## 🔬 方法详解

**问题定义**：现有中风康复数据集主要关注日常活动，缺乏临床结构化的方块转移任务数据，且数据集中常混合健康人和中风患者，导致数据集的特异性和临床实用性受限。因此，需要一个专门针对中风患者进行临床结构化评估的数据集，以支持更客观、定量和可扩展的康复评估。

**核心思路**：论文的核心思路是构建一个专门针对中风患者执行临床结构化方块转移任务的数据集StrokeVision-Bench。该数据集包含高质量的视频数据和精确的2D骨骼关键点标注，旨在为自动化中风康复评估研究提供可靠的基准。

**技术框架**：StrokeVision-Bench数据集包含1000个带注释的视频，这些视频被分为四个临床上有意义的动作类别。每个视频样本都以两种模态表示：原始视频帧和2D骨骼关键点。研究人员使用这些数据对现有的视频动作识别和基于骨骼的动作分类方法进行了基准测试，以建立性能基线。

**关键创新**：StrokeVision-Bench是第一个专门针对中风患者执行临床结构化方块转移任务的数据集。它提供了多模态数据（视频和2D骨骼关键点），并对现有方法进行了基准测试，为自动化中风康复评估研究提供了新的资源和起点。

**关键设计**：数据集包含1000个视频，分为四个动作类别。每个视频都进行了2D骨骼关键点标注。论文选择了Box and Block Test (BBT)作为临床结构化评估任务，因为它被广泛用于测量手的灵活性和跟踪中风恢复，并且提供了一个适合计算分析的结构化环境。具体标注细节和数据收集流程未知。

## 📊 实验亮点

论文构建了包含1000个视频的StrokeVision-Bench数据集，并对现有视频动作识别和基于骨骼的动作分类方法进行了基准测试。虽然论文没有明确给出具体性能数据和提升幅度，但它为该领域的研究建立了性能基线，并提供了一个新的数据集资源。

## 🎯 应用场景

该研究成果可应用于中风患者的康复评估，通过计算机视觉技术实现客观、定量和可扩展的运动功能评估。这有助于个性化康复计划的制定，并提高康复效果。未来，该数据集可促进开发更智能的康复机器人和远程康复系统。

## 📄 摘要（原文）

> Despite advancements in rehabilitation protocols, clinical assessment of upper extremity (UE) function after stroke largely remains subjective, relying heavily on therapist observation and coarse scoring systems. This subjectivity limits the sensitivity of assessments to detect subtle motor improvements, which are critical for personalized rehabilitation planning. Recent progress in computer vision offers promising avenues for enabling objective, quantitative, and scalable assessment of UE motor function. Among standardized tests, the Box and Block Test (BBT) is widely utilized for measuring gross manual dexterity and tracking stroke recovery, providing a structured setting that lends itself well to computational analysis. However, existing datasets targeting stroke rehabilitation primarily focus on daily living activities and often fail to capture clinically structured assessments such as block transfer tasks. Furthermore, many available datasets include a mixture of healthy and stroke-affected individuals, limiting their specificity and clinical utility. To address these critical gaps, we introduce StrokeVision-Bench, the first-ever dedicated dataset of stroke patients performing clinically structured block transfer tasks. StrokeVision-Bench comprises 1,000 annotated videos categorized into four clinically meaningful action classes, with each sample represented in two modalities: raw video frames and 2D skeletal keypoints. We benchmark several state-of-the-art video action recognition and skeleton-based action classification methods to establish performance baselines for this domain and facilitate future research in automated stroke rehabilitation assessment.

