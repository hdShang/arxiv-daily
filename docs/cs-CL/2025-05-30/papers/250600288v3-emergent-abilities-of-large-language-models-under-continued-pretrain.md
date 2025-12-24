---
layout: default
title: Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation
---

# Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00288" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00288v3</a>
  <a href="https://arxiv.org/pdf/2506.00288.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00288v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00288v3', 'Emergent Abilities of Large Language Models under Continued Pretraining for Language Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ahmed Elhady, Eneko Agirre, Mikel Artetxe

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-30 (更新: 2025-09-19)

**备注**: Published as a Conference Paper at the main track of ACL 2025

---

## 💡 一句话要点

**提出继续预训练方法以增强语言适应能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `继续预训练` `语言适应` `大型语言模型` `灾难性遗忘` `课程学习` `指数移动平均` `多语言处理`

## 📋 核心要点

1. 现有的继续预训练方法在适应新语言时，未能充分研究英语数据的作用，导致下游能力的缺失。
2. 本文提出了一种语言无关的基准测试，揭示了不包含英语时模型在目标语言的灾难性遗忘现象。
3. 通过引入课程学习和EMA，研究表明这些方法能有效缓解对英语数据的依赖，提升模型的泛化能力。

## 📝 摘要（中文）

继续预训练（CPT）是将现有大型语言模型（LLMs）适应新语言的常用方法。本文研究了在CPT过程中包含英语数据的作用，发现虽然其对验证困惑度没有影响，但对目标语言下游能力的出现至关重要。我们引入了一种语言无关的上下文学习基准，揭示了在不包含英语时，CPT早期会出现灾难性遗忘，损害模型在目标语言的泛化能力。基于这些发现，本文提出了课程学习和权重的指数移动平均（EMA）作为有效的替代方案，以减少对英语的依赖。整体而言，本研究揭示了在进行语言适应的CPT过程中，如何产生新兴能力的动态，为未来设计更有效的方法奠定了基础。

## 🔬 方法详解

**问题定义**：本文旨在解决在继续预训练过程中，英语数据对模型适应新语言能力的影响，现有方法未能充分探讨这一问题。

**核心思路**：通过引入语言无关的基准测试，揭示不包含英语数据时模型的灾难性遗忘现象，进而提出课程学习和EMA作为解决方案。

**技术框架**：整体流程包括数据准备、模型预训练、评估基准测试和应用课程学习与EMA等模块，确保模型在目标语言上的有效适应。

**关键创新**：最重要的创新在于识别出英语数据在CPT中的关键作用，及其对模型能力的影响，提出了新的评估方法和训练策略。

**关键设计**：在参数设置上，采用了课程学习策略和EMA技术，确保模型在训练过程中能够有效保留重要信息，避免灾难性遗忘。具体损失函数和网络结构设计未详细披露，待进一步研究。

## 📊 实验亮点

实验结果表明，在不包含英语数据的情况下，模型在目标语言的泛化能力显著下降，验证困惑度未能反映这一变化。通过引入课程学习和EMA，模型在目标语言的表现得到了有效提升，展示了新兴能力的动态变化。

## 🎯 应用场景

该研究的潜在应用领域包括多语言处理、机器翻译和跨语言信息检索等。通过提升大型语言模型的语言适应能力，可以更好地服务于全球用户，推动自然语言处理技术的普及与发展。未来，这些方法可能会影响多语言模型的设计和训练策略，促进更广泛的应用。

## 📄 摘要（原文）

> Continued pretraining (CPT) is a popular approach to adapt existing large language models (LLMs) to new languages. When doing so, it is common practice to include a portion of English data in the mixture, but its role has not been carefully studied to date. In this work, we show that including English does not impact validation perplexity, yet it is critical for the emergence of downstream capabilities in the target language. We introduce a language-agnostic benchmark for in-context learning (ICL), which reveals catastrophic forgetting early on CPT when English is not included. This in turn damages the ability of the model to generalize to downstream prompts in the target language as measured by perplexity, even if it does not manifest in terms of accuracy until later in training, and can be tied to a big shift in the model parameters. Based on these insights, we introduce curriculum learning and exponential moving average (EMA) of weights as effective alternatives to mitigate the need for English. All in all, our work sheds light into the dynamics by which emergent abilities arise when doing CPT for language adaptation, and can serve as a foundation to design more effective methods in the future.

