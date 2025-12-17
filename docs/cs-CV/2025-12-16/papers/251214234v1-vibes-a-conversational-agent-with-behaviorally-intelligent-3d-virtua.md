---
layout: default
title: ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body
---

# ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body

**arXiv**: [2512.14234v1](https://arxiv.org/abs/2512.14234) | [PDF](https://arxiv.org/pdf/2512.14234.pdf)

**作者**: Juze Zhang, Changan Chen, Xin Chen, Heng Yu, Tiange Xiang, Ali Sartaz Khan, Shrinidhi K. Lakshmikanth, Ehsan Adeli

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://ai.stanford.edu/~juze/ViBES/

---

## 💡 一句话要点

**提出ViBES对话代理，通过联合规划语言与动作解决多模态交互中的时序与社交基础问题**

🎯 **匹配领域**: **动作生成** **视觉里程计** **强化学习**

**关键词**: `多模态对话代理` `语音-语言-行为模型` `混合模态专家` `3D虚拟身体` `联合规划` `社交交互` `时序同步` `可控行为生成`

## 📋 核心要点

1. 现有方法将人类行为建模为翻译任务，导致时序脆弱、社交基础薄弱和模态孤立，限制了多模态交互的自然性。
2. ViBES采用混合模态专家骨干，通过模态分区Transformer联合处理语音、表情和动作，实现语言与动作的协同规划。
3. 实验显示，ViBES在对话-动作对齐和行为质量上优于基线，支持混合主动交互和可控流式响应，提升社交能力。

## 📝 摘要（中文）

人类交流本质上是多模态和社交性的：语言、韵律和肢体语言共同传达意图。然而，大多数现有系统将人类行为建模为语音伴随手势或文本到动作的翻译任务，将固定话语映射到动作片段，而不需要代理决策何时移动、做什么或如何在多轮对话中适应。这导致脆弱的时序、薄弱的社交基础和碎片化的堆栈，其中语音、文本和动作被孤立地训练或推断。我们介绍了ViBES（语音行为表达与同步），这是一个对话式3D代理，联合规划语言和动作，并执行对话条件化的身体动作。具体来说，ViBES是一个语音-语言-行为（SLB）模型，具有混合模态专家（MoME）骨干：模态分区的Transformer专家用于语音、面部表情和身体动作。该模型通过模态硬路由（参数按专家分割）处理交错的多模态令牌流，同时通过跨专家注意力共享信息。通过利用强大的预训练语音-语言模型，该代理支持混合主动交互：用户可以在对话中说话、打字或发出身体动作指令，系统暴露可控的行为钩子用于流式响应。我们进一步在多轮对话上使用对话-动作对齐和行为质量的自动指标进行基准测试，并观察到相对于强大的语音伴随和文本到动作基线的持续增益。ViBES超越了“语音条件化动作生成”，走向代理虚拟身体，其中语言、韵律和动作被联合生成，实现可控、社交能力强的3D交互。代码和数据将在ai.stanford.edu/~juze/ViBES/提供。

## 🔬 方法详解

ViBES的核心是一个语音-语言-行为（SLB）模型，基于混合模态专家（MoME）架构。整体框架包括模态分区的Transformer专家，分别处理语音、面部表情和身体动作的令牌流，通过硬路由按模态分配参数，同时利用跨专家注意力实现信息共享。关键技术创新在于联合规划语言和动作，而非孤立生成，并集成预训练语音-语言模型以支持多模态输入和输出。与现有方法的主要区别在于从翻译任务转向代理决策，强调时序同步和社交适应性，避免了碎片化堆栈问题。

## 📊 实验亮点

在多轮对话基准测试中，ViBES在对话-动作对齐和行为质量自动指标上均优于语音伴随和文本到动作基线，显示出持续的性能增益，验证了联合规划方法的有效性。

## 🎯 应用场景

该研究可应用于虚拟助手、社交机器人、游戏角色和远程协作系统，通过实现可控、社交能力强的3D交互，提升用户体验和自然沟通，在教育、娱乐和医疗等领域具有实际价值。

## 📄 摘要（原文）

> Human communication is inherently multimodal and social: words, prosody, and body language jointly carry intent. Yet most prior systems model human behavior as a translation task co-speech gesture or text-to-motion that maps a fixed utterance to motion clips-without requiring agentic decision-making about when to move, what to do, or how to adapt across multi-turn dialogue. This leads to brittle timing, weak social grounding, and fragmented stacks where speech, text, and motion are trained or inferred in isolation. We introduce ViBES (Voice in Behavioral Expression and Synchrony), a conversational 3D agent that jointly plans language and movement and executes dialogue-conditioned body actions. Concretely, ViBES is a speech-language-behavior (SLB) model with a mixture-of-modality-experts (MoME) backbone: modality-partitioned transformer experts for speech, facial expression, and body motion. The model processes interleaved multimodal token streams with hard routing by modality (parameters are split per expert), while sharing information through cross-expert attention. By leveraging strong pretrained speech-language models, the agent supports mixed-initiative interaction: users can speak, type, or issue body-action directives mid-conversation, and the system exposes controllable behavior hooks for streaming responses. We further benchmark on multi-turn conversation with automatic metrics of dialogue-motion alignment and behavior quality, and observe consistent gains over strong co-speech and text-to-motion baselines. ViBES goes beyond "speech-conditioned motion generation" toward agentic virtual bodies where language, prosody, and movement are jointly generated, enabling controllable, socially competent 3D interaction. Code and data will be made available at: ai.stanford.edu/~juze/ViBES/

