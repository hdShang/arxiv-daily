---
layout: default
title: "Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control"
---

# Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24198" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24198v2</a>
  <a href="https://arxiv.org/pdf/2505.24198.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24198v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24198v2', 'Hold My Beer: Learning Gentle Humanoid Locomotion and End-Effector Stabilization Control')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yitang Li, Yuanhang Zhang, Wenli Xiao, Chaoyi Pan, Haoyang Weng, Guanqi He, Tairan He, Guanya Shi

**分类**: cs.RO

**发布日期**: 2025-05-30 (更新: 2025-06-03)

---

## 💡 一句话要点

**提出SoFTA框架以解决人形机器人行走时的端执行器稳定性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `人形机器人` `端执行器控制` `步态稳定性` `慢-快双代理` `精细控制`

## 📋 核心要点

1. 核心问题：现有的人形机器人在行走时难以同时实现稳定的端执行器控制与有效的步态控制，导致在携带液体时容易洒落。
2. 方法要点：论文提出了SoFTA框架，通过将上半身和下半身控制解耦，分别以100 Hz和50 Hz的频率进行操作，从而实现精确的端执行器控制和稳健的步态控制。
3. 实验或效果：SoFTA框架在实验中减少了端执行器加速度2-5倍，显著提高了稳定性，使机器人能够完成复杂的任务，如携带满杯啤酒。

## 📝 摘要（中文）

本研究探讨了人形机器人在行走过程中如何在不洒落饮料的情况下，稳定地携带满杯啤酒。尽管人形机器人在舞蹈、包裹投递等展示中表现出色，但在行走时的精细控制仍然是一个重大挑战。为了解决这一问题，本文提出了SoFTA框架，该框架将上半身和下半身控制解耦，分别以不同的频率和奖励进行操作，从而实现协调的全身行为。实验结果表明，SoFTA显著提高了端执行器的稳定性，减少了2-5倍的加速度，使得机器人能够完成如携带满杯、稳定拍摄视频等精细任务。

## 🔬 方法详解

**问题定义**：本文旨在解决人形机器人在行走过程中端执行器的稳定性问题。现有方法在行走时难以平衡步态控制与端执行器的精确控制，导致在携带液体时容易洒落。

**核心思路**：论文提出的SoFTA框架通过将上半身和下半身的控制解耦，分别以不同的频率进行操作，旨在减少政策干扰并实现协调的全身行为。上半身以100 Hz的频率进行精确的端执行器控制，而下半身以50 Hz的频率进行稳健的步态控制。

**技术框架**：SoFTA框架包含两个主要模块：上半身控制模块和下半身控制模块。上半身模块负责端执行器的精确控制，下半身模块则负责行走的稳健性。通过这种解耦设计，两个模块可以独立优化各自的控制策略。

**关键创新**：SoFTA框架的最大创新在于其慢-快双代理的设计，能够有效地将不同控制需求的任务分开处理，从而显著提高了机器人在行走时的端执行器稳定性。与现有方法相比，该框架在任务动态上实现了更好的匹配。

**关键设计**：在设计中，论文设置了不同的奖励机制以鼓励上半身和下半身的协调动作，同时采用了适应性损失函数来优化控制策略。具体的网络结构和参数设置在实验部分进行了详细描述，以确保不同频率下的控制效果。

## 📊 实验亮点

实验结果显示，SoFTA框架在端执行器控制方面的加速度减少了2-5倍，相较于基线方法，机器人在行走时的稳定性显著提高，能够成功完成携带满杯啤酒、稳定拍摄视频等复杂任务。

## 🎯 应用场景

该研究的潜在应用场景包括服务机器人、家庭助理和工业自动化等领域。通过提高人形机器人的稳定性和精细控制能力，能够在实际应用中实现更复杂的任务，如饮料递送、精细物品搬运等，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Can your humanoid walk up and hand you a full cup of beer, without spilling a drop? While humanoids are increasingly featured in flashy demos like dancing, delivering packages, traversing rough terrain, fine-grained control during locomotion remains a significant challenge. In particular, stabilizing a filled end-effector (EE) while walking is far from solved, due to a fundamental mismatch in task dynamics: locomotion demands slow-timescale, robust control, whereas EE stabilization requires rapid, high-precision corrections. To address this, we propose SoFTA, a Slow-Fast Two-Agent framework that decouples upper-body and lower-body control into separate agents operating at different frequencies and with distinct rewards. This temporal and objective separation mitigates policy interference and enables coordinated whole-body behavior. SoFTA executes upper-body actions at 100 Hz for precise EE control and lower-body actions at 50 Hz for robust gait. It reduces EE acceleration by 2-5x relative to baselines and performs much closer to human-level stability, enabling delicate tasks such as carrying nearly full cups, capturing steady video during locomotion, and disturbance rejection with EE stability.

