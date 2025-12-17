---
layout: default
title: RECODE: Reasoning Through Code Generation for Visual Question Answering
---

# RECODE: Reasoning Through Code Generation for Visual Question Answering

**arXiv**: [2510.13756v1](https://arxiv.org/abs/2510.13756) | [PDF](https://arxiv.org/pdf/2510.13756.pdf)

**作者**: Junhong Shen, Mu Cai, Bo Hu, Ameet Talwalkar, David A Ross, Cordelia Schmid, Alireza Fathi

---

## 💡 一句话要点

**提出RECODE框架，通过代码生成解决多模态大模型在图表推理中的验证问题**

**关键词**: `视觉问答` `代码生成` `反渲染` `多模态推理` `可验证推理` `结构化视觉`

## 📋 核心要点

1. 多模态大模型在图表等结构化视觉推理中缺乏验证机制，导致精确推理困难
2. RECODE框架通过反渲染生成候选代码，并迭代优化以选择最忠实重构
3. 在CharXiv等基准上，RECODE显著优于不利用代码或仅用于辅助的方法

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) struggle with precise reasoning for
> structured visuals like charts and diagrams, as pixel-based perception lacks a
> mechanism for verification. To address this, we propose to leverage derendering
> -- the process of reverse-engineering visuals into executable code -- as a new
> modality for verifiable visual reasoning. Specifically, we propose RECODE, an
> agentic framework that first generates multiple candidate programs to reproduce
> the input image. It then uses a critic to select the most faithful
> reconstruction and iteratively refines the code. This process not only
> transforms an ambiguous perceptual task into a verifiable, symbolic problem,
> but also enables precise calculations and logical inferences later on. On
> various visual reasoning benchmarks such as CharXiv, ChartQA, and Geometry3K,
> RECODE significantly outperforms methods that do not leverage code or only use
> code for drawing auxiliary lines or cropping. Our work demonstrates that
> grounding visual perception in executable code provides a new path toward more
> accurate and verifiable multimodal reasoning.

