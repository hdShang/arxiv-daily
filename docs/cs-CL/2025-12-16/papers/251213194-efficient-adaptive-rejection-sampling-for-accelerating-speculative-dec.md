---
layout: default
title: Efficient Adaptive Rejection Sampling for Accelerating Speculative Decoding in Large Language Models
---

# Efficient Adaptive Rejection Sampling for Accelerating Speculative Decoding in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13194" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13194</a>
  <a href="https://arxiv.org/pdf/2512.13194.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13194" onclick="toggleFavorite(this, '2512.13194', 'Efficient Adaptive Rejection Sampling for Accelerating Speculative Decoding in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chendong Sun, mingmin Chen, Lei Xu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出高效自适应拒绝采样(EARS)以加速大语言模型推测解码。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `推测解码` `大语言模型` `拒绝采样` `自适应阈值` `模型不确定性`

## 📋 核心要点

1. 推测解码中固定的拒绝采样阈值导致高不确定性场景下出现不必要的token拒绝，降低效率。
2. EARS通过目标模型预测不确定性动态调整接受阈值，在不确定时放宽标准，减少随机拒绝。
3. 实验表明，EARS显著提升了推测解码的吞吐量，且对模型准确率的影响可忽略不计。

## 📝 摘要（中文）

推测解码是一种通过利用快速草稿模型提出候选token序列，并使用大型目标模型并行验证它们来加速大型语言模型(LLM)自回归推理的突出技术。然而，其核心组件——拒绝采样机制——依赖于固定的、与上下文无关的随机阈值。这导致了高不确定性生成场景中显著的“随机拒绝”问题，其中合理的候选token由于随机机会而被频繁拒绝，从而降低了推理效率。本文介绍了一种高效自适应拒绝采样(EARS)方法，该方法通过结合目标模型自身的预测不确定性（以1 - max(P_target)衡量）来动态调整接受阈值。通过引入与此不确定性成比例的容差项，EARS在模型不确定时智能地放宽接受标准，在模型有信心时保持严格标准，从而有效地减少随机拒绝。在创造性写作和开放领域问答任务上的实验表明，EARS显著提高了推测解码的效率，在GSM8K基准测试中实现了高达18.12%的吞吐量提升，而准确率仅下降了0.84%。该方法不需要修改模型架构，并且可以无缝集成到现有的推测解码框架中。

## 🔬 方法详解

**问题定义**：推测解码旨在加速LLM的自回归推理，但其拒绝采样机制依赖于固定的阈值，导致在高不确定性场景下，即使是合理的候选token也可能被随机拒绝，降低了推理效率。现有方法未能充分利用目标模型自身的信息来动态调整接受标准。

**核心思路**：EARS的核心在于利用目标模型预测的不确定性来动态调整拒绝采样的接受阈值。当目标模型对预测结果不确定时，适当放宽接受标准，允许更多可能的token通过，从而减少随机拒绝；当模型有信心时，则保持严格的标准。这样可以在保证生成质量的前提下，提高推理效率。

**技术框架**：EARS可以无缝集成到现有的推测解码框架中。其主要流程如下：首先，草稿模型生成候选token序列；然后，目标模型对这些token进行验证。在验证过程中，EARS根据目标模型预测概率的最大值(max(P_target))计算不确定性，并基于此动态调整接受阈值。最后，根据调整后的阈值决定是否接受候选token。

**关键创新**：EARS的关键创新在于引入了自适应的拒绝采样机制，它不再依赖于固定的阈值，而是根据目标模型自身的预测不确定性动态调整。这种方法能够更智能地平衡生成质量和推理效率，尤其是在高不确定性场景下，能够显著减少随机拒绝，提高吞吐量。

**关键设计**：EARS的关键设计在于容差项的引入，该容差项与目标模型预测不确定性成比例。具体来说，接受阈值被调整为原始阈值加上一个容差值，该容差值等于 `alpha * (1 - max(P_target))`，其中 `alpha` 是一个可调节的超参数，用于控制容差的强度。`alpha` 的选择需要根据具体任务进行调整，以达到最佳的性能。

## 📊 实验亮点

实验结果表明，EARS在创造性写作和开放领域问答任务中显著提高了推测解码的效率。在GSM8K基准测试中，EARS实现了高达18.12%的吞吐量提升，而准确率仅下降了0.84%。这些结果表明，EARS能够在保证生成质量的前提下，显著加速LLM的推理过程。

## 🎯 应用场景

EARS可广泛应用于需要快速生成文本的场景，例如聊天机器人、机器翻译、文本摘要、代码生成等。通过提高LLM的推理效率，EARS能够降低计算成本，提升用户体验，并促进LLM在资源受限环境中的部署。此外，EARS的自适应特性使其能够更好地应对各种生成任务，尤其是在创造性写作和开放领域问答等高不确定性场景中。

## 📄 摘要（原文）

> Speculative Decoding is a prominent technique for accelerating the autoregressive inference of large language models (LLMs) by employing a fast draft model to propose candidate token sequences and a large target model to verify them in parallel. However, its core component -- the rejection sampling mechanism -- relies on a fixed, context-independent random threshold. This leads to a significant "random rejection" problem in high-uncertainty generation scenarios, where plausible candidate tokens are frequently rejected due to random chance, undermining inference efficiency. This paper introduces Efficient Adaptive Rejection Sampling (EARS), a novel method that dynamically adjusts the acceptance threshold by incorporating the target model's own predictive uncertainty, measured as 1 - max(P_target). By introducing a tolerance term proportional to this uncertainty, EARS intelligently relaxes the acceptance criterion when the model is uncertain, effectively reducing random rejections while maintaining strict standards when the model is confident. Experiments on creative writing and open-domain QA tasks demonstrate that EARS significantly enhances the efficiency of speculative decoding, achieving up to an 18.12% increase in throughput with a negligible 0.84% accuracy drop on the GSM8K benchmark. The method requires no modifications to model architectures and can be seamlessly integrated into existing speculative decoding frameworks.

