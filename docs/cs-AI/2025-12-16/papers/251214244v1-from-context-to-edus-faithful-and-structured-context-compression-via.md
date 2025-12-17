---
layout: default
title: From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition
---

# From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition

**arXiv**: [2512.14244v1](https://arxiv.org/abs/2512.14244) | [PDF](https://arxiv.org/pdf/2512.14244.pdf)

**作者**: Yiqing Zhou, Yu Lei, Shuzheng Si, Qingyan Sun, Wei Wang, Yifei Wu, Hao Wen, Gang Chen, Fanchao Qi, Maosong Sun

**分类**: cs.CL, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出基于基本话语单元的上下文压缩框架，以解决长文档处理中的计算成本高和噪声问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `上下文压缩` `基本话语单元` `结构关系树` `长文档处理` `大型语言模型` `计算效率` `下游任务增强` `显式压缩框架`

## 📋 核心要点

1. 现有压缩方法破坏局部连贯性或存在位置偏差，导致长文档处理效率低下。
2. 提出基于基本话语单元的结构化压缩框架，通过分解和选择保留上下文完整性。
3. 实验显示该方法在结构预测和下游任务中优于前沿模型，同时降低计算成本。

## 📝 摘要（中文）

管理大量上下文仍然是大型语言模型（LLMs）的关键瓶颈，特别是在长文档问答和自主代理等应用中，冗长的输入会导致高计算成本并引入噪声。现有的压缩技术通常通过离散标记删除破坏局部连贯性，或依赖存在位置偏差且与闭源API不兼容的隐式潜在编码。为解决这些限制，我们引入了基于EDU的上下文压缩器，这是一种新颖的显式压缩框架，旨在保留全局结构和细粒度细节。我们的方法将上下文压缩重新表述为结构-然后-选择的过程。首先，我们的LingoEDU将线性文本转换为基本话语单元（EDUs）的结构关系树，这些单元严格锚定到源索引以消除幻觉。其次，一个轻量级排名模块选择与查询相关的子树进行线性化。为了严格评估结构理解，我们发布了StructBench，这是一个包含248个多样化文档的手动标注数据集。实证结果表明，我们的方法实现了最先进的结构预测准确性，并显著优于前沿LLMs，同时降低了成本。此外，我们的结构感知压缩显著提高了从长上下文任务到复杂深度搜索场景的下游任务的性能。

## 🔬 方法详解

论文提出EDU-based Context Compressor框架，整体采用结构-然后-选择的两阶段流程。首先，LingoEDU模块将线性文本分解为基本话语单元（EDUs），构建结构关系树并严格锚定源索引以避免幻觉。其次，轻量级排名模块基于查询相关性选择子树进行线性化输出。关键创新在于显式结构化压缩，通过EDU分解保留全局和局部信息，与现有基于离散删除或隐式编码的方法相比，显著提升了结构保真度和兼容性。

## 📊 实验亮点

在StructBench数据集上实现最先进的结构预测准确性，显著优于前沿LLMs；结构感知压缩使下游任务性能大幅提升，同时减少计算成本，验证了方法的有效性。

## 🎯 应用场景

该研究适用于长文档问答、自主代理系统、复杂深度搜索等场景，能有效降低LLMs的计算开销和噪声干扰，提升处理效率和准确性，具有实际部署价值。

## 📄 摘要（原文）

> Managing extensive context remains a critical bottleneck for Large Language Models (LLMs), particularly in applications like long-document question answering and autonomous agents where lengthy inputs incur high computational costs and introduce noise. Existing compression techniques often disrupt local coherence through discrete token removal or rely on implicit latent encoding that suffers from positional bias and incompatibility with closed-source APIs. To address these limitations, we introduce the EDU-based Context Compressor, a novel explicit compression framework designed to preserve both global structure and fine-grained details. Our approach reformulates context compression as a structure-then-select process. First, our LingoEDU transforms linear text into a structural relation tree of Elementary Discourse Units (EDUs) which are anchored strictly to source indices to eliminate hallucination. Second, a lightweight ranking module selects query-relevant sub-trees for linearization. To rigorously evaluate structural understanding, we release StructBench, a manually annotated dataset of 248 diverse documents. Empirical results demonstrate that our method achieves state-of-the-art structural prediction accuracy and significantly outperforms frontier LLMs while reducing costs. Furthermore, our structure-aware compression substantially enhances performance across downstream tasks ranging from long-context tasks to complex Deep Search scenarios.

