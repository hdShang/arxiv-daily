---
layout: default
title: "Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL"
---

# Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07976" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07976v4</a>
  <a href="https://arxiv.org/pdf/2508.07976.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07976v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07976v4', 'Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaxuan Gao, Wei Fu, Minyang Xie, Shusheng Xu, Chuyi He, Zhiyu Mei, Banghua Zhu, Yi Wu

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-11 (更新: 2025-10-26)

**🔗 代码/项目**: [GITHUB](https://github.com/inclusionAI/ASearcher)

---

## 💡 一句话要点

**提出ASearcher以解决长时间搜索智能不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长时间搜索` `强化学习` `大型语言模型` `搜索智能` `异步训练` `问答系统` `信息检索`

## 📋 核心要点

1. 现有的开源智能体在搜索智能方面表现不足，无法有效处理复杂查询和进行深入探索。
2. 本文提出ASearcher，通过可扩展的异步强化学习训练，支持长时间搜索并提高训练效率。
3. 实验结果显示，QwQ-32B智能体在多个基准上取得显著提升，超越了现有的开源32B智能体。

## 📝 摘要（中文）

近年来，基于大型语言模型（LLM）的智能体在处理复杂知识密集型任务方面表现出色，尤其是在集成外部工具时。然而，现有的开源智能体在搜索智能方面仍存在不足，无法有效解决模糊查询、生成精准搜索、分析结果和进行深入探索。现有方法在可扩展性、效率和数据质量上均显不足，尤其是在线强化学习方法的回合限制（如≤10）限制了复杂策略的学习。本文提出了ASearcher，一个用于大规模强化学习训练搜索智能体的开源项目，具有可扩展的完全异步RL训练能力，支持长时间搜索并保持高效的训练效率。通过RL训练，本文的QwQ-32B智能体在xBench和GAIA上分别实现了78.0%和34.3%的Avg@4提升，且在训练期间工具调用次数超过100次，输出token超过40万。

## 🔬 方法详解

**问题定义**：本文旨在解决现有开源智能体在长时间搜索智能方面的不足，特别是在处理复杂查询和策略学习时的局限性。现有方法在可扩展性和效率上存在显著短板，限制了智能体的表现。

**核心思路**：论文提出的ASearcher通过完全异步的强化学习训练，允许智能体在长时间内进行搜索，克服了传统方法的回合限制，从而实现复杂策略的学习。

**技术框架**：ASearcher的整体架构包括数据生成模块、异步训练模块和评估模块。数据生成模块利用提示生成高质量的问答对，异步训练模块则进行强化学习训练，评估模块用于测试智能体在不同基准上的表现。

**关键创新**：ASearcher的主要创新在于其完全异步的RL训练方法，允许智能体在长时间内进行搜索，且无需依赖外部大型语言模型，显著提高了训练效率和智能体的表现。

**关键设计**：在设计上，ASearcher采用了特定的损失函数和网络结构，以优化智能体的学习过程。此外，智能体的参数设置经过精心调优，以确保在长时间搜索中保持高效性和准确性。

## 📊 实验亮点

实验结果显示，QwQ-32B智能体在xBench和GAIA基准上分别取得了78.0%和34.3%的Avg@4提升，且在训练过程中工具调用次数超过100次，输出token超过40万，表现超越了现有的开源32B智能体，展示了极强的长时间搜索能力。

## 🎯 应用场景

该研究的潜在应用领域包括信息检索、智能问答系统和复杂查询处理等。ASearcher的高效搜索能力和长时间策略学习能力使其在实际应用中具有重要价值，能够帮助用户更好地获取和分析信息，提升决策支持系统的智能水平。未来，该技术有望在更多领域中得到应用，推动智能体的发展。

## 📄 摘要（原文）

> Recent advancements in LLM-based agents have demonstrated remarkable capabilities in handling complex, knowledge-intensive tasks by integrating external tools. Among diverse choices of tools, search tools play a pivotal role in accessing vast external knowledge. However, open-source agents still fall short of achieving expert-level Search Intelligence, the ability to resolve ambiguous queries, generate precise searches, analyze results, and conduct thorough exploration. Existing approaches fall short in scalability, efficiency, and data quality. For example, small turn limits in existing online RL methods, e.g. <=10, restrict complex strategy learning. This paper introduces ASearcher, an open-source project for large-scale RL training of search agents. Our key contributions include: (1) Scalable fully asynchronous RL training that enables long-horizon search while maintaining high training efficiency. (2) A prompt-based LLM agent that autonomously synthesizes high-quality and challenging QAs, creating a large-scale QA dataset. Through RL training, our prompt-based QwQ-32B agent achieves substantial improvements, with 78.0% and 34.3% Avg@4 gains on xBench and GAIA, respectively. Notably, our agent exhibits extreme long-horizon search, with tool calls exceeding 100 turns and output tokens exceeding 400k during training time. With a simple agent design and no external LLMs, ASearcher-Web-QwQ achieves Avg@4 scores of 51.1 on xBench and 58.7 on GAIA, surpassing existing open-source 32B agents. Finally, we also show that ASearcher-Web-QwQ could achieve performance of commercial systems using external summary tool in a zero-shot transfer manner and test-time search. We open-source our models, training data, and codes in https://github.com/inclusionAI/ASearcher.

