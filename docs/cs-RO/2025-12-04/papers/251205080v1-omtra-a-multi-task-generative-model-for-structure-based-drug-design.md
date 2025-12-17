---
layout: default
title: OMTRA: A Multi-Task Generative Model for Structure-Based Drug Design
---

# OMTRA: A Multi-Task Generative Model for Structure-Based Drug Design

**arXiv**: [2512.05080v1](https://arxiv.org/abs/2512.05080) | [PDF](https://arxiv.org/pdf/2512.05080.pdf)

**作者**: Ian Dunn, Liv Toft, Tyler Katz, Juhi Gupta, Riya Shah, Ramith Hettiarachchi, David R. Koes

---

## 💡 一句话要点

**提出OMTRA多模态流匹配模型，统一结构药物设计任务框架。**

**关键词**: `结构药物设计` `多任务生成模型` `流匹配` `口袋条件设计` `分子对接`

## 📋 核心要点

1. 核心问题：结构药物设计任务分散，缺乏统一生成模型框架。
2. 方法要点：基于多模态流匹配，灵活处理口袋条件设计、对接等任务。
3. 实验或效果：在口袋条件从头设计和对接任务上达到先进性能。

## 📄 摘要（原文）

> Structure-based drug design (SBDD) focuses on designing small-molecule ligands that bind to specific protein pockets. Computational methods are integral in modern SBDD workflows and often make use of virtual screening methods via docking or pharmacophore search. Modern generative modeling approaches have focused on improving novel ligand discovery by enabling de novo design. In this work, we recognize that these tasks share a common structure and can therefore be represented as different instantiations of a consistent generative modeling framework. We propose a unified approach in OMTRA, a multi-modal flow matching model that flexibly performs many tasks relevant to SBDD, including some with no analogue in conventional workflows. Additionally, we curate a dataset of 500M 3D molecular conformers, complementing protein-ligand data and expanding the chemical diversity available for training. OMTRA obtains state of the art performance on pocket-conditioned de novo design and docking; however, the effects of large-scale pretraining and multi-task training are modest. All code, trained models, and dataset for reproducing this work are available at https://github.com/gnina/OMTRA

