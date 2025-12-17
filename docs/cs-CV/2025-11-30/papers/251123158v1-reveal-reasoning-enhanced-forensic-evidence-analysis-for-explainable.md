---
layout: default
title: REVEAL: Reasoning-enhanced Forensic Evidence Analysis for Explainable AI-generated Image Detection
---

# REVEAL: Reasoning-enhanced Forensic Evidence Analysis for Explainable AI-generated Image Detection

**arXiv**: [2511.23158v1](https://arxiv.org/abs/2511.23158) | [PDF](https://arxiv.org/pdf/2511.23158.pdf)

**作者**: Huangsen Cao, Qin Mei, Zhiheng Li, Yuxi Li, Ying Zhang, Chen Li, Zhimeng Zhang, Xin Ding, Yongwei Wang, Jing Lyu, Fei Wu

---

## 💡 一句话要点

**提出REVEAL框架以解决AI生成图像检测中解释性不足和泛化能力差的问题**

**关键词**: `AI生成图像检测` `解释性人工智能` `证据链推理` `强化学习` `多模态基准` `图像取证`

## 📋 核心要点

1. 核心问题：现有AI生成图像检测方法依赖表面模式匹配，缺乏可验证证据链，导致解释性弱和泛化差。
2. 方法要点：构建REVEAL-Bench基准，基于多专家模型证据链，并设计专家驱动的强化学习框架，联合优化检测准确性和解释逻辑。
3. 实验或效果：实验显示REVEAL显著提升检测准确性、解释保真度和跨模型泛化能力，达到新SOTA。

## 📄 摘要（原文）

> With the rapid advancement of generative models, visually realistic AI-generated images have become increasingly difficult to distinguish from authentic ones, posing severe threats to social trust and information integrity. Consequently, there is an urgent need for efficient and truly explainable image forensic methods. Recent detection paradigms have shifted towards explainable forensics. However, state-of-the-art approaches primarily rely on post-hoc rationalizations or visual discrimination, lacking a verifiable chain of evidence. This reliance on surface-level pattern matching limits the generation of causally grounded explanations and often results in poor generalization. To bridge this critical gap, we introduce \textbf{REVEAL-Bench}, the first reasoning-enhanced multimodal benchmark for AI-generated image detection that is explicitly structured around a chain-of-evidence derived from multiple lightweight expert models, then records step-by-step reasoning traces and evidential justifications. Building upon this dataset, we propose \textbf{REVEAL} (\underline{R}easoning-\underline{e}nhanced Forensic E\underline{v}id\underline{e}nce \underline{A}na\underline{l}ysis), an effective and explainable forensic framework that integrates detection with a novel expert-grounded reinforcement learning. Our reward mechanism is specially tailored to jointly optimize detection accuracy, explanation fidelity, and logical coherence grounded in explicit forensic evidence, enabling REVEAL to produce fine-grained, interpretable, and verifiable reasoning chains alongside its detection outcomes. Extensive experimental results demonstrate that REVEAL significantly enhances detection accuracy, explanation fidelity, and robust cross-model generalization, benchmarking a new state of the art for explainable image forensics.

