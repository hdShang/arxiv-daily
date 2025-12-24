---
layout: default
title: "Critique to Verify: Accurate and Honest Test-Time Scaling with RL-Trained Verifiers"
---

# Critique to Verify: Accurate and Honest Test-Time Scaling with RL-Trained Verifiers

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23152" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23152v1</a>
  <a href="https://arxiv.org/pdf/2509.23152.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23152v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23152v1', 'Critique to Verify: Accurate and Honest Test-Time Scaling with RL-Trained Verifiers')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhicheng Yang, Zhijiang Guo, Yinya Huang, Yongxin Wang, Yiwei Wang, Xiaodan Liang, Jing Tang

**分类**: cs.LG

**发布日期**: 2025-09-27

**备注**: 15 pages, 7 figures

---

## 💡 一句话要点

**提出Mirror-Critique框架，通过强化学习训练验证器，提升大语言模型测试时推理的准确性和可靠性。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `测试时缩放` `强化学习` `验证器训练` `批判学习`

## 📋 核心要点

1. 大语言模型测试时缩放方法依赖奖励模型选择，但其难以识别少量正确答案，限制了性能。
2. Mirror-Critique框架通过对比模型解与真实解，利用高质量批判信号训练验证器，提升验证能力。
3. 实验表明，Mirror-Verifier显著提升了解的准确性，并增强了模型识别自身能力边界的诚实性。

## 📝 摘要（中文）

本文提出了一种名为Mirror-Critique的框架，旨在提升大语言模型（LLMs）在测试时通过解采样和聚合进行缩放的推理性能。现有方法通常采用奖励模型选择，但其无法有效识别少量但正确的答案，限制了其效果。Mirror-Critique通过对比模型生成的解与真实解，利用丰富的批判信号训练验证器，解决了现有方法缺乏信息性批判信号的问题。该框架使用一个小型指令调优模型，通过拒绝采样合成高质量的批判数据，教导验证器识别错误及其原因。合成数据用于冷启动RLVR过程中的LLMs，进一步提高验证能力。最终的Mirror-Verifier通过为每个解生成多个批判，并将它们聚合成一个验证分数，用于加权投票或选择性拒绝回答。实验结果表明，Mirror-Verifier在解的准确性方面显著优于多数投票，并提高了求解器识别和拒绝回答超出其能力范围问题的诚实性。

## 🔬 方法详解

**问题定义**：现有的大语言模型在测试时进行缩放的方法，通常依赖于奖励模型来选择最佳答案。然而，这些奖励模型往往无法准确识别那些少数但正确的答案，导致最终性能提升有限，甚至不如简单的多数投票策略。问题的核心在于，验证器在训练过程中缺乏足够的信息性批判信号，难以区分正确和错误的答案，尤其是当正确答案属于少数情况时。

**核心思路**：Mirror-Critique的核心思路是通过引入更丰富的批判信号来训练验证器。具体来说，该方法通过对比模型生成的解与真实解，让验证器学习识别错误的原因和方式。这种对比学习的方式能够提供更强的监督信号，帮助验证器更好地理解正确答案的特征，从而提高其识别少数正确答案的能力。

**技术框架**：Mirror-Critique框架主要包含以下几个阶段：1) **批判数据合成**：使用一个小型指令调优模型，通过拒绝采样的方式，生成高质量的批判数据。这些数据不仅包含对错误答案的否定，还包含对错误原因的解释。2) **验证器训练**：使用合成的批判数据冷启动强化学习过程，训练验证器。验证器学习根据模型生成的解和批判信息，给出一个验证分数。3) **解评估与聚合**：在测试时，对于每个候选解，验证器生成多个批判，并将这些批判聚合成一个验证分数。该分数用于加权投票或选择性拒绝回答。

**关键创新**：Mirror-Critique的关键创新在于引入了对比学习的思想，通过对比模型生成的解与真实解，为验证器提供了更丰富的批判信号。这种方法不仅能够提高验证器的准确性，还能够增强其识别自身能力边界的诚实性。与现有方法相比，Mirror-Critique不再仅仅依赖奖励模型，而是通过更细粒度的批判信息来指导验证器的学习。

**关键设计**：在批判数据合成阶段，使用了拒绝采样策略来保证批判数据的质量。具体来说，只有当生成的批判信息能够准确描述模型解的错误时，才会被保留。在验证器训练阶段，使用了强化学习算法，以最大化验证器对正确答案的验证分数，并最小化对错误答案的验证分数。此外，还设计了一种聚合策略，将多个批判信息聚合成一个最终的验证分数，以提高评估的鲁棒性。

## 📊 实验亮点

实验结果表明，Mirror-Verifier在解的准确性方面显著优于多数投票，尤其是在需要识别少数正确答案的场景下。此外，Mirror-Verifier还提高了求解器识别和拒绝回答超出其能力范围问题的诚实性，降低了模型给出错误答案的概率。具体的性能提升数据在论文中进行了详细的展示和分析。

## 🎯 应用场景

Mirror-Critique框架可应用于各种需要大语言模型进行推理和决策的场景，例如问答系统、代码生成、文本摘要等。通过提高模型推理的准确性和可靠性，该框架可以提升用户体验，并降低模型出错的风险。此外，该框架还可以用于评估和改进大语言模型的性能，促进其在更广泛领域的应用。

## 📄 摘要（原文）

> Test-time scaling via solution sampling and aggregation has become a key paradigm for improving the reasoning performance of Large Language Models (LLMs). While reward model selection is commonly employed in this approach, it often fails to identify minority-yet-correct answers, which limits its effectiveness beyond that of simple majority voting. We argue that this limitation stems from a lack of informative critique signals during verifier training. To bridge this gap, we introduce Mirror-Critique, a framework that trains a verifier with informative critiques. Our key insight is to leverage the rich critique signal by contrasting model-generated solutions with ground-truth solutions. We deploy a small instruction-tuned model to synthesize high-quality critique data with rejection sampling that teaches the verifier not only what is wrong, but also why. The synthetic data is used to cold-start the LLMs in the RLVR process to further improve the verification ability. The resulting Mirror-Verifier is deployed to evaluate candidate solutions by generating multiple critiques per solution, aggregating them into a verify score used for weighted voting or selective abstention. The experimental results show that our Mirror-Verifier significantly outperforms majority voting in terms of solution accuracy and also improves the solver's honesty to recognize and abstain from answering beyond its capability boundaries.

