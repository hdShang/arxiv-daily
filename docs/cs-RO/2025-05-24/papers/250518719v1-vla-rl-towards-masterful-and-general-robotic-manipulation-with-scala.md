---
layout: default
title: "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning"
---

# VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.18719" class="toolbar-btn" target="_blank">📄 arXiv: 2505.18719v1</a>
  <a href="https://arxiv.org/pdf/2505.18719.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.18719v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.18719v1', 'VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanxing Lu, Wenkai Guo, Chubin Zhang, Yuheng Zhou, Haonan Jiang, Zifeng Gao, Yansong Tang, Ziwei Wang

**分类**: cs.RO, cs.AI

**发布日期**: 2025-05-24

---

## 💡 一句话要点

**提出VLA-RL以解决机器人操作中的数据稀缺问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `强化学习` `机器人操作` `多模态学习` `稀疏奖励`

## 📋 核心要点

1. 现有的高容量VLA模型在离线数据利用上存在局限，导致在分布外场景中执行失败。
2. VLA-RL通过在线强化学习改进预训练模型，采用轨迹级RL训练方法，建模机器人操作为多模态对话。
3. VLA-RL在LIBERO数据集上超越了最强基线4.5%，并与商业模型性能相当，展示了测试时优化的潜力。

## 📝 摘要（中文）

近年来，高容量的视觉-语言-动作（VLA）模型在模仿人类示范的机器人操作任务中表现出色。然而，利用离线数据时，由于状态访问有限，可能在分布外场景中导致执行失败。为了解决这一问题，本文提出了VLA-RL，一个利用在线强化学习（RL）来改进预训练自回归VLA的算法框架。通过将机器人操作轨迹建模为多模态多轮对话，论文引入了轨迹级RL的训练方法，并通过伪奖励标签对视觉-语言模型进行微调，以应对稀疏奖励的挑战。实验结果表明，VLA-RL在40个复杂的机器人操作任务中超越了最强的微调基线，并与先进的商业模型相匹配。

## 🔬 方法详解

**问题定义**：本文旨在解决现有VLA模型在离线数据利用时的局限性，特别是在分布外场景中可能导致的执行失败问题。现有方法在状态访问上有限，无法有效应对复杂的机器人操作任务。

**核心思路**：VLA-RL的核心思路是通过在线强化学习来增强预训练的VLA模型，特别是在测试阶段通过探索性方法来改进模型性能。将机器人操作轨迹视为多模态多轮对话，有助于更好地理解和生成操作序列。

**技术框架**：VLA-RL的整体架构包括轨迹级RL训练、伪奖励模型微调以及多项实现优化策略。主要模块包括预训练的视觉-语言模型、奖励模型和在线强化学习模块。

**关键创新**：VLA-RL的主要创新在于将机器人操作轨迹建模为对话形式，并通过伪奖励标签来解决稀疏奖励问题。这一方法与传统的单一任务学习方法有本质区别，能够更好地适应复杂的操作环境。

**关键设计**：在设计上，VLA-RL采用了课程选择策略、GPU平衡的向量化环境、批量解码和评论员预热等技术细节，以提高训练的稳定性和效率。

## 📊 实验亮点

在LIBERO数据集上，VLA-RL使OpenVLA-7B在40个复杂的机器人操作任务中超越了最强的微调基线4.5%，并与先进的商业模型如$π_0$-FAST的性能相当，显示出其在实际应用中的强大能力。

## 🎯 应用场景

VLA-RL的研究成果在机器人操作领域具有广泛的应用潜力，特别是在需要高精度和灵活性的任务中，如工业自动化、服务机器人和家庭助理等。通过提高模型在复杂环境中的适应能力，未来可推动机器人技术的进一步发展与普及。

## 📄 摘要（原文）

> Recent high-capacity vision-language-action (VLA) models have demonstrated impressive performance on a range of robotic manipulation tasks by imitating human demonstrations. However, exploiting offline data with limited visited states will cause execution failure in out-of-distribution scenarios. Intuitively, an exploration-based method that improves on online collected data at test time could address this limitation. We present VLA-RL, an algorithmic and systematic framework that leverages online reinforcement learning (RL) to improve pretrained auto-regressive VLAs in downstream tasks. Within a unified perspective, we first introduce a trajectory-level RL formulation for auto-regressive VLA training, which models general robotic manipulation trajectory as multi-modal multi-turn conversation. To address the challenge of sparse rewards, we fine-tune a pretrained vision-language model as a robotic process reward model, which is trained on pseudo reward labels annotated on automatically extracted task segments. To scale up, we identify several implementation findings that improve the stability and efficiency including curriculum selection strategy, GPU-balanced vectorized environments, batch decoding, and critic warmup. VLA-RL enables OpenVLA-7B to surpass the strongest finetuned baseline by 4.5% on 40 challenging robotic manipulation tasks in LIBERO, and even matches the performance of advanced commercial models such as $π_0$-FAST. Notably, we observe that VLA-RL benefits from increased test-time optimization, indicating an early spark of inference scaling laws in robotics.

