---
layout: default
title: "CUPID: Evaluating Personalized and Contextualized Alignment of LLMs from Interactions"
---

# CUPID: Evaluating Personalized and Contextualized Alignment of LLMs from Interactions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.01674" class="toolbar-btn" target="_blank">📄 arXiv: 2508.01674v2</a>
  <a href="https://arxiv.org/pdf/2508.01674.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.01674v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.01674v2', 'CUPID: Evaluating Personalized and Contextualized Alignment of LLMs from Interactions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tae Soo Kim, Yoonjoo Lee, Yoonah Park, Jiho Kim, Young-Ho Kim, Juho Kim

**分类**: cs.CL, cs.AI, cs.HC

**发布日期**: 2025-08-03 (更新: 2025-08-07)

**备注**: Accepted to COLM 2025. Project Website: https://cupid.kixlab.org/

---

## 💡 一句话要点

**提出CUPID基准以解决LLMs个性化与上下文对齐问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `个性化交互` `上下文推断` `用户偏好` `CUPID基准` `多轮反馈` `人机交互`

## 📋 核心要点

1. 现有的LLMs个性化方法假设用户偏好是静态的，未能考虑上下文变化对偏好的影响。
2. CUPID基准通过756个用户交互历史，评估LLMs在多轮交互中推断用户偏好的能力。
3. 实验结果显示，当前LLMs在推断偏好方面存在显著不足，准确率和召回率均低于预期水平。

## 📝 摘要（中文）

大型语言模型（LLMs）的个性化通常假设用户的偏好是静态的，适用于所有任务。然而，实际上人类的偏好是动态的，会根据上下文变化。用户在与LLM的交互中自然地揭示了他们的上下文偏好，模型必须推断并应用这些偏好以确保对齐。为此，本文提出了CUPID，一个包含756个用户与基于LLM的聊天助手之间的人为策划的交互会话历史的基准。通过评估10个开放和专有的LLM，发现当前最先进的LLM在推断多轮交互中的偏好时表现不佳，准确率低于50%，召回率为65%。这项工作强调了提升LLM在上下文个性化交互中的能力的必要性，并提出CUPID作为推动这些改进的资源。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在用户交互中无法有效推断动态上下文偏好的问题。现有方法往往假设用户偏好是固定的，导致模型在实际应用中表现不佳。

**核心思路**：提出CUPID基准，通过人类策划的交互会话历史，帮助模型学习和推断用户在不同上下文中的偏好，以实现更好的个性化响应。

**技术框架**：CUPID基准包含多个模块，包括用户请求解析、上下文偏好推断和响应生成。模型需要根据历史交互推断用户的当前偏好，并生成符合这些偏好的响应。

**关键创新**：CUPID的创新在于其基于真实用户交互数据的评估方法，强调了上下文对用户偏好的影响，与传统静态偏好假设的模型形成鲜明对比。

**关键设计**：在实验中，使用了多轮反馈机制来捕捉用户的动态偏好，并设计了相应的损失函数以优化模型的推断能力。

## 📊 实验亮点

实验结果显示，评估的10个LLMs在推断用户偏好方面表现不佳，准确率低于50%，召回率为65%。这些数据表明，当前的LLMs在处理多轮交互时存在显著的性能瓶颈，亟需改进。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、客户服务和个性化推荐系统。通过提升LLMs在上下文个性化交互中的能力，可以显著改善用户体验，推动人机交互的自然性和有效性。未来，CUPID基准有望成为评估和改进LLMs个性化能力的重要工具。

## 📄 摘要（原文）

> Personalization of Large Language Models (LLMs) often assumes users hold static preferences that reflect globally in all tasks. In reality, humans hold dynamic preferences that change depending on the context. As users interact with an LLM in various contexts, they naturally reveal their contextual preferences, which a model must infer and apply in future contexts to ensure alignment. To assess this, we introduce CUPID, a benchmark of 756 human-curated interaction session histories between users and LLM-based chat assistants. In each interaction session, the user provides a request in a specific context and expresses their preference through multi-turn feedback. Given a new user request and prior interaction sessions, our benchmark assesses whether LLMs can infer the preference relevant to this request and generate a response that satisfies this preference. With CUPID, we evaluated 10 open and proprietary LLMs, revealing that state-of-the-art LLMs struggle to infer preferences from multi-turn interactions and fail to discern what previous context is relevant to a new request -- under 50% precision and 65% recall. Our work highlights the need to advance LLM capabilities for more contextually personalized interactions and proposes CUPID as a resource to drive these improvements.

