---
layout: default
title: "KompeteAI: Accelerated Autonomous Multi-Agent System for End-to-End Pipeline Generation for Machine Learning Problems"
---

# KompeteAI: Accelerated Autonomous Multi-Agent System for End-to-End Pipeline Generation for Machine Learning Problems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.10177" class="toolbar-btn" target="_blank">📄 arXiv: 2508.10177v2</a>
  <a href="https://arxiv.org/pdf/2508.10177.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.10177v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.10177v2', 'KompeteAI: Accelerated Autonomous Multi-Agent System for End-to-End Pipeline Generation for Machine Learning Problems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Stepan Kulibaba, Artem Dzhalilov, Roman Pakhomov, Oleg Svidchenko, Alexander Gasnikov, Aleksei Shpilman

**分类**: cs.AI

**发布日期**: 2025-08-13 (更新: 2025-09-29)

---

## 💡 一句话要点

**提出KompeteAI以解决AutoML系统的执行瓶颈与探索不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动机器学习` `动态探索` `合并策略` `检索增强生成` `执行效率` `多代理系统` `机器学习管道`

## 📋 核心要点

1. 现有的AutoML系统在探索策略上存在显著限制，导致解决方案多样性不足和执行效率低下。
2. KompeteAI通过动态解决方案空间探索和合并阶段，克服了传统MCTS方法的局限，并引入RAG以扩展假设空间。
3. 实验结果表明，KompeteAI在MLE-Bench基准上平均超越其他领先方法3%，并将管道评估速度提高了6.9倍。

## 📝 摘要（中文）

近年来，基于大型语言模型的自动机器学习（AutoML）系统展现了令人瞩目的能力，但也面临探索策略受限和执行瓶颈等重大挑战。探索受限于缺乏多样性的单次方法和未能重组强有力部分解的蒙特卡洛树搜索（MCTS）方法。执行瓶颈源于冗长的代码验证周期，抑制了迭代改进。为了解决这些问题，本文提出了KompeteAI，一个具有动态解决方案空间探索的新型AutoML框架。KompeteAI通过引入合并阶段来组合最佳候选方案，克服了以往MCTS方法孤立处理想法的局限。此外，通过整合检索增强生成（RAG），KompeteAI扩展了假设空间，从Kaggle笔记本和arXiv论文中获取真实世界策略。KompeteAI还通过预测评分模型和加速调试方法来解决执行瓶颈，利用早期阶段指标评估解决方案潜力，从而避免高成本的全代码执行。该方法使管道评估速度提高了6.9倍，并在主要AutoML基准MLE-Bench上平均超越领先方法3%。

## 🔬 方法详解

**问题定义**：本文旨在解决现有AutoML系统在探索策略和执行效率上的不足，特别是单次方法和MCTS方法的局限性，以及冗长的代码验证周期带来的执行瓶颈。

**核心思路**：KompeteAI通过引入动态解决方案空间探索和合并阶段，能够有效组合多个候选方案，从而提高探索的多样性和效率。同时，整合检索增强生成（RAG）技术，利用外部资源丰富假设空间。

**技术框架**：KompeteAI的整体架构包括多个主要模块：动态探索模块、合并阶段、RAG集成模块、预测评分模型和加速调试方法。这些模块协同工作，形成一个高效的AutoML管道。

**关键创新**：KompeteAI的核心创新在于其合并阶段的设计，使得多个候选方案能够有效组合，克服了传统方法的孤立性。此外，RAG的引入使得系统能够从实际案例中获取灵感，增强了模型的实用性。

**关键设计**：在设计中，KompeteAI采用了预测评分模型来评估解决方案的潜力，利用早期阶段的指标来避免全代码执行的高成本，同时在调试过程中引入了加速方法，以提高整体执行效率。

## 📊 实验亮点

KompeteAI在MLE-Bench基准测试中表现优异，平均超越其他领先方法3%。此外，其管道评估速度提高了6.9倍，显著提升了AutoML系统的执行效率，展示了其在实际应用中的巨大潜力。

## 🎯 应用场景

KompeteAI的研究成果在多个领域具有广泛的应用潜力，特别是在需要快速迭代和高效模型生成的机器学习任务中。其动态探索和合并策略能够帮助研究人员和工程师更有效地开发和优化机器学习管道，提升实际应用的效率和效果。未来，KompeteAI可能在自动化数据科学、智能决策支持系统等领域发挥重要作用。

## 📄 摘要（原文）

> Recent Large Language Model (LLM)-based AutoML systems demonstrate impressive capabilities but face significant limitations such as constrained exploration strategies and a severe execution bottleneck. Exploration is hindered by one-shot methods lacking diversity and Monte Carlo Tree Search (MCTS) approaches that fail to recombine strong partial solutions. The execution bottleneck arises from lengthy code validation cycles that stifle iterative refinement. To overcome these challenges, we introduce KompeteAI, a novel AutoML framework with dynamic solution space exploration. Unlike previous MCTS methods that treat ideas in isolation, KompeteAI introduces a merging stage that composes top candidates. We further expand the hypothesis space by integrating Retrieval-Augmented Generation (RAG), sourcing ideas from Kaggle notebooks and arXiv papers to incorporate real-world strategies. KompeteAI also addresses the execution bottleneck via a predictive scoring model and an accelerated debugging method, assessing solution potential using early stage metrics to avoid costly full-code execution. This approach accelerates pipeline evaluation 6.9 times. KompeteAI outperforms leading methods (e.g., RD-agent, AIDE, and Ml-Master) by an average of 3\% on the primary AutoML benchmark, MLE-Bench. Additionally, we propose Kompete-bench to address limitations in MLE-Bench, where KompeteAI also achieves state-of-the-art results

