---
layout: default
title: Robust Immersive Bilateral Teleoperation of Beyond-Human-Scale Systems with Enhanced Transparency and Sense of Embodiment
---

# Robust Immersive Bilateral Teleoperation of Beyond-Human-Scale Systems with Enhanced Transparency and Sense of Embodiment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14486" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14486v2</a>
  <a href="https://arxiv.org/pdf/2505.14486.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14486v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14486v2', 'Robust Immersive Bilateral Teleoperation of Beyond-Human-Scale Systems with Enhanced Transparency and Sense of Embodiment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mahdi Hejrati, Pauli Mustalahti, Jouni Mattila

**分类**: cs.RO

**发布日期**: 2025-05-20 (更新: 2025-05-25)

---

## 💡 一句话要点

**提出双向遥操作框架以增强超人规模系统的透明度与身体感知**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `遥操作` `虚拟现实` `人机交互` `鲁棒控制` `重型机械` `身体感知` `触觉反馈`

## 📋 核心要点

1. 现有的遥操作系统在重型操作器的控制中面临高任务性能和人机交互的挑战，尤其是在透明度和身体感知方面。
2. 本文提出了一种双向遥操作框架，通过沉浸式虚拟现实和分布式触觉反馈，增强操作员的代理感和自我定位感。
3. 实验证明该系统在高达1:13的运动缩放和1:1000的力缩放下实现了高精度跟踪，且用户体验良好，身体感知水平达到76.4%。

## 📝 摘要（中文）

在涉及重型操作器的人机协作系统中，实现高任务性能需要强大的控制能力和人类的高度参与。本文提出了一种双向遥操作框架，旨在通过沉浸式虚拟现实界面和分布式触觉反馈来增强操作员的透明度和身体感知，特别是代理感和自我定位感。为支持这种身体感知并实现高水平的运动和力的透明度，本文开发了一种无力传感器的鲁棒控制架构，解决了输入非线性、主从不对称、未知不确定性和任意时间延迟等问题。理论分析确认了闭环系统的半全局一致最终有界性，保证了对现实世界不确定性的鲁棒性。大量实验证明，在高达1:13的运动缩放和1:1000的力缩放下，系统能够实现高精度跟踪，结果具有重要意义。

## 🔬 方法详解

**问题定义**：本文旨在解决重型操作器遥操作系统中存在的透明度不足和身体感知缺失的问题。现有方法在面对输入非线性和不确定性时表现不佳，影响了操作员的控制体验。

**核心思路**：通过开发一种无力传感器的鲁棒控制架构，结合沉浸式虚拟现实界面和分布式触觉反馈，增强操作员的代理感和自我定位感，从而提高遥操作的透明度和人机交互的质量。

**技术框架**：整体架构包括控制环路中的人机增强动态模型、鲁棒控制算法和触觉反馈模块。控制环路通过实时数据处理来实现高效的运动和力的跟踪。

**关键创新**：最重要的创新在于无力传感器的鲁棒控制架构，能够有效应对输入非线性和未知不确定性，确保系统在复杂环境下的稳定性和可靠性。

**关键设计**：设计中采用了动态模型来增强控制器的人机适应性，并通过理论分析确保闭环系统的半全局一致最终有界性，保证了系统的鲁棒性。

## 📊 实验亮点

实验结果显示，该系统在高达1:13的运动缩放和1:1000的力缩放下实现了高精度跟踪，且在150毫秒的单向延迟下仍保持稳定性和透明度。用户研究表明，76.4%的参与者感受到良好的身体感知，且系统对性别没有限制，用户友好性高。

## 🎯 应用场景

该研究的潜在应用领域包括远程医疗、危险环境下的操作、以及重型机械的遥控操作等。通过增强操作员的身体感知和控制能力，能够提高这些领域的工作效率和安全性，未来可能推动相关技术的广泛应用。

## 📄 摘要（原文）

> In human-in-the-loop systems such as teleoperation, especially those involving heavy-duty manipulators, achieving high task performance requires both robust control and strong human engagement. This paper presents a bilateral teleoperation framework for beyond-human-scale robotic systems that enhances the transparency and the operator's sense of embodiment (SoE), specifically, the senses of agency and self-location, through an immersive virtual reality interface and distributed haptic feedback. To support this embodiment and establish high level of motion and force transparency, we develop a force-sensorless, robust control architecture that tackles input nonlinearities, master-surrogate asymmetries, unknown uncertainties, and arbitrary time delays. A human-robot augmented dynamic model is integrated into the control loop to enhance human-adaptability of the controller. Theoretical analysis confirms semi-global uniform ultimate boundedness of the closed-loop system, guaranteeing the robustness to the real-world uncertainties. Extensive real-world experiments demonstrate high accuracy tracking under up to 1:13 motion scaling and 1:1000 force scaling, showcasing the significance of the results. Additionally, the stability-transparency tradeoff for motion tracking and force reflection and tracking is established up to 150 ms of one-way fix and time-varying communication delays. The results of user study with 10 participants (9 male and 1 female) demonstrate that the system can imply a good level of SoE (76.4%), at the same time is very user friendly with no gender limitation. These results are significant given the scale and weight of the heavy-duty manipulators.

