---
layout: default
title: Multi-Granular Node Pruning for Circuit Discovery
---

# Multi-Granular Node Pruning for Circuit Discovery

**arXiv**: [2512.10903v1](https://arxiv.org/abs/2512.10903) | [PDF](https://arxiv.org/pdf/2512.10903.pdf)

**作者**: Muhammad Umair Haider, Hammad Rizwan, Hassan Sajjad, A. B. Siddique

---

## 💡 一句话要点

**提出多粒度节点剪枝框架以解决大语言模型电路发现中的可扩展性与粒度限制问题**

**关键词**: `电路发现` `节点剪枝` `多粒度优化` `大语言模型` `稀疏化`

## 📋 核心要点

1. 现有方法依赖迭代边剪枝，计算成本高且粒度粗，忽略神经元级结构
2. 引入可学习掩码与粒度特定稀疏惩罚，在统一优化中实现从块到神经元的多粒度剪枝
3. 实验显示节点更少、内存占用降低5-10倍，同时保持任务性能

## 📄 摘要（原文）

> Circuit discovery aims to identify minimal subnetworks that are responsible for specific behaviors in large language models (LLMs). Existing approaches primarily rely on iterative edge pruning, which is computationally expensive and limited to coarse-grained units such as attention heads or MLP blocks, overlooking finer structures like individual neurons. We propose a node-level pruning framework for circuit discovery that addresses both scalability and granularity limitations. Our method introduces learnable masks across multiple levels of granularity, from entire blocks to individual neurons, within a unified optimization objective. Granularity-specific sparsity penalties guide the pruning process, allowing a comprehensive compression in a single fine-tuning run. Empirically, our approach identifies circuits that are smaller in nodes than those discovered by prior methods; moreover, we demonstrate that many neurons deemed important by coarse methods are actually irrelevant, while still maintaining task performance. Furthermore, our method has a significantly lower memory footprint, 5-10x, as it does not require keeping intermediate activations in the memory to work.

