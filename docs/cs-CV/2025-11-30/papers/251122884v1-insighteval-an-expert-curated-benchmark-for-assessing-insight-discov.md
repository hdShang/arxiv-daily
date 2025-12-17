---
layout: default
title: InsightEval: An Expert-Curated Benchmark for Assessing Insight Discovery in LLM-Driven Data Agents
---

# InsightEval: An Expert-Curated Benchmark for Assessing Insight Discovery in LLM-Driven Data Agents

**arXiv**: [2511.22884v1](https://arxiv.org/abs/2511.22884) | [PDF](https://arxiv.org/pdf/2511.22884.pdf)

**作者**: Zhenghao Zhu, Yuanfeng Song, Xin Chen, Chengzhong Liu, Yakun Cui, Caleb Chen Cao, Sirui Han, Yike Guo

---

## 💡 一句话要点

**提出InsightEval基准以评估LLM驱动数据代理的洞察发现能力**

**关键词**: `洞察发现评估` `LLM驱动数据代理` `基准构建` `数据整理流程` `探索性能指标` `自动数据分析`

## 📋 核心要点

1. 核心问题：现有基准如InsightBench存在格式不一致、目标设计不佳和洞察冗余等缺陷，影响评估质量。
2. 方法要点：基于高质量基准标准，开发数据整理流程构建InsightEval数据集，并引入新指标衡量代理探索性能。
3. 实验或效果：通过广泛实验，揭示自动洞察发现的挑战，并提供关键发现指导未来研究。

## 📄 摘要（原文）

> Data analysis has become an indispensable part of scientific research. To discover the latent knowledge and insights hidden within massive datasets, we need to perform deep exploratory analysis to realize their full value. With the advent of large language models (LLMs) and multi-agent systems, more and more researchers are making use of these technologies for insight discovery. However, there are few benchmarks for evaluating insight discovery capabilities. As one of the most comprehensive existing frameworks, InsightBench also suffers from many critical flaws: format inconsistencies, poorly conceived objectives, and redundant insights. These issues may significantly affect the quality of data and the evaluation of agents. To address these issues, we thoroughly investigate shortcomings in InsightBench and propose essential criteria for a high-quality insight benchmark. Regarding this, we develop a data-curation pipeline to construct a new dataset named InsightEval. We further introduce a novel metric to measure the exploratory performance of agents. Through extensive experiments on InsightEval, we highlight prevailing challenges in automated insight discovery and raise some key findings to guide future research in this promising direction.

