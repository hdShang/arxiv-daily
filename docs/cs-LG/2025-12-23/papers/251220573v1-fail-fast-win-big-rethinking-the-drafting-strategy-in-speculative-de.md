---
layout: default
title: Fail Fast, Win Big: Rethinking the Drafting Strategy in Speculative Decoding via Diffusion LLMs
---

# Fail Fast, Win Big: Rethinking the Drafting Strategy in Speculative Decoding via Diffusion LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20573" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20573v1</a>
  <a href="https://arxiv.org/pdf/2512.20573.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20573v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20573v1', 'Fail Fast, Win Big: Rethinking the Drafting Strategy in Speculative Decoding via Diffusion LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Pan, Zhuofu Chen, Ravi Netravali

**分类**: cs.LG, cs.AI, cs.DC

**发布日期**: 2025-12-23

**🔗 代码/项目**: [GITHUB](https://github.com/ruipeterpan/failfast)

---

## 💡 一句话要点

**FailFast：利用扩散LLM加速推测解码，显著提升自回归LLM推理速度**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推测解码` `扩散模型` `大语言模型` `并行计算` `自回归模型`

## 📋 核心要点

1. 现有自回归LLM推理速度慢，而扩散LLM虽然并行生成快，但质量不高，直接应用存在效率-质量的权衡。
2. FailFast利用扩散LLM作为推测解码的起草者，动态调整推测长度，在易推测区域大胆推测，难推测区域快速失败，降低计算成本。
3. 实验表明，FailFast无需微调即可显著加速自回归LLM，在多种模型和任务上优于现有方法，最高可达4.9倍加速。

## 📝 摘要（中文）

扩散大语言模型(dLLMs)提供快速、并行的token生成能力，但其独立使用存在效率和质量之间的固有权衡。本文表明，如果谨慎应用，dLLMs的特性实际上可以成为自回归(AR)验证器中推测解码的起草者的优势。我们的核心见解是，dLLM并行解码带来的速度优势显著降低了代价高昂的拒绝风险，为有效实现(难以捉摸的)长草案提供了一种实用的机制，从而在使用推测解码时实现大幅加速。我们提出了FailFast，一个基于dLLM的推测解码框架，通过动态调整其推测长度来实现这种方法。它通过在难以推测的区域花费最少的计算来缩小推测延迟来“快速失败”，并通过在更容易的区域积极扩展草案长度来减少验证延迟来“大获全胜”(在许多情况下，一次推测和接受70个token!)。在没有任何微调的情况下，FailFast实现了AR LLM的无损加速，并且在不同的模型和工作负载中，相比于vanilla解码实现了高达4.9倍的加速，相比于最佳的naive dLLM起草者实现了1.7倍的加速，相比于EAGLE-3实现了1.4倍的加速。我们在https://github.com/ruipeterpan/failfast开源了FailFast。

## 🔬 方法详解

**问题定义**：论文旨在解决自回归大语言模型(AR LLM)推理速度慢的问题。现有的推测解码方法依赖于较短的草案长度，难以充分利用并行计算的优势，而直接使用扩散LLM(dLLM)生成文本又面临质量不高的问题。因此，如何有效地利用dLLM的并行生成能力来加速AR LLM的推理是一个关键挑战。

**核心思路**：论文的核心思路是利用dLLM作为推测解码的起草者，并根据文本生成的难易程度动态调整推测长度。在容易推测的区域，积极扩展草案长度，以减少验证延迟；在难以推测的区域，快速失败，避免浪费计算资源。这种动态调整策略旨在最大化并行计算的优势，同时避免dLLM生成低质量文本的风险。

**技术框架**：FailFast框架主要包含以下几个阶段：1) 使用dLLM并行生成草案token序列；2) 使用AR LLM验证生成的token序列；3) 根据验证结果，接受或拒绝部分或全部token；4) 基于已接受的token，继续生成后续token。框架的关键在于动态调整草案长度的策略，它会根据历史验证结果和当前生成难度，自适应地调整dLLM的推测长度。

**关键创新**：FailFast的关键创新在于动态调整推测长度的策略。与传统的推测解码方法不同，FailFast不采用固定的草案长度，而是根据文本生成的难易程度进行自适应调整。这种动态调整策略能够更有效地利用dLLM的并行生成能力，同时避免生成低质量文本的风险。

**关键设计**：FailFast的关键设计包括：1) 使用dLLM生成草案token序列；2) 使用AR LLM进行验证；3) 设计了一种动态调整草案长度的算法，该算法基于历史验证结果和当前生成难度，自适应地调整dLLM的推测长度。具体的参数设置和损失函数信息未知。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20573v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20573v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20573v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

FailFast在多种模型和任务上实现了显著的加速效果。实验结果表明，FailFast相比于vanilla解码实现了高达4.9倍的加速，相比于最佳的naive dLLM起草者实现了1.7倍的加速，相比于EAGLE-3实现了1.4倍的加速。这些结果表明，FailFast能够有效地利用dLLM的并行生成能力，并显著提升AR LLM的推理速度。

## 🎯 应用场景

FailFast可应用于各种需要快速文本生成的场景，例如：智能对话系统、机器翻译、文本摘要等。通过加速LLM的推理速度，可以显著提升用户体验，降低计算成本，并促进LLM在资源受限环境中的部署。该研究对于推动LLM的实际应用具有重要意义。

## 📄 摘要（原文）

> Diffusion Large Language Models (dLLMs) offer fast, parallel token generation, but their standalone use is plagued by an inherent efficiency-quality tradeoff. We show that, if carefully applied, the attributes of dLLMs can actually be a strength for drafters in speculative decoding with autoregressive (AR) verifiers. Our core insight is that dLLM's speed from parallel decoding drastically lowers the risk of costly rejections, providing a practical mechanism to effectively realize the (elusive) lengthy drafts that lead to large speedups with speculative decoding. We present FailFast, a dLLM-based speculative decoding framework that realizes this approach by dynamically adapting its speculation length. It "fails fast" by spending minimal compute in hard-to-speculate regions to shrink speculation latency and "wins big" by aggressively extending draft lengths in easier regions to reduce verification latency (in many cases, speculating and accepting 70 tokens at a time!). Without any fine-tuning, FailFast delivers lossless acceleration of AR LLMs and achieves up to 4.9$\times$ speedup over vanilla decoding, 1.7$\times$ over the best naive dLLM drafter, and 1.4$\times$ over EAGLE-3 across diverse models and workloads. We open-source FailFast at https://github.com/ruipeterpan/failfast.

