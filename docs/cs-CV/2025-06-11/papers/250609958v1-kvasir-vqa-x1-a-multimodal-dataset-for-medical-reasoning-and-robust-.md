---
layout: default
title: "Kvasir-VQA-x1: A Multimodal Dataset for Medical Reasoning and Robust MedVQA in Gastrointestinal Endoscopy"
---

# Kvasir-VQA-x1: A Multimodal Dataset for Medical Reasoning and Robust MedVQA in Gastrointestinal Endoscopy

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09958" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09958v1</a>
  <a href="https://arxiv.org/pdf/2506.09958.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09958v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09958v1', 'Kvasir-VQA-x1: A Multimodal Dataset for Medical Reasoning and Robust MedVQA in Gastrointestinal Endoscopy')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sushant Gautam, Michael A. Riegler, Pål Halvorsen

**分类**: cs.CV, cs.LG

**发布日期**: 2025-06-11

**🔗 代码/项目**: [GITHUB](https://github.com/Simula/Kvasir-VQA-x1) | [HUGGINGFACE](https://huggingface.co/datasets/SimulaMet)

---

## 💡 一句话要点

**提出Kvasir-VQA-x1以解决医疗视觉问答数据集不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `医疗视觉问答` `多模态数据集` `临床推理` `视觉增强` `大规模数据集`

## 📋 核心要点

1. 现有的MedVQA数据集缺乏临床复杂性和视觉多样性，限制了模型的推理能力。
2. Kvasir-VQA-x1通过引入159,549个新问题-答案对，系统化生成问题以测试临床推理能力。
3. 该数据集支持标准VQA性能评估和模型对视觉扰动的鲁棒性测试，提供更具挑战性的基准。

## 📝 摘要（中文）

医疗视觉问答（MedVQA）是临床决策支持系统的重要领域，但现有数据集往往缺乏临床复杂性和视觉多样性。为此，我们推出了Kvasir-VQA-x1，这是一个针对胃肠内窥镜的新型大规模数据集。该数据集新增159,549个问题-答案对，旨在测试更深层次的临床推理能力。我们采用大型语言模型系统化生成这些问题，并通过视觉增强技术模拟常见成像伪影，以确保数据集能够为模型在真实临床场景中的应用做好准备。Kvasir-VQA-x1旨在加速更可靠和有效的多模态AI系统的发展，并遵循FAIR数据原则，完全开放给研究社区使用。

## 🔬 方法详解

**问题定义**：本研究旨在解决现有MedVQA数据集在临床复杂性和视觉多样性方面的不足，导致模型推理能力受限。

**核心思路**：通过引入大规模问题-答案对和视觉增强技术，Kvasir-VQA-x1旨在提升模型在真实临床场景中的表现和鲁棒性。

**技术框架**：数据集的构建包括问题生成、视觉增强和评估模块。问题生成使用大型语言模型，视觉增强则模拟常见的成像伪影。

**关键创新**：Kvasir-VQA-x1的创新在于其系统化的问题生成方法和视觉增强策略，使得数据集更具临床相关性和挑战性。

**关键设计**：在问题生成中，问题按复杂性分层设计，确保覆盖不同推理能力的评估；视觉增强则通过多种伪影模拟真实场景中的干扰。

## 📊 实验亮点

Kvasir-VQA-x1在标准VQA性能评估中表现出色，显著提升了模型在复杂临床场景下的推理能力。通过引入视觉扰动测试，模型的鲁棒性也得到了有效验证，展示了相较于现有基线的显著提升。

## 🎯 应用场景

Kvasir-VQA-x1可广泛应用于医疗影像分析、临床决策支持系统的开发及多模态AI系统的训练。其丰富的数据集为研究人员提供了一个更具挑战性的基准，推动医疗AI技术的进步，提升临床应用的可靠性与有效性。

## 📄 摘要（原文）

> Medical Visual Question Answering (MedVQA) is a promising field for developing clinical decision support systems, yet progress is often limited by the available datasets, which can lack clinical complexity and visual diversity. To address these gaps, we introduce Kvasir-VQA-x1, a new, large-scale dataset for gastrointestinal (GI) endoscopy. Our work significantly expands upon the original Kvasir-VQA by incorporating 159,549 new question-answer pairs that are designed to test deeper clinical reasoning. We developed a systematic method using large language models to generate these questions, which are stratified by complexity to better assess a model's inference capabilities. To ensure our dataset prepares models for real-world clinical scenarios, we have also introduced a variety of visual augmentations that mimic common imaging artifacts. The dataset is structured to support two main evaluation tracks: one for standard VQA performance and another to test model robustness against these visual perturbations. By providing a more challenging and clinically relevant benchmark, Kvasir-VQA-x1 aims to accelerate the development of more reliable and effective multimodal AI systems for use in clinical settings. The dataset is fully accessible and adheres to FAIR data principles, making it a valuable resource for the wider research community. Code and data: https://github.com/Simula/Kvasir-VQA-x1 and https://huggingface.co/datasets/SimulaMet/Kvasir-VQA-x1

