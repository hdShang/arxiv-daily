---
layout: default
title: ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body
---

# ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14234" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14234v1</a>
  <a href="https://arxiv.org/pdf/2512.14234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14234v1" onclick="toggleFavorite(this, '2512.14234v1', 'ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juze Zhang, Changan Chen, Xin Chen, Heng Yu, Tiange Xiang, Ali Sartaz Khan, Shrinidhi K. Lakshmikanth, Ehsan Adeli

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://ai.stanford.edu/~juze/ViBES/

---

## 💡 一句话要点

**ViBES：一种具有行为智能的3D虚拟化身对话代理**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)**

**关键词**: `对话代理` `3D虚拟化身` `行为智能` `多模态融合` `语音语言行为模型`

## 📋 核心要点

1. 现有对话系统在生成虚拟化身行为时，缺乏自主决策能力，导致动作时序不自然，社交互动性弱。
2. ViBES通过联合规划语言和动作，并执行对话条件下的身体动作，实现更自然的虚拟化身行为。
3. 实验表明，ViBES在多轮对话中，对话-动作对齐和行为质量方面，均优于现有协同语音和文本到动作基线。

## 📝 摘要（中文）

人类交流本质上是多模态和社交的：语言、韵律和肢体语言共同传递意图。然而，大多数现有系统将人类行为建模为翻译任务，例如语音协同手势或文本到动作的映射，即将固定的语句映射到动作片段，而不需要代理自主决策何时移动、做什么或如何在多轮对话中适应。这导致了脆弱的时序、薄弱的社交基础以及碎片化的堆栈，其中语音、文本和动作被孤立地训练或推断。我们介绍了ViBES（语音在行为表达和同步中的体现），一个对话式3D代理，它联合规划语言和动作，并执行对话条件下的身体动作。具体来说，ViBES是一个语音-语言-行为（SLB）模型，具有混合模态专家（MoME）骨干：用于语音、面部表情和身体运动的模态划分Transformer专家。该模型处理交错的多模态token流，通过模态进行硬路由（参数按专家划分），同时通过跨专家注意力共享信息。通过利用强大的预训练语音语言模型，该代理支持混合主动性交互：用户可以在对话中说话、打字或发出身体动作指令，并且系统公开可控的行为钩子以进行流式响应。我们进一步在多轮对话中进行基准测试，使用对话-动作对齐和行为质量的自动指标，并观察到相对于强大的协同语音和文本到动作基线的持续提升。ViBES超越了“语音条件下的运动生成”，朝着代理虚拟化身的方向发展，其中语言、韵律和运动被联合生成，从而实现可控的、具有社交能力的3D交互。

## 🔬 方法详解

**问题定义**：现有对话系统在驱动3D虚拟化身时，通常采用将文本或语音直接映射到预定义的动作片段的方法。这种方法缺乏对上下文的理解和自主决策能力，导致生成的动作时序僵硬、缺乏社交互动性，无法自然地融入多轮对话中。现有方法将语音、文本和动作孤立地训练或推断，忽略了它们之间的内在联系。

**核心思路**：ViBES的核心思路是将语言、韵律和运动进行联合建模，使虚拟化身能够根据对话上下文自主地规划和执行动作。通过引入行为智能，ViBES能够更好地理解用户的意图，并生成更自然、更具社交性的行为。

**技术框架**：ViBES采用语音-语言-行为（SLB）模型，其核心是混合模态专家（MoME）骨干网络。该网络包含针对语音、面部表情和身体运动的模态划分Transformer专家。模型接收交错的多模态token流作为输入，并通过模态进行硬路由，将不同模态的信息传递给相应的专家。同时，通过跨专家注意力机制，实现不同模态之间的信息共享和融合。模型利用预训练的语音语言模型，支持混合主动性交互，允许用户在对话中随时输入语音、文本或动作指令。

**关键创新**：ViBES的关键创新在于其联合规划语言和动作的能力。与传统的“语音条件下的运动生成”方法不同，ViBES能够根据对话上下文自主地决策何时移动、做什么动作，从而生成更自然、更具社交性的行为。MoME架构允许模型针对不同模态进行专门优化，同时通过跨专家注意力实现模态间的信息融合。

**关键设计**：ViBES的关键设计包括：1) 使用模态划分的Transformer专家网络，针对不同模态进行专门优化；2) 采用跨专家注意力机制，实现模态间的信息共享和融合；3) 利用预训练的语音语言模型，提高模型的语言理解能力；4) 提供可控的行为钩子，允许用户对虚拟化身的行为进行实时控制。具体的参数设置、损失函数和网络结构等细节将在论文中详细描述（未知）。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14234v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14234v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14234v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ViBES在多轮对话的基准测试中表现出色，通过自动指标评估对话-动作对齐和行为质量，结果表明ViBES显著优于现有的协同语音和文本到动作的基线模型。具体的性能提升数据将在论文中详细给出（未知）。

## 🎯 应用场景

ViBES具有广泛的应用前景，包括虚拟助手、在线教育、游戏、社交娱乐等领域。它可以用于创建更具吸引力和互动性的虚拟化身，提升用户体验。例如，在在线教育中，ViBES可以生成更生动的教学内容，帮助学生更好地理解知识。在游戏中，ViBES可以创建更逼真的角色，增强游戏的沉浸感。

## 📄 摘要（原文）

> Human communication is inherently multimodal and social: words, prosody, and body language jointly carry intent. Yet most prior systems model human behavior as a translation task co-speech gesture or text-to-motion that maps a fixed utterance to motion clips-without requiring agentic decision-making about when to move, what to do, or how to adapt across multi-turn dialogue. This leads to brittle timing, weak social grounding, and fragmented stacks where speech, text, and motion are trained or inferred in isolation. We introduce ViBES (Voice in Behavioral Expression and Synchrony), a conversational 3D agent that jointly plans language and movement and executes dialogue-conditioned body actions. Concretely, ViBES is a speech-language-behavior (SLB) model with a mixture-of-modality-experts (MoME) backbone: modality-partitioned transformer experts for speech, facial expression, and body motion. The model processes interleaved multimodal token streams with hard routing by modality (parameters are split per expert), while sharing information through cross-expert attention. By leveraging strong pretrained speech-language models, the agent supports mixed-initiative interaction: users can speak, type, or issue body-action directives mid-conversation, and the system exposes controllable behavior hooks for streaming responses. We further benchmark on multi-turn conversation with automatic metrics of dialogue-motion alignment and behavior quality, and observe consistent gains over strong co-speech and text-to-motion baselines. ViBES goes beyond "speech-conditioned motion generation" toward agentic virtual bodies where language, prosody, and movement are jointly generated, enabling controllable, socially competent 3D interaction. Code and data will be made available at: ai.stanford.edu/~juze/ViBES/

