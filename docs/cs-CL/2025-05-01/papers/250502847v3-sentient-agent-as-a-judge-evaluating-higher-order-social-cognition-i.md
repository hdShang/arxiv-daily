---
layout: default
title: "Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models"
---

# Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.02847" class="toolbar-btn" target="_blank">📄 arXiv: 2505.02847v3</a>
  <a href="https://arxiv.org/pdf/2505.02847.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.02847v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.02847v3', 'Sentient Agent as a Judge: Evaluating Higher-Order Social Cognition in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bang Zhang, Ruotian Ma, Qingxuan Jiang, Peisong Wang, Jiaqi Chen, Zheng Xie, Xingyu Chen, Yue Wang, Fanghua Ye, Jian Li, Yifan Yang, Zhaopeng Tu, Xiaolong Li

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-05-01 (更新: 2025-05-21)

**备注**: code: https://github.com/Tencent/digitalhuman/tree/main/SAGE

---

## 💡 一句话要点

**提出SAGE框架以评估大型语言模型的高阶社会认知能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `社会认知` `情感计算` `多轮对话` `心理学评估` `同理心` `自动化评估`

## 📋 核心要点

1. 现有方法在评估大型语言模型对人类情感理解的能力时存在不足，无法真实反映其社会认知能力。
2. 本文提出的SAGE框架通过模拟人类情感和内心思维，提供了一种新的评估方式，增强了对话的真实性和深度。
3. 实验结果表明，SAGE的情感评分与传统心理学指标高度相关，且在多个模型间揭示了显著的性能差距。

## 📝 摘要（中文）

评估大型语言模型（LLM）对人类情感的理解能力仍然是一个开放性挑战。为了解决这一问题，本文提出了Sentient Agent as a Judge（SAGE）框架，该框架通过模拟人类情感变化和内心思维来评估LLM的高阶社会认知能力。SAGE在多轮对话中进行评估，分析情感变化、感受及回复策略，生成数值化的情感轨迹和可解释的内心思维。实验结果显示，SAGE的情感评分与心理学指标（如BLRI评分）高度相关，验证了其心理学的真实性。此外，SAGE还建立了一个公共的Sentient Leaderboard，揭示了前沿模型与早期基线之间的显著差距，提供了一个可扩展且可解释的工具，以追踪语言代理的同理心和社会适应能力的进展。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在理解人类情感方面的评估问题，现有方法往往只关注文本内容，缺乏对情感和社会认知的深入分析。

**核心思路**：SAGE框架通过构建一个模拟人类情感变化和内心思维的代理，提供了一个更为真实的评估环境，能够在多轮对话中动态分析情感和反应。

**技术框架**：SAGE的整体架构包括情感变化模拟模块、内心思维分析模块和回复生成模块。每个模块在对话的每一轮中协同工作，生成情感轨迹和内心思维的数值化表示。

**关键创新**：SAGE的主要创新在于其情感轨迹的生成和内心思维的可解释性，这与传统的评估方法不同，后者通常缺乏对情感变化的动态捕捉。

**关键设计**：在设计上，SAGE使用了特定的情感评分标准和心理学指标（如BLRI），并通过多轮对话的反馈机制优化情感和回复策略的生成。

## 📊 实验亮点

实验结果显示，SAGE的情感评分与BLRI评分和同理心指标高度相关，验证了其心理学的真实性。此外，Sentient Leaderboard揭示了前沿模型（如GPT-4o-Latest和Gemini2.5-Pro）与早期基线之间的性能差距，最高可达4倍，显示了SAGE在评估模型能力方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括情感计算、智能客服、社交机器人等，能够帮助开发更具同理心和社会适应能力的语言模型。未来，SAGE框架可能推动人机交互的进一步发展，使得机器在理解和回应人类情感方面更加自然和有效。

## 📄 摘要（原文）

> Assessing how well a large language model (LLM) understands human, rather than merely text, remains an open challenge. To bridge the gap, we introduce Sentient Agent as a Judge (SAGE), an automated evaluation framework that measures an LLM's higher-order social cognition. SAGE instantiates a Sentient Agent that simulates human-like emotional changes and inner thoughts during interaction, providing a more realistic evaluation of the tested model in multi-turn conversations. At every turn, the agent reasons about (i) how its emotion changes, (ii) how it feels, and (iii) how it should reply, yielding a numerical emotion trajectory and interpretable inner thoughts. Experiments on 100 supportive-dialogue scenarios show that the final Sentient emotion score correlates strongly with Barrett-Lennard Relationship Inventory (BLRI) ratings and utterance-level empathy metrics, validating psychological fidelity. We also build a public Sentient Leaderboard covering 18 commercial and open-source models that uncovers substantial gaps (up to 4x) between frontier systems (GPT-4o-Latest, Gemini2.5-Pro) and earlier baselines, gaps not reflected in conventional leaderboards (e.g., Arena). SAGE thus provides a principled, scalable and interpretable tool for tracking progress toward genuinely empathetic and socially adept language agents.

