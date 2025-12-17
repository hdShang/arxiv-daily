---
layout: default
title: The Laminar Flow Hypothesis: Detecting Jailbreaks via Semantic Turbulence in Large Language Models
---

# The Laminar Flow Hypothesis: Detecting Jailbreaks via Semantic Turbulence in Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13741" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13741</a>
  <a href="https://arxiv.org/pdf/2512.13741.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13741" onclick="toggleFavorite(this, '2512.13741', 'The Laminar Flow Hypothesis: Detecting Jailbreaks via Semantic Turbulence in Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md. Hasib Ur Rahman

**分类**: cs.LG, cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出层流假设，通过语义湍流检测大语言模型的越狱攻击**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `越狱攻击` `安全防御` `语义湍流` `层流假设`

## 📋 核心要点

1. 现有防御LLM越狱攻击的方法依赖高成本的外部分类器或脆弱的词汇过滤，忽略了模型推理的内在动态。
2. 论文提出层流假设，认为良性输入导致平滑转换，而恶意攻击导致潜在空间中的“语义湍流”。
3. 实验表明，语义湍流可有效检测越狱攻击，并能诊断黑盒模型的底层安全架构，无需额外训练。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的普及，保护它们免受对抗性“越狱”攻击的挑战日益严峻。目前的防御策略通常依赖于计算成本高昂的外部分类器或脆弱的词汇过滤器，忽略了模型推理过程的内在动态。本文提出了层流假设，该假设认为良性输入会在LLM的高维潜在空间中引起平滑、渐进的转换，而对抗性提示会触发混乱、高方差的轨迹——称为语义湍流，这是由于安全对齐和指令遵循目标之间的内部冲突造成的。通过一种新颖的零样本指标：层间余弦速度的方差，将这种现象形式化。对各种小型语言模型的实验评估揭示了惊人的诊断能力。经过RLHF对齐的Qwen2-1.5B在受到攻击时，湍流显著增加了75.4%（p小于0.001），验证了内部冲突的假设。相反，Gemma-2B的湍流减少了22.0%，体现了一种独特的、低熵的“基于反射”的拒绝机制。这些发现表明，语义湍流不仅可以作为一种轻量级的实时越狱检测器，还可以作为一种非侵入性的诊断工具，用于对黑盒模型的底层安全架构进行分类。

## 🔬 方法详解

**问题定义**：当前大型语言模型面临着日益严峻的越狱攻击威胁，现有的防御方法，如外部分类器和词汇过滤器，存在计算成本高、易被绕过等问题，无法有效捕捉模型内部的推理过程和潜在的安全漏洞。因此，需要一种轻量级、实时的检测方法，能够深入理解模型内部状态，从而更有效地防御越狱攻击。

**核心思路**：论文的核心思路是基于“层流假设”，即良性输入在LLM的潜在空间中产生平滑的轨迹，而恶意攻击会引发混乱的“语义湍流”。通过量化这种湍流程度，可以判断输入是否为越狱攻击。这种方法无需额外的训练数据或模型，直接利用模型自身的内部状态进行判断。

**技术框架**：该方法主要包含以下几个步骤：1) 获取LLM各层的输出向量；2) 计算相邻层之间输出向量的余弦相似度，得到层间余弦速度；3) 计算层间余弦速度的方差，作为语义湍流的度量；4) 将语义湍流值与预设阈值进行比较，判断是否为越狱攻击。整体流程简单高效，易于部署。

**关键创新**：该方法最重要的创新在于提出了“语义湍流”的概念，并将其与越狱攻击联系起来。通过量化模型内部状态的混乱程度，实现了对越狱攻击的零样本检测。与传统的基于规则或分类器的防御方法相比，该方法更加灵活、鲁棒，能够应对各种新型的越狱攻击。

**关键设计**：关键设计在于层间余弦速度方差的计算。选择余弦相似度是因为它能够衡量向量方向的差异，而忽略向量长度的影响，从而更好地捕捉模型内部状态的变化。方差则用于量化层间余弦速度的波动程度，反映语义湍流的强度。阈值的设定可以根据具体的模型和应用场景进行调整。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13741/Untitledpresentation.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13741/laminar.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13741/download1.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，该方法能够有效检测越狱攻击。在RLHF对齐的Qwen2-1.5B模型上，受到攻击时语义湍流显著增加了75.4%（p<0.001）。而在Gemma-2B模型上，语义湍流减少了22.0%，表明其采用了一种不同的防御机制。这些结果验证了层流假设的有效性，并展示了该方法在不同模型上的适用性。

## 🎯 应用场景

该研究成果可应用于各种需要保护大型语言模型免受越狱攻击的场景，例如智能客服、内容生成、代码助手等。通过实时检测和阻止恶意输入，可以有效防止模型被用于生成有害信息、泄露敏感数据或执行恶意代码。此外，该方法还可以作为一种诊断工具，帮助研究人员理解和改进LLM的安全架构。

## 📄 摘要（原文）

> As Large Language Models (LLMs) become ubiquitous, the challenge of securing them against adversarial "jailbreaking" attacks has intensified. Current defense strategies often rely on computationally expensive external classifiers or brittle lexical filters, overlooking the intrinsic dynamics of the model's reasoning process. In this work, the Laminar Flow Hypothesis is introduced, which posits that benign inputs induce smooth, gradual transitions in an LLM's high-dimensional latent space, whereas adversarial prompts trigger chaotic, high-variance trajectories - termed Semantic Turbulence - resulting from the internal conflict between safety alignment and instruction-following objectives. This phenomenon is formalized through a novel, zero-shot metric: the variance of layer-wise cosine velocity. Experimental evaluation across diverse small language models reveals a striking diagnostic capability. The RLHF-aligned Qwen2-1.5B exhibits a statistically significant 75.4% increase in turbulence under attack (p less than 0.001), validating the hypothesis of internal conflict. Conversely, Gemma-2B displays a 22.0% decrease in turbulence, characterizing a distinct, low-entropy "reflex-based" refusal mechanism. These findings demonstrate that Semantic Turbulence serves not only as a lightweight, real-time jailbreak detector but also as a non-invasive diagnostic tool for categorizing the underlying safety architecture of black-box models.

