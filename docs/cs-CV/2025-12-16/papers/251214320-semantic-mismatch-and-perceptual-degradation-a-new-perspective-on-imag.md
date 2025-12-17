---
layout: default
title: Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity
---

# Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.14320" class="toolbar-btn" target="_blank">📄 arXiv: 2512.14320</a>
  <a href="https://arxiv.org/pdf/2512.14320.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.14320" onclick="toggleFavorite(this, '2512.14320', 'Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuai Dong, Jie Zhang, Guoying Zhao, Shiguang Shan, Xilin Chen

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出SIFM，通过对抗扩散模型中间特征扰动实现图像编辑免疫，并提出ISR评估指标。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `图像编辑免疫` `扩散模型` `中间特征扰动` `语义错配` `感知退化` `免疫成功率` `多模态大语言模型` `恶意编辑防御`

## 📋 核心要点

1. 现有图像免疫方法仅关注视觉差异，忽略了语义对齐，无法有效阻止恶意编辑。
2. SIFM通过协同扰动扩散模型的中间特征，实现语义错配和感知退化，从而免疫恶意编辑。
3. 提出的ISR指标能更准确地评估免疫效果，实验证明SIFM优于现有方法，能有效防御恶意编辑。

## 📝 摘要（中文）

本文关注文本引导的图像编辑滥用问题，提出了一种新的图像免疫视角。现有免疫评估方法侧重于测量保护图像生成的输出与原始图像输出的视觉差异，忽略了免疫的核心需求：扰乱与攻击者意图的语义对齐。本文认为，免疫成功的关键在于编辑后的输出在语义上与提示不匹配，或遭受显著的感知退化，从而阻止恶意意图。为此，提出了协同中间特征操纵（SIFM）方法，通过双重协同目标策略性地扰动中间扩散特征：(1) 最大化与原始编辑轨迹的特征差异，以扰乱与预期编辑的语义对齐；(2) 最小化特征范数，以诱导感知退化。此外，引入了免疫成功率（ISR）这一新指标，旨在严格量化真正的免疫效果。ISR量化了免疫诱导语义失败或显著感知退化的编辑比例，并通过多模态大型语言模型（MLLM）进行评估。大量实验表明，SIFM在保护视觉内容免受基于扩散的恶意操纵方面实现了最先进的性能。

## 🔬 方法详解

**问题定义**：现有图像免疫方法主要通过在图像中添加不易察觉的扰动，使得通过扩散模型编辑后的图像与原始图像的编辑结果在视觉上产生差异。然而，这种方法忽略了图像免疫的根本目标：阻止攻击者通过文本提示实现其恶意编辑意图。即使编辑后的图像与原始图像的编辑结果存在视觉差异，如果仍然能够满足攻击者的语义意图，则免疫仍然是失败的。因此，需要一种能够有效阻止图像按照恶意文本提示进行编辑的方法。

**核心思路**：本文的核心思路是通过在扩散模型的中间特征空间中引入扰动，使得编辑后的图像要么在语义上与文本提示不匹配，要么在感知上出现显著的退化。这种方法旨在从根本上破坏攻击者利用扩散模型进行恶意编辑的能力。通过同时优化语义错配和感知退化，可以更有效地实现图像免疫。

**技术框架**：SIFM (Synergistic Intermediate Feature Manipulation) 方法主要包含以下几个步骤：1) 选择扩散模型的中间层特征；2) 设计双重协同目标函数，包括最大化特征差异和最小化特征范数；3) 通过优化目标函数，生成扰动后的中间特征；4) 将扰动后的中间特征输入扩散模型，生成免疫后的图像。此外，本文还提出了一个新的评估指标 ISR (Immunization Success Rate)，用于量化免疫的成功率。ISR 通过 MLLM (Multimodal Large Language Models) 来评估编辑后的图像是否在语义上与文本提示匹配，以及感知质量是否显著下降。

**关键创新**：本文的关键创新在于：1) 提出了基于语义错配和感知退化的图像免疫新视角；2) 设计了协同中间特征操纵（SIFM）方法，通过双重协同目标函数，同时优化语义错配和感知退化；3) 提出了免疫成功率（ISR）这一新指标，能够更准确地评估图像免疫的效果。与现有方法相比，SIFM 能够更有效地阻止恶意编辑，并且 ISR 能够更准确地反映免疫的真实效果。

**关键设计**：SIFM 的关键设计包括：1) 中间特征的选择：选择扩散模型中间层的特征，可以在保证图像质量的同时，有效地影响编辑结果；2) 双重协同目标函数：最大化特征差异的目标函数旨在破坏语义对齐，最小化特征范数的目标函数旨在诱导感知退化；3) 扰动强度的控制：通过调整目标函数的权重，可以控制扰动的强度，从而在免疫效果和图像质量之间取得平衡；4) ISR 的计算：通过 MLLM 评估编辑后的图像是否在语义上与文本提示匹配，以及感知质量是否显著下降，从而计算 ISR。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14320/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14320/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.14320/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，SIFM 方法在图像免疫方面取得了显著的性能提升。与现有方法相比，SIFM 能够更有效地阻止恶意编辑，并且提出的 ISR 指标能够更准确地反映免疫的真实效果。具体来说，SIFM 在 ISR 指标上优于现有方法，表明其能够更有效地诱导语义失败或显著的感知退化。

## 🎯 应用场景

该研究成果可应用于数字版权保护、社交媒体内容安全、新闻真实性验证等领域。通过对图像进行免疫处理，可以有效防止未经授权的恶意编辑和篡改，维护图像内容的完整性和真实性，从而保护个人和组织的合法权益，并减少虚假信息的传播。

## 📄 摘要（原文）

> Text-guided image editing via diffusion models, while powerful, raises significant concerns about misuse, motivating efforts to immunize images against unauthorized edits using imperceptible perturbations. Prevailing metrics for evaluating immunization success typically rely on measuring the visual dissimilarity between the output generated from a protected image and a reference output generated from the unprotected original. This approach fundamentally overlooks the core requirement of image immunization, which is to disrupt semantic alignment with attacker intent, regardless of deviation from any specific output. We argue that immunization success should instead be defined by the edited output either semantically mismatching the prompt or suffering substantial perceptual degradations, both of which thwart malicious intent. To operationalize this principle, we propose Synergistic Intermediate Feature Manipulation (SIFM), a method that strategically perturbs intermediate diffusion features through dual synergistic objectives: (1) maximizing feature divergence from the original edit trajectory to disrupt semantic alignment with the expected edit, and (2) minimizing feature norms to induce perceptual degradations. Furthermore, we introduce the Immunization Success Rate (ISR), a novel metric designed to rigorously quantify true immunization efficacy for the first time. ISR quantifies the proportion of edits where immunization induces either semantic failure relative to the prompt or significant perceptual degradations, assessed via Multimodal Large Language Models (MLLMs). Extensive experiments show our SIFM achieves the state-of-the-art performance for safeguarding visual content against malicious diffusion-based manipulation.

