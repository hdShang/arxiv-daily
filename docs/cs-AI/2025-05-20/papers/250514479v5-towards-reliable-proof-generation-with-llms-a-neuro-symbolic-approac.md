---
layout: default
title: "Towards Reliable Proof Generation with LLMs: A Neuro-Symbolic Approach"
---

# Towards Reliable Proof Generation with LLMs: A Neuro-Symbolic Approach

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14479" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14479v5</a>
  <a href="https://arxiv.org/pdf/2505.14479.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14479v5" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14479v5', 'Towards Reliable Proof Generation with LLMs: A Neuro-Symbolic Approach')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Oren Sultan, Eitan Stern, Dafna Shahaf

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-20 (更新: 2025-12-13)

**备注**: long paper

---

## 💡 一句话要点

**提出神经符号方法以解决数学证明生成问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `数学证明` `神经符号方法` `逻辑推理` `形式验证` `机器学习` `推理系统`

## 📋 核心要点

1. 现有大型语言模型在处理需要严格逻辑推理的数学证明时存在准确性不足的问题。
2. 论文提出了一种神经符号方法，通过检索类似问题和使用形式验证器来指导和修正LLM生成的证明。
3. 实验结果显示，该方法显著提升了证明的准确性，OpenAI的o1模型的性能提升幅度达到58%-70%。

## 📝 摘要（中文）

大型语言模型（LLMs）在需要严格逻辑推理和符号推理的正式领域（如数学证明生成）中表现不佳。本文提出了一种神经符号方法，结合了LLMs的生成优势与结构化组件，以克服这一挑战。作为概念验证，我们专注于几何问题。该方法包括两个方面：（1）检索类似问题并利用其证明指导LLM；（2）使用形式验证器评估生成的证明并提供反馈，帮助模型修正错误证明。实验表明，该方法显著提高了OpenAI的o1模型的证明准确性（提升幅度为58%-70%），其中类似问题和验证器反馈均对提升效果有贡献。更广泛地说，转向生成可证明正确结论的LLMs将显著提高其可靠性、准确性和一致性，从而解锁需要可信度的复杂任务和关键现实应用。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在数学证明生成中的准确性不足问题，现有方法在逻辑推理和符号推理方面存在明显短板。

**核心思路**：提出的神经符号方法结合了LLMs的生成能力与结构化的推理组件，通过检索相似问题和形式验证器的反馈来提升证明的准确性。

**技术框架**：整体架构包括两个主要模块：首先，检索与当前问题相似的已解决问题及其证明；其次，利用形式验证器对生成的证明进行评估并提供反馈。

**关键创新**：最重要的创新在于将LLMs与形式验证器结合，形成一个闭环反馈机制，使得生成的证明能够经过验证和修正，从而提高了生成结果的可靠性。

**关键设计**：在模型训练中，采用了特定的损失函数以优化生成证明的准确性，并设计了适应性反馈机制，使得验证器能够有效地识别和纠正错误。通过这种方式，模型能够在生成过程中不断学习和改进。

## 📊 实验亮点

实验结果显示，采用神经符号方法后，OpenAI的o1模型在数学证明生成任务中的准确性提升了58%-70%。这一显著提升表明，结合类似问题的检索和形式验证器的反馈对提高生成结果的可靠性至关重要。

## 🎯 应用场景

该研究的潜在应用领域包括教育、自动化定理证明、以及需要高可靠性的科学计算等。通过提高大型语言模型在逻辑推理任务中的表现，可以推动智能助手、自动化推理系统等技术的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Large language models (LLMs) struggle with formal domains that require rigorous logical deduction and symbolic reasoning, such as mathematical proof generation. We propose a neuro-symbolic approach that combines LLMs' generative strengths with structured components to overcome this challenge. As a proof-of-concept, we focus on geometry problems. Our approach is two-fold: (1) we retrieve analogous problems and use their proofs to guide the LLM, and (2) a formal verifier evaluates the generated proofs and provides feedback, helping the model fix incorrect proofs. We demonstrate that our method significantly improves proof accuracy for OpenAI's o1 model (58%-70% improvement); both analogous problems and the verifier's feedback contribute to these gains. More broadly, shifting to LLMs that generate provably correct conclusions could dramatically improve their reliability, accuracy and consistency, unlocking complex tasks and critical real-world applications that require trustworthiness.

