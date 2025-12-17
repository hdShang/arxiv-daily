---
layout: default
title: Benchmarking Scientific Understanding and Reasoning for Video Generation using VideoScience-Bench
---

# Benchmarking Scientific Understanding and Reasoning for Video Generation using VideoScience-Bench

**arXiv**: [2512.02942v1](https://arxiv.org/abs/2512.02942) | [PDF](https://arxiv.org/pdf/2512.02942.pdf)

**作者**: Lanxiang Hu, Abhilash Shankarampeta, Yixin Huang, Zilin Dai, Haoyang Yu, Yujie Zhao, Haoqiang Kang, Daniel Zhao, Tajana Rosing, Hao Zhang

---

## 💡 一句话要点

**提出VideoScience-Bench基准以评估视频生成模型的科学理解与推理能力**

**关键词**: `视频生成基准` `科学推理评估` `零样本推理` `物理化学理解` `多维度评估`

## 📋 核心要点

1. 现有视频基准基于物理常识，难以评估模型的科学推理能力
2. 基准包含200个提示，覆盖物理和化学的14个主题和103个概念
3. 通过专家标注和VLM评估，验证了与人类评估的强相关性

## 📄 摘要（原文）

> The next frontier for video generation lies in developing models capable of zero-shot reasoning, where understanding real-world scientific laws is crucial for accurate physical outcome modeling under diverse conditions. However, existing video benchmarks are physical commonsense-based, offering limited insight into video models' scientific reasoning capability. We introduce VideoScience-Bench, a benchmark designed to evaluate undergraduate-level scientific understanding in video models. Each prompt encodes a composite scientific scenario that requires understanding and reasoning across multiple scientific concepts to generate the correct phenomenon. The benchmark comprises 200 carefully curated prompts spanning 14 topics and 103 concepts in physics and chemistry. We conduct expert-annotated evaluations across seven state-of-the-art video models in T2V and I2V settings along five dimensions: Prompt Consistency, Phenomenon Congruency, Correct Dynamism, Immutability, and Spatio-Temporal Continuity. Using a VLM-as-a-Judge to assess video generations, we observe strong correlation with human assessments. To the best of our knowledge, VideoScience-Bench is the first benchmark to evaluate video models not only as generators but also as reasoners, requiring their generations to demonstrate scientific understanding consistent with expected physical and chemical phenomena. Our data and evaluation code are available at: \href{https://github.com/hao-ai-lab/VideoScience}{github.com/hao-ai-lab/VideoScience}.

