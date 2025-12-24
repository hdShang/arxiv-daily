---
layout: default
title: "AutoSchemaKG: Autonomous Knowledge Graph Construction through Dynamic Schema Induction from Web-Scale Corpora"
---

# AutoSchemaKG: Autonomous Knowledge Graph Construction through Dynamic Schema Induction from Web-Scale Corpora

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23628" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23628v3</a>
  <a href="https://arxiv.org/pdf/2505.23628.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23628v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23628v3', 'AutoSchemaKG: Autonomous Knowledge Graph Construction through Dynamic Schema Induction from Web-Scale Corpora')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiaxin Bai, Wei Fan, Qi Hu, Qing Zong, Chunyang Li, Hong Ting Tsang, Hongyu Luo, Yauwai Yim, Haoyu Huang, Xiao Zhou, Feng Qin, Tianshi Zheng, Xi Peng, Xin Yao, Huiwen Yang, Leijie Wu, Yi Ji, Gong Zhang, Renhai Chen, Yangqiu Song

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-29 (更新: 2025-08-01)

**备注**: 9 pages, preprint, code: https://github.com/HKUST-KnowComp/AutoSchemaKG

---

## 💡 一句话要点

**提出AutoSchemaKG以实现自主知识图谱构建**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `知识图谱` `自主构建` `模式诱导` `大型语言模型` `信息提取` `多跳问答` `语义对齐`

## 📋 核心要点

1. 现有知识图谱构建方法依赖于预定义模式，限制了其灵活性和适应性。
2. AutoSchemaKG通过大型语言模型自动提取知识三元组并诱导模式，实现了知识图谱的自主构建。
3. 实验结果显示，该方法在多跳问答任务上优于现有基线，并且模式诱导与人工模式的语义对齐率达到92%。

## 📝 摘要（中文）

我们提出了AutoSchemaKG，一个完全自主的知识图谱构建框架，消除了对预定义模式的需求。该系统利用大型语言模型同时从文本中提取知识三元组并直接诱导全面的模式，建模实体和事件，并通过概念化将实例组织成语义类别。处理超过5000万份文档，我们构建了ATLAS（自动三元组链接和模式诱导），一个包含9亿多个节点和59亿条边的知识图谱。该方法在多跳问答任务上超越了最先进的基线，并增强了大型语言模型的事实性。值得注意的是，我们的模式诱导在没有人工干预的情况下实现了92%的语义对齐，证明了动态诱导模式的十亿级知识图谱能够有效补充大型语言模型中的参数知识。

## 🔬 方法详解

**问题定义**：本论文旨在解决知识图谱构建中对预定义模式的依赖问题。现有方法通常需要人工设计模式，限制了知识图谱的灵活性和扩展性。

**核心思路**：AutoSchemaKG的核心思路是利用大型语言模型从文本中自动提取知识三元组，并动态诱导模式。这种设计使得知识图谱能够根据实际数据自动调整，提升了构建效率和准确性。

**技术框架**：该框架包括多个主要模块：首先是文本处理模块，负责从大规模文档中提取信息；其次是知识三元组提取模块，利用语言模型识别实体和事件；最后是模式诱导模块，将提取的实例组织成语义类别。

**关键创新**：最重要的技术创新在于实现了无人工干预的模式诱导，且在语义对齐上达到了92%的高水平。这一创新与传统方法的本质区别在于其完全自主性和动态适应性。

**关键设计**：在技术细节上，系统采用了特定的损失函数来优化三元组提取的准确性，并设计了适应性强的网络结构，以支持大规模数据处理和模式诱导。

## 📊 实验亮点

实验结果表明，AutoSchemaKG在多跳问答任务上超越了现有最先进的基线，且在知识图谱构建中实现了92%的语义对齐率，显示出其在知识提取和模式诱导方面的显著提升。

## 🎯 应用场景

该研究的潜在应用领域包括智能问答系统、信息检索、数据挖掘等。通过实现自主知识图谱构建，AutoSchemaKG能够在快速变化的知识环境中保持信息的时效性和准确性，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> We present AutoSchemaKG, a framework for fully autonomous knowledge graph construction that eliminates the need for predefined schemas. Our system leverages large language models to simultaneously extract knowledge triples and induce comprehensive schemas directly from text, modeling both entities and events while employing conceptualization to organize instances into semantic categories. Processing over 50 million documents, we construct ATLAS (Automated Triple Linking And Schema induction), a family of knowledge graphs with 900+ million nodes and 5.9 billion edges. This approach outperforms state-of-the-art baselines on multi-hop QA tasks and enhances LLM factuality. Notably, our schema induction achieves 92\% semantic alignment with human-crafted schemas with zero manual intervention, demonstrating that billion-scale knowledge graphs with dynamically induced schemas can effectively complement parametric knowledge in large language models.

