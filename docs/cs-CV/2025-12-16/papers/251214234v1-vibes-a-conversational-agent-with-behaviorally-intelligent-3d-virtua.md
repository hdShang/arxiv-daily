---
layout: default
title: ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body
---

# ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14234" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14234v1</a>
  <a href="https://arxiv.org/pdf/2512.14234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14234v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14234v1', 'ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juze Zhang, Changan Chen, Xin Chen, Heng Yu, Tiange Xiang, Ali Sartaz Khan, Shrinidhi K. Lakshmikanth, Ehsan Adeli

**分类**: cs.CV

**发布日期**: 2025-12-16

**备注**: Project page: https://ai.stanford.edu/~juze/ViBES/

---

## 💡 一句话要点

**ViBES：一种具有行为智能的3D虚拟身体对话代理**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对话代理` `3D虚拟身体` `行为智能` `多模态融合` `语音语言行为模型`

## 📋 核心要点

1. 现有对话系统在生成虚拟人物行为时，缺乏对时序、社交互动和多轮对话的有效建模。
2. ViBES通过联合规划语言和运动，并执行对话条件下的身体动作，实现了更自然的交互。
3. 实验表明，ViBES在对话-运动对齐和行为质量方面优于现有的协同语音和文本到运动基线。

## 📝 摘要（中文）

人类交流本质上是多模态和社交的：语言、韵律和肢体语言共同传递意图。然而，大多数现有系统将人类行为建模为翻译任务，例如语音协同手势或文本到动作，将固定的语句映射到动作片段，而不需要代理在何时移动、做什么或如何在多轮对话中适应做出决策。这导致了脆弱的时序、薄弱的社交基础以及碎片化的堆栈，其中语音、文本和动作被孤立地训练或推断。我们引入了ViBES（行为表达和同步中的语音），一个对话式3D代理，它联合规划语言和运动，并执行对话条件下的身体动作。具体来说，ViBES是一个语音-语言-行为（SLB）模型，具有混合模态专家（MoME）骨干：用于语音、面部表情和身体运动的模态划分Transformer专家。该模型处理交错的多模态token流，并通过模态进行硬路由（参数按专家划分），同时通过跨专家注意力共享信息。通过利用强大的预训练语音语言模型，该代理支持混合主动交互：用户可以在对话中说话、打字或发出身体动作指令，并且系统公开可控的行为钩子以进行流式响应。我们进一步在多轮对话中，使用对话-运动对齐和行为质量的自动指标进行基准测试，并观察到相对于强大的协同语音和文本到运动基线的持续收益。ViBES超越了“语音条件运动生成”，朝着代理虚拟身体发展，其中语言、韵律和运动被联合生成，从而实现可控的、具有社交能力的3D交互。

## 🔬 方法详解

**问题定义**：现有对话系统在生成虚拟人物行为时，通常将语音、文本和动作孤立地训练或推断，导致生成的行为时序不自然，缺乏社交互动能力，难以适应多轮对话中的复杂情况。这些方法通常依赖于将固定语句映射到预定义的动作片段，缺乏代理的自主决策能力。

**核心思路**：ViBES的核心思路是构建一个能够联合规划语言和运动的对话代理。通过将语音、语言和行为整合到一个统一的模型中，ViBES能够根据对话上下文生成更自然、更具社交性的身体动作。这种联合建模允许代理在多轮对话中进行更灵活的响应，并支持混合主动交互。

**技术框架**：ViBES采用了一种语音-语言-行为（SLB）模型，其骨干网络是混合模态专家（MoME）。该模型包含针对语音、面部表情和身体运动的模态划分Transformer专家。模型处理交错的多模态token流，并通过模态进行硬路由，同时通过跨专家注意力机制共享信息。用户可以通过语音、文本或身体动作指令与ViBES进行交互，系统则通过可控的行为钩子进行流式响应。

**关键创新**：ViBES的关键创新在于其联合建模语言和运动的能力，以及其混合模态专家（MoME）架构。MoME架构允许模型针对不同的模态使用不同的专家网络，从而更好地捕捉各个模态的特征。同时，跨专家注意力机制使得不同模态之间可以相互影响，从而生成更协调一致的行为。

**关键设计**：ViBES的关键设计包括：1) 使用预训练的语音语言模型来增强语言理解能力；2) 采用模态划分Transformer专家来处理不同模态的信息；3) 设计跨专家注意力机制来实现模态之间的信息共享；4) 提供可控的行为钩子，允许用户对生成的行为进行干预。

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

ViBES在多轮对话的基准测试中表现出色，通过对话-运动对齐和行为质量的自动指标评估，ViBES相较于强大的协同语音和文本到运动基线取得了持续的性能提升。这些结果表明，ViBES能够生成更自然、更具社交性的虚拟人物行为，从而提升用户体验。

## 🎯 应用场景

ViBES具有广泛的应用前景，包括虚拟助手、在线教育、游戏、社交娱乐等领域。它可以用于创建更具吸引力和互动性的虚拟角色，提升用户体验。例如，在在线教育中，ViBES可以作为虚拟教师，通过自然的语言和肢体语言与学生进行互动，提高学习效果。在游戏中，ViBES可以作为非玩家角色（NPC），与玩家进行更真实的对话和互动。

## 📄 摘要（原文）

> Human communication is inherently multimodal and social: words, prosody, and body language jointly carry intent. Yet most prior systems model human behavior as a translation task co-speech gesture or text-to-motion that maps a fixed utterance to motion clips-without requiring agentic decision-making about when to move, what to do, or how to adapt across multi-turn dialogue. This leads to brittle timing, weak social grounding, and fragmented stacks where speech, text, and motion are trained or inferred in isolation. We introduce ViBES (Voice in Behavioral Expression and Synchrony), a conversational 3D agent that jointly plans language and movement and executes dialogue-conditioned body actions. Concretely, ViBES is a speech-language-behavior (SLB) model with a mixture-of-modality-experts (MoME) backbone: modality-partitioned transformer experts for speech, facial expression, and body motion. The model processes interleaved multimodal token streams with hard routing by modality (parameters are split per expert), while sharing information through cross-expert attention. By leveraging strong pretrained speech-language models, the agent supports mixed-initiative interaction: users can speak, type, or issue body-action directives mid-conversation, and the system exposes controllable behavior hooks for streaming responses. We further benchmark on multi-turn conversation with automatic metrics of dialogue-motion alignment and behavior quality, and observe consistent gains over strong co-speech and text-to-motion baselines. ViBES goes beyond "speech-conditioned motion generation" toward agentic virtual bodies where language, prosody, and movement are jointly generated, enabling controllable, socially competent 3D interaction. Code and data will be made available at: ai.stanford.edu/~juze/ViBES/

