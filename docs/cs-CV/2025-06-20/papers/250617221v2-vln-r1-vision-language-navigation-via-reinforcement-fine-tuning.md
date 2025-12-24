---
layout: default
title: "VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning"
---

# VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17221" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17221v2</a>
  <a href="https://arxiv.org/pdf/2506.17221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17221v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17221v2', 'VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhangyang Qi, Zhixiong Zhang, Yizhou Yu, Jiaqi Wang, Hengshuang Zhao

**分类**: cs.CV

**发布日期**: 2025-06-20 (更新: 2025-06-25)

**备注**: project page: vlnr1.github.io

---

## 💡 一句话要点

**提出VLN-R1以解决视觉-语言导航中的路径规划问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言导航` `强化学习` `大型视觉-语言模型` `路径规划` `长短期记忆采样` `具身人工智能` `数据高效训练`

## 📋 核心要点

1. 现有的语言模型导航系统仅在离散拓扑图上操作，限制了路径规划的灵活性和实时性。
2. VLN-R1框架通过利用大型视觉-语言模型，直接将视频流转换为连续导航动作，采用两阶段训练策略。
3. 实验结果显示，VLN-R1在VLN-CE基准上表现优异，验证了其在具身导航中的有效性和创新性。

## 📝 摘要（中文）

视觉-语言导航（VLN）是具身人工智能中的核心挑战，要求智能体使用自然语言指令在现实环境中导航。目前基于语言模型的导航系统仅在离散拓扑图上操作，限制了路径规划的灵活性。本文提出了VLN-R1，一个端到端框架，利用大型视觉-语言模型（LVLM）直接将自我中心的视频流转换为连续导航动作，并采用受DeepSeek-R1启发的GRPO训练方法。为了有效训练，我们首先使用3D模拟器Habitat构建了VLN-Ego数据集，并提出了长短期记忆采样方法，以平衡历史和当前观察。实验结果表明，VLN-R1在VLN-CE基准上表现出色，证明LVLM可以驱动具身导航并通过数据高效、奖励驱动的后训练增强任务特定推理。

## 🔬 方法详解

**问题定义**：本文旨在解决现有视觉-语言导航系统在离散拓扑图上操作的局限性，导致路径规划不够灵活和实时。

**核心思路**：VLN-R1通过直接将自我中心的视频流转换为连续导航动作，采用大型视觉-语言模型（LVLM）进行训练，以实现更自然的导航方式。

**技术框架**：VLN-R1的整体架构包括两个主要阶段：监督微调（SFT）和强化微调（RFT）。SFT阶段对模型的动作序列文本预测进行对齐，而RFT阶段则引入时间衰减奖励机制以优化多步未来动作的权重。

**关键创新**：最重要的创新在于引入了长短期记忆采样方法，以平衡历史和当前观察，从而提高模型的训练效率和导航精度。

**关键设计**：在训练过程中，采用了GRPO训练方法，并设计了时间衰减奖励机制，以增强模型对未来动作的预测能力，确保模型在复杂环境中的表现。通过这些设计，VLN-R1能够有效地利用历史信息和当前状态进行决策。

## 📊 实验亮点

实验结果表明，VLN-R1在VLN-CE基准上取得了显著的性能提升，具体表现为在多项任务中超越了现有基线，验证了其在复杂导航任务中的有效性和创新性。

## 🎯 应用场景

该研究的潜在应用领域包括智能机器人、自动驾驶、虚拟现实等场景，能够提升智能体在复杂环境中的导航能力。随着技术的进步，VLN-R1有望在具身人工智能领域产生深远影响，推动人机交互的自然性和智能化水平。

## 📄 摘要（原文）

> Vision-Language Navigation (VLN) is a core challenge in embodied AI, requiring agents to navigate real-world environments using natural language instructions. Current language model-based navigation systems operate on discrete topological graphs, limiting path planning to predefined node connections. We propose VLN-R1, an end-to-end framework that leverages Large Vision-Language Models (LVLM) to directly translate egocentric video streams into continuous navigation actions, adopting GRPO-based training inspired by DeepSeek-R1. To enable effective training, we first construct the VLN-Ego dataset using a 3D simulator, Habitat, and propose Long-Short Memory Sampling to balance historical and current observations. While large language models can supervise complete textual instructions, they lack fine-grained action-level control. Our framework employs a two-stage training approach: a) Supervised fine-tuning (SFT) to align the model's action sequence text predictions with expert demonstrations, followed by b) Reinforcement fine-tuning (RFT) enhanced with a Time-Decayed Reward (TDR) mechanism that strategically weights multi-step future actions. Experimental results show VLN-R1 achieves strong performance on VLN-CE benchmark. VLN-R1 proves LVLMs can drive embodied navigation and enhance task-specific reasoning through data-efficient, reward-driven post-training.

