---
layout: default
title: "Chiron-o1: Igniting Multimodal Large Language Models towards Generalizable Medical Reasoning via Mentor-Intern Collaborative Search"
---

# Chiron-o1: Igniting Multimodal Large Language Models towards Generalizable Medical Reasoning via Mentor-Intern Collaborative Search

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16962" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16962v2</a>
  <a href="https://arxiv.org/pdf/2506.16962.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16962v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16962v2', 'Chiron-o1: Igniting Multimodal Large Language Models towards Generalizable Medical Reasoning via Mentor-Intern Collaborative Search')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haoran Sun, Yankai Jiang, Wenjie Lou, Yujie Zhang, Wenjie Li, Lilong Wang, Mianxin Liu, Lei Liu, Xiaosong Wang

**分类**: cs.CV, cs.AI, cs.CL

**发布日期**: 2025-06-20 (更新: 2025-10-22)

**🔗 代码/项目**: [GITHUB](https://github.com/manglu097/Chiron-o1)

---

## 💡 一句话要点

**提出MICS以解决医疗多模态大语言模型推理能力不足的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态大语言模型` `医疗推理` `思维链训练` `协作搜索` `视觉问答` `课程学习` `推理路径优化`

## 📋 核心要点

1. 现有方法在医疗领域的推理能力不足，缺乏有效的推理路径搜索和评估框架。
2. 提出导师-实习生协作搜索（MICS），通过导师模型初始化推理，实习生模型继续思考并选择最佳路径。
3. Chiron-o1在多个医疗视觉问答和推理基准上表现优异，达到了最先进的性能，展示了MICS的有效性。

## 📝 摘要（中文）

多模态大语言模型（MLLMs）在一般任务上展现出强大的推理能力，但在医疗领域的应用仍处于初级阶段。构建思维链（CoT）训练数据对于增强医疗MLLMs的推理能力至关重要。然而，现有方法在搜索和评估有效推理路径方面缺乏全面框架。为此，本文提出了一种新颖的推理路径搜索方案——导师-实习生协作搜索（MICS），以生成严谨有效的医疗CoT数据。MICS通过导师模型逐步初始化推理，随后促使每个实习生模型沿着这些路径继续思考，最终根据多个实习生模型的整体推理表现选择最佳推理路径。最终，我们构建了一个多任务医疗推理数据集MMRP，以及通过课程学习策略设计的新医疗MLLM——Chiron-o1，具备强大的视觉问答和可推广推理能力。实验表明，Chiron-o1在使用MICS构建的CoT数据集上训练后，在多个医疗视觉问答和推理基准上达到了最先进的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决医疗多模态大语言模型在推理能力方面的不足，现有方法缺乏有效的推理路径搜索和评估机制，导致生成的思维链数据质量不高。

**核心思路**：提出导师-实习生协作搜索（MICS），通过导师模型逐步引导推理过程，实习生模型在此基础上进行深入思考，最终选择最佳推理路径以提高推理质量。

**技术框架**：MICS的整体架构包括三个主要阶段：首先，使用导师模型初始化推理；其次，实习生模型在导师的引导下继续推理；最后，通过MICS-Score评估并选择最佳推理路径。

**关键创新**：MICS的创新在于其协作搜索机制，通过导师与实习生的互动，显著提高了推理路径的质量和有效性，与传统方法相比，提供了更系统的推理路径生成方式。

**关键设计**：在MICS中，MICS-Score作为评估指标，综合考虑多个实习生模型的推理表现，确保选择的推理路径具有较高的质量。此外，数据集MMRP的构建采用了分级难度设计，以便于多任务学习。

## 📊 实验亮点

实验结果表明，Chiron-o1在多个医疗视觉问答和推理基准上达到了最先进的性能，相较于现有基线，推理准确率提升了XX%，展示了MICS方法的有效性和优越性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断支持系统、智能医疗助手和医学教育等。通过提升医疗多模态大语言模型的推理能力，能够为医生提供更准确的决策支持，改善患者的诊疗体验，未来可能对医疗行业产生深远影响。

## 📄 摘要（原文）

> Multimodal large language models (MLLMs) have begun to demonstrate robust reasoning capabilities on general tasks, yet their application in the medical domain remains in its early stages. Constructing chain-of-thought (CoT) training data is essential for bolstering the reasoning abilities of medical MLLMs. However, existing approaches exhibit a deficiency in offering a comprehensive framework for searching and evaluating effective reasoning paths towards critical diagnosis. To address this challenge, we propose Mentor-Intern Collaborative Search (MICS), a novel reasoning-path searching scheme to generate rigorous and effective medical CoT data. MICS first leverages mentor models to initialize the reasoning, one step at a time, then prompts each intern model to continue the thinking along those initiated paths, and finally selects the optimal reasoning path according to the overall reasoning performance of multiple intern models. The reasoning performance is determined by an MICS-Score, which assesses the quality of generated reasoning paths. Eventually, we construct MMRP, a multi-task medical reasoning dataset with ranked difficulty, and Chiron-o1, a new medical MLLM devised via a curriculum learning strategy, with robust visual question-answering and generalizable reasoning capabilities. Extensive experiments demonstrate that Chiron-o1, trained on our CoT dataset constructed using MICS, achieves state-of-the-art performance across a list of medical visual question answering and reasoning benchmarks. Codes are available at https://github.com/manglu097/Chiron-o1

