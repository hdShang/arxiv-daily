---
layout: default
title: "Deceive, Detect, and Disclose: Large Language Models Play Mini-Mafia"
---

# Deceive, Detect, and Disclose: Large Language Models Play Mini-Mafia

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.23023" class="toolbar-btn" target="_blank">📄 arXiv: 2509.23023v1</a>
  <a href="https://arxiv.org/pdf/2509.23023.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.23023v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.23023v1', 'Deceive, Detect, and Disclose: Large Language Models Play Mini-Mafia')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davi Bastos Costa, Renato Vicente

**分类**: cs.AI

**发布日期**: 2025-09-27

**备注**: 20 pages, 7 figures, 5 tables; submitted to ICLR 2026; Code and data: https://github.com/bastoscostadavi/llm-mafia-game

---

## 💡 一句话要点

**提出Mini-Mafia基准测试LLM的社会智能，评估欺骗、检测和信息披露能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `社会智能` `多智能体系统` `欺骗检测` `心理理论` `基准测试` `狼人杀` `AI安全`

## 📋 核心要点

1. 现有方法难以系统评估LLM在信息不对称和需要心理理论推理的社会场景中的智能水平。
2. 论文设计了Mini-Mafia，一个简化的狼人杀游戏环境，用于隔离和评估LLM的欺骗、检测和披露信息能力。
3. 实验结果表明，Mini-Mafia能够揭示LLM在社会智能方面的优势和不足，并发现一些反直觉的现象。

## 📝 摘要（中文）

本文提出Mini-Mafia，一个简化的四人版狼人杀游戏，包含一个狼人、一个侦探和两个村民，用于评估大型语言模型（LLM）的社会智能。狼人需要在夜晚杀死一个村民，侦探调查狼人，游戏简化为白天阶段的讨论和投票。该设置通过角色特定的获胜条件，隔离了三个交互能力：狼人必须欺骗，村民必须检测欺骗，侦探必须有效披露信息。为了衡量这些技能，论文让LLM相互对战，创建了Mini-Mafia基准测试：一个两阶段框架，首先估计固定对手配置中的胜率，然后使用标准化评分汇总性能。该基准完全基于模型交互，无需外部数据，并随着新模型的引入而演进。实验结果显示了一些违反直觉的现象，包括较小模型优于较大模型的情况。Mini-Mafia还支持对涌现的多智能体动态进行定量研究，例如姓名偏见和最后发言者优势。此外，它通过生成欺骗检测器的训练数据和跟踪模型相对于人类基线的欺骗能力，为AI安全做出贡献。

## 🔬 方法详解

**问题定义**：论文旨在解决如何有效评估大型语言模型（LLM）在复杂社会互动中的智能水平，特别是在信息不对称和需要心理理论推理的场景下。现有方法缺乏一个标准化的、可控的测试环境，难以系统地评估LLM的欺骗、检测欺骗和有效沟通能力。

**核心思路**：论文的核心思路是利用简化的狼人杀游戏（Mini-Mafia）作为测试环境，通过角色扮演和胜负条件来量化LLM的社会智能。Mini-Mafia的设计旨在隔离和突出LLM在欺骗、检测和信息披露方面的能力，并通过模型之间的博弈来评估其性能。

**技术框架**：Mini-Mafia基准测试包含以下主要阶段：
1. **游戏设置**：定义角色（狼人、侦探、村民）和游戏规则，简化为单日阶段的讨论和投票。
2. **模型对战**：让不同的LLM扮演不同的角色，进行多轮游戏。
3. **胜率估计**：在固定的对手配置下，统计每个模型的胜率。
4. **性能评估**：使用标准化评分汇总模型在不同配置下的性能，形成基准测试结果。

**关键创新**：该论文的关键创新在于：
1. **Mini-Mafia游戏环境**：简化狼人杀游戏，使其更易于控制和分析，同时保留了社会互动的核心要素。
2. **基于模型交互的基准测试**：完全依赖模型之间的博弈来生成数据，无需外部数据，并能够随着新模型的出现而动态演进。
3. **角色特定的评估指标**：通过角色特定的获胜条件来评估LLM在欺骗、检测和信息披露方面的能力。

**关键设计**：
1. **角色分配**：随机分配角色，确保公平性。
2. **对话提示词设计**：精心设计提示词，引导LLM进行角色扮演和策略制定。
3. **胜率计算**：采用统计方法计算模型在不同对手配置下的胜率。
4. **标准化评分**：使用标准化评分来汇总模型在不同配置下的性能，便于比较。

## 📊 实验亮点

实验结果表明，Mini-Mafia能够有效区分不同LLM的社会智能水平，并发现了一些反直觉的现象，例如较小模型在某些情况下优于较大模型。此外，研究还揭示了姓名偏见和最后发言者优势等涌现的多智能体动态。该基准测试为LLM的社会智能研究提供了一个有价值的工具。

## 🎯 应用场景

该研究成果可应用于评估和提升LLM在多智能体协作、谈判、安全等领域的性能。通过Mini-Mafia基准测试，可以更好地理解LLM的社会智能，并开发更安全、更可靠的AI系统。此外，该方法还可以用于生成欺骗检测器的训练数据，提高AI系统的鲁棒性。

## 📄 摘要（原文）

> Mafia is a social deduction game where informed mafia compete against uninformed townsfolk. Its asymmetry of information and reliance on theory-of-mind reasoning mirror real-world multi-agent scenarios, making it a useful testbed for evaluating the social intelligence of large language models (LLMs). To support a systematic study, we introduce Mini-Mafia: a simplified four-player variant with one mafioso, one detective, and two villagers. We set the mafioso to kill a villager and the detective to investigate the mafioso during the night, reducing the game to a single day phase of discussion and voting. This setup isolates three interactive capabilities through role-specific win conditions: the mafioso must deceive, the villagers must detect deception, and the detective must effectively disclose information. To measure these skills, we have LLMs play against each other, creating the Mini-Mafia Benchmark: a two-stage framework that first estimates win rates within fixed opponent configurations, then aggregates performance across them using standardized scoring. Built entirely from model interactions without external data, the benchmark evolves as new models are introduced, with each one serving both as a new opponent and as a subject of evaluation. Our experiments reveal counterintuitive results, including cases where smaller models outperform larger ones. Beyond benchmarking, Mini-Mafia enables quantitative study of emergent multi-agent dynamics such as name bias and last-speaker advantage. It also contributes to AI safety by generating training data for deception detectors and by tracking models' deception capabilities against human baselines.

