---
layout: default
title: DIR-TIR: Dialog-Iterative Refinement for Text-to-Image Retrieval
---

# DIR-TIR: Dialog-Iterative Refinement for Text-to-Image Retrieval

**arXiv**: [2511.14449v1](https://arxiv.org/abs/2511.14449) | [PDF](https://arxiv.org/pdf/2511.14449.pdf)

**作者**: Zongwei Zhen, Biqing Zeng

---

## 💡 一句话要点

**提出DIR-TIR框架，通过对话迭代优化解决交互式文本到图像检索问题**

**关键词**: `文本到图像检索` `对话系统` `迭代精炼` `视觉语义对齐` `交互式检索`

## 📋 核心要点

1. 核心问题：传统单查询方法在交互式文本到图像检索中缺乏可控性和容错性
2. 方法要点：结合对话精炼和图像精炼模块，通过多轮对话逐步提取信息并减少视觉语义差异
3. 实验或效果：在多个数据集上显著超越仅使用初始描述的基线，提高检索精度和交互体验

## 📄 摘要（原文）

> This paper addresses the task of interactive, conversational text-to-image retrieval.
>   Our DIR-TIR framework progressively refines the target image search through two specialized modules: the Dialog Refiner Module and the Image Refiner Module.
>   The Dialog Refiner actively queries users to extract essential information and generate increasingly precise descriptions of the target image.
>   Complementarily, the Image Refiner identifies perceptual gaps between generated images and user intentions, strategically reducing the visual-semantic discrepancy. By leveraging multi-turn dialogues, DIR-TIR provides superior controllability and fault tolerance compared to conventional single-query methods, significantly improving target image hit accuracy.
>   Comprehensive experiments across diverse image datasets demonstrate our dialogue-based approach substantially outperforms initial-description-only baselines, while the synergistic module integration achieves both higher retrieval precision and enhanced interactive experience.

