---
layout: default
title: "Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators"
---

# Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.03647" class="toolbar-btn" target="_blank">📄 arXiv: 2509.03647v1</a>
  <a href="https://arxiv.org/pdf/2509.03647.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.03647v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.03647v1', 'Breaking the Mirror: Activation-Based Mitigation of Self-Preference in LLM Evaluators')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dani Roytburg, Matthew Bozoukov, Matthew Nguyen, Jou Barzdukas, Simon Fu, Narmeen Oozeer

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-03

---

## 💡 一句话要点

**提出基于激活的干预方法，缓解LLM评估器中的自我偏好问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自我偏好偏差` `模型评估` `steering vectors` `对比激活添加`

## 📋 核心要点

1. LLM评估器存在自我偏好偏差，即倾向于选择自身生成的答案，影响评估的公正性。
2. 论文提出使用steering vectors，通过对比激活添加（CAA）和优化方法，在推理时干预LLM的激活。
3. 实验表明，该方法能显著降低不合理的自我偏好偏差，最高可达97%，优于现有基线方法。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地被用作自动评估器，但它们存在“自我偏好偏差”：倾向于偏爱自己的输出而不是其他模型的输出。这种偏差损害了评估流程的公平性和可靠性，尤其是在偏好调整和模型路由等任务中。本文研究了是否可以在推理时使用轻量级的steering vectors来缓解这个问题，而无需重新训练。作者构建了一个精心策划的数据集，将自我偏好偏差区分为合理的自我偏好和不合理的自我偏好，并使用两种方法构建steering vectors：对比激活添加（CAA）和基于优化的方法。结果表明，steering vectors可以将不合理的自我偏好偏差降低高达97％，大大优于prompting和直接偏好优化基线。然而，steering vectors在合理的自我偏好和无偏一致性方面不稳定，这意味着自我偏好跨越多个或非线性方向。这突显了它们作为LLM评估器保障措施的潜力和局限性，并推动了更强大的干预措施。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型作为评估器时存在的“自我偏好偏差”问题。现有方法，如prompting和直接偏好优化，无法有效消除这种偏差，导致评估结果不准确，影响模型选择和优化。

**核心思路**：论文的核心思路是通过在推理阶段干预LLM的激活，来抑制其自我偏好。具体而言，通过构建steering vectors，引导LLM的激活状态，使其减少对自身生成内容的偏好。

**技术框架**：整体框架包括以下几个步骤：1) 构建区分合理和不合理自我偏好的数据集；2) 使用对比激活添加（CAA）和优化方法构建steering vectors；3) 在推理时，将steering vectors添加到LLM的激活中，从而影响其评估结果；4) 评估steering vectors在减少自我偏好偏差方面的效果。

**关键创新**：关键创新在于使用steering vectors在推理时干预LLM的激活，从而缓解自我偏好偏差。与传统的prompting和直接偏好优化方法相比，该方法更加轻量级，无需重新训练模型，且效果更显著。

**关键设计**：论文使用了两种方法构建steering vectors：对比激活添加（CAA）和基于优化的方法。CAA通过对比LLM对自身生成内容和其他模型生成内容的激活差异，来构建steering vectors。基于优化的方法则通过优化目标函数，直接学习steering vectors。数据集的设计也至关重要，需要区分合理和不合理的自我偏好，以确保steering vectors能够有效抑制偏差。

## 📊 实验亮点

实验结果表明，使用steering vectors可以将不合理的自我偏好偏差降低高达97％，显著优于prompting和直接偏好优化基线。然而，steering vectors在合理的自我偏好和无偏一致性方面表现不稳定，表明自我偏好可能涉及多个或非线性方向。这些结果揭示了steering vectors作为LLM评估器保障措施的潜力和局限性。

## 🎯 应用场景

该研究成果可应用于各种需要使用LLM进行自动评估的场景，例如模型选择、偏好调整、模型路由等。通过减少LLM评估器的自我偏好偏差，可以提高评估结果的准确性和公正性，从而更好地指导模型开发和应用。未来，该方法有望推广到其他类型的偏差缓解，提升LLM的可靠性和安全性。

## 📄 摘要（原文）

> Large language models (LLMs) increasingly serve as automated evaluators, yet they suffer from "self-preference bias": a tendency to favor their own outputs over those of other models. This bias undermines fairness and reliability in evaluation pipelines, particularly for tasks like preference tuning and model routing. We investigate whether lightweight steering vectors can mitigate this problem at inference time without retraining. We introduce a curated dataset that distinguishes self-preference bias into justified examples of self-preference and unjustified examples of self-preference, and we construct steering vectors using two methods: Contrastive Activation Addition (CAA) and an optimization-based approach. Our results show that steering vectors can reduce unjustified self-preference bias by up to 97\%, substantially outperforming prompting and direct preference optimization baselines. Yet steering vectors are unstable on legitimate self-preference and unbiased agreement, implying self-preference spans multiple or nonlinear directions. This underscores both their promise and limits as safeguards for LLM-as-judges and motivates more robust interventions.

