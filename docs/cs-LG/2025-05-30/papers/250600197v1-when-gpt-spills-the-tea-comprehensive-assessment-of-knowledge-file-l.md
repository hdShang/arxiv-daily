---
layout: default
title: "When GPT Spills the Tea: Comprehensive Assessment of Knowledge File Leakage in GPTs"
---

# When GPT Spills the Tea: Comprehensive Assessment of Knowledge File Leakage in GPTs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.00197" class="toolbar-btn" target="_blank">📄 arXiv: 2506.00197v1</a>
  <a href="https://arxiv.org/pdf/2506.00197.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.00197v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.00197v1', 'When GPT Spills the Tea: Comprehensive Assessment of Knowledge File Leakage in GPTs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xinyue Shen, Yun Shen, Michael Backes, Yang Zhang

**分类**: cs.CR, cs.LG

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出全面评估GPT知识文件泄露风险的方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识文件泄露` `大型语言模型` `数据安全` `风险评估` `特权提升漏洞` `数据流分析` `安全策略`

## 📋 核心要点

1. 现有研究主要集中在通过恶意提示诱导GPT泄露知识文件，但未全面评估其他潜在泄露途径。
2. 本文提出了一种新颖的风险评估工作流程，结合数据安全态势管理（DSPM）理念，系统分析知识文件泄露的多种向量。
3. 通过对大量数据的分析，发现了五种泄露向量，并揭示了高达95.95%的成功率下载原始知识文件的漏洞。

## 📝 摘要（中文）

知识文件在大型语言模型（LLM）代理中被广泛使用，以提高响应质量。然而，关于知识文件潜在泄露的担忧日益增加。现有研究表明，恶意提示可以诱使GPT泄露知识文件内容，但是否存在其他泄露途径仍不确定。本文通过分析651,022个GPT元数据、11,820个数据流和1,466个响应，识别出五种泄露向量，并提出了基于数据安全态势管理（DSPM）的新工作流程，提供了可行的解决方案以保护GPT数据供应链。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型中知识文件泄露的风险，现有方法未能全面识别所有潜在的泄露途径，导致安全隐患。

**核心思路**：通过引入数据安全态势管理（DSPM）理念，构建全面的风险评估框架，分析不同的数据流和泄露向量，以识别和缓解知识文件泄露的风险。

**技术框架**：研究采用了数据流分析的方法，分析了651,022个GPT元数据、11,820个数据流和1,466个响应，识别出五种主要的泄露向量，包括元数据、GPT初始化、检索、沙箱执行环境和提示。

**关键创新**：本研究的创新点在于系统性地识别和分析了多种知识文件泄露向量，尤其是通过激活内置工具Code Interpreter导致的特权提升漏洞，成功率高达95.95%。

**关键设计**：在数据分析过程中，采用了大规模数据集和多维度分析方法，确保了结果的可靠性和全面性，同时提出了针对性强的安全解决方案。

## 📊 实验亮点

实验结果显示，识别出的五种泄露向量中，激活Code Interpreter工具导致的特权提升漏洞具有95.95%的成功率，且28.80%的泄露文件为受版权保护的材料。这些发现强调了知识文件泄露的严重性及其对知识产权的影响。

## 🎯 应用场景

该研究的潜在应用领域包括大型语言模型的安全性提升、知识管理系统的保护以及数据隐私合规性。通过识别和缓解知识文件泄露风险，能够为GPT构建者和平台提供商提供有效的安全策略，确保用户数据的安全性和隐私性。

## 📄 摘要（原文）

> Knowledge files have been widely used in large language model (LLM) agents, such as GPTs, to improve response quality. However, concerns about the potential leakage of knowledge files have grown significantly. Existing studies demonstrate that adversarial prompts can induce GPTs to leak knowledge file content. Yet, it remains uncertain whether additional leakage vectors exist, particularly given the complex data flows across clients, servers, and databases in GPTs. In this paper, we present a comprehensive risk assessment of knowledge file leakage, leveraging a novel workflow inspired by Data Security Posture Management (DSPM). Through the analysis of 651,022 GPT metadata, 11,820 flows, and 1,466 responses, we identify five leakage vectors: metadata, GPT initialization, retrieval, sandboxed execution environments, and prompts. These vectors enable adversaries to extract sensitive knowledge file data such as titles, content, types, and sizes. Notably, the activation of the built-in tool Code Interpreter leads to a privilege escalation vulnerability, enabling adversaries to directly download original knowledge files with a 95.95% success rate. Further analysis reveals that 28.80% of leaked files are copyrighted, including digital copies from major publishers and internal materials from a listed company. In the end, we provide actionable solutions for GPT builders and platform providers to secure the GPT data supply chain.

