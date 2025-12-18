---
layout: default
title: Fast Functionally Redundant Inverse Kinematics for Robotic Toolpath Optimisation in Manufacturing Tasks
---

# Fast Functionally Redundant Inverse Kinematics for Robotic Toolpath Optimisation in Manufacturing Tasks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.10116" class="toolbar-btn" target="_blank">📄 arXiv: 2512.10116v1</a>
  <a href="https://arxiv.org/pdf/2512.10116.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.10116v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.10116v1', 'Fast Functionally Redundant Inverse Kinematics for Robotic Toolpath Optimisation in Manufacturing Tasks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Razjigaev, Hans Lohr, Alejandro Vargas-Uscategui, Peter King, Tirthankar Bandyopadhyay

**分类**: cs.RO

**发布日期**: 2025-12-10

**备注**: Published at the Australasian Conference on Robotics and Automation (ACRA 2025) https://ssl.linklings.net/conferences/acra/acra2025_proceedings/views/includes/files/pap149s2.pdf

---

## 💡 一句话要点

**提出快速功能冗余逆运动学算法，优化机器人制造任务中的工具路径**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `功能冗余` `逆运动学` `机器人` `工具路径优化` `阻尼最小二乘法`

## 📋 核心要点

1. 工业机器人六轴机械臂在制造中至关重要，但对称工具轴导致其在焊接等任务中存在功能冗余，现有方法难以有效利用。
2. 论文提出一种基于任务空间分解、阻尼最小二乘法和Halley法的功能冗余逆运动学算法，旨在快速稳健地求解并减少关节运动。
3. 实验表明，该算法能快速求解运动规划，最小化关节运动，扩大复杂工具路径的可行空间，并在ABB机械臂和冷喷涂设备上验证。

## 📝 摘要（中文）

本文提出了一种新颖的算法，用于解决机器人操作中的功能冗余逆运动学问题。该算法利用任务空间分解方法、阻尼最小二乘法和Halley法，以实现快速、稳健的解决方案并减少关节运动。我们在非平面表面冷喷涂应用中的工具路径优化案例中评估了该方法。功能冗余逆运动学算法能够快速求解运动规划，从而最大限度地减少关节运动，扩大复杂工具路径的可行操作空间。我们在工业ABB机械臂和冷喷枪上验证了该方法，执行了计算出的工具路径。

## 🔬 方法详解

**问题定义**：论文旨在解决工业机器人，特别是具有功能冗余的六轴机械臂在执行制造任务（如冷喷涂）时，如何快速、高效地求解逆运动学，从而优化工具路径的问题。现有方法，如离线规划，计算成本高昂，难以满足实时性要求。而传统的逆运动学算法在处理功能冗余时，往往无法充分利用冗余自由度来优化关节运动，导致可行工作空间受限。

**核心思路**：论文的核心思路是利用功能冗余的特性，将任务空间进行分解，并结合阻尼最小二乘法和Halley法，设计一种快速、稳健的逆运动学算法。通过任务空间分解，可以将六自由度的运动规划问题简化为更易于处理的子问题。阻尼最小二乘法用于求解逆运动学方程，而Halley法用于加速收敛并提高精度。

**技术框架**：该算法的技术框架主要包括以下几个阶段：1) 任务空间分解：将所需的工具位姿分解为位置和姿态分量。2) 逆运动学求解：使用阻尼最小二乘法和Halley法迭代求解关节角度。阻尼最小二乘法用于处理奇异性附近的运动，Halley法用于加速收敛。3) 冗余优化：利用功能冗余自由度，优化关节运动，例如最小化关节运动幅度或避免关节极限。4) 运动规划：根据求解的关节角度，生成机器人运动轨迹。

**关键创新**：论文的关键创新在于结合了任务空间分解、阻尼最小二乘法和Halley法，提出了一种快速、稳健的功能冗余逆运动学算法。与传统的逆运动学算法相比，该算法能够更好地利用功能冗余自由度，优化关节运动，扩大可行工作空间。此外，Halley法的使用显著提高了算法的收敛速度和精度。

**关键设计**：算法的关键设计包括：1) 任务空间分解方式：选择合适的任务空间分解方式，以简化逆运动学求解过程。2) 阻尼系数的选择：阻尼最小二乘法中的阻尼系数需要根据具体任务进行调整，以平衡求解精度和鲁棒性。3) Halley法的迭代步长：Halley法的迭代步长需要进行优化，以保证算法的收敛性和稳定性。4) 冗余优化目标：选择合适的冗余优化目标，例如最小化关节运动幅度或避免关节极限。

## 📊 实验亮点

该论文在冷喷涂应用中验证了所提出的算法。实验结果表明，该算法能够快速求解运动规划，最小化关节运动，扩大复杂工具路径的可行空间。具体性能数据（如计算时间、关节运动幅度减少量等）未在摘要中明确给出，但强调了算法在实际工业场景中的有效性。

## 🎯 应用场景

该研究成果可广泛应用于需要机器人进行精确工具路径控制的制造任务中，例如焊接、喷涂、增材制造等。通过优化关节运动，可以提高生产效率、降低能源消耗、延长机器人寿命。此外，该算法还可应用于医疗机器人、服务机器人等领域，提升机器人的灵活性和适应性。

## 📄 摘要（原文）

> Industrial automation with six-axis robotic arms is critical for many manufacturing tasks, including welding and additive manufacturing applications; however, many of these operations are functionally redundant due to the symmetrical tool axis, which effectively makes the operation a five-axis task. Exploiting this redundancy is crucial for achieving the desired workspace and dexterity required for the feasibility and optimisation of toolpath planning. Inverse kinematics algorithms can solve this in a fast, reactive framework, but these techniques are underutilised over the more computationally expensive offline planning methods. We propose a novel algorithm to solve functionally redundant inverse kinematics for robotic manipulation utilising a task space decomposition approach, the damped least-squares method and Halley's method to achieve fast and robust solutions with reduced joint motion. We evaluate our methodology in the case of toolpath optimisation in a cold spray coating application on a non-planar surface. The functionally redundant inverse kinematics algorithm can quickly solve motion plans that minimise joint motion, expanding the feasible operating space of the complex toolpath. We validate our approach on an industrial ABB manipulator and cold-spray gun executing the computed toolpath.

