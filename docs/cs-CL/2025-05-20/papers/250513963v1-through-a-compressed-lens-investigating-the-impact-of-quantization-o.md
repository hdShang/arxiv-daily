---
layout: default
title: "Through a Compressed Lens: Investigating the Impact of Quantization on LLM Explainability and Interpretability"
---

# Through a Compressed Lens: Investigating the Impact of Quantization on LLM Explainability and Interpretability

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13963" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13963v1</a>
  <a href="https://arxiv.org/pdf/2505.13963.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13963v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13963v1', 'Through a Compressed Lens: Investigating the Impact of Quantization on LLM Explainability and Interpretability')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qianli Wang, Mingyang Wang, Nils Feldhus, Simon Ostermann, Yuan Cao, Hinrich Schütze, Sebastian Möller, Vera Schmitt

**分类**: cs.CL, cs.LG

**发布日期**: 2025-05-20

**备注**: In submission

---

## 💡 一句话要点

**研究量化对大语言模型可解释性与可理解性的影响**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `量化技术` `大语言模型` `可解释性` `可理解性` `自然语言处理`

## 📋 核心要点

1. 现有研究主要关注量化对LLM性能的影响，但对其可解释性和可理解性的影响尚未探讨，存在研究空白。
2. 本文通过对比三种量化技术和两种可解释性、可理解性方法，系统性地评估量化对模型透明度的影响。
3. 实验结果表明，量化对可解释性和可理解性的影响不一致，某些情况下甚至提升了模型的透明度，提示需谨慎使用。

## 📝 摘要（中文）

量化方法广泛用于加速推理和简化大语言模型（LLMs）的部署。尽管先前研究已深入探讨量化对LLM能力的影响，但其对模型可解释性和可理解性的影响尚未被充分研究。为填补这一空白，本文通过三种常见的量化技术和两种可解释性方法（反事实示例和自然语言解释）以及两种可理解性方法（知识记忆分析和潜在多跳推理分析）进行了全面实验。研究发现，量化对模型的可解释性和可理解性有显著影响，且这种影响的方向依赖于量化方法、可解释性或可理解性方法及评估协议。在某些设置中，量化降低了可解释性，而在其他设置中则可能导致改善。此研究为在需要透明度的应用中部署LLMs提供了重要的启示。

## 🔬 方法详解

**问题定义**：本文旨在探讨量化对大语言模型可解释性和可理解性的影响，现有研究未能充分考虑这一重要方面，导致在实际应用中可能出现透明度不足的问题。

**核心思路**：通过系统性实验，结合不同的量化技术和可解释性方法，评估量化对模型透明度的影响，旨在揭示量化与可解释性之间的复杂关系。

**技术框架**：研究采用三种量化技术（不同位宽）与两种可解释性方法（反事实示例、自然语言解释）及两种可理解性方法（知识记忆分析、潜在多跳推理分析）进行实验，构建了一个多维度的评估框架。

**关键创新**：本研究首次系统性地探讨了量化对LLM可解释性和可理解性的影响，揭示了量化方法与可解释性方法之间的相互作用，填补了现有文献的空白。

**关键设计**：实验中采用了不同的量化位宽和评估协议，结合用户研究评估可解释性方法的有效性，确保了结果的可靠性和实用性。实验设计考虑了多种变量，以全面反映量化对模型透明度的影响。

## 📊 实验亮点

实验结果显示，量化对模型可解释性的影响具有不确定性。在某些配置下，量化导致可解释性下降，而在其他配置下则可能提升可解释性，提示研究者在部署LLM时需谨慎考虑量化策略。具体性能数据和提升幅度在不同实验设置中有所不同，强调了量化方法选择的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、智能客服和决策支持系统等，尤其是在需要高透明度和可解释性的场景中。研究结果为开发更具透明度的LLM提供了理论依据，促进了相关技术的实际应用与推广。

## 📄 摘要（原文）

> Quantization methods are widely used to accelerate inference and streamline the deployment of large language models (LLMs). While prior research has extensively investigated the degradation of various LLM capabilities due to quantization, its effects on model explainability and interpretability, which are crucial for understanding decision-making processes, remain unexplored. To address this gap, we conduct comprehensive experiments using three common quantization techniques at distinct bit widths, in conjunction with two explainability methods, counterfactual examples and natural language explanations, as well as two interpretability approaches, knowledge memorization analysis and latent multi-hop reasoning analysis. We complement our analysis with a thorough user study, evaluating selected explainability methods. Our findings reveal that, depending on the configuration, quantization can significantly impact model explainability and interpretability. Notably, the direction of this effect is not consistent, as it strongly depends on (1) the quantization method, (2) the explainability or interpretability approach, and (3) the evaluation protocol. In some settings, human evaluation shows that quantization degrades explainability, while in others, it even leads to improvements. Our work serves as a cautionary tale, demonstrating that quantization can unpredictably affect model transparency. This insight has important implications for deploying LLMs in applications where transparency is a critical requirement.

