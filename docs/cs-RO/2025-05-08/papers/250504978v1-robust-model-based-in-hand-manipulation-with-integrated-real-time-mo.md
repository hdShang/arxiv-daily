---
layout: default
title: Robust Model-Based In-Hand Manipulation with Integrated Real-Time Motion-Contact Planning and Tracking
---

# Robust Model-Based In-Hand Manipulation with Integrated Real-Time Motion-Contact Planning and Tracking

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.04978" class="toolbar-btn" target="_blank">📄 arXiv: 2505.04978v1</a>
  <a href="https://arxiv.org/pdf/2505.04978.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.04978v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.04978v1', 'Robust Model-Based In-Hand Manipulation with Integrated Real-Time Motion-Contact Planning and Tracking')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yongpeng Jiang, Mingrui Yu, Xinghao Zhu, Masayoshi Tomizuka, Xiang Li

**分类**: cs.RO

**发布日期**: 2025-05-08

**备注**: Submitted to the International Journal of Robotics Research (IJRR)

---

## 💡 一句话要点

**提出集成实时运动接触规划与跟踪的稳健模型基础手内操作方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人手内操作` `模型基础方法` `实时规划` `运动接触建模` `稳健性` `动态环境` `人类般灵巧`

## 📋 核心要点

1. 现有模型基础方法在处理复杂物理接触时面临高效在线规划和建模误差处理的挑战，限制了其实际应用。
2. 本文提出的集成框架通过层次结构实现实时规划与跟踪，并通过运动-接触建模的联合优化来增强操作的稳健性。
3. 实验结果显示，所提方法在准确性、稳健性和实时性能上均优于现有方法，成功应对多种复杂任务。

## 📝 摘要（中文）

机器人灵巧的手内操作，即多个手指动态地建立和断开接触，代表了朝向人类般灵巧的机器人应用的一步。与依赖大规模训练或特定任务数据收集的学习方法不同，模型基础方法提供了一种高效的替代方案。本文提出了一种新颖的集成框架，通过集成实时规划和跟踪以及运动-接触建模的联合优化，克服了现有模型基础方法在高效在线规划和处理建模误差方面的挑战。实验表明，该方法在准确性、稳健性和实时性能方面优于现有模型基础方法，成功完成了五个在现实环境中的挑战任务，即使在显著的外部干扰下也能有效操作。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人手内操作中由于物理接触复杂性导致的高效在线规划和建模误差处理的挑战。现有模型基础方法在这些方面存在明显不足，限制了其在实际应用中的有效性。

**核心思路**：论文的核心思路是通过集成实时规划与跟踪，以及运动和接触的联合优化，来提升模型基础方法在接触丰富的手内操作中的有效性和稳健性。这样的设计使得机器人能够在动态环境中更灵活地应对各种操作任务。

**技术框架**：整体架构分为高层和低层两个模块。高层模块使用接触隐式模型预测控制生成手指运动和接触力的参考，支持实时规划和扰动恢复；低层模块则利用手部力-运动模型和实际触觉反馈来跟踪这些参考，补偿建模误差。

**关键创新**：本文的关键创新在于将实时规划与跟踪集成在一个层次结构中，并通过运动-接触建模的联合优化来提升操作的稳健性。这与现有方法的分离处理方式形成了鲜明对比，显著提高了操作的灵活性和准确性。

**关键设计**：在高层模块中，采用了接触隐式模型预测控制来生成参考信号；低层模块则结合了手部力-运动模型和触觉反馈，确保了对建模误差的有效补偿。

## 📊 实验亮点

实验结果表明，所提方法在准确性、稳健性和实时性能方面均优于现有模型基础方法。在五个复杂任务中，成功应对显著的外部干扰，显示出较高的操作成功率和稳定性。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、医疗机器人和工业自动化等。通过实现更灵活和稳健的手内操作，机器人能够在复杂和动态的环境中执行更广泛的任务，提升其在实际应用中的价值和影响力。

## 📄 摘要（原文）

> Robotic dexterous in-hand manipulation, where multiple fingers dynamically make and break contact, represents a step toward human-like dexterity in real-world robotic applications. Unlike learning-based approaches that rely on large-scale training or extensive data collection for each specific task, model-based methods offer an efficient alternative. Their online computing nature allows for ready application to new tasks without extensive retraining. However, due to the complexity of physical contacts, existing model-based methods encounter challenges in efficient online planning and handling modeling errors, which limit their practical applications. To advance the effectiveness and robustness of model-based contact-rich in-hand manipulation, this paper proposes a novel integrated framework that mitigates these limitations. The integration involves two key aspects: 1) integrated real-time planning and tracking achieved by a hierarchical structure; and 2) joint optimization of motions and contacts achieved by integrated motion-contact modeling. Specifically, at the high level, finger motion and contact force references are jointly generated using contact-implicit model predictive control. The high-level module facilitates real-time planning and disturbance recovery. At the low level, these integrated references are concurrently tracked using a hand force-motion model and actual tactile feedback. The low-level module compensates for modeling errors and enhances the robustness of manipulation. Extensive experiments demonstrate that our approach outperforms existing model-based methods in terms of accuracy, robustness, and real-time performance. Our method successfully completes five challenging tasks in real-world environments, even under appreciable external disturbances.

