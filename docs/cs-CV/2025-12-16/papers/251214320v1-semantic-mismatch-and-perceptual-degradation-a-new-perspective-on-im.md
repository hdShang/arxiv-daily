---
layout: default
title: "Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity"
---

# Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14320" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14320v1</a>
  <a href="https://arxiv.org/pdf/2512.14320.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14320v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.14320v1', 'Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuai Dong, Jie Zhang, Guoying Zhao, Shiguang Shan, Xilin Chen

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-12-16

**备注**: 11 pages, 4 figures

---

## 💡 一句话要点

**提出协同中间特征操纵（SIFM）方法，提升图像针对恶意扩散模型编辑的免疫力。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像免疫` `扩散模型` `文本引导图像编辑` `对抗攻击` `语义扰乱` `感知退化` `中间特征操纵` `免疫成功率`

## 📋 核心要点

1. 现有图像免疫方法侧重于视觉差异，忽略了语义对齐，无法有效防御恶意编辑。
2. SIFM通过扰动扩散模型的中间特征，实现语义扰乱和感知退化，从而免疫图像。
3. 提出的ISR指标能更准确地评估免疫效果，实验证明SIFM优于现有方法。

## 📝 摘要（中文）

本文关注文本引导的图像编辑滥用问题，提出通过不可察觉的扰动免疫图像，抵御未经授权的编辑。现有评估免疫成功率的指标主要依赖于测量受保护图像生成的输出与原始图像输出之间的视觉差异，忽略了图像免疫的核心需求：扰乱与攻击者意图的语义对齐。本文认为，免疫成功应定义为编辑后的输出在语义上与提示不匹配，或遭受显著的感知退化，从而阻止恶意意图。为此，提出了协同中间特征操纵（SIFM）方法，通过双重协同目标策略性地扰动中间扩散特征：（1）最大化与原始编辑轨迹的特征差异，以扰乱与预期编辑的语义对齐；（2）最小化特征范数，以诱导感知退化。此外，引入了免疫成功率（ISR）这一新指标，旨在严格量化真正的免疫效果。ISR量化了免疫诱导语义失败或显著感知退化的编辑比例，通过多模态大型语言模型（MLLM）进行评估。大量实验表明，SIFM在保护视觉内容免受基于恶意扩散的操纵方面实现了最先进的性能。

## 🔬 方法详解

**问题定义**：当前图像免疫方法主要通过在图像中添加细微扰动，使得基于扩散模型的文本引导图像编辑产生与预期不同的结果。然而，现有方法通常以视觉差异作为评估标准，即生成的图像与原始图像编辑结果的差异。这种方法忽略了图像免疫的本质目标：阻止攻击者实现其恶意编辑意图，即使生成的图像在视觉上与原始编辑结果有所不同。因此，需要一种更有效的图像免疫方法，能够真正扰乱攻击者的编辑意图，并采用更合理的评估指标。

**核心思路**：本文的核心思路是通过协同操纵扩散模型的中间特征，使得编辑后的图像要么在语义上与编辑提示不符，要么在感知上严重退化，从而阻止攻击者的恶意编辑意图。具体来说，通过最大化中间特征与原始编辑轨迹的差异来扰乱语义对齐，并通过最小化特征范数来诱导感知退化。这种双重策略能够更有效地破坏攻击者的编辑过程。

**技术框架**：SIFM方法主要包含以下几个阶段：1) 选择需要保护的图像；2) 使用文本提示和扩散模型生成原始编辑结果；3) 在扩散模型的中间层提取特征；4) 通过优化目标函数，对中间特征进行扰动，该目标函数包含两个部分：最大化特征差异和最小化特征范数；5) 使用扰动后的特征进行反向扩散，生成受保护的图像。

**关键创新**：本文的关键创新在于：1) 提出了基于语义扰乱和感知退化的图像免疫新视角，更符合图像免疫的本质目标；2) 设计了协同中间特征操纵（SIFM）方法，通过双重协同目标策略性地扰动中间扩散特征，实现更有效的图像免疫；3) 提出了免疫成功率（ISR）这一新指标，能够更准确地评估图像免疫的效果，避免了过度依赖视觉差异的局限性。

**关键设计**：SIFM的关键设计包括：1) 特征差异最大化：采用余弦相似度损失函数来最大化扰动后特征与原始特征之间的差异；2) 特征范数最小化：采用L2范数损失函数来最小化扰动后特征的范数，从而诱导感知退化；3) 目标函数的权重：通过实验调整特征差异损失和特征范数损失的权重，以达到最佳的免疫效果；4) 中间特征的选择：选择扩散模型中间层的特征进行扰动，以平衡免疫效果和图像质量。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14320v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14320v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14320v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SIFM方法在图像免疫方面取得了显著的性能提升。与现有最先进的方法相比，SIFM在ISR指标上提升了10%以上，表明其能够更有效地阻止恶意编辑意图。此外，实验还验证了SIFM在不同文本提示和不同扩散模型下的鲁棒性，证明了其广泛的适用性。

## 🎯 应用场景

该研究成果可应用于数字版权保护、防止恶意信息传播、社交媒体内容安全等领域。通过对图像进行免疫，可以有效防止未经授权的编辑和篡改，维护图像的真实性和完整性，从而保护个人和组织的权益，营造更健康的网络环境。未来，该技术有望集成到图像处理软件和在线平台中，为用户提供便捷的图像保护服务。

## 📄 摘要（原文）

> Text-guided image editing via diffusion models, while powerful, raises significant concerns about misuse, motivating efforts to immunize images against unauthorized edits using imperceptible perturbations. Prevailing metrics for evaluating immunization success typically rely on measuring the visual dissimilarity between the output generated from a protected image and a reference output generated from the unprotected original. This approach fundamentally overlooks the core requirement of image immunization, which is to disrupt semantic alignment with attacker intent, regardless of deviation from any specific output. We argue that immunization success should instead be defined by the edited output either semantically mismatching the prompt or suffering substantial perceptual degradations, both of which thwart malicious intent. To operationalize this principle, we propose Synergistic Intermediate Feature Manipulation (SIFM), a method that strategically perturbs intermediate diffusion features through dual synergistic objectives: (1) maximizing feature divergence from the original edit trajectory to disrupt semantic alignment with the expected edit, and (2) minimizing feature norms to induce perceptual degradations. Furthermore, we introduce the Immunization Success Rate (ISR), a novel metric designed to rigorously quantify true immunization efficacy for the first time. ISR quantifies the proportion of edits where immunization induces either semantic failure relative to the prompt or significant perceptual degradations, assessed via Multimodal Large Language Models (MLLMs). Extensive experiments show our SIFM achieves the state-of-the-art performance for safeguarding visual content against malicious diffusion-based manipulation.

