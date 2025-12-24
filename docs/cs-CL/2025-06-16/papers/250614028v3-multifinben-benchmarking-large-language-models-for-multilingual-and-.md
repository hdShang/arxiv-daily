---
layout: default
title: "MultiFinBen: Benchmarking Large Language Models for Multilingual and Multimodal Financial Application"
---

# MultiFinBen: Benchmarking Large Language Models for Multilingual and Multimodal Financial Application

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.14028" class="toolbar-btn" target="_blank">📄 arXiv: 2506.14028v3</a>
  <a href="https://arxiv.org/pdf/2506.14028.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.14028v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.14028v3', 'MultiFinBen: Benchmarking Large Language Models for Multilingual and Multimodal Financial Application')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xueqing Peng, Lingfei Qian, Yan Wang, Ruoyu Xiang, Yueru He, Yang Ren, Mingyang Jiang, Vincent Jim Zhang, Yuqing Guo, Jeff Zhao, Huan He, Yi Han, Yun Feng, Yuechen Jiang, Yupeng Cao, Haohang Li, Yangyang Yu, Xiaoyu Wang, Penglei Gao, Shengyuan Lin, Keyi Wang, Shanshan Yang, Yilun Zhao, Zhiwei Liu, Peng Lu, Jerry Huang, Suyuchen Wang, Triantafillos Papadopoulos, Polydoros Giannouris, Efstathia Soufleri, Nuo Chen, Zhiyang Deng, Heming Fu, Yijia Zhao, Mingquan Lin, Meikang Qiu, Kaleb E Smith, Arman Cohan, Xiao-Yang Liu, Jimin Huang, Guojun Xiong, Alejandro Lopez-Lira, Xi Chen, Junichi Tsujii, Jian-Yun Nie, Sophia Ananiadou, Qianqian Xie

**分类**: cs.CL

**发布日期**: 2025-06-16 (更新: 2025-10-11)

---

## 💡 一句话要点

**提出MultiFinBen以解决多语言多模态金融分析评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多语言处理` `多模态分析` `金融推理` `OCR技术` `基准评估`

## 📋 核心要点

1. 现有的金融分析评估方法主要集中在单一语言和文本数据，缺乏对多语言和多模态信息的综合评估。
2. 论文提出MultiFinBen基准，结合多语言和多模态数据，设计了多语言金融推理和金融OCR两大任务，以提升评估的全面性和准确性。
3. 实验结果显示，当前最先进的多模态模型在多语言环境下表现不佳，整体得分仅为46.01%，揭示了该领域的研究空白和改进空间。

## 📝 摘要（中文）

现实世界的金融分析涉及多种语言和模态的信息，从报告和新闻到扫描文件和会议录音。然而，现有的大型语言模型（LLMs）在金融领域的评估大多仅限于文本、单语言，并且现有模型的表现已趋于饱和。为了解决这些问题，我们提出了MultiFinBen，这是首个专家注释的多语言（五种语言）和多模态（文本、视觉、音频）基准，用于在真实金融环境中评估LLMs。MultiFinBen引入了两个新的任务系列：多语言金融推理和金融OCR。通过对21个领先的LLMs进行评估，发现即使是前沿的多模态模型如GPT-4o在整体表现上也仅达到46.01%。这些发现揭示了在多语言、多模态和专家级金融推理方面的持续局限性。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有金融分析评估方法在多语言和多模态数据处理上的不足，尤其是缺乏对跨语言和多模态信息的有效整合。

**核心思路**：通过构建MultiFinBen基准，论文引入了多语言金融推理和金融OCR任务，旨在全面评估LLMs在真实金融场景中的表现，特别是跨语言和多模态的能力。

**技术框架**：MultiFinBen的整体架构包括数据收集、任务设计、模型评估和结果分析四个主要模块。数据收集阶段涵盖多种语言和模态的信息，任务设计则聚焦于金融推理和OCR。

**关键创新**：MultiFinBen的最大创新在于其多语言和多模态的结合，尤其是在金融领域的应用上，填补了现有评估方法的空白，并提供了结构化的、难度感知的数据选择策略。

**关键设计**：在数据选择过程中，论文采用了基于模型表现的难度感知选择策略，确保评估任务的平衡性，并去除了冗余任务，以提升评估的有效性和挑战性。具体的参数设置和损失函数设计未在摘要中详细说明，需参考完整论文。

## 📊 实验亮点

实验结果显示，21个领先的LLMs在MultiFinBen基准上的整体得分仅为46.01%，其中视觉和音频任务表现较强，但在多语言设置下显著下降。这一发现揭示了当前多模态模型在处理多语言金融信息时的局限性，强调了未来研究的必要性。

## 🎯 应用场景

该研究的潜在应用领域包括金融分析、投资决策支持和跨国公司的财务报告分析。通过提供多语言和多模态的评估基准，MultiFinBen能够帮助研究人员和从业者更好地理解和应用大型语言模型在复杂金融环境中的能力，推动相关技术的进一步发展。

## 📄 摘要（原文）

> Real-world financial analysis involves information across multiple languages and modalities, from reports and news to scanned filings and meeting recordings. Yet most existing evaluations of LLMs in finance remain text-only, monolingual, and largely saturated by current models. To bridge these gaps, we present MultiFinBen, the first expert-annotated multilingual (five languages) and multimodal (text, vision, audio) benchmark for evaluating LLMs in realistic financial contexts. MultiFinBen introduces two new task families: multilingual financial reasoning, which tests cross-lingual evidence integration from filings and news, and financial OCR, which extracts structured text from scanned documents containing tables and charts. Rather than aggregating all available datasets, we apply a structured, difficulty-aware selection based on advanced model performance, ensuring balanced challenge and removing redundant tasks. Evaluating 21 leading LLMs shows that even frontier multimodal models like GPT-4o achieve only 46.01% overall, stronger on vision and audio but dropping sharply in multilingual settings. These findings expose persistent limitations in multilingual, multimodal, and expert-level financial reasoning. All datasets, evaluation scripts, and leaderboards are publicly released.

