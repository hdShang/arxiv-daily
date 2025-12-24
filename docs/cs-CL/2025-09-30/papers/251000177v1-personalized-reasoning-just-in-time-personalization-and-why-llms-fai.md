---
layout: default
title: "Personalized Reasoning: Just-In-Time Personalization and Why LLMs Fail At It"
---

# Personalized Reasoning: Just-In-Time Personalization and Why LLMs Fail At It

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.00177" class="toolbar-btn" target="_blank">📄 arXiv: 2510.00177v1</a>
  <a href="https://arxiv.org/pdf/2510.00177.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.00177v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.00177v1', 'Personalized Reasoning: Just-In-Time Personalization and Why LLMs Fail At It')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuyue Stella Li, Avinandan Bose, Faeze Brahman, Simon Shaolei Du, Pang Wei Koh, Maryam Fazel, Yulia Tsvetkov

**分类**: cs.CL, cs.AI

**发布日期**: 2025-09-30

**备注**: 57 pages, 6 figures

---

## 💡 一句话要点

**提出PREFDISCO评估框架，揭示LLM在即时个性化推理上的局限性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `个性化推理` `大语言模型` `用户偏好` `交互式评估` `PREFDISCO`

## 📋 核心要点

1. 现有LLM在面向用户的应用中，难以在没有用户历史的情况下进行即时个性化推理，导致响应与用户需求不匹配。
2. 论文提出PREFDISCO评估框架，通过模拟具有稀疏偏好的人物角色，将静态基准转换为交互式个性化任务。
3. 实验表明，简单个性化尝试效果可能比通用响应更差，揭示了LLM在个性化推理方面的局限性，需专门开发。

## 📝 摘要（中文）

当前的大语言模型（LLM）开发将任务解决和偏好对齐视为分离的挑战，首先优化客观正确性，然后对齐聚合的人类偏好。这种模式在面向用户的应用中失效，因为如果响应与用户的需求不匹配，即使正确解决问题也是不够的。在由于冷启动条件或隐私限制而没有先前用户交互历史的即时场景中，这一挑战更加剧烈。LLM需要识别它们对用户偏好的未知信息，通过提问策略性地引出偏好值，然后相应地调整它们的推理过程和响应——这是一个复杂的认知过程链，我们称之为个性化推理。我们引入了PREFDISCO，一种评估方法，它使用基于心理学的人物角色和稀疏偏好将静态基准转换为交互式个性化任务。我们的框架创建了这样的场景：相同的问题需要不同的推理链，这取决于用户上下文，因为最佳解释方法因个人专业知识和偏好而异，同时保持事实准确性。对10个任务中21个前沿模型的评估表明，29.0%的朴素个性化尝试产生的偏好对齐比通用响应更差，但通用响应也未能有效地服务于个人用户需求。这些发现表明，个性化推理需要专门的开发，而不是自然而然地出现。PREFDISCO将个性化推理确立为一个可衡量的研究前沿，并揭示了当前LLM交互能力的基本局限性，为开发能够在教育、医疗保健和技术领域适应个人用户的系统奠定了基础，在这些领域中，个性化至关重要。

## 🔬 方法详解

**问题定义**：论文旨在解决大语言模型（LLM）在即时个性化推理方面的不足。现有LLM通常先优化客观正确性，再对齐聚合的人类偏好，但在实际应用中，尤其是用户偏好未知的情况下，这种方式无法满足用户的个性化需求。现有方法缺乏有效评估LLM个性化推理能力的框架，也缺乏对LLM如何主动获取并利用用户偏好的研究。

**核心思路**：论文的核心思路是构建一个交互式的评估环境，使LLM能够通过提问来了解用户的偏好，并根据这些偏好调整其推理过程和响应。这种“Just-In-Time”的个性化推理要求LLM具备识别未知偏好、策略性提问、动态调整推理过程的能力。

**技术框架**：PREFDISCO框架包含以下主要组成部分：1) 基于心理学的人物角色（Personas），这些角色具有稀疏的偏好；2) 将静态基准任务转换为交互式个性化任务；3) 评估指标，用于衡量LLM在偏好对齐方面的表现。LLM需要首先识别用户偏好的未知部分，然后通过提问来获取这些偏好信息，最后根据获取的偏好信息调整其推理过程和响应。

**关键创新**：PREFDISCO的关键创新在于其交互式评估方式和基于心理学的人物角色。传统的评估方法通常是静态的，无法模拟真实世界中用户偏好的动态变化。PREFDISCO通过引入人物角色和交互式任务，使LLM能够主动学习用户的偏好，并根据这些偏好进行个性化推理。

**关键设计**：PREFDISCO的关键设计包括：1) 人物角色的偏好是稀疏的，这意味着LLM需要主动提问才能获取完整的偏好信息；2) 任务的设计需要保证相同的问题在不同的用户上下文中需要不同的推理链；3) 评估指标需要能够衡量LLM在偏好对齐方面的表现，同时考虑事实准确性。

## 📊 实验亮点

实验结果表明，29.0%的朴素个性化尝试产生的偏好对齐效果比通用响应更差，这表明简单的个性化方法可能适得其反。同时，通用响应也未能有效地服务于个人用户需求。这些结果强调了专门开发个性化推理能力的必要性，并揭示了当前LLM在交互式个性化方面的局限性。

## 🎯 应用场景

该研究成果可应用于教育、医疗保健和技术支持等领域，提升人机交互的个性化程度。例如，在教育领域，LLM可以根据学生的学习风格和知识背景提供个性化的辅导；在医疗保健领域，LLM可以根据患者的病情和偏好提供个性化的治疗建议；在技术支持领域，LLM可以根据用户的技术水平和需求提供个性化的解决方案。该研究为开发能够适应个人用户的智能系统奠定了基础。

## 📄 摘要（原文）

> Current large language model (LLM) development treats task-solving and preference alignment as separate challenges, optimizing first for objective correctness, then for alignment to aggregated human preferences. This paradigm fails in human-facing applications where solving a problem correctly is insufficient if the response mismatches the user's needs. This challenge intensifies in just-in-time scenarios where no prior user interaction history exists due to cold-start conditions or privacy constraints. LLMs need to identify what they don't know about user preferences, strategically elicit preference values through questioning, then adapt their reasoning processes and responses accordingly -- a complicated chain of cognitive processes which we term personalized reasoning. We introduce PREFDISCO, an evaluation methodology that transforms static benchmarks into interactive personalization tasks using psychologically-grounded personas with sparse preferences. Our framework creates scenarios where identical questions require different reasoning chains depending on user context, as optimal explanation approaches vary by individual expertise and preferences while maintaining factual accuracy. Evaluation of 21 frontier models across 10 tasks reveals 29.0% of naive personalization attempts produce worse preference alignment than generic responses, yet generic responses also fail to serve individual user needs effectively. These findings suggest personalized reasoning requires dedicated development rather than emerging naturally. PREFDISCO establishes personalized reasoning as a measurable research frontier and reveals fundamental limitations in current LLMs' interactive capabilities, providing a foundation for developing systems that can adapt to individual users in education, healthcare, and technical domains where personalization is critical.

