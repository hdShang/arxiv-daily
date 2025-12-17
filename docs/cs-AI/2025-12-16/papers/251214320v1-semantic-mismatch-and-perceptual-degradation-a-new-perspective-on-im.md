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

**提出SIFM方法以解决图像免疫评估不准确的问题，通过语义失配和感知退化新视角保护图像免受恶意编辑。**

🎯 **匹配领域**: **强化学习**

**关键词**: `图像免疫` `扩散模型` `语义对齐` `特征扰动` `多模态评估` `内容保护` `恶意编辑防御`

## 📋 核心要点

1. 现有图像免疫评估方法依赖视觉差异度量，忽视了破坏语义对齐的核心要求，导致评估不准确。
2. 论文提出SIFM方法，通过最大化特征差异和最小化特征范数双重目标，协同扰动扩散中间特征。
3. 实验显示SIFM在免疫成功率上达到最先进水平，有效保护图像免受恶意编辑，验证了新视角的有效性。

## 📝 摘要（中文）

基于扩散模型的文本引导图像编辑虽然强大，但也引发了严重的滥用担忧，促使人们使用不可察觉的扰动来免疫图像以防止未经授权的编辑。评估免疫成功的主流指标通常依赖于测量受保护图像生成的输出与未受保护原始图像生成的参考输出之间的视觉差异。这种方法从根本上忽视了图像免疫的核心要求，即破坏与攻击者意图的语义对齐，而不考虑与任何特定输出的偏差。我们认为，免疫成功应定义为编辑输出要么语义上与提示不匹配，要么遭受显著的感知退化，这两者都能阻止恶意意图。为了实现这一原则，我们提出了协同中间特征操纵（SIFM），这是一种通过双重协同目标策略性地扰动扩散中间特征的方法：（1）最大化特征与原始编辑轨迹的差异，以破坏与预期编辑的语义对齐；（2）最小化特征范数以诱导感知退化。此外，我们引入了免疫成功率（ISR），这是一种新颖的指标，首次设计用于严格量化真实的免疫效果。ISR量化了免疫导致编辑输出相对于提示语义失败或显著感知退化的比例，通过多模态大语言模型（MLLMs）进行评估。大量实验表明，我们的SIFM在保护视觉内容免受基于扩散的恶意操纵方面达到了最先进的性能。

## 🔬 方法详解

**问题定义**：论文要解决的具体问题是文本引导扩散模型图像编辑的滥用风险，现有免疫评估方法依赖视觉差异度量，忽视了破坏语义对齐的核心要求，导致评估不准确，无法有效量化免疫效果。

**核心思路**：论文的核心解决思路是重新定义免疫成功为编辑输出语义失配或感知退化，并提出SIFM方法，通过双重协同目标策略性地扰动扩散中间特征，以同时破坏语义对齐和诱导感知退化，从而更全面地阻止恶意编辑。

**技术框架**：整体架构包括两个主要阶段：首先，在扩散过程中提取中间特征；其次，应用SIFM方法，通过最大化特征差异目标（如使用距离度量）和最小化特征范数目标（如L2范数），协同优化扰动，生成免疫图像。评估时使用ISR指标，结合MLLMs判断语义匹配和感知质量。

**关键创新**：最重要的技术创新点是提出了基于语义失配和感知退化的新免疫视角，以及SIFM方法中的双重协同目标设计，与现有方法本质区别在于从输出偏差转向意图破坏，更符合实际免疫需求。

**关键设计**：关键设计包括：使用扩散模型的中间特征作为扰动对象；设计损失函数结合特征差异最大化（如余弦相似度损失）和特征范数最小化（如正则化项）；参数设置可能涉及扰动强度、优化步数；网络结构依赖于预训练扩散模型，无需额外训练。

## 📊 实验亮点

实验表明，SIFM在免疫成功率（ISR）上达到最先进水平，具体数据未知，但通过对比基线方法（如基于视觉差异的免疫技术），在多个数据集和编辑任务中显著提升免疫效果，有效诱导语义失配和感知退化，验证了新评估指标的有效性。

## 🎯 应用场景

该研究在数字内容保护、隐私安全和版权管理等领域具有潜在应用价值，可用于保护个人照片、艺术作品或敏感图像免受AI驱动的恶意编辑，如深度伪造或未经授权的修改。未来可能推动更鲁棒的免疫技术发展，增强视觉数据的真实性和可信度。

## 📄 摘要（原文）

> Text-guided image editing via diffusion models, while powerful, raises significant concerns about misuse, motivating efforts to immunize images against unauthorized edits using imperceptible perturbations. Prevailing metrics for evaluating immunization success typically rely on measuring the visual dissimilarity between the output generated from a protected image and a reference output generated from the unprotected original. This approach fundamentally overlooks the core requirement of image immunization, which is to disrupt semantic alignment with attacker intent, regardless of deviation from any specific output. We argue that immunization success should instead be defined by the edited output either semantically mismatching the prompt or suffering substantial perceptual degradations, both of which thwart malicious intent. To operationalize this principle, we propose Synergistic Intermediate Feature Manipulation (SIFM), a method that strategically perturbs intermediate diffusion features through dual synergistic objectives: (1) maximizing feature divergence from the original edit trajectory to disrupt semantic alignment with the expected edit, and (2) minimizing feature norms to induce perceptual degradations. Furthermore, we introduce the Immunization Success Rate (ISR), a novel metric designed to rigorously quantify true immunization efficacy for the first time. ISR quantifies the proportion of edits where immunization induces either semantic failure relative to the prompt or significant perceptual degradations, assessed via Multimodal Large Language Models (MLLMs). Extensive experiments show our SIFM achieves the state-of-the-art performance for safeguarding visual content against malicious diffusion-based manipulation.

