---
layout: default
title: "FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency"
---

# FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08822" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08822v1</a>
  <a href="https://arxiv.org/pdf/2506.08822.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08822v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08822v1', 'FreqPolicy: Efficient Flow-based Visuomotor Policy via Frequency Consistency')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yifei Su, Ning Liu, Dong Chen, Zhen Zhao, Kun Wu, Meng Li, Zhiyuan Xu, Zhengping Che, Jian Tang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-06-10

---

## 💡 一句话要点

**提出FreqPolicy以解决流式视觉运动策略的高推理成本问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉运动策略` `生成建模` `频率一致性` `机器人操作` `时间序列生成` `自适应损失` `多模态交互`

## 📋 核心要点

1. 现有的生成建模方法在多步采样中存在高推理成本，限制了其在实时机器人操作中的应用。
2. FreqPolicy通过施加频率一致性约束来捕捉时间结构，支持高效的一步动作生成，解决了时间依赖性问题。
3. 在53个任务的实验中，FreqPolicy表现优越，并在Libero的40个任务中实现了加速而不降低性能。

## 📝 摘要（中文）

基于生成建模的视觉运动策略因其能够建模多模态动作分布而被广泛应用于机器人操作。然而，多步采样的高推理成本限制了其在实时机器人系统中的适用性。为了解决这一问题，本文提出FreqPolicy，通过施加频率一致性约束来有效利用机器人操作中的时间信息，从而支持高效且高质量的一步动作生成。实验结果表明，FreqPolicy在53个任务上优于现有的一步动作生成器，并在真实机器人场景中实现了93.5Hz的推理频率，展示了其效率和有效性。

## 🔬 方法详解

**问题定义**：本文旨在解决基于生成建模的视觉运动策略在多步采样中面临的高推理成本问题。现有方法多依赖于图像生成中的加速技术，但未能有效处理机器人操作中的时间序列动作生成的连续性和时间一致性。

**核心思路**：FreqPolicy的核心思路是施加频率一致性约束，使得流式视觉运动策略能够有效捕捉时间结构，从而实现高效的一步动作生成。通过在频域对动作特征进行一致性约束，促进了一步动作生成向目标分布的收敛。

**技术框架**：FreqPolicy的整体架构包括频率一致性约束模块和自适应一致性损失设计。频率一致性约束确保不同时间步的动作特征在频域上的对齐，而自适应一致性损失则捕捉机器人操作任务中固有的结构性时间变化。

**关键创新**：本文的关键创新在于引入频率一致性约束，强调了时间序列动作生成的连续性和一致性，这与传统图像生成方法的独立样本生成有本质区别。

**关键设计**：在损失函数设计上，采用自适应一致性损失来处理结构性时间变化，同时在网络结构中引入频率域特征对齐机制，以提高生成效率和质量。具体参数设置和网络结构细节将在代码中公开。

## 📊 实验亮点

在53个任务的实验中，FreqPolicy显著优于现有的一步动作生成器，展示了其在效率和效果上的优势。同时，在Libero的40个任务中实现了加速而不降低性能，推理频率达到93.5Hz，证明了其在真实场景中的有效性。

## 🎯 应用场景

FreqPolicy的研究成果在机器人操作、自动化生产线、智能家居等领域具有广泛的应用潜力。通过提高动作生成的效率和质量，该方法能够支持实时决策和控制，推动智能机器人在复杂环境中的应用。此外，结合视觉-语言-动作模型，FreqPolicy可在多模态交互中发挥重要作用，提升人机协作的智能化水平。

## 📄 摘要（原文）

> Generative modeling-based visuomotor policies have been widely adopted in robotic manipulation attributed to their ability to model multimodal action distributions. However, the high inference cost of multi-step sampling limits their applicability in real-time robotic systems. To address this issue, existing approaches accelerate the sampling process in generative modeling-based visuomotor policies by adapting acceleration techniques originally developed for image generation. Despite this progress, a major distinction remains: image generation typically involves producing independent samples without temporal dependencies, whereas robotic manipulation involves generating time-series action trajectories that require continuity and temporal coherence. To effectively exploit temporal information in robotic manipulation, we propose FreqPolicy, a novel approach that first imposes frequency consistency constraints on flow-based visuomotor policies. Our work enables the action model to capture temporal structure effectively while supporting efficient, high-quality one-step action generation. We introduce a frequency consistency constraint that enforces alignment of frequency-domain action features across different timesteps along the flow, thereby promoting convergence of one-step action generation toward the target distribution. In addition, we design an adaptive consistency loss to capture structural temporal variations inherent in robotic manipulation tasks. We assess FreqPolicy on 53 tasks across 3 simulation benchmarks, proving its superiority over existing one-step action generators. We further integrate FreqPolicy into the vision-language-action (VLA) model and achieve acceleration without performance degradation on the 40 tasks of Libero. Besides, we show efficiency and effectiveness in real-world robotic scenarios with an inference frequency 93.5Hz. The code will be publicly available.

