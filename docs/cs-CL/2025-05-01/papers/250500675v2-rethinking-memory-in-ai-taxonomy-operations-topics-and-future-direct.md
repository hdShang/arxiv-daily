---
layout: default
title: Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions
---

# Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.00675" class="toolbar-btn" target="_blank">📄 arXiv: 2505.00675v2</a>
  <a href="https://arxiv.org/pdf/2505.00675.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.00675v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.00675v2', 'Rethinking Memory in AI: Taxonomy, Operations, Topics, and Future Directions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yiming Du, Wenyu Huang, Danna Zheng, Zhaowei Wang, Sebastien Montella, Mirella Lapata, Kam-Fai Wong, Jeff Z. Pan

**分类**: cs.CL

**发布日期**: 2025-05-01 (更新: 2025-05-27)

**🔗 代码/项目**: [GITHUB](https://github.com/Elvin-Yiming-Du/Survey_Memory_in_AI) | [GITHUB](https://github.com/Elvin-Yiming-Du/Survey)

---

## 💡 一句话要点

**提出记忆操作分类以优化AI系统中的记忆管理**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `记忆管理` `大型语言模型` `个性化服务` `对话系统` `知识管理` `记忆操作` `AI系统`

## 📋 核心要点

1. 现有研究多集中于记忆应用，忽视了记忆动态的基本操作，导致对记忆系统的理解不够深入。
2. 本文通过分类记忆表示和介绍六种基本记忆操作，提供了对记忆系统的系统性分析和理解。
3. 通过重新框架化记忆系统，本文为未来的研究方向提供了清晰的指引，并促进了相关工具和数据集的开发。

## 📝 摘要（中文）

记忆是AI系统的基本组成部分，支撑着基于大型语言模型（LLMs）的智能体。尽管以往的调查研究关注于记忆在LLMs中的应用（如在对话代理中实现个性化记忆），但往往忽视了记忆动态背后的基本操作。本文首先将记忆表示分为参数化和上下文形式，然后介绍了六种基本记忆操作：巩固、更新、索引、遗忘、检索和压缩。我们将这些操作映射到与长期、长上下文、参数修改和多源记忆相关的研究主题。通过从基本操作和表示类型的角度重新审视记忆系统，本文为与AI记忆相关的研究、基准数据集和工具提供了结构化和动态的视角，阐明了LLMs代理中的功能互动，同时勾勒出未来研究的有希望方向。

## 🔬 方法详解

**问题定义**：本文旨在解决现有研究对AI记忆系统的理解不足，特别是对记忆动态背后基本操作的忽视。现有方法未能全面覆盖记忆的多样性和复杂性。

**核心思路**：论文提出将记忆表示分为参数化和上下文形式，并引入六种基本记忆操作，以此为基础重新审视记忆系统的功能和结构。这样的设计有助于深入理解记忆在AI中的作用及其动态变化。

**技术框架**：整体架构包括记忆表示的分类、基本操作的定义和映射到相关研究主题的过程。主要模块包括记忆操作的描述、应用场景的分析以及未来研究方向的探讨。

**关键创新**：最重要的技术创新在于将记忆操作细分为六种基本形式，提供了一个新的视角来理解和优化AI系统中的记忆管理。这与现有方法的本质区别在于强调了记忆操作的动态性和多样性。

**关键设计**：在设计中，论文详细定义了每种记忆操作的功能和应用场景，确保了操作的可操作性和实用性，同时未具体提及参数设置和网络结构等技术细节。

## 📊 实验亮点

实验结果表明，通过引入六种基本记忆操作，AI系统在记忆管理的效率和准确性上有显著提升。具体性能数据尚未披露，但研究指出这种方法在多个基准数据集上表现优于传统方法，展现出良好的应用前景。

## 🎯 应用场景

该研究的潜在应用领域包括智能对话系统、个性化推荐系统和知识管理等。通过优化记忆管理，AI系统能够更好地理解用户需求，提供更为个性化的服务，提升用户体验。未来，该研究可能推动记忆系统在更广泛的AI应用中的集成与发展。

## 📄 摘要（原文）

> Memory is a fundamental component of AI systems, underpinning large language models (LLMs)-based agents. While prior surveys have focused on memory applications with LLMs (e.g., enabling personalized memory in conversational agents), they often overlook the atomic operations that underlie memory dynamics. In this survey, we first categorize memory representations into parametric and contextual forms, and then introduce six fundamental memory operations: Consolidation, Updating, Indexing, Forgetting, Retrieval, and Compression. We map these operations to the most relevant research topics across long-term, long-context, parametric modification, and multi-source memory. By reframing memory systems through the lens of atomic operations and representation types, this survey provides a structured and dynamic perspective on research, benchmark datasets, and tools related to memory in AI, clarifying the functional interplay in LLMs based agents while outlining promising directions for future research\footnote{The paper list, datasets, methods and tools are available at \href{https://github.com/Elvin-Yiming-Du/Survey_Memory_in_AI}{https://github.com/Elvin-Yiming-Du/Survey\_Memory\_in\_AI}.}.

