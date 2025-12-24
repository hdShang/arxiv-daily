---
layout: default
title: I'll believe it when I see it: Images increase misinformation sharing in Vision-Language Models
---

# I'll believe it when I see it: Images increase misinformation sharing in Vision-Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13302" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13302v1</a>
  <a href="https://arxiv.org/pdf/2505.13302.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13302v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13302v1', 'I\'ll believe it when I see it: Images increase misinformation sharing in Vision-Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Alice Plebe, Timothy Douglas, Diana Riazi, R. Maria del Rio-Chanona

**分类**: cs.CL

**发布日期**: 2025-05-19

**🔗 代码/项目**: [GITHUB](https://github.com/3lis/misinfo_vlm)

---

## 💡 一句话要点

**提出视觉内容影响VLM信息分享倾向的研究**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉-语言模型` `虚假信息传播` `个性化条件` `多模态数据集` `信息分享决策` `模型鲁棒性` `新闻推荐系统`

## 📋 核心要点

1. 现有的视觉-语言模型在处理信息分享时，未能充分考虑视觉内容对信息可信度的影响，导致虚假信息传播风险增加。
2. 论文提出了一种新的提示策略，结合个性化条件，系统性地分析图像对VLMs重新分享决策的影响。
3. 实验结果显示，图像显著提高了虚假新闻的分享率，且不同模型对视觉信息的敏感性存在显著差异。

## 📝 摘要（中文）

随着大型语言模型在新闻推荐系统中的应用日益增多，关于其在传播虚假信息中的角色引发了关注。人类的研究表明，视觉内容能够提升信息的可信度和分享性，但其对视觉-语言模型（VLMs）的影响尚不明确。本文首次研究了图像如何影响VLMs重新分享新闻内容的倾向，探讨了不同模型家族之间的差异，以及个性化条件和内容属性如何调节这一行为。为支持分析，论文提出了两项方法论贡献：一种灵感来源于越狱的提示策略，用于引导VLMs的重新分享决策，同时模拟具有反社会特征和政治倾向的用户；以及一个包含经过事实核查的政治新闻的多模态数据集，配有相应的图像和真实的真实性标签。实验结果表明，图像的存在使得真实新闻的重新分享率提高了4.8%，而虚假新闻的重新分享率提高了15.0%。

## 🔬 方法详解

**问题定义**：本文旨在探讨视觉内容如何影响视觉-语言模型（VLMs）在新闻分享中的表现，尤其是其在传播虚假信息方面的倾向。现有方法未能有效评估图像对信息分享的影响，导致对模型行为的理解不足。

**核心思路**：论文通过引入一种新的提示策略，模拟具有特定个性特征的用户，分析图像在信息分享决策中的作用。这种设计旨在揭示不同个性特征如何影响模型对虚假信息的敏感性。

**技术框架**：研究采用了多模态数据集，包含经过事实核查的政治新闻及其对应图像。通过对不同模型家族的实验，评估图像对信息分享的影响。主要模块包括数据集构建、模型训练和实验评估。

**关键创新**：论文的主要创新在于提出了一种结合个性化条件的提示策略，能够有效引导VLMs的重新分享决策，并揭示了不同模型在处理视觉信息时的差异性。

**关键设计**：在实验中，采用了多种模型进行对比，设置了不同的个性化条件（如黑暗三角特征），并使用了特定的损失函数来优化模型的分享决策能力。

## 📊 实验亮点

实验结果显示，图像的存在使得真实新闻的重新分享率提高了4.8%，而虚假新闻的重新分享率则提高了15.0%。在所有测试的模型中，只有Claude-3-Haiku对视觉虚假信息表现出一定的鲁棒性，揭示了不同模型在处理视觉信息时的显著差异。

## 🎯 应用场景

该研究的潜在应用领域包括新闻推荐系统、社交媒体内容管理以及虚假信息检测等。通过深入理解视觉内容对信息分享的影响，可以为个性化AI系统的设计提供指导，帮助减少虚假信息的传播，提升信息的可靠性和用户的信任度。

## 📄 摘要（原文）

> Large language models are increasingly integrated into news recommendation systems, raising concerns about their role in spreading misinformation. In humans, visual content is known to boost credibility and shareability of information, yet its effect on vision-language models (VLMs) remains unclear. We present the first study examining how images influence VLMs' propensity to reshare news content, whether this effect varies across model families, and how persona conditioning and content attributes modulate this behavior. To support this analysis, we introduce two methodological contributions: a jailbreaking-inspired prompting strategy that elicits resharing decisions from VLMs while simulating users with antisocial traits and political alignments; and a multimodal dataset of fact-checked political news from PolitiFact, paired with corresponding images and ground-truth veracity labels. Experiments across model families reveal that image presence increases resharing rates by 4.8% for true news and 15.0% for false news. Persona conditioning further modulates this effect: Dark Triad traits amplify resharing of false news, whereas Republican-aligned profiles exhibit reduced veracity sensitivity. Of all the tested models, only Claude-3-Haiku demonstrates robustness to visual misinformation. These findings highlight emerging risks in multimodal model behavior and motivate the development of tailored evaluation frameworks and mitigation strategies for personalized AI systems. Code and dataset are available at: https://github.com/3lis/misinfo_vlm

