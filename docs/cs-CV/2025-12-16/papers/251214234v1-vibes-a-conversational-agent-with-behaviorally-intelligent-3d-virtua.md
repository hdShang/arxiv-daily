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

**ViBES：一种具有行为智能的3D虚拟化身对话代理**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)** **动作生成与物理动画 (Animation & Physics)** **3D感知与状态估计 (Perception & State Est)**

**关键词**: `对话代理` `3D虚拟化身` `多模态融合` `行为智能` `混合模态专家`

## 📋 核心要点

1. 现有对话系统在模拟人类多模态交流方面存在不足，缺乏对身体语言的自主规划和控制。
2. ViBES通过联合规划语言和动作，并利用混合模态专家模型，实现了更自然和可控的3D虚拟化身交互。
3. 实验表明，ViBES在对话-动作对齐和行为质量方面优于现有方法，实现了显著的性能提升。

## 📝 摘要（中文）

人类交流本质上是多模态和社交的：语言、韵律和肢体语言共同传递意图。然而，大多数现有系统将人类行为建模为翻译任务，例如语音协同手势或文本到动作，即将固定的语句映射到动作片段，而不需要代理自主决策何时移动、做什么或如何在多轮对话中适应。这导致了时间上的脆弱性、社交基础的薄弱以及语音、文本和动作被孤立训练或推断的碎片化堆栈。我们介绍了ViBES（语音行为表达与同步），一个对话式3D代理，它联合规划语言和动作，并执行对话条件下的身体动作。具体来说，ViBES是一个具有混合模态专家（MoME）主干的语音-语言-行为（SLB）模型：用于语音、面部表情和身体运动的模态划分Transformer专家。该模型处理交错的多模态token流，并通过模态进行硬路由（参数按专家划分），同时通过跨专家注意力共享信息。通过利用强大的预训练语音语言模型，该代理支持混合主动交互：用户可以在对话中说话、打字或发出身体动作指令，并且系统公开可控的行为钩子以进行流式响应。我们进一步在多轮对话中，使用对话-动作对齐和行为质量的自动指标进行基准测试，并观察到相对于强大的协同语音和文本到动作基线的持续提升。ViBES超越了“语音条件下的动作生成”，朝着代理虚拟化身的方向发展，其中语言、韵律和动作被联合生成，从而实现可控的、具有社交能力的3D交互。

## 🔬 方法详解

**问题定义**：现有对话系统难以模拟人类交流中语言、韵律和肢体语言的协同作用。它们通常将行为建模为简单的翻译任务，缺乏自主决策能力，导致时间同步性差、社交互动能力弱，并且各个模态之间缺乏有效的信息共享。

**核心思路**：ViBES的核心思路是构建一个能够联合规划语言和动作的对话代理。通过将语音、面部表情和身体运动整合到一个统一的模型中，ViBES能够更好地理解用户的意图，并生成更自然、更具表现力的响应。

**技术框架**：ViBES采用语音-语言-行为（SLB）模型，其主干是混合模态专家（MoME）。该模型包含针对语音、面部表情和身体运动的模态划分Transformer专家。模型处理交错的多模态token流，并通过模态进行硬路由，同时通过跨专家注意力共享信息。

**关键创新**：ViBES的关键创新在于其混合模态专家架构和联合规划机制。通过将不同模态的信息整合到一个统一的模型中，ViBES能够更好地理解用户的意图，并生成更自然、更具表现力的响应。此外，ViBES还支持混合主动交互，允许用户在对话中随时输入语音、文本或身体动作指令。

**关键设计**：ViBES利用预训练的语音语言模型来提升性能。模型采用模态划分Transformer专家，每个专家负责处理特定的模态信息。跨专家注意力机制用于在不同模态之间共享信息。系统还暴露了可控的行为钩子，用于流式响应。

## 📊 实验亮点

实验结果表明，ViBES在多轮对话中，使用对话-动作对齐和行为质量的自动指标进行基准测试，相对于强大的协同语音和文本到动作基线，取得了持续的性能提升。具体数据指标和提升幅度将在论文中详细展示。

## 🎯 应用场景

ViBES可应用于虚拟助手、在线教育、游戏、社交娱乐等领域。它可以创建更具吸引力和互动性的虚拟化身，从而改善用户体验。未来，ViBES有望成为人机交互的重要组成部分，促进更自然、更高效的交流。

## 📄 摘要（原文）

> Human communication is inherently multimodal and social: words, prosody, and body language jointly carry intent. Yet most prior systems model human behavior as a translation task co-speech gesture or text-to-motion that maps a fixed utterance to motion clips-without requiring agentic decision-making about when to move, what to do, or how to adapt across multi-turn dialogue. This leads to brittle timing, weak social grounding, and fragmented stacks where speech, text, and motion are trained or inferred in isolation. We introduce ViBES (Voice in Behavioral Expression and Synchrony), a conversational 3D agent that jointly plans language and movement and executes dialogue-conditioned body actions. Concretely, ViBES is a speech-language-behavior (SLB) model with a mixture-of-modality-experts (MoME) backbone: modality-partitioned transformer experts for speech, facial expression, and body motion. The model processes interleaved multimodal token streams with hard routing by modality (parameters are split per expert), while sharing information through cross-expert attention. By leveraging strong pretrained speech-language models, the agent supports mixed-initiative interaction: users can speak, type, or issue body-action directives mid-conversation, and the system exposes controllable behavior hooks for streaming responses. We further benchmark on multi-turn conversation with automatic metrics of dialogue-motion alignment and behavior quality, and observe consistent gains over strong co-speech and text-to-motion baselines. ViBES goes beyond "speech-conditioned motion generation" toward agentic virtual bodies where language, prosody, and movement are jointly generated, enabling controllable, socially competent 3D interaction. Code and data will be made available at: ai.stanford.edu/~juze/ViBES/

