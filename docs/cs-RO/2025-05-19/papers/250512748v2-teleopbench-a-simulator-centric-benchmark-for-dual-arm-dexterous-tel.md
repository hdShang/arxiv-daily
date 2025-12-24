---
layout: default
title: TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation
---

# TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12748" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12748v2</a>
  <a href="https://arxiv.org/pdf/2505.12748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12748v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12748v2', 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hangyu Li, Qin Zhao, Haoran Xu, Xinyu Jiang, Qingwei Ben, Feiyu Jia, Haoyu Zhao, Liang Xu, Jia Zeng, Hanqing Wang, Bo Dai, Junting Dong, Jiangmiao Pang

**分类**: cs.RO, cs.AI, cs.CV

**发布日期**: 2025-05-19 (更新: 2025-09-15)

**备注**: Project page:https://gorgeous2002.github.io/TeleOpBench/, Codes:https://github.com/cyjdlhy/TeleOpBench

**🔗 代码/项目**: [GITHUB](https://github.com/cyjdlhy/TeleOpBench)

---

## 💡 一句话要点

**提出TeleOpBench以解决双臂灵巧遥操作基准缺失问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `遥操作` `双臂机器人` `基准测试` `模拟器` `人机交互` `虚拟现实` `灵巧操作`

## 📋 核心要点

1. 现有的遥操作系统缺乏统一的基准，导致不同系统之间的比较缺乏公平性和可重复性。
2. 本文提出TeleOpBench，作为一个模拟器中心的基准，包含多种任务环境和遥操作模式，以便于系统性能的评估和比较。
3. 通过在物理双臂平台上进行的实验，验证了模拟器性能与实际硬件性能之间的强相关性，提升了研究的可信度。

## 📝 摘要（中文）

遥操作是具身机器人学习的重要基础，尤其是双手灵巧遥操作提供了丰富的示范，这些示范是完全自主系统难以获取的。尽管近期研究提出了多种硬件管道，但仍缺乏统一的基准来公平、可重复地比较这些系统。本文提出了TeleOpBench，这是一个针对双手灵巧遥操作的模拟器中心基准，包含30个高保真任务环境，涵盖了抓取放置、工具使用和协作操作等多种任务，展示了广泛的运动学和力交互难度。我们实现了四种代表性的遥操作模式，并在共同的协议和指标套件下进行了评估。通过在物理双臂平台上进行的实验，我们观察到模拟器与硬件性能之间存在强相关性，验证了TeleOpBench的外部有效性。该基准为遥操作研究建立了共同的标准，并为未来的算法和硬件创新提供了可扩展的平台。

## 🔬 方法详解

**问题定义**：当前遥操作领域缺乏统一的基准，导致不同系统的性能比较困难，且现有方法在评估时缺乏一致性和可重复性。

**核心思路**：本文提出TeleOpBench，旨在为双手灵巧遥操作提供一个标准化的评估平台，通过模拟器环境来实现多种遥操作模式的比较与验证。

**技术框架**：TeleOpBench包含30个高保真任务环境，涵盖抓取放置、工具使用和协作操作等任务，支持四种遥操作模式：运动捕捉、虚拟现实设备、手臂-手外骨骼和单目视觉跟踪。评估采用统一的协议和指标套件。

**关键创新**：TeleOpBench的主要创新在于其模拟器中心的设计，使得不同遥操作系统可以在相同的环境下进行公平比较，且通过与物理双臂平台的实验验证了模拟结果的有效性。

**关键设计**：在设计中，采用了高保真的任务环境和多样的遥操作模式，确保了基准的广泛适用性和灵活性，此外，实验中使用的性能指标和评估协议也经过精心设计，以便于不同系统的比较。

## 📊 实验亮点

在10个保留任务的实验中，模拟器与硬件性能之间表现出强相关性，验证了TeleOpBench的外部有效性。这一发现为遥操作系统的开发提供了重要的参考依据，提升了研究的可信度。

## 🎯 应用场景

TeleOpBench的研究成果可广泛应用于机器人遥操作、虚拟现实和人机交互等领域。通过提供一个标准化的评估平台，研究人员和工程师可以更有效地开发和优化遥操作系统，推动相关技术的进步和应用落地。

## 📄 摘要（原文）

> Teleoperation is a cornerstone of embodied-robot learning, and bimanual dexterous teleoperation in particular provides rich demonstrations that are difficult to obtain with fully autonomous systems. While recent studies have proposed diverse hardware pipelines-ranging from inertial motion-capture gloves to exoskeletons and vision-based interfaces-there is still no unified benchmark that enables fair, reproducible comparison of these systems. In this paper, we introduce TeleOpBench, a simulator-centric benchmark tailored to bimanual dexterous teleoperation. TeleOpBench contains 30 high-fidelity task environments that span pick-and-place, tool use, and collaborative manipulation, covering a broad spectrum of kinematic and force-interaction difficulty. Within this benchmark we implement four representative teleoperation modalities-(i) MoCap, (ii) VR device, (iii) arm-hand exoskeletons, and (iv) monocular vision tracking-and evaluate them with a common protocol and metric suite. To validate that performance in simulation is predictive of real-world behavior, we conduct mirrored experiments on a physical dual-arm platform equipped with two 6-DoF dexterous hands. Across 10 held-out tasks we observe a strong correlation between simulator and hardware performance, confirming the external validity of TeleOpBench. TeleOpBench establishes a common yardstick for teleoperation research and provides an extensible platform for future algorithmic and hardware innovation. Codes is now available at https://github.com/cyjdlhy/TeleOpBench .

