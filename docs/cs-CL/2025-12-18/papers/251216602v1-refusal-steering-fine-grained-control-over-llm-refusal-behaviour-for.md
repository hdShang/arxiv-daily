---
layout: default
title: "Refusal Steering: Fine-grained Control over LLM Refusal Behaviour for Sensitive Topics"
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

**Refusal Steering：通过激活向量干预实现对LLM在敏感话题上拒绝行为的细粒度控制**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `拒绝行为控制` `激活Steering` `政治敏感话题` `LLM-as-a-judge`

## 📋 核心要点

1. 现有方法难以对LLM在政治敏感话题上的拒绝行为进行细粒度控制，且依赖脆弱的模式匹配。
2. Refusal Steering通过LLM-as-a-judge评估拒绝置信度，并使用岭回归计算steering vectors，精准控制拒绝行为。
3. 实验表明，该方法在消除政治拒绝行为的同时，保持了模型在安全性和通用性能上的良好表现。

## 📝 摘要（中文）

本文提出了一种名为Refusal Steering的推理时方法，用于对大型语言模型在政治敏感话题上的拒绝行为进行细粒度控制，而无需重新训练。该方法使用LLM-as-a-judge来替代脆弱的基于模式的拒绝检测，并赋予拒绝置信度分数。同时，提出了一种岭正则化变体来计算steering vectors，从而更好地隔离拒绝-顺从方向。在Qwen3-Next-80B-A3B-Thinking模型上，该方法消除了模型在政治敏感话题上的拒绝行为，同时在JailbreakBench上保持了安全性，并在通用基准测试上保持了接近基线的性能。该方法可以推广到4B和80B模型，并且可以在需要时诱导有针对性的拒绝。分析表明，拒绝信号集中在Transformer的更深层，并且分布在许多维度上。这些结果表明，激活steering可以消除政治拒绝行为，同时保持对有害内容的安全对齐，从而为推理时可控、透明的审核提供了一条实用途径。

## 🔬 方法详解

**问题定义**：论文旨在解决大型语言模型（LLM）在处理政治敏感话题时，拒绝回答或提供信息的行为控制问题。现有方法通常依赖于基于模式的拒绝检测，这种方法脆弱且难以泛化。此外，缺乏对拒绝行为进行细粒度控制的手段，难以在安全性、通用性和政治敏感性之间取得平衡。

**核心思路**：论文的核心思路是利用激活steering技术，通过计算和应用steering vectors来干预LLM的内部激活状态，从而控制其拒绝行为。关键在于使用LLM本身作为裁判（LLM-as-a-judge）来评估拒绝的置信度，并使用岭回归来更精确地计算steering vectors，从而更好地分离拒绝和顺从的方向。

**技术框架**：整体框架包含以下几个主要步骤：1) 使用LLM-as-a-judge对模型的拒绝行为进行评分，生成拒绝置信度；2) 使用带岭正则化的线性模型，基于模型的激活状态和拒绝置信度，计算steering vectors；3) 在推理时，将计算得到的steering vectors添加到模型的激活状态中，从而引导模型的行为。

**关键创新**：最重要的创新点在于：1) 使用LLM-as-a-judge进行拒绝检测，避免了脆弱的模式匹配；2) 提出了一种岭正则化的steering vector计算方法，能够更有效地隔离拒绝和顺从的方向，从而实现更精确的控制；3) 证明了该方法可以在消除政治拒绝行为的同时，保持模型在安全性和通用性能上的良好表现。

**关键设计**：关键设计包括：1) LLM-as-a-judge的具体prompt设计，需要能够准确评估拒绝的置信度；2) 岭回归的正则化参数的选择，需要在steering vector的强度和模型的泛化能力之间进行权衡；3) steering vector应用的位置（Transformer的哪些层）和方式（加法或乘法）的选择，需要根据具体的模型和任务进行调整。

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

实验结果表明，Refusal Steering方法在Qwen3-Next-80B-A3B-Thinking模型上，成功消除了模型在政治敏感话题上的拒绝行为，同时在JailbreakBench上保持了安全性，并在通用基准测试上保持了接近基线的性能。该方法还成功推广到4B和80B模型，并实现了有针对性的拒绝。

## 🎯 应用场景

该研究成果可应用于需要对LLM输出进行精细控制的场景，例如：政治敏感话题的讨论、内容审核、个性化对话系统等。通过控制LLM的拒绝行为，可以使其在特定领域更加安全、可靠和可控。未来，该技术有望应用于更广泛的LLM应用中，实现更加透明和可控的人工智能系统。

## 📄 摘要（原文）

> We introduce Refusal Steering, an inference-time method to exercise fine-grained control over Large Language Models refusal behaviour on politically sensitive topics without retraining. We replace fragile pattern-based refusal detection with an LLM-as-a-judge that assigns refusal confidence scores and we propose a ridge-regularized variant to compute steering vectors that better isolate the refusal--compliance direction. On Qwen3-Next-80B-A3B-Thinking, our method removes the refusal behaviour of the model around politically sensitive topics while maintaining safety on JailbreakBench and near-baseline performance on general benchmarks. The approach generalizes across 4B and 80B models and can also induce targeted refusals when desired. We analize the steering vectors and show that refusal signals concentrate in deeper layers of the transformer and are distributed across many dimensions. Together, these results demonstrate that activation steering can remove political refusal behaviour while retaining safety alignment for harmful content, offering a practical path to controllable, transparent moderation at inference time.

