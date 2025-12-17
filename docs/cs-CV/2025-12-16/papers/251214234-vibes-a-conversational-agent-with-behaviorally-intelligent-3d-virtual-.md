---
layout: default
title: ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body
---

# ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14234" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14234</a>
  <a href="https://arxiv.org/pdf/2512.14234.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14234" onclick="toggleFavorite(this, '2512.14234', 'ViBES: A Conversational Agent with Behaviorally-Intelligent 3D Virtual Body')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Juze Zhang, Changan Chen, Xin Chen, Heng Yu, Tiange Xiang, Ali Sartaz Khan, Shrinidhi K. Lakshmikanth, Ehsan Adeli

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**ViBES：一个具有行为智能的3D虚拟化身对话代理**

🎯 **匹配领域**: **支柱四：生成式动作 (Generative Motion)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `对话代理` `3D虚拟化身` `行为智能` `多模态融合` `语音语言行为模型`

## 📋 核心要点

1. 现有对话系统在模拟人类交流时，难以实现语言、韵律和肢体语言的自然同步，缺乏自主决策能力。
2. ViBES通过一个语音-语言-行为（SLB）模型，联合规划语言和运动，实现对话驱动的身体动作。
3. 实验表明，ViBES在多轮对话中，对话-运动对齐和行为质量方面，优于现有的语音协同和文本到运动基线。

## 📝 摘要（中文）

人类交流本质上是多模态和社交的：语言、韵律和肢体语言共同传递意图。然而，大多数现有系统将人类行为建模为翻译任务，例如语音协同手势或文本到动作，将固定的语句映射到动作片段，而不需要代理自主决策何时移动、做什么或如何在多轮对话中适应。这导致了脆弱的时序、薄弱的社交基础以及碎片化的堆栈，其中语音、文本和动作被孤立地训练或推断。我们介绍了ViBES（语音行为表达和同步），一个对话式3D代理，它联合规划语言和运动，并执行对话条件下的身体动作。具体来说，ViBES是一个具有混合模态专家（MoME）主干的语音-语言-行为（SLB）模型：用于语音、面部表情和身体运动的模态划分Transformer专家。该模型处理交错的多模态token流，并通过模态进行硬路由（参数按专家划分），同时通过跨专家注意力共享信息。通过利用强大的预训练语音语言模型，该代理支持混合主动交互：用户可以在对话中说话、打字或发出身体动作指令，并且系统公开可控的行为钩子以进行流式响应。我们进一步在多轮对话中以对话-运动对齐和行为质量的自动指标进行基准测试，并观察到相对于强大的语音协同和文本到运动基线的持续提升。ViBES超越了“语音条件运动生成”，朝着代理虚拟化身发展，其中语言、韵律和运动被联合生成，从而实现可控的、具有社交能力的3D交互。

## 🔬 方法详解

**问题定义**：现有对话系统通常将人类行为建模为简单的翻译任务，例如语音到手势或文本到动作的映射，缺乏对何时移动、做什么以及如何适应多轮对话的自主决策能力。这导致生成动作的时序不自然，社交互动能力弱，并且语音、文本和动作的训练是孤立的。

**核心思路**：ViBES的核心思路是构建一个能够联合规划语言和运动的对话代理，使其能够根据对话内容自主地生成合适的身体动作。通过将语音、语言和行为整合到一个统一的模型中，ViBES能够更好地模拟人类交流的自然性和流畅性。

**技术框架**：ViBES采用了一个语音-语言-行为（SLB）模型，其主干是一个混合模态专家（MoME）架构。该架构包含针对语音、面部表情和身体运动的模态划分Transformer专家。模型处理交错的多模态token流，并通过模态进行硬路由，同时通过跨专家注意力机制共享信息。

**关键创新**：ViBES的关键创新在于其联合规划语言和运动的能力，以及其混合模态专家（MoME）架构。MoME架构允许模型针对不同的模态使用不同的专家网络，从而更好地捕捉不同模态的特征。同时，跨专家注意力机制使得不同模态之间可以相互影响，从而实现更自然的对话和动作生成。

**关键设计**：ViBES利用了强大的预训练语音语言模型，以支持混合主动交互。用户可以通过语音、文本或身体动作指令与代理进行交互。系统公开可控的行为钩子，以进行流式响应。模型的训练目标是最大化对话-运动对齐和行为质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14234/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14234/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14234/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

ViBES在多轮对话中进行了基准测试，并使用自动指标评估了对话-运动对齐和行为质量。实验结果表明，ViBES在这些指标上均优于现有的语音协同和文本到运动基线。这表明ViBES能够生成更自然、更具社交能力的对话和动作。

## 🎯 应用场景

ViBES具有广泛的应用前景，例如虚拟助手、在线教育、游戏和娱乐等领域。它可以用于创建更具吸引力和互动性的虚拟角色，从而改善用户体验。此外，ViBES还可以用于研究人类交流的本质，并为开发更智能的人工智能系统提供新的思路。

## 📄 摘要（原文）

> Human communication is inherently multimodal and social: words, prosody, and body language jointly carry intent. Yet most prior systems model human behavior as a translation task co-speech gesture or text-to-motion that maps a fixed utterance to motion clips-without requiring agentic decision-making about when to move, what to do, or how to adapt across multi-turn dialogue. This leads to brittle timing, weak social grounding, and fragmented stacks where speech, text, and motion are trained or inferred in isolation. We introduce ViBES (Voice in Behavioral Expression and Synchrony), a conversational 3D agent that jointly plans language and movement and executes dialogue-conditioned body actions. Concretely, ViBES is a speech-language-behavior (SLB) model with a mixture-of-modality-experts (MoME) backbone: modality-partitioned transformer experts for speech, facial expression, and body motion. The model processes interleaved multimodal token streams with hard routing by modality (parameters are split per expert), while sharing information through cross-expert attention. By leveraging strong pretrained speech-language models, the agent supports mixed-initiative interaction: users can speak, type, or issue body-action directives mid-conversation, and the system exposes controllable behavior hooks for streaming responses. We further benchmark on multi-turn conversation with automatic metrics of dialogue-motion alignment and behavior quality, and observe consistent gains over strong co-speech and text-to-motion baselines. ViBES goes beyond "speech-conditioned motion generation" toward agentic virtual bodies where language, prosody, and movement are jointly generated, enabling controllable, socially competent 3D interaction. Code and data will be made available at:this http URL

