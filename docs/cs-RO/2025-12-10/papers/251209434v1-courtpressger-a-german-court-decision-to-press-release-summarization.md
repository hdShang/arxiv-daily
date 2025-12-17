---
layout: default
title: CourtPressGER: A German Court Decision to Press Release Summarization Dataset
---

# CourtPressGER: A German Court Decision to Press Release Summarization Dataset

**arXiv**: [2512.09434v1](https://arxiv.org/abs/2512.09434) | [PDF](https://arxiv.org/pdf/2512.09434.pdf)

**作者**: Sebastian Nagl, Mohamed Elganayni, Melanie Pospisil, Matthias Grabmair

---

## 💡 一句话要点

**提出CourtPressGER数据集以解决德国法院判决到新闻稿的摘要生成问题**

**关键词**: `法律文本摘要` `数据集构建` `大语言模型评估` `事实一致性检查` `德国法院文档`

## 📋 核心要点

1. 核心问题：现有NLP研究忽视面向公众的法院新闻稿摘要需求，缺乏相关数据集
2. 方法要点：构建包含判决、人工新闻稿和合成提示的三元组数据集，用于训练和评估LLM
3. 实验或效果：通过多指标评估，大模型生成高质量草案，小模型需分层处理长文本

## 📄 摘要（原文）

> Official court press releases from Germany's highest courts present and explain judicial rulings to the public, as well as to expert audiences. Prior NLP efforts emphasize technical headnotes, ignoring citizen-oriented communication needs. We introduce CourtPressGER, a 6.4k dataset of triples: rulings, human-drafted press releases, and synthetic prompts for LLMs to generate comparable releases. This benchmark trains and evaluates LLMs in generating accurate, readable summaries from long judicial texts. We benchmark small and large LLMs using reference-based metrics, factual-consistency checks, LLM-as-judge, and expert ranking. Large LLMs produce high-quality drafts with minimal hierarchical performance loss; smaller models require hierarchical setups for long judgments. Initial benchmarks show varying model performance, with human-drafted releases ranking highest.

