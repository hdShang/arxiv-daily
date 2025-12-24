---
layout: default
title: "CVBench: Evaluating Cross-Video Synergies for Complex Multimodal Understanding and Reasoning"
---

# CVBench: Evaluating Cross-Video Synergies for Complex Multimodal Understanding and Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19542" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19542v2</a>
  <a href="https://arxiv.org/pdf/2508.19542.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19542v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19542v2', 'CVBench: Evaluating Cross-Video Synergies for Complex Multimodal Understanding and Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nannan Zhu, Yonghao Dong, Teng Wang, Xueqian Li, Shengjun Deng, Yijia Wang, Zheng Hong, Tiantian Geng, Guo Niu, Hanyan Huang, Xiongfei Yao, Shuaiwei Jiao

**分类**: cs.CV

**发布日期**: 2025-08-27 (更新: 2025-08-28)

**🔗 代码/项目**: [GITHUB](https://github.com/Hokhim2/CVBench)

---

## 💡 一句话要点

**提出CVBench以解决多视频关系推理评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多视频推理` `跨视频关联` `多模态学习` `大型语言模型` `基准评估`

## 📋 核心要点

1. 现有的多模态大型语言模型在处理多视频任务时表现不足，尤其在跨视频关系推理方面存在显著的性能差距。
2. 本文提出CVBench基准，通过1000对问答评估模型在跨视频对象和事件关联及复杂推理中的能力，填补了这一研究空白。
3. 实验结果显示，顶尖模型在因果推理任务中的准确率仅为60%，而人类表现达到91%，揭示了当前模型的关键瓶颈。

## 📝 摘要（中文）

尽管多模态大型语言模型（MLLMs）在单视频任务上表现优异，但其在多视频场景下的能力仍未得到充分探索。为填补这一空白，本文提出了CVBench，这是第一个全面的基准，旨在严格评估跨视频关系推理。CVBench包含1000对问答，涵盖跨视频对象关联、事件关联和复杂推理三个层次，挑战模型在动态视觉上下文中综合信息。对10多种领先的MLLMs进行广泛评估，发现即使是顶尖模型在因果推理任务上的准确率也仅为60%，远低于人类的91%。分析揭示了当前MLLM架构的根本瓶颈，特别是在跨视频上下文保留和重叠实体消歧方面的不足。

## 🔬 方法详解

**问题定义**：本文旨在解决多模态大型语言模型在跨视频关系推理中的不足，现有方法在多视频场景下的能力评估尚不充分，导致实际应用受限。

**核心思路**：通过构建CVBench基准，系统评估模型在跨视频对象关联、事件关联和复杂推理任务中的表现，提供全面的性能分析。

**技术框架**：CVBench由1000对问答组成，分为三个层次：跨视频对象关联、跨视频事件关联和跨视频复杂推理，涵盖多种领域的视频数据。评估过程包括对10多种MLLMs的零-shot和链式思维提示的测试。

**关键创新**：CVBench是首个针对跨视频推理的综合基准，揭示了当前MLLM在处理多视频信息时的根本瓶颈，尤其是在上下文保留和实体消歧方面的不足。

**关键设计**：在评估过程中，采用了多种提示策略，并对模型在不同任务中的表现进行了详细分析，确保评估的全面性和准确性。通过对比人类表现，揭示了模型的潜在改进方向。

## 📊 实验亮点

实验结果显示，尽管顶尖模型如GPT-4o在因果推理任务中的表现仅为60%的准确率，但人类的表现达到了91%。这一发现突显了当前多模态大型语言模型在跨视频推理中的关键瓶颈，尤其是在上下文保留和实体消歧方面的不足。

## 🎯 应用场景

CVBench的研究成果在多个领域具有潜在应用价值，包括多摄像头监控、跨视频程序学习等。通过提升多视频理解能力，能够推动智能监控系统的进步，增强人机交互体验，并为未来的多模态AI系统提供重要的理论基础和实践指导。

## 📄 摘要（原文）

> While multimodal large language models (MLLMs) exhibit strong performance on single-video tasks (e.g., video question answering), their ability across multiple videos remains critically underexplored. However, this capability is essential for real-world applications, including multi-camera surveillance and cross-video procedural learning. To bridge this gap, we present CVBench, the first comprehensive benchmark designed to assess cross-video relational reasoning rigorously. CVBench comprises 1,000 question-answer pairs spanning three hierarchical tiers: cross-video object association (identifying shared entities), cross-video event association (linking temporal or causal event chains), and cross-video complex reasoning (integrating commonsense and domain knowledge). Built from five domain-diverse video clusters (e.g., sports, life records), the benchmark challenges models to synthesise information across dynamic visual contexts. Extensive evaluation of 10+ leading MLLMs (including GPT-4o, Gemini-2.0-flash, Qwen2.5-VL) under zero-shot or chain-of-thought prompting paradigms. Key findings reveal stark performance gaps: even top models, such as GPT-4o, achieve only 60% accuracy on causal reasoning tasks, compared to the 91% accuracy of human performance. Crucially, our analysis reveals fundamental bottlenecks inherent in current MLLM architectures, notably deficient inter-video context retention and poor disambiguation of overlapping entities. CVBench establishes a rigorous framework for diagnosing and advancing multi-video reasoning, offering architectural insights for next-generation MLLMs. The data and evaluation code are available at https://github.com/Hokhim2/CVBench.

