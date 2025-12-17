---
layout: default
title: Dual Attention Guided Defense Against Malicious Edits
---

# Dual Attention Guided Defense Against Malicious Edits

**arXiv**: [2512.14333v1](https://arxiv.org/abs/2512.14333) | [PDF](https://arxiv.org/pdf/2512.14333.pdf)

**作者**: Jie Zhang, Shuai Dong, Shiguang Shan, Xilin Chen

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-12-16

**备注**: 11 pages, 7 figures

---

## 💡 一句话要点

**提出双注意力引导噪声扰动免疫方法，以防御文本到图像扩散模型中的恶意编辑风险。**

**关键词**: `文本到图像扩散模型` `恶意编辑防御` `注意力机制` `噪声扰动` `语义理解干扰` `图像安全` `伦理挑战` `动态阈值`

## 📋 核心要点

1. 现有防御方法依赖不可感知扰动，但对抗恶意篡改效果有限，面临语义理解干扰不足的挑战。
2. 提出DANP方法，通过动态阈值生成掩码，操纵交叉注意力和噪声预测，误导编辑并保护目标区域。
3. 实验显示DANP在防御恶意编辑方面达到最先进性能，有效提升免疫力和生成干扰能力。

## 📝 摘要（中文）

文本到图像扩散模型的进展通过文本提示改变了图像编辑方式，但也带来了因潜在滥用创建欺骗性或有害内容而引发的重大伦理挑战。现有防御方法试图通过嵌入不可感知的扰动来降低风险，但其在对抗恶意篡改方面的有效性有限。为解决此问题，我们提出了一种双注意力引导噪声扰动免疫方法，该方法添加不可感知的扰动以破坏模型的语义理解和生成过程。DANP在多个时间步上操作，通过动态阈值生成掩码来识别文本相关和不相关区域，从而操纵交叉注意力图和噪声预测过程。它减少相关区域的注意力，同时增加不相关区域的注意力，从而误导编辑朝向错误区域并保护目标内容。此外，我们的方法最大化注入噪声与模型预测噪声之间的差异，以进一步干扰生成。通过同时针对注意力和噪声预测机制，DANP展现出对恶意编辑的显著免疫力，大量实验证实我们的方法实现了最先进的性能。

## 🔬 方法详解

DANP的整体框架基于文本到图像扩散模型，在多个时间步上添加不可感知噪声扰动。关键技术创新包括：使用动态阈值生成掩码来区分文本相关和不相关区域，从而精确操纵交叉注意力图；同时，通过最大化注入噪声与模型预测噪声的差异，干扰噪声预测过程。与现有方法的主要区别在于，DANP同时针对注意力和噪声预测两个核心机制，实现更全面的防御，而传统方法通常仅关注单一扰动或静态策略。

## 📊 实验亮点

DANP在防御恶意编辑方面实现最先进性能，通过双注意力引导和噪声扰动，显著提升免疫力，实验证实其有效误导编辑并保护目标，性能优于现有方法。

## 🎯 应用场景

该研究可应用于图像安全领域，如防止恶意编辑用于虚假新闻、深度伪造或有害内容生成，提升数字媒体的可信度和伦理合规性，具有实际价值于社交媒体、新闻审核和内容创作平台。

## 📄 摘要（原文）

> Recent progress in text-to-image diffusion models has transformed image editing via text prompts, yet this also introduces significant ethical challenges from potential misuse in creating deceptive or harmful content. While current defenses seek to mitigate this risk by embedding imperceptible perturbations, their effectiveness is limited against malicious tampering. To address this issue, we propose a Dual Attention-Guided Noise Perturbation (DANP) immunization method that adds imperceptible perturbations to disrupt the model's semantic understanding and generation process. DANP functions over multiple timesteps to manipulate both cross-attention maps and the noise prediction process, using a dynamic threshold to generate masks that identify text-relevant and irrelevant regions. It then reduces attention in relevant areas while increasing it in irrelevant ones, thereby misguides the edit towards incorrect regions and preserves the intended targets. Additionally, our method maximizes the discrepancy between the injected noise and the model's predicted noise to further interfere with the generation. By targeting both attention and noise prediction mechanisms, DANP exhibits impressive immunity against malicious edits, and extensive experiments confirm that our method achieves state-of-the-art performance.

