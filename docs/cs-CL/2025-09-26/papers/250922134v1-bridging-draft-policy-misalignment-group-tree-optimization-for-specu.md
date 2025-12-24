---
layout: default
title: "Bridging Draft Policy Misalignment: Group Tree Optimization for Speculative Decoding"
---

# Bridging Draft Policy Misalignment: Group Tree Optimization for Speculative Decoding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.22134" class="toolbar-btn" target="_blank">📄 arXiv: 2509.22134v1</a>
  <a href="https://arxiv.org/pdf/2509.22134.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.22134v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.22134v1', 'Bridging Draft Policy Misalignment: Group Tree Optimization for Speculative Decoding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shijing Hu, Jingyang Li, Zhihui Lu, Pan Zhou

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出Group Tree Optimization，解决推测解码中草稿策略不对齐问题，提升LLM推理速度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推测解码` `大型语言模型` `模型加速` `策略对齐` `树搜索`

## 📋 核心要点

1. 现有推测解码方法训练目标与实际解码策略不一致，导致草稿模型性能受限，无法充分加速LLM推理。
2. GTO通过Draft Tree Reward直接优化解码性能，并使用Group-based Draft Policy Training稳定训练草稿模型。
3. 实验表明，GTO在多个LLM和任务上显著提升了接受长度和推理速度，优于现有最佳方法。

## 📝 摘要（中文）

推测解码通过轻量级草稿模型并行生成多个token，供目标模型验证，从而加速大型语言模型（LLM）的推理。然而，现有的训练目标仅优化单一贪婪草稿路径，而解码过程遵循树策略，对多个分支进行重排序和验证。这种草稿策略的不对齐限制了可实现的加速。我们引入了Group Tree Optimization (GTO)，通过两个组成部分使训练与解码时的树策略对齐：（i）Draft Tree Reward，一种无采样的目标，等于目标模型下草稿树的预期接受长度，直接衡量解码性能；（ii）Group-based Draft Policy Training，一种稳定的优化方案，对比来自当前和冻结的参考草稿模型的树，形成去偏的组标准化优势，并沿着最长接受序列应用PPO风格的替代目标，以实现稳健的更新。我们进一步证明，增加我们的Draft Tree Reward可以显著提高接受长度和加速。在对话（MT-Bench）、代码（HumanEval）和数学（GSM8K）以及多个LLM（例如，LLaMA-3.1-8B、LLaMA-3.3-70B、Vicuna-1.3-13B、DeepSeek-R1-Distill-LLaMA-8B）上，GTO将接受长度提高了7.4%，并比之前的最先进EAGLE-3实现了额外的7.7%的加速。通过弥合草稿策略的不对齐，GTO为高效的LLM推理提供了一种实用、通用的解决方案。

## 🔬 方法详解

**问题定义**：现有推测解码方法在训练草稿模型时，通常只关注单一的贪婪解码路径，而实际解码过程中会探索多个分支，形成一棵树。这种训练目标与解码策略的不一致（draft policy misalignment）导致草稿模型无法充分利用目标模型的反馈，限制了推测解码的加速效果。现有方法未能有效解决这种不对齐问题，导致草稿模型预测的token被目标模型接受的比例较低，降低了整体推理速度。

**核心思路**：GTO的核心思路是将草稿模型的训练目标与实际解码时的树策略对齐。具体来说，GTO直接优化草稿树的预期接受长度，即目标模型接受的token数量的期望值。通过最大化这个期望值，GTO鼓励草稿模型生成更有可能被目标模型接受的token序列，从而提高推测解码的效率。此外，GTO还引入了一种稳定的训练方案，以避免训练过程中的不稳定性和崩溃。

**技术框架**：GTO主要包含两个核心模块：Draft Tree Reward和Group-based Draft Policy Training。Draft Tree Reward是一个无采样的目标函数，用于衡量草稿树的质量。Group-based Draft Policy Training是一种基于PPO的优化方案，用于更新草稿模型的参数。该方案通过对比当前草稿模型和冻结的参考草稿模型生成的树，计算优势函数，并使用该优势函数来更新草稿模型。整体流程如下：首先，使用草稿模型生成一棵草稿树；然后，使用目标模型验证草稿树中的token；接着，计算Draft Tree Reward；最后，使用Group-based Draft Policy Training更新草稿模型的参数。

**关键创新**：GTO最重要的技术创新点在于其直接优化草稿树的预期接受长度。与现有方法不同，GTO不依赖于单一的贪婪解码路径，而是考虑了整个草稿树的结构。这种方法能够更准确地反映草稿模型的实际解码性能，从而实现更有效的训练。此外，Group-based Draft Policy Training通过引入参考模型和组标准化，提高了训练的稳定性，避免了训练过程中的崩溃。

**关键设计**：Draft Tree Reward的设计关键在于如何有效地计算草稿树的预期接受长度。GTO采用了一种无采样的计算方法，避免了采样带来的方差。Group-based Draft Policy Training的关键在于如何选择合适的参考模型和如何计算优势函数。GTO选择冻结的草稿模型作为参考模型，并使用组标准化来减少方差。损失函数采用PPO风格的替代目标函数，以保证训练的稳定性。

## 📊 实验亮点

实验结果表明，GTO在多个LLM（如LLaMA-3.1-8B、LLaMA-3.3-70B、Vicuna-1.3-13B、DeepSeek-R1-Distill-LLaMA-8B）和任务（如MT-Bench、HumanEval、GSM8K）上均取得了显著的性能提升。GTO将接受长度提高了7.4%，并比之前的最先进EAGLE-3实现了额外的7.7%的加速。这些结果表明，GTO是一种有效的推测解码加速方法。

## 🎯 应用场景

GTO可广泛应用于各种需要加速LLM推理的场景，例如对话系统、代码生成、机器翻译等。通过提高LLM的推理速度，GTO可以降低计算成本，提高用户体验，并促进LLM在资源受限环境中的部署。未来，GTO可以与其他加速技术相结合，进一步提高LLM的推理效率。

## 📄 摘要（原文）

> Speculative decoding accelerates large language model (LLM) inference by letting a lightweight draft model propose multiple tokens that the target model verifies in parallel. Yet existing training objectives optimize only a single greedy draft path, while decoding follows a tree policy that re-ranks and verifies multiple branches. This draft policy misalignment limits achievable speedups. We introduce Group Tree Optimization (GTO), which aligns training with the decoding-time tree policy through two components: (i) Draft Tree Reward, a sampling-free objective equal to the expected acceptance length of the draft tree under the target model, directly measuring decoding performance; (ii) Group-based Draft Policy Training, a stable optimization scheme that contrasts trees from the current and a frozen reference draft model, forming debiased group-standardized advantages and applying a PPO-style surrogate along the longest accepted sequence for robust updates. We further prove that increasing our Draft Tree Reward provably improves acceptance length and speedup. Across dialogue (MT-Bench), code (HumanEval), and math (GSM8K), and multiple LLMs (e.g., LLaMA-3.1-8B, LLaMA-3.3-70B, Vicuna-1.3-13B, DeepSeek-R1-Distill-LLaMA-8B), GTO increases acceptance length by 7.4% and yields an additional 7.7% speedup over prior state-of-the-art EAGLE-3. By bridging draft policy misalignment, GTO offers a practical, general solution for efficient LLM inference.

