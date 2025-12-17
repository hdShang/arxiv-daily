---
layout: default
title: Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation
---

# Where Culture Fades: Revealing the Cultural Gap in Text-to-Image Generation

**arXiv**: [2511.17282v1](https://arxiv.org/abs/2511.17282) | [PDF](https://arxiv.org/pdf/2511.17282.pdf)

**作者**: Chuancheng Shi, Shangze Li, Shiming Guo, Simiao Xie, Wenhua Wu, Jingtong Dou, Chao Wu, Canran Xiao, Cong Wang, Zifeng Cheng, Fei Shen, Tat-Seng Chua

---

## 💡 一句话要点

**提出神经元激活与层增强方法以解决多语言文本到图像生成中的文化偏差问题**

**关键词**: `文本到图像生成` `文化一致性` `神经元激活` `层目标增强` `多语言模型` `文化偏差`

## 📋 核心要点

1. 核心问题：多语言T2I模型输出存在文化中性或英语偏见，源于文化相关表征激活不足
2. 方法要点：定位文化敏感神经元，采用推理时激活和层目标增强策略提升文化一致性
3. 实验或效果：在CultureBench上验证，文化一致性提升，同时保持保真度和多样性

## 📄 摘要（原文）

> Multilingual text-to-image (T2I) models have advanced rapidly in terms of visual realism and semantic alignment, and are now widely utilized. Yet outputs vary across cultural contexts: because language carries cultural connotations, images synthesized from multilingual prompts should preserve cross-lingual cultural consistency. We conduct a comprehensive analysis showing that current T2I models often produce culturally neutral or English-biased results under multilingual prompts. Analyses of two representative models indicate that the issue stems not from missing cultural knowledge but from insufficient activation of culture-related representations. We propose a probing method that localizes culture-sensitive signals to a small set of neurons in a few fixed layers. Guided by this finding, we introduce two complementary alignment strategies: (1) inference-time cultural activation that amplifies the identified neurons without backbone fine-tuned; and (2) layer-targeted cultural enhancement that updates only culturally relevant layers. Experiments on our CultureBench demonstrate consistent improvements over strong baselines in cultural consistency while preserving fidelity and diversity.

