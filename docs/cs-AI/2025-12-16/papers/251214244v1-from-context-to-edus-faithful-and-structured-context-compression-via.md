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

**提出基于基本话语单元的上下文压缩框架，通过结构化分解与选择解决长文本处理中的计算成本与噪声问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `上下文压缩` `基本话语单元` `结构化分解` `长文本处理` `大型语言模型` `计算效率` `下游任务增强` `显式压缩框架`

## 📋 核心要点

1. 现有压缩方法破坏局部连贯性或依赖隐含编码，导致位置偏差和API不兼容，难以平衡压缩效率与信息保留。
2. 提出基于基本话语单元的结构化分解框架，通过先构建关系树再选择相关子树，实现显式、可解释的上下文压缩。
3. 在StructBench数据集上实现最先进的结构预测精度，显著优于前沿LLMs，并在下游任务中提升性能，同时降低计算成本。

## 📝 摘要（中文）

管理大量上下文仍然是大型语言模型（LLMs）的关键瓶颈，特别是在长文档问答和自主代理等应用中，长输入会导致高计算成本并引入噪声。现有的压缩技术通常通过离散标记删除破坏局部连贯性，或依赖隐含的潜在编码，这些方法存在位置偏差且与闭源API不兼容。为解决这些限制，我们引入了基于EDU的上下文压缩器，这是一种新颖的显式压缩框架，旨在保留全局结构和细粒度细节。我们的方法将上下文压缩重新表述为“先结构后选择”的过程。首先，我们的LingoEDU将线性文本转换为基本话语单元（EDUs）的结构关系树，这些单元严格锚定到源索引以消除幻觉。其次，一个轻量级排名模块选择与查询相关的子树进行线性化。为了严格评估结构理解，我们发布了StructBench，这是一个包含248个多样化文档的手动标注数据集。实证结果表明，我们的方法实现了最先进的结构预测准确性，并显著优于前沿LLMs，同时降低了成本。此外，我们的结构感知压缩显著提高了从长上下文任务到复杂深度搜索场景的下游任务性能。

## 🔬 方法详解

**问题定义**：论文旨在解决长文本处理中上下文压缩的挑战，现有方法如离散标记删除会破坏局部连贯性，而隐含编码方法存在位置偏差且与闭源API不兼容，导致压缩后信息失真或难以集成。

**核心思路**：将上下文压缩重新定义为“先结构后选择”的过程，通过将线性文本分解为基本话语单元（EDUs）的结构关系树，再基于查询相关性选择子树，实现显式、结构化的压缩，以保留全局逻辑和细粒度细节。

**技术框架**：整体架构包含两个主要阶段：首先，LingoEDU模块将输入文本转换为EDUs的结构关系树，每个EDU严格锚定到源文本索引；其次，轻量级排名模块评估查询与子树的相关性，选择高相关子树进行线性化输出为压缩文本。

**关键创新**：最重要的创新是引入EDU-based显式压缩框架，通过结构化分解消除幻觉，与现有方法相比，本质区别在于强调可解释性和结构保留，而非仅依赖隐含表示或简单删减。

**关键设计**：LingoEDU基于语言学规则或预训练模型自动识别EDUs并构建关系树；排名模块可能使用注意力机制或相似度计算，具体参数和损失函数在论文中未详细说明，但强调轻量化和高效性以降低计算开销。

## 📊 实验亮点

在StructBench数据集上，该方法实现了最先进的结构预测准确性，具体性能数据未在摘要中提供，但显著优于前沿LLMs；实验表明，结构感知压缩在下游任务中提升性能，同时减少计算开销，例如在长上下文任务和深度搜索场景中表现优异。

## 🎯 应用场景

该研究在长文档问答、自主代理、复杂深度搜索等场景具有广泛应用价值，能显著降低LLMs的计算成本并提升处理效率，未来可推动智能文档分析和多轮对话系统的发展，增强AI在真实世界任务中的实用性。

## 📄 摘要（原文）

> Managing extensive context remains a critical bottleneck for Large Language Models (LLMs), particularly in applications like long-document question answering and autonomous agents where lengthy inputs incur high computational costs and introduce noise. Existing compression techniques often disrupt local coherence through discrete token removal or rely on implicit latent encoding that suffers from positional bias and incompatibility with closed-source APIs. To address these limitations, we introduce the EDU-based Context Compressor, a novel explicit compression framework designed to preserve both global structure and fine-grained details. Our approach reformulates context compression as a structure-then-select process. First, our LingoEDU transforms linear text into a structural relation tree of Elementary Discourse Units (EDUs) which are anchored strictly to source indices to eliminate hallucination. Second, a lightweight ranking module selects query-relevant sub-trees for linearization. To rigorously evaluate structural understanding, we release StructBench, a manually annotated dataset of 248 diverse documents. Empirical results demonstrate that our method achieves state-of-the-art structural prediction accuracy and significantly outperforms frontier LLMs while reducing costs. Furthermore, our structure-aware compression substantially enhances performance across downstream tasks ranging from long-context tasks to complex Deep Search scenarios.

