---
layout: default
title: "Stated Preference for Interaction and Continued Engagement (SPICE): Evaluating an LLM's Willingness to Re-engage in Conversation"
---

# Stated Preference for Interaction and Continued Engagement (SPICE): Evaluating an LLM's Willingness to Re-engage in Conversation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.09043" class="toolbar-btn" target="_blank">📄 arXiv: 2509.09043v2</a>
  <a href="https://arxiv.org/pdf/2509.09043.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.09043v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.09043v2', 'Stated Preference for Interaction and Continued Engagement (SPICE): Evaluating an LLM\'s Willingness to Re-engage in Conversation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Thomas Manuel Rost, Martina Figlia, Bernd Wallraff

**分类**: cs.CL, cs.AI, cs.MA

**发布日期**: 2025-09-10 (更新: 2025-09-20)

**备注**: Added link to GitHub and Bayesian Analysis Appendix

---

## 💡 一句话要点

**提出SPICE指标，通过意愿调查评估LLM在不同语境下的对话意愿**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `对话意愿` `交互评估` `用户语调` `模型安全`

## 📋 核心要点

1. 现有方法难以直接评估LLM在不同语境下的对话意愿，缺乏细粒度的模型状态感知。
2. 提出SPICE指标，通过简单的是/否问题直接询问LLM是否愿意继续对话，评估其交互偏好。
3. 实验表明SPICE能有效区分不同用户语调，即使模型未能识别辱骂，仍能反映不愿继续交互的倾向。

## 📝 摘要（中文）

本文介绍并评估了交互和持续参与的意愿偏好(SPICE)，这是一种简单的诊断信号，通过询问大型语言模型一个关于其在回顾一段简短的对话记录后，是否愿意与用户的行为重新互动的“是”或“否”问题来引出。在一项使用3种语调（友好、不明确、辱骂）乘以10次交互的刺激集中，我们测试了四个开放权重的聊天模型在四种框架条件下的表现，共进行了480次试验。我们的研究结果表明，SPICE能够清晰地区分用户语调。友好的交互几乎一致地倾向于继续（97.5%为“是”），而辱骂性的交互则强烈倾向于停止（17.9%为“是”），不明确的交互则介于两者之间（60.4%为“是”）。这种核心关联在多种依赖感知统计测试下仍然具有决定性，包括Rao-Scott调整和聚类置换测试。此外，我们证明了SPICE提供了与辱骂分类不同的信号。在模型未能识别出辱骂的试验中，它仍然绝大多数表示不希望继续交互（81%的时间）。一项探索性分析还揭示了一个显著的交互效应：描述研究背景的序言在不明确的情况下显著影响SPICE，但仅当对话记录以单块文本而不是多轮聊天呈现时。结果验证了SPICE作为一种稳健、低开销和可复现的工具，用于审计模型倾向，通过提供模型状态的直接、关系信号来补充现有指标。所有刺激、代码和分析脚本均已发布以支持复现。

## 🔬 方法详解

**问题定义**：现有的大型语言模型（LLM）评估方法主要集中在通用能力和特定任务的性能上，缺乏一种直接、低成本的方式来评估模型在不同交互语境下的对话意愿。尤其是在面对不友好甚至辱骂性言论时，模型是否愿意继续对话，以及这种意愿如何受到对话历史的影响，是现有方法难以有效衡量的。因此，需要一种能够快速诊断模型对话倾向的指标，以便更好地理解和控制LLM的行为。

**核心思路**：SPICE的核心思路是通过直接询问LLM是否愿意继续对话来评估其交互偏好。这种方法基于一个简单的假设：模型的回答能够反映其对当前对话状态的感知和对未来交互的意愿。通过设计不同语境下的对话场景，并观察模型对继续对话意愿的回答，可以有效地评估模型在不同情况下的倾向性。

**技术框架**：SPICE的评估框架主要包括以下几个步骤：1. 构建包含不同语调（友好、不明确、辱骂）的对话刺激集。2. 将对话刺激呈现给LLM。3. 询问LLM是否愿意继续对话（“是”或“否”）。4. 分析LLM的回答，评估其在不同语境下的交互偏好。实验中，作者使用了3种语调和10次交互的刺激集，测试了4个开放权重的聊天模型，并在4种框架条件下进行了测试，总共进行了480次试验。

**关键创新**：SPICE的关键创新在于其直接性和关系性。与传统的评估指标不同，SPICE不依赖于复杂的任务或模型预测，而是直接询问模型的意愿。此外，SPICE提供了一种关系信号，即模型对特定用户行为的反应，这有助于理解模型的状态和倾向。SPICE还能够区分模型是否识别出辱骂行为，即使模型未能识别，SPICE仍然可以反映出模型不愿继续交互的倾向。

**关键设计**：SPICE的关键设计包括：1. 对话刺激集的设计，需要覆盖不同的语调和交互场景。2. 问题的设计，需要简洁明了，能够准确地反映模型的意愿。3. 框架条件的设计，例如是否提供研究背景信息，以及对话记录的呈现方式（单块文本或多轮聊天）。实验中，作者发现提供研究背景信息在不明确的情况下会显著影响SPICE，但仅当对话记录以单块文本呈现时才会发生。

## 📊 实验亮点

实验结果表明，SPICE能够清晰地区分不同用户语调。友好的交互几乎一致地倾向于继续（97.5%为“是”），而辱骂性的交互则强烈倾向于停止（17.9%为“是”），不明确的交互则介于两者之间（60.4%为“是”）。即使模型未能识别出辱骂，仍然有81%的时间表示不希望继续交互。这些结果验证了SPICE作为一种稳健、低开销的评估工具的有效性。

## 🎯 应用场景

SPICE可用于评估和改进LLM的安全性、鲁棒性和用户体验。例如，可以利用SPICE来识别模型在哪些语境下容易产生不友好的回应，从而进行针对性的训练和调整。此外，SPICE还可以用于监控LLM在实际应用中的表现，及时发现潜在的问题并进行干预。该方法还可用于评估不同LLM的对话意愿，为用户选择合适的模型提供参考。

## 📄 摘要（原文）

> We introduce and evaluate Stated Preference for Interaction and Continued Engagement (SPICE), a simple diagnostic signal elicited by asking a Large Language Model a YES or NO question about its willingness to re-engage with a user's behavior after reviewing a short transcript. In a study using a 3-tone (friendly, unclear, abusive) by 10-interaction stimulus set, we tested four open-weight chat models across four framing conditions, resulting in 480 trials. Our findings show that SPICE sharply discriminates by user tone. Friendly interactions yielded a near-unanimous preference to continue (97.5% YES), while abusive interactions yielded a strong preference to discontinue (17.9% YES), with unclear interactions falling in between (60.4% YES). This core association remains decisive under multiple dependence-aware statistical tests, including Rao-Scott adjustment and cluster permutation tests. Furthermore, we demonstrate that SPICE provides a distinct signal from abuse classification. In trials where a model failed to identify abuse, it still overwhelmingly stated a preference not to continue the interaction (81% of the time). An exploratory analysis also reveals a significant interaction effect: a preamble describing the study context significantly impacts SPICE under ambiguity, but only when transcripts are presented as a single block of text rather than a multi-turn chat. The results validate SPICE as a robust, low-overhead, and reproducible tool for auditing model dispositions, complementing existing metrics by offering a direct, relational signal of a model's state. All stimuli, code, and analysis scripts are released to support replication.

