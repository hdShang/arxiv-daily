---
layout: default
title: "TreeRPO: Tree Relative Policy Optimization"
---

# TreeRPO: Tree Relative Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05183" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05183v2</a>
  <a href="https://arxiv.org/pdf/2506.05183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05183v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05183v2', 'TreeRPO: Tree Relative Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhicheng Yang, Zhijiang Guo, Yinya Huang, Xiaodan Liang, Yiwei Wang, Jing Tang

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-05 (更新: 2025-09-27)

**备注**: 13pages, 6 figures

**🔗 代码/项目**: [GITHUB](https://github.com/yangzhch6/TreeRPO)

---

## 💡 一句话要点

**提出TreeRPO以优化推理过程中的奖励信号**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `奖励优化` `推理过程` `树采样` `大型语言模型` `自然语言处理` `模型训练`

## 📋 核心要点

1. 现有方法在推理过程中的奖励信号指导不足，难以优化中间步骤，影响模型性能。
2. 本文提出TreeRPO，通过树采样直接估计推理步骤的奖励，避免了单独步骤奖励模型的局限性。
3. 实验表明，TreeRPO在Qwen-2.5-Math的测试基准上显著提高了准确率，并减少了响应长度，展现了优越的性能。

## 📝 摘要（中文）

大型语言模型（LLMs）通过可验证奖励的强化学习方法展现了卓越的推理能力。然而，现有方法在全轨迹层面定义的奖励对优化推理过程中的中间步骤指导不足。为此，本文提出了TreeRPO，一种通过树采样估计各推理步骤奖励数学期望的新方法。与依赖单独步骤奖励模型的先前方法不同，TreeRPO直接通过采样过程估计这些奖励。基于GRPO的组相对奖励训练机制，TreeRPO创新性地根据树采样生成的步骤级组计算奖励，显著增强了学习过程和LLMs的整体性能。实验结果表明，TreeRPO显著提高了Qwen-2.5-Math在测试基准上的平均Pass@1准确率，从19.0%提升至35.5%。此外，TreeRPO在性能上比GRPO提升了2.9%，同时平均响应长度减少了18.1%，展示了其有效性和高效性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有强化学习方法在推理过程中的奖励信号不足的问题，特别是在中间步骤的优化指导上存在的挑战。现有方法往往依赖全轨迹奖励，导致对推理过程的细粒度优化能力不足。

**核心思路**：TreeRPO的核心思路是通过树采样直接估计各推理步骤的奖励期望，而不是依赖于单独的步骤奖励模型。这种设计使得模型能够在推理过程中获得更为细致和密集的奖励信号，从而提升学习效果。

**技术框架**：TreeRPO的整体架构包括树采样模块和奖励计算模块。首先，通过树采样生成推理过程的不同路径，然后在这些路径上计算步骤级的奖励，最后将这些奖励用于模型的训练。

**关键创新**：TreeRPO的主要创新在于其通过树采样生成的步骤级组来计算奖励，这一方法与现有的依赖全轨迹奖励的方式有本质区别，能够提供更为细致的反馈信号。

**关键设计**：在设计上，TreeRPO采用了基于组相对奖励的训练机制，关键参数设置和损失函数的设计旨在最大化奖励信号的有效性和密度，确保模型在学习过程中能够获得充分的指导。具体的网络结构和参数设置将在代码中详细说明。

## 📊 实验亮点

实验结果显示，TreeRPO显著提高了Qwen-2.5-Math在测试基准上的平均Pass@1准确率，从19.0%提升至35.5%。此外，TreeRPO在性能上比GRPO提升了2.9%，同时平均响应长度减少了18.1%，展示了其在有效性和高效性上的优势。

## 🎯 应用场景

TreeRPO的研究成果在多个领域具有潜在应用价值，尤其是在需要复杂推理能力的任务中，如自然语言处理、智能问答系统和自动化决策支持等。通过优化推理过程中的奖励信号，TreeRPO能够提升模型的推理准确性和效率，推动相关技术的发展。

## 📄 摘要（原文）

> Large Language Models (LLMs) have shown remarkable reasoning capabilities through Reinforcement Learning with Verifiable Rewards (RLVR) methods. However, a key limitation of existing approaches is that rewards defined at the full trajectory level provide insufficient guidance for optimizing the intermediate steps of a reasoning process. To address this, we introduce \textbf{\name}, a novel method that estimates the mathematical expectations of rewards at various reasoning steps using tree sampling. Unlike prior methods that rely on a separate step reward model, \name directly estimates these rewards through this sampling process. Building on the group-relative reward training mechanism of GRPO, \name innovatively computes rewards based on step-level groups generated during tree sampling. This advancement allows \name to produce fine-grained and dense reward signals, significantly enhancing the learning process and overall performance of LLMs. Experimental results demonstrate that our \name algorithm substantially improves the average Pass@1 accuracy of Qwen-2.5-Math on test benchmarks, increasing it from 19.0\% to 35.5\%. Furthermore, \name significantly outperforms GRPO by 2.9\% in performance while simultaneously reducing the average response length by 18.1\%, showcasing its effectiveness and efficiency. Our code will be available at \href{https://github.com/yangzhch6/TreeRPO}{https://github.com/yangzhch6/TreeRPO}.

