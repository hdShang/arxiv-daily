---
layout: default
title: Long Context Scaling: Divide and Conquer via Multi-Agent Question-driven Collaboration
---

# Long Context Scaling: Divide and Conquer via Multi-Agent Question-driven Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20625" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20625v3</a>
  <a href="https://arxiv.org/pdf/2505.20625.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20625v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20625v3', 'Long Context Scaling: Divide and Conquer via Multi-Agent Question-driven Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sibo Xiao, Zixin Lin, Wenyang Gao, Hui Chen, Yue Zhang

**分类**: cs.CL

**发布日期**: 2025-05-27 (更新: 2025-09-28)

---

## 💡 一句话要点

**提出XpandA框架以解决长文本处理中的信息损失问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长文本处理` `多代理框架` `动态分区` `问题引导` `信息一致性` `自然语言处理` `性能提升`

## 📋 核心要点

1. 现有的长文本处理方法存在累积延迟高和信息损失等问题，影响了模型的性能。
2. 提出的XpandA框架通过动态分区和问题引导协议来优化长文本的处理流程。
3. 实验结果表明，XpandA在多个基准测试中实现了20%的性能提升和1.5倍的推理速度加快。

## 📝 摘要（中文）

处理长文本已成为现代大型语言模型（LLMs）的关键能力。现有的基于代理的分治方法在处理长文本时面临显著的局限性，包括累积延迟过高、信息损失加剧以及文本依赖关系的破坏。本文提出了一种新颖的多代理框架XpandA，结合了基于问题的工作流程和动态分区，旨在增强长文本处理的鲁棒性。XpandA通过动态分区、问题引导协议和选择性重放特定分区来克服这些限制。我们在多个长文本基准上对XpandA进行了全面评估，结果显示其在处理超长序列方面的可行性和显著效果，较基线方法提高了20%的性能和1.5倍的推理速度。

## 🔬 方法详解

**问题定义**：本文旨在解决现有长文本处理方法在信息损失和延迟方面的不足，尤其是在代理调用过多时导致的文本依赖关系破坏。

**核心思路**：XpandA框架通过动态分区和问题引导的工作流程，灵活调整输入序列的上下文窗口填充率，从而提高长文本的处理效率和准确性。

**技术框架**：XpandA的整体架构包括动态分区模块、问题引导协议和状态跟踪机制。动态分区模块根据文本长度自适应调整分区策略，问题引导协议则在共享内存中更新信息，确保各代理间知识的一致性。

**关键创新**：XpandA的主要创新在于其动态分区和问题引导的结合，能够有效减少信息损失并保持文本的依赖关系，这与传统的静态分区方法形成鲜明对比。

**关键设计**：在XpandA中，动态分区的填充率和问题引导的更新策略是关键设计元素，确保了信息在各个分区间的有效传递和重放，进而提升了模型的整体性能。

## 📊 实验亮点

XpandA在多个长文本基准测试中表现出色，相较于全上下文、RAG和以往的代理方法，性能提升达20%，推理速度提高1.5倍，显示出其在处理超长序列方面的显著优势。

## 🎯 应用场景

XpandA框架在长文本处理领域具有广泛的应用潜力，尤其适用于需要分析和理解超长文本的任务，如法律文书、学术论文和长篇小说等。其高效的信息处理能力将为自然语言处理的各类应用提供支持，推动相关技术的发展。

## 📄 摘要（原文）

> Processing long contexts has become a critical capability for modern large language models (LLMs). Existing works leverage agent-based divide-and-conquer methods for processing long contexts. But these methods face crucial limitations, including prohibitive accumulated latency and amplified information loss from excessive agent invocations, and the disruption of inherent textual dependencies by immoderate partitioning. In this paper, we propose a novel multi-agent framework XpandA (Expand-Agent) coupled with question-driven workflow and dynamic partitioning for robust long-context processing. XpandA overcomes these limitations through: 1) dynamic partitioning of long texts, which adaptively modulates the filling rate of context windows for input sequences of vastly varying lengths; 2) question-guided protocol to update flat information ensembles within centralized shared memory, constructing consistent inter-agent knowledge across partitions; and 3) selectively replaying specific partitions based on the state-tracking of question-information couples to promote the resolution of inverted-order structures across partitions (e.g., flashbacks). We perform a comprehensive evaluation of XpandA on multiple long-context benchmarks with length varying from 1k to 1M, demonstrating XpandA's feasibility for processing ultra-long sequences and its significant effectiveness in enhancing the long-context capabilities of various LLMs by achieving 20\% improvements and 1.5x inference speedup over baselines of full-context, RAG and previous agent-based methods.

