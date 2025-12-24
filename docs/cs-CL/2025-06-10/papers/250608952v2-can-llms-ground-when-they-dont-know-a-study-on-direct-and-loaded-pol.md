---
layout: default
title: "Can LLMs Ground when they (Don't) Know: A Study on Direct and Loaded Political Questions"
---

# Can LLMs Ground when they (Don't) Know: A Study on Direct and Loaded Political Questions

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.08952" class="toolbar-btn" target="_blank">📄 arXiv: 2506.08952v2</a>
  <a href="https://arxiv.org/pdf/2506.08952.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.08952v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.08952v2', 'Can LLMs Ground when they (Don\'t) Know: A Study on Direct and Loaded Political Questions')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Clara Lachenmaier, Judith Sieker, Sina Zarrieß

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-10 (更新: 2025-06-11)

**备注**: Preprint accepted at ACL Main Conference 2025

---

## 💡 一句话要点

**研究大型语言模型在政治问题中的信息基础能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `政治对话` `误信息` `共同基础` `知识管理` `加载问题` `用户信念纠正`

## 📋 核心要点

1. 核心问题：现有大型语言模型在处理政治领域的知识问题时，常常无法有效管理共同基础，导致误信息传播。
2. 方法要点：本文通过分析LLMs在回答直接和加载问题时的表现，探讨其在知识缺失情况下的基础管理能力。
3. 实验或效果：研究发现LLMs在主动纠正用户错误信念方面存在显著挑战，影响其在政治对话中的有效性。

## 📝 摘要（中文）

人类之间的交流依赖于对话基础，使对话者即使在知识不完备的情况下也能达成共识。本文研究大型语言模型（LLMs）在知识缺失时如何管理共同基础，特别关注政治领域中的事实，因为该领域存在误信息和基础失败的高风险。我们考察LLMs回答直接知识问题和假设误信息的加载问题的能力，并评估加载问题是否促使LLMs主动纠正用户的错误信念。研究结果揭示了LLMs在参与基础建设和拒绝错误用户信念方面面临的重大挑战，提出了对其在政治话语中减轻误信息作用的担忧。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在政治领域中处理知识问题时的共同基础管理能力不足的问题。现有方法在面对加载问题时，往往无法有效纠正用户的错误信念，导致误信息的传播。

**核心思路**：论文的核心思路是通过对直接知识问题和加载问题的比较分析，评估LLMs在知识缺失情况下的表现，探讨其主动纠正错误信念的能力。这样的设计旨在揭示LLMs在政治对话中的潜在局限性。

**技术框架**：研究采用了对比实验的方法，首先设计了直接知识问题和加载问题的问卷，然后通过LLMs进行回答，最后分析其回答的准确性和对用户信念的影响。主要模块包括问题设计、模型回答和结果分析。

**关键创新**：本文的创新点在于首次系统性地探讨了LLMs在面对加载问题时的表现，特别是其在主动纠正用户错误信念方面的能力，与现有研究相比，提供了更深入的理解。

**关键设计**：研究中采用了多种问题类型，并对LLMs的回答进行了定量和定性的分析，关注其在不同知识水平和政治偏见下的表现差异。

## 📊 实验亮点

实验结果显示，LLMs在处理加载问题时，主动纠正用户错误信念的能力显著不足，尤其在知识缺失的情况下，表现出较高的误信息传播风险。这一发现对LLMs在政治话语中的应用提出了重要警示。

## 🎯 应用场景

该研究的潜在应用领域包括政治传播、社交媒体内容审核和教育领域，能够为设计更有效的对话系统提供理论支持。通过改善LLMs在政治对话中的表现，可以帮助减少误信息的传播，提高公众对政治信息的理解和判断能力。

## 📄 摘要（原文）

> Communication among humans relies on conversational grounding, allowing interlocutors to reach mutual understanding even when they do not have perfect knowledge and must resolve discrepancies in each other's beliefs. This paper investigates how large language models (LLMs) manage common ground in cases where they (don't) possess knowledge, focusing on facts in the political domain where the risk of misinformation and grounding failure is high. We examine the ability of LLMs to answer direct knowledge questions and loaded questions that presuppose misinformation. We evaluate whether loaded questions lead LLMs to engage in active grounding and correct false user beliefs, in connection to their level of knowledge and their political bias. Our findings highlight significant challenges in LLMs' ability to engage in grounding and reject false user beliefs, raising concerns about their role in mitigating misinformation in political discourse.

