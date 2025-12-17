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

1. 现有多模态思维链方法存在感知与推理阶段解耦、依赖密集标注的问题，导致自动驾驶中视觉语言模型可靠性不足。
2. 提出交错多模态思维链机制，通过强化学习驱动的视觉接地能力实现端到端联合优化，无需密集标注。
3. 在DriveLMM-o1数据集上，整体推理分数提升28.58个百分点，最终答案准确率提升35.81个百分点。

## 📝 摘要（中文）

在自动驾驶等安全关键领域部署视觉语言模型时，可靠性问题（特别是物体幻觉）严重阻碍了其应用。这种问题源于模型依赖未接地的文本思维链推理。现有多模态思维链方法虽然尝试缓解，但存在两个根本缺陷：（1）感知与推理阶段解耦，无法进行端到端联合优化；（2）依赖昂贵密集的定位标注。为此，我们提出了OmniDrive-R1，这是一个为自动驾驶设计的端到端视觉语言模型框架，通过交错多模态思维链机制统一了感知与推理。我们的核心创新是强化学习驱动的视觉接地能力，使模型能够自主引导注意力并“放大”关键区域进行细粒度分析。这一能力通过我们的纯两阶段强化学习训练流程和Clip-GRPO算法实现。关键的是，Clip-GRPO引入了无需标注、基于过程的接地奖励。该奖励不仅消除了对密集标注的需求，还通过强制视觉焦点与文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在DriveLMM-o1数据集上的大量实验表明，我们的模型取得了显著改进。与基线Qwen2.5VL-7B相比，OmniDrive-R1将整体推理分数从51.77%提升到80.35%，最终答案准确率从37.81%提升到73.62%。

## 🔬 方法详解

**问题定义**：论文旨在解决自动驾驶中视觉语言模型因物体幻觉导致的可靠性问题。现有多模态思维链方法存在两个主要痛点：一是感知与推理阶段解耦，限制了端到端优化；二是依赖昂贵密集的定位标注，增加了部署成本。

**核心思路**：论文提出通过交错多模态思维链机制统一感知与推理，利用强化学习驱动的视觉接地能力，使模型能自主聚焦关键区域进行细粒度分析，实现无需密集标注的端到端训练。

**技术框架**：整体架构为端到端视觉语言模型框架，包含交错多模态思维链模块和强化学习训练流程。主要阶段包括：输入多模态数据，通过iMCoT机制进行交错推理，利用Clip-GRPO算法优化视觉接地，输出可靠答案。

**关键创新**：最重要的技术创新是强化学习驱动的视觉接地能力，通过Clip-GRPO算法引入基于过程的接地奖励，实现实时跨模态一致性，与现有方法相比，本质区别在于消除了标注依赖和外部工具调用。

**关键设计**：采用纯两阶段强化学习训练流程，第一阶段预训练基础模型，第二阶段使用Clip-GRPO算法优化接地奖励；关键参数包括奖励函数中的跨模态一致性约束，网络结构基于视觉语言模型骨干，如Qwen2.5VL-7B变体。

## 📊 实验亮点

在DriveLMM-o1数据集上的实验显示，OmniDrive-R1相比基线Qwen2.5VL-7B，整体推理分数从51.77%提升至80.35%，绝对提升28.58个百分点；最终答案准确率从37.81%提升至73.62%，绝对提升35.81个百分点，显著改善了自动驾驶中视觉语言模型的可靠性。

## 🎯 应用场景

该研究主要应用于自动驾驶领域，特别是视觉语言模型在安全关键任务中的部署，如环境感知、决策制定和路径规划。其实际价值在于提高模型的可靠性和安全性，减少物体幻觉风险，未来可能扩展到机器人导航、智能监控等需要多模态推理的场景，推动可信人工智能的发展。

## 📄 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning.While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels.Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

