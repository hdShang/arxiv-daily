---
layout: default
title: Self Distillation Fine-Tuning of Protein Language Models Improves Versatility in Protein Design
---

# Self Distillation Fine-Tuning of Protein Language Models Improves Versatility in Protein Design

**arXiv**: [2512.09329v1](https://arxiv.org/abs/2512.09329) | [PDF](https://arxiv.org/pdf/2512.09329.pdf)

**作者**: Amin Tavakoli, Raswanth Murugan, Ozan Gokdemir, Arvind Ramanathan, Frances Arnold, Anima Anandkumar

---

## 💡 一句话要点

**提出自蒸馏微调方法以提升蛋白质语言模型在蛋白质设计中的通用性**

**关键词**: `蛋白质语言模型` `监督微调` `自蒸馏` `蛋白质设计` `序列生成`

## 📋 核心要点

1. 核心问题：蛋白质语言模型微调缺乏高质量标注数据，导致生成序列保真度低。
2. 方法要点：利用模型自身输出构建训练数据，结合轻量级筛选管道进行监督微调。
3. 实验或效果：在色氨酸合酶家族中验证，生成序列更新颖且稳定性与功能性提升。

## 📄 摘要（原文）

> Supervised fine-tuning (SFT) is a standard approach for adapting large language models to specialized domains, yet its application to protein sequence modeling and protein language models (PLMs) remains ad hoc. This is in part because high-quality annotated data are far more difficult to obtain for proteins than for natural language. We present a simple and general recipe for fast SFT of PLMs, designed to improve the fidelity, reliability, and novelty of generated protein sequences. Unlike existing approaches that require costly precompiled experimental datasets for SFT, our method leverages the PLM itself, integrating a lightweight curation pipeline with domain-specific filters to construct high-quality training data. These filters can independently refine a PLM's output and identify candidates for in vitro evaluation; when combined with SFT, they enable PLMs to generate more stable and functional enzymes, while expanding exploration into protein sequence space beyond natural variants. Although our approach is agnostic to both the choice of protein language model (PLM) and the protein system, we demonstrate its effectiveness with a genome-scale PLM (GenSLM) applied to the tryptophan synthase enzyme family. The supervised fine-tuned model generates sequences that are not only more novel but also display improved characteristics across both targeted design constraints and emergent protein property measures.

