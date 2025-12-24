---
layout: default
title: "RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning"
---

# RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.15034" class="toolbar-btn" target="_blank">📄 arXiv: 2505.15034v2</a>
  <a href="https://arxiv.org/pdf/2505.15034.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.15034v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.15034v2', 'RL Tango: Reinforcing Generator and Verifier Together for Language Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kaiwen Zha, Zhengqi Gao, Maohao Shen, Zhang-Wei Hong, Duane S. Boning, Dina Katabi

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-05-21 (更新: 2025-10-23)

**备注**: NeurIPS 2025. The first two authors contributed equally

**🔗 代码/项目**: [GITHUB](https://github.com/kaiwenzha/rl-tango)

---

## 💡 一句话要点

**提出Tango框架以解决LLM推理能力不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `语言模型` `推理能力` `生成式验证器` `互相强化` `数学基准` `过程级验证`

## 📋 核心要点

1. 现有的LLM后训练方法通常依赖固定的验证器，导致奖励黑客和泛化能力不足的问题。
2. Tango框架通过强化学习同时训练生成器和验证器，采用生成式验证器以增强互相强化的效果。
3. 实验结果显示，生成器在多个数学基准和推理任务中表现最佳，验证器在ProcessBench数据集上表现突出。

## 📝 摘要（中文）

强化学习（RL）最近成为增强大型语言模型（LLMs）推理能力的有效方法，其中LLM生成器作为由验证器（奖励模型）指导的策略。然而，现有的LLM后训练方法通常使用固定的验证器，容易受到奖励黑客攻击，并且在训练分布之外的泛化能力较差。为了解决这些问题，本文提出了Tango，一个新颖的框架，通过RL同时训练LLM生成器和验证器。Tango的核心创新在于其生成式的过程级LLM验证器，该验证器通过RL训练，并与生成器共同进化。验证器仅基于结果级验证正确性奖励进行训练，无需显式的过程级注释。实验表明，Tango的两个组件在7B/8B规模模型中均实现了最先进的结果，生成器在五个数学基准和四个具有挑战性的推理任务中表现优异，而验证器在ProcessBench数据集上领先。

## 🔬 方法详解

**问题定义**：本文旨在解决现有LLM后训练方法中验证器固定导致的奖励黑客和泛化能力不足的问题。现有方法通常依赖于规则基础或监督微调的验证器，限制了模型的适应性和鲁棒性。

**核心思路**：Tango框架的核心在于通过强化学习同时训练生成器和验证器，采用生成式的过程级验证器，使其与生成器共同进化，提升了模型的整体推理能力。

**技术框架**：Tango的整体架构包括生成器和验证器两个主要模块。生成器负责生成推理结果，而验证器则对生成的结果进行评估和反馈。两者通过强化学习的方式进行交互和优化。

**关键创新**：Tango的最重要创新在于其生成式的过程级验证器，该验证器通过强化学习训练，能够在没有显式过程级注释的情况下进行有效的结果验证。这一设计显著提高了验证器的鲁棒性和泛化能力。

**关键设计**：在设计中，验证器的训练仅依赖于结果级的验证正确性奖励，避免了对过程级注释的需求。此外，模型的参数设置和损失函数设计也经过精心调整，以确保生成器和验证器的有效协同训练。

## 📊 实验亮点

实验结果显示，Tango的生成器在五个数学基准测试中表现最佳，并在四个具有挑战性的推理任务中取得了领先地位。验证器在ProcessBench数据集上也表现突出，整体性能显著优于现有的基线方法，尤其在最困难的数学推理问题上取得了显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括教育、金融和科学研究等需要复杂推理的场景。通过提升LLM的推理能力，Tango框架可以帮助用户更高效地解决数学问题、进行数据分析和生成决策支持，从而在实际应用中创造更大的价值。

## 📄 摘要（原文）

> Reinforcement learning (RL) has recently emerged as a compelling approach for enhancing the reasoning capabilities of large language models (LLMs), where an LLM generator serves as a policy guided by a verifier (reward model). However, current RL post-training methods for LLMs typically use verifiers that are fixed (rule-based or frozen pretrained) or trained discriminatively via supervised fine-tuning (SFT). Such designs are susceptible to reward hacking and generalize poorly beyond their training distributions. To overcome these limitations, we propose Tango, a novel framework that uses RL to concurrently train both an LLM generator and a verifier in an interleaved manner. A central innovation of Tango is its generative, process-level LLM verifier, which is trained via RL and co-evolves with the generator. Importantly, the verifier is trained solely based on outcome-level verification correctness rewards without requiring explicit process-level annotations. This generative RL-trained verifier exhibits improved robustness and superior generalization compared to deterministic or SFT-trained verifiers, fostering effective mutual reinforcement with the generator. Extensive experiments demonstrate that both components of Tango achieve state-of-the-art results among 7B/8B-scale models: the generator attains best-in-class performance across five competition-level math benchmarks and four challenging out-of-domain reasoning tasks, while the verifier leads on the ProcessBench dataset. Remarkably, both components exhibit particularly substantial improvements on the most difficult mathematical reasoning problems. Code is at: https://github.com/kaiwenzha/rl-tango.

