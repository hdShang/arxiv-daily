---
layout: default
title: What's in a prompt? Language models encode literary style in prompt embeddings
---

# What's in a prompt? Language models encode literary style in prompt embeddings

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.17071" class="toolbar-btn" target="_blank">📄 arXiv: 2505.17071v1</a>
  <a href="https://arxiv.org/pdf/2505.17071.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.17071v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.17071v1', 'What\'s in a prompt? Language models encode literary style in prompt embeddings')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Raphaël Sarfati, Haley Moller, Toni J. B. Liu, Nicolas Boullé, Christopher Earls

**分类**: cs.CL

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**提出通过提示嵌入分析文学风格的语言模型方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `语言模型` `提示嵌入` `文学风格` `深层表示` `作者归属` `潜在空间` `信息处理`

## 📋 核心要点

1. 现有研究主要集中在单词的概念内容与其向量表示之间的关系，缺乏对整个提示信息的深入分析。
2. 本文通过分析文学作品，提出了提示嵌入中包含非具体信息的观点，揭示了深层表示的复杂性。
3. 实验结果显示，不同作者的作品在潜在空间中呈现出明显的风格特征，为作者归属和文学分析提供了新的视角。

## 📝 摘要（中文）

大型语言模型使用高维潜在空间来编码和处理文本信息。尽管已有研究探讨了单词的概念内容如何转化为其向量表示之间的几何关系，但对整个提示信息如何在变换层的作用下被浓缩为单个嵌入的分析相对较少。本文通过文学作品展示了提示的非具体、抽象方面的信息如何在深层表示中被编码。我们观察到，不同小说的短摘录在潜在空间中独立于其预测的下一个标记而分离，且同一作者的书籍嵌入比不同作者的书籍更为纠缠，表明嵌入编码了风格特征。这种风格几何的发现可能在作者归属和文学分析中具有应用价值，同时揭示了语言模型在信息处理和压缩方面的复杂性。

## 🔬 方法详解

**问题定义**：本文旨在探讨大型语言模型如何在提示嵌入中编码文学风格，现有方法未能充分分析提示信息的深层次特征。

**核心思路**：通过使用文学作品的短摘录，研究提示的非具体信息如何在深层表示中被编码，揭示其在潜在空间中的几何特征。

**技术框架**：研究采用变换器模型对短摘录进行处理，分析其在潜在空间中的分布情况，主要模块包括文本编码、嵌入生成和潜在空间分析。

**关键创新**：本文的创新在于首次系统性地分析了提示嵌入中风格信息的几何特征，揭示了不同作者作品之间的风格纠缠现象。

**关键设计**：实验中使用了10到100个标记的短摘录，采用了标准的变换器架构，重点关注嵌入的相似性和分布特征。通过对比不同作者的作品，分析其在潜在空间中的表现。

## 📊 实验亮点

实验结果表明，不同作者的短摘录在潜在空间中呈现出显著的分离现象，且同一作者的作品嵌入比不同作者的作品更为纠缠。这一发现不仅验证了嵌入中风格特征的存在，也为作者归属提供了新的实证支持。

## 🎯 应用场景

该研究的潜在应用领域包括作者归属分析和文学作品的风格研究。通过对提示嵌入的深入分析，能够帮助研究人员更好地理解文本的风格特征，并为文学批评提供新的工具和视角。未来，该方法可能在文本生成和创作辅助工具中发挥重要作用。

## 📄 摘要（原文）

> Large language models use high-dimensional latent spaces to encode and process textual information. Much work has investigated how the conceptual content of words translates into geometrical relationships between their vector representations. Fewer studies analyze how the cumulative information of an entire prompt becomes condensed into individual embeddings under the action of transformer layers. We use literary pieces to show that information about intangible, rather than factual, aspects of the prompt are contained in deep representations. We observe that short excerpts (10 - 100 tokens) from different novels separate in the latent space independently from what next-token prediction they converge towards. Ensembles from books from the same authors are much more entangled than across authors, suggesting that embeddings encode stylistic features. This geometry of style may have applications for authorship attribution and literary analysis, but most importantly reveals the sophistication of information processing and compression accomplished by language models.

