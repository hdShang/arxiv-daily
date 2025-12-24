---
layout: default
title: "APO: Enhancing Reasoning Ability of MLLMs via Asymmetric Policy Optimization"
---

# APO: Enhancing Reasoning Ability of MLLMs via Asymmetric Policy Optimization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.21655" class="toolbar-btn" target="_blank">📄 arXiv: 2506.21655v1</a>
  <a href="https://arxiv.org/pdf/2506.21655.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.21655v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.21655v1', 'APO: Enhancing Reasoning Ability of MLLMs via Asymmetric Policy Optimization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Minjie Hong, Zirun Guo, Yan Xia, Zehan Wang, Ziang Zhang, Tao Jin, Zhou Zhao

**分类**: cs.LG, cs.AI, cs.CV

**发布日期**: 2025-06-26

**🔗 代码/项目**: [GITHUB](https://github.com/Indolent-Kawhi/View-R1)

---

## 💡 一句话要点

**提出不对称策略优化以提升多模态大语言模型的推理能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `推理能力` `强化学习` `不对称策略优化` `难度自适应散度调整` `次优轨迹复杂度正则化` `模型泛化` `复杂推理`

## 📋 核心要点

1. 现有的多模态大语言模型在复杂推理任务中表现不佳，强化学习的应用导致性能下降和过度推理现象。
2. 本文提出不对称策略优化（APO），通过将响应分为正负样本，动态调整KL散度权重以提高训练稳定性和利用率。
3. 实验表明，View-R1-3B模型在推理能力上平均提升7%，在多个基准测试中超越了7-11B的其他大型MLLMs。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在整合多样数据方面表现出色，但在复杂推理上常常面临挑战。尽管强化学习（RL）可以增强LLMs的推理能力，但在MLLMs中的应用却存在性能下降和过度推理等问题。本文提出不对称策略优化（APO），通过将采样响应分为正负两组，利用难度自适应散度调整（DADS）和次优轨迹复杂度正则化（STCR）来解决这些问题。实验结果表明，应用APO的View-R1-3B模型在推理能力上平均提升7%，并在多个推理基准上超越了更大的MLLMs，同时保持了对一般任务的良好表现。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大语言模型在复杂推理任务中的性能下降和过度推理问题。现有方法在应用强化学习时，常导致模型在一般任务上的表现不佳。

**核心思路**：提出不对称策略优化（APO），将采样响应分为正负两组。对正样本应用难度自适应散度调整（DADS），动态调整KL散度权重；对负样本应用次优轨迹复杂度正则化（STCR），以减少过度推理。

**技术框架**：APO的整体架构包括两个主要模块：正样本处理模块和负样本处理模块。正样本通过DADS进行动态调整，负样本则通过STCR进行复杂度控制。

**关键创新**：DADS和STCR是本文的核心创新，DADS通过动态调整KL散度权重来提高训练稳定性，而STCR则通过惩罚过长的响应来鼓励简洁推理。这与现有方法的本质区别在于更好地平衡了探索与利用。

**关键设计**：在DADS中，KL散度权重根据样本难度动态调整；在STCR中，设计了惩罚机制以限制响应长度。这些设计确保了模型在保持已有知识的同时，能够有效进行推理。

## 📊 实验亮点

实验结果显示，View-R1-3B模型在推理能力上平均提升7%，并在多个推理基准测试中超越了7-11B的其他大型多模态大语言模型，且在一般任务上保持了良好的性能，展示了其优越的泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动内容生成和多模态数据分析等。通过提升多模态大语言模型的推理能力，能够更好地处理复杂的用户查询和任务，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) are powerful at integrating diverse data, but they often struggle with complex reasoning. While Reinforcement learning (RL) can boost reasoning in LLMs, applying it to MLLMs is tricky. Common issues include a drop in performance on general tasks and the generation of overly detailed or "overthinking" reasoning. Our work investigates how the KL penalty and overthinking affect RL training in MLLMs. We propose Asymmetric Policy Optimization (APO) to address these issues, which divides the sampled responses into positive and negative groups. For positive samples, Difficulty-Adaptive Divergence Shaping (DADS) is introduced to dynamically adjust the KL divergence weight based on their difficulty. This method prevents policy entropy from dropping sharply, improves training stability, utilizes samples better, and preserves the model's existing knowledge. For negative samples, Suboptimal Trajectory Complexity Regularization (STCR) is proposed to penalize overly long responses. This helps mitigate overthinking and encourages more concise reasoning while preserving the model's explorative capacity. We apply our method to Qwen2.5-VL-3B, creating View-R1-3B. View-R1-3B significantly enhances reasoning capabilities, showing an average 7\% gain over the base model and outperforming larger MLLMs (7-11B) on various reasoning benchmarks. Importantly, unlike other reasoning-tuned MLLMs that often degrade on general tasks, View-R1-3B maintains consistent improvement, demonstrating superior generalization. These results highlight the effectiveness and broad applicability of our DADS and STCR techniques for advancing complex multimodal reasoning in MLLMs. The code will be made available at https://github.com/Indolent-Kawhi/View-R1.

