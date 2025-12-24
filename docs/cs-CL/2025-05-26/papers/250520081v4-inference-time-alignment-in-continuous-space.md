---
layout: default
title: Inference-time Alignment in Continuous Space
---

# Inference-time Alignment in Continuous Space

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20081" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20081v4</a>
  <a href="https://arxiv.org/pdf/2505.20081.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20081v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20081v4', 'Inference-time Alignment in Continuous Space')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yige Yuan, Teng Xiao, Li Yunfan, Bingbing Xu, Shuchang Tao, Yunqi Qiu, Huawei Shen, Xueqi Cheng

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-10-24)

**备注**: Accepted at NeurIPS 2025

**🔗 代码/项目**: [GITHUB](https://github.com/yuanyige/sea)

---

## 💡 一句话要点

**提出简单能量适应算法以解决推理时对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推理对齐` `大型语言模型` `人类反馈` `能量适应` `梯度采样` `自然语言处理` `算法优化`

## 📋 核心要点

1. 现有方法在推理时对齐大型语言模型与人类反馈时，面临基础策略弱或候选集小导致的有效性不足问题。
2. 本文提出的简单能量适应（SEA）算法，通过在连续潜在空间中进行梯度采样，直接调整基础策略的响应，简化了对齐过程。
3. SEA在多个基准测试中表现优异，AdvBench上相较于第二优基线提升了77.51%，MATH上提升了16.36%。

## 📝 摘要（中文）

在推理时将大型语言模型与人类反馈对齐的研究逐渐受到关注，现有方法依赖于从基础策略生成多个响应进行搜索，但在基础策略较弱或候选集较小时，探索有效候选的能力有限。为了解决这一问题，本文提出了简单能量适应（SEA）算法，该算法通过在连续潜在空间中进行基于梯度的采样，直接将基础策略的原始响应调整为最优响应，从而实现简单有效的对齐。实验结果表明，SEA在AdvBench上相较于第二优基线提升了77.51%，在MATH上提升了16.36%。

## 🔬 方法详解

**问题定义**：本文旨在解决推理时大型语言模型与人类反馈对齐的有效性问题。现有方法依赖于离散响应空间的搜索，难以在基础策略较弱或候选集较小时找到有效候选。

**核心思路**：提出简单能量适应（SEA）算法，利用梯度采样在连续潜在空间中直接调整基础策略的响应，避免了离散空间中昂贵的搜索过程。

**技术框架**：SEA算法将推理过程视为在定义为最优策略的连续空间中的能量函数上的迭代优化过程，主要包括响应调整和能量计算两个模块。

**关键创新**：SEA的核心创新在于通过在连续空间中进行优化，简化了对齐过程，与现有方法相比，能够更有效地探索响应候选。

**关键设计**：SEA算法的设计包括选择合适的能量函数和梯度计算方法，以确保在调整过程中保持响应的有效性和多样性。

## 📊 实验亮点

SEA算法在多个基准测试中表现出色，特别是在AdvBench上相较于第二优基线提升了77.51%，在MATH上提升了16.36%。这些结果表明，SEA在推理时对齐任务中具有显著的优势，能够有效提升模型的响应质量。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理中的对话系统、文本生成和人机交互等场景。通过提高语言模型的响应质量和对齐能力，SEA算法能够增强模型在实际应用中的表现，提升用户体验。未来，随着算法的进一步优化，可能会在更广泛的AI应用中发挥重要作用。

## 📄 摘要（原文）

> Aligning large language models with human feedback at inference time has received increasing attention due to its flexibility. Existing methods rely on generating multiple responses from the base policy for search using a reward model, which can be considered as searching in a discrete response space. However, these methods struggle to explore informative candidates when the base policy is weak or the candidate set is small, resulting in limited effectiveness. In this paper, to address this problem, we propose Simple Energy Adaptation ($\textbf{SEA}$), a simple yet effective algorithm for inference-time alignment. In contrast to expensive search over the discrete space, SEA directly adapts original responses from the base policy toward the optimal one via gradient-based sampling in continuous latent space. Specifically, SEA formulates inference as an iterative optimization procedure on an energy function over actions in the continuous space defined by the optimal policy, enabling simple and effective alignment. For instance, despite its simplicity, SEA outperforms the second-best baseline with a relative improvement of up to $ \textbf{77.51%}$ on AdvBench and $\textbf{16.36%}$ on MATH. Our code is publicly available at https://github.com/yuanyige/sea

