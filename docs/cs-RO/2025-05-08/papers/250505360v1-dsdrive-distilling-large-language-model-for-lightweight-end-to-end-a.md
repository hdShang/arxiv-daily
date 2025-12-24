---
layout: default
title: DSDrive: Distilling Large Language Model for Lightweight End-to-End Autonomous Driving with Unified Reasoning and Planning
---

# DSDrive: Distilling Large Language Model for Lightweight End-to-End Autonomous Driving with Unified Reasoning and Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05360" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05360v1</a>
  <a href="https://arxiv.org/pdf/2505.05360.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05360v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05360v1', 'DSDrive: Distilling Large Language Model for Lightweight End-to-End Autonomous Driving with Unified Reasoning and Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenru Liu, Pei Liu, Jun Ma

**分类**: cs.RO

**发布日期**: 2025-05-08

---

## 💡 一句话要点

**提出DSDrive以解决轻量化自主驾驶系统的推理与规划整合问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自主驾驶` `推理与规划` `轻量化模型` `蒸馏技术` `双头协调模块` `闭环仿真` `可解释性` `计算效率`

## 📋 核心要点

1. 现有自主驾驶系统在推理与规划的整合上存在不足，导致可解释性和可靠性较低。
2. DSDrive通过蒸馏方法构建紧凑的语言模型，并引入双头协调模块，实现推理与规划的有效对齐。
3. 在闭环仿真测试中，DSDrive在多个关键指标上超越基准模型，同时显著提升了计算效率。

## 📝 摘要（中文）

我们提出了DSDrive，这是一个精简的端到端框架，旨在将自主车辆的推理与规划整合到一个统一的体系中。DSDrive利用了一种紧凑的语言模型，通过蒸馏方法保留了大型视觉语言模型的增强推理能力。为有效对齐推理与规划任务，进一步开发了基于航点的双头协调模块，确保数据集结构、优化目标和学习过程的同步。通过将这些任务整合到统一框架中，DSDrive在规划结果的基础上融入了详细的推理见解，从而提高了端到端管道的可解释性和可靠性。DSDrive在闭环仿真中经过全面测试，性能与基准模型相当，且在多个关键指标上表现优异，同时体积更小。此外，DSDrive在推理过程中的计算效率显著提升，展现了轻量化系统在提供可解释和高效解决方案方面的潜力。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有自主驾驶系统在推理与规划整合方面的不足，尤其是在可解释性和计算效率方面的挑战。现有方法往往无法有效结合推理与规划，导致系统的整体性能受限。

**核心思路**：DSDrive的核心思想是通过蒸馏技术构建一个紧凑的语言模型，以保留大型视觉语言模型的推理能力，并通过双头协调模块实现推理与规划任务的有效对齐。这种设计旨在提升系统的可解释性和可靠性，同时降低计算资源的需求。

**技术框架**：DSDrive的整体架构包括数据预处理、推理模块、规划模块和双头协调模块。推理模块负责从传感器数据中提取信息，规划模块则基于推理结果生成驾驶决策，双头协调模块确保两者之间的同步与协调。

**关键创新**：DSDrive的主要创新在于引入了双头协调模块，该模块不仅同步了数据集结构和优化目标，还优化了学习过程，使得推理与规划能够在同一框架下高效运行。这一设计与现有方法的本质区别在于其统一性和高效性。

**关键设计**：在关键设计方面，DSDrive采用了特定的损失函数来平衡推理与规划的目标，同时在网络结构上进行了优化，以适应轻量化需求。参数设置经过精细调整，以确保在推理和规划任务中均能达到最佳性能。

## 📊 实验亮点

DSDrive在闭环仿真中的表现与基准模型相当，且在多个关键指标上超越了它们，展现出显著的性能提升。此外，DSDrive在推理过程中的时间和内存需求显著降低，显示出其计算效率的提升。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶汽车、智能交通系统和机器人导航等。DSDrive的轻量化设计使其能够在资源受限的环境中高效运行，具有广泛的实际价值和未来影响，尤其是在提升自主驾驶系统的可解释性和可靠性方面。

## 📄 摘要（原文）

> We present DSDrive, a streamlined end-to-end paradigm tailored for integrating the reasoning and planning of autonomous vehicles into a unified framework. DSDrive leverages a compact LLM that employs a distillation method to preserve the enhanced reasoning capabilities of a larger-sized vision language model (VLM). To effectively align the reasoning and planning tasks, a waypoint-driven dual-head coordination module is further developed, which synchronizes dataset structures, optimization objectives, and the learning process. By integrating these tasks into a unified framework, DSDrive anchors on the planning results while incorporating detailed reasoning insights, thereby enhancing the interpretability and reliability of the end-to-end pipeline. DSDrive has been thoroughly tested in closed-loop simulations, where it performs on par with benchmark models and even outperforms in many key metrics, all while being more compact in size. Additionally, the computational efficiency of DSDrive (as reflected in its time and memory requirements during inference) has been significantly enhanced. Evidently thus, this work brings promising aspects and underscores the potential of lightweight systems in delivering interpretable and efficient solutions for AD.

