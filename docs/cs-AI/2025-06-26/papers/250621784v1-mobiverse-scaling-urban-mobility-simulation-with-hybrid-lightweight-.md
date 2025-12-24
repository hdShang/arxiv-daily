---
layout: default
title: "MobiVerse: Scaling Urban Mobility Simulation with Hybrid Lightweight Domain-Specific Generator and Large Language Models"
---

# MobiVerse: Scaling Urban Mobility Simulation with Hybrid Lightweight Domain-Specific Generator and Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21784" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21784v1</a>
  <a href="https://arxiv.org/pdf/2506.21784.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21784v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21784v1', 'MobiVerse: Scaling Urban Mobility Simulation with Hybrid Lightweight Domain-Specific Generator and Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifan Liu, Xishun Liao, Haoxuan Ma, Jonathan Liu, Rohan Jadhav, Jiaqi Ma

**分类**: cs.AI

**发布日期**: 2025-06-26

**🔗 代码/项目**: [GITHUB](https://github.com/ucla-mobility/MobiVerse)

---

## 💡 一句话要点

**提出MobiVerse以解决城市交通模拟的效率与适应性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `城市交通模拟` `大型语言模型` `混合框架` `活动链生成` `环境反馈` `计算效率` `行为真实感`

## 📋 核心要点

1. 现有的交通模拟平台在算法开发和政策实施方面存在效率低下和适应性不足的问题。
2. MobiVerse框架结合了轻量级生成器与大型语言模型，能够高效生成和动态调整活动链。
3. 实验结果显示，MobiVerse在处理环境反馈时保持了计算效率，并提升了行为的真实感。

## 📝 摘要（中文）

理解和建模人类移动模式对于有效的交通规划和城市发展至关重要。尽管在移动性研究方面取得了显著进展，但在允许算法开发、政策实施和全面评估的大规模模拟平台方面仍存在关键差距。传统的基于活动的模型需要大量数据收集和手动校准，机器学习方法在动态条件下的适应性不足，而基于代理的语言模型在大规模模拟中面临计算限制。为了解决这些挑战，本文提出了MobiVerse，一个混合框架，利用轻量级领域特定生成器的效率生成基础活动链，并结合大型语言模型的上下文感知修改能力。通过在洛杉矶Westwood的案例研究，我们在标准PC上高效生成并动态调整了约53,000个代理的日程安排。实验表明，MobiVerse成功使代理能够响应环境反馈，保持计算效率的同时增强行为的真实感。

## 🔬 方法详解

**问题定义**：本文旨在解决现有交通模拟平台在算法开发和政策实施中的效率低下和适应性不足的问题。传统模型需要大量数据和手动校准，而机器学习方法在动态环境中的适应性较差。

**核心思路**：MobiVerse框架通过结合轻量级领域特定生成器和大型语言模型，提供了一种高效且灵活的解决方案，能够生成基础活动链并进行上下文感知的动态调整。

**技术框架**：MobiVerse的整体架构包括两个主要模块：轻量级生成器用于生成基础活动链，LLM用于根据环境反馈进行动态调整。该框架支持在标准PC上处理大规模代理的调度。

**关键创新**：MobiVerse的创新在于其混合框架设计，能够在保持计算效率的同时，增强代理的行为真实感。这一设计与传统模型的静态和低效特性形成鲜明对比。

**关键设计**：在MobiVerse中，关键的参数设置和网络结构设计使得生成器能够快速生成活动链，而LLM则通过上下文信息进行动态调整，确保了系统的灵活性和适应性。具体的损失函数和优化策略在论文中进行了详细讨论。

## 📊 实验亮点

实验结果表明，MobiVerse能够在标准PC上高效处理约53,000个代理的调度，成功响应环境变化，如道路封闭和大型活动，保持计算效率的同时，行为真实感提升显著。

## 🎯 应用场景

MobiVerse的研究成果在城市交通规划、政策评估和应急管理等领域具有广泛的应用潜力。通过提供一个可定制的平台，城市规划者和政策制定者可以更有效地模拟和优化交通系统，提升城市的可持续发展能力。

## 📄 摘要（原文）

> Understanding and modeling human mobility patterns is crucial for effective transportation planning and urban development. Despite significant advances in mobility research, there remains a critical gap in simulation platforms that allow for algorithm development, policy implementation, and comprehensive evaluation at scale. Traditional activity-based models require extensive data collection and manual calibration, machine learning approaches struggle with adaptation to dynamic conditions, and treding agent-based Large Language Models (LLMs) implementations face computational constraints with large-scale simulations. To address these challenges, we propose MobiVerse, a hybrid framework leverages the efficiency of lightweight domain-specific generator for generating base activity chains with the adaptability of LLMs for context-aware modifications. A case study was conducted in Westwood, Los Angeles, where we efficiently generated and dynamically adjusted schedules for the whole population of approximately 53,000 agents on a standard PC. Our experiments demonstrate that MobiVerse successfully enables agents to respond to environmental feedback, including road closures, large gathering events like football games, and congestion, through our hybrid framework. Its modular design facilitates testing various mobility algorithms at both transportation system and agent levels. Results show our approach maintains computational efficiency while enhancing behavioral realism. MobiVerse bridges the gap in mobility simulation by providing a customizable platform for mobility systems planning and operations with benchmark algorithms. Code and videos are available at https://github.com/ucla-mobility/MobiVerse.

