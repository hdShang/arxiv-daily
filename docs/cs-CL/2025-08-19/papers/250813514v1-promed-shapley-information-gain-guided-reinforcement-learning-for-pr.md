---
layout: default
title: "ProMed: Shapley Information Gain Guided Reinforcement Learning for Proactive Medical LLMs"
---

# ProMed: Shapley Information Gain Guided Reinforcement Learning for Proactive Medical LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13514" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13514v1</a>
  <a href="https://arxiv.org/pdf/2508.13514.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13514v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13514v1', 'ProMed: Shapley Information Gain Guided Reinforcement Learning for Proactive Medical LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hongxin Ding, Baixiang Huang, Yue Fang, Weibin Liao, Xinke Jiang, Zheng Li, Junfeng Zhao, Yasha Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-19

---

## 💡 一句话要点

**提出ProMed以解决医疗LLMs反应性不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗语言模型` `主动提问` `强化学习` `信息增益` `临床决策`

## 📋 核心要点

1. 现有医疗LLMs在互动式问答中主要依赖反应性生成，缺乏主动提问能力，可能导致诊断错误。
2. ProMed通过强化学习框架，结合Shapley信息增益，赋予医疗LLMs主动提问的能力，以提高临床决策质量。
3. 在两个新创建的医疗基准上，ProMed的表现优于最先进的方法，平均提升6.29%，并在反应性模式下实现54.45%的增益。

## 📝 摘要（中文）

在现实临床咨询中，互动式医疗提问至关重要，医生需主动收集患者信息。尽管医疗大型语言模型（LLMs）在静态问答中表现出色，但它们主要处于反应性模式，直接生成答案而不主动寻求额外信息，这在互动环境中可能导致错误诊断。为了解决这一局限性，本文提出了ProMed，一个强化学习框架，使医疗LLMs转向主动模式，具备在决策前提出临床有价值问题的能力。ProMed的核心是Shapley信息增益（SIG）奖励，通过结合新获得信息量和其上下文重要性来量化每个问题的临床效用。实验结果表明，ProMed在两个新创建的部分信息医疗基准上显著优于现有方法，平均提升6.29%，并在反应性模式上实现54.45%的增益。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗LLMs在互动式问答中反应性不足的问题，现有方法无法主动询问患者信息，导致潜在的错误诊断。

**核心思路**：ProMed通过强化学习框架，利用Shapley信息增益（SIG）奖励机制，鼓励模型在决策前主动提问，从而提高临床决策的准确性和有效性。

**技术框架**：ProMed的整体架构包括两个主要阶段：第一阶段是SIG引导的模型初始化，使用蒙特卡洛树搜索（MCTS）构建高奖励的交互轨迹来监督模型；第二阶段是SIG增强的策略优化，结合SIG并通过新颖的SIG引导奖励分配机制优化模型。

**关键创新**：ProMed的核心创新在于引入Shapley信息增益作为奖励机制，量化问题的临床效用，与现有方法相比，能够更有效地引导模型进行有价值的提问。

**关键设计**：在模型训练中，SIG奖励机制通过评估问题的重要性和新信息量来分配奖励，确保模型优先学习提出信息丰富的问题，同时结合强化学习的策略优化方法，提升模型的整体性能。

## 📊 实验亮点

在实验中，ProMed在两个新创建的部分信息医疗基准上表现优异，平均提升6.29%，并在反应性模式下实现54.45%的增益，显示出其在主动提问能力上的显著优势，超越了现有的最先进方法。

## 🎯 应用场景

ProMed的研究成果在医疗领域具有广泛的应用潜力，能够提升医生在临床咨询中的决策质量。通过主动提问，医疗LLMs可以更有效地收集患者信息，从而提高诊断的准确性和治疗效果。未来，ProMed有望在远程医疗、智能问诊系统等场景中发挥重要作用，推动医疗服务的智能化和个性化发展。

## 📄 摘要（原文）

> Interactive medical questioning is essential in real-world clinical consultations, where physicians must actively gather information from patients. While medical Large Language Models (LLMs) have shown impressive capabilities in static medical question answering, they predominantly operate under a reactive paradigm: generating answers directly without seeking additional information, which risks incorrect diagnoses in such interactive settings. To address this limitation, we propose ProMed, a reinforcement learning (RL) framework that transitions medical LLMs toward a proactive paradigm, equipping them with the ability to ask clinically valuable questions before decision-making. At the core of ProMed is the Shapley Information Gain (SIG) reward, which quantifies the clinical utility of each question by combining the amount of newly acquired information with its contextual importance, estimated via Shapley values. We integrate SIG into a two-stage training pipeline: (1) SIG-Guided Model Initialization uses Monte Carlo Tree Search (MCTS) to construct high-reward interaction trajectories to supervise the model, and (2) SIG-Augmented Policy Optimization, which integrates SIG and enhances RL with a novel SIG-guided Reward Distribution Mechanism that assigns higher rewards to informative questions for targeted optimization. Extensive experiments on two newly curated partial-information medical benchmarks demonstrate that ProMed significantly outperforms state-of-the-art methods by an average of 6.29% and delivers a 54.45% gain over the reactive paradigm, while also generalizing robustly to out-of-domain cases.

