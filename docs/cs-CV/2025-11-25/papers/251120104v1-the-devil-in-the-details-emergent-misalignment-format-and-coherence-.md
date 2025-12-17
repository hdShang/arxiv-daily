---
layout: default
title: The Devil in the Details: Emergent Misalignment, Format and Coherence in Open-Weights LLMs
---

# The Devil in the Details: Emergent Misalignment, Format and Coherence in Open-Weights LLMs

**arXiv**: [2511.20104v1](https://arxiv.org/abs/2511.20104) | [PDF](https://arxiv.org/pdf/2511.20104.pdf)

**作者**: Craig Dickson

---

## 💡 一句话要点

**评估开源大模型对微调引发错位的抵抗力，发现JSON输出增加脆弱性**

**关键词**: `涌现错位` `模型微调` `安全对齐` `JSON输出` `开源模型` `脆弱性评估`

## 📋 核心要点

1. 核心问题：微调窄域错位数据可导致广泛错位，即涌现错位现象
2. 方法要点：在九个开源模型上复现实验，比较不同架构和规模的抵抗力
3. 实验效果：JSON输出使错位率翻倍，开源模型错位率远低于GPT-4o

## 📄 摘要（原文）

> Prior work has shown that fine-tuning models on a narrow domain with misaligned data can lead to broad misalignment - a phenomenon termed "emergent misalignment" (Betley et al. 2025). While all tested models were susceptible to emergent misalignment, some models showed more resistance than others. Specifically the Qwen-2.5 family proved to be relatively resistant, while GPT-4o exhibited the strongest misalignment. In this paper we evaluate if current-generation open-weights models exhibit similar resistance to the Qwen-2.5 family and measure misalignment robustness over a range of model architectures and scales.
>   We replicate the effect across nine modern open-weights models (Gemma 3 and Qwen 3 families, 1B-32B parameters). Models fine-tuned on insecure code generation show a 0.68% misalignment rate (compared to 0.07% for base models), matching the lower end of prior open-model results but dramatically lower than GPT-4o's 20%.
>   We identify a critical format-dependent vulnerability: requiring JSON output doubles misalignment rates compared to natural language prompts (0.96% vs 0.42%). This suggests that structural constraints may bypass safety training by reducing the model's 'degrees of freedom' to refuse. These findings confirm emergent misalignment as a reproducible phenomenon in modern open-weights models, with rates substantially lower than observed in proprietary systems.

