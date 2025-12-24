---
layout: default
title: "QiMeng-CodeV-R1: Reasoning-Enhanced Verilog Generation"
---

# QiMeng-CodeV-R1: Reasoning-Enhanced Verilog Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24183" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24183v4</a>
  <a href="https://arxiv.org/pdf/2505.24183.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24183v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24183v4', 'QiMeng-CodeV-R1: Reasoning-Enhanced Verilog Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yaoyu Zhu, Di Huang, Hanqi Lyu, Xiaoyun Zhang, Chongxiao Li, Wenxuan Shi, Yutong Wu, Jianan Mu, Jinghua Wang, Yang Zhao, Pengwei Jin, Shuyao Cheng, Shengwen Liang, Xishan Zhang, Rui Zhang, Zidong Du, Qi Guo, Xing Hu, Yunji Chen

**分类**: cs.LG, cs.AR, cs.PL

**发布日期**: 2025-05-30 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出CodeV-R1框架以解决HDL自动生成中的验证挑战**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `电子设计自动化` `硬件描述语言` `自然语言处理` `强化学习` `数据合成` `模型蒸馏` `验证环境`

## 📋 核心要点

1. 现有方法在电子设计自动化中面临验证环境缺乏和高质量数据稀缺等挑战。
2. 提出了CodeV-R1框架，通过规则生成测试平台和往返数据合成来提高数据质量和验证能力。
3. 实验结果显示，CodeV-R1-7B在多个基准测试中超越了现有最先进模型，提升幅度达12~20%。

## 📝 摘要（中文）

大型语言模型（LLMs）通过可验证奖励的强化学习（RLVR）在软件编程和数学问题等任务上取得了突破。然而，将RLVR扩展到电子设计自动化（EDA），特别是从自然语言（NL）规范自动生成硬件描述语言（HDL）如Verilog，面临三个主要挑战：缺乏自动化和准确的验证环境、高质量NL-代码对的稀缺以及RLVR的高计算成本。为此，本文提出了CodeV-R1，一个用于训练Verilog生成LLMs的RLVR框架。我们开发了基于规则的测试平台生成器，提出了往返数据合成方法，并采用了两阶段的“蒸馏-再强化学习”训练流程。最终模型CodeV-R1-7B在VerilogEval v2和RTLLM v1.1上分别达到了68.6%和72.9%的通过率，超越了之前的最先进水平。

## 🔬 方法详解

**问题定义**：本文旨在解决在电子设计自动化中，从自然语言生成硬件描述语言（如Verilog）时的验证环境不足和高质量数据稀缺的问题。现有方法在这方面的有效性受到限制，导致生成的代码难以验证其正确性。

**核心思路**：论文提出的核心思路是通过开发一个规则基础的测试平台生成器和往返数据合成方法，来增强生成模型的验证能力和数据质量。这种设计旨在确保生成的代码与自然语言描述之间的一致性，从而提高生成的可靠性。

**技术框架**：整体架构包括三个主要模块：规则基础的测试平台生成器、往返数据合成方法和两阶段的“蒸馏-再强化学习”训练流程。测试平台生成器用于执行等价性检查，往返数据合成方法则用于生成高质量的NL-代码对。

**关键创新**：最重要的技术创新点在于提出了自适应采样率的RLVR算法（DAPO），该算法能够在训练过程中动态调整采样率，从而降低计算成本。这一创新与传统的RLVR方法相比，显著提高了训练效率。

**关键设计**：在模型训练中，采用了蒸馏技术来提升推理能力，并在后续阶段应用自适应的RLVR算法。关键参数设置和损失函数的设计也经过精心调整，以确保模型在生成Verilog代码时的准确性和一致性。

## 📊 实验亮点

实验结果表明，CodeV-R1-7B在VerilogEval v2和RTLLM v1.1基准测试中分别达到了68.6%和72.9%的通过率，超越了之前的最先进模型12~20%。该模型的性能甚至超过了671B参数的DeepSeek-R1，显示出其在HDL生成任务中的卓越能力。

## 🎯 应用场景

该研究的潜在应用领域包括电子设计自动化、硬件开发和智能系统设计。通过提高硬件描述语言的自动生成能力，能够显著降低开发成本和时间，提高设计效率，推动智能硬件的快速迭代与创新。

## 📄 摘要（原文）

> Large language models (LLMs) trained via reinforcement learning with verifiable reward (RLVR) have achieved breakthroughs on tasks with explicit, automatable verification, such as software programming and mathematical problems. Extending RLVR to electronic design automation (EDA), especially automatically generating hardware description languages (HDLs) like Verilog from natural-language (NL) specifications, however, poses three key challenges: the lack of automated and accurate verification environments, the scarcity of high-quality NL-code pairs, and the prohibitive computation cost of RLVR. To this end, we introduce CodeV-R1, an RLVR framework for training Verilog generation LLMs. First, we develop a rule-based testbench generator that performs robust equivalence checking against golden references. Second, we propose a round-trip data synthesis method that pairs open-source Verilog snippets with LLM-generated NL descriptions, verifies code-NL-code consistency via the generated testbench, and filters out inequivalent examples to yield a high-quality dataset. Third, we employ a two-stage "distill-then-RL" training pipeline: distillation for the cold start of reasoning abilities, followed by adaptive DAPO, our novel RLVR algorithm that can reduce training cost by adaptively adjusting sampling rate. The resulting model, CodeV-R1-7B, achieves 68.6% and 72.9% pass@1 on VerilogEval v2 and RTLLM v1.1, respectively, surpassing prior state-of-the-art by 12~20%, while even exceeding the performance of 671B DeepSeek-R1 on RTLLM. We have released our model, training code, and dataset to facilitate research in EDA and LLM communities.

