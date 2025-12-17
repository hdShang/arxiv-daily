---
layout: default
title: ARC Is a Vision Problem!
---

# ARC Is a Vision Problem!

**arXiv**: [2511.14761v1](https://arxiv.org/abs/2511.14761) | [PDF](https://arxiv.org/pdf/2511.14761.pdf)

**作者**: Keya Hu, Ali Cy, Linlu Qiu, Xiaoman Delores Ding, Runqian Wang, Yeyin Eva Zhu, Jacob Andreas, Kaiming He

---

## 💡 一句话要点

**提出视觉ARC框架，将抽象推理视为图像翻译问题。**

**关键词**: `抽象推理` `图像翻译` `Vision Transformer` `测试时训练` `视觉先验`

## 📋 核心要点

1. 核心问题：ARC作为抽象推理任务，常被语言模型处理，但本质是视觉问题。
2. 方法要点：使用画布表示输入，应用Vision Transformer进行图像到图像映射。
3. 实验效果：在ARC-1基准上达到60.4%准确率，优于同类从头训练方法。

## 📄 摘要（原文）

> The Abstraction and Reasoning Corpus (ARC) is designed to promote research on abstract reasoning, a fundamental aspect of human intelligence. Common approaches to ARC treat it as a language-oriented problem, addressed by large language models (LLMs) or recurrent reasoning models. However, although the puzzle-like tasks in ARC are inherently visual, existing research has rarely approached the problem from a vision-centric perspective. In this work, we formulate ARC within a vision paradigm, framing it as an image-to-image translation problem. To incorporate visual priors, we represent the inputs on a "canvas" that can be processed like natural images. It is then natural for us to apply standard vision architectures, such as a vanilla Vision Transformer (ViT), to perform image-to-image mapping. Our model is trained from scratch solely on ARC data and generalizes to unseen tasks through test-time training. Our framework, termed Vision ARC (VARC), achieves 60.4% accuracy on the ARC-1 benchmark, substantially outperforming existing methods that are also trained from scratch. Our results are competitive with those of leading LLMs and close the gap to average human performance.

