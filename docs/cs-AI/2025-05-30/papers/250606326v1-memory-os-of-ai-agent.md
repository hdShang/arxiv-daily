---
layout: default
title: Memory OS of AI Agent
---

# Memory OS of AI Agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.06326" class="toolbar-btn" target="_blank">📄 arXiv: 2506.06326v1</a>
  <a href="https://arxiv.org/pdf/2506.06326.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.06326v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.06326v1', 'Memory OS of AI Agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiazheng Kang, Mingming Ji, Zhe Zhao, Ting Bai

**分类**: cs.AI

**发布日期**: 2025-05-30

**🔗 代码/项目**: [GITHUB](https://github.com/BAI-LAB/MemoryOS)

---

## 💡 一句话要点

**提出MemoryOS以解决大语言模型的长期记忆管理问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `记忆操作系统` `大语言模型` `长期记忆` `个性化交互` `动态更新` `分层存储` `AI代理`

## 📋 核心要点

1. 现有大语言模型在长期记忆管理方面存在显著不足，导致个性化交互体验受限。
2. 本文提出MemoryOS，通过分层存储架构和动态更新机制，提升AI代理的记忆管理能力。
3. 在LoCoMo基准测试中，MemoryOS在F1和BLEU-1指标上分别较基线提升了49.11%和46.18%。

## 📝 摘要（中文）

大语言模型（LLMs）面临固定上下文窗口和不足的记忆管理带来的挑战，导致长期记忆能力严重不足，个性化交互体验受限。为此，本文创新性地提出了Memory操作系统（MemoryOS），旨在实现AI代理的全面高效记忆管理。MemoryOS借鉴操作系统中的记忆管理原则，设计了分层存储架构，并包含四个关键模块：记忆存储、更新、检索和生成。该架构由短期记忆、中期记忆和长期个人记忆三个层次的存储单元组成。MemoryOS的关键操作包括存储单元之间的动态更新，短期到中期的更新遵循对话链FIFO原则，而中期到长期的更新则采用分段页面组织策略。实验结果表明，MemoryOS在LoCoMo基准测试中，GPT-4o-mini模型的F1和BLEU-1指标分别提高了49.11%和46.18%。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在长期记忆管理方面的不足，现有方法无法有效支持个性化和上下文连贯的交互体验。

**核心思路**：提出MemoryOS，通过分层存储架构和动态更新机制，提升AI代理的记忆管理能力，使其能够更好地处理长期对话。

**技术框架**：MemoryOS的整体架构包括四个主要模块：记忆存储、更新、检索和生成，分为短期记忆、中期记忆和长期个人记忆三个层次。

**关键创新**：MemoryOS的核心创新在于其分层存储和动态更新机制，允许在不同记忆层次之间进行高效的信息传递和更新，显著提升了记忆的个性化和上下文连贯性。

**关键设计**：短期到中期的更新遵循对话链FIFO原则，而中期到长期的更新采用分段页面组织策略，确保信息的有效管理与检索。具体的参数设置和网络结构细节在论文中进行了详细描述。

## 📊 实验亮点

在LoCoMo基准测试中，MemoryOS在GPT-4o-mini模型上实现了F1和BLEU-1指标的显著提升，分别提高了49.11%和46.18%。这些结果表明，MemoryOS在上下文连贯性和个性化记忆保留方面表现出色，验证了其有效性。

## 🎯 应用场景

MemoryOS的研究成果具有广泛的应用潜力，尤其在智能助手、个性化推荐系统和人机交互领域。通过提升AI代理的记忆管理能力，能够显著改善用户体验，实现更自然和个性化的交互。未来，该技术可能推动更复杂的AI系统的发展，使其在长期任务和对话中表现更佳。

## 📄 摘要（原文）

> Large Language Models (LLMs) face a crucial challenge from fixed context windows and inadequate memory management, leading to a severe shortage of long-term memory capabilities and limited personalization in the interactive experience with AI agents. To overcome this challenge, we innovatively propose a Memory Operating System, i.e., MemoryOS, to achieve comprehensive and efficient memory management for AI agents. Inspired by the memory management principles in operating systems, MemoryOS designs a hierarchical storage architecture and consists of four key modules: Memory Storage, Updating, Retrieval, and Generation. Specifically, the architecture comprises three levels of storage units: short-term memory, mid-term memory, and long-term personal memory. Key operations within MemoryOS include dynamic updates between storage units: short-term to mid-term updates follow a dialogue-chain-based FIFO principle, while mid-term to long-term updates use a segmented page organization strategy. Our pioneering MemoryOS enables hierarchical memory integration and dynamic updating. Extensive experiments on the LoCoMo benchmark show an average improvement of 49.11% on F1 and 46.18% on BLEU-1 over the baselines on GPT-4o-mini, showing contextual coherence and personalized memory retention in long conversations. The implementation code is open-sourced at https://github.com/BAI-LAB/MemoryOS.

