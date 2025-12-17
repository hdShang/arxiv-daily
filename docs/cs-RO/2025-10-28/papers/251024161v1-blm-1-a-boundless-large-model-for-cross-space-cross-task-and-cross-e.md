---
layout: default
title: BLM$_1$: A Boundless Large Model for Cross-Space, Cross-Task, and Cross-Embodiment Learning
---

# BLM$_1$: A Boundless Large Model for Cross-Space, Cross-Task, and Cross-Embodiment Learning

**arXiv**: [2510.24161v1](https://arxiv.org/abs/2510.24161) | [PDF](https://arxiv.org/pdf/2510.24161.pdf)

**作者**: Wentao Tan, Bowen Wang, Heng Zhi, Chenyu Liu, Zhe Li, Jian Liu, Zengrong Lin, Yukun Dai, Yipeng Chen, Wenjie Yang, Enci Xie, Hao Xue, Baixu Ji, Chen Xu, Zhibin Wang, Tianshi Wang, Lei Zhu, Heng Tao Shen

---

## 💡 一句话要点

**提出BLM$_1$模型以实现跨空间、跨任务和跨具身的统一学习**

**关键词**: `多模态大语言模型` `跨空间学习` `跨任务学习` `跨具身泛化` `两阶段训练` `意图桥接接口`

## 📋 核心要点

1. 核心问题：现有MLLMs在数字-物理空间和具身间泛化能力差，缺乏统一模型。
2. 方法要点：采用两阶段训练，注入具身知识并构建意图桥接接口指导控制。
3. 实验或效果：在数字和物理基准测试中，BLM$_1$优于多类模型，性能提升约6%和3%。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have advanced vision-language
> reasoning and are increasingly deployed in embodied agents. However,
> significant limitations remain: MLLMs generalize poorly across digital-physical
> spaces and embodiments; vision-language-action models (VLAs) produce low-level
> actions yet lack robust high-level embodied reasoning; and most embodied large
> language models (ELLMs) are constrained to digital-space with poor
> generalization to the physical world. Thus, unified models that operate
> seamlessly across digital and physical spaces while generalizing across
> embodiments and tasks remain absent. We introduce the \textbf{Boundless Large
> Model (BLM$_1$)}, a multimodal spatial foundation model that preserves
> instruction following and reasoning, incorporates embodied knowledge, and
> supports robust cross-embodiment control. BLM$_1$ integrates three key
> capabilities -- \textit{cross-space transfer, cross-task learning, and
> cross-embodiment generalization} -- via a two-stage training paradigm. Stage I
> injects embodied knowledge into the MLLM through curated digital corpora while
> maintaining language competence. Stage II trains a policy module through an
> intent-bridging interface that extracts high-level semantics from the MLLM to
> guide control, without fine-tuning the MLLM backbone. This process is supported
> by a self-collected cross-embodiment demonstration suite spanning four robot
> embodiments and six progressively challenging tasks. Evaluations across digital
> and physical benchmarks show that a single BLM$_1$ instance outperforms four
> model families -- MLLMs, ELLMs, VLAs, and GMLMs -- achieving
> $\sim\!\textbf{6%}$ gains in digital tasks and $\sim\!\textbf{3%}$ in physical
> tasks.

