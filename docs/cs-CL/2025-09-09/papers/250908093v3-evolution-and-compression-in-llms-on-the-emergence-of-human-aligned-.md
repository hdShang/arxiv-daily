---
layout: default
title: "Evolution and compression in LLMs: On the emergence of human-aligned categorization"
---

# Evolution and compression in LLMs: On the emergence of human-aligned categorization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.08093" class="toolbar-btn" target="_blank">📄 arXiv: 2509.08093v3</a>
  <a href="https://arxiv.org/pdf/2509.08093.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.08093v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.08093v3', 'Evolution and compression in LLMs: On the emergence of human-aligned categorization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Nathaniel Imel, Noga Zaslavsky

**分类**: cs.CL

**发布日期**: 2025-09-09 (更新: 2025-12-01)

**备注**: Accepted at CogInterp: Interpreting Cognition in Deep Learning Models Workshop at NeurIPS 2025

---

## 💡 一句话要点

**研究表明，大型语言模型可以通过迭代学习进化出与人类对齐的语义分类系统。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `语义分类` `信息瓶颈` `文化演化` `迭代学习`

## 📋 核心要点

1. 现有大型语言模型未针对信息瓶颈优化，导致其语义系统与人类对齐程度未知。
2. 论文提出迭代上下文语言学习(IICLL)方法，模拟LLM中伪颜色命名系统的文化演变。
3. 实验表明，LLM可以通过IICLL迭代地优化语义系统，使其更接近人类的IB效率。

## 📝 摘要（中文）

大量证据表明，人类的语义类别系统通过信息瓶颈(IB)的复杂性-准确性权衡实现了近乎最优的压缩。大型语言模型(LLM)的训练目标并非如此，这引出了一个问题：LLM是否能够进化出高效的、与人类对齐的语义系统？为了解决这个问题，我们以颜色分类为重点——这是认知类别理论的关键试验台，拥有非常丰富的人类数据——并使用LLM复制了两项有影响力的人类研究。首先，我们进行了一项英语颜色命名研究，表明LLM在复杂性和英语对齐方面差异很大，其中更大的指令调整模型实现了更好的对齐和IB效率。其次，为了测试这些LLM是否仅仅模仿其训练数据中的模式，或者实际上表现出类似人类的、趋向于IB效率的归纳偏置，我们通过一种称为迭代上下文语言学习(IICLL)的方法，在LLM中模拟了伪颜色命名系统的文化演变。我们发现，与人类类似，LLM迭代地将最初随机的系统重构为更高的IB效率。然而，只有具有最强上下文能力的模型(Gemini 2.0)能够重现人类观察到的广泛的近乎最优的IB权衡，而其他最先进的模型则收敛到低复杂度的解决方案。这些发现表明，与人类语义效率的基本原理相同，与人类对齐的语义类别可以在LLM中涌现。

## 🔬 方法详解

**问题定义**：论文旨在研究大型语言模型(LLM)是否能够像人类一样，通过学习和演化，形成高效且与人类认知对齐的语义分类系统。现有LLM的训练目标并非直接针对语义压缩和人类对齐，因此其语义系统的效率和对齐程度是未知的，需要进行深入研究。

**核心思路**：论文的核心思路是模拟人类文化演化的过程，通过迭代地让LLM学习和改进颜色命名系统，观察其是否会自发地趋向于信息瓶颈(IB)理论所预测的优化状态。这种方法模拟了人类语言的演化过程，可以揭示LLM是否具有类似人类的归纳偏置。

**技术框架**：论文的技术框架主要包含两个部分：1) 英语颜色命名研究：评估LLM在英语颜色命名任务中的表现，衡量其复杂性和与人类的对齐程度。2) 迭代上下文语言学习(IICLL)：通过迭代地让LLM学习和改进伪颜色命名系统，模拟文化演化过程。IICLL包含以下步骤：a) 初始化一个随机的颜色命名系统。b) 使用LLM根据上下文学习该系统。c) 使用学习后的系统生成新的颜色命名数据。d) 重复步骤b和c，进行多次迭代。

**关键创新**：论文的关键创新在于提出了迭代上下文语言学习(IICLL)方法，这是一种模拟文化演化过程的创新方法，可以用于研究LLM的语义学习和演化能力。通过IICLL，研究人员可以观察LLM是否具有类似人类的归纳偏置，以及其语义系统是否会自发地趋向于优化状态。

**关键设计**：在IICLL中，关键的设计包括：1) 颜色空间的表示：使用CIE Lab颜色空间来表示颜色。2) 颜色命名系统的表示：使用一个映射表，将颜色映射到名称。3) LLM的学习方式：使用上下文学习，让LLM根据上下文学习颜色命名系统。4) 迭代次数：进行多次迭代，以观察LLM的语义系统是否会趋向于优化状态。

## 📊 实验亮点

实验结果表明，较大的指令调整模型在英语颜色命名任务中表现出更好的对齐和IB效率。通过IICLL，LLM能够迭代地优化语义系统，使其更接近人类的IB效率。Gemini 2.0模型能够重现人类观察到的广泛的近乎最优的IB权衡，而其他模型则收敛到低复杂度的解决方案。

## 🎯 应用场景

该研究成果可应用于提升大型语言模型的语义理解能力，使其更符合人类认知习惯。通过优化LLM的语义表示，可以提高其在自然语言处理任务中的性能，例如文本分类、信息检索和机器翻译。此外，该研究还有助于理解人类语言的演化机制。

## 📄 摘要（原文）

> Converging evidence suggests that human systems of semantic categories achieve near-optimal compression via the Information Bottleneck (IB) complexity-accuracy tradeoff. Large language models (LLMs) are not trained for this objective, which raises the question: are LLMs capable of evolving efficient human-aligned semantic systems? To address this question, we focus on color categorization -- a key testbed of cognitive theories of categorization with uniquely rich human data -- and replicate with LLMs two influential human studies. First, we conduct an English color-naming study, showing that LLMs vary widely in their complexity and English-alignment, with larger instruction-tuned models achieving better alignment and IB-efficiency. Second, to test whether these LLMs simply mimic patterns in their training data or actually exhibit a human-like inductive bias toward IB-efficiency, we simulate cultural evolution of pseudo color-naming systems in LLMs via a method we refer to as Iterated in-Context Language Learning (IICLL). We find that akin to humans, LLMs iteratively restructure initially random systems towards greater IB-efficiency. However, only a model with strongest in-context capabilities (Gemini 2.0) is able to recapitulate the wide range of near-optimal IB-tradeoffs observed in humans, while other state-of-the-art models converge to low-complexity solutions. These findings demonstrate how human-aligned semantic categories can emerge in LLMs via the same fundamental principle that underlies semantic efficiency in humans.

