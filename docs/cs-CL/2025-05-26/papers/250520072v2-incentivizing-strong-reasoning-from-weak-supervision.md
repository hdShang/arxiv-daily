---
layout: default
title: Incentivizing Strong Reasoning from Weak Supervision
---

# Incentivizing Strong Reasoning from Weak Supervision

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20072" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20072v2</a>
  <a href="https://arxiv.org/pdf/2505.20072.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20072v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20072v2', 'Incentivizing Strong Reasoning from Weak Supervision')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yige Yuan, Teng Xiao, Shuchang Tao, Xue Wang, Jinyang Gao, Bolin Ding, Bingbing Xu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-26 (更新: 2025-05-28)

**🔗 代码/项目**: [GITHUB](https://github.com/yuanyige/w2sr)

---

## 💡 一句话要点

**提出弱监督激励强推理以提升大语言模型推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `弱监督` `推理能力` `大语言模型` `强化学习` `模型蒸馏` `自然语言处理` `成本降低`

## 📋 核心要点

1. 现有方法通常依赖昂贵的高质量示范或强化学习，限制了推理能力的提升。
2. 本文提出通过显著较弱模型的监督来激励LLMs的推理能力，探索其有效性。
3. 实验表明，弱推理者的监督能显著提升强模型的推理表现，接近94%的RL收益，且成本低廉。

## 📝 摘要（中文）

大型语言模型（LLMs）在推理密集型任务中表现出色，但提升其推理能力通常依赖于昂贵的强化学习（RL）或高质量的监督微调（SFT）。本文研究了在没有高质量示范和强化学习的情况下，如何通过显著较弱模型的监督来激励LLMs的推理能力。研究表明，来自弱推理者的监督可以显著提高强模型的推理表现，恢复近94%的RL收益，且成本大幅降低。实验结果表明，弱推理者能够有效激励强学生模型的推理能力，广泛提升多种推理任务的表现。该研究提出的弱到强的范式为在推理时激励LLMs的强推理能力提供了一种有前景且可推广的替代方案。

## 🔬 方法详解

**问题定义**：本文旨在解决如何在没有高质量示范和强化学习的情况下，提升大型语言模型的推理能力。现有方法的痛点在于其高成本和对高质量数据的依赖。

**核心思路**：论文提出通过显著较弱的推理模型来提供监督，激励强模型的推理能力。这样的设计旨在降低成本，同时保持推理性能的提升。

**技术框架**：整体架构包括弱推理者和强学生模型两个主要模块。弱推理者提供低成本的监督信号，而强模型则通过学习这些信号来提升自身的推理能力。

**关键创新**：最重要的技术创新在于提出了弱到强的监督范式，显著降低了推理能力提升的成本，与传统的高质量示范和强化学习方法形成鲜明对比。

**关键设计**：在实验中，采用了特定的损失函数来优化强模型的推理能力，同时对弱推理者的选择和训练进行了精心设计，以确保其输出的监督信号能够有效激励强模型。

## 📊 实验亮点

实验结果显示，来自弱推理者的监督能够使强模型的推理表现显著提升，恢复近94%的强化学习收益，且在多种基准测试和模型架构中均表现出一致的性能提升，展示了该方法的有效性和广泛适用性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和自动推理等。通过降低推理能力提升的成本，研究成果能够使更多的企业和研究机构能够利用大型语言模型，推动相关技术的普及和发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated impressive performance on reasoning-intensive tasks, but enhancing their reasoning abilities typically relies on either reinforcement learning (RL) with verifiable signals or supervised fine-tuning (SFT) with high-quality long chain-of-thought (CoT) demonstrations, both of which are expensive. In this paper, we study a novel problem of incentivizing the reasoning capacity of LLMs without expensive high-quality demonstrations and reinforcement learning. We investigate whether the reasoning capabilities of LLMs can be effectively incentivized via supervision from significantly weaker models. We further analyze when and why such weak supervision succeeds in eliciting reasoning abilities in stronger models. Our findings show that supervision from significantly weaker reasoners can substantially improve student reasoning performance, recovering close to 94% of the gains of expensive RL at a fraction of the cost. Experiments across diverse benchmarks and model architectures demonstrate that weak reasoners can effectively incentivize reasoning in stronger student models, consistently improving performance across a wide range of reasoning tasks. Our results suggest that this simple weak-to-strong paradigm is a promising and generalizable alternative to costly methods for incentivizing strong reasoning capabilities at inference-time in LLMs. The code is publicly available at https://github.com/yuanyige/w2sr.

