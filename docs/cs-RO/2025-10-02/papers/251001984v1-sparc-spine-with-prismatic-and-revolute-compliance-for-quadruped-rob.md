---
layout: default
title: SPARC: Spine with Prismatic and Revolute Compliance for Quadruped Robot
---

# SPARC: Spine with Prismatic and Revolute Compliance for Quadruped Robot

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01984" target="_blank" class="toolbar-btn">arXiv: 2510.01984v1</a>
    <a href="https://arxiv.org/pdf/2510.01984.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01984v1" 
            onclick="toggleFavorite(this, '2510.01984v1', 'SPARC: Spine with Prismatic and Revolute Compliance for Quadruped Robot')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Yue Wang

**分类**: cs.RO, eess.SY

**发布日期**: 2025-10-02

---

## 💡 一句话要点

**SPARC：用于四足机器人的具有棱柱和旋转柔顺性的脊柱模块**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `四足机器人` `脊柱模块` `柔顺性控制` `任务空间阻抗` `RNEA控制` `Stribeck摩擦补偿` `机器人运动` `机器人设计`

## 📋 核心要点

1. 现有四足机器人缺乏灵活的脊柱设计，限制了其在复杂地形下的运动能力和能量效率。
2. SPARC模块通过结合旋转和棱柱运动，以及可编程的任务空间阻抗，实现了对脊柱柔顺性的精确控制。
3. 实验验证了SPARC模块的线性力-位移特性和质量-弹簧-阻尼器响应，为脊柱柔顺性研究提供平台。

## 📝 摘要（中文）

本文提出SPARC，一个紧凑、开源的三自由度矢状面脊柱模块，它结合了旋转（俯仰）和棱柱（轴向）运动，并为四足机器人提供可编程的任务空间阻抗。该系统在一个1.26公斤的封装中集成了三个扭矩控制的执行器、一个定制的1 kHz控制板和一个受保护的电源单元，从而能够沿x、z和theta方向进行闭环刚度和阻尼整形。我们开发了一种基于RNEA的计算加速度控制器，具有平滑的Stribeck摩擦补偿，以呈现弹簧-阻尼器行为，而无需显式的惯性整形。基准实验验证了该方法。准静态推拉试验显示了线性力-位移特性，命令水平刚度跨度为300-700 N/m，相对误差<= 1.5% (R^2 >= 0.992，窄95%置信区间)。动态位移-释放试验证实了多个阻尼设置下的质量-弹簧-阻尼器响应，由于配置相关的惯性和低速摩擦效应，相位偏差小且可解释。任务空间PD控制器产生大致线性的刚度，但具有更大的可变性和耦合敏感性。SPARC为系统研究腿式运动中的脊柱柔顺性提供了一个便携式平台，并将发布完整的硬件和固件资源。

## 🔬 方法详解

**问题定义**：现有的四足机器人设计通常采用刚性或被动柔顺的脊柱，难以在复杂地形中实现高效和稳定的运动。主动控制脊柱的柔顺性可以提高机器人的适应性和能量效率，但需要紧凑、轻量且易于控制的脊柱模块。

**核心思路**：SPARC模块的核心思路是结合旋转和棱柱运动，并通过扭矩控制的执行器实现可编程的任务空间阻抗。通过精确控制执行器的扭矩，可以模拟弹簧-阻尼器的行为，从而实现对脊柱柔顺性的主动控制。这种设计允许在x、z和theta方向上独立调节刚度和阻尼。

**技术框架**：SPARC模块的整体架构包括三个扭矩控制的执行器、一个定制的1 kHz控制板和一个受保护的电源单元。控制系统采用基于RNEA（Recursive Newton-Euler Algorithm）的计算加速度控制器，该控制器具有平滑的Stribeck摩擦补偿。控制流程包括：1) 接收期望的任务空间阻抗参数；2) 计算执行器所需的扭矩；3) 通过控制板控制执行器；4) 通过传感器反馈进行闭环控制。

**关键创新**：SPARC模块的关键创新在于其紧凑的设计、可编程的任务空间阻抗以及基于RNEA的计算加速度控制器。该模块将所有必要的组件集成在一个1.26公斤的封装中，使其易于集成到各种四足机器人平台。可编程的任务空间阻抗允许用户根据不同的任务需求调整脊柱的柔顺性。基于RNEA的计算加速度控制器能够精确地模拟弹簧-阻尼器行为，而无需显式的惯性整形。

**关键设计**：SPARC模块的关键设计包括：1) 使用三个扭矩控制的执行器来实现旋转和棱柱运动；2) 设计定制的1 kHz控制板以实现高速控制；3) 使用基于RNEA的计算加速度控制器，并采用Stribeck摩擦补偿来提高控制精度；4) 通过准静态推拉试验和动态位移-释放试验来验证模块的性能。

## 📊 实验亮点

实验结果表明，SPARC模块具有良好的线性力-位移特性，命令水平刚度跨度为300-700 N/m，相对误差<= 1.5% (R^2 >= 0.992)。动态位移-释放试验证实了多个阻尼设置下的质量-弹簧-阻尼器响应。这些结果验证了SPARC模块的性能，并表明其可以作为研究脊柱柔顺性的有效平台。

## 🎯 应用场景

SPARC模块可应用于各种四足机器人平台，提高其在复杂地形中的运动能力和能量效率。例如，可以用于搜索救援机器人、农业机器人和检查机器人。通过调整脊柱的柔顺性，机器人可以更好地适应不平坦的地面，减少能量消耗，并提高运动的稳定性。该模块还可用于研究脊柱柔顺性对四足机器人运动的影响，为未来的机器人设计提供指导。

## 📄 摘要（原文）

> We present SPARC, a compact, open-source 3-DoF sagittal-plane spine module that combines revolute (pitch) and prismatic (axial) motion with programmable task-space impedance for quadruped robots. The system integrates three torque-controlled actuators, a custom 1 kHz control board, and a protected power unit in a 1.26 kg package, enabling closed-loop stiffness and damping shaping along x, z, and theta. We develop an RNEA-based computed-acceleration controller with smooth Stribeck friction compensation to render spring-damper behavior without explicit inertia shaping. Bench experiments validate the approach. Quasi-static push-pull tests show linear force-displacement characteristics with commanded horizontal stiffness spanning 300-700 N/m and <= 1.5% relative error (R^2 >= 0.992, narrow 95% CIs). Dynamic displace-and-release trials confirm mass-spring-damper responses over multiple damping settings, with small, interpretable phase deviations due to configuration-dependent inertia and low-speed friction effects. A task-space PD controller produces roughly linear stiffness but with greater variability and coupling sensitivity. SPARC provides a portable platform for systematic studies of spine compliance in legged locomotion and will be released with complete hardware and firmware resources.

