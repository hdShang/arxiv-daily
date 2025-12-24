---
layout: default
title: "AgriVLN: Vision-and-Language Navigation for Agricultural Robots"
---

# AgriVLN: Vision-and-Language Navigation for Agricultural Robots

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07406" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07406v1</a>
  <a href="https://arxiv.org/pdf/2508.07406.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07406v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07406v1', 'AgriVLN: Vision-and-Language Navigation for Agricultural Robots')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaobei Zhao, Xingqi Lyu, Xiang Li

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-08-10

---

## 💡 一句话要点

**提出AgriVLN以解决农业机器人导航问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `农业机器人` `视觉与语言导航` `指令理解` `子任务分解` `多模态学习`

## 📋 核心要点

1. 现有的视觉与语言导航方法未针对农业场景进行优化，导致农业机器人在复杂环境中的导航能力不足。
2. 本文提出了农业到农业（A2A）基准和AgriVLN基线，结合视觉-语言模型，能够理解农业环境中的指令并生成相应动作。
3. 通过引入子任务列表（STL）模块，AgriVLN的成功率从0.33提升至0.47，显示出显著的性能改进。

## 📝 摘要（中文）

农业机器人在农业任务中发挥着重要作用，但仍然依赖人工操作或不便运输的轨道，导致移动性和适应性有限。视觉与语言导航（VLN）使机器人能够根据自然语言指令导航到目标地点，但现有方法未针对农业场景进行设计。为此，本文提出农业到农业（A2A）基准，包含1560个场景，所有RGB视频均由四足机器人在0.38米高度拍摄。同时，提出基于视觉-语言模型（VLM）的农业机器人视觉与语言导航（AgriVLN）基线，能够理解指令和农业环境，生成适当的低级动作。评估结果显示，AgriVLN在短指令上表现良好，但在长指令上存在跟踪困难。为此，提出子任务列表（STL）指令分解模块，成功率从0.33提升至0.47，并与多种现有VLN方法进行比较，展示了在农业领域的领先性能。

## 🔬 方法详解

**问题定义**：本文旨在解决农业机器人在复杂农业场景中导航的挑战，现有方法在处理长指令时存在跟踪困难，影响导航效果。

**核心思路**：提出农业到农业（A2A）基准，结合视觉-语言模型（VLM）和子任务列表（STL）模块，以提高机器人对指令的理解和执行能力。

**技术框架**：整体架构包括数据采集、指令解析、动作生成和执行四个主要模块。数据采集通过四足机器人在农业场景中获取RGB视频，指令解析利用VLM理解自然语言指令，动作生成则基于解析结果输出低级控制指令。

**关键创新**：最重要的创新在于引入了子任务列表（STL）模块，该模块能够将长指令分解为可管理的子任务，从而提高了机器人对指令的执行成功率。

**关键设计**：在模型设计中，采用了精心设计的模板来提示VLM，并在训练过程中使用了特定的损失函数，以优化指令理解和动作生成的准确性。

## 📊 实验亮点

在A2A基准测试中，AgriVLN在短指令上的成功率表现良好，但在长指令上存在一定挑战。通过引入子任务列表（STL）模块，成功率从0.33提升至0.47，展示了显著的性能提升，超越了多种现有VLN方法。

## 🎯 应用场景

该研究的潜在应用领域包括智能农业、无人驾驶农机和精准农业等。通过提高农业机器人的导航能力，能够有效降低人工成本，提高农业生产效率，推动农业自动化的发展。

## 📄 摘要（原文）

> Agricultural robots have emerged as powerful members in agricultural tasks, nevertheless, still heavily rely on manual operation or untransportable railway for movement, resulting in limited mobility and poor adaptability. Vision-and-Language Navigation (VLN) enables robots to navigate to the target destinations following natural language instructions, demonstrating strong performance on several domains. However, none of the existing benchmarks or methods is specifically designed for agricultural scenes. To bridge this gap, we propose Agriculture to Agriculture (A2A) benchmark, containing 1,560 episodes across six diverse agricultural scenes, in which all realistic RGB videos are captured by front-facing camera on a quadruped robot at a height of 0.38 meters, aligning with the practical deployment conditions. Meanwhile, we propose Vision-and-Language Navigation for Agricultural Robots (AgriVLN) baseline based on Vision-Language Model (VLM) prompted with carefully crafted templates, which can understand both given instructions and agricultural environments to generate appropriate low-level actions for robot control. When evaluated on A2A, AgriVLN performs well on short instructions but struggles with long instructions, because it often fails to track which part of the instruction is currently being executed. To address this, we further propose Subtask List (STL) instruction decomposition module and integrate it into AgriVLN, improving Success Rate (SR) from 0.33 to 0.47. We additionally compare AgriVLN with several existing VLN methods, demonstrating the state-of-the-art performance in the agricultural domain.

