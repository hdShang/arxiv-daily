---
layout: default
title: "PPMI: Privacy-Preserving LLM Interaction with Socratic Chain-of-Thought Reasoning and Homomorphically Encrypted Vector Databases"
---

# PPMI: Privacy-Preserving LLM Interaction with Socratic Chain-of-Thought Reasoning and Homomorphically Encrypted Vector Databases

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.17336" class="toolbar-btn" target="_blank">📄 arXiv: 2506.17336v3</a>
  <a href="https://arxiv.org/pdf/2506.17336.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.17336v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.17336v3', 'PPMI: Privacy-Preserving LLM Interaction with Socratic Chain-of-Thought Reasoning and Homomorphically Encrypted Vector Databases')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yubeen Bae, Minchan Kim, Jaejin Lee, Sangbum Kim, Jaehyung Kim, Yejin Choi, Niloofar Mireshghallah

**分类**: cs.CR, cs.AI

**发布日期**: 2025-06-19 (更新: 2025-11-01)

**备注**: 29 pages

---

## 💡 一句话要点

**提出PPMI以解决用户隐私保护与LLM交互问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `大型语言模型` `同态加密` `Socratic推理` `数据安全` `语义搜索` `本地模型` `用户数据`

## 📋 核心要点

1. 现有方法在处理用户敏感数据时面临隐私风险，用户不得不在强大模型与本地弱模型之间做出选择。
2. 论文提出了一种新颖的Socratic Chain-of-Thought Reasoning方法，结合同态加密技术，实现了隐私保护的LLM交互。
3. 在LoCoMo长上下文问答基准上，混合框架的表现优于单一使用GPT-4o，提升幅度达到7.1个百分点。

## 📝 摘要（中文）

大型语言模型（LLMs）越来越多地作为个人代理使用，访问敏感用户数据，如日历、电子邮件和医疗记录。用户面临着一个权衡：要么将私人记录发送给强大但不可信的LLM提供商，从而增加暴露风险；要么在可信设备上运行较弱的本地模型。本文提出的Socratic Chain-of-Thought Reasoning方法，首先向强大的不可信LLM发送通用的非私密用户查询，生成Chain-of-Thought（CoT）提示和详细的子查询，而不访问用户数据。接着，利用同态加密向量数据库对用户的私人数据进行加密的语义搜索。最后，将CoT提示和解密后的记录输入本地语言模型，生成最终响应。实验结果表明，该混合框架在LoCoMo长上下文问答基准上，性能比单独使用GPT-4o提升了7.1个百分点。

## 🔬 方法详解

**问题定义**：本文旨在解决用户在使用大型语言模型时面临的隐私保护问题。现有方法往往需要将敏感数据发送给不可信的LLM提供商，增加了用户数据泄露的风险。

**核心思路**：论文提出的核心思路是通过Socratic Chain-of-Thought Reasoning，首先生成非私密的用户查询，然后通过同态加密技术对用户的私人数据进行安全处理，从而在不暴露用户隐私的情况下，利用强大的LLM进行推理。

**技术框架**：整体架构包括三个主要模块：首先，向不可信的LLM发送通用查询以生成CoT提示；其次，利用同态加密向量数据库对用户的私人数据进行加密的语义搜索；最后，将CoT提示和解密后的记录输入本地模型生成最终响应。

**关键创新**：最重要的技术创新在于将强大的LLM与本地弱模型结合，通过分解任务实现隐私保护。这种方法与传统的直接发送用户数据给LLM的方式有本质区别。

**关键设计**：在设计中，采用同态加密技术确保数据在处理过程中的安全性，设置了高效的搜索算法以支持对百万条私人记录的快速检索，同时优化了CoT提示生成的策略以提高响应的准确性和相关性。

## 📊 实验亮点

实验结果显示，混合框架在LoCoMo长上下文问答基准上的表现优于单独使用GPT-4o，提升幅度达到7.1个百分点。这一结果表明，结合强大LLM与本地模型的策略在实际应用中具有显著优势。

## 🎯 应用场景

该研究的潜在应用领域包括个人助理、医疗记录管理和敏感信息处理等场景。通过保护用户隐私，PPMI可以在不牺牲模型性能的情况下，促进用户对AI技术的信任和接受，未来可能推动更广泛的隐私保护技术在各行业的应用。

## 📄 摘要（原文）

> Large language models (LLMs) are increasingly used as personal agents, accessing sensitive user data such as calendars, emails, and medical records. Users currently face a trade-off: They can send private records, many of which are stored in remote databases, to powerful but untrusted LLM providers, increasing their exposure risk. Alternatively, they can run less powerful models locally on trusted devices. We bridge this gap. Our Socratic Chain-of-Thought Reasoning first sends a generic, non-private user query to a powerful, untrusted LLM, which generates a Chain-of-Thought (CoT) prompt and detailed sub-queries without accessing user data. Next, we embed these sub-queries and perform encrypted sub-second semantic search using our Homomorphically Encrypted Vector Database across one million entries of a single user's private data. This represents a realistic scale of personal documents, emails, and records accumulated over years of digital activity. Finally, we feed the CoT prompt and the decrypted records to a local language model and generate the final response. On the LoCoMo long-context QA benchmark, our hybrid framework, combining GPT-4o with a local Llama-3.2-1B model, outperforms using GPT-4o alone by up to 7.1 percentage points. This demonstrates a first step toward systems where tasks are decomposed and split between untrusted strong LLMs and weak local ones, preserving user privacy.

