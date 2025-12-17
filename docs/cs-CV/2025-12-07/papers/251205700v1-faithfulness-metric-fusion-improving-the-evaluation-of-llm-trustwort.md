---
layout: default
title: Faithfulness metric fusion: Improving the evaluation of LLM trustworthiness across domains
---

# Faithfulness metric fusion: Improving the evaluation of LLM trustworthiness across domains

**arXiv**: [2512.05700v1](https://arxiv.org/abs/2512.05700) | [PDF](https://arxiv.org/pdf/2512.05700.pdf)

**作者**: Ben Malin, Tatiana Kalganova, Nikolaos Boulgouris

---

## 💡 一句话要点

**提出基于树模型融合基础指标的方法，以提升大语言模型跨领域忠实度评估的准确性。**

**关键词**: `大语言模型` `忠实度评估` `指标融合` `树模型` `跨领域评估` `人类判断`

## 📋 核心要点

1. 核心问题：大语言模型输出忠实度评估准确性不足，影响模型可信度与跨场景应用。
2. 方法要点：融合多个基础忠实度指标，采用树模型根据人类判断确定指标权重，生成综合评估指标。
3. 实验或效果：融合指标在所有测试领域与人类判断相关性更强，提升评估能力，支持跨领域数据集复现与试验。

## 📄 摘要（原文）

> We present a methodology for improving the accuracy of faithfulness evaluation in Large Language Models (LLMs). The proposed methodology is based on the combination of elementary faithfulness metrics into a combined (fused) metric, for the purpose of improving the faithfulness of LLM outputs. The proposed strategy for metric fusion deploys a tree-based model to identify the importance of each metric, which is driven by the integration of human judgements evaluating the faithfulness of LLM responses. This fused metric is demonstrated to correlate more strongly with human judgements across all tested domains for faithfulness. Improving the ability to evaluate the faithfulness of LLMs, allows for greater confidence to be placed within models, allowing for their implementation in a greater diversity of scenarios. Additionally, we homogenise a collection of datasets across question answering and dialogue-based domains and implement human judgements and LLM responses within this dataset, allowing for the reproduction and trialling of faithfulness evaluation across domains.

