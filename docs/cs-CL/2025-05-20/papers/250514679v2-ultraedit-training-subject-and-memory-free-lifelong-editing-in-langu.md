---
layout: default
title: "UltraEdit: Training-, Subject-, and Memory-Free Lifelong Editing in Language Models"
---

# UltraEdit: Training-, Subject-, and Memory-Free Lifelong Editing in Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14679" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14679v2</a>
  <a href="https://arxiv.org/pdf/2505.14679.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14679v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14679v2', 'UltraEdit: Training-, Subject-, and Memory-Free Lifelong Editing in Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaojie Gu, Ziying Huang, Jia-Chen Gu, Kai Zhang

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-05-20 (更新: 2025-09-26)

**🔗 代码/项目**: [GITHUB](https://github.com/XiaojieGu/UltraEdit)

---

## 💡 一句话要点

**提出UltraEdit以解决大规模语言模型的终身编辑问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `终身学习` `模型编辑` `语言模型` `高效计算` `数据集构建` `自然语言处理` `深度学习`

## 📋 核心要点

1. 现有的模型编辑方法在实际应用中难以满足大规模终身适应的需求，尤其是在效率和资源消耗方面存在明显不足。
2. UltraEdit通过无训练、无主题和无记忆的方式，利用隐藏状态和梯度一步计算参数变化，提供了一种简单高效的终身编辑方案。
3. 实验结果表明，UltraEdit的编辑速度比之前的最先进方法快7倍，且显存使用量不到四分之一，支持高达200万次编辑，准确率保持高水平。

## 📝 摘要（中文）

终身学习使大型语言模型（LLMs）能够通过不断更新内部知识来适应不断变化的信息。理想的系统应支持高效、广泛的更新，同时保持现有能力并确保可靠部署。模型编辑作为一种有前景的解决方案，提供了一种集中且高效的方式来修订模型的内部知识。为此，本文提出UltraEdit，一种无训练、无主题、无记忆的终身编辑方法，适合超大规模的实际应用。UltraEdit通过仅使用隐藏状态及其梯度一步计算参数变化，显著提高了效率。该方法在终身设置中采用终身归一化策略，持续更新特征统计，以适应分布变化并保持一致性。UltraEdit的编辑速度比之前的最先进方法快7倍，同时使用的显存不到四分之一，使其成为唯一能够在24GB消费级GPU上编辑7B LLM的方法。我们构建了UltraEditBench，这是迄今为止该领域最大的编辑对数据集，支持高达200万次编辑且保持高准确率。综合实验表明，UltraEdit在多种模型编辑场景中表现优异，向安全和可扩展的终身学习迈出了重要一步。

## 🔬 方法详解

**问题定义**：本文旨在解决现有模型编辑方法在大规模终身学习中的效率和资源消耗问题。现有方法往往无法在保持性能的同时进行高效的知识更新。

**核心思路**：UltraEdit的核心思路是通过无训练、无主题和无记忆的方式，利用隐藏状态和梯度一步计算参数变化，从而简化编辑过程，提高效率。

**技术框架**：UltraEdit的整体架构包括三个主要模块：参数计算模块、终身归一化模块和编辑执行模块。参数计算模块负责根据隐藏状态和梯度计算参数变化，终身归一化模块持续更新特征统计，编辑执行模块则应用这些变化进行模型编辑。

**关键创新**：UltraEdit的关键创新在于其无训练、无主题和无记忆的设计，使得模型编辑过程更加高效且适应性强。这一方法与传统模型编辑方法的本质区别在于其计算方式的简化和对资源的优化使用。

**关键设计**：在参数设置上，UltraEdit采用了动态的特征统计更新机制，损失函数设计上注重保持模型的原有能力，同时引入了高效的梯度计算方法，以确保编辑过程的快速性和准确性。

## 📊 实验亮点

UltraEdit在实验中表现出色，其编辑速度超过了之前的最先进方法7倍，且显存使用量不到四分之一。该方法支持高达200万次编辑，且在多种模型编辑场景中保持高准确率，展示了其在终身学习中的优越性。

## 🎯 应用场景

UltraEdit的研究成果在多个领域具有广泛的应用潜力，包括自然语言处理、对话系统和智能助手等。其高效的终身编辑能力使得模型能够快速适应新信息，保持高性能，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Lifelong learning enables large language models (LLMs) to adapt to evolving information by continually updating their internal knowledge. An ideal system should support efficient, wide-ranging updates while preserving existing capabilities and ensuring reliable deployment. Model editing stands out as a promising solution for this goal, offering a focused and efficient way to revise a model's internal knowledge. Although recent paradigms have made notable progress, they often struggle to meet the demands of practical lifelong adaptation at scale. To bridge this gap, we propose UltraEdit, a training-, subject-, and memory-free approach that is well-suited for ultra-scalable, real-world lifelong model editing. UltraEdit fundamentally differs from traditional paradigms by computing parameter shifts in one step using only a hidden state and its gradient, making the approach simple yet efficient. To improve scalability in lifelong settings, UltraEdit employs a lifelong normalization strategy that continuously updates feature statistics across turns, allowing it to adapt to distributional shifts and maintain consistency over time. UltraEdit achieves editing speeds over 7x faster than the previous state-of-the-art method, which was also the fastest known approach, while using less than 1/4 the VRAM. This makes it the only method currently capable of editing a 7B LLM on a 24GB consumer-grade GPU. Furthermore, we construct UltraEditBench, the largest dataset in the field to date with over 2M editing pairs, and demonstrate that our method supports up to 2M edits while maintaining high accuracy. Comprehensive experiments on five datasets and six models show that UltraEdit consistently achieves superior performance across diverse model editing scenarios, taking a further step towards safe and scalable lifelong learning. Our code is available at: https://github.com/XiaojieGu/UltraEdit

