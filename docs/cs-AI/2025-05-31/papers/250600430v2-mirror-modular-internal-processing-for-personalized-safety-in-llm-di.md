---
layout: default
title: "MIRROR: Modular Internal Processing for Personalized Safety in LLM Dialogue"
---

# MIRROR: Modular Internal Processing for Personalized Safety in LLM Dialogue

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00430" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00430v2</a>
  <a href="https://arxiv.org/pdf/2506.00430.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00430v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00430v2', 'MIRROR: Modular Internal Processing for Personalized Safety in LLM Dialogue')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nicole Hsing

**分类**: cs.AI

**发布日期**: 2025-05-31 (更新: 2025-10-03)

---

## 💡 一句话要点

**提出MIRROR以解决大型语言模型对用户安全的忽视问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `个性化安全` `模块化架构` `对话系统` `深思熟虑处理`

## 📋 核心要点

1. 现有大型语言模型在多轮对话中常常忽视用户的安全需求，导致生成不安全的建议。
2. 本文提出的MIRROR架构通过模块化设计，分离即时响应生成与深思熟虑处理，保持用户的个人信息。
3. 在CuRaTe基准测试中，MIRROR增强的模型相较于传统模型实现了21%的性能提升，且成本低廉。

## 📝 摘要（中文）

大型语言模型在个人多轮对话中常常忽视用户特定的安全背景，导致生成有害建议。为了解决这一问题，本文提出了MIRROR，一个模块化的生产导向架构，通过持久的、有限的内部状态在对话轮次间保留个人信息。MIRROR的双组件设计灵感来源于双重过程理论，将即时响应生成（Talker）与异步深思熟虑处理（Thinker）分开，能够在对话轮次间合成平行推理线程，且延迟极小。在CuRaTe个性化安全基准上，MIRROR增强的模型在七个不同的前沿模型上实现了21%的相对提升，开源的Llama 4和Mistral 3变体在每轮仅需额外成本0.0028到0.0172美元的情况下超越了GPT-4o和Claude 3.7 Sonnet，缩小了经济实惠的开源模型与前沿系统在安全领域的差距。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在多轮对话中忽视用户特定安全背景的问题。现有方法往往导致模型生成有害建议，缺乏对用户个性化安全的关注。

**核心思路**：MIRROR架构通过模块化设计，分离即时响应生成（Talker）与异步深思熟虑处理（Thinker），从而在对话轮次间保持用户的个人信息，避免模型对用户安全的妥协。

**技术框架**：MIRROR的整体架构包括两个主要模块：Talker负责即时生成响应，而Thinker则进行深思熟虑的处理，合成平行推理线程，确保信息的连贯性与安全性。

**关键创新**：MIRROR的最重要创新在于其模块化设计与双组件架构，能够在保持用户安全的同时，提供高效的对话生成，与现有方法相比，显著提升了模型的安全性与个性化能力。

**关键设计**：在设计上，MIRROR采用了持久的、有限的内部状态来存储用户信息，确保在对话中能够有效利用这些信息，同时在延迟上保持在可接受范围内。

## 📊 实验亮点

在CuRaTe个性化安全基准测试中，MIRROR增强的模型实现了21%的相对提升，从69%提高到84%。开源的Llama 4和Mistral 3变体在成本仅为每轮0.0028到0.0172美元的情况下，超越了GPT-4o和Claude 3.7 Sonnet，展示了其在安全性方面的显著优势。

## 🎯 应用场景

MIRROR架构的潜在应用场景包括个性化助手、心理健康支持系统及其他需要高安全性和个性化的对话系统。其模块化特性使得不同预算的开发者都能实现安全的AI对话，具有广泛的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models frequently generate harmful recommendations in personal multi-turn dialogue by ignoring user-specific safety context, exhibiting sycophantic agreement, and compromising user safety for larger group preferences. We introduce MIRROR, a modular production-focused architecture that prevents these failures through a persistent, bounded internal state that preserves personal conversational information across conversational turns. Our dual-component design inspired by Dual Process Theory separates immediate response generation (Talker) from asynchronous deliberative processing (Thinker), which synthesizes parallel reasoning threads between turns with marginal latency. On the CuRaTe personalized safety benchmark, MIRROR-augmented models achieve a 21% relative improvement (69% to 84%) across seven diverse frontier models, with open-source Llama 4 and Mistral 3 variants surpassing both GPT-4o and Claude 3.7 Sonnet at only \$0.0028 to \$0.0172 additional cost per turn, narrowing the gap between affordable open-source models to frontier systems in the safety space. The modular architecture enables flexible deployment: full internal processing for affordable models or single-component configurations for expensive systems, democratizing access to safer, personalized AI.

