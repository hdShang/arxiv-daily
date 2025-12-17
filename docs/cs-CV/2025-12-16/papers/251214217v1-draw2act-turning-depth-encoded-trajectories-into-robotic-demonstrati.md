---
layout: default
title: DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos
---

# DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14217" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14217v1</a>
  <a href="https://arxiv.org/pdf/2512.14217.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14217v1" onclick="toggleFavorite(this, '2512.14217v1', 'DRAW2ACT: Turning Depth-Encoded Trajectories into Robotic Demonstration Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yang Bai, Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Ziyuan Liu, Gitta Kutyniok

**分类**: cs.CV, cs.RO

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出DRAW2ACT以解决机器人演示视频生成的可控性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `视频生成` `机器人演示` `多模态融合` `深度学习` `轨迹条件生成`

## 📋 核心要点

1. 现有的轨迹条件视频生成方法通常依赖于二维轨迹或单一模态，导致生成的机器人演示缺乏可控性和一致性。
2. 本文提出的DRAW2ACT框架通过提取深度、语义、形状和运动等多种正交表示，增强了视频生成的多模态特性。
3. 在Bridge V2、Berkeley Autolab和仿真基准上的实验表明，DRAW2ACT在视觉质量和一致性上显著优于现有方法，并提高了操作成功率。

## 📝 摘要（中文）

视频扩散模型为具身人工智能提供了强大的现实世界模拟器，但在机器人操作的可控性方面仍然有限。近期的轨迹条件视频生成研究虽然填补了这一空白，但通常依赖于二维轨迹或单一模态条件，限制了其生成可控且一致的机器人演示的能力。本文提出了DRAW2ACT，一个深度感知的轨迹条件视频生成框架，从输入轨迹中提取多个正交表示，捕捉深度、语义、形状和运动，并将其注入扩散模型。此外，我们提出联合生成空间对齐的RGB和深度视频，利用跨模态注意机制和深度监督来增强时空一致性。最后，我们引入一个多模态策略模型，基于生成的RGB和深度序列回归机器人的关节角度。实验结果表明，DRAW2ACT在视觉保真度和一致性方面优于现有基线，同时提高了操作成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决现有轨迹条件视频生成方法在机器人演示中的可控性和一致性不足的问题。现有方法多依赖于二维轨迹或单一模态，导致生成结果的局限性。

**核心思路**：DRAW2ACT框架的核心思想是通过深度感知的轨迹条件生成视频，提取多种正交表示（如深度、语义、形状和运动），并将其注入到扩散模型中，以增强生成视频的可控性和一致性。

**技术框架**：该框架包括多个主要模块：首先，从输入轨迹中提取多模态特征；其次，利用跨模态注意机制生成空间对齐的RGB和深度视频；最后，基于生成的视频序列回归机器人的关节角度。

**关键创新**：最重要的创新点在于联合生成RGB和深度视频，并通过跨模态注意机制和深度监督来增强时空一致性。这一设计与现有方法的本质区别在于多模态融合的深度感知能力。

**关键设计**：在参数设置上，采用了深度监督损失函数以提升深度信息的准确性，同时设计了特定的网络结构以支持多模态特征的提取和融合。

## 📊 实验亮点

实验结果显示，DRAW2ACT在视觉保真度和一致性方面显著优于现有基线，具体表现为在操作成功率上提高了XX%（具体数据未知），并在多个基准测试中展现出更好的性能。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动化生产线和人机交互等场景。通过提升机器人在复杂环境中的操作能力，DRAW2ACT能够为实际应用提供更高的灵活性和可靠性，推动机器人技术的进一步发展。

## 📄 摘要（原文）

> Video diffusion models provide powerful real-world simulators for embodied AI but remain limited in controllability for robotic manipulation. Recent works on trajectory-conditioned video generation address this gap but often rely on 2D trajectories or single modality conditioning, which restricts their ability to produce controllable and consistent robotic demonstrations. We present DRAW2ACT, a depth-aware trajectory-conditioned video generation framework that extracts multiple orthogonal representations from the input trajectory, capturing depth, semantics, shape and motion, and injects them into the diffusion model. Moreover, we propose to jointly generate spatially aligned RGB and depth videos, leveraging cross-modality attention mechanisms and depth supervision to enhance the spatio-temporal consistency. Finally, we introduce a multimodal policy model conditioned on the generated RGB and depth sequences to regress the robot's joint angles. Experiments on Bridge V2, Berkeley Autolab, and simulation benchmarks show that DRAW2ACT achieves superior visual fidelity and consistency while yielding higher manipulation success rates compared to existing baselines.

