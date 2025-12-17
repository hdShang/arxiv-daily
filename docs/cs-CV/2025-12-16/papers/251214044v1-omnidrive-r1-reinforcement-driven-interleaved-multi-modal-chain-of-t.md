---
layout: default
title: OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving
---

# OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving

**arXiv**: [2512.14044v1](https://arxiv.org/abs/2512.14044) | [PDF](https://arxiv.org/pdf/2512.14044.pdf)

**作者**: Zhenguo Zhang, Haohan Zhen, Yishen Wang, Le Xu, Tianchen Deng, Xuefeng Chen, Qu Chen, Bo Zhang, Wuxiong Huang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出OmniDrive-R1框架，通过强化驱动的交错多模态思维链解决自动驾驶中视觉语言模型的可靠性问题**

**关键词**: `自动驾驶` `视觉语言模型` `思维链推理` `强化学习` `多模态融合` `端到端优化` `视觉接地` `跨模态一致性`

## 📋 核心要点

1. 现有视觉语言模型在自动驾驶中因物体幻觉等可靠性问题受限，源于文本思维链推理未接地，且多模态方法存在感知与推理解耦、依赖密集标注的缺陷。
2. 提出OmniDrive-R1框架，通过交错多模态思维链统一感知与推理，并利用强化学习驱动视觉接地，实现端到端优化和无需标注的实时跨模态一致性。
3. 在DriveLMM-o1实验中，模型整体推理分数提升至80.35%，最终答案准确率达73.62%，显著优于基线Qwen2.5VL-7B的性能表现。

## 📝 摘要（中文）

在自动驾驶等安全关键领域部署视觉语言模型（VLMs）时，可靠性问题（特别是物体幻觉）严重阻碍了其应用。这种失败源于模型依赖未接地的、基于文本的思维链（CoT）推理。现有的多模态CoT方法试图缓解这一问题，但存在两个根本缺陷：（1）解耦的感知和推理阶段阻碍了端到端的联合优化；（2）依赖昂贵、密集的定位标注。为此，我们提出了OmniDrive-R1，这是一个专为自动驾驶设计的端到端VLM框架，通过交错多模态思维链（iMCoT）机制统一了感知和推理。我们的核心创新是强化驱动的视觉接地能力，使模型能够自主引导注意力并“放大”关键区域进行细粒度分析。这一能力通过我们的纯两阶段强化学习训练流程和Clip-GRPO算法实现。关键的是，Clip-GRPO引入了无需标注、基于过程的接地奖励。该奖励不仅消除了对密集标注的需求，还通过强制视觉焦点与文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在DriveLMM-o1数据集上的大量实验证明了我们模型的显著改进。与基线Qwen2.5VL-7B相比，OmniDrive-R1将整体推理分数从51.77%提升至80.35%，最终答案准确率从37.81%提升至73.62%。

## 🔬 方法详解

OmniDrive-R1是一个端到端的视觉语言模型框架，专为自动驾驶设计。其核心是交错多模态思维链（iMCoT）机制，将感知和推理阶段统一起来，实现联合优化。关键技术创新包括强化驱动的视觉接地能力，使模型能自主聚焦关键区域进行细粒度分析；以及Clip-GRPO算法，该算法通过基于过程的接地奖励，无需密集标注，并强制视觉焦点与文本推理的实时一致性，避免外部工具的不稳定性。与现有方法的主要区别在于：它解决了感知与推理解耦的问题，实现了端到端优化；同时，通过强化学习替代了传统依赖昂贵标注的方法，提高了效率和稳定性。

## 📊 实验亮点

在DriveLMM-o1数据集上，OmniDrive-R1相比基线Qwen2.5VL-7B，整体推理分数从51.77%大幅提升至80.35%，最终答案准确率从37.81%跃升至73.62%，证明了其在自动驾驶推理任务中的显著性能改进。

## 🎯 应用场景

该研究主要应用于自动驾驶领域，特别是视觉语言模型的可靠部署，可提升车辆在复杂环境中的感知和决策能力，减少物体幻觉等安全风险，推动智能交通系统的发展。

## 📄 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning.While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels.Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

