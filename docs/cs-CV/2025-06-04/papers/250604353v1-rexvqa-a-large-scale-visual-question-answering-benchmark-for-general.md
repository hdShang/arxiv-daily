---
layout: default
title: "ReXVQA: A Large-scale Visual Question Answering Benchmark for Generalist Chest X-ray Understanding"
---

# ReXVQA: A Large-scale Visual Question Answering Benchmark for Generalist Chest X-ray Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04353" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04353v1</a>
  <a href="https://arxiv.org/pdf/2506.04353.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04353v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04353v1', 'ReXVQA: A Large-scale Visual Question Answering Benchmark for Generalist Chest X-ray Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ankit Pal, Jung-Oh Lee, Xiaoman Zhang, Malaikannan Sankarasubbu, Seunghyeon Roh, Won Jung Kim, Meesun Lee, Pranav Rajpurkar

**分类**: cs.CV, cs.AI, cs.CE, cs.CL, cs.LG

**发布日期**: 2025-06-04

**🔗 代码/项目**: [HUGGINGFACE](https://huggingface.co/datasets/rajpurkarlab)

---

## 💡 一句话要点

**提出ReXVQA以解决胸部X光视觉问答基准问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉问答` `胸部X光` `放射学` `多模态学习` `人工智能` `医学影像` `数据集`

## 📋 核心要点

1. 现有的视觉问答基准在胸部X光领域缺乏多样性和临床真实性，限制了AI模型的评估和应用。
2. ReXVQA通过引入多样化的任务，涵盖放射学推理技能，提供了一个全面的评估框架，推动了AI在医学影像分析中的应用。
3. 实验结果显示，MedGemma模型的准确率为83.24%，超过了人类放射科医生的表现，展示了AI在胸部X光解读中的潜力。

## 📝 摘要（中文）

我们提出了ReXVQA，这是胸部放射学领域最大的视觉问答基准，包含约696,000个问题和160,000个胸部X光研究。与以往依赖模板查询的方法不同，ReXVQA引入了多样且临床真实的任务，涵盖五种核心放射学推理技能。我们评估了八种最先进的多模态大语言模型，其中表现最佳的模型MedGemma达到了83.24%的整体准确率。通过与人类放射科医生的比较研究，MedGemma的表现超越了人类专家，标志着AI在胸部X光解读中的重要里程碑。ReXVQA为评估通用放射学AI系统设立了新标准，并将数据集开放源代码。

## 🔬 方法详解

**问题定义**：本论文旨在解决胸部X光视觉问答领域缺乏全面、真实基准的问题。现有方法多依赖模板查询，无法有效评估AI模型的推理能力。

**核心思路**：ReXVQA通过设计多样化的任务，反映临床实际需求，涵盖五种核心放射学推理技能，提供了更具挑战性的评估标准。

**技术框架**：整体架构包括数据集构建、任务设计和模型评估三个主要模块。数据集包含大量问题与X光图像的配对，任务设计则聚焦于临床推理技能的评估。

**关键创新**：ReXVQA的最大创新在于其多样化的任务设计和大规模数据集，突破了以往基于模板的评估方式，使得AI模型的评估更具临床相关性。

**关键设计**：在模型评估中，使用了多种先进的多模态大语言模型，并通过与人类放射科医生的比较研究，验证了模型的有效性和准确性。

## 📊 实验亮点

实验结果显示，MedGemma模型在胸部X光解读中的准确率达到83.24%，超过了人类放射科医生的最佳表现（77.27%），展示了AI在医学影像分析中的巨大潜力和优势。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、放射学教育和AI辅助诊断。通过提供一个标准化的评估基准，ReXVQA将推动AI在临床环境中的应用，提升放射学的工作效率和准确性。

## 📄 摘要（原文）

> We present ReXVQA, the largest and most comprehensive benchmark for visual question answering (VQA) in chest radiology, comprising approximately 696,000 questions paired with 160,000 chest X-rays studies across training, validation, and test sets. Unlike prior efforts that rely heavily on template based queries, ReXVQA introduces a diverse and clinically authentic task suite reflecting five core radiological reasoning skills: presence assessment, location analysis, negation detection, differential diagnosis, and geometric reasoning. We evaluate eight state-of-the-art multimodal large language models, including MedGemma-4B-it, Qwen2.5-VL, Janus-Pro-7B, and Eagle2-9B. The best-performing model (MedGemma) achieves 83.24% overall accuracy. To bridge the gap between AI performance and clinical expertise, we conducted a comprehensive human reader study involving 3 radiology residents on 200 randomly sampled cases. Our evaluation demonstrates that MedGemma achieved superior performance (83.84% accuracy) compared to human readers (best radiology resident: 77.27%), representing a significant milestone where AI performance exceeds expert human evaluation on chest X-ray interpretation. The reader study reveals distinct performance patterns between AI models and human experts, with strong inter-reader agreement among radiologists while showing more variable agreement patterns between human readers and AI models. ReXVQA establishes a new standard for evaluating generalist radiological AI systems, offering public leaderboards, fine-grained evaluation splits, structured explanations, and category-level breakdowns. This benchmark lays the foundation for next-generation AI systems capable of mimicking expert-level clinical reasoning beyond narrow pathology classification. Our dataset will be open-sourced at https://huggingface.co/datasets/rajpurkarlab/ReXVQA

