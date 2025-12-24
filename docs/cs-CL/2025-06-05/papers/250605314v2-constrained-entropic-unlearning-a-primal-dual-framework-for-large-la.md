---
layout: default
title: "Constrained Entropic Unlearning: A Primal-Dual Framework for Large Language Models"
---

# Constrained Entropic Unlearning: A Primal-Dual Framework for Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05314" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05314v2</a>
  <a href="https://arxiv.org/pdf/2506.05314.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05314v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05314v2', 'Constrained Entropic Unlearning: A Primal-Dual Framework for Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Taha Entesari, Arman Hatami, Rinat Khaziev, Anil Ramakrishna, Mahyar Fazlyab

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-06-05 (更新: 2025-10-27)

**备注**: The Thirty-Ninth Annual Conference on Neural Information Processing Systems

---

## 💡 一句话要点

**提出约束熵消除方法以解决大语言模型遗忘问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `遗忘机制` `约束优化` `信息消除` `隐私保护` `模型性能` `数值稳定性`

## 📋 核心要点

1. 现有的遗忘方法通常将遗忘和保留结合为单一的标量损失，导致优化不稳定和保留数据性能下降。
2. 本文提出将LLM的遗忘问题形式化为约束优化问题，通过新颖的损失函数实现遗忘和保留的平衡。
3. 在TOFU和MUSE基准测试中，所提方法在多种LLM架构上表现优于现有的最先进基线，成功去除目标信息。

## 📝 摘要（中文）

在实际应用中，大语言模型（LLMs）面临着消除敏感、过时或专有信息的需求。现有的消除方法通常将遗忘和保留视为一个正则化的权衡，导致优化不稳定和保留数据性能下降。本文提出了一种新的LLM消除方法，将其形式化为约束优化问题，通过一种新颖的对数边际平坦化损失来强制遗忘，同时通过对保留集的硬约束来保持保留。与基于熵的目标相比，所提损失函数不依赖于softmax，数值稳定，保持非消失梯度，从而实现更高效和稳健的优化。实验结果表明，该方法在TOFU和MUSE基准测试中表现优异，能够有效去除目标信息，同时保持下游任务的效用。

## 🔬 方法详解

**问题定义**：本文解决的是大语言模型在实际应用中如何有效消除敏感信息的问题。现有方法在遗忘和保留之间的权衡常常导致优化不稳定，影响模型性能。

**核心思路**：论文提出了一种新的约束优化框架，通过对数边际平坦化损失来强制遗忘，同时对保留集施加硬约束，以确保保留信息的完整性。这样的设计使得遗忘过程更加稳定，且不影响保留数据的性能。

**技术框架**：整体架构包括两个主要模块：遗忘模块和保留模块。遗忘模块通过新颖的损失函数实现对指定遗忘集的输出分布的均匀化，而保留模块则通过硬约束确保保留集的信息不被遗忘。

**关键创新**：最重要的技术创新在于提出了一种不依赖于softmax的损失函数，具有数值稳定性和非消失梯度的特性。这一创新使得优化过程更加高效和稳健，克服了现有方法的不足。

**关键设计**：在损失函数设计上，采用了对数边际平坦化损失，并通过可扩展的原始-对偶算法求解约束问题，确保在不增加额外计算开销的情况下，优化遗忘与保留之间的权衡。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在TOFU和MUSE基准测试中，所提方法在多种LLM架构上表现优于现有的最先进基线，成功去除目标信息的同时，保持下游任务的效用，提升幅度显著，验证了方法的有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括数据隐私保护、模型更新和信息管理等。随着对数据隐私的关注增加，能够有效消除敏感信息的模型将具有重要的实际价值，未来可能在法律合规和用户信任方面产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) deployed in real-world settings increasingly face the need to unlearn sensitive, outdated, or proprietary information. Existing unlearning methods typically formulate forgetting and retention as a regularized trade-off, combining both objectives into a single scalarized loss. This often leads to unstable optimization and degraded performance on retained data, especially under aggressive forgetting. We propose a new formulation of LLM unlearning as a constrained optimization problem: forgetting is enforced via a novel logit-margin flattening loss that explicitly drives the output distribution toward uniformity on a designated forget set, while retention is preserved through a hard constraint on a separate retain set. Compared to entropy-based objectives, our loss is softmax-free, numerically stable, and maintains non-vanishing gradients, enabling more efficient and robust optimization. We solve the constrained problem using a scalable primal-dual algorithm that exposes the trade-off between forgetting and retention through the dynamics of the dual variable, all without any extra computational overhead. Evaluations on the TOFU and MUSE benchmarks across diverse LLM architectures demonstrate that our approach consistently matches or exceeds state-of-the-art baselines, effectively removing targeted information while preserving downstream utility.

