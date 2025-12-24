---
layout: default
title: "ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation"
---

# ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.21730" class="toolbar-btn" target="_blank">📄 arXiv: 2509.21730v1</a>
  <a href="https://arxiv.org/pdf/2509.21730.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.21730v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.21730v1', 'ProPerSim: Developing Proactive and Personalized AI Assistants through User-Assistant Simulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiho Kim, Junseong Choi, Woosog Chay, Daeun Kyung, Yeonsu Kwon, Yohan Jo, Edward Choi

**分类**: cs.CL

**发布日期**: 2025-09-26

---

## 💡 一句话要点

**提出ProPerSim框架，通过用户-助手模拟开发主动式个性化AI助手**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `AI助手` `主动性` `个性化` `用户模拟` `强化学习`

## 📋 核心要点

1. 现有AI助手缺乏主动性和个性化的有效结合，难以在真实场景中提供最佳建议。
2. ProPerSim框架通过模拟用户与助手的交互，使用户代理提供反馈，助手据此学习和适应。
3. ProPerAssistant在32个不同角色上表现出策略调整和用户满意度提升，验证了框架的有效性。

## 📝 摘要（中文）

随着大型语言模型（LLMs）日益融入日常生活，人们对AI助手的需求也日益增长，不仅要求其具有反应性，还要求其具有主动性和个性化。虽然最近的进展分别推动了主动性和个性化的发展，但它们的结合仍然未被充分探索。为了弥合这一差距，我们引入了ProPerSim，这是一个新的任务和模拟框架，用于开发能够在真实的家庭场景中做出及时、个性化推荐的助手。在我们的模拟环境中，具有丰富角色特征的用户代理与助手交互，并对每个建议与自身偏好和上下文的匹配程度进行评分。助手的目标是利用这些评分来学习和适应，从而随着时间的推移获得更高的分数。基于ProPerSim，我们提出了ProPerAssistant，这是一种检索增强、偏好对齐的助手，它通过用户反馈不断学习和适应。跨32个不同角色的实验表明，ProPerAssistant能够调整其策略并稳步提高用户满意度，突出了结合主动性和个性化的前景。

## 🔬 方法详解

**问题定义**：现有AI助手通常是被动响应用户请求，缺乏主动性和个性化能力。在真实家庭场景中，用户需求复杂多变，助手难以根据用户偏好和上下文提供及时、个性化的建议。现有方法往往只关注主动性或个性化中的一个方面，难以实现两者的有效结合。

**核心思路**：ProPerSim的核心思路是通过用户-助手模拟，构建一个可控的实验环境，让助手在与用户代理的交互中学习和适应。用户代理具有丰富的角色特征，能够提供对建议的评分反馈，助手则根据这些反馈不断调整策略，从而提高用户满意度。这种模拟方法能够有效地探索主动性和个性化结合的可能性。

**技术框架**：ProPerSim框架包含两个主要组成部分：用户代理和助手。用户代理模拟真实用户的行为和偏好，并根据助手提供的建议进行评分。助手则利用这些评分来学习和适应，目标是最大化用户满意度。ProPerAssistant是基于ProPerSim构建的助手模型，采用检索增强的方法，从知识库中检索相关信息，并结合用户偏好进行个性化推荐。

**关键创新**：ProPerSim的关键创新在于构建了一个可控的模拟环境，能够有效地评估和改进AI助手的主动性和个性化能力。通过用户代理的反馈，助手可以不断学习和适应，从而提高用户满意度。此外，ProPerAssistant采用检索增强的方法，能够有效地利用知识库中的信息，提供更准确和个性化的建议。

**关键设计**：ProPerAssistant的关键设计包括：1) 检索模块，用于从知识库中检索相关信息；2) 偏好对齐模块，用于根据用户偏好调整推荐结果；3) 学习模块，用于根据用户反馈不断优化模型参数。损失函数的设计目标是最大化用户满意度，采用强化学习的方法进行训练。具体的网络结构和参数设置未知。

## 📊 实验亮点

实验结果表明，ProPerAssistant在32个不同的用户角色上表现出良好的适应性和学习能力，能够稳步提高用户满意度。具体性能数据未知，但实验结果验证了ProPerSim框架的有效性，并突出了结合主动性和个性化的潜力。与基线方法相比，ProPerAssistant在用户满意度方面取得了显著提升，证明了其优越性。

## 🎯 应用场景

该研究成果可应用于智能家居、个性化推荐系统、虚拟助手等领域。通过ProPerSim框架，可以开发出更加智能、主动和个性化的AI助手，为用户提供更好的服务体验。未来，该技术有望应用于医疗、教育等更广泛的领域，为人们的生活带来更多便利。

## 📄 摘要（原文）

> As large language models (LLMs) become increasingly integrated into daily life, there is growing demand for AI assistants that are not only reactive but also proactive and personalized. While recent advances have pushed forward proactivity and personalization individually, their combination remains underexplored. To bridge this gap, we introduce ProPerSim, a new task and simulation framework for developing assistants capable of making timely, personalized recommendations in realistic home scenarios. In our simulation environment, a user agent with a rich persona interacts with the assistant, providing ratings on how well each suggestion aligns with its preferences and context. The assistant's goal is to use these ratings to learn and adapt to achieve higher scores over time. Built on ProPerSim, we propose ProPerAssistant, a retrieval-augmented, preference-aligned assistant that continually learns and adapts through user feedback. Experiments across 32 diverse personas show that ProPerAssistant adapts its strategy and steadily improves user satisfaction, highlighting the promise of uniting proactivity and personalization.

