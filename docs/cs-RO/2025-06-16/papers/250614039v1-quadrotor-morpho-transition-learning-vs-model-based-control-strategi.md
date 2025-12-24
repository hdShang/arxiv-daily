---
layout: default
title: "Quadrotor Morpho-Transition: Learning vs Model-Based Control Strategies"
---

# Quadrotor Morpho-Transition: Learning vs Model-Based Control Strategies

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14039" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14039v1</a>
  <a href="https://arxiv.org/pdf/2506.14039.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14039v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14039v1', 'Quadrotor Morpho-Transition: Learning vs Model-Based Control Strategies')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ioannis Mandralis, Richard M. Murray, Morteza Gharib

**分类**: cs.RO, eess.SY

**发布日期**: 2025-06-16

---

## 💡 一句话要点

**提出基于强化学习的四旋翼变形控制策略以解决复杂过渡问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `四旋翼` `变形过渡` `强化学习` `控制策略` `模型预测控制` `气动交互` `自主飞行`

## 📋 核心要点

1. 现有的模型基础控制方法在处理四旋翼变形过渡时存在未建模动态和接触规划的局限性。
2. 本文提出了一种基于强化学习的控制策略，通过端到端训练来学习变形过渡的策略。
3. 实验结果表明，强化学习控制策略在考虑电机动态和延迟时能够成功转移到硬件，并实现灵活着陆。

## 📝 摘要（中文）

四旋翼变形过渡，即通过空中变形从空中过渡到地面，涉及复杂的气动交互和接近执行器饱和的操作，给控制器设计带来了挑战。尽管已有模型基础控制方法，但由于未建模的动态和接触规划的需求，这些方法仍然有限。本文训练了一种端到端的强化学习控制器以学习变形过渡策略，并成功转移到硬件上。研究发现，强化学习控制策略能够实现灵活着陆，但只有在考虑电机动态和观测延迟的情况下才能转移到硬件上。相比之下，基线的模型预测控制（MPC）控制器在没有执行器动态和延迟知识的情况下即可直接转移，但在未知执行器故障的情况下恢复能力较差。我们的研究为需要空中变形的灵活飞行四旋翼机动控制开辟了新的方向。

## 🔬 方法详解

**问题定义**：本文旨在解决四旋翼在空中变形过渡时的控制问题，现有模型基础控制方法在应对未建模动态和接触规划时存在局限性，导致控制效果不佳。

**核心思路**：论文提出通过强化学习训练控制器，学习变形过渡策略，以应对复杂的气动交互和执行器饱和问题，从而提高控制的灵活性和鲁棒性。

**技术框架**：整体架构包括数据采集、强化学习训练和硬件转移三个主要阶段。首先，通过模拟环境收集数据，然后使用这些数据训练强化学习模型，最后将训练好的模型应用于实际硬件中进行测试。

**关键创新**：最重要的技术创新在于使用强化学习方法来学习变形过渡策略，并成功实现了从模拟到硬件的转移，克服了传统模型基础控制方法的局限性。

**关键设计**：在训练过程中，考虑了电机动态和观测延迟等关键参数，设计了适应这些因素的损失函数和网络结构，以确保控制策略的有效性和稳定性。

## 📊 实验亮点

实验结果显示，强化学习控制策略在考虑电机动态和延迟时成功转移到硬件，实现了灵活着陆。相比之下，基线的MPC控制器虽然能够直接转移，但在未知执行器故障情况下的恢复能力较差，表明强化学习方法在复杂任务中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括无人机的自主飞行、复杂环境下的搜索与救援任务、以及多种任务的协同作业等。通过提高四旋翼在空中变形过程中的控制能力，能够显著提升其在动态环境中的适应性和灵活性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Quadrotor Morpho-Transition, or the act of transitioning from air to ground through mid-air transformation, involves complex aerodynamic interactions and a need to operate near actuator saturation, complicating controller design. In recent work, morpho-transition has been studied from a model-based control perspective, but these approaches remain limited due to unmodeled dynamics and the requirement for planning through contacts. Here, we train an end-to-end Reinforcement Learning (RL) controller to learn a morpho-transition policy and demonstrate successful transfer to hardware. We find that the RL control policy achieves agile landing, but only transfers to hardware if motor dynamics and observation delays are taken into account. On the other hand, a baseline MPC controller transfers out-of-the-box without knowledge of the actuator dynamics and delays, at the cost of reduced recovery from disturbances in the event of unknown actuator failures. Our work opens the way for more robust control of agile in-flight quadrotor maneuvers that require mid-air transformation.

