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

**提出基于基本话语单元的上下文压缩器，通过结构化分解与选择解决长文本处理中的计算成本与噪声问题。**

**关键词**: `上下文压缩` `基本话语单元` `结构关系树` `长文本处理` `大语言模型` `计算效率` `下游任务增强` `显式压缩框架`

## 📋 核心要点

1. 现有压缩方法常破坏文本局部连贯性或依赖隐式编码，导致位置偏差和API不兼容问题。
2. 提出基于基本话语单元的显式压缩框架，通过结构关系树分解和查询相关子树选择实现忠实压缩。
3. 在StructBench数据集上实现最先进结构预测准确性，显著降低计算成本并提升下游任务性能。

## 📝 摘要（中文）

管理长上下文是大语言模型（LLMs）的关键瓶颈，尤其在长文档问答和自主代理等应用中，长输入导致高计算成本和噪声引入。现有压缩技术常通过离散令牌移除破坏局部连贯性，或依赖隐式潜在编码，存在位置偏差且与闭源API不兼容。为应对这些限制，我们引入了基于基本话语单元（EDU）的上下文压缩器，这是一种新颖的显式压缩框架，旨在保留全局结构和细粒度细节。我们的方法将上下文压缩重新表述为“先结构后选择”的过程：首先，LingoEDU将线性文本转换为基于源索引锚定的基本话语单元结构关系树，以消除幻觉；其次，轻量级排名模块选择查询相关的子树进行线性化。为严格评估结构理解，我们发布了StructBench，一个包含248个多样化文档的手动标注数据集。实证结果表明，我们的方法在结构预测准确性上达到最先进水平，显著优于前沿LLMs，同时降低成本。此外，我们的结构感知压缩在从长上下文任务到复杂深度搜索场景的下游任务中大幅提升了性能。

## 🔬 方法详解

论文提出EDU-based Context Compressor框架，整体流程为结构-then-选择。首先，LingoEDU模块将线性文本分解为基本话语单元（EDU），构建严格锚定源索引的结构关系树，确保压缩忠实性。其次，轻量级排名模块基于查询相关性选择子树进行线性化输出。关键创新在于显式结构化压缩，避免了隐式编码的偏差，并保持全局与局部细节。与现有方法的主要区别在于强调结构保留和显式索引，而非依赖离散令牌移除或潜在表示。

## 📊 实验亮点

在StructBench数据集上，方法实现最先进的结构预测准确性，显著优于前沿LLMs，同时压缩成本降低，并在长上下文任务和复杂搜索中带来性能提升。

## 🎯 应用场景

该研究适用于长文档问答、自主代理、深度搜索等场景，能有效降低LLMs的计算开销和噪声干扰，提升处理效率和准确性，具有实际部署价值。

## 📄 摘要（原文）

> Managing extensive context remains a critical bottleneck for Large Language Models (LLMs), particularly in applications like long-document question answering and autonomous agents where lengthy inputs incur high computational costs and introduce noise. Existing compression techniques often disrupt local coherence through discrete token removal or rely on implicit latent encoding that suffers from positional bias and incompatibility with closed-source APIs. To address these limitations, we introduce the EDU-based Context Compressor, a novel explicit compression framework designed to preserve both global structure and fine-grained details. Our approach reformulates context compression as a structure-then-select process. First, our LingoEDU transforms linear text into a structural relation tree of Elementary Discourse Units (EDUs) which are anchored strictly to source indices to eliminate hallucination. Second, a lightweight ranking module selects query-relevant sub-trees for linearization. To rigorously evaluate structural understanding, we release StructBench, a manually annotated dataset of 248 diverse documents. Empirical results demonstrate that our method achieves state-of-the-art structural prediction accuracy and significantly outperforms frontier LLMs while reducing costs. Furthermore, our structure-aware compression substantially enhances performance across downstream tasks ranging from long-context tasks to complex Deep Search scenarios.

