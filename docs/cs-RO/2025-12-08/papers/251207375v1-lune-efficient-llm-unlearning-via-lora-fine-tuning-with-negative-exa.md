---
layout: default
title: LUNE: Efficient LLM Unlearning via LoRA Fine-Tuning with Negative Examples
---

# LUNE: Efficient LLM Unlearning via LoRA Fine-Tuning with Negative Examples

**arXiv**: [2512.07375v1](https://arxiv.org/abs/2512.07375) | [PDF](https://arxiv.org/pdf/2512.07375.pdf)

**作者**: Yezi Liu, Hanning Chen, Wenjun Huang, Yang Ni, Mohsen Imani

---

## 💡 一句话要点

**提出LUNE框架，通过LoRA微调与负例实现高效LLM遗忘，以解决隐私、偏见和知识修正问题。**

**关键词**: `大语言模型遗忘` `LoRA微调` `负例学习` `计算效率` `隐私保护` `知识修正`

## 📋 核心要点

1. 核心问题：LLM难以移除特定信息，传统遗忘方法计算成本高，不适用于实际部署。
2. 方法要点：基于LoRA的轻量级框架，仅更新低秩适配器，冻结主干，通过负例进行遗忘，定位编辑并避免全局变化。
3. 实验或效果：在多项事实遗忘任务中，效果与全微调和记忆编辑方法相当，计算成本降低约一个数量级。

## 📄 摘要（原文）

> Large language models (LLMs) possess vast knowledge acquired from extensive training corpora, but they often cannot remove specific pieces of information when needed, which makes it hard to handle privacy, bias mitigation, and knowledge correction. Traditional model unlearning approaches require computationally expensive fine-tuning or direct weight editing, making them impractical for real-world deployment. In this work, we introduce LoRA-based Unlearning with Negative Examples (LUNE), a lightweight framework that performs negative-only unlearning by updating only low-rank adapters while freezing the backbone, thereby localizing edits and avoiding disruptive global changes. Leveraging Low-Rank Adaptation (LoRA), LUNE targets intermediate representations to suppress (or replace) requested knowledge with an order-of-magnitude lower compute and memory than full fine-tuning or direct weight editing. Extensive experiments on multiple factual unlearning tasks show that LUNE: (I) achieves effectiveness comparable to full fine-tuning and memory-editing methods, and (II) reduces computational cost by about an order of magnitude.

