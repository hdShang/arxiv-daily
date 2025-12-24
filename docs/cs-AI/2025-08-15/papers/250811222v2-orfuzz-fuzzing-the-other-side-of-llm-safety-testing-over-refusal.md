---
layout: default
title: "ORFuzz: Fuzzing the \"Other Side\" of LLM Safety -- Testing Over-Refusal"
---

# ORFuzz: Fuzzing the "Other Side" of LLM Safety -- Testing Over-Refusal

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.11222" class="toolbar-btn" target="_blank">📄 arXiv: 2508.11222v2</a>
  <a href="https://arxiv.org/pdf/2508.11222.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.11222v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.11222v2', 'ORFuzz: Fuzzing the &quot;Other Side&quot; of LLM Safety -- Testing Over-Refusal')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haonan Zhang, Dongxia Wang, Yi Liu, Kexin Chen, Jiashui Wang, Xinlei Ying, Long Liu, Wenhai Wang

**分类**: cs.SE, cs.AI, cs.CL, cs.IR

**发布日期**: 2025-08-15 (更新: 2025-12-05)

**备注**: Accepted by ASE 2025

---

## 💡 一句话要点

**提出ORFuzz框架以解决大语言模型的过度拒绝问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大语言模型` `过度拒绝` `安全性测试` `进化测试` `自动化测试` `人类对齐评判` `测试生成` `人工智能`

## 📋 核心要点

1. 当前方法无法有效测试大语言模型的过度拒绝现象，存在基准测试缺陷和测试生成能力不足的问题。
2. 本文提出的ORFuzz框架通过安全类别感知的种子选择和自适应变异优化，系统性地检测LLM的过度拒绝。
3. 实验结果显示，ORFuzz生成的过度拒绝实例速率达到6.98%，是现有基线的两倍，且新基准ORFuzzSet在10个不同LLM上表现优异。

## 📝 摘要（中文）

大语言模型（LLMs）越来越多地表现出过度拒绝现象，即由于过于保守的安全措施错误地拒绝良性查询，这一关键功能缺陷削弱了它们的可靠性和可用性。现有测试方法明显不足，存在基准测试缺陷和有限的测试生成能力。本文首次提出了进化测试框架ORFuzz，系统检测和分析LLM的过度拒绝。ORFuzz独特地整合了三个核心组件：安全类别感知的种子选择、使用推理LLM的自适应变异优化以及经过验证的OR-Judge人类对齐评判模型。我们的评估表明，ORFuzz生成的过度拒绝实例的速率超过领先基线的两倍，形成了新的基准ORFuzzSet，包含1855个高度可转移的测试用例，显著提升了现有数据集的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在安全性过度保守下导致的过度拒绝问题。现有方法在测试此类行为时存在基准不完善和测试生成能力有限的痛点。

**核心思路**：ORFuzz框架通过结合安全类别感知的种子选择、自适应变异优化和人类对齐的评判模型，系统性地检测和分析过度拒绝现象，以提高测试的全面性和有效性。

**技术框架**：ORFuzz的整体架构包括三个主要模块：安全类别感知的种子选择模块、使用推理LLM的自适应变异优化模块和OR-Judge评判模型。这些模块协同工作，以生成多样化的测试用例并评估其有效性。

**关键创新**：ORFuzz的核心创新在于其综合性测试框架，特别是引入了人类对齐的评判模型OR-Judge，以准确反映用户对毒性和拒绝的感知，这在现有方法中尚属首次。

**关键设计**：在设计中，种子选择基于安全类别，变异优化通过推理LLM进行，OR-Judge模型经过验证以确保其评判的准确性。这些设计确保了测试用例的有效性和多样性。

## 📊 实验亮点

实验结果表明，ORFuzz生成的过度拒绝实例的平均速率为6.98%，是领先基线的两倍，且新基准ORFuzzSet在10个不同LLM上的平均过度拒绝率达到63.56%，显著优于现有数据集，展示了其有效性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括大语言模型的安全性测试、人工智能系统的可靠性评估以及相关软件开发。ORFuzz框架为开发更可靠和可信赖的LLM基础软件系统提供了重要工具，未来可能推动更广泛的AI应用和标准化测试流程。

## 📄 摘要（原文）

> Large Language Models (LLMs) increasingly exhibit over-refusal - erroneously rejecting benign queries due to overly conservative safety measures - a critical functional flaw that undermines their reliability and usability. Current methods for testing this behavior are demonstrably inadequate, suffering from flawed benchmarks and limited test generation capabilities, as highlighted by our empirical user study. To the best of our knowledge, this paper introduces the first evolutionary testing framework, ORFuzz, for the systematic detection and analysis of LLM over-refusals. ORFuzz uniquely integrates three core components: (1) safety category-aware seed selection for comprehensive test coverage, (2) adaptive mutator optimization using reasoning LLMs to generate effective test cases, and (3) OR-Judge, a human-aligned judge model validated to accurately reflect user perception of toxicity and refusal. Our extensive evaluations demonstrate that ORFuzz generates diverse, validated over-refusal instances at a rate (6.98% average) more than double that of leading baselines, effectively uncovering vulnerabilities. Furthermore, ORFuzz's outputs form the basis of ORFuzzSet, a new benchmark of 1,855 highly transferable test cases that achieves a superior 63.56% average over-refusal rate across 10 diverse LLMs, significantly outperforming existing datasets. ORFuzz and ORFuzzSet provide a robust automated testing framework and a valuable community resource, paving the way for developing more reliable and trustworthy LLM-based software systems.

