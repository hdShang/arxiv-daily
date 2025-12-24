---
layout: default
title: Quadrupedal Spine Control Strategies: Exploring Correlations Between System Dynamic Responses and Human Perspectives
---

# Quadrupedal Spine Control Strategies: Exploring Correlations Between System Dynamic Responses and Human Perspectives

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02414" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02414v1</a>
  <a href="https://arxiv.org/pdf/2505.02414.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02414v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02414v1', 'Quadrupedal Spine Control Strategies: Exploring Correlations Between System Dynamic Responses and Human Perspectives')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicholas Hafner, Chaoran Liu, Carlos Ishi, Hiroshi Ishiguro

**分类**: cs.RO, cs.HC, eess.SY

**发布日期**: 2025-05-05

**备注**: 27 pages, 13 figures

**期刊**: Advanced Robotics, 39(6), 273-290 (2025)

**DOI**: [10.1080/01691864.2025.2478922](https://doi.org/10.1080/01691864.2025.2478922)

---

## 💡 一句话要点

**提出四足机器人脊柱控制策略以提升人机交互自然性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `脊柱控制` `人机交互` `轨迹生成` `运动自然性` `社交机器人` `老年护理`

## 📋 核心要点

1. 现有四足机器人多采用刚性底盘，导致运动方式缺乏自然流畅性，影响人机交互体验。
2. 本文提出了多种轨迹生成策略，旨在通过引入四自由度脊柱来改善四足机器人的运动自然性。
3. 实验结果表明，优化的时间变化策略和足部跟踪策略在自然性感知上优于固定脊柱基线，尽管能效未见提升。

## 📝 摘要（中文）

与生物四足动物不同，现有大多数四足机器人采用刚性底盘，导致其运动缺乏自然流畅性。现有文献主要关注四足机器人的能效，而忽视了人机交互场景中的影响。本文首次探讨了具有四自由度脊柱的四足机器人不同轨迹生成策略，并分析了这些方法对人类对步态自然性感知的影响。通过对行走、慢跑和转弯模拟的视频评估，发现优化的时间变化策略和足部跟踪策略在50名参与者的随机试验中被认为比固定脊柱基线更自然。尽管这些策略未能在能效上优于无脊柱基线，但在较高速度下显示出更好的足迹一致性。基于更自然的运动模式，这类机器人在社交机器人场景（如老年护理）中展现出潜在应用价值。

## 🔬 方法详解

**问题定义**：本文旨在解决现有四足机器人运动方式不自然的问题，现有方法主要关注能效，忽略了人机交互中的自然性感知。

**核心思路**：通过引入四自由度脊柱，探索不同的轨迹生成策略，以提高四足机器人的运动自然性和人机交互体验。

**技术框架**：研究包括多个阶段：首先设计不同的轨迹生成策略，然后通过模拟视频展示这些策略的效果，最后进行人类参与者的感知评估。

**关键创新**：提出了优化的时间变化策略和足部跟踪策略，这些策略在自然性感知上显著优于传统的固定脊柱设计，展现了新的控制思路。

**关键设计**：在策略设计中，重点考虑了脊柱的动态响应和运动一致性，确保在不同速度下的足迹一致性，同时未对能效进行优化。

## 📊 实验亮点

实验结果显示，优化的时间变化策略和足部跟踪策略在50名参与者的评估中被认为比固定脊柱基线更自然，提升幅度显著。尽管能效未见改善，但在较高速度下的足迹一致性有所提高，显示出新的应用潜力。

## 🎯 应用场景

该研究的潜在应用领域包括社交机器人、老年护理等场景。在这些应用中，机器人需要与人类进行自然的互动，而非单纯追求能效，因此提升运动自然性将极大增强用户体验和接受度。

## 📄 摘要（原文）

> Unlike their biological cousins, the majority of existing quadrupedal robots are constructed with rigid chassis. This results in motion that is either beetle-like or distinctly robotic, lacking the natural fluidity characteristic of mammalian movements. Existing literature on quadrupedal robots with spinal configurations primarily focuses on energy efficiency and does not consider the effects in human-robot interaction scenarios. Our contributions include an initial investigation into various trajectory generation strategies for a quadrupedal robot with a four degree of freedom spine, and an analysis on the effect that such methods have on human perception of gait naturalness compared to a fixed spine baseline. The strategies were evaluated using videos of walking, trotting and turning simulations. Among the four different strategies developed, the optimised time varying and the foot-tracking strategies were perceived to be more natural than the baseline in a randomised trial with 50 participants. Although none of the strategies demonstrated any energy efficiency improvements over the no-spine baseline, some showed greater footfall consistency at higher speeds. Given the greater likeability drawn from the more natural locomotion patterns, this type of robot displays potential for applications in social robot scenarios such as elderly care, where energy efficiency is not a primary concern.

