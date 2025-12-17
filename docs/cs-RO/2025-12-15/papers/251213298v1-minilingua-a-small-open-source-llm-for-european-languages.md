---
layout: default
title: MiniLingua: A Small Open-Source LLM for European Languages
---

# MiniLingua: A Small Open-Source LLM for European Languages

**arXiv**: [2512.13298v1](https://arxiv.org/abs/2512.13298) | [PDF](https://arxiv.org/pdf/2512.13298.pdf)

**作者**: Anna Aksenova, Boris Zverkov, Nicola Dainese, Alexander Nikitin, Pekka Marttinen

---

## 💡 一句话要点

**提出MiniLingua小型开源多语言大模型，以解决欧洲语言覆盖与指令跟随的平衡问题。**

**关键词**: `多语言大模型` `小型模型` `指令跟随` `欧洲语言` `开源模型`

## 📋 核心要点

1. 核心问题：大模型计算成本高、隐私担忧及英语中心化训练限制应用。
2. 方法要点：从头训练10亿参数模型，覆盖13种欧洲语言，注重指令跟随能力。
3. 实验或效果：在多项任务中优于EuroLLM，与先进模型在开放生成任务中竞争。

## 📄 摘要（原文）

> Large language models are powerful but often limited by high computational cost, privacy concerns, and English-centric training. Recent progress demonstrates that small, efficient models with around one billion parameters can deliver strong results and enable on-device use. This paper introduces MiniLingua, a multilingual open-source LLM of one billion parameters trained from scratch for 13 European languages, designed to balance coverage and instruction-following capabilities. Based on evaluation results, the instruction-tuned version of MiniLingua outperforms EuroLLM, a model with a similar training approach but a larger training budget, on summarization, classification and both open- and closed-book question answering. Moreover, it remains competitive with more advanced state-of-the-art models on open-ended generation tasks. We release model weights, tokenizer and source code used for data processing and model training.

