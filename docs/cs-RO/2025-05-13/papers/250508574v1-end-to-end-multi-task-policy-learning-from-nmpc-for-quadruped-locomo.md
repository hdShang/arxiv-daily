---
layout: default
title: End-to-End Multi-Task Policy Learning from NMPC for Quadruped Locomotion
---

# End-to-End Multi-Task Policy Learning from NMPC for Quadruped Locomotion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.08574" class="toolbar-btn" target="_blank">📄 arXiv: 2505.08574v1</a>
  <a href="https://arxiv.org/pdf/2505.08574.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.08574v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.08574v1', 'End-to-End Multi-Task Policy Learning from NMPC for Quadruped Locomotion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anudeep Sajja, Shahram Khorshidi, Sebastian Houben, Maren Bennewitz

**分类**: cs.RO

**发布日期**: 2025-05-13

---

## 💡 一句话要点

**提出多任务学习框架以解决四足机器人运动控制问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `四足机器人` `多任务学习` `非线性模型预测控制` `运动控制` `实时部署` `神经网络` `适应性运动`

## 📋 核心要点

1. 四足机器人在复杂环境中的运动控制面临非线性动力学和高计算需求的挑战，现有NMPC方法难以实时应用。
2. 提出的多任务学习框架通过专家示范训练神经网络，直接从传感器输入预测多种步态的动作，简化控制流程。
3. 在Go1机器人上进行的实验表明，该方法能够准确再现专家行为，实现平滑步态切换，并在多任务中表现出色。

## 📝 摘要（中文）

四足机器人在复杂、不规则环境中的表现优于轮式机器人，但由于其非线性动力学和高自由度，适应性运动控制仍然面临挑战。基于优化的控制器如非线性模型预测控制（NMPC）虽然表现出色，但对准确状态估计和高计算开销的依赖使其在实际应用中困难重重。本文提出了一种多任务学习（MTL）框架，利用专家NMPC示范训练单一神经网络，直接从原始本体传感器输入中预测多种运动行为的动作。通过在四足机器人Go1上进行广泛评估，证明了该方法能够准确再现专家行为，实现平滑的步态切换，并简化实时部署的控制流程。我们的MTL架构在统一策略中学习多样化步态，在所有任务中实现了高R²分数的关节目标预测。

## 🔬 方法详解

**问题定义**：本文旨在解决四足机器人在复杂环境中运动控制的挑战，现有的NMPC方法依赖于准确的状态估计和高计算开销，限制了其实时应用的可行性。

**核心思路**：通过多任务学习框架，利用专家NMPC示范来训练一个单一的神经网络，使其能够从原始传感器输入中直接预测多种运动行为的动作，从而简化控制流程并提高适应性。

**技术框架**：整体架构包括数据采集、专家示范、神经网络训练和实时控制四个主要模块。首先收集四足机器人在不同步态下的传感器数据，然后利用这些数据训练神经网络，最后在实际机器人上进行实时控制。

**关键创新**：最重要的创新在于将多任务学习与NMPC结合，通过单一神经网络实现多种步态的学习与切换，显著降低了计算复杂度和实时控制的难度。

**关键设计**：在网络结构上，采用了适应性损失函数以平衡不同任务的学习效果，并通过优化超参数来提高模型的泛化能力，确保在多种步态下的高效表现。

## 📊 实验亮点

实验结果显示，所提出的多任务学习框架在Go1机器人上成功再现了专家行为，步态切换平滑，且在所有任务中实现了高R²分数，表明模型在关节目标预测上的准确性显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括服务机器人、救援机器人以及任何需要在复杂环境中高效移动的四足机器人。通过简化控制流程和提高适应性，该方法能够在实际应用中显著提升四足机器人的性能和灵活性，未来可能推动更多自主移动系统的发展。

## 📄 摘要（原文）

> Quadruped robots excel in traversing complex, unstructured environments where wheeled robots often fail. However, enabling efficient and adaptable locomotion remains challenging due to the quadrupeds' nonlinear dynamics, high degrees of freedom, and the computational demands of real-time control. Optimization-based controllers, such as Nonlinear Model Predictive Control (NMPC), have shown strong performance, but their reliance on accurate state estimation and high computational overhead makes deployment in real-world settings challenging. In this work, we present a Multi-Task Learning (MTL) framework in which expert NMPC demonstrations are used to train a single neural network to predict actions for multiple locomotion behaviors directly from raw proprioceptive sensor inputs. We evaluate our approach extensively on the quadruped robot Go1, both in simulation and on real hardware, demonstrating that it accurately reproduces expert behavior, allows smooth gait switching, and simplifies the control pipeline for real-time deployment. Our MTL architecture enables learning diverse gaits within a unified policy, achieving high $R^{2}$ scores for predicted joint targets across all tasks.

