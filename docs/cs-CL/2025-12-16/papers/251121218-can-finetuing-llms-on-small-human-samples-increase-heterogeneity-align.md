---
layout: default
title: Can Finetuing LLMs on Small Human Samples Increase Heterogeneity, Alignment, and Belief-Action Coherence?
---

# Can Finetuing LLMs on Small Human Samples Increase Heterogeneity, Alignment, and Belief-Action Coherence?

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21218" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21218</a>
  <a href="https://arxiv.org/pdf/2511.21218.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21218" onclick="toggleFavorite(this, '2511.21218', 'Can Finetuing LLMs on Small Human Samples Increase Heterogeneity, Alignment, and Belief-Action Coherence?')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Steven Wang, Kyle Hunt, Shaojie Tang, Kenneth Joseph

**分类**: cs.CL

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**通过少量人工样本微调LLM能否提升异质性、对齐性和信念-行为一致性？**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `行为模拟` `微调` `人类行为` `信念-行为一致性`

## 📋 核心要点

1. 现有研究表明，LLM在模拟人类行为时存在多样性不足、与少数群体错位以及信念与行为不一致等问题。
2. 该研究探索了使用少量人类数据微调LLM，以期改善其模拟人类行为的能力，使其更具真实性和可靠性。
3. 实验结果表明，微调可以显著提高LLM的异质性、对齐性和信念-行为一致性，但仍无法完全替代人类参与者进行推断分析。

## 📝 摘要（中文）

关于大型语言模型（LLM）是否可以替代人类参与者进行调查和实验研究，目前存在争议。尽管市场营销和心理学等领域的最新研究探索了基于LLM的模拟的潜力，但越来越多的证据表明这种做法存在问题：LLM通常无法与真实的人类行为对齐，表现出有限的多样性、少数群体系统性错位、组内方差不足以及陈述的信念与行为之间的差异。本研究探讨了一个重要且独特的问题：在少量人类调查数据（例如从初步研究中获得的数据）上进行微调，是否可以缓解这些问题并产生真实的模拟结果。我们使用关于信息披露的行为实验，比较了人类和LLM生成的响应在多个维度上的差异，包括分布差异、子群体对齐、信念-行为一致性以及回归系数的恢复。我们发现，相对于基础模型，在少量人类样本上进行微调可以显著提高异质性、对齐性和信念-行为一致性。然而，即使是性能最佳的微调模型也无法重现原始研究的回归系数，这表明LLM生成的数据仍然不适合替代人类参与者进行正式的推断分析。

## 🔬 方法详解

**问题定义**：论文旨在解决LLM在模拟人类行为时存在的不足，具体表现为异质性不足、与特定人群（如少数群体）的认知偏差不一致、以及信念和行为的不一致。现有方法直接使用预训练的LLM进行模拟，忽略了真实人类行为的细微差别，导致模拟结果与真实情况存在较大差距。

**核心思路**：论文的核心思路是通过在少量真实人类数据上对LLM进行微调，使LLM能够学习到人类行为的分布特征和内在逻辑，从而提高其模拟人类行为的真实性和可靠性。这种方法旨在弥合LLM的通用知识与特定人群或情境下的行为模式之间的差距。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 收集少量人类行为数据（例如，通过调查或实验）；2) 选择一个预训练的LLM作为基础模型；3) 使用收集到的人类数据对LLM进行微调；4) 使用微调后的LLM生成模拟数据；5) 将模拟数据与真实人类数据进行比较，评估微调的效果。评估指标包括分布差异、子群体对齐、信念-行为一致性以及回归系数的恢复。

**关键创新**：该研究的关键创新在于探索了使用少量人类数据微调LLM以改善其行为模拟能力。与直接使用预训练LLM相比，这种方法能够更好地捕捉人类行为的细微差别和内在逻辑。此外，该研究还系统地评估了微调对LLM在多个维度上的影响，包括异质性、对齐性和信念-行为一致性。

**关键设计**：该研究的关键设计包括：1) 选择合适的LLM作为基础模型；2) 设计有效的微调策略，例如选择合适的损失函数和学习率；3) 选择合适的评估指标来衡量微调的效果。具体来说，论文使用了一个关于信息披露的行为实验来收集人类数据，并使用回归分析来评估LLM是否能够重现原始研究的回归系数。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.21218/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.21218/x3.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2511.21218/x4.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，在少量人类样本上进行微调可以显著提高LLM的异质性、对齐性和信念-行为一致性。具体来说，微调后的LLM在分布差异、子群体对齐和信念-行为一致性方面都更接近真实人类数据。然而，即使是性能最佳的微调模型也无法完全重现原始研究的回归系数，这表明LLM生成的数据仍然不适合替代人类参与者进行正式的推断分析。

## 🎯 应用场景

该研究的潜在应用领域包括社会科学研究、市场调研、政策模拟等。通过使用微调后的LLM模拟人类行为，研究人员可以更高效地进行实验和分析，从而更好地理解人类行为的规律和影响因素。此外，该研究还可以为开发更智能、更人性化的AI系统提供借鉴，例如，可以用于构建更贴近用户需求的智能助手或推荐系统。

## 📄 摘要（原文）

> There is ongoing debate about whether large language models (LLMs) can serve as substitutes for human participants in survey and experimental research. While recent work in fields such as marketing and psychology has explored the potential of LLM-based simulation, a growing body of evidence cautions against this practice: LLMs often fail to align with real human behavior, exhibiting limited diversity, systematic misalignment for minority subgroups, insufficient within-group variance, and discrepancies between stated beliefs and actions. This study examines an important and distinct question in this domain: whether fine-tuning on a small subset of human survey data, such as that obtainable from a pilot study, can mitigate these issues and yield realistic simulated outcomes. Using a behavioral experiment on information disclosure, we compare human and LLM-generated responses across multiple dimensions, including distributional divergence, subgroup alignment, belief-action coherence, and the recovery of regression coefficients. We find that fine-tuning on small human samples substantially improves heterogeneity, alignment, and belief-action coherence relative to the base model. However, even the best-performing fine-tuned models fail to reproduce the regression coefficients of the original study, suggesting that LLM-generated data remain unsuitable for replacing human participants in formal inferential analyses.

