---
layout: default
title: Neural-Enhanced Rate Adaptation and Computation Distribution for Emerging mmWave Multi-User 3D Video Streaming Systems
---

# Neural-Enhanced Rate Adaptation and Computation Distribution for Emerging mmWave Multi-User 3D Video Streaming Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13337" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13337v1</a>
  <a href="https://arxiv.org/pdf/2505.13337.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13337v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13337v1', 'Neural-Enhanced Rate Adaptation and Computation Distribution for Emerging mmWave Multi-User 3D Video Streaming Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Babak Badnava, Jacob Chakareski, Morteza Hashemi

**分类**: cs.IT, cs.ET, cs.MM, eess.SY

**发布日期**: 2025-05-19

**备注**: Accepted to be published in IEEE Transaction on Multimedia

---

## 💡 一句话要点

**提出基于深度强化学习的多任务速率适应与计算分配方法以优化360度视频流**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `毫米波通信` `深度强化学习` `视频流优化` `虚拟现实` `多任务学习`

## 📋 核心要点

1. 现有方法在多用户环境中难以有效平衡通信与计算资源，导致视频流质量不稳定。
2. 提出了一种深度强化学习框架MTRC，能够实时调整视频比特率和计算分配，优化用户体验。
3. 实验结果表明，C1R2方法在PSNR、缓冲时间和质量变化方面均显著优于现有算法，提升幅度达到6.06 dB和2.70倍。

## 📝 摘要（中文）

本文研究了在边缘计算支持的毫米波多用户虚拟现实系统中，针对360度视频流的多任务边缘用户通信计算资源分配问题。为平衡通信与计算之间的权衡，提出了一个视频质量最大化问题，并结合多任务/多用户的相互依赖性和缓冲时间/质量变化约束，构建了深度强化学习框架（MTRC）来解决该问题。该方法不依赖于环境的先验知识，仅利用视频流统计数据和内容信息，实时调整视频比特率和计算分配。通过真实的毫米波网络数据和360度视频数据集进行训练，评估了期望的用户体验（QoE）、视口峰值信噪比（PSNR）、缓冲时间和质量变化等性能指标。

## 🔬 方法详解

**问题定义**：本文旨在解决在毫米波多用户虚拟现实系统中，如何有效分配通信与计算资源以优化360度视频流质量的问题。现有方法未能充分考虑多任务和多用户之间的相互依赖性，导致视频流体验不佳。

**核心思路**：提出的MTRC框架通过深度强化学习，实时调整视频比特率和计算分配，利用历史视频流统计数据和内容信息，避免了对环境先验知识的依赖。

**技术框架**：整体架构包括三个主要模块：环境状态观察、策略学习和动作执行。环境状态观察模块收集视频流的实时统计数据，策略学习模块通过深度强化学习算法优化资源分配，动作执行模块根据学习到的策略调整比特率和计算分配。

**关键创新**：本研究的关键创新在于引入了神经网络级联来捕捉任务间的相互依赖性，并提出了两个新变体R1C2和C1R2，显著提升了资源分配的灵活性和效果。

**关键设计**：在设计中，采用了基于历史数据的损失函数，优化了网络结构以适应多任务学习，确保了模型在动态环境下的适应性和实时性。

## 📊 实验亮点

实验结果显示，提出的C1R2方法在PSNR上提高了5.21-6.06 dB，缓冲时间减少了2.18-2.70倍，质量变化降低了4.14-4.50 dB，显著优于现有的速率适应算法，验证了方法的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、增强现实和高质量视频流服务等。通过优化资源分配，可以显著提升用户体验，降低延迟和缓冲时间，推动下一代视频流技术的发展，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> We investigate multitask edge-user communication-computation resource allocation for $360^\circ$ video streaming in an edge-computing enabled millimeter wave (mmWave) multi-user virtual reality system. To balance the communication-computation trade-offs that arise herein, we formulate a video quality maximization problem that integrates interdependent multitask/multi-user action spaces and rebuffering time/quality variation constraints. We formulate a deep reinforcement learning framework for \underline{m}ulti-\underline{t}ask \underline{r}ate adaptation and \underline{c}omputation distribution (MTRC) to solve the problem of interest. Our solution does not rely on a priori knowledge about the environment and uses only prior video streaming statistics (e.g., throughput, decoding time, and transmission delay), and content information, to adjust the assigned video bitrates and computation distribution, as it observes the induced streaming performance online. Moreover, to capture the task interdependence in the environment, we leverage neural network cascades to extend our MTRC method to two novel variants denoted as R1C2 and C1R2. We train all three methods with real-world mmWave network traces and $360^\circ$ video datasets to evaluate their performance in terms of expected quality of experience (QoE), viewport peak signal-to-noise ratio (PSNR), rebuffering time, and quality variation. We outperform state-of-the-art rate adaptation algorithms, with C1R2 showing best results and achieving $5.21-6.06$ dB PSNR gains, $2.18-2.70$x rebuffering time reduction, and $4.14-4.50$ dB quality variation reduction.

