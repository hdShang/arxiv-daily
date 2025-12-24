---
layout: default
title: "Mind the XAI Gap: A Human-Centered LLM Framework for Democratizing Explainable AI"
---

# Mind the XAI Gap: A Human-Centered LLM Framework for Democratizing Explainable AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.12240" class="toolbar-btn" target="_blank">📄 arXiv: 2506.12240v1</a>
  <a href="https://arxiv.org/pdf/2506.12240.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.12240v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.12240v1', 'Mind the XAI Gap: A Human-Centered LLM Framework for Democratizing Explainable AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Eva Paraschou, Ioannis Arapakis, Sofia Yfantidou, Sebastian Macaluso, Athena Vakali

**分类**: cs.LG, cs.AI

**发布日期**: 2025-06-13

**备注**: Accepted for publication at The 3rd World Conference on eXplainable Artificial Intelligence. This version corresponds to the camera-ready manuscript submitted to the conference proceedings

---

## 💡 一句话要点

**提出人本中心的LLM框架以解决可解释AI的透明性问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `可解释AI` `大型语言模型` `人本中心` `透明性` `上下文学习` `用户研究` `基准测试`

## 📋 核心要点

1. 现有可解释AI方法多面向专家，非专家难以理解，导致透明性不足。
2. 提出一个通用框架，利用大型语言模型和上下文学习，提供适合专家和非专家的解释。
3. 通过基准测试和用户研究，验证了框架的高质量内容和对非专家的友好性，Spearman相关系数达到0.92。

## 📝 摘要（中文）

人工智能（AI）迅速融入关键决策系统，但其基础的“黑箱”模型需要可解释AI（XAI）解决方案以增强透明性，现有方案多面向专家，非专家难以理解。本文提出一个领域、模型和解释无关的通用框架，确保透明性和人本中心的解释，适应专家和非专家的需求。该框架利用大型语言模型（LLMs）和上下文学习，将领域和可解释性相关的知识传递给LLMs。通过严格的基准测试，我们证明了该框架的高内容质量和对非专家的友好性，建立了信任于LLMs作为人本中心可解释AI的推动者。

## 🔬 方法详解

**问题定义**：本文旨在解决现有可解释AI方法对非专家的理解障碍，现有方法多为专家导向，缺乏人本中心的透明性和可理解性。

**核心思路**：提出一个领域、模型和解释无关的框架，利用大型语言模型（LLMs）和上下文学习，将相关知识融入模型中，以便为不同背景的用户提供适当的解释。

**技术框架**：框架包括结构化提示和系统设置，能够在单一响应中提供非专家可理解的解释和专家所需的技术信息，确保符合领域和可解释性原则。

**关键创新**：最重要的创新在于框架的通用性和可重复性，能够同时满足专家和非专家的需求，显著提升了可解释AI的透明性。

**关键设计**：框架通过严格的基准测试建立了真实的上下文“同义词库”，并在超过40种数据、模型和XAI组合中进行评估，确保了高质量的内容和用户友好性。具体的参数设置和损失函数细节在论文中进行了详细描述。

## 📊 实验亮点

实验结果显示，框架的内容质量与真实解释之间的Spearman相关系数达到0.92，表明高一致性。此外，用户研究表明，非专家用户对框架提供的解释感到更易理解和友好，显著提升了解释的可解释性和人性化。

## 🎯 应用场景

该研究的潜在应用领域包括医疗决策、金融分析和自动化系统等，能够帮助非专家用户理解AI决策过程，提升对AI系统的信任和接受度。未来，该框架可能在各类需要透明性和可解释性的AI应用中发挥重要作用。

## 📄 摘要（原文）

> Artificial Intelligence (AI) is rapidly embedded in critical decision-making systems, however their foundational ``black-box'' models require eXplainable AI (XAI) solutions to enhance transparency, which are mostly oriented to experts, making no sense to non-experts. Alarming evidence about AI's unprecedented human values risks brings forward the imperative need for transparent human-centered XAI solutions. In this work, we introduce a domain-, model-, explanation-agnostic, generalizable and reproducible framework that ensures both transparency and human-centered explanations tailored to the needs of both experts and non-experts. The framework leverages Large Language Models (LLMs) and employs in-context learning to convey domain- and explainability-relevant contextual knowledge into LLMs. Through its structured prompt and system setting, our framework encapsulates in one response explanations understandable by non-experts and technical information to experts, all grounded in domain and explainability principles. To demonstrate the effectiveness of our framework, we establish a ground-truth contextual ``thesaurus'' through a rigorous benchmarking with over 40 data, model, and XAI combinations for an explainable clustering analysis of a well-being scenario. Through a comprehensive quality and human-friendliness evaluation of our framework's explanations, we prove high content quality through strong correlations with ground-truth explanations (Spearman rank correlation=0.92) and improved interpretability and human-friendliness to non-experts through a user study (N=56). Our overall evaluation confirms trust in LLMs as HCXAI enablers, as our framework bridges the above Gaps by delivering (i) high-quality technical explanations aligned with foundational XAI methods and (ii) clear, efficient, and interpretable human-centered explanations for non-experts.

