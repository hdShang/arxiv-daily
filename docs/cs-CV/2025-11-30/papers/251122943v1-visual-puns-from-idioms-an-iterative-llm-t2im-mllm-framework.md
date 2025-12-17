---
layout: default
title: Visual Puns from Idioms: An Iterative LLM-T2IM-MLLM Framework
---

# Visual Puns from Idioms: An Iterative LLM-T2IM-MLLM Framework

**arXiv**: [2511.22943v1](https://arxiv.org/abs/2511.22943) | [PDF](https://arxiv.org/pdf/2511.22943.pdf)

**作者**: Kelaiti Xiao, Liang Yang, Dongyu Zhang, Paerhati Tulajiang, Hongfei Lin

---

## 💡 一句话要点

**提出迭代LLM-T2IM-MLLM框架以自动生成和评估基于习语的视觉双关图像。**

**关键词**: `视觉双关` `多模态生成` `迭代框架` `习语理解` `自动评估`

## 📋 核心要点

1. 研究基于习语的视觉双关图像，结合字面与比喻意义。
2. 开发迭代框架，协调LLM、T2IM和MLLM进行生成与评估。
3. 实验使用1,000个习语，评估10个LLM、10个MLLM和一个T2IM的性能。

## 📄 摘要（原文）

> We study idiom-based visual puns--images that align an idiom's literal and figurative meanings--and present an iterative framework that coordinates a large language model (LLM), a text-to-image model (T2IM), and a multimodal LLM (MLLM) for automatic generation and evaluation. Given an idiom, the system iteratively (i) generates detailed visual prompts, (ii) synthesizes an image, (iii) infers the idiom from the image, and (iv) refines the prompt until recognition succeeds or a step limit is reached. Using 1,000 idioms as inputs, we synthesize a corresponding dataset of visual pun images with paired prompts, enabling benchmarking of both generation and understanding. Experiments across 10 LLMs, 10 MLLMs, and one T2IM (Qwen-Image) show that MLLM choice is the primary performance driver: GPT achieves the highest accuracies, Gemini follows, and the best open-source MLLM (Gemma) is competitive with some closed models. On the LLM side, Claude attains the strongest average performance for prompt generation.

