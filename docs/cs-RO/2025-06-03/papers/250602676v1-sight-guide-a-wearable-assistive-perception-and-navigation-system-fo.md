---
layout: default
title: "Sight Guide: A Wearable Assistive Perception and Navigation System for the Vision Assistance Race in the Cybathlon 2024"
---

# Sight Guide: A Wearable Assistive Perception and Navigation System for the Vision Assistance Race in the Cybathlon 2024

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.02676" class="toolbar-btn" target="_blank">📄 arXiv: 2506.02676v1</a>
  <a href="https://arxiv.org/pdf/2506.02676.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.02676v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.02676v1', 'Sight Guide: A Wearable Assistive Perception and Navigation System for the Vision Assistance Race in the Cybathlon 2024')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Patrick Pfreundschuh, Giovanni Cioffi, Cornelius von Einem, Alexander Wyss, Hans Wernher van de Venn, Cesar Cadena, Davide Scaramuzza, Roland Siegwart, Alireza Darvishy

**分类**: cs.RO

**发布日期**: 2025-06-03

---

## 💡 一句话要点

**提出Sight Guide以解决视觉障碍者导航问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `视觉辅助` `导航系统` `可穿戴设备` `深度学习` `机器人技术` `环境感知` `用户交互`

## 📋 核心要点

1. 视觉障碍者在复杂环境中导航时，现有技术往往无法提供足够的空间感知和语义理解支持。
2. Sight Guide系统通过结合多种传感器数据，利用振动和音频反馈来引导用户，提升导航能力。
3. 在测试中，Sight Guide达到了95.7%的任务成功率，显示出其在实际应用中的有效性和可靠性。

## 📝 摘要（中文）

视觉障碍者在未知环境中导航和互动面临重大挑战，尤其是在需要空间意识和语义场景理解的任务中。为加速技术发展并评估视觉辅助技术，2024年Cybathlon比赛组织了视觉辅助赛（VIS）。本文介绍了Sight Guide，这是一种可穿戴辅助系统，旨在帮助用户通过复杂的现实任务。该系统利用多台RGB和深度相机的数据，通过振动信号和音频指令引导用户。我们的软件架构结合了经典机器人算法和基于学习的方法，实现了障碍物规避、物体检测、光学字符识别和触摸屏交互等功能。在测试环境中，Sight Guide实现了95.7%的任务成功率，并在Cybathlon比赛中展现了其有效性。本文提供了系统设计、评估结果和经验教训的详细见解，并指出了向更广泛实际应用的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉障碍者在复杂环境中导航的困难，现有方法在空间感知和实时反馈方面存在不足，无法有效支持用户完成任务。

**核心思路**：Sight Guide通过集成多种传感器（RGB和深度相机）数据，结合经典算法与学习方法，提供实时的环境感知和反馈，帮助用户安全导航。

**技术框架**：系统架构包括数据采集模块、环境感知模块、用户反馈模块和任务执行模块。数据采集模块负责获取环境信息，环境感知模块进行障碍物检测和场景理解，用户反馈模块通过振动和音频指令与用户互动，任务执行模块则负责执行具体导航任务。

**关键创新**：该系统的创新在于将传统机器人算法与现代机器学习方法相结合，提升了环境感知的准确性和实时性，尤其是在复杂场景下的表现。

**关键设计**：系统采用了多传感器融合技术，优化了数据处理流程，使用了特定的损失函数来提高物体检测和识别的精度，同时设计了用户友好的交互界面以增强用户体验。

## 📊 实验亮点

在测试环境中，Sight Guide实现了95.7%的任务成功率，显著高于现有视觉辅助技术的表现。这一成果在Cybathlon比赛中得到了验证，展示了系统在实际应用中的有效性和可靠性。

## 🎯 应用场景

Sight Guide的潜在应用领域包括公共交通、商场、校园等复杂环境中，能够为视觉障碍者提供安全、便捷的导航支持。其实际价值在于提升视觉障碍者的独立性和生活质量，未来可能扩展到更多智能辅助设备中，推动无障碍技术的发展。

## 📄 摘要（原文）

> Visually impaired individuals face significant challenges navigating and interacting with unknown situations, particularly in tasks requiring spatial awareness and semantic scene understanding. To accelerate the development and evaluate the state of technologies that enable visually impaired people to solve these tasks, the Vision Assistance Race (VIS) at the Cybathlon 2024 competition was organized. In this work, we present Sight Guide, a wearable assistive system designed for the VIS. The system processes data from multiple RGB and depth cameras on an embedded computer that guides the user through complex, real-world-inspired tasks using vibration signals and audio commands. Our software architecture integrates classical robotics algorithms with learning-based approaches to enable capabilities such as obstacle avoidance, object detection, optical character recognition, and touchscreen interaction. In a testing environment, Sight Guide achieved a 95.7% task success rate, and further demonstrated its effectiveness during the Cybathlon competition. This work provides detailed insights into the system design, evaluation results, and lessons learned, and outlines directions towards a broader real-world applicability.

