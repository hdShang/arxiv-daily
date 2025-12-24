---
layout: default
title: "Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint"
---

# Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12314" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12314v1</a>
  <a href="https://arxiv.org/pdf/2506.12314.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12314v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12314v1', 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaoshuai Ma, Haoxiang Qi, Qingqing Li, Haochen Xu, Xuechao Chen, Junyao Gao, Zhangguo Yu, Qiang Huang

**分类**: cs.RO, eess.SY

**发布日期**: 2025-06-14

---

## 💡 一句话要点

**提出动态减速比设计以增强类人机器人跳跃能力**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `类人机器人` `膝关节设计` `动态减速比` `跳跃能力` `电机输出` `运动学分析` `控制策略`

## 📋 核心要点

1. 现有的膝关节设计在跳跃时存在传动比与重心不匹配的问题，导致高功率输出时间受限。
2. 本文提出了一种动态减小的减速比设计，能够在跳跃过程中优化电机输出和膝关节运动学。
3. 实验结果显示，该设计在单关节平台上实现了63厘米的垂直跳跃，显著提升了跳跃性能。

## 📝 摘要（中文）

增强膝关节的爆发力输出对于提高类人机器人的灵活性和跨越障碍的能力至关重要。然而，膝关节与重心之间的传动比与跳跃需求不匹配，以及在高速下电机性能的下降，限制了高功率输出的持续时间，进而影响跳跃性能。为了解决这些问题，本文提出了一种新颖的膝关节设计范式，采用动态减小的减速比以实现跳跃时的爆发输出。通过对跳跃过程中电机输出特性和膝关节运动学的分析，提出了一种耦合策略，使得在关节伸展时减速比逐渐减小。高初始比率在跳跃开始时迅速增加扭矩，而逐渐减小的比率则最小化电机速度增量和功率损失，从而保持持续的高功率输出。实验验证表明，该设计在单关节平台上实现了63厘米的垂直跳跃，理论上比最佳固定比关节提高了28.1%。集成到类人机器人中，该设计实现了1.1米的水平跳跃、0.5米的垂直跳跃和0.5米的箱子跳跃。

## 🔬 方法详解

**问题定义**：本文旨在解决类人机器人膝关节在跳跃时的爆发力输出不足问题，现有方法在高速度下电机性能下降，导致高功率输出持续时间受限。

**核心思路**：提出一种动态减小的减速比设计，使得在关节伸展时减速比逐渐减小，从而优化扭矩输出和电机速度，保持高功率输出。

**技术框架**：整体架构包括膝关节设计、线性驱动器、耦合策略和参数优化四个主要模块，结合爆发跳跃控制策略进行优化。

**关键创新**：最重要的创新在于动态减小的减速比设计，与传统固定比设计相比，能够更好地适应跳跃需求，减少功率损失。

**关键设计**：关键参数设置包括初始减速比、减速比变化率等，损失函数设计用于优化电机输出特性，确保在跳跃过程中保持高效能。

## 📊 实验亮点

实验结果显示，所提出的设计在单关节平台上实现了63厘米的垂直跳跃，理论上比最佳固定比关节提高了28.1%。集成到类人机器人中后，成功实现了1.1米的水平跳跃和0.5米的垂直跳跃，展示了显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括类人机器人、仿生机器人及其他需要高效跳跃和灵活运动的机器人系统。通过提升跳跃能力，能够在救援、探索和人机协作等场景中发挥重要作用，未来可能推动机器人在复杂环境中的应用。

## 📄 摘要（原文）

> Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1\% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

