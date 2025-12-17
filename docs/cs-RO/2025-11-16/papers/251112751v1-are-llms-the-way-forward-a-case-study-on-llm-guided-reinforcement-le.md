---
layout: default
title: Are LLMs The Way Forward? A Case Study on LLM-Guided Reinforcement Learning for Decentralized Autonomous Driving
---

# Are LLMs The Way Forward? A Case Study on LLM-Guided Reinforcement Learning for Decentralized Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.12751" class="toolbar-btn" target="_blank">📄 arXiv: 2511.12751v1</a>
  <a href="https://arxiv.org/pdf/2511.12751.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.12751v1" onclick="toggleFavorite(this, '2511.12751v1', 'Are LLMs The Way Forward? A Case Study on LLM-Guided Reinforcement Learning for Decentralized Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Timur Anvar, Jeffrey Chen, Yuyan Wang, Rohan Chandra

**分类**: cs.LG, cs.AI, cs.RO

**发布日期**: 2025-11-16

---

## 💡 一句话要点

**探索LLM辅助强化学习在分散式自动驾驶中的应用：奖励塑造的案例研究**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `自动驾驶` `强化学习` `大型语言模型` `奖励塑造` `分散式控制`

## 📋 核心要点

1. 现有强化学习方法在复杂自动驾驶场景中依赖人工设计的奖励函数，难以捕捉真实世界的语义和社会复杂性。
2. 本研究探索利用小型本地LLM通过奖励塑造来辅助强化学习，旨在提升自动驾驶策略的性能和泛化能力。
3. 实验表明，LLM辅助的强化学习方法虽然能提高成功率，但存在保守偏差和模型依赖性，效率低于纯强化学习。

## 📝 摘要（中文）

在复杂环境中，如拥挤的高速公路和车辆汇入场景中，自动驾驶车辆的导航仍然是一个活跃的研究领域。强化学习（RL）的一个关键限制在于其对良好定义的奖励函数的依赖，这些函数通常无法捕捉各种分布外情况的完整语义和社会复杂性。因此，越来越多的研究探索使用大型语言模型（LLM）来替代或补充RL，以进行直接规划和控制，因为它们能够推理丰富的语义上下文。然而，LLM也存在显著的缺点：在零样本安全关键设置中可能不稳定，产生不一致的输出，并且通常依赖于昂贵的API调用和网络延迟。这促使我们研究小型、本地部署的LLM（<14B参数）是否可以通过奖励塑造而非直接控制来有意义地支持自动高速公路驾驶。我们提出了一个案例研究，比较了纯RL、纯LLM和混合方法，其中LLM通过在训练期间对状态-动作转换进行评分来增强RL奖励，而标准RL策略在测试时执行。我们的研究结果表明，纯RL智能体以合理的效率实现了中等的成功率（73-89%），纯LLM智能体可以达到更高的成功率（高达94%），但速度性能严重下降，而混合方法始终介于这些极端之间。关键的是，尽管有明确的效率指令，受LLM影响的方法表现出系统的保守偏差，并具有显著的模型依赖性可变性，这突出了当前小型LLM在安全关键控制任务中的重要局限性。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶中，传统强化学习方法依赖于人工设计的奖励函数，难以适应复杂交通场景的问题。现有方法的痛点在于奖励函数难以捕捉真实世界驾驶的语义和社会规则，导致策略泛化能力不足。

**核心思路**：论文的核心思路是利用小型本地部署的LLM，通过奖励塑造来增强强化学习的奖励函数。LLM能够理解更丰富的语义信息，从而为强化学习提供更准确的奖励信号，引导智能体学习更符合人类驾驶习惯的策略。

**技术框架**：整体框架包含三个主要部分：纯RL智能体、纯LLM智能体和混合智能体。混合智能体在训练阶段利用LLM对状态-动作转换进行评分，以此增强RL的奖励函数。在测试阶段，混合智能体使用训练好的RL策略进行控制。

**关键创新**：最重要的技术创新点在于将LLM引入到强化学习的奖励塑造过程中，利用LLM的语义理解能力来改善奖励函数的质量。与直接使用LLM进行控制相比，该方法旨在利用LLM的优势，同时避免其在安全关键场景中的不稳定性和高延迟问题。

**关键设计**：论文使用了小于14B参数的小型LLM，以保证本地部署和低延迟。LLM的输出被用于调整强化学习的奖励函数，具体的调整方式和权重是关键的设计参数。此外，论文还设计了明确的效率指令，试图引导LLM生成更高效的驾驶策略，但实验结果表明效果有限。

## 📊 实验亮点

实验结果表明，纯RL智能体成功率在73-89%之间，纯LLM智能体成功率高达94%，但速度性能显著下降。混合方法介于两者之间，但表现出保守偏差和模型依赖性。尽管有明确的效率指令，LLM辅助的方法在效率方面仍不如纯RL方法，表明当前小型LLM在安全关键控制任务中存在局限性。

## 🎯 应用场景

该研究成果可应用于自动驾驶车辆的决策控制系统，尤其是在复杂和动态的交通环境中。通过LLM辅助的奖励塑造，有望提升自动驾驶策略的安全性、效率和泛化能力。此外，该方法也可以推广到其他需要复杂奖励函数设计的强化学习任务中，例如机器人导航和游戏AI。

## 📄 摘要（原文）

> Autonomous vehicle navigation in complex environments such as dense and fast-moving highways and merging scenarios remains an active area of research. A key limitation of RL is its reliance on well-specified reward functions, which often fail to capture the full semantic and social complexity of diverse, out-of-distribution situations. As a result, a rapidly growing line of research explores using Large Language Models (LLMs) to replace or supplement RL for direct planning and control, on account of their ability to reason about rich semantic context. However, LLMs present significant drawbacks: they can be unstable in zero-shot safety-critical settings, produce inconsistent outputs, and often depend on expensive API calls with network latency. This motivates our investigation into whether small, locally deployed LLMs (< 14B parameters) can meaningfully support autonomous highway driving through reward shaping rather than direct control. We present a case study comparing RL-only, LLM-only, and hybrid approaches, where LLMs augment RL rewards by scoring state-action transitions during training, while standard RL policies execute at test time. Our findings reveal that RL-only agents achieve moderate success rates (73-89%) with reasonable efficiency, LLM-only agents can reach higher success rates (up to 94%) but with severely degraded speed performance, and hybrid approaches consistently fall between these extremes. Critically, despite explicit efficiency instructions, LLM-influenced approaches exhibit systematic conservative bias with substantial model-dependent variability, highlighting important limitations of current small LLMs for safety-critical control tasks.

