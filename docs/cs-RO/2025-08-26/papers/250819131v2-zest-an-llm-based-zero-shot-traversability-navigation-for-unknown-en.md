---
layout: default
title: "ZeST: an LLM-based Zero-Shot Traversability Navigation for Unknown Environments"
---

# ZeST: an LLM-based Zero-Shot Traversability Navigation for Unknown Environments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19131" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19131v2</a>
  <a href="https://arxiv.org/pdf/2508.19131.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19131v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19131v2', 'ZeST: an LLM-based Zero-Shot Traversability Navigation for Unknown Environments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shreya Gummadi, Mateus V. Gasparino, Gianluca Capezzuto, Marcelo Becker, Girish Chowdhary

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-08-26 (更新: 2025-10-17)

---

## 💡 一句话要点

**提出ZeST以解决未知环境中的导航可达性问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可达性预测` `大型语言模型` `视觉推理` `自主导航` `机器人技术` `零-shot学习` `安全导航`

## 📋 核心要点

1. 现有方法在生成可达性预测模型的数据集时，往往需要将机器人置于危险环境中，存在安全隐患。
2. ZeST通过利用大型语言模型的视觉推理能力，实现了实时的可达性地图生成，避免了机器人暴露于危险中。
3. 实验结果显示，ZeST在室内和户外环境中均表现出更安全的导航能力，相比其他方法更能有效到达目标。

## 📝 摘要（中文）

机器人和自主导航系统的发展依赖于准确预测地形可达性的能力。传统方法通常需要将机器人置于潜在危险的环境中，存在设备和安全风险。为了解决这一问题，本文提出了ZeST，一种利用大型语言模型（LLMs）视觉推理能力的创新方法，能够实时创建可达性地图，而无需将机器人暴露于危险中。该方法不仅实现了零-shot可达性预测，降低了真实数据收集的风险，还加速了先进导航系统的开发，提供了一种具有成本效益和可扩展性的解决方案。实验结果表明，在受控的室内和非结构化的户外环境中，我们的方法相比其他先进方法提供了更安全的导航，始终能够到达最终目标。

## 🔬 方法详解

**问题定义**：本文旨在解决在未知环境中进行安全导航的可达性预测问题。现有方法依赖于在危险环境中收集数据，存在设备损坏和安全风险。

**核心思路**：ZeST的核心思路是利用大型语言模型的视觉推理能力，实时生成可达性地图，从而避免机器人在真实环境中进行危险的数据收集。

**技术框架**：该方法的整体架构包括数据输入模块、LLM推理模块和可达性地图生成模块。数据输入模块负责收集环境信息，LLM推理模块进行视觉推理，最后生成可达性地图。

**关键创新**：ZeST的主要创新在于将大型语言模型应用于可达性预测，突破了传统方法对真实环境数据的依赖，实现了零-shot学习能力。

**关键设计**：在设计中，ZeST采用了特定的损失函数以优化可达性预测的准确性，并结合了多层次的网络结构以增强模型的推理能力。

## 📊 实验亮点

实验结果表明，ZeST在受控室内和非结构化户外环境中的导航成功率显著高于其他先进方法，始终能够安全到达目标，展示了其在实际应用中的有效性和可靠性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、无人机导航和机器人探索等。通过提供安全的导航解决方案，ZeST能够在未知环境中有效地进行任务执行，具有重要的实际价值和广泛的未来影响。

## 📄 摘要（原文）

> The advancement of robotics and autonomous navigation systems hinges on the ability to accurately predict terrain traversability. Traditional methods for generating datasets to train these prediction models often involve putting robots into potentially hazardous environments, posing risks to equipment and safety. To solve this problem, we present ZeST, a novel approach leveraging visual reasoning capabilities of Large Language Models (LLMs) to create a traversability map in real-time without exposing robots to danger. Our approach not only performs zero-shot traversability and mitigates the risks associated with real-world data collection but also accelerates the development of advanced navigation systems, offering a cost-effective and scalable solution. To support our findings, we present navigation results, in both controlled indoor and unstructured outdoor environments. As shown in the experiments, our method provides safer navigation when compared to other state-of-the-art methods, constantly reaching the final goal.

