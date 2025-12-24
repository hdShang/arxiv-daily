---
layout: default
title: "BaseReward: A Strong Baseline for Multimodal Reward Model"
---

# BaseReward: A Strong Baseline for Multimodal Reward Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16127" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16127v1</a>
  <a href="https://arxiv.org/pdf/2509.16127.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16127v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16127v1', 'BaseReward: A Strong Baseline for Multimodal Reward Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yi-Fan Zhang, Haihua Yang, Huanyu Zhang, Yang Shi, Zezhou Chen, Haochen Tian, Chaoyou Fu, Haotian Wang, Kai Wu, Bo Cui, Xu Wang, Jianfei Pan, Haotian Wang, Zhang Zhang, Liang Wang

**分类**: cs.CV

**发布日期**: 2025-09-19

---

## 💡 一句话要点

**BaseReward：多模态奖励模型新基准，为MLLM对齐提供实用指南**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态奖励模型` `人类偏好对齐` `大型语言模型` `强化学习` `基准测试`

## 📋 核心要点

1. 现有MLLM奖励模型构建缺乏系统性指导，难以有效对齐人类偏好。
2. 提出BaseReward，通过系统实验分析，优化奖励建模范式、架构、训练和数据。
3. BaseReward在多个基准测试中达到SOTA，并成功应用于实际强化学习流程，提升MLLM性能。

## 📝 摘要（中文）

多模态大型语言模型（MLLM）的快速发展使得将其与人类偏好对齐成为一项关键挑战。奖励模型（RM）是实现此目标的核心技术，但目前学术界和工业界都缺乏构建最先进的多模态奖励模型（MRM）的系统指南。本文通过详尽的实验分析，旨在为构建高性能MRM提供清晰的“配方”。我们系统地研究了MRM开发流程中的每个关键组件，包括奖励建模范式（例如，Naive-RM、基于Critic的RM和生成式RM）、奖励头架构、训练策略、数据整理（涵盖十多个多模态和纯文本偏好数据集）、骨干模型和模型规模以及集成方法。基于这些实验见解，我们推出了BaseReward，这是一个强大而高效的多模态奖励建模基线。BaseReward采用简单而有效的架构，建立在Qwen2.5-VL骨干之上，具有优化的两层奖励头，并在精心策划的高质量多模态和纯文本偏好数据混合上进行训练。我们的结果表明，BaseReward在MM-RLHF-Reward Bench、VL-Reward Bench和Multimodal Reward Bench等主要基准测试中建立了新的SOTA，优于之前的模型。此外，为了验证其在静态基准之外的实际效用，我们将BaseReward集成到真实的强化学习流程中，成功地提高了MLLM在各种感知、推理和对话任务中的性能。这项工作不仅提供了一个顶级的MRM，更重要的是，为社区提供了一个清晰的、经验支持的指南，用于为下一代MLLM开发强大的奖励模型。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态大型语言模型（MLLM）与人类偏好对齐的问题。现有的多模态奖励模型（MRM）构建缺乏系统性的指导，导致难以有效地训练出能够准确反映人类偏好的奖励模型。这阻碍了MLLM在实际应用中的性能提升，尤其是在需要理解和生成多模态内容的任务中。

**核心思路**：论文的核心思路是通过详尽的实验分析，系统地研究MRM开发流程中的各个关键组件，从而为构建高性能MRM提供清晰的指导。通过对不同奖励建模范式、奖励头架构、训练策略、数据整理、骨干模型和模型规模以及集成方法进行对比分析，找到最优的组合方式。

**技术框架**：BaseReward的整体架构基于Qwen2.5-VL骨干模型，并在此基础上构建了一个优化的两层奖励头。训练流程包括：1) 数据收集和整理，构建高质量的多模态和纯文本偏好数据集；2) 模型训练，使用合适的训练策略优化模型参数；3) 模型评估，在多个基准测试中评估模型性能；4) 实际应用，将模型集成到强化学习流程中，验证其在实际任务中的效果。

**关键创新**：论文的关键创新在于提供了一个系统性的MRM构建指南，并通过实验验证了各个组件对模型性能的影响。此外，BaseReward本身也是一个强大的基线模型，其性能优于之前的模型。这种系统性的研究方法和高性能的基线模型为后续研究提供了重要的参考。

**关键设计**：BaseReward的关键设计包括：1) 选择Qwen2.5-VL作为骨干模型，因为它具有强大的多模态理解能力；2) 使用优化的两层奖励头，以提高奖励预测的准确性；3) 精心策划高质量的多模态和纯文本偏好数据混合，以提高模型的泛化能力；4) 采用合适的训练策略，例如学习率调整和正则化方法，以防止过拟合。

## 📊 实验亮点

BaseReward在MM-RLHF-Reward Bench、VL-Reward Bench和Multimodal Reward Bench等主要基准测试中取得了SOTA性能，超越了之前的模型。此外，将其集成到实际强化学习流程中，成功提升了MLLM在感知、推理和对话任务中的表现，验证了其在真实场景中的有效性。

## 🎯 应用场景

该研究成果可广泛应用于多模态大型语言模型的对齐训练，提升模型在图像理解、视频分析、人机对话等领域的性能。通过更精准地捕捉人类偏好，可以使MLLM在实际应用中更加智能、可靠，例如智能客服、自动驾驶、医疗诊断等。

## 📄 摘要（原文）

> The rapid advancement of Multimodal Large Language Models (MLLMs) has made aligning them with human preferences a critical challenge. Reward Models (RMs) are a core technology for achieving this goal, but a systematic guide for building state-of-the-art Multimodal Reward Models (MRMs) is currently lacking in both academia and industry. Through exhaustive experimental analysis, this paper aims to provide a clear ``recipe'' for constructing high-performance MRMs. We systematically investigate every crucial component in the MRM development pipeline, including \textit{reward modeling paradigms} (e.g., Naive-RM, Critic-based RM, and Generative RM), \textit{reward head architecture}, \textit{training strategies}, \textit{data curation} (covering over ten multimodal and text-only preference datasets), \textit{backbone model} and \textit{model scale}, and \textit{ensemble methods}.
>   Based on these experimental insights, we introduce \textbf{BaseReward}, a powerful and efficient baseline for multimodal reward modeling. BaseReward adopts a simple yet effective architecture, built upon a {Qwen2.5-VL} backbone, featuring an optimized two-layer reward head, and is trained on a carefully curated mixture of high-quality multimodal and text-only preference data. Our results show that BaseReward establishes a new SOTA on major benchmarks such as MM-RLHF-Reward Bench, VL-Reward Bench, and Multimodal Reward Bench, outperforming previous models. Furthermore, to validate its practical utility beyond static benchmarks, we integrate BaseReward into a real-world reinforcement learning pipeline, successfully enhancing an MLLM's performance across various perception, reasoning, and conversational tasks. This work not only delivers a top-tier MRM but, more importantly, provides the community with a clear, empirically-backed guide for developing robust reward models for the next generation of MLLMs.

