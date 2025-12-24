---
layout: default
title: "PersonaFuse: A Personality Activation-Driven Framework for Enhancing Human-LLM Interactions"
---

# PersonaFuse: A Personality Activation-Driven Framework for Enhancing Human-LLM Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07370" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07370v2</a>
  <a href="https://arxiv.org/pdf/2509.07370.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07370v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07370v2', 'PersonaFuse: A Personality Activation-Driven Framework for Enhancing Human-LLM Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yixuan Tang, Yi Yang, Ahmed Abbasi

**分类**: cs.CL

**发布日期**: 2025-09-09 (更新: 2025-09-11)

---

## 💡 一句话要点

**PersonaFuse：基于人格激活的框架，增强人与LLM的交互**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `人格化` `人机交互` `情感计算` `混合专家模型` `特质激活理论` `后训练` `动态路由`

## 📋 核心要点

1. 现有LLM在情感感知和社会能力方面存在局限，无法根据不同情境调整沟通风格。
2. PersonaFuse框架通过混合专家架构和动态路由网络，使LLM能够表达不同人格特质。
3. 实验表明，PersonaFuse在社会情感智能方面显著提升，且不牺牲推理能力和安全性。

## 📝 摘要（中文）

大型语言模型（LLM）的最新进展展示了在各个领域的卓越能力。这些发展促成了人类与LLM之间在各种情境下的更直接沟通，例如社交陪伴和心理支持。然而，LLM在现实对话中常常表现出情感感知和社会能力方面的局限性。这些局限性部分源于它们无法根据不同的社交和任务环境调整其沟通风格和情感表达。本文介绍PersonaFuse，一种新颖的LLM后训练框架，使LLM能够适应并表达不同情境下的人格。受特质激活理论和五大人格模型的启发，PersonaFuse采用混合专家架构，将人格适配器与动态路由网络相结合，从而实现情境化的特质表达。实验结果表明，PersonaFuse在社会情感智能的多个维度上显著优于基线模型。重要的是，这些提升是在不牺牲通用推理能力或模型安全性的前提下实现的，而这仍然是直接提示和监督微调方法的常见局限性。PersonaFuse还在下游以人为本的应用中实现了持续改进，例如心理健康咨询和基于评论的客户服务。最后，针对包括GPT-4o和DeepSeek在内的领先LLM的人工偏好评估表明，尽管PersonaFuse的模型尺寸相对较小，但仍实现了具有竞争力的响应质量。这些发现表明，PersonaFuse为开发具有社会情感增强的LLM提供了一种理论基础扎实且实用的方法，标志着朝着更以人为本的AI系统迈出了重要一步。

## 🔬 方法详解

**问题定义**：现有大型语言模型（LLM）在人机交互中，尤其是在需要情感理解和社交技巧的场景下，表现出明显的局限性。它们难以根据不同的社交情境和任务目标调整自身的表达方式，缺乏足够的情感感知能力，导致交互体验不自然、不流畅。直接提示工程和监督微调等方法虽然可以一定程度上改善这一问题，但往往会牺牲模型的通用推理能力和安全性，或者泛化性较差。

**核心思路**：PersonaFuse的核心思路是借鉴心理学中的特质激活理论和五大人格模型，构建一个能够动态激活不同人格特质的LLM框架。通过将不同的人格特质解耦为独立的模块（人格适配器），并利用动态路由网络根据上下文情境选择合适的适配器组合，从而使LLM能够灵活地表达不同的人格，提升其在社交和情感交互中的表现。这种方法旨在使LLM更具适应性和情境感知能力，从而实现更自然、更有效的交流。

**技术框架**：PersonaFuse采用混合专家（Mixture-of-Experts, MoE）架构，主要包含以下几个关键模块：1) 预训练的LLM backbone：作为基础模型，提供通用的语言理解和生成能力。2) 人格适配器（Persona Adapters）：每个适配器代表一种特定的人格特质，例如外向性、责任心等。这些适配器通过轻量级的参数更新，学习特定人格的表达方式。3) 动态路由网络（Dynamic Routing Network）：根据输入的上下文信息，动态地选择激活哪些人格适配器。该网络通常由一个或多个全连接层组成，输出每个适配器的权重。4) 融合层（Fusion Layer）：将LLM backbone的输出和激活的人格适配器的输出进行融合，生成最终的响应。

**关键创新**：PersonaFuse的关键创新在于其动态人格激活机制。与以往直接对LLM进行微调或提示工程的方法不同，PersonaFuse将人格特质解耦为独立的模块，并通过动态路由网络根据上下文情境选择性地激活这些模块。这种方法不仅提高了模型的灵活性和适应性，还避免了对整个模型进行大规模的微调，从而降低了训练成本，并保持了模型的通用推理能力和安全性。

**关键设计**：PersonaFuse的关键设计包括：1) 人格适配器的设计：采用轻量级的适配器结构，例如Adapter layers或LoRA，以减少训练参数。2) 动态路由网络的设计：可以使用不同的网络结构，例如全连接网络、Transformer网络等，来学习上下文与人格特质之间的映射关系。3) 损失函数的设计：除了传统的语言模型损失函数外，还可以引入额外的损失函数来鼓励模型学习到更具区分性的人格表达，例如对比学习损失或对抗学习损失。4) 训练策略：可以采用多阶段训练策略，例如先预训练LLM backbone，然后训练人格适配器和动态路由网络，最后进行端到端的微调。

## 📊 实验亮点

实验结果表明，PersonaFuse在社会情感智能的多个维度上显著优于基线模型，包括情感感知、社交能力和沟通技巧。与直接提示工程和监督微调方法相比，PersonaFuse在提升社会情感智能的同时，保持了模型的通用推理能力和安全性。人工评估表明，PersonaFuse生成的响应质量与GPT-4o和DeepSeek等领先LLM具有竞争力，但模型尺寸更小。

## 🎯 应用场景

PersonaFuse具有广泛的应用前景，尤其是在需要情感支持和个性化交互的领域。例如，它可以应用于心理健康咨询，为用户提供更具同理心和个性化的支持；在客户服务领域，可以根据客户的性格和需求，提供更贴心的服务；在社交陪伴机器人中，可以赋予机器人更丰富的人格，提升用户的交互体验。未来，PersonaFuse有望成为构建更人性化、更智能的AI系统的关键技术。

## 📄 摘要（原文）

> Recent advancements in Large Language Models (LLMs) demonstrate remarkable capabilities across various fields. These developments have led to more direct communication between humans and LLMs in various situations, such as social companionship and psychological support. However, LLMs often exhibit limitations in emotional perception and social competence during real-world conversations. These limitations partly originate from their inability to adapt their communication style and emotional expression to different social and task contexts. In this work, we introduce PersonaFuse, a novel LLM post-training framework that enables LLMs to adapt and express different personalities for varying situations. Inspired by Trait Activation Theory and the Big Five personality model, PersonaFuse employs a Mixture-of-Expert architecture that combines persona adapters with a dynamic routing network, enabling contextual trait expression. Experimental results show that PersonaFuse substantially outperforms baseline models across multiple dimensions of social-emotional intelligence. Importantly, these gains are achieved without sacrificing general reasoning ability or model safety, which remain common limitations of direct prompting and supervised fine-tuning approaches. PersonaFuse also delivers consistent improvements in downstream human-centered applications, such as mental health counseling and review-based customer service. Finally, human preference evaluations against leading LLMs, including GPT-4o and DeepSeek, demonstrate that PersonaFuse achieves competitive response quality despite its comparatively smaller model size. These findings demonstrate that PersonaFuse offers a theoretically grounded and practical approach for developing social-emotional enhanced LLMs, marking a significant advancement toward more human-centric AI systems.

