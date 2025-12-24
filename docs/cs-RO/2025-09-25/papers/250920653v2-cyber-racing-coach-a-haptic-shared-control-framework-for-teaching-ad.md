---
layout: default
title: "Cyber Racing Coach: A Haptic Shared Control Framework for Teaching Advanced Driving Skills"
---

# Cyber Racing Coach: A Haptic Shared Control Framework for Teaching Advanced Driving Skills

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20653" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20653v2</a>
  <a href="https://arxiv.org/pdf/2509.20653.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20653v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20653v2', 'Cyber Racing Coach: A Haptic Shared Control Framework for Teaching Advanced Driving Skills')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Congkai Shen, Siyuan Yu, Yifan Weng, Haoran Ma, Chen Li, Hiroshi Yasuda, James Dallas, Michael Thompson, John Subosits, Tulga Ersal

**分类**: cs.RO, cs.HC

**发布日期**: 2025-09-25 (更新: 2025-10-04)

**备注**: Added the statement written as red text for the IEEE preprint policy

---

## 💡 一句话要点

**提出触觉共享控制框架，用于提升驾驶员高阶驾驶技能**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `触觉共享控制` `人机协作` `驾驶技能学习` `自动驾驶` `高性能驾驶`

## 📋 核心要点

1. 现有共享控制方案在提升驾驶性能和安全性方面有优势，但缺乏对复杂任务中技能习得的评估。
2. 提出基于触觉共享控制的网络赛车教练框架，通过人机协作和辅助衰减提升驾驶技能。
3. 人体实验表明，该框架能有效帮助驾驶员掌握赛车技能，提升驾驶性能和驾驶一致性。

## 📝 摘要（中文）

本研究提出了一种触觉共享控制框架，旨在教授人类驾驶员高级驾驶技能。在此背景下，共享控制指的是一种驾驶模式，其中人类驾驶员与自动驾驶系统协作，同时控制车辆的转向。高级驾驶技能是指在高性能驾驶（如赛车和紧急避障）中，安全地将车辆推向操控极限所需的技能。之前的研究已经证明了共享控制方案在性能和安全性方面的优势，但这些方案尚未评估其对复杂和高要求任务中技能习得的影响。以往关于长期技能习得的研究要么将触觉共享控制应用于简单任务，要么采用其他反馈方法，如视觉和听觉辅助。为了弥补这一差距，本研究创建了一个基于触觉共享控制范式的网络赛车教练框架，并评估其在帮助人类驾驶员获得高性能驾驶技能方面的性能。该框架引入了：（1）一个能够在高性能驾驶场景中与人类合作的自动驾驶系统；以及（2）一种触觉共享控制机制，以及一种衰减方案，以根据人类驾驶员在训练期间的表现，逐步减少来自自主系统的转向辅助。考虑了两个基准：自学（无辅助）和训练期间的完全辅助。人体实验的结果表明，与基准相比，所提出的框架有助于人类驾驶员发展卓越的赛车技能，从而获得更好的性能和一致性。

## 🔬 方法详解

**问题定义**：论文旨在解决人类驾驶员在学习高性能驾驶技能（如赛车和紧急避障）时，如何有效地利用自动驾驶系统的辅助，并最终实现独立驾驶的问题。现有方法要么是完全自主驾驶，要么是简单的触觉反馈，无法有效地帮助驾驶员掌握复杂驾驶技巧，并且缺乏对驾驶员技能提升的长期评估。

**核心思路**：论文的核心思路是利用触觉共享控制，让人类驾驶员与自动驾驶系统协同工作。通过自动驾驶系统提供辅助，并根据驾驶员的表现逐渐减少辅助，最终使驾驶员能够独立完成高性能驾驶任务。这种方法结合了自动驾驶系统的精确控制和人类驾驶员的决策能力，从而实现更高效的技能学习。

**技术框架**：该框架包含两个主要模块：（1）高性能自动驾驶系统，负责在复杂驾驶场景中提供精确的车辆控制；（2）触觉共享控制机制，通过方向盘力反馈与驾驶员进行交互，并根据驾驶员的表现动态调整辅助力度。训练过程中，系统首先提供较强的辅助，然后逐渐减弱，促使驾驶员主动学习和掌握驾驶技巧。

**关键创新**：该论文的关键创新在于将触觉共享控制与辅助衰减方案相结合，用于提升驾驶员的高性能驾驶技能。与传统的完全自主或完全人工驾驶相比，该方法能够更有效地引导驾驶员学习，并最终实现独立驾驶。此外，该框架针对高性能驾驶场景进行了优化，能够处理复杂的路况和车辆动力学。

**关键设计**：触觉共享控制机制通过力反馈方向盘实现，其辅助力矩的大小由自动驾驶系统的控制输出和驾驶员的输入共同决定。辅助衰减方案根据驾驶员的驾驶表现（例如，与理想轨迹的偏差、速度等）动态调整辅助力度。具体参数设置和损失函数（用于评估驾驶员表现）在论文中未明确说明，属于未知信息。

## 📊 实验亮点

人体实验结果表明，使用该框架训练的驾驶员在赛道上的表现优于自学组和完全辅助组，在圈速和驾驶一致性方面均有显著提升。具体性能数据和提升幅度在摘要中未明确给出，属于未知信息。但结论表明，该框架能有效帮助驾驶员发展卓越的赛车技能。

## 🎯 应用场景

该研究成果可应用于驾驶员培训、赛车游戏、以及高级驾驶辅助系统（ADAS）等领域。通过触觉共享控制，驾驶员可以在安全的环境下学习和掌握高性能驾驶技能，提高驾驶安全性，并提升驾驶乐趣。未来，该技术有望应用于自动驾驶汽车的人机协作控制，实现更安全、更高效的驾驶体验。

## 📄 摘要（原文）

> This study introduces a haptic shared control framework designed to teach human drivers advanced driving skills. In this context, shared control refers to a driving mode where the human driver collaborates with an autonomous driving system to control the steering of a vehicle simultaneously. Advanced driving skills are those necessary to safely push the vehicle to its handling limits in high-performance driving such as racing and emergency obstacle avoidance. Previous research has demonstrated the performance and safety benefits of shared control schemes using both subjective and objective evaluations. However, these schemes have not been assessed for their impact on skill acquisition on complex and demanding tasks. Prior research on long-term skill acquisition either applies haptic shared control to simple tasks or employs other feedback methods like visual and auditory aids. To bridge this gap, this study creates a cyber racing coach framework based on the haptic shared control paradigm and evaluates its performance in helping human drivers acquire high-performance driving skills. The framework introduces (1) an autonomous driving system that is capable of cooperating with humans in a highly performant driving scenario; and (2) a haptic shared control mechanism along with a fading scheme to gradually reduce the steering assistance from autonomy based on the human driver's performance during training. Two benchmarks are considered: self-learning (no assistance) and full assistance during training. Results from a human subject study indicate that the proposed framework helps human drivers develop superior racing skills compared to the benchmarks, resulting in better performance and consistency.

