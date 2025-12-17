---
layout: default
title: Towards Transferable Defense Against Malicious Image Edits
---

# Towards Transferable Defense Against Malicious Image Edits

**arXiv**: [2512.14341v1](https://arxiv.org/abs/2512.14341) | [PDF](https://arxiv.org/pdf/2512.14341.pdf)

**作者**: Jie Zhang, Shuai Dong, Shiguang Shan, Xilin Chen

**分类**: cs.CV, cs.AI, cs.CY, cs.LG

**发布日期**: 2025-12-16

**备注**: 14 pages, 5 figures

---

## 💡 一句话要点

**提出TDAE框架以解决恶意图像编辑防御中跨模型可迁移性不足的问题。**

**关键词**: `恶意图像编辑防御` `跨模型可迁移性` `双模态优化` `梯度正则化` `动态提示防御` `扩散模型` `图像免疫力` `对抗攻击`

## 📋 核心要点

1. 现有方法在对抗恶意图像编辑时，跨模型可迁移性有限，难以泛化到未见编辑模型。
2. 提出TDAE框架，结合FDM的梯度正则化和DPD的动态文本优化，通过双模态协调增强免疫鲁棒性。
3. 实验显示TDAE在内部和跨模型评估中均实现最优性能，显著提升防御效果和可迁移性。

## 📝 摘要（中文）

近期研究表明，在输入图像中添加不可感知的扰动，在对抗基于扩散模型的恶意图像编辑系统方面展现出潜力，但现有方法在跨模型评估中可迁移性有限。为此，我们提出可迁移防御恶意图像编辑（TDAE），一种新颖的双模态框架，通过协调图像-文本优化增强图像对恶意编辑的免疫力。具体而言，在视觉防御层面，我们引入FlatGrad防御机制（FDM），将梯度正则化融入对抗目标，通过显式引导扰动朝向平坦最小值，增强对未见编辑模型的免疫鲁棒性。在文本增强保护方面，我们提出动态提示防御（DPD）的对抗优化范式，周期性优化文本嵌入，使免疫化图像的编辑结果与原始图像对齐，然后在优化嵌入下更新图像。通过对多样化嵌入的迭代对抗更新，DPD强制生成免疫化图像，寻求更广泛的免疫增强特征集，从而实现跨模型可迁移性。大量实验结果表明，我们的TDAE在内部和跨模型评估中，在减轻恶意编辑方面均达到最先进性能。

## 🔬 方法详解

TDAE是一个双模态框架，通过图像-文本协调优化增强图像免疫力。整体框架包括视觉防御和文本增强保护两部分：FDM在图像层面引入梯度正则化，引导扰动朝向平坦最小值以提升鲁棒性；DPD在文本层面动态优化嵌入，通过迭代对抗更新使免疫化图像与原始图像编辑结果对齐。关键创新在于结合平坦最小值和动态文本优化，与现有方法相比，TDAE强调跨模型可迁移性，通过双模态交互实现更广泛的免疫特征学习。

## 📊 实验亮点

TDAE在内部和跨模型评估中均达到最先进性能，实验表明其能有效减轻恶意编辑，显著提升防御可迁移性，验证了双模态优化的有效性。

## 🎯 应用场景

该研究可应用于图像安全领域，如保护社交媒体、数字媒体内容免受恶意篡改，增强AI生成内容的可信度，适用于版权保护、身份验证和内容审核等场景。

## 📄 摘要（原文）

> Recent approaches employing imperceptible perturbations in input images have demonstrated promising potential to counter malicious manipulations in diffusion-based image editing systems. However, existing methods suffer from limited transferability in cross-model evaluations. To address this, we propose Transferable Defense Against Malicious Image Edits (TDAE), a novel bimodal framework that enhances image immunity against malicious edits through coordinated image-text optimization. Specifically, at the visual defense level, we introduce FlatGrad Defense Mechanism (FDM), which incorporates gradient regularization into the adversarial objective. By explicitly steering the perturbations toward flat minima, FDM amplifies immune robustness against unseen editing models. For textual enhancement protection, we propose an adversarial optimization paradigm named Dynamic Prompt Defense (DPD), which periodically refines text embeddings to align the editing outcomes of immunized images with those of the original images, then updates the images under optimized embeddings. Through iterative adversarial updates to diverse embeddings, DPD enforces the generation of immunized images that seek a broader set of immunity-enhancing features, thereby achieving cross-model transferability. Extensive experimental results demonstrate that our TDAE achieves state-of-the-art performance in mitigating malicious edits under both intra- and cross-model evaluations.

