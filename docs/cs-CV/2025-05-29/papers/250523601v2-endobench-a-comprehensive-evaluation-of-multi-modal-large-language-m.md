---
layout: default
title: "EndoBench: A Comprehensive Evaluation of Multi-Modal Large Language Models for Endoscopy Analysis"
---

# EndoBench: A Comprehensive Evaluation of Multi-Modal Large Language Models for Endoscopy Analysis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.23601" class="toolbar-btn" target="_blank">📄 arXiv: 2505.23601v2</a>
  <a href="https://arxiv.org/pdf/2505.23601.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.23601v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.23601v2', 'EndoBench: A Comprehensive Evaluation of Multi-Modal Large Language Models for Endoscopy Analysis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shengyuan Liu, Boyun Zheng, Wenting Chen, Zhihao Peng, Zhenfei Yin, Jing Shao, Jiancong Hu, Yixuan Yuan

**分类**: cs.CV

**发布日期**: 2025-05-29 (更新: 2025-09-24)

**备注**: 40 pages, 22 figures; Accepted by NeurIPS 2025 Dataset and Benchmark Track

---

## 💡 一句话要点

**提出EndoBench以解决内窥镜分析多模态模型评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `内窥镜分析` `多模态大语言模型` `基准测试` `临床任务` `视觉提示` `模型评估` `医学人工智能`

## 📋 核心要点

1. 现有的内窥镜分析基准测试仅覆盖特定场景和少量任务，无法反映真实临床需求。
2. EndoBench是一个综合性基准，旨在全面评估多模态大语言模型在内窥镜实践中的表现。
3. 实验结果显示，专有模型整体表现优于开源和医学专用模型，但仍落后于人类专家。

## 📝 摘要（中文）

内窥镜程序在内部疾病的诊断和治疗中至关重要，而多模态大语言模型（MLLMs）在内窥镜分析中应用日益广泛。然而，现有基准测试通常局限于特定的内窥镜场景和少量临床任务，无法捕捉内窥镜场景的真实多样性及临床工作流程所需的全方位技能。为此，我们提出了EndoBench，这是第一个专门设计用于评估MLLMs在内窥镜实践中多维能力的综合基准。EndoBench涵盖4种不同的内窥镜场景、12个专业临床任务及12个次任务，并提供5种视觉提示粒度，生成6832对经过严格验证的VQA对。我们的多维评估框架反映了临床工作流程，全面评估MLLMs在真实场景中的感知和诊断能力。我们对23个最先进的模型进行了基准测试，并将人类临床医生的表现作为参考标准。

## 🔬 方法详解

**问题定义**：当前内窥镜分析的基准测试缺乏全面性，无法涵盖多样化的临床场景和任务，导致模型评估不够准确。

**核心思路**：EndoBench通过设计一个多维度的评估框架，涵盖不同的内窥镜场景和任务，旨在全面评估MLLMs的能力。

**技术框架**：该框架包括4种内窥镜场景、12个主要临床任务及其次任务，结合5种视觉提示粒度，形成6832对VQA对，模拟真实的临床工作流程。

**关键创新**：EndoBench是首个针对内窥镜分析的综合性基准，能够全面反映模型在真实场景中的表现，填补了现有评估的空白。

**关键设计**：在评估过程中，采用了严格的验证机制，确保数据的多样性和代表性，同时引入了人类专家表现作为参考标准。实验中还考察了提示格式和任务复杂性对模型表现的影响。

## 📊 实验亮点

实验结果表明，专有的多模态大语言模型在整体表现上优于开源和医学专用模型，但仍未达到人类专家的水平。医学领域的监督微调显著提高了任务特定的准确性，同时模型表现对提示格式和任务复杂性敏感。

## 🎯 应用场景

EndoBench的研究成果可广泛应用于医疗领域，尤其是在内窥镜分析、疾病诊断和治疗决策支持等方面。通过提升多模态大语言模型的评估标准，未来可能推动更智能的医疗辅助系统的发展，改善临床工作效率和患者护理质量。

## 📄 摘要（原文）

> Endoscopic procedures are essential for diagnosing and treating internal diseases, and multi-modal large language models (MLLMs) are increasingly applied to assist in endoscopy analysis. However, current benchmarks are limited, as they typically cover specific endoscopic scenarios and a small set of clinical tasks, failing to capture the real-world diversity of endoscopic scenarios and the full range of skills needed in clinical workflows. To address these issues, we introduce EndoBench, the first comprehensive benchmark specifically designed to assess MLLMs across the full spectrum of endoscopic practice with multi-dimensional capacities. EndoBench encompasses 4 distinct endoscopic scenarios, 12 specialized clinical tasks with 12 secondary subtasks, and 5 levels of visual prompting granularities, resulting in 6,832 rigorously validated VQA pairs from 21 diverse datasets. Our multi-dimensional evaluation framework mirrors the clinical workflow--spanning anatomical recognition, lesion analysis, spatial localization, and surgical operations--to holistically gauge the perceptual and diagnostic abilities of MLLMs in realistic scenarios. We benchmark 23 state-of-the-art models, including general-purpose, medical-specialized, and proprietary MLLMs, and establish human clinician performance as a reference standard. Our extensive experiments reveal: (1) proprietary MLLMs outperform open-source and medical-specialized models overall, but still trail human experts; (2) medical-domain supervised fine-tuning substantially boosts task-specific accuracy; and (3) model performance remains sensitive to prompt format and clinical task complexity. EndoBench establishes a new standard for evaluating and advancing MLLMs in endoscopy, highlighting both progress and persistent gaps between current models and expert clinical reasoning. We publicly release our benchmark and code.

