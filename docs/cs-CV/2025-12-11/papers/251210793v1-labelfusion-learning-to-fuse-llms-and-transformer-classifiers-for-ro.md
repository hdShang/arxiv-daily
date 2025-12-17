---
layout: default
title: LabelFusion: Learning to Fuse LLMs and Transformer Classifiers for Robust Text Classification
---

# LabelFusion: Learning to Fuse LLMs and Transformer Classifiers for Robust Text Classification

**arXiv**: [2512.10793v1](https://arxiv.org/abs/2512.10793) | [PDF](https://arxiv.org/pdf/2512.10793.pdf)

**作者**: Michael Schlee, Christoph Weisser, Timo Kivimäki, Melchizedek Mashiku, Benjamin Saefken

---

## 💡 一句话要点

**提出LabelFusion融合方法，结合传统Transformer分类器与LLMs，实现鲁棒文本分类**

**关键词**: `文本分类` `融合集成` `大语言模型` `Transformer分类器` `端到端训练`

## 📋 核心要点

1. 核心问题：如何融合传统Transformer分类器与LLMs的优势，提升文本分类的准确性和成本效率
2. 方法要点：通过拼接ML骨干嵌入和LLM生成的分值，输入FusionMLP进行端到端学习融合
3. 实验或效果：在AG News和Reuters 21578数据集上分别达到92.4%和92.3%的准确率

## 📄 摘要（原文）

> LabelFusion is a fusion ensemble for text classification that learns to combine a traditional transformer-based classifier (e.g., RoBERTa) with one or more Large Language Models (LLMs such as OpenAI GPT, Google Gemini, or DeepSeek) to deliver accurate and cost-aware predictions across multi-class and multi-label tasks. The package provides a simple high-level interface (AutoFusionClassifier) that trains the full pipeline end-to-end with minimal configuration, and a flexible API for advanced users. Under the hood, LabelFusion integrates vector signals from both sources by concatenating the ML backbone's embeddings with the LLM-derived per-class scores -- obtained through structured prompt-engineering strategies -- and feeds this joint representation into a compact multi-layer perceptron (FusionMLP) that produces the final prediction. This learned fusion approach captures complementary strengths of LLM reasoning and traditional transformer-based classifiers, yielding robust performance across domains -- achieving 92.4% accuracy on AG News and 92.3% on 10-class Reuters 21578 topic classification -- while enabling practical trade-offs between accuracy, latency, and cost.

