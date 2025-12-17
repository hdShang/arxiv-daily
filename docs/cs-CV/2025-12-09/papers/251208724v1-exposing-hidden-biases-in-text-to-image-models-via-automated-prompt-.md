---
layout: default
title: Exposing Hidden Biases in Text-to-Image Models via Automated Prompt Search
---

# Exposing Hidden Biases in Text-to-Image Models via Automated Prompt Search

**arXiv**: [2512.08724v1](https://arxiv.org/abs/2512.08724) | [PDF](https://arxiv.org/pdf/2512.08724.pdf)

**作者**: Manos Plitsis, Giorgos Bouritsas, Vassilis Katsouros, Yannis Panagakis

---

## 💡 一句话要点

**提出Bias-Guided Prompt Search框架，通过自动提示搜索暴露文本到图像模型的隐藏偏见**

**关键词**: `文本到图像模型` `偏见检测` `提示搜索` `公平性评估` `扩散模型`

## 📋 核心要点

1. 问题：现有方法依赖人工或LLM构建提示数据集，可能忽略触发偏见的未预期提示，影响偏见缓解效果。
2. 方法：结合LLM生成属性中性提示和属性分类器引导解码，自动搜索放大图像偏见的提示。
3. 实验：在Stable Diffusion 1.5和去偏见模型上发现新偏见，提示可解释且提升困惑度指标。

## 📄 摘要（原文）

> Text-to-image (TTI) diffusion models have achieved remarkable visual quality, yet they have been repeatedly shown to exhibit social biases across sensitive attributes such as gender, race and age. To mitigate these biases, existing approaches frequently depend on curated prompt datasets - either manually constructed or generated with large language models (LLMs) - as part of their training and/or evaluation procedures. Beside the curation cost, this also risks overlooking unanticipated, less obvious prompts that trigger biased generation, even in models that have undergone debiasing. In this work, we introduce Bias-Guided Prompt Search (BGPS), a framework that automatically generates prompts that aim to maximize the presence of biases in the resulting images. BGPS comprises two components: (1) an LLM instructed to produce attribute-neutral prompts and (2) attribute classifiers acting on the TTI's internal representations that steer the decoding process of the LLM toward regions of the prompt space that amplify the image attributes of interest. We conduct extensive experiments on Stable Diffusion 1.5 and a state-of-the-art debiased model and discover an array of subtle and previously undocumented biases that severely deteriorate fairness metrics. Crucially, the discovered prompts are interpretable, i.e they may be entered by a typical user, quantitatively improving the perplexity metric compared to a prominent hard prompt optimization counterpart. Our findings uncover TTI vulnerabilities, while BGPS expands the bias search space and can act as a new evaluation tool for bias mitigation.

