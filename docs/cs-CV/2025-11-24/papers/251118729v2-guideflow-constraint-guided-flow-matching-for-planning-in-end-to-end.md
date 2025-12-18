---
layout: default
title: GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving
---

# GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18729" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18729v2</a>
  <a href="https://arxiv.org/pdf/2511.18729.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18729v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.18729v2', 'GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Lin Liu, Caiyan Jia, Guanyi Yu, Ziying Song, JunQiao Li, Feiyang Jia, Peiliang Wu, Xiaoshuai Hao, Yandan Luo

**分类**: cs.CV

**发布日期**: 2025-11-24 (更新: 2025-12-11)

**🔗 代码/项目**: [GITHUB](https://github.com/liulin815/GuideFlow)

---

## 💡 一句话要点

**GuideFlow：一种约束引导的Flow Matching方法，用于端到端自动驾驶规划。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `自动驾驶` `端到端规划` `Flow Matching` `约束优化` `轨迹生成`

## 📋 核心要点

1. 现有端到端自动驾驶规划器存在多模态轨迹模式崩溃问题，且难以直接将安全和物理约束融入生成过程。
2. GuideFlow通过约束Flow Matching显式建模生成过程，直接在生成过程中强制执行约束，缓解模式崩溃。
3. GuideFlow在多个驾驶基准测试中表现出色，在NavSim测试集hard split上取得了SOTA结果，EPDMS得分为43.0。

## 📝 摘要（中文）

本文提出GuideFlow，一种新颖的规划框架，它利用约束Flow Matching来解决端到端自动驾驶中的规划问题。现有的模仿学习端到端规划器常常面临多模态轨迹模式崩溃的问题，无法生成多样化的轨迹方案。而生成式端到端规划器难以将关键的安全和物理约束直接融入生成过程，需要额外的优化阶段来改进输出。GuideFlow显式地建模Flow Matching过程，从而缓解模式崩溃，并允许来自各种条件信号的灵活引导。其核心贡献在于直接在Flow Matching生成过程中强制执行显式约束，而不是依赖于隐式约束编码。GuideFlow统一了Flow Matching和基于能量的模型(EBM)的训练，以增强模型自主优化能力，从而稳健地满足物理约束。此外，GuideFlow将驾驶激进程度参数化为生成过程中的控制信号，从而能够精确地操纵轨迹风格。在多个主流驾驶基准测试(Bench2Drive, NuScenes, NavSim和ADV-NuScenes)上的大量评估验证了GuideFlow的有效性。在NavSim测试集hard split (Navhard)上，GuideFlow达到了SOTA，EPDMS得分为43.0。

## 🔬 方法详解

**问题定义**：端到端自动驾驶规划旨在直接从传感器输入生成车辆的行驶轨迹。现有模仿学习方法容易陷入模式崩溃，导致轨迹多样性不足。而生成式方法难以将安全和物理约束有效地融入轨迹生成过程，需要额外的优化步骤，增加了计算负担和复杂性。

**核心思路**：GuideFlow的核心在于利用约束Flow Matching，将轨迹生成过程建模为一个连续的流动过程，并通过显式约束引导该流动过程，从而生成满足约束条件的多样化轨迹。这种方法避免了模式崩溃，并允许直接在生成过程中施加约束，无需额外的优化步骤。

**技术框架**：GuideFlow框架包含以下主要模块：1) Flow Matching模块，用于建模轨迹生成过程；2) 约束引导模块，用于将安全和物理约束融入生成过程；3) 基于能量的模型(EBM)，用于增强模型自主优化能力，确保满足物理约束；4) 驾驶激进程度控制模块，用于控制轨迹的驾驶风格。整体流程为：输入场景信息和驾驶激进程度控制信号，Flow Matching模块生成初始轨迹，约束引导模块施加约束，EBM模块优化轨迹，最终输出满足约束条件且具有特定驾驶风格的轨迹。

**关键创新**：GuideFlow的关键创新在于：1) 显式约束引导的Flow Matching，可以直接在生成过程中施加约束，避免了额外的优化步骤；2) 统一Flow Matching和EBM的训练，增强了模型自主优化能力，确保满足物理约束；3) 将驾驶激进程度参数化为控制信号，实现了对轨迹风格的精确控制。与现有方法相比，GuideFlow能够生成更安全、更合理、更具多样性的轨迹。

**关键设计**：GuideFlow的关键设计包括：1) 使用神经网络参数化Flow Matching过程中的速度场；2) 使用拉格朗日乘子法将约束条件转化为损失函数的一部分，从而在训练过程中强制执行约束；3) 设计特定的EBM结构，以有效地学习物理约束；4) 将驾驶激进程度映射到速度场的参数空间，从而实现对轨迹风格的控制。

## 📊 实验亮点

GuideFlow在Bench2Drive, NuScenes, NavSim和ADV-NuScenes等多个主流驾驶基准测试中进行了广泛评估，结果表明GuideFlow能够显著提高自动驾驶规划的性能。特别是在NavSim测试集hard split (Navhard)上，GuideFlow达到了SOTA，EPDMS得分为43.0，验证了其在复杂场景下的有效性。

## 🎯 应用场景

GuideFlow在自动驾驶领域具有广泛的应用前景，可用于提高自动驾驶系统的安全性、可靠性和舒适性。例如，可以应用于城市道路、高速公路等不同场景的自动驾驶，也可以用于自动泊车、自动避障等特定任务。此外，GuideFlow还可以应用于驾驶员辅助系统，为驾驶员提供更安全、更舒适的驾驶体验。该研究的未来影响在于推动自动驾驶技术的进步，加速自动驾驶汽车的商业化落地。

## 📄 摘要（原文）

> Driving planning is a critical component of end-to-end (E2E) autonomous driving. However, prevailing Imitative E2E Planners often suffer from multimodal trajectory mode collapse, failing to produce diverse trajectory proposals. Meanwhile, Generative E2E Planners struggle to incorporate crucial safety and physical constraints directly into the generative process, necessitating an additional optimization stage to refine their outputs. In this paper, we propose \textit{\textbf{GuideFlow}}, a novel planning framework that leverages Constrained Flow Matching. Concretely, \textit{\textbf{GuideFlow}} explicitly models the flow matching process, which inherently mitigates mode collapse and allows for flexible guidance from various conditioning signals. Our core contribution lies in directly enforcing explicit constraints within the flow matching generation process, rather than relying on implicit constraint encoding. Crucially, \textit{\textbf{GuideFlow}} unifies the training of the flow matching with the Energy-Based Model (EBM) to enhance the model's autonomous optimization capability to robustly satisfy physical constraints. Secondly, \textit{\textbf{GuideFlow}} parameterizes driving aggressiveness as a control signal during generation, enabling precise manipulation of trajectory style. Extensive evaluations on major driving benchmarks (Bench2Drive, NuScenes, NavSim and ADV-NuScenes) validate the effectiveness of \textit{\textbf{GuideFlow}}. Notably, on the NavSim test hard split (Navhard), \textit{\textbf{GuideFlow}} achieved SOTA with an EPDMS score of 43.0. The code will be in https://github.com/liulin815/GuideFlow.

