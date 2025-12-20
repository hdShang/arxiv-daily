---
layout: default
title: Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics
---

# Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16602" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16602v1</a>
  <a href="https://arxiv.org/pdf/2512.16602.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16602v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16602v1', 'Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Iker García-Ferrero, David Montero, Roman Orus

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Refusal Steering：通过激活向量调控LLM在敏感话题上的拒绝行为**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `拒绝行为控制` `激活向量调控` `政治敏感话题` `推理时干预`

## 📋 核心要点

1. 现有方法依赖脆弱的模式匹配进行拒绝检测，缺乏细粒度控制能力，难以适应复杂场景。
2. Refusal Steering通过LLM裁判评估拒绝置信度，并使用岭回归计算steering vectors，精准控制拒绝行为。
3. 实验表明，该方法在消除政治敏感话题拒绝行为的同时，保持了模型在安全性和通用性能上的良好表现。

## 📝 摘要（中文）

本文提出了一种名为Refusal Steering的推理时方法，用于对大型语言模型（LLM）在政治敏感话题上的拒绝行为进行细粒度控制，而无需重新训练模型。该方法使用LLM作为裁判，取代了脆弱的基于模式的拒绝检测，并赋予拒绝置信度分数。此外，还提出了一种岭正则化变体来计算steering vectors，从而更好地隔离拒绝-顺从方向。在Qwen3-Next-80B-A3B-Thinking模型上，该方法消除了模型在政治敏感话题上的拒绝行为，同时保持了JailbreakBench上的安全性以及在通用基准测试上的接近基线性能。该方法可以推广到4B和80B模型，并且可以在需要时诱导有针对性的拒绝。通过分析steering vectors，表明拒绝信号集中在transformer的更深层，并且分布在许多维度上。这些结果表明，激活steering可以消除政治拒绝行为，同时保持对有害内容的安全对齐，从而为推理时可控、透明的审核提供了一条实用途径。

## 🔬 方法详解

**问题定义**：大型语言模型（LLM）在处理政治敏感话题时，常常会采取拒绝回答的方式以避免潜在的风险或争议。然而，这种一刀切的拒绝策略缺乏灵活性，无法满足不同场景下的需求。现有的基于模式匹配的拒绝检测方法脆弱且难以维护，无法实现细粒度的控制。因此，需要一种能够在推理时动态调整LLM拒绝行为的方法，使其既能避免有害内容，又能灵活应对政治敏感话题。

**核心思路**：Refusal Steering的核心思路是通过学习一个steering vector，在推理时对LLM的激活状态进行微调，从而改变其拒绝或顺从的倾向。该方法利用另一个LLM作为裁判，评估模型对特定问题的拒绝置信度，并基于此训练steering vector。通过调整steering vector的方向和强度，可以实现对LLM拒绝行为的精细控制。

**技术框架**：Refusal Steering主要包含以下几个阶段：1) **拒绝置信度评估**：使用一个预训练的LLM（裁判模型）对目标LLM的回答进行评估，输出一个拒绝置信度分数。2) **Steering Vector计算**：基于拒绝置信度分数，使用岭正则化回归方法学习一个steering vector，该向量代表了拒绝-顺从的方向。3) **推理时激活调控**：在推理时，将steering vector添加到目标LLM的激活状态中，从而改变其拒绝行为。

**关键创新**：Refusal Steering的关键创新在于：1) 使用LLM作为裁判，取代了传统的基于模式匹配的拒绝检测方法，提高了鲁棒性和泛化能力。2) 提出了一种岭正则化变体，用于计算steering vector，更好地隔离了拒绝-顺从方向，提高了控制精度。3) 实现了在推理时对LLM拒绝行为的细粒度控制，无需重新训练模型。

**关键设计**：在steering vector计算过程中，使用了岭正则化来防止过拟合，并提高steering vector的泛化能力。具体而言，损失函数包含一个L2正则化项，用于约束steering vector的模长。此外，实验中发现，将steering vector添加到transformer的更深层，可以获得更好的控制效果。具体添加的位置和层数需要根据具体模型进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16602v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16602v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16602v1/images/top_layer_pca_2d_chinabadWRMD.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

在Qwen3-Next-80B-A3B-Thinking模型上的实验表明，Refusal Steering可以有效消除模型在政治敏感话题上的拒绝行为，同时保持了JailbreakBench上的安全性以及在通用基准测试上的接近基线性能。该方法还可以推广到4B和80B模型，并且可以在需要时诱导有针对性的拒绝。分析表明，拒绝信号集中在transformer的更深层，并且分布在许多维度上。

## 🎯 应用场景

Refusal Steering可应用于各种需要对LLM拒绝行为进行精细控制的场景，例如：内容审核、智能客服、教育辅导等。通过调整LLM在政治敏感话题上的拒绝策略，可以使其更好地适应不同文化背景和用户需求。此外，该方法还可以用于诱导LLM在特定情况下采取拒绝行为，例如，当用户提出的问题涉及个人隐私或安全风险时。

## 📄 摘要（原文）

> We introduce Refusal Steering, an inference-time method to exercise fine-grained control over Large Language Models refusal behaviour on politically sensitive topics without retraining. We replace fragile pattern-based refusal detection with an LLM-as-a-judge that assigns refusal confidence scores and we propose a ridge-regularized variant to compute steering vectors that better isolate the refusal--compliance direction. On Qwen3-Next-80B-A3B-Thinking, our method removes the refusal behaviour of the model around politically sensitive topics while maintaining safety on JailbreakBench and near-baseline performance on general benchmarks. The approach generalizes across 4B and 80B models and can also induce targeted refusals when desired. We analize the steering vectors and show that refusal signals concentrate in deeper layers of the transformer and are distributed across many dimensions. Together, these results demonstrate that activation steering can remove political refusal behaviour while retaining safety alignment for harmful content, offering a practical path to controllable, transparent moderation at inference time.

