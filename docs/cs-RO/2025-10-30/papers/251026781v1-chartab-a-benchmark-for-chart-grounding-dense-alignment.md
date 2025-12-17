---
layout: default
title: ChartAB: A Benchmark for Chart Grounding & Dense Alignment
---

# ChartAB: A Benchmark for Chart Grounding & Dense Alignment

**arXiv**: [2510.26781v1](https://arxiv.org/abs/2510.26781) | [PDF](https://arxiv.org/pdf/2510.26781.pdf)

**作者**: Aniruddh Bansal, Davit Soselia, Dang Nguyen, Tianyi Zhou

---

## 💡 一句话要点

**提出ChartAB基准以评估视觉语言模型在图表细粒度对齐与比较中的能力**

**关键词**: `图表理解` `视觉语言模型评估` `细粒度对齐` `基准测试` `多图表比较` `JSON模板`

## 📋 核心要点

1. 现有视觉语言模型在图表细节感知和结构提取方面存在不足，影响多图表比较与推理
2. 设计JSON模板和两阶段推理工作流，支持图表元素定位、属性识别和跨图表对齐评估
3. 评估多个模型揭示感知偏差、弱点和幻觉，为模型改进提供具体方向

## 📄 摘要（原文）

> Charts play an important role in visualization, reasoning, data analysis, and
> the exchange of ideas among humans. However, existing vision-language models
> (VLMs) still lack accurate perception of details and struggle to extract
> fine-grained structures from charts. Such limitations in chart grounding also
> hinder their ability to compare multiple charts and reason over them. In this
> paper, we introduce a novel "ChartAlign Benchmark (ChartAB)" to provide a
> comprehensive evaluation of VLMs in chart grounding tasks, i.e., extracting
> tabular data, localizing visualization elements, and recognizing various
> attributes from charts of diverse types and complexities. We design a JSON
> template to facilitate the calculation of evaluation metrics specifically
> tailored for each grounding task. By incorporating a novel two-stage inference
> workflow, the benchmark can further evaluate VLMs' capability to align and
> compare elements/attributes across two charts. Our analysis of evaluations on
> several recent VLMs reveals new insights into their perception biases,
> weaknesses, robustness, and hallucinations in chart understanding. These
> findings highlight the fine-grained discrepancies among VLMs in chart
> understanding tasks and point to specific skills that need to be strengthened
> in current models.

