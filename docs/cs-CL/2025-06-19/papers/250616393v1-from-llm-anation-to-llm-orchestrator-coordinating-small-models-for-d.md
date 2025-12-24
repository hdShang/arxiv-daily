---
layout: default
title: "From LLM-anation to LLM-orchestrator: Coordinating Small Models for Data Labeling"
---

# From LLM-anation to LLM-orchestrator: Coordinating Small Models for Data Labeling

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16393" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16393v1</a>
  <a href="https://arxiv.org/pdf/2506.16393.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16393v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16393v1', 'From LLM-anation to LLM-orchestrator: Coordinating Small Models for Data Labeling')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yao Lu, Zhaiyuan Ji, Jiawei Du, Yu Shanqing, Qi Xuan, Tianyi Zhou

**分类**: cs.CL, cs.AI

**发布日期**: 2025-06-19

**🔗 代码/项目**: [GITHUB](https://github.com/Zhaiyuan-Ji/AutoAnnotator)

---

## 💡 一句话要点

**提出多模型协作注释框架AutoAnnotator以解决大语言模型成本高和精度低的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模型协作` `自动注释` `小语言模型` `大语言模型` `强化学习` `文本分类` `成本优化`

## 📋 核心要点

1. 现有大语言模型在大规模注释中的成本高昂，且在细粒度语义理解任务中的准确性低于小语言模型。
2. 提出的AutoAnnotator框架通过多模型协作注释，利用元控制器选择和优化小语言模型的注释效果。
3. 实验结果显示，AutoAnnotator在多种注释设置下性能优越，注释成本降低74.15%，准确性提升6.21%。

## 📝 摘要（中文）

尽管基于大语言模型（LLMs）的注释范式近年来取得了显著突破，但其实际应用仍面临两个核心瓶颈：一是大规模注释时调用商业API的成本非常高；二是在需要细粒度语义理解的场景中，如情感分类和毒性分类，LLMs的注释准确性甚至低于专门针对该领域的小语言模型（SLMs）。为了解决这些问题，本文提出了一种新的多模型协作注释范式，并基于此设计了一个全自动注释框架AutoAnnotator。该框架由两个层次组成，上层的元控制器利用LLMs的生成和推理能力选择SLMs进行注释，并自动生成注释代码和验证困难样本；下层的任务专家层由多个SLMs通过多模型投票进行注释。实验表明，AutoAnnotator在多种设置下均优于现有的开源/API LLMs，并显著降低了注释成本。

## 🔬 方法详解

**问题定义**：本文旨在解决大语言模型在大规模注释中的高成本和在细粒度语义理解任务中的低准确性问题。现有方法在这些场景中表现不佳，无法满足实际需求。

**核心思路**：论文提出的核心思路是通过多模型协作注释，利用大语言模型的生成和推理能力来优化小语言模型的选择和使用，从而提高注释的效率和准确性。

**技术框架**：AutoAnnotator框架分为两个层次：上层的元控制器负责选择合适的小语言模型进行注释，并生成注释代码；下层的任务专家层由多个小语言模型组成，通过多模型投票进行最终注释。

**关键创新**：最重要的创新点在于引入了元控制器层，通过对困难样本的二次审核，利用强化学习策略对小语言模型进行阶段性微调，从而提升其泛化能力。这一设计与传统的单一模型注释方法有本质区别。

**关键设计**：在框架中，元控制器的选择机制和困难样本的处理策略是关键设计，此外，采用了持续学习策略来微调小语言模型，以适应不断变化的注释需求。

## 📊 实验亮点

实验结果表明，AutoAnnotator在零-shot、one-shot、链式推理（CoT）和多数投票设置下均优于现有的开源/API LLMs，注释成本相比直接使用GPT-3.5-turbo降低了74.15%，同时准确性提升了6.21%。

## 🎯 应用场景

该研究的潜在应用领域包括社交媒体内容审核、情感分析、在线评论分类等需要高效且准确的文本注释的场景。通过降低注释成本和提高准确性，AutoAnnotator能够为企业和研究机构提供更具成本效益的解决方案，推动相关领域的发展。

## 📄 摘要（原文）

> Although the annotation paradigm based on Large Language Models (LLMs) has made significant breakthroughs in recent years, its actual deployment still has two core bottlenecks: first, the cost of calling commercial APIs in large-scale annotation is very expensive; second, in scenarios that require fine-grained semantic understanding, such as sentiment classification and toxicity classification, the annotation accuracy of LLMs is even lower than that of Small Language Models (SLMs) dedicated to this field. To address these problems, we propose a new paradigm of multi-model cooperative annotation and design a fully automatic annotation framework AutoAnnotator based on this. Specifically, AutoAnnotator consists of two layers. The upper-level meta-controller layer uses the generation and reasoning capabilities of LLMs to select SLMs for annotation, automatically generate annotation code and verify difficult samples; the lower-level task-specialist layer consists of multiple SLMs that perform annotation through multi-model voting. In addition, we use the difficult samples obtained by the secondary review of the meta-controller layer as the reinforcement learning set and fine-tune the SLMs in stages through a continual learning strategy, thereby improving the generalization of SLMs. Extensive experiments show that AutoAnnotator outperforms existing open-source/API LLMs in zero-shot, one-shot, CoT, and majority voting settings. Notably, AutoAnnotator reduces the annotation cost by 74.15% compared to directly annotating with GPT-3.5-turbo, while still improving the accuracy by 6.21%. Project page: https://github.com/Zhaiyuan-Ji/AutoAnnotator.

