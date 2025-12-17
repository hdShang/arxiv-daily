---
layout: default
title: RePo: Language Models with Context Re-Positioning
---

# RePo: Language Models with Context Re-Positioning

**arXiv**: [2512.14391v1](https://arxiv.org/abs/2512.14391) | [PDF](https://arxiv.org/pdf/2512.14391.pdf)

**作者**: Huayang Li, Tianyu Zhao, Richard Sproat

**分类**: cs.LG, cs.AI, cs.CL

**发布日期**: 2025-12-16

**🔗 代码/项目**: [GITHUB](https://github.com/SakanaAI/repo)

---

## 💡 一句话要点

**提出RePo机制，通过上下文重定位减少外部认知负荷，提升大语言模型在噪声上下文和长文本任务中的性能。**

**关键词**: `上下文学习` `位置编码` `认知负荷理论` `大语言模型` `注意力机制` `持续预训练` `噪声上下文处理` `长文本建模`

## 📋 核心要点

1. 现有大语言模型使用线性或恒定位置索引，导致上下文结构僵化，增加外部认知负荷，限制深度推理能力。
2. 提出RePo机制，利用可微分模块fφ动态分配标记位置，捕捉上下文依赖，减少外部负荷，优化注意力分配。
3. 实验表明，RePo在噪声上下文、结构化数据和长文本任务中性能显著提升，同时保持短上下文任务竞争力，注意力更聚焦相关远距离信息。

## 📝 摘要（中文）

上下文学习是现代大语言模型（LLMs）的基础；然而，主流架构通过分配线性或恒定的位置索引，强加了僵化固定的上下文结构。基于认知负荷理论（CLT），我们认为这种无信息结构增加了外部认知负荷，消耗了本应用于深度推理和注意力分配的有限工作记忆容量。为解决此问题，我们提出了RePo，一种通过上下文重定位减少外部负荷的新机制。与标准方法不同，RePo使用可微分模块fφ来分配捕捉上下文依赖关系的标记位置，而非依赖预定义的整数范围。通过在OLMo-2 1B骨干网络上持续预训练，我们证明RePo在涉及噪声上下文、结构化数据和更长上下文长度的任务中显著提升性能，同时在一般短上下文任务上保持竞争力。详细分析显示，RePo成功将更高注意力分配给遥远但相关的信息，在密集和非线性空间中分配位置，并捕捉输入上下文的内在结构。我们的代码可在https://github.com/SakanaAI/repo获取。

## 🔬 方法详解

RePo的整体框架基于大语言模型骨干（如OLMo-2 1B），通过持续预训练集成上下文重定位机制。关键技术创新点是引入可微分模块fφ，该模块动态学习并分配标记位置，以捕捉上下文依赖关系，而非依赖预定义的线性或恒定位置索引。与现有方法的主要区别在于：RePo打破了传统位置编码的僵化结构，允许位置在密集和非线性空间中灵活调整，从而更有效地建模上下文内在结构，减少外部认知负荷，提升模型在复杂任务中的表现。

## 📊 实验亮点

RePo在噪声上下文、结构化数据和长文本任务中性能显著提升，同时保持一般短上下文任务竞争力；分析显示模型能分配更高注意力给遥远相关信息，并有效捕捉输入结构。

## 🎯 应用场景

该研究可应用于需要处理噪声上下文、结构化数据或长文本的自然语言处理任务，如文档摘要、问答系统和代码生成，提升模型在实际场景中的鲁棒性和效率。

## 📄 摘要（原文）

> In-context learning is fundamental to modern Large Language Models (LLMs); however, prevailing architectures impose a rigid and fixed contextual structure by assigning linear or constant positional indices. Drawing on Cognitive Load Theory (CLT), we argue that this uninformative structure increases extraneous cognitive load, consuming finite working memory capacity that should be allocated to deep reasoning and attention allocation. To address this, we propose RePo, a novel mechanism that reduces extraneous load via context re-positioning. Unlike standard approaches, RePo utilizes a differentiable module, $f_φ$, to assign token positions that capture contextual dependencies, rather than replying on pre-defined integer range. By continually pre-training on the OLMo-2 1B backbone, we demonstrate that RePo significantly enhances performance on tasks involving noisy contexts, structured data, and longer context length, while maintaining competitive performance on general short-context tasks. Detailed analysis reveals that RePo successfully allocate higher attention to distant but relevant information, assign positions in dense and non-linear space, and capture the intrinsic structure of the input context. Our code is available at https://github.com/SakanaAI/repo.

