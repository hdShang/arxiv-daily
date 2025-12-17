---
layout: default
title: Towards Trustworthy Dermatology MLLMs: A Benchmark and Multimodal Evaluator for Diagnostic Narratives
---

# Towards Trustworthy Dermatology MLLMs: A Benchmark and Multimodal Evaluator for Diagnostic Narratives

**arXiv**: [2511.09195v1](https://arxiv.org/abs/2511.09195) | [PDF](https://arxiv.org/pdf/2511.09195.pdf)

**作者**: Yuhao Shen, Jiahe Qian, Shuping Zhang, Zhangtianyi Chen, Tao Lu, Juexiao Zhou

---

## 💡 一句话要点

**提出DermBench基准与DermEval评估器以解决皮肤病学多模态大模型可靠评估问题**

**关键词**: `皮肤病学诊断` `多模态大语言模型` `基准评估` `自动评估器` `临床部署` `模型可信度`

## 📋 核心要点

1. 核心问题：皮肤病学多模态大模型生成诊断叙述的可靠评估是临床部署的主要瓶颈
2. 方法要点：构建DermBench基准和DermEval无参考多模态评估器，支持结构化评分
3. 实验或效果：在4500个案例上，评估结果与专家评分偏差分别为0.251和0.117

## 📄 摘要（原文）

> Multimodal large language models (LLMs) are increasingly used to generate dermatology diagnostic narratives directly from images. However, reliable evaluation remains the primary bottleneck for responsible clinical deployment. We introduce a novel evaluation framework that combines DermBench, a meticulously curated benchmark, with DermEval, a robust automatic evaluator, to enable clinically meaningful, reproducible, and scalable assessment. We build DermBench, which pairs 4,000 real-world dermatology images with expert-certified diagnostic narratives and uses an LLM-based judge to score candidate narratives across clinically grounded dimensions, enabling consistent and comprehensive evaluation of multimodal models. For individual case assessment, we train DermEval, a reference-free multimodal evaluator. Given an image and a generated narrative, DermEval produces a structured critique along with an overall score and per-dimension ratings. This capability enables fine-grained, per-case analysis, which is critical for identifying model limitations and biases. Experiments on a diverse dataset of 4,500 cases demonstrate that DermBench and DermEval achieve close alignment with expert ratings, with mean deviations of 0.251 and 0.117 (out of 5), respectively, providing reliable measurement of diagnostic ability and trustworthiness across different multimodal LLMs.

