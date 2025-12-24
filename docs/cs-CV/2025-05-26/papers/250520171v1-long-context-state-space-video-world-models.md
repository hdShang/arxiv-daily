---
layout: default
title: Long-Context State-Space Video World Models
---

# Long-Context State-Space Video World Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20171" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20171v1</a>
  <a href="https://arxiv.org/pdf/2505.20171.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20171v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20171v1', 'Long-Context State-Space Video World Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ryan Po, Yotam Nitzan, Richard Zhang, Berlin Chen, Tri Dao, Eli Shechtman, Gordon Wetzstein, Xun Huang

**分类**: cs.CV

**发布日期**: 2025-05-26

**备注**: Project website: https://ryanpo.com/ssm_wm

---

## 💡 一句话要点

**提出长上下文状态空间视频世界模型以解决长时记忆问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长视频理解` `状态空间模型` `因果序列建模` `长期记忆` `视频扩散模型`

## 📋 核心要点

1. 现有视频扩散模型在长序列处理时面临高计算成本，导致长期记忆保持能力不足。
2. 提出利用状态空间模型（SSMs）来扩展时间记忆，采用块状SSM扫描方案与密集局部注意力结合。
3. 在Memory Maze和Minecraft数据集上进行实验，结果显示该方法在长距离记忆保持上超越基线，同时推理速度适合交互应用。

## 📝 摘要（中文）

视频扩散模型在基于动作的自回归帧预测中展现了世界建模的潜力，但在处理长序列时由于计算成本高而难以维持长期记忆。为此，本文提出了一种新颖的架构，利用状态空间模型（SSMs）在不牺牲计算效率的情况下扩展时间记忆。与以往将SSMs改造为非因果视觉任务的方法不同，我们的方法充分利用了SSMs在因果序列建模中的固有优势。我们的设计核心是块状SSM扫描方案，战略性地在空间一致性与扩展时间记忆之间进行权衡，并结合密集局部注意力以确保连续帧之间的连贯性。通过在Memory Maze和Minecraft数据集上的实验，我们的方法在保持长距离记忆的同时，展现了适合交互应用的实际推理速度。

## 🔬 方法详解

**问题定义**：本文旨在解决视频扩散模型在处理长序列时的长期记忆保持能力不足的问题。现有方法在计算成本高的情况下难以有效维持长时记忆，影响了模型的性能和应用。

**核心思路**：论文提出了一种基于状态空间模型（SSMs）的新架构，充分利用SSMs在因果序列建模中的优势，通过块状SSM扫描方案来扩展时间记忆，同时结合密集局部注意力以确保帧间连贯性。

**技术框架**：整体架构包括块状SSM扫描模块和密集局部注意力模块。块状SSM扫描模块负责处理时间序列数据，而密集局部注意力模块则确保连续帧之间的空间一致性。

**关键创新**：最重要的创新在于将SSMs应用于因果序列建模，充分发挥其在长期记忆保持方面的优势，与传统方法相比，显著提高了模型在长序列处理中的效率和效果。

**关键设计**：在设计中，采用了块状扫描策略以优化计算效率，并在网络结构中引入了密集局部注意力机制，以增强帧间的连贯性和一致性。

## 📊 实验亮点

实验结果表明，所提出的方法在Memory Maze和Minecraft数据集上显著超越了基线模型，尤其在长距离记忆保持方面表现出色，推理速度也保持在适合交互应用的范围内，展示了良好的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括游戏AI、机器人导航和视频分析等。通过提升模型的长期记忆能力，可以在复杂环境中实现更智能的决策和交互，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Video diffusion models have recently shown promise for world modeling through autoregressive frame prediction conditioned on actions. However, they struggle to maintain long-term memory due to the high computational cost associated with processing extended sequences in attention layers. To overcome this limitation, we propose a novel architecture leveraging state-space models (SSMs) to extend temporal memory without compromising computational efficiency. Unlike previous approaches that retrofit SSMs for non-causal vision tasks, our method fully exploits the inherent advantages of SSMs in causal sequence modeling. Central to our design is a block-wise SSM scanning scheme, which strategically trades off spatial consistency for extended temporal memory, combined with dense local attention to ensure coherence between consecutive frames. We evaluate the long-term memory capabilities of our model through spatial retrieval and reasoning tasks over extended horizons. Experiments on Memory Maze and Minecraft datasets demonstrate that our approach surpasses baselines in preserving long-range memory, while maintaining practical inference speeds suitable for interactive applications.

