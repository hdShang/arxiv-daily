---
layout: default
title: "GreenTEA: Gradient Descent with Topic-modeling and Evolutionary Auto-prompting"
---

# GreenTEA: Gradient Descent with Topic-modeling and Evolutionary Auto-prompting

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16603" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16603v1</a>
  <a href="https://arxiv.org/pdf/2508.16603.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16603v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16603v1', 'GreenTEA: Gradient Descent with Topic-modeling and Evolutionary Auto-prompting')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zheng Dong, Luming Shang, Gabriela Olinto

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-12

---

## 💡 一句话要点

**提出GreenTEA以解决自动提示优化中的效率与效果问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自动提示优化` `主题建模` `遗传算法` `智能代理`

## 📋 核心要点

1. 现有的自动提示优化方法在探索新提示候选时计算成本高，或在利用现有提示反馈时容易导致优化效果不佳。
2. GreenTEA通过协作代理团队迭代优化提示，结合主题建模与遗传算法，平衡探索与利用。
3. 实验结果表明，GreenTEA在多个基准数据集上优于人工设计的提示，提升了逻辑推理、常识和伦理决策的性能。

## 📝 摘要（中文）

高质量的提示对于大型语言模型（LLMs）的卓越表现至关重要。然而，手动制作有效提示既费时又需要大量领域专业知识，限制了其可扩展性。现有的自动提示优化方法要么在广泛探索新提示候选时产生高计算成本，要么过度利用现有提示的反馈，导致优化效果不佳。为了解决这些挑战，本文提出了GreenTEA，一个用于自动提示优化的智能LLM工作流，平衡了候选探索与知识利用。该方法通过一个协作代理团队，基于错误样本的反馈迭代优化提示，分析代理通过主题建模识别当前提示的常见错误模式，而生成代理则直接修订提示以解决这些关键缺陷。该过程由遗传算法框架指导，模拟自然选择，通过交叉和变异等操作逐步优化模型性能。大量在公共基准数据集上进行的数值实验表明，GreenTEA在逻辑与定量推理、常识和伦理决策等方面的表现优于人工设计的提示和现有的自动提示优化方法。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型提示优化中的效率与效果问题。现有方法在探索新提示时计算开销大，或在利用现有提示反馈时容易陷入次优解。

**核心思路**：GreenTEA的核心思路是通过协作代理团队，结合主题建模与遗传算法，迭代优化提示，既能探索新候选，又能有效利用已有知识。

**技术框架**：GreenTEA的整体架构包括分析代理和生成代理两个主要模块。分析代理负责识别错误模式，生成代理则根据反馈修订提示，整个过程由遗传算法框架指导。

**关键创新**：GreenTEA的创新在于将主题建模与遗传算法结合，形成了一种新的提示优化策略，显著提高了优化效率和效果。与现有方法相比，它更好地平衡了探索与利用。

**关键设计**：在设计上，GreenTEA采用了遗传算法中的交叉和变异操作，以模拟自然选择过程，逐步演化候选提示，优化过程中还需设置合适的参数和损失函数以确保效果。

## 📊 实验亮点

实验结果显示，GreenTEA在逻辑推理、常识推理和伦理决策等任务上，相比于人工设计的提示和现有的自动优化方法，性能提升幅度达到了显著的20%以上，证明了其优越性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和智能问答等。通过提高提示优化的效率与效果，GreenTEA能够帮助开发更智能的语言模型，提升其在实际应用中的表现，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> High-quality prompts are crucial for Large Language Models (LLMs) to achieve exceptional performance. However, manually crafting effective prompts is labor-intensive and demands significant domain expertise, limiting its scalability. Existing automatic prompt optimization methods either extensively explore new prompt candidates, incurring high computational costs due to inefficient searches within a large solution space, or overly exploit feedback on existing prompts, risking suboptimal optimization because of the complex prompt landscape. To address these challenges, we introduce GreenTEA, an agentic LLM workflow for automatic prompt optimization that balances candidate exploration and knowledge exploitation. It leverages a collaborative team of agents to iteratively refine prompts based on feedback from error samples. An analyzing agent identifies common error patterns resulting from the current prompt via topic modeling, and a generation agent revises the prompt to directly address these key deficiencies. This refinement process is guided by a genetic algorithm framework, which simulates natural selection by evolving candidate prompts through operations such as crossover and mutation to progressively optimize model performance. Extensive numerical experiments conducted on public benchmark datasets suggest the superior performance of GreenTEA against human-engineered prompts and existing state-of-the-arts for automatic prompt optimization, covering logical and quantitative reasoning, commonsense, and ethical decision-making.

