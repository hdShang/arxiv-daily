---
layout: default
title: Planning Oriented Integrated Sensing and Communication
---

# Planning Oriented Integrated Sensing and Communication

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.23021" class="toolbar-btn" target="_blank">📄 arXiv: 2510.23021v1</a>
  <a href="https://arxiv.org/pdf/2510.23021.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23021v1" onclick="toggleFavorite(this, '2510.23021v1', 'Planning Oriented Integrated Sensing and Communication')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xibin Jin, Guoliang Li, Shuai Wang, Fan Liu, Miaowen Wen, Huseyin Arslan, Derrick Wing Kwan Ng, Chengzhong Xu

**分类**: eess.SP, cs.RO, eess.SY

**发布日期**: 2025-10-27

---

## 💡 一句话要点

**提出面向规划的集成感知与通信框架，提升自动驾驶安全性和效率**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `集成感知与通信` `自动驾驶` `运动规划` `功率分配` `安全约束`

## 📋 核心要点

1. 现有集成感知与通信(ISAC)设计忽略了关键障碍物对运动效率的影响，且对所有目标同等对待。
2. PISAC框架通过降低规划瓶颈障碍物的感知不确定性，扩展安全可导航路径，从而优化运动规划。
3. 实验结果表明，PISAC相比现有方法，成功率提升高达40%，行驶时间缩短超过5%。

## 📝 摘要（中文）

本文提出了一种面向规划的集成感知与通信（PISAC）框架，旨在为互联自动驾驶车辆提供同步定位、环境感知和数据交换。与现有ISAC设计不同，PISAC优先考虑规划瓶颈障碍物的感知不确定性，并扩展车辆的安全可导航路径，从而弥合了物理层优化和运动层规划之间的差距。PISAC的核心在于推导出一个闭式安全边界，该边界基于Cramér-Rao下界和占用膨胀原则，将ISAC发射功率与感知不确定性显式关联。基于此，构建了一个双层功率分配和运动规划（PAMP）问题，内层优化ISAC波束功率分布，外层计算不确定性感知安全约束下的无碰撞轨迹。在高保真城市驾驶环境中的综合仿真表明，PISAC比现有的基于ISAC和面向通信的基准方法，成功率提高了40%，行驶时间缩短了5%以上，验证了其在提高安全性和效率方面的有效性。

## 🔬 方法详解

**问题定义**：现有ISAC设计主要关注感知精度和通信吞吐量，忽略了环境中的关键障碍物对自动驾驶车辆运动规划的影响。这种一视同仁的处理方式可能导致车辆在规划路径时，对关键障碍物的不确定性估计不足，从而影响行驶安全性和效率。因此，需要一种能够根据规划需求，优化感知资源分配的ISAC框架。

**核心思路**：PISAC的核心在于将物理层的ISAC资源分配与运动层的路径规划相结合，通过优化ISAC的发射功率分布，降低对规划至关重要的障碍物的感知不确定性，从而扩展车辆的安全可导航路径。这种方法的核心思想是，并非所有障碍物都同等重要，应该优先感知那些对规划影响最大的障碍物。

**技术框架**：PISAC框架包含两个主要模块：ISAC波束功率分配和运动规划。首先，基于Cramér-Rao下界和占用膨胀原则，推导出一个闭式安全边界，将ISAC发射功率与感知不确定性显式关联。然后，构建一个双层优化问题（PAMP）。内层优化ISAC波束功率分布，以外层运动规划提供更精确的感知信息；外层在不确定性感知安全约束下，计算无碰撞轨迹。

**关键创新**：PISAC的关键创新在于：1）提出了面向规划的ISAC框架，将物理层资源分配与运动层规划相结合；2）推导了闭式安全边界，显式地将ISAC发射功率与感知不确定性关联；3）构建了双层优化问题，实现了ISAC资源分配和运动规划的联合优化。与现有方法相比，PISAC能够更有效地利用ISAC资源，提高自动驾驶的安全性和效率。

**关键设计**：PISAC的关键设计包括：1）基于Cramér-Rao下界的感知不确定性建模；2）基于占用膨胀原则的安全边界推导；3）双层优化问题的构建，其中内层优化ISAC波束功率分布，目标是最小化规划瓶颈障碍物的感知不确定性，外层优化运动轨迹，目标是在安全约束下最小化行驶时间或路径长度。双层优化问题可以使用交替优化算法求解。

## 📊 实验亮点

在高保真城市驾驶环境中的仿真结果表明，PISAC框架相比于现有的ISAC和面向通信的基准方法，成功率提高了高达40%，行驶时间缩短了超过5%。这些结果验证了PISAC在提高自动驾驶安全性和效率方面的有效性，表明其能够显著改善自动驾驶车辆的性能。

## 🎯 应用场景

PISAC框架可应用于各种需要集成感知与通信的自动驾驶场景，例如城市道路、高速公路和停车场等。通过优化感知资源分配，提高对关键障碍物的感知精度，PISAC能够显著提升自动驾驶车辆的安全性和效率，降低事故风险，并缩短行驶时间。此外，该框架还可以扩展到其他机器人应用，例如无人机和仓储机器人等。

## 📄 摘要（原文）

> Integrated sensing and communication (ISAC) enables simultaneous localization, environment perception, and data exchange for connected autonomous vehicles. However, most existing ISAC designs prioritize sensing accuracy and communication throughput, treating all targets uniformly and overlooking the impact of critical obstacles on motion efficiency. To overcome this limitation, we propose a planning-oriented ISAC (PISAC) framework that reduces the sensing uncertainty of planning-bottleneck obstacles and expands the safe navigable path for the ego-vehicle, thereby bridging the gap between physical-layer optimization and motion-level planning. The core of PISAC lies in deriving a closed-form safety bound that explicitly links ISAC transmit power to sensing uncertainty, based on the Cramér-Rao Bound and occupancy inflation principles. Using this model, we formulate a bilevel power allocation and motion planning (PAMP) problem, where the inner layer optimizes the ISAC beam power distribution and the outer layer computes a collision-free trajectory under uncertainty-aware safety constraints. Comprehensive simulations in high-fidelity urban driving environments demonstrate that PISAC achieves up to 40% higher success rates and over 5% shorter traversal times than existing ISAC-based and communication-oriented benchmarks, validating its effectiveness in enhancing both safety and efficiency.

