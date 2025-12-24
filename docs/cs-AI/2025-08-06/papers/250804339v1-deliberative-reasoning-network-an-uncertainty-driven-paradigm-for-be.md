---
layout: default
title: "Deliberative Reasoning Network: An Uncertainty-Driven Paradigm for Belief-Tracked Inference with Pretrained Language Models"
---

# Deliberative Reasoning Network: An Uncertainty-Driven Paradigm for Belief-Tracked Inference with Pretrained Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04339" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04339v1</a>
  <a href="https://arxiv.org/pdf/2508.04339.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04339v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04339v1', 'Deliberative Reasoning Network: An Uncertainty-Driven Paradigm for Belief-Tracked Inference with Pretrained Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Anran Xu, Jincheng Wang, Baigen Cai, Tao Wen

**分类**: cs.AI

**发布日期**: 2025-08-06

**备注**: 8 pages, 3 figures

---

## 💡 一句话要点

**提出DRN以解决大语言模型逻辑推理中的认知陷阱问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `逻辑推理` `不确定性最小化` `深思熟虑推理网络` `信念跟踪` `认知陷阱` `语言模型` `可解释性` `零-shot学习`

## 📋 核心要点

1. 现有的大型语言模型在逻辑推理时容易陷入认知陷阱，导致推理结果不可靠。
2. 本文提出的深思熟虑推理网络（DRN）通过不确定性最小化来改进逻辑推理，强调内部一致性证据的追踪。
3. 在LCR-1000基准测试中，DRN相较于标准基线提升了15.2%，并在与Mistral-7B集成后实现了显著的准确率提升。

## 📝 摘要（中文）

大型语言模型在逻辑推理中常常面临认知陷阱，即语义启发与决定性证据之间的冲突。为了解决这一根本性限制，本文提出了深思熟虑推理网络（DRN），该方法将逻辑推理从概率最大化重新框架为不确定性最小化。DRN通过迭代证据综合过程，明确跟踪信念状态并量化竞争假设的认知不确定性，从而实现内在可解释性。实验结果表明，DRN在新设计的LCR-1000基准上相较于标准基线提升了15.2%，并且与Mistral-7B集成后，在最具挑战性的问题上准确率从20%提升至80%。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在逻辑推理中面临的认知陷阱问题，即当语义启发与决定性证据冲突时，模型的推理能力受到限制。现有方法往往依赖于概率最大化，导致推理结果的不可靠性。

**核心思路**：DRN的核心思想是将逻辑推理的目标从概率最大化转变为不确定性最小化。通过这种方式，DRN能够更好地评估假设的内部一致性，从而提高推理的准确性和可靠性。

**技术框架**：DRN的整体架构包括两个主要模块：一个定制的判别模型，专注于不确定性最小化的核心原则；另一个轻量级验证模块，用于增强现有生成型语言模型的推理能力。

**关键创新**：DRN的主要创新在于其不确定性驱动的推理机制，通过明确跟踪信念状态和量化认知不确定性，提供了比传统方法更高的可解释性和可靠性。

**关键设计**：在技术细节上，DRN采用了迭代证据综合过程，设计了特定的损失函数以优化不确定性，并在网络结构上进行了调整，以支持信念状态的跟踪和更新。该设计使得DRN能够在推理过程中有效地整合和评估证据。

## 📊 实验亮点

DRN在新设计的LCR-1000基准测试中，相较于标准基线实现了高达15.2%的性能提升。此外，作为与Mistral-7B集成的参数高效验证器，DRN在最具挑战性的问题上将准确率从20%提升至80%。该方法还展示了强大的零-shot泛化能力，在TruthfulQA上提升了23.6%的表现，表明其学习到的推理原则具有可迁移性。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、自动推理和决策支持系统等。通过提高逻辑推理的可靠性，DRN能够为构建更可信赖的人工智能系统奠定基础，推动AI在复杂任务中的应用。未来，DRN的框架可能会被广泛应用于需要高水平推理能力的领域，如法律、医疗和金融等。

## 📄 摘要（原文）

> Large language models often fail at logical reasoning when semantic heuristics conflict with decisive evidence - a phenomenon we term cognitive traps. To address this fundamental limitation, we introduce the Deliberative Reasoning Network (DRN), a novel paradigm that reframes logical reasoning from probability maximization to uncertainty minimization. Instead of asking "Which answer is most likely?", DRN asks "Which hypothesis has the most internally consistent evidence?". DRN achieves intrinsic interpretability by explicitly tracking belief states and quantifying epistemic uncertainty for competing hypotheses through an iterative evidence synthesis process. We validate our approach through two complementary architectures - a bespoke discriminative model that embodies the core uncertainty minimization principle, and a lightweight verification module that enhances existing generative LLMs. Evaluated on LCR-1000, our new adversarial reasoning benchmark designed to expose cognitive traps, the bespoke DRN achieves up to 15.2% improvement over standard baselines. When integrated as a parameter-efficient verifier with Mistral-7B, our hybrid system boosts accuracy from 20% to 80% on the most challenging problems. Critically, DRN demonstrates strong zero-shot generalization, improving TruthfulQA performance by 23.6% without additional training, indicating that uncertainty-driven deliberation learns transferable reasoning principles. We position DRN as a foundational, verifiable System 2 reasoning component for building more trustworthy AI systems.

