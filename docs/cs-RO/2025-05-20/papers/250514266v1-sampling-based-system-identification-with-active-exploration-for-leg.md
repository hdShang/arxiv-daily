---
layout: default
title: Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning
---

# Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14266" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14266v1</a>
  <a href="https://arxiv.org/pdf/2505.14266.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14266v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14266v1', 'Sampling-Based System Identification with Active Exploration for Legged Robot Sim2Real Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nikhil Sobanbabu, Guanqi He, Tairan He, Yuxiang Yang, Guanya Shi

**分类**: cs.RO

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出SPI-Active以解决腿部机器人Sim2Real学习问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `Sim-to-real` `系统识别` `腿部机器人` `主动探索` `领域随机化` `物理参数识别` `机器学习` `机器人控制`

## 📋 核心要点

1. 现有方法如领域随机化在处理Sim-to-real差异时常依赖启发式，导致策略性能不稳定。
2. 论文提出SPI-Active，通过大规模并行采样和主动探索策略，精准识别腿部机器人的物理参数。
3. 实验结果显示，SPI-Active在多种运动任务中实现了42-63%的性能提升，显著改善了sim-to-real转移效果。

## 📝 摘要（中文）

Sim-to-real差异阻碍了基于学习的策略在现实世界中实现高精度任务。虽然领域随机化（DR）常用于弥合这一差距，但通常依赖启发式方法，可能导致过于保守的策略，且在未正确调优时性能下降。系统识别（Sys-ID）提供了一种有针对性的方法，但标准技术依赖于可微分动力学和/或直接扭矩测量，这些假设在接触丰富的腿部系统中很少成立。为此，我们提出了SPI-Active（基于采样的参数识别与主动探索），这是一个两阶段框架，旨在估计腿部机器人的物理参数，以最小化sim-to-real差距。SPI-Active通过大规模并行采样稳健地识别关键物理参数，最小化模拟与现实世界轨迹之间的状态预测误差。为了进一步提高收集数据的信息量，我们引入了一种主动探索策略，通过优化探索策略的输入命令来最大化收集到的现实世界轨迹的Fisher信息。这种有针对性的探索导致了准确的识别和更好的任务泛化。实验表明，SPI-Active使学习策略的精确sim-to-real转移到现实世界，在各种运动任务中超越基线42-63%。

## 🔬 方法详解

**问题定义**：本论文旨在解决腿部机器人在Sim-to-real学习中的物理参数识别问题。现有方法如领域随机化依赖启发式，导致策略在实际应用中的性能不稳定，尤其是在接触丰富的环境中。

**核心思路**：论文提出的SPI-Active框架通过大规模并行采样和主动探索，针对性地识别物理参数，从而缩小模拟与现实之间的差距。通过优化输入命令，增强数据的有效性，提高识别精度。

**技术框架**：SPI-Active框架分为两个阶段：第一阶段是通过并行采样识别关键物理参数，第二阶段是通过主动探索优化输入命令，最大化收集数据的信息量。这一过程确保了对真实世界轨迹的准确建模。

**关键创新**：SPI-Active的创新在于结合了大规模采样与主动探索策略，突破了传统Sys-ID方法对可微分动力学和直接扭矩测量的依赖，使其适用于复杂的腿部机器人。

**关键设计**：在设计中，采用了优化的输入命令策略以最大化Fisher信息，并通过并行计算提高了参数识别的效率。损失函数设计上关注状态预测误差，确保模拟与现实轨迹的高一致性。

## 📊 实验亮点

实验结果表明，SPI-Active在多种运动任务中实现了42-63%的性能提升，显著优于基线方法，证明了其在Sim-to-real转移中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人控制、自动驾驶和人机交互等。通过提高Sim-to-real转移的精度，SPI-Active能够在复杂环境中实现更高效的机器人操作，推动智能机器人在现实世界中的应用。未来，该方法可能影响机器人学习和自主系统的设计与实现。

## 📄 摘要（原文）

> Sim-to-real discrepancies hinder learning-based policies from achieving high-precision tasks in the real world. While Domain Randomization (DR) is commonly used to bridge this gap, it often relies on heuristics and can lead to overly conservative policies with degrading performance when not properly tuned. System Identification (Sys-ID) offers a targeted approach, but standard techniques rely on differentiable dynamics and/or direct torque measurement, assumptions that rarely hold for contact-rich legged systems. To this end, we present SPI-Active (Sampling-based Parameter Identification with Active Exploration), a two-stage framework that estimates physical parameters of legged robots to minimize the sim-to-real gap. SPI-Active robustly identifies key physical parameters through massive parallel sampling, minimizing state prediction errors between simulated and real-world trajectories. To further improve the informativeness of collected data, we introduce an active exploration strategy that maximizes the Fisher Information of the collected real-world trajectories via optimizing the input commands of an exploration policy. This targeted exploration leads to accurate identification and better generalization across diverse tasks. Experiments demonstrate that SPI-Active enables precise sim-to-real transfer of learned policies to the real world, outperforming baselines by 42-63% in various locomotion tasks.

