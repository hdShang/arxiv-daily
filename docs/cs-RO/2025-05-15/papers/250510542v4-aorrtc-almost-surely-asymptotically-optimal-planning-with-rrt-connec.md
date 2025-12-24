---
layout: default
title: AORRTC: Almost-Surely Asymptotically Optimal Planning with RRT-Connect
---

# AORRTC: Almost-Surely Asymptotically Optimal Planning with RRT-Connect

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.10542" class="toolbar-btn" target="_blank">📄 arXiv: 2505.10542v4</a>
  <a href="https://arxiv.org/pdf/2505.10542.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.10542v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.10542v4', 'AORRTC: Almost-Surely Asymptotically Optimal Planning with RRT-Connect')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tyler Wilson, Wil Thomason, Zachary Kingston, Jonathan Gammell

**分类**: cs.RO

**发布日期**: 2025-05-15 (更新: 2025-09-24)

**备注**: IEEE Robotics and Automation Letters (RA-L). 8 pages, 4 figures, 1 table. A video of AORRTC can be found at https://www.youtube.com/watch?v=j1itxP3KuiM . Information on the implementation of AORRTC is available at https://robotic-esp.com/code/aorrtc/

---

## 💡 一句话要点

**提出AORRTC以解决高自由度机器人运动规划问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `运动规划` `高自由度机器人` `渐近最优` `RRT-Connect` `AO-x算法` `机器人技术` `路径优化`

## 📋 核心要点

1. 现有的满意度规划器在找到可行解方面表现良好，但缺乏对解的最优性保证，导致在复杂场景中效果不佳。
2. 本文提出的AORRTC通过AO-x元算法扩展了RRT-Connect规划器，能够在保证概率完整性的同时实现渐近最优规划。
3. 实验结果显示，AORRTC在Panda和Fetch机器人上能够快速找到初始解，并且收敛到更优解的速度超过了现有的最优规划算法。

## 📝 摘要（中文）

快速找到高质量解决方案是运动规划中的重要目标，尤其对于高自由度机器人而言。传统的满意度规划器能够快速找到可行解，但对最优性没有保证；而几乎肯定渐近最优的规划器则在收敛到最优解方面提供了概率保证，但计算开销较大。本文使用AO-x元算法扩展了满意度RRT-Connect规划器，提出了渐近最优RRT-Connect（AORRTC），能够在与RRT-Connect相似的时间内找到初始解，并利用额外的规划时间以随时收敛到最优解。实验表明，AORRTC在高自由度规划问题上表现优异，能够在毫秒级别找到解决方案，而其他几乎肯定渐近最优的规划器则无法在秒级内稳定找到解。

## 🔬 方法详解

**问题定义**：本文旨在解决高自由度机器人运动规划中的最优解问题。现有的满意度规划器虽然能快速找到可行解，但缺乏对解的最优性保证，导致在复杂环境中表现不佳。

**核心思路**：AORRTC通过引入AO-x元算法，将满意度RRT-Connect规划器扩展为渐近最优规划器，能够在与传统方法相似的时间内找到初始解，并利用额外时间逐步收敛到最优解。

**技术框架**：AORRTC的整体架构包括初始解的快速生成模块和基于时间的优化收敛模块。初始解生成与RRT-Connect相同，而后续优化则通过不断调整路径来提高解的质量。

**关键创新**：AORRTC的主要创新在于结合了满意度规划与渐近最优规划的优点，既能快速找到可行解，又能在后续时间内逐步优化，确保解的质量。与现有方法相比，AORRTC在计算效率和解的质量上均有显著提升。

**关键设计**：在设计上，AORRTC采用了灵活的时间管理策略，允许在规划过程中动态调整优化的时间分配。此外，算法在实现上支持SIMD加速，进一步提升了计算效率。

## 📊 实验亮点

实验结果表明，AORRTC在Panda（7自由度）和Fetch（8自由度）机器人上能够在毫秒级别找到初始解，且收敛到更优解的速度超过了现有的几乎肯定渐近最优算法，展现出优越的性能和稳定性。

## 🎯 应用场景

AORRTC的研究成果在高自由度机器人运动规划中具有广泛的应用潜力，特别是在工业自动化、服务机器人和无人驾驶等领域。其高效的规划能力能够显著提高机器人在复杂环境中的操作效率，推动智能机器人技术的发展。

## 📄 摘要（原文）

> Finding high-quality solutions quickly is an important objective in motion planning. This is especially true for high-degree-of-freedom robots. Satisficing planners have traditionally found feasible solutions quickly but provide no guarantees on their optimality, while almost-surely asymptotically optimal (a.s.a.o.) planners have probabilistic guarantees on their convergence towards an optimal solution but are more computationally expensive.
>   This paper uses the AO-x meta-algorithm to extend the satisficing RRT-Connect planner to optimal planning. The resulting Asymptotically Optimal RRT-Connect (AORRTC) finds initial solutions in similar times as RRT-Connect and uses any additional planning time to converge towards the optimal solution in an anytime manner. It is proven to be probabilistically complete and a.s.a.o.
>   AORRTC was tested with the Panda (7 DoF) and Fetch (8 DoF) robotic arms on the MotionBenchMaker dataset. These experiments show that AORRTC finds initial solutions as fast as RRT-Connect and faster than the tested state-of-the-art a.s.a.o. algorithms while converging to better solutions faster. AORRTC finds solutions to difficult high-DoF planning problems in milliseconds where the other a.s.a.o. planners could not consistently find solutions in seconds. This performance was demonstrated both with and without single instruction/multiple data (SIMD) acceleration.

