---
layout: default
title: Reinforcement Learning from User Feedback
---

# Reinforcement Learning from User Feedback

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14946" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14946v1</a>
  <a href="https://arxiv.org/pdf/2505.14946.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14946v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14946v1', 'Reinforcement Learning from User Feedback')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eric Han, Jun Chen, Karthik Abinav Sankararaman, Xiaoliang Peng, Tengyu Xu, Eryk Helenowski, Kaiyan Peng, Mrinal Kumar, Sinong Wang, Han Fang, Arya Talebzadeh

**分类**: cs.AI

**发布日期**: 2025-05-20

---

## 💡 一句话要点

**提出用户反馈强化学习框架以解决用户偏好对齐问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `用户反馈` `强化学习` `大型语言模型` `多目标优化` `用户偏好对齐`

## 📋 核心要点

1. 现有的强化学习方法依赖专家评估者，其判断可能无法准确反映普通用户的真实偏好。
2. 提出用户反馈强化学习（RLUF）框架，直接利用用户的隐性反馈信号进行模型对齐。
3. 实验结果显示，使用P[Love]模型进行策略优化，正面反馈率显著提高，A/B测试中“爱”反应增加了28%。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在多种用户应用中的广泛部署，使其与真实用户偏好对齐变得至关重要。现有方法如基于人类反馈的强化学习（RLHF）依赖于经过培训的专家评估者，其判断可能无法反映普通用户的优先级。我们提出了用户反馈强化学习（RLUF）框架，旨在直接对齐生产环境中用户的隐性信号。RLUF解决了用户反馈的关键挑战：用户反馈通常是二元的（例如，表情符号反应）、稀疏且偶尔具有对抗性。我们训练了一个奖励模型P[Love]，预测LLM响应获得“爱”反应的可能性，并将其整合到多目标策略优化框架中。大规模实验表明，P[Love]能够有效预测用户的正面反馈，并作为未来用户行为的可靠离线评估器。使用P[Love]的策略优化显著提高了正面反馈率，包括在实时A/B测试中“爱”反应增加了28%。然而，优化正面反应引入了奖励黑客挑战，需要仔细平衡目标。通过直接利用用户的隐性信号，RLUF为大规模对齐LLMs与真实用户偏好提供了一条路径。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型与用户偏好对齐的问题。现有方法如RLHF依赖专家评估，可能导致用户偏好未被准确捕捉。

**核心思路**：论文提出用户反馈强化学习（RLUF）框架，直接从用户的隐性反馈中提取信息，以更好地对齐模型与用户的真实需求。

**技术框架**：RLUF框架包括一个奖励模型P[Love]，用于预测用户对LLM响应的“爱”反应，并将其与有用性和安全性目标结合在多目标策略优化中。

**关键创新**：RLUF的核心创新在于直接利用用户的隐性反馈信号，而不是依赖专家评估，从而更真实地反映用户的偏好。

**关键设计**：在模型设计中，P[Love]的训练采用了用户的二元反馈数据，优化过程中需要平衡正面反应与潜在的奖励黑客问题。

## 📊 实验亮点

实验结果显示，使用P[Love]进行策略优化后，正面反馈率显著提高，尤其是在实时A/B测试中，“爱”反应增加了28%。这一结果表明，RLUF框架在提升用户满意度方面具有显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括智能助手、在线客服和内容推荐系统等，能够帮助这些系统更好地理解和响应用户的真实需求，从而提升用户体验和满意度。未来，RLUF框架可能会在更广泛的用户交互场景中得到应用，推动人机交互的智能化进程。

## 📄 摘要（原文）

> As large language models (LLMs) are increasingly deployed in diverse user facing applications, aligning them with real user preferences becomes essential. Existing methods like Reinforcement Learning from Human Feedback (RLHF) rely on expert annotators trained on manually defined guidelines, whose judgments may not reflect the priorities of everyday users. We introduce Reinforcement Learning from User Feedback (RLUF), a framework for aligning LLMs directly to implicit signals from users in production. RLUF addresses key challenges of user feedback: user feedback is often binary (e.g., emoji reactions), sparse, and occasionally adversarial. We train a reward model, P[Love], to predict the likelihood that an LLM response will receive a Love Reaction, a lightweight form of positive user feedback, and integrate P[Love] into a multi-objective policy optimization framework alongside helpfulness and safety objectives. In large-scale experiments, we show that P[Love] is predictive of increased positive feedback and serves as a reliable offline evaluator of future user behavior. Policy optimization using P[Love] significantly raises observed positive-feedback rates, including a 28% increase in Love Reactions during live A/B tests. However, optimizing for positive reactions introduces reward hacking challenges, requiring careful balancing of objectives. By directly leveraging implicit signals from users, RLUF offers a path to aligning LLMs with real-world user preferences at scale.

