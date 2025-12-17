---
layout: default
title: SMoG: Schema Matching on Graph
---

# SMoG: Schema Matching on Graph

**arXiv**: [2511.20285v1](https://arxiv.org/abs/2511.20285) | [PDF](https://arxiv.org/pdf/2511.20285.pdf)

**作者**: Mingyu Jeon, Jaeyoung Suh, Suwan Cho

---

## 💡 一句话要点

**提出SMoG框架，利用简单1跳SPARQL查询解决医疗数据集成中的模式匹配问题。**

**关键词**: `模式匹配` `知识图谱` `SPARQL查询` `医疗数据集成` `LLM增强` `可解释性`

## 📋 核心要点

1. 核心问题：LLM在模式匹配中易产生幻觉且缺乏最新领域知识，影响医疗EHR系统对齐。
2. 方法要点：采用迭代执行1跳SPARQL查询，增强可解释性并减少存储需求。
3. 实验或效果：在真实医疗数据集上性能媲美先进基线，验证其高效性和可靠性。

## 📄 摘要（原文）

> Schema matching is a critical task in data integration, par- ticularly in the medical domain where disparate Electronic Health Record (EHR) systems must be aligned to standard models like OMOP CDM. While Large Language Models (LLMs) have shown promise in schema matching, they suf- fer from hallucination and lack of up-to-date domain knowl- edge. Knowledge Graphs (KGs) offer a solution by pro- viding structured, verifiable knowledge. However, existing KG-augmented LLM approaches often rely on inefficient complex multi-hop queries or storage-intensive vector-based retrieval methods. This paper introduces SMoG (Schema Matching on Graph), a novel framework that leverages iter- ative execution of simple 1-hop SPARQL queries, inspired by successful strategies in Knowledge Graph Question An- swering (KGQA). SMoG enhances explainability and relia- bility by generating human-verifiable query paths while sig- nificantly reducing storage requirements by directly querying SPARQL endpoints. Experimental results on real-world med- ical datasets demonstrate that SMoG achieves performance comparable to state-of-the-art baselines, validating its effec- tiveness and efficiency in KG-augmented schema matching.

