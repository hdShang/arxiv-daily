---
layout: default
title: "HMVLM: Multistage Reasoning-Enhanced Vision-Language Model for Long-Tailed Driving Scenarios"
---

# HMVLM: Multistage Reasoning-Enhanced Vision-Language Model for Long-Tailed Driving Scenarios

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05883" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05883v1</a>
  <a href="https://arxiv.org/pdf/2506.05883.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05883v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05883v1', 'HMVLM: Multistage Reasoning-Enhanced Vision-Language Model for Long-Tailed Driving Scenarios')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Daming Wang, Yuhao Song, Zijian He, Kangliang Chen, Xing Pan, Lu Deng, Weihao Gu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-06

**备注**: WOD Vision-based End-to-End Driving Challenge

---

## 💡 一句话要点

**提出HMVLM以解决长尾驾驶场景中的决策问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长尾驾驶` `视觉-语言模型` `快慢架构` `多阶段推理` `轨迹规划` `自动驾驶` `决策优化`

## 📋 核心要点

1. 现有方法在长尾驾驶场景中面临决策延迟和准确性不足的挑战。
2. 论文提出的HMVLM通过快慢架构结合视觉-语言模型，优化了驾驶决策流程。
3. 实验结果显示，HMVLM在Waymo挑战中取得了优异成绩，显著提升了评分。

## 📝 摘要（中文）

我们提出了HaoMo视觉-语言模型（HMVLM），这是一个端到端的驾驶框架，采用了受认知启发的快慢架构。快速控制器输出低级别的转向、油门和刹车指令，而慢速规划器——一个大型视觉-语言模型——生成高层次的意图，如“让行给行人”或“在卡车后并入”。HMVLM引入了三项升级：选择性五视图提示，嵌入4秒的自我运动历史；多阶段思维链提示，强制执行场景理解、驾驶决策和轨迹推断的推理流程；基于样条的轨迹后处理，消除后期抖动和急转弯。经过在Waymo开放数据集上的训练，这些升级使HMVLM在2025年Waymo基于视觉的端到端驾驶挑战中获得了7.7367的评分，排名第二，超越公共基线2.77%。

## 🔬 方法详解

**问题定义**：本论文旨在解决长尾驾驶场景中决策延迟和准确性不足的问题。现有方法在复杂场景下难以快速做出合理的驾驶决策，导致安全性和效率的降低。

**核心思路**：HMVLM采用快慢架构，快速控制器负责实时低级别指令输出，而慢速规划器则利用大型视觉-语言模型生成高层次的驾驶意图。这种设计旨在平衡决策的速度与准确性。

**技术框架**：HMVLM的整体架构包括两个主要模块：快速控制器和慢速规划器。快速控制器实时处理传感器数据并输出低级别控制指令，慢速规划器则通过多阶段推理生成高层次的驾驶决策。

**关键创新**：HMVLM的三项关键创新包括选择性五视图提示、强制推理流程的多阶段思维链提示，以及基于样条的轨迹后处理。这些创新使得模型在复杂场景下的决策能力显著提升。

**关键设计**：在模型设计中，选择性五视图提示结合了4秒的自我运动历史，以增强场景理解；多阶段思维链提示确保了推理流程的连贯性；样条轨迹后处理则有效减少了决策后的抖动和急转弯现象。

## 📊 实验亮点

HMVLM在2025年Waymo基于视觉的端到端驾驶挑战中取得了7.7367的评分，排名第二，超越公共基线2.77%。这一成绩展示了其在长尾驾驶场景中的优越性能，特别是在复杂决策和轨迹规划方面的显著提升。

## 🎯 应用场景

HMVLM的研究成果在自动驾驶领域具有广泛的应用潜力，特别是在复杂和动态的城市驾驶环境中。通过提高决策的准确性和实时性，该模型能够显著提升自动驾驶系统的安全性和用户体验，未来可应用于无人驾驶出租车、物流运输等场景。

## 📄 摘要（原文）

> We present HaoMo Vision-Language Model (HMVLM), an end-to-end driving framework that implements the slow branch of a cognitively inspired fast-slow architecture. A fast controller outputs low-level steering, throttle, and brake commands, while a slow planner-a large vision-language model-generates high-level intents such as "yield to pedestrian" or "merge after the truck" without compromising latency. HMVLM introduces three upgrades: (1) selective five-view prompting with an embedded 4s history of ego kinematics, (2) multi-stage chain-of-thought (CoT) prompting that enforces a Scene Understanding -> Driving Decision -> Trajectory Inference reasoning flow, and (3) spline-based trajectory post-processing that removes late-stage jitter and sharp turns. Trained on the Waymo Open Dataset, these upgrades enable HMVLM to achieve a Rater Feedback Score (RFS) of 7.7367, securing 2nd place in the 2025 Waymo Vision-based End-to-End (E2E) Driving Challenge and surpassing the public baseline by 2.77%.

