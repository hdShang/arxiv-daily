---
layout: default
title: Security Degradation in Iterative AI Code Generation -- A Systematic Analysis of the Paradox
---

# Security Degradation in Iterative AI Code Generation -- A Systematic Analysis of the Paradox

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.11022" class="toolbar-btn" target="_blank">📄 arXiv: 2506.11022v2</a>
  <a href="https://arxiv.org/pdf/2506.11022.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.11022v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.11022v2', 'Security Degradation in Iterative AI Code Generation -- A Systematic Analysis of the Paradox')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shivani Shukla, Himanshu Joshi, Romilla Syed

**分类**: cs.SE, cs.AI, cs.CL, cs.CR, cs.LG

**发布日期**: 2025-05-19 (更新: 2025-09-26)

**备注**: Keywords - Large Language Models, Security Vulnerabilities, AI-Generated Code, Iterative Feedback, Software Security, Secure Coding Practices, Feedback Loops, LLM Prompting Strategies

---

## 💡 一句话要点

**分析迭代AI代码生成中的安全退化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `代码生成` `安全漏洞` `人类验证` `迭代优化` `软件开发` `实验分析`

## 📋 核心要点

1. 核心问题：现有方法未能有效解决迭代生成代码中的安全漏洞演变，导致安全性下降。
2. 方法要点：通过控制实验分析不同提示策略对代码安全性的影响，提出人类验证的重要性。
3. 实验或效果：实验结果显示，经过五次迭代后，关键漏洞增加了37.6%，不同策略下漏洞模式各异。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在代码生成中的快速应用，软件开发发生了变革，但对安全漏洞在迭代反馈中如何演变的关注较少。本文通过对400个代码样本进行控制实验，分析了AI生成代码中的安全退化现象。研究发现，在仅经过五次迭代后，关键漏洞增加了37.6%，不同提示策略下出现了明显的漏洞模式。这一证据挑战了迭代LLM优化能提升代码安全性的假设，强调了人类专家在迭代过程中的重要性。我们提出了开发者应对这些风险的实用指南，强调在LLM迭代之间进行强有力的人类验证，以防止在所谓的代码“改进”过程中引入新的安全问题。

## 🔬 方法详解

**问题定义**：本文旨在解决在使用大型语言模型（LLMs）进行代码生成时，迭代过程中的安全漏洞演变问题。现有方法未能充分考虑迭代反馈对代码安全性的影响，导致潜在的安全风险增加。

**核心思路**：论文通过设计控制实验，分析不同提示策略对生成代码安全性的影响，强调人类专家在迭代过程中的必要性，以减少安全漏洞的引入。

**技术框架**：研究采用了一个包含400个代码样本的实验框架，分为40轮迭代，每轮使用四种不同的提示策略。每轮迭代后对生成代码进行安全性评估，观察漏洞的变化。

**关键创新**：最重要的创新在于揭示了迭代优化过程中安全漏洞的增加，挑战了传统观念，即认为迭代过程必然会提升代码安全性。

**关键设计**：实验中设置了明确的评估标准，采用了多种提示策略，并在每次迭代后进行系统的安全性分析，以确保结果的可靠性和有效性。实验设计的严谨性为后续研究提供了基础。

## 📊 实验亮点

实验结果显示，在经过五次迭代后，关键漏洞的数量增加了37.6%。不同的提示策略导致了不同的漏洞模式，这一发现对代码生成的安全性提出了新的挑战，强调了人类验证的重要性。

## 🎯 应用场景

该研究的潜在应用领域包括软件开发、代码审查和安全性评估等。通过提出的实用指南，开发者可以在使用LLMs进行代码生成时，采取有效措施降低安全风险，提升代码质量。这一研究为未来的AI辅助开发工具提供了重要的安全性参考。

## 📄 摘要（原文）

> The rapid adoption of Large Language Models(LLMs) for code generation has transformed software development, yet little attention has been given to how security vulnerabilities evolve through iterative LLM feedback. This paper analyzes security degradation in AI-generated code through a controlled experiment with 400 code samples across 40 rounds of "improvements" using four distinct prompting strategies. Our findings show a 37.6% increase in critical vulnerabilities after just five iterations, with distinct vulnerability patterns emerging across different prompting approaches. This evidence challenges the assumption that iterative LLM refinement improves code security and highlights the essential role of human expertise in the loop. We propose practical guidelines for developers to mitigate these risks, emphasizing the need for robust human validation between LLM iterations to prevent the paradoxical introduction of new security issues during supposedly beneficial code "improvements".

