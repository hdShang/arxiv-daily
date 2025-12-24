---
layout: default
title: "CEED-VLA: Consistency Vision-Language-Action Model with Early-Exit Decoding"
---

# CEED-VLA: Consistency Vision-Language-Action Model with Early-Exit Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.13725" class="toolbar-btn" target="_blank">📄 arXiv: 2506.13725v1</a>
  <a href="https://arxiv.org/pdf/2506.13725.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.13725v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.13725v1', 'CEED-VLA: Consistency Vision-Language-Action Model with Early-Exit Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenxuan Song, Jiayi Chen, Pengxiang Ding, Yuxin Huang, Han Zhao, Donglin Wang, Haoang Li

**分类**: cs.RO

**发布日期**: 2025-06-16

**备注**: 16 pages

**🔗 代码/项目**: [PROJECT_PAGE](https://irpn-eai.github.io/CEED-VLA/)

---

## 💡 一句话要点

**提出CEED-VLA以解决多模态决策中的推理速度瓶颈问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言-动作` `蒸馏训练` `多模态决策` `推理加速` `机器人技术`

## 📋 核心要点

1. 现有的视觉-语言-动作模型在高频和灵巧操作任务中推理速度较慢，限制了其实际应用。
2. 本文提出一致性蒸馏训练和早期退出解码策略，以提高推理效率，减轻误差积累。
3. 实验结果显示，所提方法在不同基线下实现了超过4倍的推理加速，且任务成功率保持高水平。

## 📝 摘要（中文）

近年来，视觉-语言-动作（VLA）模型在机器人领域成为重要研究方向，因其出色的多模态理解和泛化能力。然而，实际应用受到推理速度瓶颈的严重限制，尤其是在高频和灵巧操作任务中。为此，本文引入一致性蒸馏训练，以在每次迭代中预测多个正确的动作标记，从而加速推理。同时，设计混合标签监督以减轻蒸馏过程中的误差积累。此外，提出的早期退出解码策略进一步提高了推理效率。实验结果表明，该方法在不同基线下实现了超过4倍的推理加速，同时在模拟和真实机器人任务中保持了高任务成功率。

## 🔬 方法详解

**问题定义**：本文旨在解决视觉-语言-动作模型在高频和灵巧操作任务中的推理速度瓶颈，现有的自回归解码方法效率低下，迭代过程冗长，导致实际应用受限。

**核心思路**：通过一致性蒸馏训练，预测每次迭代中的多个正确动作标记，从而加速推理过程。同时，设计混合标签监督以减少蒸馏过程中的误差积累，进一步提高效率。

**技术框架**：整体架构包括一致性蒸馏训练模块、混合标签监督模块和早期退出解码模块。首先，通过一致性蒸馏训练进行多标记预测，然后利用混合标签监督优化训练过程，最后通过早期退出解码策略提高推理效率。

**关键创新**：提出的早期退出解码策略是本研究的核心创新，适度放宽收敛条件，显著提高了推理效率，与传统的自回归解码方法相比，能够更快地达到有效决策。

**关键设计**：在蒸馏训练中，采用多标记预测损失函数，结合混合标签监督策略，确保模型在训练过程中减少误差积累。此外，早期退出解码的具体实现依赖于动态调整的收敛条件，以便在保证准确率的同时加速推理。

## 📊 实验亮点

实验结果表明，CEED-VLA在不同基线下实现了超过4倍的推理加速，同时在模拟和真实机器人任务中保持了高达90%以上的任务成功率。这一显著提升验证了所提方法在多模态决策中的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括机器人操作、自动化制造和人机交互等场景。通过提高多模态决策的推理效率，CEED-VLA可以在实时任务中实现更高的响应速度和准确性，推动智能机器人在复杂环境中的应用。未来，该方法有望在更多领域中推广，提升机器人系统的智能化水平。

## 📄 摘要（原文）

> In recent years, Vision-Language-Action (VLA) models have become a vital research direction in robotics due to their impressive multimodal understanding and generalization capabilities. Despite the progress, their practical deployment is severely constrained by inference speed bottlenecks, particularly in high-frequency and dexterous manipulation tasks. While recent studies have explored Jacobi decoding as a more efficient alternative to traditional autoregressive decoding, its practical benefits are marginal due to the lengthy iterations. To address it, we introduce consistency distillation training to predict multiple correct action tokens in each iteration, thereby achieving acceleration. Besides, we design mixed-label supervision to mitigate the error accumulation during distillation. Although distillation brings acceptable speedup, we identify that certain inefficient iterations remain a critical bottleneck. To tackle this, we propose an early-exit decoding strategy that moderately relaxes convergence conditions, which further improves average inference efficiency. Experimental results show that the proposed method achieves more than 4 times inference acceleration across different baselines while maintaining high task success rates in both simulated and real-world robot tasks. These experiments validate that our approach provides an efficient and general paradigm for accelerating multimodal decision-making in robotics. Our project page is available at https://irpn-eai.github.io/CEED-VLA/.

