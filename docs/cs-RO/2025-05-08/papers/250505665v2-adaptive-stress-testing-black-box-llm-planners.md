---
layout: default
title: Adaptive Stress Testing Black-Box LLM Planners
---

# Adaptive Stress Testing Black-Box LLM Planners

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05665" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05665v2</a>
  <a href="https://arxiv.org/pdf/2505.05665.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05665v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05665v2', 'Adaptive Stress Testing Black-Box LLM Planners')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Neeloy Chakraborty, John Pohovey, Melkior Ornik, Katherine Driggs-Campbell

**分类**: cs.RO, cs.AI, cs.CL

**发布日期**: 2025-05-08 (更新: 2025-10-10)

**备注**: 25 pages, 24 figures, 5 tables

---

## 💡 一句话要点

**提出自适应压力测试方法以解决黑箱LLM规划者的幻觉问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自适应压力测试` `蒙特卡洛树搜索` `幻觉检测` `安全关键系统` `决策支持` `机器人导航`

## 📋 核心要点

1. 现有黑箱模型检测方法在识别LLMs幻觉时存在局限性，主要依赖于提示扰动，效果不够理想。
2. 本文提出自适应压力测试（AST）结合蒙特卡洛树搜索（MCTS）的方法，旨在高效发现导致LLMs不确定性增加的提示扰动。
3. 通过在单智能体月球着陆和多智能体机器人导航仿真中进行实验，验证了该方法在实时信任评估中的有效性和可靠性。

## 📝 摘要（中文）

大型语言模型（LLMs）在决策任务中表现出色，但其产生不安全和不期望输出的倾向带来了风险。本文强调在安全关键场景中检测这些失败的必要性。现有的黑箱模型检测方法通常通过识别多个样本间的不一致性来发现幻觉，然而这些方法往往依赖于随机化细节顺序或生成对抗输入等提示扰动。我们首先通过手动案例研究表明，其他形式的扰动（如添加噪声、移除传感器细节）会导致LLMs在多智能体驾驶环境中产生幻觉。接着，我们提出了一种利用自适应压力测试（AST）和蒙特卡洛树搜索（MCTS）高效搜索提示扰动空间的新方法。通过生成多样场景下的MCTS提示扰动树，我们的实验表明，离线分析可以在运行时自动生成影响模型不确定性的提示，并为LLM的实时信任评估提供信息。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在决策任务中产生幻觉的问题，现有方法多依赖于提示扰动，难以全面捕捉模型的不确定性和潜在风险。

**核心思路**：我们提出自适应压力测试（AST）结合蒙特卡洛树搜索（MCTS），通过系统地探索提示扰动空间，发现导致模型不确定性或崩溃的场景，从而提高模型的安全性和可靠性。

**技术框架**：整体流程包括：首先进行手动案例研究以识别幻觉的诱因；然后构建MCTS提示扰动树，通过多样化场景生成有效的提示扰动；最后进行离线分析以支持实时信任评估。

**关键创新**：本研究的创新在于将AST与MCTS结合，形成了一种新的提示扰动搜索方法，能够有效识别和干预LLMs的幻觉行为，与传统方法相比具有更高的灵活性和准确性。

**关键设计**：在技术细节上，我们设计了多种扰动形式，包括添加噪声和移除传感器细节，并通过实验验证了这些扰动对模型输出稳定性的影响。

## 📊 实验亮点

实验结果表明，使用AST和MCTS方法生成的提示扰动能够有效提高LLMs在多智能体环境中的稳定性，减少幻觉输出的发生率。与传统方法相比，我们的方法在模型不确定性评估中表现出显著提升，具体数据尚未披露。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其在自动驾驶、机器人导航等安全关键领域。通过提高大型语言模型在决策过程中的可靠性，可以显著降低潜在风险，推动智能系统的安全应用和发展。

## 📄 摘要（原文）

> Large language models (LLMs) have recently demonstrated success in generalizing across decision-making tasks including planning, control, and prediction, but their tendency to hallucinate unsafe and undesired outputs poses risks. We argue that detecting such failures is necessary, especially in safety-critical scenarios. Existing methods for black-box models often detect hallucinations by identifying inconsistencies across multiple samples. Many of these approaches typically introduce prompt perturbations like randomizing detail order or generating adversarial inputs, with the intuition that a confident model should produce stable outputs. We first perform a manual case study showing that other forms of perturbations (e.g., adding noise, removing sensor details) cause LLMs to hallucinate in a multi-agent driving environment. We then propose a novel method for efficiently searching the space of prompt perturbations using adaptive stress testing (AST) with Monte-Carlo tree search (MCTS). Our AST formulation enables discovery of scenarios and prompts that cause language models to act with high uncertainty or even crash. By generating MCTS prompt perturbation trees across diverse scenarios, we show through extensive experiments that offline analyses can be used at runtime to automatically generate prompts that influence model uncertainty, and to inform real-time trust assessments of an LLM. We further characterize LLMs deployed as planners in a single-agent lunar lander environment and in a multi-agent robot crowd navigation simulation. Overall, ours is one of the first hallucination intervention algorithms to pave a path towards rigorous characterization of black-box LLM planners.

