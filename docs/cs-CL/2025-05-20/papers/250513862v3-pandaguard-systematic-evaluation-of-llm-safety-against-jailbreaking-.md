---
layout: default
title: PandaGuard: Systematic Evaluation of LLM Safety against Jailbreaking Attacks
---

# PandaGuard: Systematic Evaluation of LLM Safety against Jailbreaking Attacks

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13862" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13862v3</a>
  <a href="https://arxiv.org/pdf/2505.13862.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13862v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13862v3', 'PandaGuard: Systematic Evaluation of LLM Safety against Jailbreaking Attacks')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guobin Shen, Dongcheng Zhao, Linghao Feng, Xiang He, Jihang Wang, Sicheng Shen, Haibo Tong, Yiting Dong, Jindong Li, Xiang Zheng, Yi Zeng

**分类**: cs.CR, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-05-26)

---

## 💡 一句话要点

**提出PandaGuard以系统评估LLM安全性应对越狱攻击**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `安全性评估` `越狱攻击` `多智能体系统` `模块化框架` `对抗性提示` `评判策略` `实验可重复性`

## 📋 核心要点

1. 现有的LLM安全评估往往缺乏系统性，集中于孤立的攻击或防御技术，导致分析结果不够全面。
2. PandaGuard框架通过将LLM越狱安全建模为多智能体系统，整合了多种攻击和防御方法，提升了评估的系统性和可重复性。
3. 实验结果表明，没有单一的防御方法在所有维度上都是最佳的，评判者之间的分歧会导致安全评估的显著差异。

## 📝 摘要（中文）

大型语言模型（LLMs）在能力上取得了显著进展，但仍然容易受到称为越狱的对抗性提示的攻击，这些攻击可以绕过安全对齐并引发有害输出。尽管LLM安全研究的努力不断增加，但现有评估往往是零散的，集中于孤立的攻击或防御技术，缺乏系统性和可重复的分析。本文提出了PandaGuard，一个统一且模块化的框架，将LLM越狱安全建模为一个多智能体系统，包括攻击者、防御者和评判者。该框架实现了19种攻击方法和12种防御机制，支持多种判断策略，并采用灵活的插件架构，增强了可重复性和实际部署的可能性。基于此框架，我们开发了PandaBench，一个全面的基准，评估49种LLM及各种判断方法之间的交互，执行需要超过30亿个标记的实验。我们的广泛评估揭示了模型脆弱性、防御成本与性能的权衡，以及评判者一致性的问题。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型（LLM）在面对越狱攻击时的安全性评估问题。现有方法往往缺乏系统性，无法全面评估不同攻击和防御机制的相互作用。

**核心思路**：PandaGuard框架通过将LLM越狱安全视为一个多智能体系统，整合了攻击者、防御者和评判者的角色，提供了一个统一的评估平台。这样的设计使得不同方法之间的交互可以被系统化地分析。

**技术框架**：PandaGuard框架包括19种攻击方法和12种防御机制，采用灵活的插件架构，支持多种LLM接口和交互模式。实验过程通过配置驱动，增强了可重复性。

**关键创新**：该框架的最大创新在于其模块化设计和多智能体系统的构建，使得不同的攻击和防御策略可以在同一平台上进行系统评估，解决了以往研究的零散性问题。

**关键设计**：框架中实现的攻击和防御机制均为模块化设计，允许用户根据需求进行配置。实验中使用的评判策略也多样化，确保了评估结果的全面性和可靠性。

## 📊 实验亮点

实验结果显示，PandaGuard在评估49种LLM的安全性时，揭示了关键的模型脆弱性和防御成本性能权衡。评判者之间的分歧导致安全评估结果的显著差异，强调了多样化评判策略的重要性。整体实验需要超过30亿个标记，确保了评估的全面性。

## 🎯 应用场景

PandaGuard的研究成果可广泛应用于大型语言模型的安全性评估，尤其是在需要防范对抗性攻击的场景中，如自动化客服、内容生成和社交媒体等领域。其模块化设计和灵活性使得研究人员和开发者能够根据具体需求进行安全性测试和优化，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) have achieved remarkable capabilities but remain vulnerable to adversarial prompts known as jailbreaks, which can bypass safety alignment and elicit harmful outputs. Despite growing efforts in LLM safety research, existing evaluations are often fragmented, focused on isolated attack or defense techniques, and lack systematic, reproducible analysis. In this work, we introduce PandaGuard, a unified and modular framework that models LLM jailbreak safety as a multi-agent system comprising attackers, defenders, and judges. Our framework implements 19 attack methods and 12 defense mechanisms, along with multiple judgment strategies, all within a flexible plugin architecture supporting diverse LLM interfaces, multiple interaction modes, and configuration-driven experimentation that enhances reproducibility and practical deployment. Built on this framework, we develop PandaBench, a comprehensive benchmark that evaluates the interactions between these attack/defense methods across 49 LLMs and various judgment approaches, requiring over 3 billion tokens to execute. Our extensive evaluation reveals key insights into model vulnerabilities, defense cost-performance trade-offs, and judge consistency. We find that no single defense is optimal across all dimensions and that judge disagreement introduces nontrivial variance in safety assessments. We release the code, configurations, and evaluation results to support transparent and reproducible research in LLM safety.

