---
layout: default
title: DEER: Draft with Diffusion, Verify with Autoregressive Models
---

# DEER: Draft with Diffusion, Verify with Autoregressive Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.15176" class="toolbar-btn" target="_blank">📄 arXiv: 2512.15176v1</a>
  <a href="https://arxiv.org/pdf/2512.15176.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.15176v1" onclick="toggleFavorite(this, '2512.15176v1', 'DEER: Draft with Diffusion, Verify with Autoregressive Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zicong Cheng, Guo-Wei Yang, Jia Li, Zhijie Deng, Meng-Hao Guo, Shi-Min Hu

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-17

**备注**: Homepage : https://czc726.github.io/DEER/

**🔗 代码/项目**: [PROJECT_PAGE](https://czc726.github.io/DEER/)

---

## 💡 一句话要点

**DEER：利用扩散模型进行草稿生成，自回归模型进行验证，提升LLM推理效率。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推测解码` `扩散模型` `大型语言模型` `效率优化` `并行解码`

## 📋 核心要点

1. 现有推测解码方法依赖自回归草稿模型，存在不确定性累积和串行解码的瓶颈，限制了加速效果。
2. DEER利用扩散大型语言模型（dLLM）并行生成草稿，克服了自回归草稿模型的局限性，提升了效率。
3. 实验表明，DEER显著提高了草稿接受长度和加速效果，在HumanEval数据集上实现了5.54倍的加速。

## 📝 摘要（中文）

大型语言模型驱动的智能体和推理系统面临着效率挑战，自回归解码的固有延迟是主要瓶颈。推测解码通过草稿-验证机制缓解这个问题，但现有方法依赖于自回归草稿模型，导致两个问题：(1) 逐步累积的不确定性导致目标模型和草稿模型之间的信任逐渐崩溃；(2) 自回归草稿模型的固有串行解码。这些因素限制了加速效果。本文提出使用扩散大型语言模型（dLLM）作为草稿模型，通过其概率建模和高效并行解码策略克服这些问题。基于此，我们提出了DEER，一个高效的推测解码框架，使用扩散模型生成草稿，自回归模型进行验证。为了实现高质量的草稿生成，DEER采用两阶段训练流程，使基于dLLM的草稿模型与目标自回归模型对齐，并采用单步解码生成长草稿段。实验表明，DEER的草稿接受长度高达32个token，远超EAGLE-3的10个token。在HumanEval数据集上，使用Qwen3-30B-A3B，DEER实现了5.54倍的加速，而EAGLE-3仅为2.41倍。

## 🔬 方法详解

**问题定义**：现有基于自回归模型的推测解码方法，由于草稿模型也是自回归的，存在两个主要问题：一是每一步预测的不确定性会累积，导致目标模型对草稿的信任度降低；二是自回归模型固有的串行解码方式限制了生成速度，最终导致整体加速效果不佳。因此，需要一种能够并行生成高质量草稿的方法，以突破现有推测解码的效率瓶颈。

**核心思路**：DEER的核心思路是使用扩散大型语言模型（dLLM）作为草稿模型。扩散模型具有并行解码的特性，可以一次性生成较长的草稿段，避免了自回归模型逐步累积误差的问题。同时，通过训练使dLLM的生成结果与目标自回归模型对齐，保证草稿的质量，从而提高目标模型接受草稿的概率，最终提升整体推理速度。

**技术框架**：DEER框架主要包含两个阶段：草稿生成阶段和验证阶段。在草稿生成阶段，使用训练好的dLLM并行生成一段草稿文本。在验证阶段，使用目标自回归模型对草稿进行验证，判断草稿是否可以被接受。如果草稿被接受，则可以跳过对这些token的自回归解码，从而实现加速。如果草稿未被完全接受，则从接受的最后一个token开始，使用自回归模型继续生成。

**关键创新**：DEER的关键创新在于使用扩散模型作为草稿模型，替代了传统的自回归草稿模型。这使得草稿生成过程可以并行进行，显著提高了生成速度。此外，DEER还提出了一个两阶段的训练流程，用于对齐dLLM和目标自回归模型，保证了草稿的质量。单步解码策略进一步提升了草稿的长度。

**关键设计**：DEER采用了两阶段训练流程：首先，使用目标自回归模型的输出作为监督信号，训练dLLM生成与目标模型一致的文本。其次，使用强化学习进一步微调dLLM，使其生成的草稿更容易被目标模型接受。此外，DEER采用单步解码策略，直接生成较长的草稿段，避免了逐步生成带来的误差累积。具体的损失函数和网络结构细节在论文中有详细描述。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15176v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15176v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.15176v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

DEER在HumanEval数据集上，使用Qwen3-30B-A3B模型，实现了5.54倍的加速，显著优于EAGLE-3的2.41倍。DEER的草稿接受长度高达32个token，远超EAGLE-3的10个token。这些实验结果表明，DEER能够有效提高LLM的推理效率，并在草稿质量和加速效果方面取得了显著的提升。

## 🎯 应用场景

DEER具有广泛的应用前景，可以应用于各种需要高效LLM推理的场景，例如智能对话系统、代码生成、文本摘要、机器翻译等。通过提高LLM的推理速度，DEER可以降低计算成本，提升用户体验，并促进LLM在资源受限设备上的部署。未来，DEER还可以与其他加速技术相结合，进一步提升LLM的推理效率。

## 📄 摘要（原文）

> Efficiency, as a critical practical challenge for LLM-driven agentic and reasoning systems, is increasingly constrained by the inherent latency of autoregressive (AR) decoding. Speculative decoding mitigates this cost through a draft-verify scheme, yet existing approaches rely on AR draft models (a.k.a., drafters), which introduce two fundamental issues: (1) step-wise uncertainty accumulation leads to a progressive collapse of trust between the target model and the drafter, and (2) inherently sequential decoding of AR drafters. Together, these factors cause limited speedups. In this paper, we show that a diffusion large language model (dLLM) drafters can naturally overcome these issues through its fundamentally different probabilistic modeling and efficient parallel decoding strategy. Building on this insight, we introduce DEER, an efficient speculative decoding framework that drafts with diffusion and verifies with AR models. To enable high-quality drafting, DEER employs a two-stage training pipeline to align the dLLM-based drafters with the target AR model, and further adopts single-step decoding to generate long draft segments. Experiments show DEER reaches draft acceptance lengths of up to 32 tokens, far surpassing the 10 tokens achieved by EAGLE-3. Moreover, on HumanEval with Qwen3-30B-A3B, DEER attains a 5.54x speedup, while EAGLE-3 achieves only 2.41x. Code, model, demo, etc, will be available at https://czc726.github.io/DEER/

