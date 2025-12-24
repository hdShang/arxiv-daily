---
layout: default
title: "Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management"
---

# Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04664" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04664v2</a>
  <a href="https://arxiv.org/pdf/2508.04664.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04664v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04664v2', 'Sculptor: Empowering LLMs with Cognitive Agency via Active Context Management')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mo Li, L. H. Xu, Qitai Tan, Long Ma, Ting Cao, Yunxin Liu

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-08-06 (更新: 2025-09-27)

**备注**: Preprint. Work in progress

---

## 💡 一句话要点

**提出Sculptor以解决长上下文处理中的干扰问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `主动上下文管理` `长上下文处理` `认知能力` `强化学习`

## 📋 核心要点

1. 现有方法主要依赖外部记忆系统，未能有效解决长上下文中的主动干扰问题。
2. 论文提出Sculptor框架，通过主动上下文管理工具，帮助LLMs主动管理注意力和工作记忆。
3. 实验结果显示，Sculptor在长上下文任务中显著提升了性能，证明了上下文控制策略的重要性。

## 📝 摘要（中文）

大型语言模型（LLMs）在处理长上下文时常因主动干扰而导致性能显著下降，早期上下文中的无关信息会干扰推理和记忆回忆。尽管大多数研究集中在外部记忆系统上以增强LLMs的能力，我们提出了一种补充方法：通过主动上下文管理（ACM）工具赋予LLMs认知能力。我们引入了Sculptor框架，为LLMs提供三类工具：上下文碎片化、摘要、隐藏与恢复，以及精确搜索。实验评估表明，Sculptor在多种长上下文基准测试中显著提升了性能，且无需特定训练，充分利用了LLMs固有的工具调用和指令跟随能力。

## 🔬 方法详解

**问题定义**：论文要解决的问题是大型语言模型在处理长上下文时因主动干扰导致的性能下降。现有方法主要依赖外部记忆系统，未能有效解决上下文中的无关信息干扰问题。

**核心思路**：论文的核心解决思路是通过主动上下文管理（ACM）工具赋予LLMs认知能力，使其能够主动管理内部工作记忆，类似于人类选择性关注相关信息并过滤干扰。

**技术框架**：Sculptor框架包含三个主要模块：上下文碎片化、摘要与隐藏恢复、精确搜索。这些模块协同工作，使LLMs能够在长上下文中更有效地处理信息。

**关键创新**：最重要的技术创新点在于引入了主动上下文管理工具，而不是单纯依赖更大的令牌窗口。这种设计使得LLMs能够更灵活地应对长上下文中的信息干扰。

**关键设计**：在设计中，Sculptor采用了动态上下文感知的强化学习方法，以优化LLMs的上下文管理策略。具体的参数设置和损失函数设计尚未详细披露，可能为未知。

## 📊 实验亮点

实验结果表明，Sculptor在多种长上下文基准测试中显著提升了性能，具体提升幅度未知。与基线模型相比，Sculptor在处理长上下文时的表现更为优越，验证了主动上下文管理策略的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括对话系统、文本生成和信息检索等长上下文任务。通过提升LLMs在长上下文中的处理能力，Sculptor能够为实际应用提供更可靠的推理支持，未来可能在智能助手和自动化内容生成等领域产生深远影响。

## 📄 摘要（原文）

> Large Language Models (LLMs) suffer from significant performance degradation when processing long contexts due to proactive interference, where irrelevant information in earlier parts of the context disrupts reasoning and memory recall. While most research focuses on external memory systems to augment LLMs' capabilities, we propose a complementary approach: empowering LLMs with Active Context Management (ACM) tools to actively sculpt their internal working memory. We introduce Sculptor, a framework that equips LLMs with three categories of tools: (1) context fragmentation, (2) summary, hide, and restore, and (3) precise search. Our approach enables LLMs to proactively manage their attention and working memory, analogous to how humans selectively focus on relevant information while filtering out distractions. Experimental evaluation on diverse long-context benchmarks demonstrates that Sculptor significantly improves performance even without specific training, leveraging LLMs' inherent tool-calling and instruction-following capabilities. To further optimize these strategies, we introduce a novel dynamic context-aware reinforcement learning (RL) approach, advancing the training of an agent that actively modifies its own conversational history. By enabling Active Context Management, Sculptor not only mitigates proactive interference but also provides a cognitive foundation for more reliable reasoning across diverse long-context tasks-highlighting that explicit context-control strategies, rather than merely larger token windows, are key to robustness at scale.

