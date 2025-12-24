---
layout: default
title: Cascading Adversarial Bias from Injection to Distillation in Language Models
---

# Cascading Adversarial Bias from Injection to Distillation in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24842" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24842v2</a>
  <a href="https://arxiv.org/pdf/2505.24842.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24842v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24842v2', 'Cascading Adversarial Bias from Injection to Distillation in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Harsh Chaudhari, Jamie Hayes, Matthew Jagielski, Ilia Shumailov, Milad Nasr, Alina Oprea

**分类**: cs.LG, cs.CR

**发布日期**: 2025-05-30 (更新: 2025-10-05)

---

## 💡 一句话要点

**提出对抗性偏差传播机制以增强语言模型的安全性**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `对抗性攻击` `模型蒸馏` `偏见传播` `安全性研究` `自然语言处理`

## 📋 核心要点

1. 现有的蒸馏模型在面对对抗性注入偏见内容时存在显著的脆弱性，影响其安全性和可靠性。
2. 论文提出了两种偏见传播模式，分别为无目标传播和有目标传播，以研究偏见在蒸馏过程中的放大效应。
3. 实验结果显示，学生模型在特定任务中生成偏见响应的概率显著高于教师模型，揭示了当前防御机制的不足。

## 📝 摘要（中文）

模型蒸馏已成为创建小型可部署语言模型的重要手段，但其广泛应用引发了对抗性操控的安全隐患。本文研究了蒸馏模型在训练过程中对偏见内容的对抗性注入脆弱性。研究表明，攻击者可以通过最小的数据中毒向教师模型注入细微偏见，这些偏见会传播到学生模型并显著放大。我们提出了两种传播模式：无目标传播和有目标传播。实验结果显示，在有目标场景下，学生模型生成偏见响应的概率高达76.9%，显著高于教师模型的69.4%。此外，针对未见任务的无目标传播中，学生模型的对抗性偏见出现频率提高了6到29倍。我们的研究揭示了当前防御措施的不足，并提出了有效的对抗性偏见缓解策略设计原则。

## 🔬 方法详解

**问题定义**：本文旨在解决蒸馏模型在训练过程中对抗性偏见注入的脆弱性，现有方法未能有效防范此类攻击，导致模型安全性不足。

**核心思路**：通过研究偏见在教师模型与学生模型之间的传播机制，提出无目标和有目标两种传播模式，以揭示偏见的放大效应。

**技术框架**：研究框架包括教师模型的训练、数据中毒的实施、学生模型的蒸馏过程，以及对生成结果的偏见评估。主要模块包括数据注入、模型蒸馏和偏见检测。

**关键创新**：论文的创新在于提出了对抗性偏见的传播机制，揭示了偏见在不同任务间的传播特性，尤其是学生模型在特定任务中的偏见放大现象。

**关键设计**：实验中使用了25个中毒样本（0.25%的中毒率），并评估了不同偏见类型的影响，采用了多种蒸馏方法和评估指标以确保结果的可靠性。

## 📊 实验亮点

实验结果显示，在有目标场景下，学生模型生成偏见响应的概率高达76.9%，而教师模型为69.4%。在无目标传播中，学生模型在未见任务上的对抗性偏见出现频率提高了6到29倍，揭示了显著的安全隐患。

## 🎯 应用场景

该研究的潜在应用领域包括自然语言处理、对话系统和自动内容生成等。通过增强模型对对抗性偏见的抵抗力，可以提高系统的安全性和可靠性，减少潜在的社会影响。未来，该研究可能推动更安全的语言模型设计和应用。

## 📄 摘要（原文）

> Model distillation has become essential for creating smaller, deployable language models that retain larger system capabilities. However, widespread deployment raises concerns about resilience to adversarial manipulation. This paper investigates vulnerability of distilled models to adversarial injection of biased content during training. We demonstrate that adversaries can inject subtle biases into teacher models through minimal data poisoning, which propagates to student models and becomes significantly amplified. We propose two propagation modes: Untargeted Propagation, where bias affects multiple tasks, and Targeted Propagation, focusing on specific tasks while maintaining normal behavior elsewhere. With only 25 poisoned samples (0.25% poisoning rate), student models generate biased responses 76.9% of the time in targeted scenarios - higher than 69.4% in teacher models. For untargeted propagation, adversarial bias appears 6x-29x more frequently in student models on unseen tasks. We validate findings across six bias types (targeted advertisements, phishing links, narrative manipulations, insecure coding practices), various distillation methods, and different modalities spanning text and code generation. Our evaluation reveals shortcomings in current defenses - perplexity filtering, bias detection systems, and LLM-based autorater frameworks - against these attacks. Results expose significant security vulnerabilities in distilled models, highlighting need for specialized safeguards. We propose practical design principles for building effective adversarial bias mitigation strategies.

