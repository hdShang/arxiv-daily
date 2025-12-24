---
layout: default
title: X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains
---

# X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.03981" class="toolbar-btn" target="_blank">📄 arXiv: 2505.03981v1</a>
  <a href="https://arxiv.org/pdf/2505.03981.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.03981v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.03981v1', 'X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianchu Liu, Sheng Zhang, Guanghui Qin, Timothy Ossowski, Yu Gu, Ying Jin, Sid Kiblawi, Sam Preston, Mu Wei, Paul Vozila, Tristan Naumann, Hoifung Poon

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-05-06

---

## 💡 一句话要点

**提出X-Reasoner以解决多模态与领域间推理能力不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态推理` `领域泛化` `视觉-语言模型` `强化学习` `监督微调` `医疗应用` `文本后训练`

## 📋 核心要点

1. 现有方法主要集中于文本推理，缺乏有效的多模态和领域间推理能力。
2. 提出X-Reasoner，通过基于一般领域文本的后训练，实现跨模态和领域的推理泛化。
3. 实验结果显示，X-Reasoner在多个一般和医疗基准上超越了现有最先进模型，且在特定领域的表现可通过继续训练进一步提升。

## 📝 摘要（中文）

近年来，一些专有模型（如o3）展示了强大的多模态推理能力。然而，现有的开源研究主要集中于文本推理模型的训练，评估也主要限于数学和一般领域任务。因此，如何有效扩展推理能力超越文本输入和一般领域仍不明确。本文探讨了一个基本研究问题：推理是否可以跨模态和领域进行泛化？我们的研究结果支持肯定的答案：基于一般领域文本的后训练可以实现强大的可泛化推理。基于此，我们提出了X-Reasoner，一个仅基于一般领域文本后训练的视觉-语言模型，采用两阶段方法：初始的监督微调阶段结合蒸馏的长链思维，随后进行可验证奖励的强化学习。实验表明，X-Reasoner成功地将推理能力转移到多模态和超领域设置，超越了现有的在领域内和多模态数据上训练的最先进模型。

## 🔬 方法详解

**问题定义**：本文旨在解决现有推理模型在多模态和领域间推理能力不足的问题。现有方法多集中于文本推理，缺乏跨模态的有效性和泛化能力。

**核心思路**：论文提出的核心思路是通过基于一般领域文本的后训练，利用监督微调和强化学习相结合的方式，提升模型的推理能力，实现跨模态和领域的泛化。

**技术框架**：X-Reasoner的整体架构包括两个主要阶段：首先是监督微调阶段，使用蒸馏的长链思维进行训练；其次是强化学习阶段，通过可验证的奖励机制进一步优化模型性能。

**关键创新**：X-Reasoner的关键创新在于其基于一般领域文本的后训练方法，能够有效地将推理能力迁移到多模态和超领域设置，显著提升了模型的泛化能力。

**关键设计**：在训练过程中，采用了蒸馏长链思维的策略，结合特定的损失函数和网络结构设计，以确保模型在推理任务中的有效性和准确性。

## 📊 实验亮点

实验结果表明，X-Reasoner在多个一般和医疗基准上超越了现有最先进模型，尤其是在特定领域的推理任务中表现出色。具体而言，X-Reasoner在医疗基准上实现了新的最优性能，显示出其在领域特定任务中的强大能力。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、跨模态信息检索以及智能问答系统等。通过提升模型的推理能力，X-Reasoner能够在多种实际场景中提供更为准确和高效的解决方案，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Recent proprietary models (e.g., o3) have begun to demonstrate strong multimodal reasoning capabilities. Yet, most existing open-source research concentrates on training text-only reasoning models, with evaluations limited to mainly mathematical and general-domain tasks. Therefore, it remains unclear how to effectively extend reasoning capabilities beyond text input and general domains. This paper explores a fundamental research question: Is reasoning generalizable across modalities and domains? Our findings support an affirmative answer: General-domain text-based post-training can enable such strong generalizable reasoning. Leveraging this finding, we introduce X-Reasoner, a vision-language model post-trained solely on general-domain text for generalizable reasoning, using a two-stage approach: an initial supervised fine-tuning phase with distilled long chain-of-thoughts, followed by reinforcement learning with verifiable rewards. Experiments show that X-Reasoner successfully transfers reasoning capabilities to both multimodal and out-of-domain settings, outperforming existing state-of-the-art models trained with in-domain and multimodal data across various general and medical benchmarks (Figure 1). Additionally, we find that X-Reasoner's performance in specialized domains can be further enhanced through continued training on domain-specific text-only data. Building upon this, we introduce X-Reasoner-Med, a medical-specialized variant that achieves new state of the art on numerous text-only and multimodal medical benchmarks.

