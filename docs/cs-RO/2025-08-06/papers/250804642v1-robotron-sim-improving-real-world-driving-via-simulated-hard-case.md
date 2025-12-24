---
layout: default
title: "RoboTron-Sim: Improving Real-World Driving via Simulated Hard-Case"
---

# RoboTron-Sim: Improving Real-World Driving via Simulated Hard-Case

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04642" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04642v1</a>
  <a href="https://arxiv.org/pdf/2508.04642.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04642v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04642v1', 'RoboTron-Sim: Improving Real-World Driving via Simulated Hard-Case')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Baihui Xiao, Chengjian Feng, Zhijian Huang, Feng yan, Yujie Zhong, Lin Ma

**分类**: cs.RO, cs.CV

**发布日期**: 2025-08-06

**备注**: ICCV 2025

**🔗 代码/项目**: [PROJECT_PAGE](https://stars79689.github.io/RoboTron-Sim/)

---

## 💡 一句话要点

**提出RoboTron-Sim以改善高风险驾驶场景下的自动驾驶性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `高风险场景` `模拟数据集` `多模态学习` `场景感知`

## 📋 核心要点

1. 现有自动驾驶系统在稀有高风险场景和复杂交互中表现不佳，导致安全性和可靠性不足。
2. 提出RoboTron-Sim，通过模拟困难案例和开发HASS数据集，增强自动驾驶系统在高风险场景下的学习能力。
3. 实验结果显示，RoboTron-Sim在nuScenes数据集上提升了约50%的驾驶性能，展示了其在实际应用中的有效性。

## 📝 摘要（中文）

收集稀有高风险场景、长尾驾驶事件和复杂交互的真实数据仍然具有挑战性，导致现有自动驾驶系统在这些关键情况下表现不佳。本文提出RoboTron-Sim，通过利用模拟的困难案例来改善现实世界的驾驶。首先，我们开发了一个名为Hard-case Augmented Synthetic Scenarios (HASS)的模拟数据集，涵盖13个高风险边缘案例类别，以及日/night和晴/雨等平衡环境条件。其次，我们引入了场景感知提示工程（SPE）和图像到自我编码器（I2E Encoder），使多模态大型语言模型能够有效地从HASS中学习现实世界的挑战性驾驶技能，适应现实与模拟场景之间的环境偏差和硬件差异。大量实验表明，RoboTron-Sim在挑战性场景中的驾驶性能提高了约50%，在现实世界的开放环规划中达到了最先进的结果。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自动驾驶系统在稀有高风险驾驶场景中的性能不足，尤其是在复杂交互和长尾事件中的表现。现有方法在收集真实数据方面面临挑战，导致系统在关键情况下的表现不佳。

**核心思路**：论文提出RoboTron-Sim，通过构建模拟的困难案例数据集（HASS），帮助自动驾驶系统在高风险场景中进行有效学习。通过引入场景感知提示工程（SPE）和图像到自我编码器（I2E Encoder），实现对环境变化的适应。

**技术框架**：整体架构包括数据集构建、模型训练和性能评估三个主要阶段。首先，生成HASS数据集以覆盖多种高风险场景；其次，利用SPE和I2E Encoder进行模型训练；最后，通过在nuScenes数据集上的实验评估模型性能。

**关键创新**：最重要的创新在于HASS数据集的构建和SPE、I2E Encoder的引入，使得多模态大型语言模型能够更好地适应现实与模拟场景之间的差异。这一方法显著提升了模型在复杂场景中的学习能力。

**关键设计**：在模型训练中，采用了特定的损失函数以平衡不同场景的学习效果，并设计了适应性强的网络结构，以应对环境变化和硬件差异。

## 📊 实验亮点

实验结果表明，RoboTron-Sim在nuScenes数据集上的驾驶性能提升约50%，在现实世界的开放环规划中达到了最先进的结果。这一显著提升证明了该方法在处理高风险驾驶场景中的有效性和实用性。

## 🎯 应用场景

RoboTron-Sim的研究成果在自动驾驶领域具有广泛的应用潜力，尤其是在高风险驾驶场景的安全性提升方面。通过有效学习复杂场景中的驾驶技能，该方法能够增强自动驾驶系统的可靠性，降低事故风险，推动智能交通的发展。未来，该技术还可扩展至其他需要处理复杂环境的机器人系统。

## 📄 摘要（原文）

> Collecting real-world data for rare high-risk scenarios, long-tailed driving events, and complex interactions remains challenging, leading to poor performance of existing autonomous driving systems in these critical situations. In this paper, we propose RoboTron-Sim that improves real-world driving in critical situations by utilizing simulated hard cases. First, we develop a simulated dataset called Hard-case Augmented Synthetic Scenarios (HASS), which covers 13 high-risk edge-case categories, as well as balanced environmental conditions such as day/night and sunny/rainy. Second, we introduce Scenario-aware Prompt Engineering (SPE) and an Image-to-Ego Encoder (I2E Encoder) to enable multimodal large language models to effectively learn real-world challenging driving skills from HASS, via adapting to environmental deviations and hardware differences between real-world and simulated scenarios. Extensive experiments on nuScenes show that RoboTron-Sim improves driving performance in challenging scenarios by around 50%, achieving state-of-the-art results in real-world open-loop planning. Qualitative results further demonstrate the effectiveness of RoboTron-Sim in better managing rare high-risk driving scenarios. Project page: https://stars79689.github.io/RoboTron-Sim/

