---
layout: default
title: "UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation"
---

# UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22441" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22441v1</a>
  <a href="https://arxiv.org/pdf/2509.22441.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22441v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22441v1', 'UnderwaterVLA: Dual-brain Vision-Language-Action architecture for Autonomous Underwater Navigation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhangyuan Wang, Yunpeng Zhu, Yuqi Yan, Xiaoyuan Tian, Xinhao Shao, Meixuan Li, Weikun Li, Guangsheng Su, Weicheng Cui, Dixia Fan

**分类**: cs.RO

**发布日期**: 2025-09-26

**备注**: This paper introduces the first VLA framework for AUVs, featuring a dual-brain architecture and zero-data MPC for real-world underwater navigation

---

## 💡 一句话要点

**提出UnderwaterVLA，用于水下自主导航，提升复杂水域任务完成度。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `水下机器人` `自主导航` `视觉-语言-动作模型` `模型预测控制` `双脑架构`

## 📋 核心要点

1. 水下环境复杂，存在水动力扰动、通信带宽限制和视觉退化等问题，导致现有水下导航方法鲁棒性不足。
2. UnderwaterVLA采用双脑架构分离高低层控制，并引入VLA模型进行可解释推理，结合流体动力学MPC进行实时补偿。
3. 实验表明，UnderwaterVLA在视觉退化条件下降低了导航误差，任务完成度比基线提高了19%到27%。

## 📝 摘要（中文）

本文提出了一种名为UnderwaterVLA的新型水下自主导航框架，该框架集成了多模态基础模型和具身智能系统。由于水动力扰动、有限的通信带宽以及浑浊水域中退化的传感，水下作业仍然很困难。为了应对这些挑战，我们引入了三项创新。首先，双脑架构将高层任务推理与低层反应控制分离，从而在通信和计算约束下实现稳健运行。其次，我们首次将视觉-语言-动作（VLA）模型应用于水下机器人，结合结构化的思维链推理以实现可解释的决策。第三，一种基于流体动力学的模型预测控制（MPC）方案实时补偿流体效应，而无需昂贵的特定于任务的训练。现场测试的实验结果表明，UnderwaterVLA降低了退化视觉条件下的导航误差，同时比基线提高了19%到27%的任务完成度。通过最大限度地减少对水下特定训练数据的依赖并提高跨环境的适应性，UnderwaterVLA为下一代智能AUV提供了一条可扩展且经济高效的路径。

## 🔬 方法详解

**问题定义**：水下自主导航面临的主要问题是水动力扰动、通信带宽限制以及浑浊水域中传感器性能下降，这些因素导致传统导航方法在复杂水下环境中表现不佳，需要大量特定环境的数据训练，泛化性差。现有方法难以在资源受限的环境中进行有效的任务规划和控制。

**核心思路**：UnderwaterVLA的核心思路是将高层任务推理和低层反应控制解耦，通过双脑架构实现。高层“大脑”负责任务规划和决策，利用视觉-语言-动作模型进行推理；低层“大脑”负责实时控制，采用模型预测控制（MPC）补偿流体动力学影响。这种设计旨在提高系统的鲁棒性、可解释性和适应性。

**技术框架**：UnderwaterVLA的整体架构包含三个主要模块：1) 双脑架构：包括高层任务推理脑和低层反应控制脑。2) 视觉-语言-动作（VLA）模型：用于高层任务规划和决策，通过链式思维进行推理。3) 基于流体动力学的模型预测控制（MPC）：用于低层实时控制，补偿水动力影响。整个流程是：首先，VLA模型根据视觉输入和任务指令生成行动序列；然后，MPC根据当前状态和行动序列生成控制指令，驱动AUV执行任务。

**关键创新**：UnderwaterVLA的关键创新在于：1) 双脑架构，有效分离了高层推理和低层控制，提高了系统的鲁棒性。2) 首次将VLA模型应用于水下机器人，实现了可解释的决策过程。3) 提出了基于流体动力学的MPC方案，无需大量特定任务的训练数据即可实现实时补偿。与现有方法相比，UnderwaterVLA更具通用性和适应性。

**关键设计**：VLA模型采用预训练的视觉-语言模型，并针对水下环境进行了微调。MPC方案的关键在于准确建模水动力影响，并设计合适的成本函数，以实现精确的轨迹跟踪和姿态控制。具体参数设置和网络结构细节在论文中进行了详细描述（未知）。

## 📊 实验亮点

实验结果表明，UnderwaterVLA在退化视觉条件下显著降低了导航误差，并且任务完成度比基线方法提高了19%到27%。这些结果验证了UnderwaterVLA在复杂水下环境中具有优越的性能和鲁棒性。该框架最大限度地减少了对水下特定训练数据的依赖，并提高了跨环境的适应性。

## 🎯 应用场景

UnderwaterVLA可应用于水下环境监测、水下基础设施维护、水下搜救、海洋资源勘探等领域。该研究降低了对水下特定训练数据的依赖，提高了AUV在复杂环境中的适应性，为下一代智能水下机器人提供了可扩展且经济高效的解决方案，具有重要的实际应用价值和广阔的未来发展前景。

## 📄 摘要（原文）

> This paper presents UnderwaterVLA, a novel framework for autonomous underwater navigation that integrates multimodal foundation models with embodied intelligence systems. Underwater operations remain difficult due to hydrodynamic disturbances, limited communication bandwidth, and degraded sensing in turbid waters. To address these challenges, we introduce three innovations. First, a dual-brain architecture decouples high-level mission reasoning from low-level reactive control, enabling robust operation under communication and computational constraints. Second, we apply Vision-Language-Action(VLA) models to underwater robotics for the first time, incorporating structured chain-of-thought reasoning for interpretable decision-making. Third, a hydrodynamics-informed Model Predictive Control(MPC) scheme compensates for fluid effects in real time without costly task-specific training. Experimental results in field tests show that UnderwaterVLA reduces navigation errors in degraded visual conditions while maintaining higher task completion by 19% to 27% over baseline. By minimizing reliance on underwater-specific training data and improving adaptability across environments, UnderwaterVLA provides a scalable and cost-effective path toward the next generation of intelligent AUVs.

