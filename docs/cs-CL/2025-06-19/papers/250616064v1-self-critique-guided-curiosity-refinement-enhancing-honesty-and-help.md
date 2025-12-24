---
layout: default
title: "Self-Critique-Guided Curiosity Refinement: Enhancing Honesty and Helpfulness in Large Language Models via In-Context Learning"
---

# Self-Critique-Guided Curiosity Refinement: Enhancing Honesty and Helpfulness in Large Language Models via In-Context Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16064" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16064v1</a>
  <a href="https://arxiv.org/pdf/2506.16064.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16064v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16064v1', 'Self-Critique-Guided Curiosity Refinement: Enhancing Honesty and Helpfulness in Large Language Models via In-Context Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Duc Hieu Ho, Chenglin Fan

**分类**: cs.CL

**发布日期**: 2025-06-19

---

## 💡 一句话要点

**提出自我批评引导的好奇心优化以提升大型语言模型的诚实性与帮助性**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `自我批评` `好奇心优化` `诚实性` `帮助性` `自然语言处理` `模型评估`

## 📋 核心要点

1. 现有大型语言模型在生成诚实和有帮助的输出方面仍存在显著挑战，导致输出质量不稳定。
2. 本文提出了一种自我批评引导的好奇心优化提示策略，使模型能够在不额外训练的情况下自我优化响应。
3. 实验结果显示，该方法在所有评估模型中均实现了1.4%至4.3%的诚实性与帮助性得分提升，显著改善了输出质量。

## 📝 摘要（中文）

大型语言模型（LLMs）在多种自然语言任务中展现了强大的能力，但始终面临生成一致诚实和有帮助的输出的挑战。为了解决这一问题，本文通过对十种广泛使用的大型语言模型进行全面基准评估，并提出了一种新颖的提示策略——自我批评引导的好奇心优化提示。该策略的核心思想是使模型能够自我批评并在不进行额外训练的情况下优化其响应。实验结果表明，该方法在HONESET数据集上显著提高了模型的诚实性和帮助性得分，减少了低质量响应，提升了高质量响应的比例。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在生成输出时缺乏一致性和可靠性的问题。现有方法往往无法有效提升模型的诚实性和帮助性，导致用户体验不佳。

**核心思路**：论文提出的自我批评引导的好奇心优化策略，允许模型在生成响应后进行自我评估和优化，从而提高输出的质量和可靠性。该方法不需要额外的训练，具有较高的灵活性和可扩展性。

**技术框架**：整体架构包括两个主要模块：自我批评步骤和优化步骤。首先，模型生成初步响应，然后通过自我批评步骤评估该响应的质量，最后在优化步骤中进行调整和改进。

**关键创新**：最重要的创新在于引入了自我批评机制，使模型能够在生成过程中主动反思和改进，区别于传统的静态生成方法。

**关键设计**：在实现过程中，设计了轻量级的上下文步骤以支持自我批评和优化，确保模型能够在不增加计算负担的情况下提升输出质量。

## 📊 实验亮点

实验结果表明，采用自我批评引导的好奇心优化提示策略后，所有评估模型的诚实性与帮助性得分均有显著提升，相较于传统的好奇心驱动提示，得分提升幅度在1.4%至4.3%之间，显示出该方法的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括智能客服、教育辅导、内容生成等场景，能够显著提升用户与大型语言模型的交互体验。通过增强模型的诚实性和帮助性，该方法有助于构建更可信赖的人工智能系统，推动相关技术的广泛应用与发展。

## 📄 摘要（原文）

> Large language models (LLMs) have demonstrated robust capabilities across various natural language tasks. However, producing outputs that are consistently honest and helpful remains an open challenge. To overcome this challenge, this paper tackles the problem through two complementary directions. It conducts a comprehensive benchmark evaluation of ten widely used large language models, including both proprietary and open-weight models from OpenAI, Meta, and Google. In parallel, it proposes a novel prompting strategy, self-critique-guided curiosity refinement prompting. The key idea behind this strategy is enabling models to self-critique and refine their responses without additional training. The proposed method extends the curiosity-driven prompting strategy by incorporating two lightweight in-context steps including self-critique step and refinement step.
>   The experiment results on the HONESET dataset evaluated using the framework $\mathrm{H}^2$ (honesty and helpfulness), which was executed with GPT-4o as a judge of honesty and helpfulness, show consistent improvements across all models. The approach reduces the number of poor-quality responses, increases high-quality responses, and achieves relative gains in $\mathrm{H}^2$ scores ranging from 1.4% to 4.3% compared to curiosity-driven prompting across evaluated models. These results highlight the effectiveness of structured self-refinement as a scalable and training-free strategy to improve the trustworthiness of LLMs outputs.

