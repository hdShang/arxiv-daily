---
layout: default
title: VideoSSR: Video Self-Supervised Reinforcement Learning
---

# VideoSSR: Video Self-Supervised Reinforcement Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06281" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06281v1</a>
  <a href="https://arxiv.org/pdf/2511.06281.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06281v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.06281v1', 'VideoSSR: Video Self-Supervised Reinforcement Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zefeng He, Xiaoye Qu, Yafu Li, Siyuan Huang, Daizong Liu, Yu Cheng

**分类**: cs.CV

**发布日期**: 2025-11-09

**🔗 代码/项目**: [GITHUB](https://github.com/lcqysl/VideoSSR)

---

## 💡 一句话要点

**提出VideoSSR，利用视频自监督强化学习提升多模态大语言模型的视频理解能力。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频理解` `自监督学习` `强化学习` `多模态大语言模型` `视频问答`

## 📋 核心要点

1. 现有视频数据集难以满足快速发展的多模态大语言模型的需求，而人工标注高质量数据成本高昂。
2. VideoSSR利用视频内在信息自监督生成高质量、可验证的训练数据，通过强化学习提升模型性能。
3. 实验表明，VideoSSR在多个视频理解基准测试中持续提升模型性能，平均提升超过5%。

## 📝 摘要（中文）

本文研究了如何利用视频中丰富的内在信息来自我生成高质量、可验证的训练数据，以提升多模态大语言模型（MLLM）的视频理解能力。为此，作者提出了三个自监督预训练任务：异常定位、物体计数和时间拼图，并构建了视频内在理解基准（VIUBench）来验证这些任务的难度。实验表明，当前最先进的MLLM在这些任务上表现不佳。基于这些预训练任务，作者构建了VideoSSR-30K数据集，并提出了VideoSSR，一种用于RLVR的视频自监督强化学习框架。在涵盖四个主要视频领域（通用视频问答、长视频问答、时间定位和复杂推理）的17个基准测试中，广泛的实验表明VideoSSR能够持续提升模型性能，平均提升超过5%。这些结果表明VideoSSR是开发更高级MLLM视频理解能力的强大基础框架。

## 🔬 方法详解

**问题定义**：现有视频数据集的复杂度和规模已经无法满足快速发展的多模态大语言模型（MLLM）的需求。人工标注新的高质量视频数据成本高昂，限制了MLLM在视频理解方面的进一步发展。因此，如何高效地获取高质量的视频训练数据成为一个关键问题。

**核心思路**：论文的核心思路是利用视频本身所蕴含的丰富信息，通过自监督学习的方式，自动生成高质量、可验证的训练数据。这种方法避免了昂贵的人工标注，并且能够充分挖掘视频数据的内在价值，从而提升MLLM的视频理解能力。

**技术框架**：VideoSSR框架主要包含以下几个阶段：1) 自监督预训练任务设计：设计了Anomaly Grounding（异常定位）、Object Counting（物体计数）和Temporal Jigsaw（时间拼图）三个自监督预训练任务，用于挖掘视频的内在信息。2) VideoSSR-30K数据集构建：基于上述预训练任务，构建了一个大规模的自监督视频数据集VideoSSR-30K。3) 强化学习训练：利用VideoSSR-30K数据集，采用强化学习方法训练MLLM，提升其视频理解能力。

**关键创新**：VideoSSR的关键创新在于提出了一个完整的视频自监督强化学习框架，该框架能够自动生成高质量的训练数据，并利用强化学习方法提升MLLM的视频理解能力。与传统的监督学习方法相比，VideoSSR无需人工标注数据，能够更高效地利用视频数据。

**关键设计**：在自监督预训练任务设计方面，Anomaly Grounding旨在让模型学习识别视频中的异常事件；Object Counting旨在让模型学习视频中物体的数量；Temporal Jigsaw旨在让模型学习视频的时间顺序。在强化学习训练方面，采用了Reinforcement Learning with Verifiable Rewards (RLVR)框架，并根据不同的视频理解任务设计了相应的奖励函数。

## 📊 实验亮点

实验结果表明，VideoSSR在17个视频理解基准测试中均取得了显著的性能提升，平均提升超过5%。具体来说，在通用视频问答、长视频问答、时间定位和复杂推理等任务上，VideoSSR都优于现有的基线方法，证明了其有效性和泛化能力。这些结果表明，VideoSSR是一种很有潜力的视频自监督学习框架，能够有效提升MLLM的视频理解能力。

## 🎯 应用场景

VideoSSR具有广泛的应用前景，可应用于智能监控、自动驾驶、视频搜索、智能客服等领域。通过提升MLLM的视频理解能力，可以实现更智能化的视频分析和处理，例如自动识别监控视频中的异常行为、理解自动驾驶车辆周围的交通状况、根据用户query检索相关视频内容、以及为用户提供更精准的视频问答服务。未来，VideoSSR有望成为构建更强大的视频智能系统的关键技术。

## 📄 摘要（原文）

> Reinforcement Learning with Verifiable Rewards (RLVR) has substantially advanced the video understanding capabilities of Multimodal Large Language Models (MLLMs). However, the rapid progress of MLLMs is outpacing the complexity of existing video datasets, while the manual annotation of new, high-quality data remains prohibitively expensive. This work investigates a pivotal question: Can the rich, intrinsic information within videos be harnessed to self-generate high-quality, verifiable training data? To investigate this, we introduce three self-supervised pretext tasks: Anomaly Grounding, Object Counting, and Temporal Jigsaw. We construct the Video Intrinsic Understanding Benchmark (VIUBench) to validate their difficulty, revealing that current state-of-the-art MLLMs struggle significantly on these tasks. Building upon these pretext tasks, we develop the VideoSSR-30K dataset and propose VideoSSR, a novel video self-supervised reinforcement learning framework for RLVR. Extensive experiments across 17 benchmarks, spanning four major video domains (General Video QA, Long Video QA, Temporal Grounding, and Complex Reasoning), demonstrate that VideoSSR consistently enhances model performance, yielding an average improvement of over 5\%. These results establish VideoSSR as a potent foundational framework for developing more advanced video understanding in MLLMs. The code is available at https://github.com/lcqysl/VideoSSR.

