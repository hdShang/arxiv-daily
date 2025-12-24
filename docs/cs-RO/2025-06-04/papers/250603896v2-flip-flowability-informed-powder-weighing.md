---
layout: default
title: "FLIP: Flowability-Informed Powder Weighing"
---

# FLIP: Flowability-Informed Powder Weighing

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.03896" class="toolbar-btn" target="_blank">📄 arXiv: 2506.03896v2</a>
  <a href="https://arxiv.org/pdf/2506.03896.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.03896v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.03896v2', 'FLIP: Flowability-Informed Powder Weighing')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikola Radulov, Alex Wright, Thomas Little, Andrew I. Cooper, Gabriella Pizzuto

**分类**: cs.RO

**发布日期**: 2025-06-04 (更新: 2025-06-05)

**备注**: Paper video can be found at https://youtu.be/pVwqjzgT0Co

---

## 💡 一句话要点

**提出FLIP框架以解决粉末称量中的自适应自动化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `粉末操控` `机器人自动化` `流动性量化` `课程学习` `贝叶斯推断` `物理模拟` `实验室自动化`

## 📋 核心要点

1. 现有的粉末操控方法在应对粉末流动性和实验室条件变化时表现不佳，导致自动化效率低下。
2. FLIP框架通过量化粉末的流动性，优化物理模拟，并结合课程学习策略，提升机器人策略的学习效率。
3. 实验结果表明，FLIP在真实实验室环境下的粉末称量任务中显著降低了分配误差，表现出更好的泛化能力。

## 📝 摘要（中文）

粉末的自主操控在科学实验室的机器人自动化中仍然是一个重大挑战。粉末在流动过程中的固有变异性和复杂物理交互，加上实验室条件的变化，要求自适应的自动化。本文提出FLIP，一个基于流动性的信息化粉末称量框架，旨在增强颗粒材料处理的机器人策略学习。我们的主要贡献在于利用通过静止角量化的材料流动性，通过贝叶斯推断优化基于物理的模拟。这产生了能够生成准确训练数据的材料特定模拟环境，反映多样的粉末行为，从而训练“机器人化学家”。FLIP还将量化的流动性整合到课程学习策略中，逐步引入更具挑战性的、流动性较差的粉末，以促进稳健机器人策略的高效获取。我们在真实实验室条件下验证了该方法在粉末称量任务上的有效性，实验结果显示，采用课程策略的FLIP实现了2.12 +/- 1.53 mg的低分配误差，优于未利用流动性数据的方法（如领域随机化的6.11 +/- 3.92 mg）。

## 🔬 方法详解

**问题定义**：本文旨在解决粉末在流动性和实验室条件变化下的自主操控问题。现有方法未能有效应对粉末的复杂物理交互和流动性变异，导致自动化效率低下。

**核心思路**：FLIP框架的核心思想是利用量化的流动性（通过静止角）来优化物理模拟，并通过课程学习逐步引入更具挑战性的粉末，以提高机器人策略的学习效果。

**技术框架**：FLIP的整体架构包括两个主要模块：首先，通过贝叶斯推断优化的物理模拟环境生成准确的训练数据；其次，结合课程学习策略，逐步引入不同流动性的粉末进行训练。

**关键创新**：FLIP的最大创新在于将流动性量化与课程学习相结合，形成了一种新的训练策略，使得机器人能够更好地适应不同类型的粉末，尤其是那些流动性较差的粉末。

**关键设计**：在设计中，采用了静止角作为流动性量化的关键参数，通过贝叶斯推断优化模拟环境。此外，课程学习策略的实施使得训练过程更加高效，逐步增加难度以提升机器人策略的稳健性。

## 📊 实验亮点

实验结果显示，FLIP框架结合课程学习策略在粉末称量任务中实现了2.12 +/- 1.53 mg的低分配误差，相较于未利用流动性数据的领域随机化方法（6.11 +/- 3.92 mg）有显著提升，展示了其在处理新型粉末和目标质量方面的优越性。

## 🎯 应用场景

该研究的潜在应用领域包括科学实验室的自动化粉末处理、制药行业的药物配制以及材料科学中的粉末加工等。FLIP框架的实际价值在于提高粉末操控的精确性和效率，未来可能推动更多领域的自动化进程。

## 📄 摘要（原文）

> Autonomous manipulation of powders remains a significant challenge for robotic automation in scientific laboratories. The inherent variability and complex physical interactions of powders in flow, coupled with variability in laboratory conditions necessitates adaptive automation. This work introduces FLIP, a flowability-informed powder weighing framework designed to enhance robotic policy learning for granular material handling. Our key contribution lies in using material flowability, quantified by the angle of repose, to optimise physics-based simulations through Bayesian inference. This yields material-specific simulation environments capable of generating accurate training data, which reflects diverse powder behaviours, for training "robot chemists". Building on this, FLIP integrates quantified flowability into a curriculum learning strategy, fostering efficient acquisition of robust robotic policies by gradually introducing more challenging, less flowable powders. We validate the efficacy of our method on a robotic powder weighing task under real-world laboratory conditions. Experimental results show that FLIP with a curriculum strategy achieves a low dispensing error of 2.12 +/- 1.53 mg, outperforming methods that do not leverage flowability data, such as domain randomisation (6.11 +/- 3.92 mg). These results demonstrate FLIP's improved ability to generalise to previously unseen, more cohesive powders and to new target masses.

