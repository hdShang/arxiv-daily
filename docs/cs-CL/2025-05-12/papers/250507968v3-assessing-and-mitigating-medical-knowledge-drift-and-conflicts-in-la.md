---
layout: default
title: Assessing and Mitigating Medical Knowledge Drift and Conflicts in Large Language Models
---

# Assessing and Mitigating Medical Knowledge Drift and Conflicts in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07968" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07968v3</a>
  <a href="https://arxiv.org/pdf/2505.07968.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07968v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07968v3', 'Assessing and Mitigating Medical Knowledge Drift and Conflicts in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Weiyi Wu, Xinwen Xu, Chongyang Gao, Xingjian Diao, Siting Li, Lucas A. Salas, Jiang Gui

**分类**: cs.CL

**发布日期**: 2025-05-12 (更新: 2025-09-07)

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/RDBH)

---

## 💡 一句话要点

**提出DriftMedQA基准以解决医疗知识漂移问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗知识漂移` `大型语言模型` `临床指南` `DriftMedQA` `偏好微调` `增强检索生成` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在快速变化的医疗知识面前，容易产生过时或矛盾的治疗建议，影响临床决策的可靠性。
2. 论文提出了DriftMedQA基准，通过模拟临床指南的演变，评估LLMs在应对医疗知识漂移方面的表现，并探索缓解策略。
3. 实验结果表明，七种模型在4290个场景中表现不佳，组合使用两种缓解策略后，模型性能显著提升，结果更为一致可靠。

## 📝 摘要（中文）

大型语言模型（LLMs）在医疗领域具有巨大潜力，但在快速发展的医学知识面前面临重大挑战。这可能导致过时或矛盾的治疗建议。本研究调查了LLMs如何应对临床指南的演变，重点关注概念漂移和内部不一致性。我们开发了DriftMedQA基准来模拟指南演变，并评估了多种LLMs的时间可靠性。对七种最先进模型在4290个场景中的评估显示，它们在拒绝过时建议和经常支持矛盾指导方面存在困难。此外，我们探索了两种缓解策略：增强检索生成和通过直接偏好优化进行的偏好微调。尽管每种方法都提高了模型性能，但它们的组合产生了最一致和可靠的结果。这些发现强调了提高LLM对时间变化的鲁棒性的重要性，以确保在临床实践中的更可靠应用。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型语言模型在医疗知识快速演变中的适应性问题，现有方法在处理过时和矛盾建议时表现不佳。

**核心思路**：通过开发DriftMedQA基准，模拟临床指南的演变，评估模型的时间可靠性，并探索增强检索生成和偏好微调的组合策略。

**技术框架**：研究包括数据集构建、模型评估和缓解策略实施三个主要模块。首先构建DriftMedQA基准，然后对七种LLMs进行评估，最后应用两种缓解策略。

**关键创新**：最重要的创新在于提出了DriftMedQA基准，系统性地评估了LLMs在医疗知识漂移中的表现，并结合两种缓解策略以提高模型的鲁棒性。

**关键设计**：在偏好微调中采用直接偏好优化方法，结合增强检索生成技术，优化模型的输出质量和一致性。

## 📊 实验亮点

实验结果显示，七种最先进的模型在4290个场景中普遍存在拒绝过时建议的困难，且经常支持矛盾指导。通过结合增强检索生成和偏好微调，模型性能显著提升，结果更为一致可靠，展示了组合策略的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗决策支持系统、临床指南自动生成和医疗咨询服务。通过提高大型语言模型的鲁棒性，可以更好地适应快速变化的医疗环境，从而提升临床实践的可靠性和有效性。

## 📄 摘要（原文）

> Large Language Models (LLMs) have great potential in the field of health care, yet they face great challenges in adapting to rapidly evolving medical knowledge. This can lead to outdated or contradictory treatment suggestions. This study investigated how LLMs respond to evolving clinical guidelines, focusing on concept drift and internal inconsistencies. We developed the DriftMedQA benchmark to simulate guideline evolution and assessed the temporal reliability of various LLMs. Our evaluation of seven state-of-the-art models across 4,290 scenarios demonstrated difficulties in rejecting outdated recommendations and frequently endorsing conflicting guidance. Additionally, we explored two mitigation strategies: Retrieval-Augmented Generation and preference fine-tuning via Direct Preference Optimization. While each method improved model performance, their combination led to the most consistent and reliable results. These findings underscore the need to improve LLM robustness to temporal shifts to ensure more dependable applications in clinical practice. The dataset is available at https://huggingface.co/datasets/RDBH/DriftMed.

