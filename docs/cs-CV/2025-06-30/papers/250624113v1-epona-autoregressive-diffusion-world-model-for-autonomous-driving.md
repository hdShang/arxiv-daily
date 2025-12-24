---
layout: default
title: "Epona: Autoregressive Diffusion World Model for Autonomous Driving"
---

# Epona: Autoregressive Diffusion World Model for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.24113" class="toolbar-btn" target="_blank">📄 arXiv: 2506.24113v1</a>
  <a href="https://arxiv.org/pdf/2506.24113.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.24113v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.24113v1', 'Epona: Autoregressive Diffusion World Model for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Zhang, Zhenyu Tang, Xiaotao Hu, Xingang Pan, Xiaoyang Guo, Yuan Liu, Jingwei Huang, Li Yuan, Qian Zhang, Xiao-Xiao Long, Xun Cao, Wei Yin

**分类**: cs.CV

**发布日期**: 2025-06-30

**备注**: ICCV2025, Project Page: https://kevin-thu.github.io/Epona/

**🔗 代码/项目**: [GITHUB](https://github.com/Kevin-thu/Epona/)

---

## 💡 一句话要点

**提出Epona以解决自主驾驶中的长时序预测问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `自主驾驶` `扩散模型` `时空建模` `轨迹规划` `长时序预测` `高分辨率生成` `运动规划`

## 📋 核心要点

1. 现有视频扩散模型在长时序预测和轨迹规划整合方面存在局限，难以满足自主驾驶的需求。
2. Epona通过解耦时空因子化和模块化轨迹与视频预测，提供了一种新的自回归扩散世界模型，能够进行局部时空分布建模。
3. 实验结果显示，Epona在FVD指标上提升了7.4%，并且在预测时长上显著优于以往方法，同时作为运动规划器表现出色。

## 📝 摘要（中文）

扩散模型在视频生成中展现了卓越的视觉质量，使其在自主驾驶世界建模中具有潜力。然而，现有基于视频扩散的世界模型在灵活长度、长时间预测及轨迹规划整合方面存在困难。本文提出Epona，一种自回归扩散世界模型，通过解耦时空因子化和模块化轨迹与视频预测，实现了局部时空分布建模。该架构支持高分辨率、长时长生成，并引入新颖的前向训练策略以解决自回归循环中的误差累积问题。实验结果表明，Epona在FVD指标上提升了7.4%，并在预测时长上超越了先前工作，且作为实时运动规划器在NAVSIM基准测试中表现优异。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视频扩散模型在自主驾驶中的长时序预测和轨迹规划整合不足的问题。传统模型依赖于固定长度帧序列的全局联合分布建模，导致灵活性不足。

**核心思路**：Epona的核心思路是通过解耦时空因子化，将时间动态建模与细粒度未来世界生成分开，同时采用模块化的轨迹与视频预测，形成端到端的框架，提升模型的灵活性和准确性。

**技术框架**：Epona的整体架构包括两个主要模块：时空因子化模块和轨迹预测模块。时空因子化模块负责建模时间动态，而轨迹预测模块则与视觉建模无缝集成，支持高分辨率和长时长的生成。

**关键创新**：Epona的主要创新在于引入了局部时空分布建模和新颖的前向训练策略，解决了自回归循环中的误差累积问题。这一设计与传统方法的全局建模方式形成鲜明对比。

**关键设计**：在参数设置上，Epona采用了特定的损失函数以优化时空因子化效果，并设计了适应性网络结构以支持高分辨率生成，确保模型在长时序预测中的稳定性与准确性。

## 📊 实验亮点

Epona在实验中实现了7.4%的FVD提升，且预测时长显著超过了以往模型，展现了其在长时序生成中的优势。此外，作为实时运动规划器，Epona在NAVSIM基准测试中超越了多个强大的端到端规划器，验证了其实际应用价值。

## 🎯 应用场景

Epona的研究成果在自主驾驶领域具有广泛的应用潜力，能够为自动驾驶系统提供高效的世界建模和实时运动规划能力。这将有助于提升自动驾驶车辆在复杂环境中的决策能力和安全性，推动智能交通系统的发展。

## 📄 摘要（原文）

> Diffusion models have demonstrated exceptional visual quality in video generation, making them promising for autonomous driving world modeling. However, existing video diffusion-based world models struggle with flexible-length, long-horizon predictions and integrating trajectory planning. This is because conventional video diffusion models rely on global joint distribution modeling of fixed-length frame sequences rather than sequentially constructing localized distributions at each timestep. In this work, we propose Epona, an autoregressive diffusion world model that enables localized spatiotemporal distribution modeling through two key innovations: 1) Decoupled spatiotemporal factorization that separates temporal dynamics modeling from fine-grained future world generation, and 2) Modular trajectory and video prediction that seamlessly integrate motion planning with visual modeling in an end-to-end framework. Our architecture enables high-resolution, long-duration generation while introducing a novel chain-of-forward training strategy to address error accumulation in autoregressive loops. Experimental results demonstrate state-of-the-art performance with 7.4\% FVD improvement and minutes longer prediction duration compared to prior works. The learned world model further serves as a real-time motion planner, outperforming strong end-to-end planners on NAVSIM benchmarks. Code will be publicly available at \href{https://github.com/Kevin-thu/Epona/}{https://github.com/Kevin-thu/Epona/}.

