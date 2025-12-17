---
layout: default
title: AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion
---

# AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.18857" class="toolbar-btn" target="_blank">📄 arXiv: 2511.18857v1</a>
  <a href="https://arxiv.org/pdf/2511.18857.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.18857v1" onclick="toggleFavorite(this, '2511.18857v1', 'AutoOdom: Learning Auto-regressive Proprioceptive Odometry for Legged Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changsheng Luo, Yushi Wang, Wenhan Cai, Mingguo Zhao

**分类**: cs.RO

**发布日期**: 2025-11-24

---

## 💡 一句话要点

**AutoOdom：用于足式机器人运动的自回归本体系里程计学习方法**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `足式机器人` `本体系里程计` `自回归学习` `仿真到现实迁移` `机器人导航`

## 📋 核心要点

1. 现有足式机器人里程计方法在复杂环境中存在建模误差、累积漂移和仿真到现实迁移困难等问题。
2. AutoOdom采用两阶段训练，先在仿真环境中学习运动动力学，再通过自回归机制在真实数据上进行微调。
3. 实验表明，AutoOdom在绝对轨迹误差、Umeyama对齐误差和相对位姿误差上均显著优于现有方法。

## 📝 摘要（中文）

在GPS拒止和视觉退化的环境中，精确的本体系里程计对于足式机器人导航至关重要。现有方法面临诸多限制：解析滤波方法受困于建模不确定性和累积漂移；混合学习-滤波方法仍受限于解析组件；纯学习方法难以实现从仿真到现实的迁移，并需要大量真实世界数据。本文提出了AutoOdom，一种新颖的自回归本体系里程计系统，通过创新的两阶段训练范式克服了这些挑战。第一阶段利用大规模仿真数据学习足式运动中复杂的非线性动力学和快速变化的接触状态，第二阶段引入自回归增强机制，使用有限的真实世界数据有效弥合了仿真到现实的差距。关键创新在于自回归训练方法，模型通过学习自身的预测来增强对传感器噪声的抵抗力，并提高在高度动态环境中的鲁棒性。在Booster T1人形机器人上的综合实验验证表明，AutoOdom在所有评估指标上均显著优于最先进的方法，绝对轨迹误差降低了57.2%，Umeyama对齐误差降低了59.2%，相对位姿误差降低了36.2%（与Legolas基线相比）。大量的消融研究提供了关于传感器模态选择和时间建模的关键见解，揭示了关于IMU加速度数据的反直觉发现，并验证了我们为具有挑战性的运动场景中鲁棒的本体系里程计所做的系统设计选择。

## 🔬 方法详解

**问题定义**：足式机器人在GPS拒止或视觉受限的环境中，依赖本体系传感器（如IMU和关节编码器）进行里程计推算。现有方法，如基于滤波的方法，依赖于精确的运动学和动力学模型，容易受到建模误差和累积漂移的影响。纯学习方法虽然避免了显式建模，但需要大量真实数据进行训练，且难以从仿真环境迁移到真实环境。因此，如何在有限的真实数据下，学习到鲁棒且精确的本体系里程计是一个关键问题。

**核心思路**：AutoOdom的核心思路是利用大规模仿真数据预训练模型，学习足式机器人的运动动力学，然后通过自回归训练，利用少量真实数据微调模型，从而弥合仿真和现实之间的差距。自回归训练的关键在于让模型学习从自身的预测中进行纠正，从而提高对传感器噪声和环境变化的鲁棒性。

**技术框架**：AutoOdom系统包含两个主要阶段：1) 仿真预训练阶段：使用大规模仿真数据训练一个初始的里程计模型，该模型学习从本体系传感器数据（如IMU和关节角度）预测机器人位姿的变化。2) 自回归微调阶段：使用少量真实世界数据，通过自回归的方式微调预训练模型。在自回归训练中，模型不仅接收真实的传感器数据，还接收自身前一时刻的位姿预测作为输入，从而学习纠正自身预测误差的能力。

**关键创新**：AutoOdom的关键创新在于其自回归训练方法。传统的里程计方法通常假设传感器数据是独立的，而忽略了时间上的相关性。AutoOdom通过将前一时刻的位姿预测作为输入，显式地建模了时间上的依赖关系，从而提高了模型的鲁棒性和精度。此外，两阶段训练范式有效地利用了仿真数据，减少了对真实数据的依赖。

**关键设计**：AutoOdom使用循环神经网络（RNN）作为其主要架构，以捕捉时间序列数据中的依赖关系。损失函数包括位姿预测误差和速度预测误差。在自回归训练中，引入了Teacher Forcing策略，即在训练初期使用真实的位姿作为输入，然后逐渐过渡到使用模型的预测位姿作为输入，从而提高模型的稳定性。此外，作者还进行了消融研究，探索了不同传感器模态（如IMU加速度计和陀螺仪）对性能的影响。

## 📊 实验亮点

AutoOdom在Booster T1人形机器人上进行了实验验证，结果表明，与Legolas基线相比，AutoOdom在绝对轨迹误差上降低了57.2%，在Umeyama对齐误差上降低了59.2%，在相对位姿误差上降低了36.2%。这些结果表明，AutoOdom在精度和鲁棒性方面均显著优于现有方法。

## 🎯 应用场景

AutoOdom可应用于各种足式机器人的自主导航，尤其是在GPS拒止或视觉受限的复杂环境中，例如灾难救援、地下矿井勘探、以及室内服务机器人等。该研究成果有助于提高足式机器人在实际应用中的可靠性和适应性，推动足式机器人在更广泛领域的应用。

## 📄 摘要（原文）

> Accurate proprioceptive odometry is fundamental for legged robot navigation in GPS-denied and visually degraded environments where conventional visual odometry systems fail. Current approaches face critical limitations: analytical filtering methods suffer from modeling uncertainties and cumulative drift, hybrid learning-filtering approaches remain constrained by their analytical components, while pure learning-based methods struggle with simulation-to-reality transfer and demand extensive real-world data collection. This paper introduces AutoOdom, a novel autoregressive proprioceptive odometry system that overcomes these challenges through an innovative two-stage training paradigm. Stage 1 employs large-scale simulation data to learn complex nonlinear dynamics and rapidly changing contact states inherent in legged locomotion, while Stage 2 introduces an autoregressive enhancement mechanism using limited real-world data to effectively bridge the sim-to-real gap. The key innovation lies in our autoregressive training approach, where the model learns from its own predictions to develop resilience against sensor noise and improve robustness in highly dynamic environments. Comprehensive experimental validation on the Booster T1 humanoid robot demonstrates that AutoOdom significantly outperforms state-of-the-art methods across all evaluation metrics, achieving 57.2% improvement in absolute trajectory error, 59.2% improvement in Umeyama-aligned error, and 36.2% improvement in relative pose error compared to the Legolas baseline. Extensive ablation studies provide critical insights into sensor modality selection and temporal modeling, revealing counterintuitive findings about IMU acceleration data and validating our systematic design choices for robust proprioceptive odometry in challenging locomotion scenarios.

