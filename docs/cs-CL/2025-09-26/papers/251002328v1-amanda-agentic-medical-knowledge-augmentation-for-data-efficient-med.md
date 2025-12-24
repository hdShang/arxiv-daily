---
layout: default
title: "AMANDA: Agentic Medical Knowledge Augmentation for Data-Efficient Medical Visual Question Answering"
---

# AMANDA: Agentic Medical Knowledge Augmentation for Data-Efficient Medical Visual Question Answering

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.02328" class="toolbar-btn" target="_blank">📄 arXiv: 2510.02328v1</a>
  <a href="https://arxiv.org/pdf/2510.02328.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.02328v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.02328v1', 'AMANDA: Agentic Medical Knowledge Augmentation for Data-Efficient Medical Visual Question Answering')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziqing Wang, Chengsheng Mao, Xiaole Wen, Yuan Luo, Kaize Ding

**分类**: cs.CL, cs.AI, cs.MA

**发布日期**: 2025-09-26

**备注**: EMNLP Findings

**🔗 代码/项目**: [GITHUB](https://github.com/REAL-Lab-NU/AMANDA)

---

## 💡 一句话要点

**提出AMANDA，利用LLM Agent进行医学知识增强，解决Med-VQA在低资源下的推理瓶颈。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学视觉问答` `多模态学习` `大型语言模型` `知识增强` `低资源学习` `智能Agent` `生物医学知识图谱`

## 📋 核心要点

1. 现有Med-MLLM在低资源Med-VQA任务中，面临内在的图像细节忽略和外在的医学知识缺乏的双重推理瓶颈。
2. AMANDA框架利用LLM agent，通过问题分解和知识图谱检索，实现医学知识的有效增强，无需额外训练。
3. 实验结果表明，AMANDA在多个Med-VQA基准测试中，零样本和少样本设置下均取得了显著的性能提升。

## 📝 摘要（中文）

医学多模态大型语言模型(Med-MLLMs)在医学视觉问答(Med-VQA)方面展现出巨大潜力。然而，当部署在缺乏充足标注数据的低资源环境中时，现有的Med-MLLMs通常会因为医学推理能力的瓶颈而失效，这些瓶颈包括：(i)忽略医学图像细节的内在推理瓶颈；(ii)无法整合专业医学知识的外在推理瓶颈。为了解决这些限制，我们提出了AMANDA，一个无需训练的agentic框架，通过LLM agent执行医学知识增强。具体来说，我们的内在医学知识增强侧重于由粗到精的问题分解以进行全面诊断，而外在医学知识增强则通过生物医学知识图谱检索来支持推理过程。在八个Med-VQA基准上的大量实验表明，在零样本和少样本Med-VQA设置中均取得了显著的改进。

## 🔬 方法详解

**问题定义**：现有的医学视觉问答模型（Med-VQA）在数据资源匮乏的情况下，难以充分利用医学图像中的细节信息，并且无法有效地整合外部的专业医学知识，导致推理能力受限，无法准确回答医学相关问题。这些问题严重阻碍了Med-VQA在实际临床场景中的应用。

**核心思路**：AMANDA的核心思路是利用大型语言模型（LLM）作为智能体（Agent），通过问题分解和知识图谱检索来增强模型的医学知识。通过将复杂问题分解为更小的、更易于处理的子问题，并结合外部知识图谱提供的医学信息，模型可以更全面、更准确地理解问题并给出答案。这种方法无需额外的训练，可以直接应用于现有的Med-VQA模型。

**技术框架**：AMANDA框架主要包含两个阶段：内在医学知识增强和外在医学知识增强。在内在医学知识增强阶段，模型首先将原始问题分解为一系列由粗到精的子问题，以便更全面地分析医学图像。在外在医学知识增强阶段，模型利用生物医学知识图谱检索与问题相关的医学知识，并将这些知识融入到推理过程中。整个框架无需训练，可以即插即用。

**关键创新**：AMANDA的关键创新在于利用LLM agent进行医学知识增强，这与传统的Med-VQA模型依赖于大量标注数据进行训练的方法不同。通过问题分解和知识图谱检索，AMANDA能够有效地利用外部知识，提高模型在低资源环境下的推理能力。此外，AMANDA是一个无需训练的框架，可以方便地应用于现有的Med-VQA模型。

**关键设计**：AMANDA框架的关键设计包括：(1) 使用LLM进行问题分解，将复杂问题分解为更小的子问题；(2) 利用生物医学知识图谱进行知识检索，获取与问题相关的医学信息；(3) 将检索到的知识融入到推理过程中，提高模型的推理能力。具体的参数设置和网络结构取决于所使用的LLM和知识图谱。

## 📊 实验亮点

AMANDA在八个Med-VQA基准测试中取得了显著的性能提升。在零样本设置下，AMANDA的性能优于现有的Med-VQA模型。在少样本设置下，AMANDA的性能也得到了显著提升，表明其具有很强的数据效率。实验结果表明，AMANDA能够有效地解决Med-VQA在低资源环境下的推理瓶颈。

## 🎯 应用场景

AMANDA具有广泛的应用前景，可用于辅助医生进行诊断、提供医学教育和患者咨询等。在医疗资源匮乏的地区，AMANDA可以作为一种低成本、高效益的解决方案，帮助医生做出更准确的诊断。此外，AMANDA还可以用于开发智能医学助手，为患者提供个性化的健康建议。

## 📄 摘要（原文）

> Medical Multimodal Large Language Models (Med-MLLMs) have shown great promise in medical visual question answering (Med-VQA). However, when deployed in low-resource settings where abundant labeled data are unavailable, existing Med-MLLMs commonly fail due to their medical reasoning capability bottlenecks: (i) the intrinsic reasoning bottleneck that ignores the details from the medical image; (ii) the extrinsic reasoning bottleneck that fails to incorporate specialized medical knowledge. To address those limitations, we propose AMANDA, a training-free agentic framework that performs medical knowledge augmentation via LLM agents. Specifically, our intrinsic medical knowledge augmentation focuses on coarse-to-fine question decomposition for comprehensive diagnosis, while extrinsic medical knowledge augmentation grounds the reasoning process via biomedical knowledge graph retrieval. Extensive experiments across eight Med-VQA benchmarks demonstrate substantial improvements in both zero-shot and few-shot Med-VQA settings. The code is available at https://github.com/REAL-Lab-NU/AMANDA.

