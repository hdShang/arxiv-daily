---
layout: default
title: Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates
---

# Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates

**arXiv**: [2512.04844v1](https://arxiv.org/abs/2512.04844) | [PDF](https://arxiv.org/pdf/2512.04844.pdf)

**作者**: Atsuki Yamaguchi, Terufumi Morishita, Aline Villavicencio, Nikolaos Aletras

---

## 💡 一句话要点

**提出源屏蔽更新以解决大语言模型在低资源目标语言适应中的灾难性遗忘问题**

**关键词**: `灾难性遗忘缓解` `低资源语言适应` `参数选择性更新` `大语言模型微调` `源知识保护`

## 📋 核心要点

1. 核心问题：大语言模型在仅用无标注目标语言数据适应时，易发生灾难性遗忘，损害源语言能力。
2. 方法要点：基于源数据参数重要性评分，采用列级冻结策略选择性更新参数，保护源知识。
3. 实验或效果：在5种语言和7B/13B模型上，显著减少源任务性能下降，目标语言性能与全微调竞争。

## 📄 摘要（原文）

> Expanding the linguistic diversity of instruct large language models (LLMs) is crucial for global accessibility but is often hindered by the reliance on costly specialized target language labeled data and catastrophic forgetting during adaptation. We tackle this challenge under a realistic, low-resource constraint: adapting instruct LLMs using only unlabeled target language data. We introduce Source-Shielded Updates (SSU), a selective parameter update strategy that proactively preserves source knowledge. Using a small set of source data and a parameter importance scoring method, SSU identifies parameters critical to maintaining source abilities. It then applies a column-wise freezing strategy to protect these parameters before adaptation. Experiments across five typologically diverse languages and 7B and 13B models demonstrate that SSU successfully mitigates catastrophic forgetting. It reduces performance degradation on monolingual source tasks to just 3.4% (7B) and 2.8% (13B) on average, a stark contrast to the 20.3% and 22.3% from full fine-tuning. SSU also achieves target-language performance highly competitive with full fine-tuning, outperforming it on all benchmarks for 7B models and the majority for 13B models.

