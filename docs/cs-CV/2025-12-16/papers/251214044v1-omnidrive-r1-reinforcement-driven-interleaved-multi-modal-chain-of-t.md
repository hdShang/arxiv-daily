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

**OmniDrive-R1：强化学习驱动的交错多模态CoT，提升自动驾驶视觉语言模型的可靠性**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)** **自动驾驶 (Autonomous Driving)**

**关键词**: `自动驾驶` `视觉语言模型` `多模态推理` `强化学习` `思维链` `视觉 grounding` `跨模态一致性`

## 📋 核心要点

1. 现有视觉语言模型在自动驾驶中存在对象幻觉问题，源于对无根据文本CoT推理的依赖，且感知与推理解耦。
2. OmniDrive-R1提出交错多模态CoT机制，通过强化学习驱动视觉 grounding，使模型自主关注关键区域。
3. 在DriveLMM-o1数据集上，OmniDrive-R1显著提升了推理得分和答案准确率，优于基线模型Qwen2.5VL-7B。

## 📝 摘要（中文）

视觉语言模型(VLMs)在自动驾驶(AD)等安全关键领域的部署受到可靠性问题的严重阻碍，尤其是对象幻觉。这种失败源于它们对无根据的、基于文本的思维链(CoT)推理的依赖。现有的多模态CoT方法试图缓解这个问题，但存在两个根本缺陷：(1)解耦的感知和推理阶段，阻止了端到端的联合优化；(2)依赖于昂贵的、密集的定位标签。因此，我们引入了OmniDrive-R1，这是一个为自动驾驶设计的端到端VLM框架，它通过交错多模态CoT(iMCoT)机制统一了感知和推理。我们的核心创新是强化学习驱动的视觉 grounding 能力，使模型能够自主地将其注意力导向关键区域，以进行细粒度分析。这种能力由我们的纯两阶段强化学习训练流程和Clip-GRPO算法实现。至关重要的是，Clip-GRPO引入了一种无标注的、基于过程的 grounding 奖励。这种奖励不仅消除了对密集标签的需求，而且通过强制视觉焦点和文本推理之间的实时跨模态一致性，规避了外部工具调用的不稳定性。在DriveLMM-o1上的大量实验证明了我们模型的显著改进。与基线Qwen2.5VL-7B相比，OmniDrive-R1将整体推理得分从51.77%提高到80.35%，最终答案准确率从37.81%提高到73.62%。

## 🔬 方法详解

**问题定义**：现有视觉语言模型在自动驾驶场景中存在对象幻觉问题，导致决策错误。现有的多模态CoT方法要么感知和推理阶段解耦，无法端到端优化，要么依赖于昂贵的密集标注数据，限制了其应用。

**核心思路**：OmniDrive-R1的核心思路是通过交错多模态CoT (iMCoT) 机制，将视觉感知和语言推理紧密结合，实现端到端的联合优化。同时，利用强化学习驱动视觉 grounding，使模型能够自主地关注图像中的关键区域，从而减少对象幻觉。

**技术框架**：OmniDrive-R1是一个端到端的视觉语言模型框架，包含以下主要模块：1) 交错多模态CoT (iMCoT) 模块，用于视觉和语言信息的融合推理；2) 强化学习模块，用于训练视觉 grounding 能力；3) Clip-GRPO 算法，用于提供无标注的 grounding 奖励。整体流程是，模型首先通过iMCoT进行多模态推理，然后利用强化学习模块优化视觉关注机制，最后通过Clip-GRPO算法提供奖励信号，引导模型关注关键区域。

**关键创新**：OmniDrive-R1的关键创新在于：1) 提出了交错多模态CoT (iMCoT) 机制，实现了感知和推理的端到端联合优化；2) 引入了强化学习驱动的视觉 grounding 能力，使模型能够自主地关注图像中的关键区域；3) 提出了 Clip-GRPO 算法，提供了一种无标注的、基于过程的 grounding 奖励，避免了对密集标注数据的依赖。

**关键设计**：OmniDrive-R1使用了两阶段强化学习训练流程。第一阶段，使用预训练的视觉语言模型初始化模型参数。第二阶段，使用 Clip-GRPO 算法训练视觉 grounding 能力。Clip-GRPO 算法的关键在于设计了一种基于过程的 grounding 奖励，该奖励基于视觉焦点和文本推理之间的跨模态一致性。具体的奖励函数设计未知，但强调了实时跨模态一致性。

## 📊 实验亮点

OmniDrive-R1在DriveLMM-o1数据集上取得了显著的性能提升。与基线模型Qwen2.5VL-7B相比，OmniDrive-R1将整体推理得分从51.77%提高到80.35%，提升了28.58个百分点；最终答案准确率从37.81%提高到73.62%，提升了35.81个百分点。这些结果表明，OmniDrive-R1在自动驾驶场景下的视觉语言推理能力得到了显著提升。

## 🎯 应用场景

OmniDrive-R1的研究成果可应用于自动驾驶、机器人导航、智能监控等领域。通过提高视觉语言模型的可靠性和准确性，可以提升自动驾驶系统的安全性，减少事故发生率。此外，该方法还可以应用于其他需要视觉和语言理解的任务，例如图像描述生成、视觉问答等，具有广泛的应用前景。

## 📄 摘要（原文）

> The deployment of Vision-Language Models (VLMs) in safety-critical domains like autonomous driving (AD) is critically hindered by reliability failures, most notably object hallucination. This failure stems from their reliance on ungrounded, text-based Chain-of-Thought (CoT) reasoning.While existing multi-modal CoT approaches attempt mitigation, they suffer from two fundamental flaws: (1) decoupled perception and reasoning stages that prevent end-to-end joint optimization, and (2) reliance on expensive, dense localization labels.Thus we introduce OmniDrive-R1, an end-to-end VLM framework designed for autonomous driving, which unifies perception and reasoning through an interleaved Multi-modal Chain-of-Thought (iMCoT) mechanism. Our core innovation is an Reinforcement-driven visual grounding capability, enabling the model to autonomously direct its attention and "zoom in" on critical regions for fine-grained analysis. This capability is enabled by our pure two-stage reinforcement learning training pipeline and Clip-GRPO algorithm. Crucially, Clip-GRPO introduces an annotation-free, process-based grounding reward. This reward not only eliminates the need for dense labels but also circumvents the instability of external tool calls by enforcing real-time cross-modal consistency between the visual focus and the textual reasoning. Extensive experiments on DriveLMM-o1 demonstrate our model's significant improvements. Compared to the baseline Qwen2.5VL-7B, OmniDrive-R1 improves the overall reasoning score from 51.77% to 80.35%, and the final answer accuracy from 37.81% to 73.62%.

