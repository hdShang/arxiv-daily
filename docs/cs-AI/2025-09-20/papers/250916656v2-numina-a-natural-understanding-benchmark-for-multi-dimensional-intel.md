---
layout: default
title: "NUMINA: A Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities"
---

# NUMINA: A Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.16656" class="toolbar-btn" target="_blank">📄 arXiv: 2509.16656v2</a>
  <a href="https://arxiv.org/pdf/2509.16656.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.16656v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.16656v2', 'NUMINA: A Natural Understanding Benchmark for Multi-dimensional Intelligence and Numerical Reasoning Abilities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changyu Zeng, Yifan Wang, Zimu Wang, Wei Wang, Zhengni Yang, Muyi Bao, Jiming Xiao, Anh Nguyen, Yutao Yue

**分类**: cs.AI

**发布日期**: 2025-09-20 (更新: 2025-10-01)

**🔗 代码/项目**: [GITHUB](https://github.com/fengshun124/NUMINA)

---

## 💡 一句话要点

**提出NUMINA基准，用于评估多模态LLM在3D室内场景中的数值推理能力**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D场景理解` `数值推理` `多模态学习` `大语言模型` `基准数据集`

## 📋 核心要点

1. 现有3D基准缺乏细粒度的数值推理标注，限制了MLLM在3D场景中进行精确空间测量和复杂数值推理的能力。
2. NUMINA基准通过NUMINA-Flow自动标注流程，生成多尺度标注和问答对，提升模型在3D场景中的数值推理能力。
3. 实验表明，现有LLM在NUMINA基准上进行多模态数值推理时表现不佳，尤其是在距离和体积估计等精确计算方面。

## 📝 摘要（中文）

本文提出了NUMINA，这是一个用于多维智能和数值推理能力的自然理解基准，旨在提升多模态室内感知理解。现有的2D多模态大语言模型(MLLM)在视觉-语言任务中取得了显著进展。然而，由于空间推理的复杂性，将这些能力扩展到3D环境仍然是一个独特的挑战。现有的3D基准通常缺乏细粒度的数值推理任务标注，限制了MLLM执行精确空间测量和复杂数值推理的能力。NUMINA通过NUMINA-Flow自动标注流程生成多尺度标注和各种问答对，该流程集成了LLM重写和基于规则的自验证。在Chat-Scene框架下，对各种最先进的LLM在NUMINA上进行了评估，结果表明，当前的LLM在多模态数值推理方面存在困难，尤其是在执行精确计算（如距离和体积估计）时，这突出了对3D模型进行进一步改进的需求。数据集和源代码可在https://github.com/fengshun124/NUMINA 获取。

## 🔬 方法详解

**问题定义**：论文旨在解决现有3D视觉语言模型在室内场景下缺乏精确数值推理能力的问题。现有3D基准数据集通常缺乏细粒度的数值推理标注，使得模型难以进行精确的空间测量和复杂的数值计算，例如距离、体积估计等。这限制了模型在实际应用中的能力。

**核心思路**：论文的核心思路是构建一个包含丰富数值推理标注的3D室内场景数据集NUMINA。通过设计自动标注流程NUMINA-Flow，利用LLM进行问题生成和规则验证，从而高效地创建高质量的问答对，用于训练和评估模型的数值推理能力。

**技术框架**：NUMINA的整体框架包括以下几个主要部分：1) 3D室内场景数据收集；2) NUMINA-Flow自动标注流程，该流程包含LLM问题生成模块和基于规则的自验证模块；3) 构建NUMINA基准数据集，包含多尺度标注和问答对；4) 在Chat-Scene框架下，评估现有LLM在NUMINA上的性能。

**关键创新**：NUMINA的关键创新在于提出了NUMINA-Flow自动标注流程，该流程能够高效地生成高质量的数值推理问答对。与传统的人工标注相比，NUMINA-Flow利用LLM进行问题生成，并采用规则进行自验证，大大提高了标注效率和数据质量。此外，NUMINA是首个专注于3D室内场景数值推理的基准数据集。

**关键设计**：NUMINA-Flow流程的关键设计包括：1) 使用LLM进行问题生成，利用LLM的自然语言理解和生成能力，生成多样化的数值推理问题；2) 设计基于规则的自验证模块，用于过滤掉不准确或不合理的标注，保证数据质量；3) 采用多尺度标注，提供不同粒度的信息，以支持更复杂的推理任务。

## 📊 实验亮点

实验结果表明，现有的LLM在NUMINA基准上表现不佳，尤其是在执行精确计算（如距离和体积估计）时。例如，在距离估计任务中，模型的平均误差较高，表明模型缺乏精确的空间感知和数值推理能力。这些结果突出了当前LLM在3D场景数值推理方面的不足，并为未来的研究方向提供了指导。

## 🎯 应用场景

NUMINA基准的潜在应用领域包括机器人导航、智能家居、虚拟现实和增强现实等。通过提升模型在3D室内场景中的数值推理能力，可以使机器人更好地理解和操作周围环境，例如进行精确的物体定位、路径规划和任务执行。此外，该研究还可以促进虚拟现实和增强现实技术的发展，提供更逼真和交互性更强的用户体验。

## 📄 摘要（原文）

> Recent advancements in 2D multimodal large language models (MLLMs) have significantly improved performance in vision-language tasks. However, extending these capabilities to 3D environments remains a distinct challenge due to the complexity of spatial reasoning. Nevertheless, existing 3D benchmarks often lack fine-grained numerical reasoning task annotations, limiting MLLMs' ability to perform precise spatial measurements and complex numerical reasoning. To address this gap, we introduce NUMINA, the first Natural Understanding benchmark for Multi-dimensional Intelligence and Numerical reasoning Abilities to enhance multimodal indoor perceptual understanding. NUMINA features multi-scale annotations and various question-answer pairs, generated using NUMINA-Flow, an automated annotation pipeline that integrates LLM rewriting and rule-based self-verification. We evaluate the performance of various state-of-the-art LLMs on NUMINA following the Chat-Scene framework, demonstrating that current LLMs struggle with multimodal numerical reasoning, particularly in performing precise computations such as distance and volume estimation, highlighting the need for further advancements in 3D models. The dataset and source codes can be obtained from https://github.com/fengshun124/NUMINA.

