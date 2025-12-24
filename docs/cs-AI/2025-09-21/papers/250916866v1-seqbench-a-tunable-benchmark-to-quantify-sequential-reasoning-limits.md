---
layout: default
title: "seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs"
---

# seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16866" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16866v1</a>
  <a href="https://arxiv.org/pdf/2509.16866.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16866v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16866v1', 'seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mohammad Ramezanali, Mo Vazifeh, Paolo Santi

**分类**: cs.AI, cs.CL, cs.LG

**发布日期**: 2025-09-21

---

## 💡 一句话要点

**seqBench：可调基准测试，量化LLM的序列推理能力极限**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `序列推理` `大型语言模型` `基准测试` `逻辑深度` `回溯` `噪声比` `常识推理` `参数化控制`

## 📋 核心要点

1. 现有LLM基准测试缺乏对序列推理能力极限的细粒度控制，难以系统性地分析推理失败的原因。
2. seqBench通过参数化控制逻辑深度、回溯步数和噪声比，实现了对LLM序列推理能力的精确评估。
3. 实验表明，LLM在超过特定逻辑深度后准确率急剧下降，即使在低搜索复杂度下也存在推理失败。

## 📝 摘要（中文）

本文提出seqBench，一个参数化的基准测试，旨在通过精确的多维度控制关键复杂性维度，来探究大型语言模型（LLM）的序列推理能力极限。seqBench允许系统性地改变：（1）逻辑深度，定义为解决任务所需的连续动作数量；（2）最优路径上的回溯步数，量化智能体为了满足延迟的先决条件（例如，遇到锁着的门后取回钥匙）而必须重新访问先前状态的频率；（3）噪声比，定义为关于环境的支持性事实和干扰性事实之间的比率。对最先进的LLM的评估揭示了一种普遍的失败模式：准确率在超过模型特定的逻辑深度后呈指数级下降。与现有基准测试不同，seqBench的细粒度控制有助于对这些推理失败进行有针对性的分析，阐明普遍的缩放规律和统计限制。结果表明，即使是性能最佳的模型在seqBench的结构化推理任务上也系统性地失败，尽管搜索复杂度很小，这突显了它们常识推理能力的关键局限性。seqBench数据集已公开发布，旨在激发对LLM推理的更深入科学探究，以期更清楚地了解其在鲁棒的实际应用中的真正潜力和当前边界。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）在常识推理方面表现出一定的能力，但其序列推理能力，即处理需要按顺序执行多个步骤的任务的能力，仍然存在局限性。现有的基准测试往往缺乏对任务复杂度的细粒度控制，难以系统性地分析LLM在序列推理中失败的原因。因此，需要一个可控的基准测试来量化LLM的序列推理能力极限，并深入了解其推理失败的模式。

**核心思路**：seqBench的核心思路是通过参数化控制任务的多个关键维度（逻辑深度、回溯步数和噪声比），来构建一系列具有不同复杂度的序列推理任务。通过系统性地改变这些参数，可以精确地评估LLM在不同条件下的推理性能，并识别导致推理失败的关键因素。这种方法允许研究人员深入了解LLM的序列推理能力，并为改进LLM的推理能力提供指导。

**技术框架**：seqBench的整体框架包括以下几个主要模块：1) 任务生成器：根据设定的参数（逻辑深度、回溯步数、噪声比）自动生成序列推理任务。2) LLM接口：将生成的任务输入到待评估的LLM中，并获取LLM的输出结果。3) 评估指标：设计了一系列评估指标，用于衡量LLM在不同任务上的推理性能，例如准确率、成功率等。4) 分析工具：提供了一系列分析工具，用于分析LLM的推理失败模式，例如错误类型分析、错误原因分析等。

**关键创新**：seqBench的最重要的技术创新点在于其参数化的任务生成方法，它允许研究人员对任务的复杂度进行精确控制。与现有的基准测试相比，seqBench可以更全面、更深入地评估LLM的序列推理能力。此外，seqBench还提供了一系列分析工具，可以帮助研究人员深入了解LLM的推理失败模式，并为改进LLM的推理能力提供指导。

**关键设计**：seqBench的关键设计包括：1) 逻辑深度的定义：逻辑深度是指解决任务所需的连续动作数量，它反映了任务的复杂程度。2) 回溯步数的定义：回溯步数是指智能体为了满足延迟的先决条件而必须重新访问先前状态的频率，它反映了任务的规划难度。3) 噪声比的定义：噪声比是指关于环境的支持性事实和干扰性事实之间的比率，它反映了任务的信息干扰程度。4) 评估指标的设计：评估指标包括准确率、成功率等，用于衡量LLM在不同任务上的推理性能。

## 📊 实验亮点

实验结果表明，即使是性能最佳的LLM在seqBench的结构化推理任务上也系统性地失败，尤其是在逻辑深度增加时，准确率呈指数级下降。这表明LLM在常识推理方面仍然存在局限性，需要进一步的研究和改进。seqBench提供了一个有价值的平台，用于深入研究LLM的推理能力。

## 🎯 应用场景

seqBench可用于评估和比较不同LLM的序列推理能力，指导LLM的改进和优化。它还可用于研究LLM的推理失败模式，并为开发更鲁棒的LLM提供理论基础。此外，seqBench可以应用于需要复杂推理能力的实际场景，例如智能助手、机器人导航和游戏AI等。

## 📄 摘要（原文）

> We introduce seqBench, a parametrized benchmark for probing sequential reasoning limits in Large Language Models (LLMs) through precise, multi-dimensional control over several key complexity dimensions. seqBench allows systematic variation of (1) the logical depth, defined as the number of sequential actions required to solve the task; (2) the number of backtracking steps along the optimal path, quantifying how often the agent must revisit prior states to satisfy deferred preconditions (e.g., retrieving a key after encountering a locked door); and (3) the noise ratio, defined as the ratio between supporting and distracting facts about the environment. Our evaluations on state-of-the-art LLMs reveal a universal failure pattern: accuracy collapses exponentially beyond a model-specific logical depth. Unlike existing benchmarks, seqBench's fine-grained control facilitates targeted analyses of these reasoning failures, illuminating universal scaling laws and statistical limits, as detailed in this paper alongside its generation methodology and evaluation metrics. We find that even top-performing models systematically fail on seqBench's structured reasoning tasks despite minimal search complexity, underscoring key limitations in their commonsense reasoning capabilities. Designed for future evolution to keep pace with advancing models, the seqBench datasets are publicly released to spur deeper scientific inquiry into LLM reasoning, aiming to establish a clearer understanding of their true potential and current boundaries for robust real-world application.

