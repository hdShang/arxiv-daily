---
layout: default
title: Guiding What Not to Generate: Automated Negative Prompting for Text-Image Alignment
---

# Guiding What Not to Generate: Automated Negative Prompting for Text-Image Alignment

**arXiv**: [2512.07702v1](https://arxiv.org/abs/2512.07702) | [PDF](https://arxiv.org/pdf/2512.07702.pdf)

**作者**: Sangha Park, Eunji Kim, Yeongtak Oh, Jooyoung Choi, Sungroh Yoon

---

## 💡 一句话要点

**提出自动化负提示方法NPC以提升扩散模型中文本-图像对齐精度**

**关键词**: `文本到图像生成` `负提示` `扩散模型` `文本-图像对齐` `自动化校正`

## 📋 核心要点

1. 核心问题：文本到图像生成中，复杂或想象性提示的文本-图像对齐仍具挑战性
2. 方法要点：通过分析交叉注意力模式，自动识别并应用负提示来抑制不期望内容
3. 实验或效果：在GenEval++和Imagine-Bench上优于基线，实现更强对齐

## 📄 摘要（原文）

> Despite substantial progress in text-to-image generation, achieving precise text-image alignment remains challenging, particularly for prompts with rich compositional structure or imaginative elements. To address this, we introduce Negative Prompting for Image Correction (NPC), an automated pipeline that improves alignment by identifying and applying negative prompts that suppress unintended content. We begin by analyzing cross-attention patterns to explain why both targeted negatives-those directly tied to the prompt's alignment error-and untargeted negatives-tokens unrelated to the prompt but present in the generated image-can enhance alignment. To discover useful negatives, NPC generates candidate prompts using a verifier-captioner-proposer framework and ranks them with a salient text-space score, enabling effective selection without requiring additional image synthesis. On GenEval++ and Imagine-Bench, NPC outperforms strong baselines, achieving 0.571 vs. 0.371 on GenEval++ and the best overall performance on Imagine-Bench. By guiding what not to generate, NPC provides a principled, fully automated route to stronger text-image alignment in diffusion models. Code is released at https://github.com/wiarae/NPC.

