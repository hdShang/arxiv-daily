---
layout: default
title: BAID: A Benchmark for Bias Assessment of AI Detectors
---

# BAID: A Benchmark for Bias Assessment of AI Detectors

**arXiv**: [2512.11505v1](https://arxiv.org/abs/2512.11505) | [PDF](https://arxiv.org/pdf/2512.11505.pdf)

**作者**: Priyam Basu, Yunfeng Zhang, Vipul Raheja

---

## 💡 一句话要点

**提出BAID基准以系统评估AI文本检测器在广泛社会语言因素中的偏见问题。**

**关键词**: `AI文本检测器` `偏见评估` `社会语言因素` `基准测试` `合成文本生成`

## 📋 核心要点

1. 核心问题：AI文本检测器缺乏对人口统计、方言等社会语言偏见的系统性评估。
2. 方法要点：构建包含20万样本的框架，覆盖7类偏见，并生成保留内容但反映子群写作风格的合成文本。
3. 实验或效果：评估四个开源检测器，发现对少数群体文本的召回率低，强调部署前需偏见感知评估。

## 📄 摘要（原文）

> AI-generated text detectors have recently gained adoption in educational and professional contexts. Prior research has uncovered isolated cases of bias, particularly against English Language Learners (ELLs) however, there is a lack of systematic evaluation of such systems across broader sociolinguistic factors. In this work, we propose BAID, a comprehensive evaluation framework for AI detectors across various types of biases. As a part of the framework, we introduce over 200k samples spanning 7 major categories: demographics, age, educational grade level, dialect, formality, political leaning, and topic. We also generated synthetic versions of each sample with carefully crafted prompts to preserve the original content while reflecting subgroup-specific writing styles. Using this, we evaluate four open-source state-of-the-art AI text detectors and find consistent disparities in detection performance, particularly low recall rates for texts from underrepresented groups. Our contributions provide a scalable, transparent approach for auditing AI detectors and emphasize the need for bias-aware evaluation before these tools are deployed for public use.

