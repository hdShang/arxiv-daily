---
layout: default
title: HalluShift++: Bridging Language and Vision through Internal Representation Shifts for Hierarchical Hallucinations in MLLMs
---

# HalluShift++: Bridging Language and Vision through Internal Representation Shifts for Hierarchical Hallucinations in MLLMs

**arXiv**: [2512.07687v1](https://arxiv.org/abs/2512.07687) | [PDF](https://arxiv.org/pdf/2512.07687.pdf)

**作者**: Sujoy Nath, Arkaprabha Basu, Sharanya Dasgupta, Swagatam Das

---

## 💡 一句话要点

**提出HalluShift++方法，通过分析内部层动态检测多模态大语言模型中的幻觉问题。**

**关键词**: `多模态大语言模型` `幻觉检测` `内部层分析` `视觉语言理解` `模型评估`

## 📋 核心要点

1. 核心问题：MLLMs在视觉语言任务中常产生与视觉内容不一致的幻觉描述，现有评估方法依赖外部LLM评估器，易受幻觉影响且领域适应性差。
2. 方法要点：假设幻觉表现为MLLMs内部层动态的可测量异常，通过层间分析检测这些异常，扩展幻觉检测至多模态场景。
3. 实验或效果：HalluShift++提升了幻觉检测的效能，代码已开源，具体效果未知。

## 📄 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in vision-language understanding tasks. While these models often produce linguistically coherent output, they often suffer from hallucinations, generating descriptions that are factually inconsistent with the visual content, potentially leading to adverse consequences. Therefore, the assessment of hallucinations in MLLM has become increasingly crucial in the model development process. Contemporary methodologies predominantly depend on external LLM evaluators, which are themselves susceptible to hallucinations and may present challenges in terms of domain adaptation. In this study, we propose the hypothesis that hallucination manifests as measurable irregularities within the internal layer dynamics of MLLMs, not merely due to distributional shifts but also in the context of layer-wise analysis of specific assumptions. By incorporating such modifications, \textsc{\textsc{HalluShift++}} broadens the efficacy of hallucination detection from text-based large language models (LLMs) to encompass multimodal scenarios. Our codebase is available at https://github.com/C0mRD/HalluShift_Plus.

