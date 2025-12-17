---
layout: default
title: VideoChat-M1: Collaborative Policy Planning for Video Understanding via Multi-Agent Reinforcement Learning
---

# VideoChat-M1: Collaborative Policy Planning for Video Understanding via Multi-Agent Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.19524" class="toolbar-btn" target="_blank">📄 arXiv: 2511.19524v1</a>
  <a href="https://arxiv.org/pdf/2511.19524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.19524v1" onclick="toggleFavorite(this, '2511.19524v1', 'VideoChat-M1: Collaborative Policy Planning for Video Understanding via Multi-Agent Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Boyu Chen, Zikang Wang, Zhengrong Yue, Kainan Yan, Chenyun Yu, Yi Huang, Zijun Liu, Yafei Wen, Xiaoxin Chen, Yang Liu, Peng Li, Yali Wang

**分类**: cs.CV, cs.MA

**发布日期**: 2025-11-24

**备注**: 21 pages, 9 figures

---

## 💡 一句话要点

**提出VideoChat-M1，通过多智能体强化学习实现视频理解的协同策略规划。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频理解` `多智能体系统` `强化学习` `协同策略规划` `多模态大语言模型`

## 📋 核心要点

1. 现有工具增强的多模态大语言模型在视频理解中采用静态且不可学习的工具调用机制，限制了对复杂视频线索的发现。
2. VideoChat-M1采用协同策略规划（CPP）范式，通过多个策略智能体协同工作，动态优化策略以响应用户查询。
3. 通过多智能体强化学习（MARL）方法联合优化策略智能体团队，实验表明VideoChat-M1在多个基准测试中达到SOTA性能。

## 📝 摘要（中文）

本文提出了一种用于视频理解的新型多智能体系统VideoChat-M1。该系统采用独特的协同策略规划（CPP）范式，包含多个策略智能体，而非单一或固定的策略。CPP包含三个关键过程：(1)策略生成：每个智能体根据用户查询生成独特的工具调用策略；(2)策略执行：每个智能体依次调用相关工具来执行其策略并探索视频内容；(3)策略通信：在策略执行的中间阶段，智能体相互交互以更新各自的策略。通过这种协同框架，所有智能体协同工作，基于来自同行的上下文信息动态地改进其策略，从而有效地响应用户查询。此外，我们为CPP范式配备了一种简洁的多智能体强化学习（MARL）方法。因此，可以联合优化策略智能体团队，以提高VideoChat-M1的性能，并由最终答案奖励和中间协作过程反馈来指导。大量实验表明，VideoChat-M1在跨越四个任务的八个基准测试中实现了SOTA性能。值得注意的是，在LongVideoBench上，我们的方法优于SOTA模型Gemini 2.5 pro 3.6%，优于GPT-4o 15.6%。

## 🔬 方法详解

**问题定义**：现有基于工具增强的多模态大语言模型在视频理解任务中，通常采用静态或固定的工具调用策略，无法充分挖掘视频中存在的时序或空间上的复杂线索。这导致模型在处理长视频或需要复杂推理的视频理解任务时，性能受到限制。现有方法缺乏动态调整和学习的能力，难以适应不同视频内容和用户查询的需求。

**核心思路**：VideoChat-M1的核心思路是引入多智能体协同策略规划（CPP）范式，让多个智能体各自生成并执行工具调用策略，并通过智能体之间的通信和协作，动态地调整和优化这些策略。这种方法旨在模拟人类团队协作解决问题的过程，每个智能体负责探索视频的不同方面，并通过信息共享和策略调整，共同完成视频理解任务。

**技术框架**：VideoChat-M1的整体框架包含三个主要阶段：策略生成、策略执行和策略通信。在策略生成阶段，每个智能体根据用户查询生成一个独特的工具调用策略。在策略执行阶段，每个智能体按照其策略依次调用相关工具来探索视频内容。在策略通信阶段，智能体之间进行信息交互，更新各自的策略。整个过程通过多智能体强化学习（MARL）进行优化，利用最终答案奖励和中间协作过程反馈来指导智能体的学习。

**关键创新**：VideoChat-M1的关键创新在于其协同策略规划（CPP）范式和多智能体强化学习（MARL）方法的结合。与现有方法采用的单一或固定策略不同，CPP允许每个智能体生成并执行不同的策略，从而实现对视频内容更全面的探索。MARL方法的引入使得智能体团队能够通过学习不断优化其策略，从而提高整体性能。

**关键设计**：VideoChat-M1采用多智能体强化学习方法进行训练，奖励函数包括最终答案的奖励和中间协作过程的反馈。具体来说，最终答案的奖励用于鼓励智能体生成正确的答案，而中间协作过程的反馈则用于鼓励智能体之间的有效通信和策略调整。具体的网络结构和参数设置在论文中未详细说明，属于未知信息。

## 📊 实验亮点

VideoChat-M1在八个基准测试中实现了SOTA性能，尤其在LongVideoBench上，超越了Gemini 2.5 pro 3.6%，超越了GPT-4o 15.6%。这些结果表明，该方法在处理长视频和需要复杂推理的视频理解任务方面具有显著优势。

## 🎯 应用场景

VideoChat-M1在视频理解领域具有广泛的应用前景，可用于智能视频监控、视频内容分析、智能客服、教育视频理解等场景。通过提升视频理解的准确性和效率，该研究可以帮助人们更好地理解和利用视频信息，具有重要的实际价值和社会意义。未来，该方法有望应用于更复杂的视频理解任务，例如视频生成、视频编辑等。

## 📄 摘要（原文）

> By leveraging tool-augmented Multimodal Large Language Models (MLLMs), multi-agent frameworks are driving progress in video understanding. However, most of them adopt static and non-learnable tool invocation mechanisms, which limit the discovery of diverse clues essential for robust perception and reasoning regarding temporally or spatially complex videos. To address this challenge, we propose a novel Multi-agent system for video understanding, namely VideoChat-M1. Instead of using a single or fixed policy, VideoChat-M1 adopts a distinct Collaborative Policy Planning (CPP) paradigm with multiple policy agents, which comprises three key processes. (1) Policy Generation: Each agent generates its unique tool invocation policy tailored to the user's query; (2) Policy Execution: Each agent sequentially invokes relevant tools to execute its policy and explore the video content; (3) Policy Communication: During the intermediate stages of policy execution, agents interact with one another to update their respective policies. Through this collaborative framework, all agents work in tandem, dynamically refining their preferred policies based on contextual insights from peers to effectively respond to the user's query. Moreover, we equip our CPP paradigm with a concise Multi-Agent Reinforcement Learning (MARL) method. Consequently, the team of policy agents can be jointly optimized to enhance VideoChat-M1's performance, guided by both the final answer reward and intermediate collaborative process feedback. Extensive experiments demonstrate that VideoChat-M1 achieves SOTA performance across eight benchmarks spanning four tasks. Notably, on LongVideoBench, our method outperforms the SOTA model Gemini 2.5 pro by 3.6% and GPT-4o by 15.6%.

