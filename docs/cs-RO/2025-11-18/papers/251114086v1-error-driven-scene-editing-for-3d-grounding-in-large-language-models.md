---
layout: default
title: Error-Driven Scene Editing for 3D Grounding in Large Language Models
---

# Error-Driven Scene Editing for 3D Grounding in Large Language Models

**arXiv**: [2511.14086v1](https://arxiv.org/abs/2511.14086) | [PDF](https://arxiv.org/pdf/2511.14086.pdf)

**作者**: Yue Zhang, Zun Wang, Han Lin, Jialu Li, Jianing Yang, Yonatan Bitton, Idan Szpektor, Mohit Bansal

---

## 💡 一句话要点

**提出DEER-3D框架，通过错误驱动的3D场景编辑提升大语言模型的空间基础能力**

**关键词**: `3D基础` `场景编辑` `错误驱动学习` `大语言模型` `空间理解`

## 📋 核心要点

1. 核心问题：3D-LLMs在语言到视觉和空间元素的基础中存在偏差，源于训练数据缺乏空间理解。
2. 方法要点：采用分解、诊断、编辑和再训练流程，生成精确视觉反事实以迭代优化模型。
3. 实验或效果：在多个3D基础基准测试中，通过迭代精炼一致提升模型准确性。

## 📄 摘要（原文）

> Despite recent progress in 3D-LLMs, they remain limited in accurately grounding language to visual and spatial elements in 3D environments. This limitation stems in part from training data that focuses on language reasoning rather than spatial understanding due to scarce 3D resources, leaving inherent grounding biases unresolved. To address this, we propose 3D scene editing as a key mechanism to generate precise visual counterfactuals that mitigate these biases through fine-grained spatial manipulation, without requiring costly scene reconstruction or large-scale 3D data collection. Furthermore, to make these edits targeted and directly address the specific weaknesses of the model, we introduce DEER-3D, an error-driven framework following a structured "Decompose, Diagnostic Evaluation, Edit, and Re-train" workflow, rather than broadly or randomly augmenting data as in conventional approaches. Specifically, upon identifying a grounding failure of the 3D-LLM, our framework first diagnoses the exact predicate-level error (e.g., attribute or spatial relation). It then executes minimal, predicate-aligned 3D scene edits, such as recoloring or repositioning, to produce targeted counterfactual supervision for iterative model fine-tuning, significantly enhancing grounding accuracy. We evaluate our editing pipeline across multiple benchmarks for 3D grounding and scene understanding tasks, consistently demonstrating improvements across all evaluated datasets through iterative refinement. DEER-3D underscores the effectiveness of targeted, error-driven scene editing in bridging linguistic reasoning capabilities with spatial grounding in 3D LLMs.

