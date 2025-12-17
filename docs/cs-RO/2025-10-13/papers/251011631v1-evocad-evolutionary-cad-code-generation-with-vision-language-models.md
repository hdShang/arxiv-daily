---
layout: default
title: EvoCAD: Evolutionary CAD Code Generation with Vision Language Models
---

# EvoCAD: Evolutionary CAD Code Generation with Vision Language Models

**arXiv**: [2510.11631v1](https://arxiv.org/abs/2510.11631) | [PDF](https://arxiv.org/pdf/2510.11631.pdf)

**作者**: Tobias Preintner, Weixuan Yuan, Adrian König, Thomas Bäck, Elena Raponi, Niki van Stein

---

## 💡 一句话要点

**提出EvoCAD方法，结合视觉语言模型与进化算法生成CAD对象。**

**关键词**: `CAD生成` `进化算法` `视觉语言模型` `拓扑指标` `符号表示`

## 📋 核心要点

1. 核心问题：如何生成符号表示的CAD对象，并确保拓扑正确性。
2. 方法要点：使用视觉语言模型采样CAD对象，并通过进化算法优化。
3. 实验或效果：在CADPrompt基准上评估，新拓扑指标显示优于先前方法。

## 📄 摘要（原文）

> Combining large language models with evolutionary computation algorithms
> represents a promising research direction leveraging the remarkable generative
> and in-context learning capabilities of LLMs with the strengths of evolutionary
> algorithms. In this work, we present EvoCAD, a method for generating
> computer-aided design (CAD) objects through their symbolic representations
> using vision language models and evolutionary optimization. Our method samples
> multiple CAD objects, which are then optimized using an evolutionary approach
> with vision language and reasoning language models. We assess our method using
> GPT-4V and GPT-4o, evaluating it on the CADPrompt benchmark dataset and
> comparing it to prior methods. Additionally, we introduce two new metrics based
> on topological properties defined by the Euler characteristic, which capture a
> form of semantic similarity between 3D objects. Our results demonstrate that
> EvoCAD outperforms previous approaches on multiple metrics, particularly in
> generating topologically correct objects, which can be efficiently evaluated
> using our two novel metrics that complement existing spatial metrics.

