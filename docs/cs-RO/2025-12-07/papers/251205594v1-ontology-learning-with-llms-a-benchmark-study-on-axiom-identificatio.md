---
layout: default
title: Ontology Learning with LLMs: A Benchmark Study on Axiom Identification
---

# Ontology Learning with LLMs: A Benchmark Study on Axiom Identification

**arXiv**: [2512.05594v1](https://arxiv.org/abs/2512.05594) | [PDF](https://arxiv.org/pdf/2512.05594.pdf)

**作者**: Roos M. Bakker, Daan L. Di Scala, Maaike H. T. de Boer, Stephan A. Raaijmakers

---

## 💡 一句话要点

**提出OntoAxiom基准以评估LLMs在公理识别中的性能，支持本体工程自动化。**

**关键词**: `本体学习` `公理识别` `大型语言模型` `基准测试` `提示策略`

## 📋 核心要点

1. 核心问题：自动化本体学习中的公理识别，即定义类与属性间逻辑关系的基础组件。
2. 方法要点：引入OntoAxiom基准，包含9个本体和2771个公理，测试12个LLMs的两种提示策略。
3. 实验或效果：Axiom-by-Axiom提示策略优于直接方法，但性能因公理类型和本体而异，LLMs可提供候选公理辅助工程师。

## 📄 摘要（原文）

> Ontologies are an important tool for structuring domain knowledge, but their development is a complex task that requires significant modelling and domain expertise. Ontology learning, aimed at automating this process, has seen advancements in the past decade with the improvement of Natural Language Processing techniques, and especially with the recent growth of Large Language Models (LLMs). This paper investigates the challenge of identifying axioms: fundamental ontology components that define logical relations between classes and properties. In this work, we introduce an Ontology Axiom Benchmark OntoAxiom, and systematically test LLMs on that benchmark for axiom identification, evaluating different prompting strategies, ontologies, and axiom types. The benchmark consists of nine medium-sized ontologies with together 17.118 triples, and 2.771 axioms. We focus on subclass, disjoint, subproperty, domain, and range axioms. To evaluate LLM performance, we compare twelve LLMs with three shot settings and two prompting strategies: a Direct approach where we query all axioms at once, versus an Axiom-by-Axiom (AbA) approach, where each prompt queries for one axiom only. Our findings show that the AbA prompting leads to higher F1 scores than the direct approach. However, performance varies across axioms, suggesting that certain axioms are more challenging to identify. The domain also influences performance: the FOAF ontology achieves a score of 0.642 for the subclass axiom, while the music ontology reaches only 0.218. Larger LLMs outperform smaller ones, but smaller models may still be viable for resource-constrained settings. Although performance overall is not high enough to fully automate axiom identification, LLMs can provide valuable candidate axioms to support ontology engineers with the development and refinement of ontologies.

