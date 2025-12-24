---
layout: default
title: "UniMedVL: Unifying Medical Multimodal Understanding And Generation Through Observation-Knowledge-Analysis"
---

# UniMedVL: Unifying Medical Multimodal Understanding And Generation Through Observation-Knowledge-Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.15710" class="toolbar-btn" target="_blank">📄 arXiv: 2510.15710v2</a>
  <a href="https://arxiv.org/pdf/2510.15710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.15710v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.15710v2', 'UniMedVL: Unifying Medical Multimodal Understanding And Generation Through Observation-Knowledge-Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junzhi Ning, Wei Li, Cheng Tang, Jiashi Lin, Chenglong Ma, Chaoyang Zhang, Jiyao Liu, Ying Chen, Shujian Gao, Lihao Liu, Yuandong Pu, Huihui Xu, Chenhui Gou, Ziyan Huang, Yi Xin, Qi Qin, Zhongying Deng, Diping Song, Bin Fu, Guang Yang, Yuanfeng Ji, Tianbin Li, Yanzhou Su, Jin Ye, Shixiang Tang, Ming Hu, Junjun He

**分类**: cs.CV

**发布日期**: 2025-10-17 (更新: 2025-10-27)

**🔗 代码/项目**: [GITHUB](https://github.com/uni-medical/UniMedVL)

---

## 💡 一句话要点

**提出UniMedVL，统一医学多模态理解与生成，提升医疗诊断应用性能。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医学多模态` `图像理解` `图像生成` `统一模型` `知识共享`

## 📋 核心要点

1. 现有医学AI系统在处理多模态医学数据时，图像理解和生成能力相互割裂，限制了模型的综合诊断能力。
2. UniMedVL模型基于观察-知识-分析（OKA）范式，通过统一的架构同时处理图像理解和生成任务，实现双向知识共享。
3. UniMedVL在多个医学图像理解基准测试中表现出色，并在多种医学成像模式下达到专业模型的生成质量。

## 📝 摘要（中文）

医学诊断应用需要能够处理多模态医学输入（图像、病史、实验室结果）并生成多样化输出（包括文本报告和视觉内容，如注释、分割掩码和图像）的模型。然而，现有的医学AI系统割裂了这一统一过程：医学图像理解模型解释图像但无法生成视觉输出，而医学图像生成模型合成图像但无法提供文本解释。这导致了数据表示、特征集成和任务级多模态能力的不足。为此，我们提出了一个多层次框架，该框架从诊断工作流程中汲取灵感，采用观察-知识-分析（OKA）范式。具体来说，在观察层面，我们构建了UniMed-5M，一个包含超过560万个样本的数据集，它将各种单模态数据重新格式化为多模态对，用于基础观察。在知识层面，我们提出了渐进式课程学习，系统地引入医学多模态知识。在分析层面，我们引入了UniMedVL，这是第一个医学统一多模态模型，用于在单个架构中同时分析图像理解和生成任务。UniMedVL在五个医学图像理解基准测试中取得了优异的性能，并在八种医学成像模式中匹配了专业模型的生成质量。至关重要的是，我们的统一架构实现了双向知识共享：生成任务增强了视觉理解特征，表明在一个单一医学框架内整合传统上分离的能力可以解锁各种医学视觉语言任务的改进。

## 🔬 方法详解

**问题定义**：现有医学AI系统在处理多模态医学数据时，图像理解模型无法生成视觉输出，而图像生成模型无法提供文本解释，导致数据表示、特征集成和任务级多模态能力的不足。这阻碍了模型在实际医疗诊断中的应用，因为医生需要同时理解图像和生成报告。

**核心思路**：UniMedVL的核心思路是构建一个统一的多模态模型，能够同时进行图像理解和生成任务，并通过双向知识共享来提升整体性能。该模型借鉴了医生诊断的流程，即观察（Observation）、知识（Knowledge）和分析（Analysis），将多模态数据整合到一个统一的框架中。

**技术框架**：UniMedVL的技术框架包含三个主要层面：观察层面、知识层面和分析层面。在观察层面，构建了UniMed-5M数据集，将各种单模态数据转化为多模态对。在知识层面，采用渐进式课程学习，逐步引入医学多模态知识。在分析层面，UniMedVL模型统一处理图像理解和生成任务。

**关键创新**：UniMedVL的关键创新在于其统一的架构，能够同时进行图像理解和生成任务，并实现双向知识共享。这种统一的架构打破了传统医学AI系统中图像理解和生成任务相互独立的局面，使得模型能够更好地利用多模态数据进行诊断。

**关键设计**：UniMedVL的关键设计包括：1) UniMed-5M数据集，包含大规模的多模态医学数据；2) 渐进式课程学习策略，逐步引入医学知识；3) 统一的多模态模型架构，能够同时处理图像理解和生成任务；4) 双向知识共享机制，使得图像理解和生成任务能够相互促进。

## 📊 实验亮点

UniMedVL在五个医学图像理解基准测试中取得了优异的性能，并在八种医学成像模式中匹配了专业模型的生成质量。实验结果表明，UniMedVL的统一架构能够实现双向知识共享，从而提升图像理解和生成任务的性能。例如，生成任务可以增强视觉理解特征，从而提高图像理解的准确性。

## 🎯 应用场景

UniMedVL具有广泛的应用前景，可用于辅助医生进行疾病诊断、生成医学报告、进行医学图像标注和分割等。该模型能够处理多模态医学数据，并生成多样化的输出，有助于提高诊断效率和准确性。未来，UniMedVL有望应用于远程医疗、智能医疗设备等领域，为医疗行业带来变革。

## 📄 摘要（原文）

> Medical diagnostic applications require models that can process multimodal medical inputs (images, patient histories, lab results) and generate diverse outputs including both textual reports and visual content (annotations, segmentation masks, and images). Despite this need, existing medical AI systems disrupt this unified process: medical image understanding models interpret images but cannot generate visual outputs, while medical image generation models synthesize images but cannot provide textual explanations. This leads to gaps in data representation, feature integration, and task-level multimodal capabilities. To this end, we propose a multi-level framework that draws inspiration from diagnostic workflows through the Observation-Knowledge-Analysis (OKA) paradigm. Specifically, at the observation level, we construct UniMed-5M, a dataset comprising over 5.6M samples that reformat diverse unimodal data into multimodal pairs for foundational observation. At the knowledge level, we propose Progressive Curriculum Learning that systematically introduces medical multimodal knowledge. At the analysis level, we introduce UniMedVL, the first medical unified multimodal model for the simultaneous analysis of image understanding and generation tasks within a single architecture. UniMedVL achieves superior performance on five medical image understanding benchmarks, while matching specialized models in generation quality across eight medical imaging modalities. Crucially, our unified architecture enables bidirectional knowledge sharing: generation tasks enhance visual understanding features, demonstrating that integrating traditionally separate capabilities within a single medical framework unlocks improvements across diverse medical vision-language tasks. Code is available at https://github.com/uni-medical/UniMedVL.

