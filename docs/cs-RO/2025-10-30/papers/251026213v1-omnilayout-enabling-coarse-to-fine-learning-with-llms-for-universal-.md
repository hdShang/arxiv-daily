---
layout: default
title: OmniLayout: Enabling Coarse-to-Fine Learning with LLMs for Universal Document Layout Generation
---

# OmniLayout: Enabling Coarse-to-Fine Learning with LLMs for Universal Document Layout Generation

**arXiv**: [2510.26213v1](https://arxiv.org/abs/2510.26213) | [PDF](https://arxiv.org/pdf/2510.26213.pdf)

**作者**: Hengrui Kang, Zhuangcheng Gu, Zhiyuan Zhao, Zichen Wen, Bin Wang, Weijia Li, Conghui He

---

## 💡 一句话要点

**提出OmniLayout-LLM与数据集，通过粗到细学习解决通用文档布局生成问题**

**关键词**: `文档布局生成` `粗到细学习` `大语言模型` `数据集构建` `多领域评估`

## 📋 核心要点

1. 核心问题：文档布局生成领域缺乏多样布局数据，现有方法难以处理复杂和长序列布局
2. 方法要点：构建百万级数据集OmniLayout-1M，并设计两阶段粗到细学习范式训练0.5B模型
3. 实验或效果：在M$^{6}$Doc数据集上超越现有布局生成专家和通用大语言模型

## 📄 摘要（原文）

> Document AI has advanced rapidly and is attracting increasing attention. Yet,
> while most efforts have focused on document layout analysis (DLA), its
> generative counterpart, document layout generation, remains underexplored. A
> major obstacle lies in the scarcity of diverse layouts: academic papers with
> Manhattan-style structures dominate existing studies, while open-world genres
> such as newspapers and magazines remain severely underrepresented. To address
> this gap, we curate OmniLayout-1M, the first million-scale dataset of diverse
> document layouts, covering six common document types and comprising
> contemporary layouts collected from multiple sources. Moreover, since existing
> methods struggle in complex domains and often fail to arrange long sequences
> coherently, we introduce OmniLayout-LLM, a 0.5B model with designed two-stage
> Coarse-to-Fine learning paradigm: 1) learning universal layout principles from
> OmniLayout-1M with coarse category definitions, and 2) transferring the
> knowledge to a specific domain with fine-grained annotations. Extensive
> experiments demonstrate that our approach achieves strong performance on
> multiple domains in M$^{6}$Doc dataset, substantially surpassing both existing
> layout generation experts and several latest general-purpose LLMs. Our code,
> models, and dataset will be publicly released.

