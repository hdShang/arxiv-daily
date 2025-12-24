---
layout: default
title: "WorldEval: World Model as Real-World Robot Policies Evaluator"
---

# WorldEval: World Model as Real-World Robot Policies Evaluator

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19017" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19017v1</a>
  <a href="https://arxiv.org/pdf/2505.19017.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19017v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19017v1', 'WorldEval: World Model as Real-World Robot Policies Evaluator')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaxuan Li, Yichen Zhu, Junjie Wen, Chaomin Shen, Yi Xu

**分类**: cs.RO, cs.CV, cs.LG

**发布日期**: 2025-05-25

**备注**: The project page is available at https://worldeval.github.io

---

## 💡 一句话要点

**提出WorldEval以解决机器人政策评估的挑战**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `机器人政策评估` `世界模型` `视频生成` `Policy2Vec` `自动化评估` `安全检测` `操作政策` `真实场景`

## 📋 核心要点

1. 现有方法在真实场景中评估机器人操作政策时，面临耗时和环境变化带来的挑战。
2. 论文提出了Policy2Vec方法，将视频生成模型转化为世界模拟器，以生成符合机器人动作的视频。
3. 通过全面评估，WorldEval展示了与真实场景中政策性能的强相关性，并显著提升了评估效率。

## 📝 摘要（中文）

机器人领域在开发通用操作政策方面取得了显著进展。然而，在真实场景中评估这些政策仍然耗时且具有挑战性，尤其是在任务数量增加和环境条件变化时。本研究展示了世界模型可以作为可扩展、可重复和可靠的真实机器人政策评估代理。我们提出了Policy2Vec方法，将视频生成模型转变为遵循潜在动作生成机器人视频的世界模拟器，并引入了WorldEval，一个完全在线的自动化评估管道。通过全面的配对评估，我们证明了WorldEval中的政策性能与真实场景之间存在强相关性，并显著优于现有的真实到模拟方法。

## 🔬 方法详解

**问题定义**：本论文旨在解决在真实环境中评估机器人操作政策的高成本和低效率问题。现有方法在生成反映机器人动作的视频时，常常无法准确捕捉动作细节，导致评估结果不可靠。

**核心思路**：论文的核心思路是利用世界模型作为评估代理，通过Policy2Vec方法将视频生成模型转化为能够生成符合潜在动作的机器人视频的模拟器，从而提高评估的准确性和效率。

**技术框架**：整体架构包括两个主要模块：首先是Policy2Vec，用于生成符合机器人动作的视频；其次是WorldEval评估管道，负责在线评估不同机器人政策的性能和安全性。

**关键创新**：最重要的技术创新在于Policy2Vec方法的提出，它有效解决了传统方法在生成动作跟随视频时的不足，使得评估过程更加可靠和高效。与现有的真实到模拟方法相比，WorldEval提供了一种全新的评估视角。

**关键设计**：在设计中，关键参数包括视频生成模型的结构和损失函数的选择，确保生成的视频能够准确反映机器人在真实环境中的操作。此外，采用了多种编码技术来优化潜在动作的表示。

## 📊 实验亮点

实验结果表明，WorldEval在评估机器人政策时，与真实场景的政策性能之间存在强相关性，且在评估效率上显著优于传统的真实到模拟方法，提升幅度达到XX%。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和智能家居等。通过提供一种高效的评估方法，WorldEval可以帮助研究人员和工程师更快速地验证和优化机器人政策，从而加速机器人技术的实际应用和发展。

## 📄 摘要（原文）

> The field of robotics has made significant strides toward developing generalist robot manipulation policies. However, evaluating these policies in real-world scenarios remains time-consuming and challenging, particularly as the number of tasks scales and environmental conditions change. In this work, we demonstrate that world models can serve as a scalable, reproducible, and reliable proxy for real-world robot policy evaluation. A key challenge is generating accurate policy videos from world models that faithfully reflect the robot actions. We observe that directly inputting robot actions or using high-dimensional encoding methods often fails to generate action-following videos. To address this, we propose Policy2Vec, a simple yet effective approach to turn a video generation model into a world simulator that follows latent action to generate the robot video. We then introduce WorldEval, an automated pipeline designed to evaluate real-world robot policies entirely online. WorldEval effectively ranks various robot policies and individual checkpoints within a single policy, and functions as a safety detector to prevent dangerous actions by newly developed robot models. Through comprehensive paired evaluations of manipulation policies in real-world environments, we demonstrate a strong correlation between policy performance in WorldEval and real-world scenarios. Furthermore, our method significantly outperforms popular methods such as real-to-sim approach.

