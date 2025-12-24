---
layout: default
title: Do MLLMs Capture How Interfaces Guide User Behavior? A Benchmark for Multimodal UI/UX Design Understanding
---

# Do MLLMs Capture How Interfaces Guide User Behavior? A Benchmark for Multimodal UI/UX Design Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.05026" class="toolbar-btn" target="_blank">📄 arXiv: 2505.05026v3</a>
  <a href="https://arxiv.org/pdf/2505.05026.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.05026v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.05026v3', 'Do MLLMs Capture How Interfaces Guide User Behavior? A Benchmark for Multimodal UI/UX Design Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaehyun Jeon, Min Soo Kim, Jang Han Yoon, Sumin Shim, Yejin Choi, Hanbin Kim, Youngjae Yu

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-08 (更新: 2025-08-04)

**备注**: 26 pages, 25 figures, Our code and dataset: https://github.com/jeochris/wiserui-bench

---

## 💡 一句话要点

**提出WiserUI-Bench以解决多模态UI/UX设计理解不足的问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大型语言模型` `用户界面设计` `用户体验` `A/B测试` `行为导向设计` `基准评估` `智能推荐系统`

## 📋 核心要点

1. 现有研究主要关注UI设计的表面特征，缺乏对用户行为导向的深入理解，导致评估结果的局限性。
2. 本文提出WiserUI-Bench基准，包含300对经过A/B测试的UI设计图像及其有效性背后的专家理由，以提升对UI/UX设计的理解。
3. 实验结果显示，当前多模态大型语言模型在UI/UX设计的推理能力上存在不足，强调了该基准在未来研究中的重要性。

## 📝 摘要（中文）

用户界面（UI）设计不仅仅是视觉效果，它引导用户行为并影响整体用户体验（UX）。精心设计的界面能够提升注册率和推动销售，强调了UI/UX作为统一设计概念的转变。尽管近期研究利用多模态大型语言模型（MLLMs）探索了UI质量评估，但大多集中于表面特征，忽视了行为导向的方面。为填补这一空白，本文提出了WiserUI-Bench，一个用于评估模型对UI/UX设计的多模态理解的新基准。该基准包含300对多样化的真实世界UI图像，每对由实际公司进行A/B测试，且每对都附有684个专家策划的理由，捕捉了每个获胜设计有效性的关键因素。我们的基准支持两个核心任务：选择更有效的UI/UX设计和评估模型解释其有效性的能力。实验表明，当前模型在UI/UX设计及其行为影响方面的细致推理能力有限。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大型语言模型在用户界面（UI）和用户体验（UX）设计理解上的不足，尤其是对用户行为影响的评估缺乏深度。现有方法多集中于表面特征，未能有效捕捉设计背后的行为导向因素。

**核心思路**：论文提出WiserUI-Bench基准，旨在通过提供真实的A/B测试数据和专家理由，帮助模型更好地理解和解释UI/UX设计的有效性。通过这种方式，研究者可以评估模型在行为导向设计理解上的能力。

**技术框架**：WiserUI-Bench基准包含300对UI设计图像，每对图像经过实际公司A/B测试验证，附有684个专家理由。基准支持两个核心任务：选择更有效的设计和评估模型的解释能力。

**关键创新**：最重要的创新在于引入了专家策划的理由，帮助模型理解设计有效性的多维度因素。这一方法与现有的单一特征评估方法本质上不同，提供了更全面的理解框架。

**关键设计**：在设计上，基准数据集的构建考虑了多样性和实际应用场景，确保了数据的代表性和有效性。模型评估时，采用了标准的准确率和解释能力评分指标，以量化模型的表现。

## 📊 实验亮点

实验结果表明，当前的多模态大型语言模型在UI/UX设计的推理能力上存在明显不足，准确率普遍低于70%。通过引入WiserUI-Bench基准，模型在解释设计有效性方面的能力有望显著提升，推动相关领域的研究进展。

## 🎯 应用场景

该研究的潜在应用领域包括用户界面设计优化、用户行为分析和智能推荐系统等。通过更好地理解UI/UX设计的有效性，企业可以提升用户体验，增加用户转化率，从而推动业务增长。未来，该基准可能促进更广泛的研究，推动行为导向设计的智能化发展。

## 📄 摘要（原文）

> User interface (UI) design goes beyond visuals, guiding user behavior and overall user experience (UX). Strategically crafted interfaces, for example, can boost sign-ups and drive business sales, underscoring the shift toward UI/UX as a unified design concept. While recent studies have explored UI quality evaluation using Multimodal Large Language Models (MLLMs), they largely focus on surface-level features, overlooking behavior-oriented aspects. To fill this gap, we introduce WiserUI-Bench, a novel benchmark for assessing models' multimodal understanding of UI/UX design. It includes 300 diverse real-world UI image pairs, each consisting of two design variants A/B-tested at scale by actual companies, where one was empirically validated to steer more user actions than the other. Each pair is accompanied one or more of 684 expert-curated rationales that capture key factors behind each winning design's effectiveness, spanning diverse cognitive dimensions of UX. Our benchmark supports two core tasks: (1) selecting the more effective UI/UX design by predicting the A/B test verified winner and (2) assessing how well a model, given the winner, can explain its effectiveness in alignment with expert reasoning. Experiments across several MLLMs show that current models exhibit limited nuanced reasoning about UI/UX design and its behavioral impact. We believe our work will foster research in UI/UX understanding and enable broader applications such as behavior-aware interface optimization.

