---
layout: default
title: "WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios"
---

# WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.26125" class="toolbar-btn" target="_blank">📄 arXiv: 2510.26125v3</a>
  <a href="https://arxiv.org/pdf/2510.26125.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.26125v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.26125v3', 'WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Runsheng Xu, Hubert Lin, Wonseok Jeon, Hao Feng, Yuliang Zou, Liting Sun, John Gorman, Ekaterina Tolstaya, Sarah Tang, Brandyn White, Ben Sapp, Mingxing Tan, Jyh-Jing Hwang, Dragomir Anguelov

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-30 (更新: 2025-11-13)

---

## 💡 一句话要点

**WOD-E2E：针对端到端驾驶中长尾场景的Waymo开放数据集**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `端到端驾驶` `自动驾驶` `长尾场景` `数据集` `评估指标` `Waymo开放数据集` `Rater Feedback Score`

## 📋 核心要点

1. 现有端到端驾驶基准侧重于常见场景，缺乏对罕见但关键的长尾场景的有效评估。
2. 提出WOD-E2E数据集，包含大量长尾驾驶场景，并引入新的评估指标RFS，以更准确地衡量驾驶性能。
3. 发布了验证集的评分员偏好标签，并举办WOD-E2E挑战赛，旨在推动通用、鲁棒和安全的自动驾驶研究。

## 📝 摘要（中文）

基于视觉的端到端(E2E)驾驶因其可扩展性以及与多模态大型语言模型(MLLM)的协同作用而引起了研究界的广泛关注。然而，当前的E2E驾驶基准主要集中于常规场景，未能充分测试这些系统的真正潜力。此外，现有的开环评估指标通常无法捕捉驾驶的多模态特性，也无法有效评估长尾场景下的性能。为了解决这些差距，我们推出了Waymo端到端驾驶开放数据集(WOD-E2E)。WOD-E2E包含4021个驾驶片段（约12小时），专门为具有挑战性的长尾场景而设计，这些场景在日常生活中发生的频率低于0.03%。具体而言，WOD-E2E中的每个片段都包含高级路线信息、自车状态以及来自8个周围摄像头的360度摄像头视图。为了评估E2E驾驶在这些长尾情况下的性能，我们提出了一种新的开环评估指标：评分员反馈分数(RFS)。与测量预测路径点与日志之间距离的传统指标不同，RFS衡量预测轨迹与评分员标注的轨迹偏好标签的匹配程度。我们已经发布了所有WOD-E2E验证集片段的评分员偏好标签，而保留的测试集标签已用于2025年WOD-E2E挑战赛。通过我们的工作，我们旨在促进最先进的研究，以开发能够处理复杂现实世界情况的通用、鲁棒和安全的端到端自动驾驶代理。

## 🔬 方法详解

**问题定义**：现有端到端驾驶研究主要集中在常见驾驶场景，忽略了现实世界中大量存在的长尾场景，例如罕见交通状况、恶劣天气等。这些长尾场景虽然发生频率低，但往往对自动驾驶系统的安全性和可靠性至关重要。现有的开环评估指标，如轨迹距离误差，无法充分捕捉驾驶行为的多样性和安全性，尤其是在长尾场景下。

**核心思路**：论文的核心思路是构建一个包含大量长尾场景的数据集，并设计一种更符合人类驾驶习惯的评估指标。通过WOD-E2E数据集，研究人员可以更好地训练和评估自动驾驶系统在复杂和罕见情况下的表现。RFS指标则通过引入人工评分员的偏好信息，更准确地反映驾驶行为的合理性和安全性。

**技术框架**：WOD-E2E数据集包含4021个驾驶片段，每个片段包含：1) 高级路线信息；2) 自车状态；3) 来自8个环绕摄像头的360度图像。评估方面，使用提出的Rater Feedback Score (RFS) 指标，该指标基于人工评分员对不同轨迹的偏好进行评估。数据集分为验证集和测试集，验证集提供评分员偏好标签，测试集用于挑战赛评估。

**关键创新**：主要创新点在于：1) 数据集本身，WOD-E2E专注于长尾驾驶场景，弥补了现有数据集的不足；2) 评估指标RFS，通过引入人工评分员的偏好，更准确地评估驾驶行为的合理性和安全性。与传统基于距离的指标相比，RFS更能反映人类驾驶员的决策过程。

**关键设计**：RFS指标的具体计算方法未知，但其核心思想是利用人工评分员对不同轨迹的偏好进行排序或评分。评分员根据安全性、舒适性、效率等因素对轨迹进行评估，RFS指标则基于这些评分结果来衡量预测轨迹的质量。数据集的构建过程中，作者精心挑选了发生频率低于0.03%的罕见场景，以保证数据集的长尾特性。

## 📊 实验亮点

论文发布了包含4021个驾驶片段的WOD-E2E数据集，专注于发生频率低于0.03%的长尾场景。同时，提出了新的评估指标RFS，通过人工评分员的偏好来评估驾驶行为。验证集已发布评分员偏好标签，测试集用于2025年WOD-E2E挑战赛，旨在推动自动驾驶领域的研究。

## 🎯 应用场景

该研究成果可应用于自动驾驶系统的开发和测试，尤其是在提高系统应对复杂和罕见场景的能力方面。通过使用WOD-E2E数据集和RFS评估指标，可以更有效地训练和评估自动驾驶系统，从而提高其安全性和可靠性。此外，该数据集和评估方法也可以促进自动驾驶领域的研究进展，推动更通用、鲁棒和安全的自动驾驶技术的发展。

## 📄 摘要（原文）

> Vision-based end-to-end (E2E) driving has garnered significant interest in the research community due to its scalability and synergy with multimodal large language models (MLLMs). However, current E2E driving benchmarks primarily feature nominal scenarios, failing to adequately test the true potential of these systems. Furthermore, existing open-loop evaluation metrics often fall short in capturing the multi-modal nature of driving or effectively evaluating performance in long-tail scenarios. To address these gaps, we introduce the Waymo Open Dataset for End-to-End Driving (WOD-E2E). WOD-E2E contains 4,021 driving segments (approximately 12 hours), specifically curated for challenging long-tail scenarios that that are rare in daily life with an occurring frequency of less than 0.03%. Concretely, each segment in WOD-E2E includes the high-level routing information, ego states, and 360-degree camera views from 8 surrounding cameras. To evaluate the E2E driving performance on these long-tail situations, we propose a novel open-loop evaluation metric: Rater Feedback Score (RFS). Unlike conventional metrics that measure the distance between predicted way points and the logs, RFS measures how closely the predicted trajectory matches rater-annotated trajectory preference labels. We have released rater preference labels for all WOD-E2E validation set segments, while the held out test set labels have been used for the 2025 WOD-E2E Challenge. Through our work, we aim to foster state of the art research into generalizable, robust, and safe end-to-end autonomous driving agents capable of handling complex real-world situations.

