---
layout: default
title: SAGE: Training Smart Any-Horizon Agents for Long Video Reasoning with Reinforcement Learning
---

# SAGE: Training Smart Any-Horizon Agents for Long Video Reasoning with Reinforcement Learning

**arXiv**: [2512.13874v1](https://arxiv.org/abs/2512.13874) | [PDF](https://arxiv.org/pdf/2512.13874.pdf)

**作者**: Jitesh Jain, Jialuo Li, Zixian Ma, Jieyu Zhang, Chris Dongjoo Kim, Sangho Lee, Rohun Tripathi, Tanmay Gupta, Christopher Clark, Humphrey Shi

**分类**: cs.CV

**发布日期**: 2025-12-15

**备注**: Project Page: https://praeclarumjj3.github.io/sage/

---

## 💡 一句话要点

**提出SAGE，利用强化学习训练智能任意时域Agent，用于长视频推理。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `长视频推理` `任意时域推理` `强化学习` `智能Agent` `视频理解`

## 📋 核心要点

1. 现有视频推理模型通常以单轮方式处理大量帧，类似于观看完整长视频，消耗大量资源，缺乏灵活性。
2. SAGE系统通过多轮推理处理长视频，并能以单轮方式处理简单问题，模仿人类的观看习惯，提升效率。
3. 通过合成数据生成和强化学习后训练，SAGE在长视频推理任务上取得了显著提升，尤其是在长视频上。

## 📝 摘要（中文）

本文提出SAGE，一个智能Agent系统，它能够像人类一样进行任意时域的推理，即根据任务需要，决定是快速浏览长视频还是完整观看短视频。为了训练SAGE的核心模块SAGE-MM，我们利用Gemini-2.5-Flash提出了一个简易的合成数据生成流程。此外，我们还提出了一种有效的强化学习后训练方法，这对于在SAGE-MM中培养任意时域推理能力至关重要。为了评估真实娱乐场景下视频推理能力，我们构建了SAGE-Bench，其平均视频时长超过700秒。实验结果表明，我们的系统、数据和强化学习方法是有效的，在开放式视频推理任务上取得了高达6.1%的显著提升，在超过10分钟的视频上取得了8.2%的提升。

## 🔬 方法详解

**问题定义**：现有视频推理模型通常需要一次性处理大量视频帧，计算成本高昂，并且缺乏像人类一样的灵活推理能力，无法根据视频内容和任务需求调整观看策略。它们无法在需要时快速浏览长视频，或者在必要时完整观看短视频。

**核心思路**：SAGE的核心思路是训练一个智能Agent，使其能够像人类一样进行任意时域的推理。该Agent可以决定是迭代地浏览长视频，还是完整地观看短视频，从而在效率和准确性之间取得平衡。这种设计模仿了人类在处理视频时的自然行为。

**技术框架**：SAGE系统包含一个核心模块SAGE-MM，它负责根据当前状态决定下一步的动作，例如观看一部分视频、回答问题等。整个流程是多轮交互式的，Agent根据每一轮的观察和奖励，不断优化其推理策略。系统使用Gemini-2.5-Flash生成合成数据，用于预训练SAGE-MM。之后，采用强化学习对SAGE-MM进行后训练，以提升其任意时域推理能力。

**关键创新**：SAGE的关键创新在于其任意时域推理能力和强化学习后训练方法。传统的视频推理模型通常是单轮的，而SAGE能够进行多轮交互式推理，更加灵活高效。强化学习后训练方法能够有效地提升Agent的推理能力，使其能够更好地适应不同的视频和任务。

**关键设计**：SAGE-MM的训练包括预训练和强化学习两个阶段。预训练使用合成数据，目标是让Agent初步具备视频理解和推理能力。强化学习阶段则使用奖励函数来引导Agent学习最佳的观看策略。奖励函数的设计至关重要，需要平衡准确性和效率。具体的网络结构和参数设置在论文中有详细描述，但此处未提供。

## 📊 实验亮点

SAGE在开放式视频推理任务上取得了显著提升，高达6.1%。尤其是在超过10分钟的长视频上，SAGE的性能提升达到了8.2%。这些结果表明，SAGE的任意时域推理能力和强化学习后训练方法是有效的，能够显著提升长视频推理的性能。

## 🎯 应用场景

SAGE可应用于智能视频监控、智能教育、娱乐视频分析等领域。例如，在视频监控中，SAGE可以快速定位异常事件；在智能教育中，SAGE可以根据学生的学习进度和理解程度，智能推荐学习内容；在娱乐视频分析中，SAGE可以帮助用户快速找到感兴趣的片段。

## 📄 摘要（原文）

> As humans, we are natural any-horizon reasoners, i.e., we can decide whether to iteratively skim long videos or watch short ones in full when necessary for a given task. With this in mind, one would expect video reasoning models to reason flexibly across different durations. However, SOTA models are still trained to predict answers in a single turn while processing a large number of frames, akin to watching an entire long video, requiring significant resources. This raises the question: Is it possible to develop performant any-horizon video reasoning systems? Inspired by human behavior, we first propose SAGE, an agent system that performs multi-turn reasoning on long videos while handling simpler problems in a single turn. Secondly, we introduce an easy synthetic data generation pipeline using Gemini-2.5-Flash to train the orchestrator, SAGE-MM, which lies at the core of SAGE. We further propose an effective RL post-training recipe essential for instilling any-horizon reasoning ability in SAGE-MM. Thirdly, we curate SAGE-Bench with an average duration of greater than 700 seconds for evaluating video reasoning ability in real-world entertainment use cases. Lastly, we empirically validate the effectiveness of our system, data, and RL recipe, observing notable improvements of up to 6.1% on open-ended video reasoning tasks, as well as an impressive 8.2% improvement on videos longer than 10 minutes.

