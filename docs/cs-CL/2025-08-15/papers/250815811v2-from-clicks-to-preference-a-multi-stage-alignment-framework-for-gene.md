---
layout: default
title: "From Clicks to Preference: A Multi-stage Alignment Framework for Generative Query Suggestion in Conversational System"
---

# From Clicks to Preference: A Multi-stage Alignment Framework for Generative Query Suggestion in Conversational System

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.15811" class="toolbar-btn" target="_blank">📄 arXiv: 2508.15811v2</a>
  <a href="https://arxiv.org/pdf/2508.15811.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.15811v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.15811v2', 'From Clicks to Preference: A Multi-stage Alignment Framework for Generative Query Suggestion in Conversational System')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhao Yin, Haolin Wang, Peng Bao, Ju Xu, Yongliang Wang

**分类**: cs.CL, cs.AI

**发布日期**: 2025-08-15 (更新: 2025-12-15)

**备注**: Accepted by SIGKDD Conference on Knowledge Discovery and Data Mining (KDD 26)

---

## 💡 一句话要点

**提出多阶段对齐框架以解决生成查询建议中的用户偏好问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成查询建议` `用户偏好对齐` `高斯奖励模型` `强化学习` `多阶段框架` `点击率提升` `对话系统`

## 📋 核心要点

1. 现有的生成查询建议方法在对齐用户偏好方面存在显著挑战，导致生成内容与用户意图不匹配。
2. 本文提出的多阶段对齐框架通过逐步对齐生成策略与用户意图，利用高斯奖励模型来更好地捕捉用户偏好的不确定性。
3. 实验结果显示，该框架在自动评估和人工评估中均显著优于基线，并在用户点击率上实现了34%的相对提升。

## 📝 摘要（中文）

生成查询建议利用大型语言模型为对话系统提供了强大的增强能力，但如何将输出与细微的用户偏好对齐仍然是一个关键挑战。为此，本文提出了一种多阶段框架，旨在实现生成策略与用户意图之间的逐步对齐。该流程首先通过提示工程作为冷启动策略，然后在监督微调阶段引入点击日志的蒸馏方法，以创建稳健的基础模型。为了更好地建模用户偏好并捕捉其固有的不确定性，本文开发了一种高斯奖励模型（GaRM），将用户偏好表示为概率分布而非点估计。最后，采用强化学习将生成策略与这些偏好对齐，使用复合奖励函数将GaRM与辅助启发式结合，以减轻奖励黑客行为。大量实验表明，该框架在自动和人工评估中显著优于基线，并在实时A/B测试中实现了34%的用户参与度相对提升。

## 🔬 方法详解

**问题定义**：本文旨在解决生成查询建议中用户偏好对齐不足的问题。现有方法往往无法有效捕捉用户的细微意图和偏好，导致生成内容的相关性和用户满意度降低。

**核心思路**：论文提出的多阶段对齐框架通过逐步优化生成策略与用户意图的对齐，利用高斯奖励模型（GaRM）将用户偏好建模为概率分布，从而更好地反映用户的真实需求。

**技术框架**：整体架构包括三个主要阶段：首先是提示工程作为冷启动策略，其次是监督微调阶段，通过点击日志的蒸馏方法构建基础模型，最后是通过强化学习对生成策略进行优化。

**关键创新**：最重要的创新在于引入高斯奖励模型（GaRM），它将用户偏好表示为概率分布，克服了传统方法的局限性。此外，结合复合奖励函数和辅助启发式设计，有效减轻了奖励黑客行为。

**关键设计**：在模型训练中，采用了新的分布外正则化方法和两阶段奖励融合技术，以保持训练的稳定性和提高模型的泛化能力。

## 📊 实验亮点

实验结果显示，提出的框架在自动评估和人工评估中均显著优于基线，用户点击率在实时A/B测试中实现了34%的相对提升，证明了该方法在提升用户参与度方面的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、在线搜索引擎和个性化推荐系统等。通过更好地理解和对齐用户偏好，能够显著提升用户体验和满意度，进而推动商业价值的增长。未来，该框架可扩展至更多对话系统和交互场景，具有广泛的应用前景。

## 📄 摘要（原文）

> Generative query suggestion using large language models offers a powerful way to enhance conversational systems, but aligning outputs with nuanced user preferences remains a critical challenge. To address this, we introduce a multi-stage framework designed for progressive alignment between the generation policy and user intent. Our pipeline begins with prompt engineering as a cold-start strategy, followed by the Supervised Fine-Tuning stage, in which we introduce a distillation method on click logs to create a robust foundational model. To better model user preferences while capturing their inherent uncertainty, we develop a Gaussian Reward Model (GaRM) that represents user preferences as probability distributions rather than point estimates. Finally, we employ reinforcement learning to align the generation policy with these preferences, guided by a composite reward function that integrates GaRM with auxiliary heuristics to mitigate reward hacking. To maintain training stability, this process is enhanced by a novel out-of-distribution regularization method and a two-stage reward fusion technique. Extensive experiments demonstrate that our framework significantly outperforms baselines on both automatic and human evaluations and yields a 34\% relative increase in user engagement as measured by click-through rate in live A/B tests.

