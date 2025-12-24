---
layout: default
title: "CARFT: Boosting LLM Reasoning via Contrastive Learning with Annotated Chain-of-Thought-based Reinforced Fine-Tuning"
---

# CARFT: Boosting LLM Reasoning via Contrastive Learning with Annotated Chain-of-Thought-based Reinforced Fine-Tuning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15868" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15868v2</a>
  <a href="https://arxiv.org/pdf/2508.15868.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15868v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15868v2', 'CARFT: Boosting LLM Reasoning via Contrastive Learning with Annotated Chain-of-Thought-based Reinforced Fine-Tuning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenqiao Zhu, Ji Liu, Rongjuncheng Zhang, Haipang Wu, Yulun Zhang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-21 (更新: 2025-09-08)

**备注**: 14 pages, to appear in EMNLP25

**🔗 代码/项目**: [GITHUB](https://github.com/WNQzhu/CARFT)

---

## 💡 一句话要点

**提出CARFT以解决大语言模型推理能力不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `推理能力` `对比学习` `强化学习` `思维链` `微调方法` `自然语言处理`

## 📋 核心要点

1. 现有的强化学习微调方法忽视了带注释的思维链，导致模型训练不稳定和性能下降。
2. 本文提出了一种新的对比学习与带注释思维链结合的强化微调方法，旨在充分利用注释信息并稳定训练过程。
3. 实验结果表明，CARFT在鲁棒性和性能上显著优于三种基线方法，性能提升高达10.15%。

## 📝 摘要（中文）

推理能力在大语言模型（LLMs）的广泛应用中扮演着至关重要的角色。为提升LLMs的推理性能，研究者们提出了多种基于强化学习（RL）的微调方法，以解决仅通过监督微调（SFT）训练的LLMs的有限泛化能力。然而，现有方法存在两个主要限制：一是传统的RL方法忽视了带注释的思维链（CoT），并采用不稳定的推理路径采样，导致模型崩溃和训练过程不稳定；二是现有的SFT方法过于强调注释的CoT，可能因未充分利用潜在CoT而导致性能下降。为此，本文提出了一种基于带注释CoT的对比学习强化微调方法CARFT，旨在提升LLMs的推理性能，同时克服上述限制。我们通过全面的实验和深入分析，展示了CARFT在鲁棒性、性能（提升高达10.15%）和效率（提升高达30.62%）方面的显著优势。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型推理能力不足的问题，现有方法在利用带注释的思维链时存在不稳定性和性能下降的风险。

**核心思路**：提出了一种结合对比学习与带注释思维链的强化微调方法，通过学习每个思维链的表示，设计新的对比信号来指导微调过程。

**技术框架**：整体架构包括两个主要模块：带注释思维链的表示学习和对比信号的生成与应用。首先，模型学习思维链的表示，然后利用这些表示生成对比信号以稳定训练过程。

**关键创新**：最重要的创新在于通过对比学习充分利用带注释的思维链，同时引入额外的无监督学习信号以增强训练稳定性，这与传统方法的单一依赖注释信息形成鲜明对比。

**关键设计**：在损失函数设计上，结合了对比损失和强化学习信号，确保模型在微调过程中能够有效利用注释信息和潜在的思维链。

## 📊 实验亮点

实验结果显示，CARFT在鲁棒性和性能方面显著优于三种基线方法，性能提升高达10.15%，效率提升高达30.62%。这些结果表明，CARFT在实际应用中具有较强的竞争力和实用价值。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能问答系统和对话生成等。通过提升大语言模型的推理能力，CARFT可以在多种实际场景中提供更为准确和可靠的结果，推动智能助手和自动化系统的发展。

## 📄 摘要（原文）

> Reasoning capability plays a significantly critical role in the the broad applications of Large Language Models (LLMs). To enhance the reasoning performance of LLMs, diverse Reinforcement Learning (RL)-based fine-tuning approaches have been proposed to address the limited generalization capability of LLMs trained solely via Supervised Fine-Tuning (SFT). Despite their effectiveness, two major limitations hinder the advancement of LLMs. First, vanilla RL-based approaches ignore annotated Chain-of-Thought (CoT) and incorporate unstable reasoning path sampling, which typically results in model collapse, unstable training process, and suboptimal performance. Second, existing SFT approaches generally overemphasize the annotated CoT, potentially leading to performance degradation due to insufficient exploitation of potential CoT. In this paper, we propose a Contrastive learning with annotated CoT-based Reinforced Fine-Tuning approach, i.e., \TheName{}, to enhance the reasoning performance of LLMs while addressing the aforementioned limitations. Specifically, we propose learning a representation for each CoT. Based on this representation, we design novel contrastive signals to guide the fine-tuning process. Our approach not only fully exploits the available annotated CoT but also stabilizes the fine-tuning procedure by incorporating an additional unsupervised learning signal. We conduct comprehensive experiments and in-depth analysis with three baseline approaches, two foundation models, and two datasets to demonstrate significant advantages of \TheName{} in terms of robustness, performance (up to 10.15\%), and efficiency (up to 30.62\%). Code is available at https://github.com/WNQzhu/CARFT.

