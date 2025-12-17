---
layout: default
title: Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity
---

# Semantic Mismatch and Perceptual Degradation: A New Perspective on Image Editing Immunity

**arXiv**: [2512.14320v1](https://arxiv.org/abs/2512.14320) | [PDF](https://arxiv.org/pdf/2512.14320.pdf)

**作者**: Shuai Dong, Jie Zhang, Guoying Zhao, Shiguang Shan, Xilin Chen

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-12-16

**备注**: 11 pages, 4 figures

---

## 💡 一句话要点

**提出SIFM方法以解决图像免疫评估指标不准确的问题，通过语义失配和感知退化新视角保护图像免受恶意编辑。**

**关键词**: `图像免疫` `扩散模型` `语义失配` `感知退化` `特征扰动` `评估指标` `多模态大语言模型` `内容安全`

## 📋 核心要点

1. 现有图像免疫评估指标依赖视觉差异，忽略了破坏语义对齐的核心要求，导致评估不准确。
2. 提出SIFM方法，通过最大化特征差异和最小化特征范数，协同扰动扩散特征以实现语义失配和感知退化。
3. 实验显示SIFM在免疫成功率上达到最优，有效保护图像免受恶意编辑，验证了新视角的有效性。

## 📝 摘要（中文）

基于扩散模型的文本引导图像编辑虽然强大，但也引发了滥用担忧，促使人们使用不可察觉的扰动来免疫图像以防止未经授权的编辑。评估免疫成功的主流指标通常依赖于测量受保护图像生成的输出与未受保护原始图像生成的参考输出之间的视觉差异。这种方法从根本上忽视了图像免疫的核心要求，即破坏与攻击者意图的语义对齐，而不考虑与任何特定输出的偏差。我们认为，免疫成功应定义为编辑输出要么语义上与提示不匹配，要么遭受显著的感知退化，这两者都能阻止恶意意图。为实现这一原则，我们提出了协同中间特征操纵（SIFM），该方法通过双重协同目标策略性地扰动中间扩散特征：（1）最大化特征与原始编辑轨迹的差异，以破坏与预期编辑的语义对齐；（2）最小化特征范数以诱导感知退化。此外，我们引入了免疫成功率（ISR），这是一种新颖的指标，首次设计用于严格量化真实的免疫效果。ISR量化了免疫导致相对于提示的语义失败或显著感知退化的编辑比例，通过多模态大语言模型（MLLMs）进行评估。大量实验表明，我们的SIFM在保护视觉内容免受基于扩散的恶意操纵方面达到了最先进的性能。

## 🔬 方法详解

论文提出协同中间特征操纵（SIFM）作为核心方法，整体框架基于扩散模型，在中间特征层施加扰动。关键技术创新点包括：设计双重协同目标，一是最大化特征与原始编辑轨迹的差异以破坏语义对齐，二是最小化特征范数以诱导感知退化；同时引入免疫成功率（ISR）作为新评估指标，利用多模态大语言模型量化语义失败和感知退化。与现有方法的主要区别在于，SIFM从语义失配和感知退化新视角出发，直接针对攻击者意图进行免疫，而非依赖输出视觉差异，从而更准确地评估和实现免疫效果。

## 📊 实验亮点

SIFM在免疫成功率（ISR）上达到最先进性能，实验表明其能有效诱导语义失配和感知退化，显著提升图像免疫效果，验证了新评估指标和方法的优越性。

## 🎯 应用场景

该研究可应用于数字版权保护、社交媒体内容安全、新闻图像防篡改等领域，通过免疫技术防止恶意编辑，保障视觉内容的真实性和完整性，具有重要的实际价值。

## 📄 摘要（原文）

> Text-guided image editing via diffusion models, while powerful, raises significant concerns about misuse, motivating efforts to immunize images against unauthorized edits using imperceptible perturbations. Prevailing metrics for evaluating immunization success typically rely on measuring the visual dissimilarity between the output generated from a protected image and a reference output generated from the unprotected original. This approach fundamentally overlooks the core requirement of image immunization, which is to disrupt semantic alignment with attacker intent, regardless of deviation from any specific output. We argue that immunization success should instead be defined by the edited output either semantically mismatching the prompt or suffering substantial perceptual degradations, both of which thwart malicious intent. To operationalize this principle, we propose Synergistic Intermediate Feature Manipulation (SIFM), a method that strategically perturbs intermediate diffusion features through dual synergistic objectives: (1) maximizing feature divergence from the original edit trajectory to disrupt semantic alignment with the expected edit, and (2) minimizing feature norms to induce perceptual degradations. Furthermore, we introduce the Immunization Success Rate (ISR), a novel metric designed to rigorously quantify true immunization efficacy for the first time. ISR quantifies the proportion of edits where immunization induces either semantic failure relative to the prompt or significant perceptual degradations, assessed via Multimodal Large Language Models (MLLMs). Extensive experiments show our SIFM achieves the state-of-the-art performance for safeguarding visual content against malicious diffusion-based manipulation.

