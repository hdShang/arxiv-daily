---
layout: default
title: "ReDit: Reward Dithering for Improved LLM Policy Optimization"
---

# ReDit: Reward Dithering for Improved LLM Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.18631" class="toolbar-btn" target="_blank">📄 arXiv: 2506.18631v4</a>
  <a href="https://arxiv.org/pdf/2506.18631.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.18631v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.18631v4', 'ReDit: Reward Dithering for Improved LLM Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chenxing Wei, Jiarui Yu, Ying Tiffany He, Hande Dong, Yao Shu, Fei Yu

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-06-23 (更新: 2025-10-24)

**备注**: 34 pages, 19 figures

---

## 💡 一句话要点

**提出ReDit以解决LLM优化中的离散奖励问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `奖励机制` `优化算法` `深度学习` `大型语言模型` `随机噪声` `梯度更新` `策略探索`

## 📋 核心要点

1. 现有的离散奖励系统可能导致梯度异常和优化不稳定，从而影响大型语言模型的训练效率。
2. ReDit方法通过在离散奖励信号中添加随机噪声，提供持续的探索性梯度，促进更平滑的优化过程。
3. 实验表明，ReDit在多个任务上仅需约10%的训练步骤即可达到与传统GRPO相当的性能，并在相似训练时间内实现4%的性能提升。

## 📝 摘要（中文）

DeepSeek-R1通过基于规则的奖励系统成功增强了大型语言模型（LLM）的推理能力。尽管该奖励系统有效缓解了奖励黑客问题，但离散奖励可能导致梯度异常、不稳定的优化和缓慢的收敛。为了解决这一问题，本文提出了ReDit（奖励抖动）方法，通过添加简单的随机噪声来抖动离散奖励信号。这样可以在学习过程中持续提供探索性梯度，促进更平滑的梯度更新并加速收敛。实验结果表明，ReDit在多个任务中表现出色，平均仅需约10%的训练步骤便能达到与传统GRPO相当的性能，并在相似训练时间内实现4%的性能提升。可视化结果证实了ReDit在缓解梯度问题方面的显著效果。

## 🔬 方法详解

**问题定义**：本文旨在解决现有离散奖励系统导致的梯度异常和优化不稳定问题，这些问题会影响大型语言模型（LLM）的训练效率和效果。

**核心思路**：ReDit方法通过在离散奖励信号中引入随机噪声，旨在提供持续的探索性梯度，从而促进更平滑的梯度更新和加速收敛。这样的设计使得模型能够在平坦的奖励区域中引入随机性，鼓励探索新策略，避免陷入局部最优解。

**技术框架**：ReDit的整体架构包括奖励信号的抖动模块和梯度更新模块。首先，通过添加随机噪声对离散奖励进行抖动，然后利用这些抖动后的奖励信号进行模型的梯度更新。

**关键创新**：ReDit的主要创新在于通过简单的随机噪声抖动离散奖励信号，显著改善了梯度更新的平滑性和收敛速度。这与传统的离散奖励方法形成了鲜明对比，后者往往导致优化过程中的不稳定性。

**关键设计**：在ReDit中，随机噪声的幅度和分布是关键设计参数，影响抖动效果的强度。此外，损失函数的设计也考虑了抖动后的奖励信号，以确保模型能够有效利用这些信息进行学习。

## 📊 实验亮点

实验结果显示，ReDit在多个任务上表现优异，平均仅需约10%的训练步骤便能达到与传统GRPO相当的性能。此外，在相似的训练时间内，ReDit还实现了4%的性能提升，显著缓解了梯度问题。

## 🎯 应用场景

ReDit方法具有广泛的应用潜力，尤其在需要优化大型语言模型的任务中，如对话系统、文本生成和智能问答等领域。通过提高训练效率和模型性能，ReDit能够为实际应用提供更快速和高效的解决方案，推动相关技术的发展。

## 📄 摘要（原文）

> DeepSeek-R1 has successfully enhanced Large Language Model (LLM) reasoning capabilities through its rule-based reward system. While it's a ''perfect'' reward system that effectively mitigates reward hacking, such reward functions are often discrete. Our experimental observations suggest that discrete rewards can lead to gradient anomaly, unstable optimization, and slow convergence. To address this issue, we propose ReDit (Reward Dithering), a method that dithers the discrete reward signal by adding simple random noise. With this perturbed reward, exploratory gradients are continuously provided throughout the learning process, enabling smoother gradient updates and accelerating convergence. The injected noise also introduces stochasticity into flat reward regions, encouraging the model to explore novel policies and escape local optima. Experiments across diverse tasks demonstrate the effectiveness and efficiency of ReDit. On average, ReDit achieves performance comparable to vanilla GRPO with only approximately 10% the training steps, and furthermore, still exhibits a 4% performance improvement over vanilla GRPO when trained for a similar duration. Visualizations confirm significant mitigation of gradient issues with ReDit. Moreover, theoretical analyses are provided to further validate these advantages.

