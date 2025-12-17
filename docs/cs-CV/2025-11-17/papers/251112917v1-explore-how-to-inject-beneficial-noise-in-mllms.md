---
layout: default
title: Explore How to Inject Beneficial Noise in MLLMs
---

# Explore How to Inject Beneficial Noise in MLLMs

**arXiv**: [2511.12917v1](https://arxiv.org/abs/2511.12917) | [PDF](https://arxiv.org/pdf/2511.12917.pdf)

**作者**: Ruishu Zhu, Sida Huang, Ziheng Jiao, Hongyuan Zhang

---

## 💡 一句话要点

**提出多模态噪声生成器以优化MLLMs跨模态对齐，实现高效微调**

**关键词**: `多模态大语言模型` `噪声注入` `跨模态对齐` `高效微调` `变分推理`

## 📋 核心要点

1. 核心问题：现有MLLMs微调方法忽略跨模态异构性，限制性能提升
2. 方法要点：基于变分推理设计噪声生成器，动态分析跨模态关系注入有益噪声
3. 实验或效果：在QwenVL和LLaVA上超越全参数微调，仅需1~2%额外参数

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have played an increasingly important role in multimodal intelligence. However, the existing fine-tuning methods often ignore cross-modal heterogeneity, limiting their full potential. In this work, we propose a novel fine-tuning strategy by injecting beneficial random noise, which outperforms previous methods and even surpasses full fine-tuning, with minimal additional parameters. The proposed Multimodal Noise Generator (MuNG) enables efficient modality fine-tuning by injecting customized noise into the frozen MLLMs. Specifically, we reformulate the reasoning process of MLLMs from a variational inference perspective, upon which we design a multimodal noise generator that dynamically analyzes cross-modal relationships in image-text pairs to generate task-adaptive beneficial noise. Injecting this type of noise into the MLLMs effectively suppresses irrelevant semantic components, leading to significantly improved cross-modal representation alignment and enhanced performance on downstream tasks. Experiments on two mainstream MLLMs, QwenVL and LLaVA, demonstrate that our method surpasses full-parameter fine-tuning and other existing fine-tuning approaches, while requiring adjustments to only about $1\sim2\%$ additional parameters. The relevant code is uploaded in the supplementary.

