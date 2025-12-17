---
layout: default
title: Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations
---

# Evaluating Reasoning Faithfulness in Medical Vision-Language Models using Multimodal Perturbations

**arXiv**: [2510.11196v1](https://arxiv.org/abs/2510.11196) | [PDF](https://arxiv.org/pdf/2510.11196.pdf)

**作者**: Johannes Moll, Markus Graf, Tristan Lemke, Nicolas Lenhart, Daniel Truhn, Jean-Benoit Delbrouck, Jiazhen Pan, Daniel Rueckert, Lisa C. Adams, Keno K. Bressem

---

## 💡 一句话要点

**提出基于多模态扰动的医学视觉语言模型推理忠实性评估框架，用于胸部X光视觉问答。**

**关键词**: `医学视觉语言模型` `推理忠实性评估` `多模态扰动` `胸部X光视觉问答` `链式思维解释` `临床可信度`

## 📋 核心要点

1. 核心问题：视觉语言模型的链式思维解释常与决策过程不符，影响临床高风险应用的可信度。
2. 方法要点：通过文本和图像修改，评估临床保真度、因果归因和置信度校准三个维度。
3. 实验或效果：基准测试显示答案准确性与解释质量脱钩，专有模型在归因和保真度上表现更优。

## 📄 摘要（原文）

> Vision-language models (VLMs) often produce chain-of-thought (CoT)
> explanations that sound plausible yet fail to reflect the underlying decision
> process, undermining trust in high-stakes clinical use. Existing evaluations
> rarely catch this misalignment, prioritizing answer accuracy or adherence to
> formats. We present a clinically grounded framework for chest X-ray visual
> question answering (VQA) that probes CoT faithfulness via controlled text and
> image modifications across three axes: clinical fidelity, causal attribution,
> and confidence calibration. In a reader study (n=4), evaluator-radiologist
> correlations fall within the observed inter-radiologist range for all axes,
> with strong alignment for attribution (Kendall's $\tau_b=0.670$), moderate
> alignment for fidelity ($\tau_b=0.387$), and weak alignment for confidence tone
> ($\tau_b=0.091$), which we report with caution. Benchmarking six VLMs shows
> that answer accuracy and explanation quality are decoupled, acknowledging
> injected cues does not ensure grounding, and text cues shift explanations more
> than visual cues. While some open-source models match final answer accuracy,
> proprietary models score higher on attribution (25.0% vs. 1.4%) and often on
> fidelity (36.1% vs. 31.7%), highlighting deployment risks and the need to
> evaluate beyond final answer accuracy.

