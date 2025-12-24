---
layout: default
title: Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders
---

# Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14536" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14536v2</a>
  <a href="https://arxiv.org/pdf/2505.14536.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14536v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14536v2', 'Breaking Bad Tokens: Detoxification of LLMs Using Sparse Autoencoders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Agam Goyal, Vedant Rathi, William Yeh, Yian Wang, Yuen Chen, Hari Sundaram

**分类**: cs.CL

**发布日期**: 2025-05-20 (更新: 2025-10-23)

**备注**: EMNLP 2025

---

## 💡 一句话要点

**利用稀疏自编码器实现大型语言模型的去毒化**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `去毒化` `稀疏自编码器` `激活引导` `因果干预` `安全性` `自然语言处理`

## 📋 核心要点

1. 现有的去毒化方法多为表面修复，容易被越狱攻击规避，无法有效解决大型语言模型生成的有毒输出问题。
2. 本文提出利用稀疏自编码器识别毒性相关方向，通过有针对性的激活引导进行去毒化，增强了干预的有效性。
3. 实验结果表明，在较强的引导强度下，毒性减少可达20%，同时保持了模型的知识和能力，尽管流畅性可能有所下降。

## 📝 摘要（中文）

大型语言模型（LLMs）在用户应用中广泛使用，但仍会生成不良的有毒输出，如粗俗语言和贬损性言论。尽管存在多种去毒化方法，但大多数仅进行表面修复，容易被越狱攻击规避。本文利用稀疏自编码器（SAEs）识别模型残差流中的毒性相关方向，并通过相应的解码器向量进行有针对性的激活引导。我们引入三种引导强度，并在GPT-2 Small和Gemma-2-2B上进行评估，揭示了毒性减少与语言流畅性之间的权衡。在较强的引导强度下，这些因果干预在减少毒性方面优于竞争基线，最高可减少20%的毒性，尽管在GPT-2 Small上流畅性可能会显著下降。重要的是，引导后的标准NLP基准分数保持稳定，表明模型的知识和一般能力得以保留。我们进一步表明，较宽的SAEs中的特征分离会妨碍安全干预，强调了分离特征学习的重要性。我们的发现突显了基于SAE的因果干预在LLM去毒化中的潜力和当前局限性，并为更安全的语言模型部署提供了实际指导。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型生成的有毒输出问题，现有方法多为表面修复，容易被规避，缺乏有效性和针对性。

**核心思路**：通过稀疏自编码器（SAEs）识别模型残差流中的毒性方向，进行有针对性的激活引导，以实现更有效的去毒化。

**技术框架**：整体架构包括稀疏自编码器的训练、毒性方向的识别、激活引导的实施以及效果评估，主要模块包括编码器、解码器和激活引导机制。

**关键创新**：引入了三种不同强度的引导策略，能够在减少毒性的同时保持语言流畅性，显著优于现有的去毒化基线方法。

**关键设计**：在设计中，采用了特定的损失函数来优化毒性识别，调整了解码器的参数设置，以实现最佳的激活引导效果。

## 📊 实验亮点

实验结果显示，在较强的激活引导下，毒性减少可达20%，同时在GPT-2 Small上保持了标准NLP基准分数的稳定，表明模型的知识和能力未受损。流畅性在不同引导强度下有所变化，强调了权衡的重要性。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在社交媒体、在线客服和内容生成等领域，能够有效减少有毒内容的生成，提高用户体验和安全性。未来，该方法可能推动更安全的语言模型部署，促进人机交互的健康发展。

## 📄 摘要（原文）

> Large language models (LLMs) are now ubiquitous in user-facing applications, yet they still generate undesirable toxic outputs, including profanity, vulgarity, and derogatory remarks. Although numerous detoxification methods exist, most apply broad, surface-level fixes and can therefore easily be circumvented by jailbreak attacks. In this paper we leverage sparse autoencoders (SAEs) to identify toxicity-related directions in the residual stream of models and perform targeted activation steering using the corresponding decoder vectors. We introduce three tiers of steering aggressiveness and evaluate them on GPT-2 Small and Gemma-2-2B, revealing trade-offs between toxicity reduction and language fluency. At stronger steering strengths, these causal interventions surpass competitive baselines in reducing toxicity by up to 20%, though fluency can degrade noticeably on GPT-2 Small depending on the aggressiveness. Crucially, standard NLP benchmark scores upon steering remain stable, indicating that the model's knowledge and general abilities are preserved. We further show that feature-splitting in wider SAEs hampers safety interventions, underscoring the importance of disentangled feature learning. Our findings highlight both the promise and the current limitations of SAE-based causal interventions for LLM detoxification, further suggesting practical guidelines for safer language-model deployment.

