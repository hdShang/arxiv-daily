---
layout: default
title: A Lightweight Multi-Expert Generative Language Model System for Engineering Information and Knowledge Extraction
---

# A Lightweight Multi-Expert Generative Language Model System for Engineering Information and Knowledge Extraction

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21109" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21109v1</a>
  <a href="https://arxiv.org/pdf/2505.21109.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21109v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21109v1', 'A Lightweight Multi-Expert Generative Language Model System for Engineering Information and Knowledge Extraction')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bogdan Bogachov, Yaoyao Fiona Zhao

**分类**: cs.CL, cs.AI, cs.CE, cs.IR, cs.LG

**发布日期**: 2025-05-27

**备注**: 10 pages, 4 Figures, 6 Tables. This paper has been accepted to be published in the proceedings of IDETC-CIE 2025

---

## 💡 一句话要点

**提出小型语言图以解决工程信息提取中的计算资源问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生成模型` `领域适应` `轻量级模型` `工程信息提取` `计算资源优化` `小型语言图` `微调技术`

## 📋 核心要点

1. 现有的领域适应方法计算资源消耗大，且生成模型仍存在幻觉问题，尤其在工程领域尤为突出。
2. 本文提出的小型语言图（SLG）通过构建轻量级专家节点，旨在高效解决微调和推理中的计算资源问题。
3. SLG在精确匹配指标上超越传统方法3倍，微调速度提升1.7倍，为中小型企业使用生成AI提供了新机遇。

## 📝 摘要（中文）

尽管近年来大语言模型的领域适应技术取得了进展，但这些方法仍然计算密集，且生成的模型可能出现幻觉问题。现有的适应方法未能优先考虑减少语言模型微调和推理所需的计算资源。本文提出了一种名为小型语言图（SLG）的轻量级适应解决方案，旨在解决上述两个关键挑战。该系统以图的形式构建，每个节点代表一个轻量级专家——一个在特定简洁文本上微调的小语言模型。研究结果表明，SLG在精确匹配指标上超越传统微调方法3倍，且微调过程比大型独立语言模型快1.7倍。这一发现为中小型工程公司自信使用生成AI技术提供了可能，而无需投资昂贵的计算资源。

## 🔬 方法详解

**问题定义**：本文旨在解决现有领域适应方法在微调和推理过程中计算资源消耗过高及模型幻觉问题，尤其是在工程信息生成的场景中。

**核心思路**：提出小型语言图（SLG），通过构建轻量级专家节点，针对特定文本进行微调，从而降低计算资源需求并提高生成文本的准确性。

**技术框架**：SLG系统以图的形式组织，每个节点为一个经过微调的小语言模型，整体架构包括专家节点的选择、微调过程及生成文本的评估模块。

**关键创新**：SLG的主要创新在于其轻量级设计和图结构，使得多个小模型协同工作，显著降低了计算资源需求，与传统的单一大型模型微调方法形成鲜明对比。

**关键设计**：在设计中，专家节点的选择基于特定领域的文本，损失函数采用适应性调整策略，以优化微调效果，确保生成文本的结构性和一致性。

## 📊 实验亮点

实验结果显示，SLG在精确匹配指标上超越传统微调方法3倍，且微调速度提升1.7倍。这些数据表明，SLG在资源效率和生成质量上均有显著提升，为中小型企业提供了可行的AI解决方案。

## 🎯 应用场景

该研究的潜在应用领域包括中小型工程公司在信息提取和知识生成中的实际应用。通过使用SLG，这些公司能够以较低的计算成本利用生成AI技术，提升工作效率和文本生成质量，进而推动工程领域的创新与发展。

## 📄 摘要（原文）

> Despite recent advancements in domain adaptation techniques for large language models, these methods remain computationally intensive, and the resulting models can still exhibit hallucination issues. Most existing adaptation methods do not prioritize reducing the computational resources required for fine-tuning and inference of language models. Hallucination issues have gradually decreased with each new model release. However, they remain prevalent in engineering contexts, where generating well-structured text with minimal errors and inconsistencies is critical. This work introduces a novel approach called the Small Language Graph (SLG), which is a lightweight adaptation solution designed to address the two key challenges outlined above. The system is structured in the form of a graph, where each node represents a lightweight expert - a small language model fine-tuned on specific and concise texts. The results of this study have shown that SLG was able to surpass conventional fine-tuning methods on the Exact Match metric by 3 times. Additionally, the fine-tuning process was 1.7 times faster compared to that of a larger stand-alone language model. These findings introduce a potential for small to medium-sized engineering companies to confidently use generative AI technologies, such as LLMs, without the necessity to invest in expensive computational resources. Also, the graph architecture and the small size of expert nodes offer a possible opportunity for distributed AI systems, thus potentially diverting the global need for expensive centralized compute clusters.

