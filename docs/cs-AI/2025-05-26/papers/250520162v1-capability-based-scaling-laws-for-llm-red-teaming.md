---
layout: default
title: Capability-Based Scaling Laws for LLM Red-Teaming
---

# Capability-Based Scaling Laws for LLM Red-Teaming

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20162" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20162v1</a>
  <a href="https://arxiv.org/pdf/2505.20162.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20162v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20162v1', 'Capability-Based Scaling Laws for LLM Red-Teaming')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alexander Panfilov, Paul Kassianik, Maksym Andriushchenko, Jonas Geiping

**分类**: cs.AI, cs.CL, cs.CR, cs.LG

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出能力差距框架以优化大型语言模型的红队测试**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `红队测试` `能力差距` `大型语言模型` `越狱攻击` `安全性评估` `模型能力` `攻击策略`

## 📋 核心要点

1. 现有红队测试方法在面对能力差距时效果不佳，尤其是当目标模型能力超越攻击者时。
2. 论文提出通过能力差距框架分析红队测试，评估攻击者与目标模型的能力差异，以优化攻击策略。
3. 实验表明，攻击者能力越强，攻击成功率越高，且成功率与社科领域的MMLU-Pro基准表现高度相关。

## 📝 摘要（中文）

随着大型语言模型能力和自主性的发展，通过红队测试识别其脆弱性变得至关重要。然而，传统的提示工程方法在面对能力差距时可能失效。本文通过分析攻击者与目标模型之间的能力差距，评估了500多个攻击者-目标对的LLM越狱攻击，发现更强的模型作为攻击者更有效，且当目标模型能力超过攻击者时，攻击成功率显著下降。基于这些发现，提出了一种越狱规模法则，预测固定目标的攻击成功率。这些结果表明，固定能力的攻击者（如人类）可能在未来模型面前变得无效，且开放源代码模型的能力提升加大了现有系统的风险。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型红队测试中，攻击者与目标模型能力差距导致的测试效果不佳问题。现有方法在面对能力强大的目标时，无法有效识别其脆弱性。

**核心思路**：通过分析攻击者与目标模型之间的能力差距，提出一种新的红队测试框架，以评估不同能力模型的攻击效果。这种设计旨在更准确地反映现实场景中的能力对抗。

**技术框架**：整体框架包括三个主要模块：能力评估模块、攻击策略生成模块和攻击效果评估模块。首先评估攻击者和目标的能力，然后生成相应的攻击策略，最后评估攻击的成功率。

**关键创新**：提出的越狱规模法则是本文的核心创新，能够根据攻击者与目标模型的能力差距预测攻击成功率。这一方法与传统的提示工程方法有本质区别，强调能力差距的重要性。

**关键设计**：在实验中，使用了多种攻击策略，并根据不同模型的能力设置了相应的参数。损失函数设计考虑了攻击成功率与模型能力的关系，确保了实验结果的有效性。

## 📊 实验亮点

实验结果显示，攻击者能力越强，攻击成功率显著提高，尤其当目标模型能力超过攻击者时，成功率急剧下降。通过对500多个攻击者-目标对的评估，发现攻击成功率与MMLU-Pro基准的社科领域表现高度相关，提供了新的红队测试视角。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性评估、模型开发过程中的脆弱性识别以及针对未来模型的红队测试策略优化。通过准确测量和控制模型的说服和操控能力，可以有效降低其作为攻击者的风险，确保安全部署。

## 📄 摘要（原文）

> As large language models grow in capability and agency, identifying vulnerabilities through red-teaming becomes vital for safe deployment. However, traditional prompt-engineering approaches may prove ineffective once red-teaming turns into a weak-to-strong problem, where target models surpass red-teamers in capabilities. To study this shift, we frame red-teaming through the lens of the capability gap between attacker and target. We evaluate more than 500 attacker-target pairs using LLM-based jailbreak attacks that mimic human red-teamers across diverse families, sizes, and capability levels. Three strong trends emerge: (i) more capable models are better attackers, (ii) attack success drops sharply once the target's capability exceeds the attacker's, and (iii) attack success rates correlate with high performance on social science splits of the MMLU-Pro benchmark. From these trends, we derive a jailbreaking scaling law that predicts attack success for a fixed target based on attacker-target capability gap. These findings suggest that fixed-capability attackers (e.g., humans) may become ineffective against future models, increasingly capable open-source models amplify risks for existing systems, and model providers must accurately measure and control models' persuasive and manipulative abilities to limit their effectiveness as attackers.

