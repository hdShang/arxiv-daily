---
layout: default
title: On Path to Multimodal Historical Reasoning: HistBench and HistAgent
---

# On Path to Multimodal Historical Reasoning: HistBench and HistAgent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20246" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20246v3</a>
  <a href="https://arxiv.org/pdf/2505.20246.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20246v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20246v3', 'On Path to Multimodal Historical Reasoning: HistBench and HistAgent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiahao Qiu, Fulian Xiao, Yimin Wang, Yuchen Mao, Yijia Chen, Xinzhe Juan, Shu Zhang, Siran Wang, Xuan Qi, Tongcheng Zhang, Zixin Yao, Jiacheng Guo, Yifu Lu, Charles Argon, Jundi Cui, Daixin Chen, Junran Zhou, Shuyao Zhou, Zhanpeng Zhou, Ling Yang, Shilong Liu, Hongru Wang, Kaixuan Huang, Xun Jiang, Yuming Cao, Yue Chen, Yunfei Chen, Zhengyi Chen, Ruowei Dai, Mengqiu Deng, Jiye Fu, Yunting Gu, Zijie Guan, Zirui Huang, Xiaoyan Ji, Yumeng Jiang, Delong Kong, Haolong Li, Jiaqi Li, Ruipeng Li, Tianze Li, Zhuoran Li, Haixia Lian, Mengyue Lin, Xudong Liu, Jiayi Lu, Jinghan Lu, Wanyu Luo, Ziyue Luo, Zihao Pu, Zhi Qiao, Ruihuan Ren, Liang Wan, Ruixiang Wang, Tianhui Wang, Yang Wang, Zeyu Wang, Zihua Wang, Yujia Wu, Zhaoyi Wu, Hao Xin, Weiao Xing, Ruojun Xiong, Weijie Xu, Yao Shu, Yao Xiao, Xiaorui Yang, Yuchen Yang, Nan Yi, Jiadong Yu, Yangyuxuan Yu, Huiting Zeng, Danni Zhang, Yunjie Zhang, Zhaoyu Zhang, Zhiheng Zhang, Xiaofeng Zheng, Peirong Zhou, Linyan Zhong, Xiaoyin Zong, Ying Zhao, Zhenxin Chen, Lin Ding, Xiaoyu Gao, Bingbing Gong, Yichao Li, Yang Liao, Guang Ma, Tianyuan Ma, Xinrui Sun, Tianyi Wang, Han Xia, Ruobing Xian, Gen Ye, Tengfei Yu, Wentao Zhang, Yuxi Wang, Xi Gao, Mengdi Wang

**分类**: cs.AI, cs.CL

**发布日期**: 2025-05-26 (更新: 2025-06-19)

**备注**: 17 pages, 7 figures

---

## 💡 一句话要点

**提出HistBench和HistAgent以解决历史推理中的多模态挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `历史推理` `多模态学习` `大型语言模型` `OCR技术` `智能体设计` `跨语言分析` `基准测试`

## 📋 核心要点

1. 现有的通用智能体在历史推理任务上表现不佳，缺乏必要的领域专业知识。
2. 本文提出HistBench基准和HistAgent智能体，专注于历史推理的多模态挑战。
3. HistAgent在HistBench上取得了27.54%的pass@1和36.47%的pass@2，显著优于其他通用模型。

## 📝 摘要（中文）

近年来，大型语言模型（LLMs）的进展在多个领域取得了显著进展，但在历史学等人文学科中的能力仍未得到充分探索。历史推理面临独特挑战，包括多模态源解释、时间推理和跨语言分析。为填补这一空白，本文提出了HistBench，一个包含414个高质量问题的新基准，旨在评估AI在历史推理方面的能力。此外，本文还介绍了HistAgent，一个专门针对历史的智能体，配备了OCR、翻译、档案搜索和图像理解等工具。实验结果表明，HistAgent在HistBench上的表现显著优于现有的LLMs和通用智能体。

## 🔬 方法详解

**问题定义**：本文旨在解决现有大型语言模型在历史推理任务中的不足，特别是在多模态信息处理和领域特定知识的缺乏。现有方法在面对复杂的历史材料时表现不佳，无法有效进行时间推理和跨语言分析。

**核心思路**：论文提出HistBench作为评估工具，并设计HistAgent智能体，专门针对历史推理任务，集成了OCR、翻译和图像理解等功能，以提升对历史材料的处理能力。

**技术框架**：HistAgent的整体架构包括多个模块：OCR模块用于文本提取，翻译模块处理多语言文本，档案搜索模块用于获取相关历史资料，图像理解模块则分析历史图像。各模块协同工作，形成一个综合的历史推理系统。

**关键创新**：HistBench的构建和HistAgent的设计是本研究的主要创新。HistBench提供了一个多样化的历史问题集，而HistAgent则通过专门的工具和模块化设计，显著提升了历史推理的准确性和效率。

**关键设计**：HistAgent的设计中，OCR和翻译模块采用了最新的深度学习技术，确保高准确率；档案搜索模块则利用了高效的索引机制，以快速检索相关历史文献。

## 📊 实验亮点

在HistBench基准测试中，HistAgent基于GPT-4o的表现为27.54%的pass@1和36.47%的pass@2，显著优于其他通用模型，如GPT-4o（18.60%）、DeepSeek-R1（14.49%）和Open Deep Research-smolagents（20.29% pass@1和25.12% pass@2），显示出HistAgent在历史推理任务中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括教育、历史研究和文化遗产保护。HistAgent可以帮助历史学者和学生更好地理解和分析历史材料，提高历史研究的效率和准确性。此外，该技术还可用于开发智能教育工具，促进历史知识的传播和学习。

## 📄 摘要（原文）

> Recent advances in large language models (LLMs) have led to remarkable progress across domains, yet their capabilities in the humanities, particularly history, remain underexplored. Historical reasoning poses unique challenges for AI, involving multimodal source interpretation, temporal inference, and cross-linguistic analysis. While general-purpose agents perform well on many existing benchmarks, they lack the domain-specific expertise required to engage with historical materials and questions. To address this gap, we introduce HistBench, a new benchmark of 414 high-quality questions designed to evaluate AI's capacity for historical reasoning and authored by more than 40 expert contributors. The tasks span a wide range of historical problems-from factual retrieval based on primary sources to interpretive analysis of manuscripts and images, to interdisciplinary challenges involving archaeology, linguistics, or cultural history. Furthermore, the benchmark dataset spans 29 ancient and modern languages and covers a wide range of historical periods and world regions. Finding the poor performance of LLMs and other agents on HistBench, we further present HistAgent, a history-specific agent equipped with carefully designed tools for OCR, translation, archival search, and image understanding in History. On HistBench, HistAgent based on GPT-4o achieves an accuracy of 27.54% pass@1 and 36.47% pass@2, significantly outperforming LLMs with online search and generalist agents, including GPT-4o (18.60%), DeepSeek-R1(14.49%) and Open Deep Research-smolagents(20.29% pass@1 and 25.12% pass@2). These results highlight the limitations of existing LLMs and generalist agents and demonstrate the advantages of HistAgent for historical reasoning.

