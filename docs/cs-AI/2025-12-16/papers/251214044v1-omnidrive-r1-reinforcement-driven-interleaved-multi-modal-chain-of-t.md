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

**提出OmniDrive-R1框架，通过强化学习驱动的交错多模态思维链解决自动驾驶中视觉语言模型的可靠性问题**

🎯 **匹配领域**: **自动驾驶** **视觉里程计** **强化学习**

**关键词**: `自动驾驶` `视觉语言模型` `强化学习` `多模态思维链` `视觉接地` `端到端优化` `可靠性提升` `跨模态一致性`

## 📋 核心要点

1. 现有方法存在感知与推理阶段解耦的问题，无法实现端到端联合优化，且依赖昂贵密集的定位标注，限制了自动驾驶中视觉语言模型的可靠性。
2. 论文提出交错多模态思维链机制，通过强化学习驱动的视觉接地能力，使模型能自主聚焦关键区域，实现细粒度分析和实时跨模态一致性。
3. 在DriveLMM-o1数据集上，OmniDrive-R1相比基线模型，整体推理分数提升至80.35%，最终答案准确率提升至73.62%，显著改善性能。

## 📝 摘要（中文）

在自动驾驶等安全关键领域部署视觉语言模型时，可靠性问题（特别是物体幻觉）严重阻碍了其应用。这种失败源于模型依赖未接地的、基于文本的思维链推理。现有的多模态思维链方法虽然尝试缓解这一问题，但存在两个根本缺陷：（1）解耦的感知和推理阶段阻碍了端到端的联合优化；（2）依赖昂贵且密集的定位标注。为此，我们提出了OmniDrive-R1，这是一个专为自动驾驶设计的端到端视觉语言模型框架，通过交错多模态思维链机制统一了感知和推理。我们的核心创新是强化学习驱动的视觉接地能力，使模型能够自主引导注意力并“放大”关键区域进行细粒度分析。这一能力通过我们的纯两阶段强化学习训练流程和Clip-GRPO算法实现。关键的是，Clip-GRPO引入了无需标注的、基于过程的接地奖励。该奖励不仅消除了对密集标注的需求，还通过强制视觉焦点和文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在DriveLMM-o1数据集上的大量实验证明了我们模型的显著改进。与基线Qwen2.5VL-7B相比，OmniDrive-R1将整体推理分数从51.77%提升到80.35%，最终答案准确率从37.81%提升到73.62%。

## 🔬 方法详解

OmniDrive-R1是一个端到端的视觉语言模型框架，专为自动驾驶设计。其核心是交错多模态思维链机制，通过强化学习驱动的视觉接地能力统一感知和推理。关键技术创新包括纯两阶段强化学习训练流程和Clip-GRPO算法，后者引入无需标注的、基于过程的接地奖励，强制视觉焦点与文本推理的实时一致性。与现有方法的主要区别在于：它避免了感知和推理阶段的解耦，实现了端到端优化；同时，不依赖密集定位标注，通过强化学习自主引导注意力，提高了模型的可靠性和效率。

## 📊 实验亮点

在DriveLMM-o1数据集上，OmniDrive-R1相比基线Qwen2.5VL-7B，整体推理分数从51.77%大幅提升至80.35%，最终答案准确率从37.81%提升至73.62%，显示出显著的性能改进和可靠性增强。

## 🎯 应用场景

该研究主要应用于自动驾驶领域，特别是视觉语言模型的部署，以提高在安全关键场景中的可靠性和决策准确性。潜在应用包括智能车辆的环境感知、实时推理和自主导航，有助于推动自动驾驶技术的实际落地和安全性提升。

## 📄 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning.While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels.Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

