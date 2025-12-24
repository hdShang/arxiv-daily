---
layout: default
title: "Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning"
---

# Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15279" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15279v1</a>
  <a href="https://arxiv.org/pdf/2509.15279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15279v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15279v1', 'Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chi Liu, Derek Li, Yan Shu, Robin Chen, Derek Duan, Teng Fang, Bryan Dai

**分类**: cs.LG, cs.CL

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**Fleming-R1：通过强化学习实现专家级医学推理**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学推理` `强化学习` `知识图谱` `思维链` `临床决策支持`

## 📋 核心要点

1. 现有医学AI模型在临床推理中面临挑战，需要兼顾准确性和推理过程的透明性。
2. Fleming-R1通过RODS数据策略、CoT冷启动和RLVR框架，提升模型的可验证医学推理能力。
3. 实验结果表明，Fleming-R1在多个医学基准测试中超越了大型基线模型，接近GPT-4o的性能。

## 📝 摘要（中文）

大型语言模型在医学应用中展现出潜力，但由于需要准确的答案和透明的推理过程，实现专家级临床推理仍然具有挑战性。为了解决这个问题，我们引入了Fleming-R1模型，该模型通过三个互补的创新设计来实现可验证的医学推理。首先，我们的面向推理的数据策略（RODS）结合了精选的医学问答数据集和知识图谱引导的合成数据，以提高对代表性不足的疾病、药物和多跳推理链的覆盖。其次，我们采用思维链（CoT）冷启动来从教师模型中提炼高质量的推理轨迹，从而建立稳健的推理先验。第三，我们使用群体相对策略优化实施了一个两阶段的可验证奖励强化学习（RLVR）框架，该框架巩固了核心推理技能，同时通过自适应硬样本挖掘来针对持续存在的失败模式。在各种医学基准测试中，Fleming-R1提供了显著的参数高效改进：7B变体超过了更大的基线模型，而32B模型实现了与GPT-4o接近的性能，并且始终优于强大的开源替代方案。这些结果表明，结构化数据设计、面向推理的初始化和可验证的强化学习可以推动临床推理超越简单的准确性优化。我们公开发布Fleming-R1，以促进医学AI中透明、可重复和可审计的进展，从而在高度敏感的临床环境中实现更安全的部署。

## 🔬 方法详解

**问题定义**：现有医学AI模型，特别是大型语言模型，虽然在医学问答方面取得进展，但缺乏专家级别的临床推理能力。主要痛点在于：1）对罕见疾病、药物和复杂推理链的覆盖不足；2）推理过程不透明，难以验证；3）难以从错误中学习，持续改进。

**核心思路**：Fleming-R1的核心思路是通过结构化的数据设计、面向推理的初始化和可验证的强化学习，提升模型的推理能力和透明度。通过知识图谱增强数据，模仿专家推理过程，并利用强化学习从可验证的奖励中学习，从而实现更可靠的临床推理。

**技术框架**：Fleming-R1的技术框架包含三个主要部分：1）**面向推理的数据策略（RODS）**：结合医学QA数据集和知识图谱，生成更全面的训练数据。2）**思维链（CoT）冷启动**：从教师模型中提炼高质量的推理轨迹，作为模型的初始推理能力。3）**可验证奖励强化学习（RLVR）**：使用群体相对策略优化，通过可验证的奖励信号，巩固核心推理技能，并针对失败模式进行优化。

**关键创新**：Fleming-R1的关键创新在于其RLVR框架，该框架使用可验证的奖励信号，而非简单的准确率，来训练模型。这种方法允许模型学习更可靠的推理过程，并针对特定的失败模式进行优化。此外，RODS数据策略通过知识图谱增强数据，解决了罕见病例和复杂推理链的覆盖问题。

**关键设计**：RODS数据策略使用知识图谱来识别和生成缺乏代表性的疾病、药物和推理路径的合成数据。CoT冷启动使用教师模型生成高质量的推理轨迹，并将其作为模型的初始推理能力。RLVR框架使用群体相对策略优化，通过比较不同推理路径的奖励，来训练模型。具体的奖励函数设计和硬样本挖掘策略是影响模型性能的关键因素，但论文中未详细说明具体参数设置，属于未知。

## 📊 实验亮点

Fleming-R1在多个医学基准测试中表现出色。7B变体超越了更大的基线模型，而32B模型实现了与GPT-4o接近的性能，并且始终优于强大的开源替代方案。这些结果表明，通过结构化数据设计、面向推理的初始化和可验证的强化学习，可以显著提升医学AI模型的推理能力。

## 🎯 应用场景

Fleming-R1具有广泛的潜在应用领域，包括辅助诊断、药物研发、临床决策支持等。通过提供透明、可验证的推理过程，该模型可以帮助医生做出更明智的决策，提高医疗质量，并降低医疗风险。未来，该模型有望成为医疗领域的重要工具，促进医学AI的进步。

## 📄 摘要（原文）

> While large language models show promise in medical applications, achieving expert-level clinical reasoning remains challenging due to the need for both accurate answers and transparent reasoning processes. To address this challenge, we introduce Fleming-R1, a model designed for verifiable medical reasoning through three complementary innovations. First, our Reasoning-Oriented Data Strategy (RODS) combines curated medical QA datasets with knowledge-graph-guided synthesis to improve coverage of underrepresented diseases, drugs, and multi-hop reasoning chains. Second, we employ Chain-of-Thought (CoT) cold start to distill high-quality reasoning trajectories from teacher models, establishing robust inference priors. Third, we implement a two-stage Reinforcement Learning from Verifiable Rewards (RLVR) framework using Group Relative Policy Optimization, which consolidates core reasoning skills while targeting persistent failure modes through adaptive hard-sample mining. Across diverse medical benchmarks, Fleming-R1 delivers substantial parameter-efficient improvements: the 7B variant surpasses much larger baselines, while the 32B model achieves near-parity with GPT-4o and consistently outperforms strong open-source alternatives. These results demonstrate that structured data design, reasoning-oriented initialization, and verifiable reinforcement learning can advance clinical reasoning beyond simple accuracy optimization. We release Fleming-R1 publicly to promote transparent, reproducible, and auditable progress in medical AI, enabling safer deployment in high-stakes clinical environments.

