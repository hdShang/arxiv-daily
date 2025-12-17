---
layout: default
title: LongT2IBench: A Benchmark for Evaluating Long Text-to-Image Generation with Graph-structured Annotations
---

# LongT2IBench: A Benchmark for Evaluating Long Text-to-Image Generation with Graph-structured Annotations

**arXiv**: [2512.09271v1](https://arxiv.org/abs/2512.09271) | [PDF](https://arxiv.org/pdf/2512.09271.pdf)

**作者**: Zhichao Yang, Tianjiao Gu, Jianjie Wang, Feiyu Lin, Xiangfei Sheng, Pengfei Chen, Leida Li

---

## 💡 一句话要点

**提出LongT2IBench基准以评估长文本到图像生成的对齐性，并基于此开发LongT2IExpert评估器。**

**关键词**: `长文本到图像生成` `图结构标注` `对齐评估` `多模态大语言模型` `指令调优`

## 📋 核心要点

1. 现有基准主要针对短提示，缺乏长文本场景下的细粒度对齐评估。
2. 设计图结构标注协议，将长提示转换为实体、属性和关系的图结构以实现细粒度对齐。
3. 通过指令调优开发LongT2IExpert，提供量化分数和结构化解释，实验显示其优越性。

## 📄 摘要（原文）

> The increasing popularity of long Text-to-Image (T2I) generation has created an urgent need for automatic and interpretable models that can evaluate the image-text alignment in long prompt scenarios. However, the existing T2I alignment benchmarks predominantly focus on short prompt scenarios and only provide MOS or Likert scale annotations. This inherent limitation hinders the development of long T2I evaluators, particularly in terms of the interpretability of alignment. In this study, we contribute LongT2IBench, which comprises 14K long text-image pairs accompanied by graph-structured human annotations. Given the detail-intensive nature of long prompts, we first design a Generate-Refine-Qualify annotation protocol to convert them into textual graph structures that encompass entities, attributes, and relations. Through this transformation, fine-grained alignment annotations are achieved based on these granular elements. Finally, the graph-structed annotations are converted into alignment scores and interpretations to facilitate the design of T2I evaluation models. Based on LongT2IBench, we further propose LongT2IExpert, a LongT2I evaluator that enables multi-modal large language models (MLLMs) to provide both quantitative scores and structured interpretations through an instruction-tuning process with Hierarchical Alignment Chain-of-Thought (CoT). Extensive experiments and comparisons demonstrate the superiority of the proposed LongT2IExpert in alignment evaluation and interpretation. Data and code have been released in https://welldky.github.io/LongT2IBench-Homepage/.

