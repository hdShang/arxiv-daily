---
layout: default
title: "No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization"
---

# No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23387" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23387v1</a>
  <a href="https://arxiv.org/pdf/2509.23387.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23387v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23387v1', 'No Loss, No Gain: Gated Refinement and Adaptive Compression for Prompt Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenhang Shi, Yiren Chen, Shuqing Bian, Xinyi Zhang, Kai Tang, Pengfei Hu, Zhe Zhao, Wei Lu, Xiaoyong Du

**分类**: cs.CL

**发布日期**: 2025-09-27

**备注**: 10 pages for main content

**🔗 代码/项目**: [GITHUB](https://github.com/Eric8932/GRACE)

---

## 💡 一句话要点

**提出GRACE框架，通过门控优化和自适应压缩提升Prompt优化效率与性能。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `Prompt优化` `大型语言模型` `门控机制` `自适应压缩` `局部最优` `高效优化` `反馈调节` `更新拒绝`

## 📋 核心要点

1. 现有Prompt优化方法难以稳定生成改进Prompt，效率低且易陷入局部最优。
2. GRACE框架通过门控优化稳定Prompt更新，自适应压缩跳出局部最优，提升优化效率。
3. 实验表明，GRACE在多个任务上显著优于现有方法，且仅需25%的计算资源。

## 📝 摘要（中文）

Prompt工程对于充分利用大型语言模型（LLMs）至关重要。自动prompt优化为代价高昂的手动设计提供了一种可扩展的替代方案，但生成有效的prompt仍然具有挑战性。现有方法通常难以稳定地生成改进的prompt，导致效率低下，并且忽略了prompt优化容易陷入局部最优的问题。为了解决这个问题，我们提出了GRACE，一个集成了两种协同策略的框架：门控优化和自适应压缩，从而实现高效的prompt优化。门控优化策略引入了反馈调节门和更新拒绝门，它们优化更新信号以产生稳定有效的prompt改进。当优化停滞时，自适应压缩策略提炼prompt的核心概念，重构优化轨迹并开辟新的路径。通过策略性地引入信息损失，GRACE在性能和效率方面都实现了显著的提升。在跨三个实际领域的11个任务（包括BIG-Bench Hard (BBH)、特定领域和通用NLP任务）的广泛实验中，GRACE相对于最先进的方法分别实现了4.7%、4.4%和2.7%的显著平均相对性能提升。进一步的分析表明，GRACE仅使用先前方法所需的25%的prompt生成预算就实现了这些收益，突出了其高优化效率和低计算开销。

## 🔬 方法详解

**问题定义**：论文旨在解决自动Prompt优化中效率低、易陷入局部最优的问题。现有方法难以稳定生成改进的Prompt，导致优化过程效率低下，且容易陷入局部最优解，难以找到全局最优的Prompt。

**核心思路**：论文的核心思路是通过引入门控机制来稳定Prompt的更新过程，并利用自适应压缩策略来跳出局部最优。门控机制可以过滤掉无效或有害的更新信号，从而保证Prompt的稳定改进。自适应压缩则可以在优化停滞时，提炼Prompt的核心信息，重构优化轨迹，从而开辟新的优化路径。

**技术框架**：GRACE框架包含两个主要模块：门控优化（Gated Refinement）和自适应压缩（Adaptive Compression）。门控优化模块通过反馈调节门和更新拒绝门来控制Prompt的更新过程，确保更新的有效性和稳定性。自适应压缩模块则在优化停滞时，对Prompt进行压缩，提取核心信息，并基于压缩后的Prompt重新开始优化。

**关键创新**：GRACE的关键创新在于将门控机制和自适应压缩策略结合起来，共同作用于Prompt优化过程。门控机制保证了Prompt更新的稳定性，避免了无效或有害的更新，而自适应压缩则提供了跳出局部最优的手段，从而提高了Prompt优化的效率和性能。与现有方法相比，GRACE能够更稳定、更高效地生成高质量的Prompt。

**关键设计**：门控优化模块中的反馈调节门和更新拒绝门的设计是关键。反馈调节门根据Prompt的性能反馈来调整更新信号的强度，而更新拒绝门则根据更新信号的质量来决定是否接受更新。自适应压缩模块则需要设计合适的压缩算法，以保证压缩后的Prompt能够保留核心信息，并能够有效地引导后续的优化过程。具体的参数设置和损失函数选择需要根据具体的任务进行调整。

## 📊 实验亮点

GRACE在11个任务上进行了广泛的实验，包括BIG-Bench Hard (BBH)、特定领域和通用NLP任务。实验结果表明，GRACE相对于最先进的方法分别实现了4.7%、4.4%和2.7%的显著平均相对性能提升。更重要的是，GRACE仅使用先前方法所需的25%的Prompt生成预算就实现了这些收益，突出了其高优化效率和低计算开销。

## 🎯 应用场景

GRACE框架可广泛应用于各种需要Prompt工程的场景，例如文本生成、问答系统、机器翻译等。通过自动优化Prompt，可以显著提升这些应用的效果，并降低人工设计的成本。该研究对于推动LLM在实际应用中的普及具有重要意义。

## 📄 摘要（原文）

> Prompt engineering is crucial for leveraging the full potential of large language models (LLMs). While automatic prompt optimization offers a scalable alternative to costly manual design, generating effective prompts remains challenging. Existing methods often struggle to stably generate improved prompts, leading to low efficiency, and overlook that prompt optimization easily gets trapped in local optima. Addressing this, we propose GRACE, a framework that integrates two synergistic strategies: Gated Refinement and Adaptive Compression, achieving Efficient prompt optimization. The gated refinement strategy introduces a feedback regulation gate and an update rejection gate, which refine update signals to produce stable and effective prompt improvements. When optimization stagnates, the adaptive compression strategy distills the prompt's core concepts, restructuring the optimization trace and opening new paths. By strategically introducing information loss through refinement and compression, GRACE delivers substantial gains in performance and efficiency. In extensive experiments on 11 tasks across three practical domains, including BIG-Bench Hard (BBH), domain-specific, and general NLP tasks, GRACE achieves significant average relative performance improvements of 4.7%, 4.4% and 2.7% over state-of-the-art methods, respectively. Further analysis shows that GRACE achieves these gains using only 25% of the prompt generation budget required by prior methods, highlighting its high optimization efficiency and low computational overhead. Our code is available at https://github.com/Eric8932/GRACE.

