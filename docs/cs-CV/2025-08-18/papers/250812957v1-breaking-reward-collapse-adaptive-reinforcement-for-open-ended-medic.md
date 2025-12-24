---
layout: default
title: "Breaking Reward Collapse: Adaptive Reinforcement for Open-ended Medical Reasoning with Enhanced Semantic Discrimination"
---

# Breaking Reward Collapse: Adaptive Reinforcement for Open-ended Medical Reasoning with Enhanced Semantic Discrimination

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12957" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12957v1</a>
  <a href="https://arxiv.org/pdf/2508.12957.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12957v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12957v1', 'Breaking Reward Collapse: Adaptive Reinforcement for Open-ended Medical Reasoning with Enhanced Semantic Discrimination')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yizhou Liu, Jingwei Wei, Zizhi Chen, Minghao Han, Xukun Zhang, Keliang Liu, Lihua Zhang

**分类**: cs.CV

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出ARMed以解决医疗推理中的奖励崩溃问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `强化学习` `医学推理` `视觉问答` `自适应奖励` `语义区分` `模型泛化` `临床应用`

## 📋 核心要点

1. 现有的强化学习方法在医学影像领域应用不足，尤其是在开放式医疗视觉问答中，导致临床推理能力受限。
2. 本文提出ARMed框架，通过监督微调引入领域知识，并结合自适应语义奖励，提升推理的准确性和质量。
3. ARMed在六个医学VQA基准上表现优异，域内任务准确率提升32.64%，域外基准提升11.65%，验证了奖励可区分性的重要性。

## 📝 摘要（中文）

基于规则的奖励的强化学习（RL）在提升视觉语言模型（VLMs）和大型语言模型（LLMs）的推理与泛化能力方面展现出强大潜力，但在医学影像领域的应用仍然较少。现有的强化微调方法主要集中于封闭式视觉问答（VQA），限制了其在真实临床推理中的适用性。为此，本文提出了一种新颖的RL框架ARMed（Adaptive Reinforcement for Medical Reasoning），通过在链式思维数据上进行监督微调（SFT），结合文本正确性和自适应语义奖励的强化学习，显著提升了推理质量。实验结果表明，ARMed在六个具有挑战性的医学VQA基准上均表现出色，域内任务准确率提升32.64%，域外基准提升11.65%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有医学影像领域强化学习方法在开放式视觉问答中面临的奖励崩溃问题，现有方法多集中于封闭式视觉问答，限制了其实际应用。

**核心思路**：ARMed框架通过在链式思维数据上进行监督微调，结合文本正确性和自适应语义奖励，旨在提升模型的推理质量和泛化能力。

**技术框架**：ARMed的整体架构包括两个主要阶段：首先进行监督微调以引入领域知识，然后应用强化学习以优化模型的推理能力。

**关键创新**：ARMed的核心创新在于引入自适应语义奖励机制，解决了传统模型在语义奖励中出现的崩溃现象，使得语义差异显著的响应能够获得不同的评分。

**关键设计**：在设计中，ARMed采用了特定的损失函数以平衡文本正确性与语义奖励，并在网络结构上进行了优化，以确保模型能够有效学习和推理。

## 📊 实验亮点

ARMed在六个医学VQA基准上取得了显著的实验结果，域内任务准确率提升32.64%，域外基准提升11.65%。这些结果表明，ARMed在提升模型推理能力和泛化能力方面具有显著优势，验证了自适应语义奖励的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、临床决策支持系统和智能医疗助手等。通过提升模型在开放式医疗视觉问答中的表现，ARMed有望在实际临床环境中提供更为精准和可靠的推理支持，推动智能医疗的发展。

## 📄 摘要（原文）

> Reinforcement learning (RL) with rule-based rewards has demonstrated strong potential in enhancing the reasoning and generalization capabilities of vision-language models (VLMs) and large language models (LLMs), while reducing computational overhead. However, its application in medical imaging remains underexplored. Existing reinforcement fine-tuning (RFT) approaches in this domain primarily target closed-ended visual question answering (VQA), limiting their applicability to real-world clinical reasoning. In contrast, open-ended medical VQA better reflects clinical practice but has received limited attention. While some efforts have sought to unify both formats via semantically guided RL, we observe that model-based semantic rewards often suffer from reward collapse, where responses with significant semantic differences receive similar scores. To address this, we propose ARMed (Adaptive Reinforcement for Medical Reasoning), a novel RL framework for open-ended medical VQA. ARMed first incorporates domain knowledge through supervised fine-tuning (SFT) on chain-of-thought data, then applies reinforcement learning with textual correctness and adaptive semantic rewards to enhance reasoning quality. We evaluate ARMed on six challenging medical VQA benchmarks. Results show that ARMed consistently boosts both accuracy and generalization, achieving a 32.64% improvement on in-domain tasks and an 11.65% gain on out-of-domain benchmarks. These results highlight the critical role of reward discriminability in medical RL and the promise of semantically guided rewards for enabling robust and clinically meaningful multimodal reasoning.

