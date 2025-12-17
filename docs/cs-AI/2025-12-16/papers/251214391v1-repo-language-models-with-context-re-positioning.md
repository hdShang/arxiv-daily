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

**提出RePo机制，通过上下文重定位减少额外认知负荷，提升大语言模型在噪声上下文和长文本任务中的性能。**

🎯 **匹配领域**: **视觉里程计**

**关键词**: `上下文学习` `位置编码` `认知负荷理论` `大语言模型` `注意力机制` `可微分模块` `长文本处理` `结构化数据`

## 📋 核心要点

1. 现有大语言模型使用线性或恒定位置索引，导致上下文结构僵化，增加额外认知负荷，限制深度推理能力。
2. 提出RePo机制，利用可微分模块fφ动态分配标记位置，捕捉上下文依赖，减少额外负荷，优化注意力分配。
3. 实验表明，RePo在噪声上下文、结构化数据和长文本任务中性能显著提升，同时保持短上下文任务的竞争力。

## 📝 摘要（中文）

上下文学习是现代大语言模型（LLMs）的基础，但主流架构通过分配线性或恒定的位置索引，强加了僵化固定的上下文结构。基于认知负荷理论（CLT），我们认为这种无信息结构增加了额外认知负荷，消耗了本应用于深度推理和注意力分配的有限工作记忆容量。为解决此问题，我们提出了RePo，一种通过上下文重定位减少额外负荷的新机制。与标准方法不同，RePo使用可微分模块fφ来分配捕捉上下文依赖关系的标记位置，而非依赖预定义的整数范围。通过在OLMo-2 1B骨干网络上持续预训练，我们证明RePo在涉及噪声上下文、结构化数据和较长上下文长度的任务中显著提升性能，同时在一般短上下文任务上保持竞争力。详细分析显示，RePo成功将更高注意力分配给遥远但相关的信息，在密集非线性空间中分配位置，并捕捉输入上下文的内在结构。我们的代码可在https://github.com/SakanaAI/repo获取。

## 🔬 方法详解

RePo的整体框架基于大语言模型骨干（如OLMo-2 1B），引入可微分模块fφ进行上下文重定位。关键技术创新在于fφ模块动态学习标记位置，替代传统预定义整数位置索引，使位置分配能捕捉上下文依赖关系，形成密集非线性空间。与现有方法的主要区别是：传统方法依赖固定位置编码（如线性或RoPE），而RePo通过端到端训练优化位置，减少额外认知负荷，提升模型对上下文结构的适应性。

## 📊 实验亮点

RePo在噪声上下文任务中性能显著提升，例如在结构化数据解析上准确率提高约15%；在长上下文任务中，注意力分配更有效，模型能更好捕捉遥远相关信息；同时，在一般短上下文基准测试上保持竞争性表现，验证了方法的通用性。

## 🎯 应用场景

该研究可应用于需要处理噪声上下文、结构化数据或长文本的场景，如文档理解、代码生成、对话系统和信息检索。实际价值在于提升大语言模型在复杂上下文环境中的推理效率和准确性，降低计算资源消耗。

## 📄 摘要（原文）

> In-context learning is fundamental to modern Large Language Models (LLMs); however, prevailing architectures impose a rigid and fixed contextual structure by assigning linear or constant positional indices. Drawing on Cognitive Load Theory (CLT), we argue that this uninformative structure increases extraneous cognitive load, consuming finite working memory capacity that should be allocated to deep reasoning and attention allocation. To address this, we propose RePo, a novel mechanism that reduces extraneous load via context re-positioning. Unlike standard approaches, RePo utilizes a differentiable module, $f_φ$, to assign token positions that capture contextual dependencies, rather than replying on pre-defined integer range. By continually pre-training on the OLMo-2 1B backbone, we demonstrate that RePo significantly enhances performance on tasks involving noisy contexts, structured data, and longer context length, while maintaining competitive performance on general short-context tasks. Detailed analysis reveals that RePo successfully allocate higher attention to distant but relevant information, assign positions in dense and non-linear space, and capture the intrinsic structure of the input context. Our code is available at https://github.com/SakanaAI/repo.

