---
layout: default
title: "MLE-Dojo: Interactive Environments for Empowering LLM Agents in Machine Learning Engineering"
---

# MLE-Dojo: Interactive Environments for Empowering LLM Agents in Machine Learning Engineering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07782" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07782v1</a>
  <a href="https://arxiv.org/pdf/2505.07782.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07782v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07782v1', 'MLE-Dojo: Interactive Environments for Empowering LLM Agents in Machine Learning Engineering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rushi Qiang, Yuchen Zhuang, Yinghao Li, Dingu Sagar V K, Rongzhi Zhang, Changhao Li, Ian Shu-Hei Wong, Sherry Yang, Percy Liang, Chao Zhang, Bo Dai

**分类**: cs.LG

**发布日期**: 2025-05-12

---

## 💡 一句话要点

**提出MLE-Dojo以解决LLM代理在机器学习工程中的交互性不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `机器学习工程` `交互式环境` `强化学习` `Kaggle挑战` `迭代优化` `模型调优`

## 📋 核心要点

1. 现有方法主要依赖静态数据集和单次评估，缺乏交互性和迭代优化能力。
2. MLE-Dojo提供了一个交互环境，支持代理进行实验、调试和优化，基于真实的Kaggle挑战构建。
3. 实验结果显示，尽管当前模型在迭代改进上取得了一定进展，但在生成长远解决方案和高效解决复杂错误方面仍存在显著局限。

## 📝 摘要（中文）

我们介绍了MLE-Dojo，这是一个类似Gym的框架，旨在系统性地强化学习、评估和改进自主大型语言模型（LLM）代理在迭代机器学习工程（MLE）工作流中的表现。与现有基准主要依赖静态数据集或单次评估不同，MLE-Dojo提供了一个交互环境，使代理能够通过结构化反馈循环进行迭代实验、调试和优化解决方案。MLE-Dojo基于200多个真实的Kaggle挑战，涵盖了多样化的开放式MLE任务，反映了数据处理、架构搜索、超参数调优和代码调试等现实工程场景。其完全可执行的环境支持通过监督微调和强化学习进行全面的代理训练，促进迭代实验、真实数据采样和实时结果验证。

## 🔬 方法详解

**问题定义**：论文旨在解决现有大型语言模型（LLM）代理在机器学习工程中缺乏交互性和迭代优化的问题。现有方法通常依赖静态数据集，无法有效支持代理的实验和调试。

**核心思路**：MLE-Dojo通过构建一个交互式环境，使代理能够在真实场景中进行迭代实验和优化，利用结构化反馈循环来提升模型性能。

**技术框架**：MLE-Dojo的整体架构包括多个模块，如数据处理、模型训练、反馈循环和评估机制。代理在这些模块中可以进行实验、调试和优化，形成闭环反馈。

**关键创新**：MLE-Dojo的最大创新在于其交互性和迭代性，允许代理在真实的工程任务中进行多次尝试和改进，区别于传统的静态评估方法。

**关键设计**：框架支持通过监督微调和强化学习进行训练，采用灵活的参数设置和损失函数设计，以适应不同的MLE任务和数据源。

## 📊 实验亮点

在对八个前沿LLM的广泛评估中，尽管当前模型在迭代改进方面取得了一定的进展，但仍然在自主生成长远解决方案和高效解决复杂错误方面存在显著局限。具体性能数据和提升幅度尚未明确，但实验结果表明MLE-Dojo的有效性。

## 🎯 应用场景

MLE-Dojo可广泛应用于机器学习工程的各个领域，如数据处理、模型调优和代码调试等。其交互式环境能够帮助研究人员和工程师更高效地开发和优化机器学习模型，推动相关技术的进步和应用。未来，该框架有望促进社区驱动的创新，推动下一代MLE代理的发展。

## 📄 摘要（原文）

> We introduce MLE-Dojo, a Gym-style framework for systematically reinforcement learning, evaluating, and improving autonomous large language model (LLM) agents in iterative machine learning engineering (MLE) workflows. Unlike existing benchmarks that primarily rely on static datasets or single-attempt evaluations, MLE-Dojo provides an interactive environment enabling agents to iteratively experiment, debug, and refine solutions through structured feedback loops. Built upon 200+ real-world Kaggle challenges, MLE-Dojo covers diverse, open-ended MLE tasks carefully curated to reflect realistic engineering scenarios such as data processing, architecture search, hyperparameter tuning, and code debugging. Its fully executable environment supports comprehensive agent training via both supervised fine-tuning and reinforcement learning, facilitating iterative experimentation, realistic data sampling, and real-time outcome verification. Extensive evaluations of eight frontier LLMs reveal that while current models achieve meaningful iterative improvements, they still exhibit significant limitations in autonomously generating long-horizon solutions and efficiently resolving complex errors. Furthermore, MLE-Dojo's flexible and extensible architecture seamlessly integrates diverse data sources, tools, and evaluation protocols, uniquely enabling model-based agent tuning and promoting interoperability, scalability, and reproducibility. We open-source our framework and benchmarks to foster community-driven innovation towards next-generation MLE agents.

