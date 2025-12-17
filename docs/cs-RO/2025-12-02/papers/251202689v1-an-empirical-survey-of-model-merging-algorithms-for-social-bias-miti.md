---
layout: default
title: An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation
---

# An Empirical Survey of Model Merging Algorithms for Social Bias Mitigation

**arXiv**: [2512.02689v1](https://arxiv.org/abs/2512.02689) | [PDF](https://arxiv.org/pdf/2512.02689.pdf)

**作者**: Daiki Shirafuji, Tatsuhiko Saito, Yasutomo Kimura

---

## 💡 一句话要点

**实证比较七种模型合并算法在缓解大语言模型社会偏见中的效果与权衡**

**关键词**: `模型合并算法` `社会偏见缓解` `大语言模型` `实证调查` `性能权衡`

## 📋 核心要点

1. 核心问题：大语言模型继承并放大社会偏见，威胁公平性，需参数编辑缓解。
2. 方法要点：实证调查Linear、SLERP等七种合并算法，应用于GPT、LLaMA等13个开源权重模型。
3. 实验或效果：评估偏见减少与下游任务性能的权衡，发现SLERP在中等插值权重下表现最平衡。

## 📄 摘要（原文）

> Large language models (LLMs) are known to inherit and even amplify societal biases present in their pre-training corpora, threatening fairness and social trust. To address this issue, recent work has explored ``editing'' LLM parameters to mitigate social bias with model merging approaches; however, there is no empirical comparison. In this work, we empirically survey seven algorithms: Linear, Karcher Mean, SLERP, NuSLERP, TIES, DELLA, and Nearswap, applying 13 open weight models in the GPT, LLaMA, and Qwen families. We perform a comprehensive evaluation using three bias datasets (BBQ, BOLD, and HONEST) and measure the impact of these techniques on LLM performance in downstream tasks of the SuperGLUE benchmark. We find a trade-off between bias reduction and downstream performance: methods achieving greater bias mitigation degrade accuracy, particularly on tasks requiring reading comprehension and commonsense and causal reasoning. Among the merging algorithms, Linear, SLERP, and Nearswap consistently reduce bias while maintaining overall performance, with SLERP at moderate interpolation weights emerging as the most balanced choice. These results highlight the potential of model merging algorithms for bias mitigation, while indicating that excessive debiasing or inappropriate merging methods may lead to the degradation of important linguistic abilities.

