---
layout: default
title: A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs
---

# A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00077" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00077v1</a>
  <a href="https://arxiv.org/pdf/2512.00077.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00077v1" onclick="toggleFavorite(this, '2512.00077v1', 'A Hierarchical Framework for Humanoid Locomotion with Supernumerary Limbs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bowen Zhi

**分类**: cs.RO

**发布日期**: 2025-11-25

**🔗 代码/项目**: [GITHUB](https://github.com/heyzbw/HuSLs)

---

## 💡 一句话要点

**提出一种分层控制框架，提升超冗余肢人形机器人运动稳定性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `人形机器人` `超冗余肢` `分层控制` `动态平衡` `模仿学习`

## 📋 核心要点

1. 超冗余肢的引入给人形机器人带来了显著的动态扰动，导致稳定性成为关键挑战。
2. 论文提出一种解耦的分层控制架构，结合学习步态和模型平衡，利用超冗余肢进行动态平衡。
3. 实验表明，该方法显著提升了人形机器人的运动稳定性，并使步态更接近基线状态。

## 📝 摘要（中文）

本研究针对人形机器人集成超冗余肢(SLs)带来的稳定性挑战，设计了一种新颖的分层控制架构，以提高其运动稳定性。该框架的核心是解耦策略，结合了基于学习的运动控制和基于模型的平衡控制。底层组件通过模仿学习和课程学习，为优必选H1人形机器人生成行走步态。高层组件主动利用SLs进行动态平衡。在基于物理的仿真环境中，通过三种条件评估了系统的有效性：无人形机器人的基线步态（基线行走）、携带静态SL载荷的行走（静态载荷）以及使用主动动态平衡控制器的行走（动态平衡）。评估结果表明，动态平衡控制器提高了稳定性。与静态载荷条件相比，平衡策略产生了更接近基线的步态模式，并将质心(CoM)轨迹的动态时间规整(DTW)距离降低了47%。平衡控制器还改善了步态周期内的再稳定过程，并实现了更协调的反相地面反作用力(GRF)模式。结果表明，解耦的分层设计可以有效地减轻由SLs的质量和运动引起的内部动态扰动，从而使配备功能肢体的人形机器人能够稳定运动。

## 🔬 方法详解

**问题定义**：论文旨在解决人形机器人集成超冗余肢后，由于其质量和运动产生的动态扰动，导致机器人难以保持稳定运动的问题。现有方法难以有效应对这种内部动态扰动，导致机器人步态不稳定，甚至跌倒。

**核心思路**：论文的核心思路是将运动控制和平衡控制解耦，采用分层控制架构。底层专注于生成稳定的行走步态，高层则利用超冗余肢进行主动动态平衡，从而减轻超冗余肢带来的扰动。这种解耦设计使得控制更加模块化，易于优化和调整。

**技术框架**：整体架构分为两层：底层是基于模仿学习的步态生成器，负责生成基础的行走步态。高层是基于模型的动态平衡控制器，利用超冗余肢的运动来补偿由超冗余肢自身引起的动态扰动。底层步态生成器为高层平衡控制器提供参考轨迹和状态信息，高层控制器则通过控制超冗余肢的运动来调整机器人的整体平衡。

**关键创新**：该论文的关键创新在于将学习的步态生成器与基于模型的平衡控制器相结合，形成一个解耦的分层控制架构。这种架构能够有效地分离运动控制和平衡控制，使得系统能够更好地应对超冗余肢带来的动态扰动。此外，利用超冗余肢进行主动动态平衡也是一个重要的创新点。

**关键设计**：底层步态生成器使用模仿学习，通过学习人类的行走数据来生成自然的行走步态。课程学习被用于逐步增加训练难度，提高步态生成器的鲁棒性。高层平衡控制器基于质心动力学模型，通过优化超冗余肢的运动轨迹来最小化质心偏移。具体参数设置和损失函数细节在论文中未明确给出，属于未知信息。

## 📊 实验亮点

实验结果表明，动态平衡控制器显著提高了人形机器人的运动稳定性。与静态载荷条件相比，平衡策略使步态模式更接近基线，质心轨迹的动态时间规整距离降低了47%。此外，平衡控制器还改善了步态周期内的再稳定过程，并实现了更协调的反相地面反作用力模式。这些数据表明，该方法能够有效地减轻超冗余肢带来的动态扰动。

## 🎯 应用场景

该研究成果可应用于需要人形机器人携带额外负载或执行复杂操作的场景，例如搜救、建筑、医疗等。通过超冗余肢的辅助，机器人可以更稳定地行走和操作，提高工作效率和安全性。未来，该技术有望扩展到更多类型的人形机器人和外骨骼设备。

## 📄 摘要（原文）

> The integration of Supernumerary Limbs (SLs) on humanoid robots poses a significant stability challenge due to the dynamic perturbations they introduce. This thesis addresses this issue by designing a novel hierarchical control architecture to improve humanoid locomotion stability with SLs. The core of this framework is a decoupled strategy that combines learning-based locomotion with model-based balancing. The low-level component consists of a walking gait for a Unitree H1 humanoid through imitation learning and curriculum learning. The high-level component actively utilizes the SLs for dynamic balancing. The effectiveness of the system is evaluated in a physics-based simulation under three conditions: baseline gait for an unladen humanoid (baseline walking), walking with a static SL payload (static payload), and walking with the active dynamic balancing controller (dynamic balancing). Our evaluation shows that the dynamic balancing controller improves stability. Compared to the static payload condition, the balancing strategy yields a gait pattern closer to the baseline and decreases the Dynamic Time Warping (DTW) distance of the CoM trajectory by 47\%. The balancing controller also improves the re-stabilization within gait cycles and achieves a more coordinated anti-phase pattern of Ground Reaction Forces (GRF). The results demonstrate that a decoupled, hierarchical design can effectively mitigate the internal dynamic disturbances arising from the mass and movement of the SLs, enabling stable locomotion for humanoids equipped with functional limbs. Code and videos are available here: https://github.com/heyzbw/HuSLs.

