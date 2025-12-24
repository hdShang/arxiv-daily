---
layout: default
title: "M-PACE: Mother Child Framework for Multimodal Compliance"
---

# M-PACE: Mother Child Framework for Multimodal Compliance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15241" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15241v1</a>
  <a href="https://arxiv.org/pdf/2509.15241.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15241v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15241v1', 'M-PACE: Mother Child Framework for Multimodal Compliance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shreyash Verma, Amit Kesari, Vinayak Trivedi, Anupam Purwar, Ratnesh Jamidar

**分类**: cs.CV, cs.CL

**发布日期**: 2025-09-17

**备注**: The M-PACE framework uses a "mother-child" AI model system to automate and unify compliance checks for ads, reducing costs while maintaining high accuracy

---

## 💡 一句话要点

**M-PACE：用于多模态合规性的母子框架，显著降低推理成本。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `合规性检查` `大型语言模型` `母子模型` `广告审核`

## 📋 核心要点

1. 传统多模态内容合规流程依赖分离模块，导致高运营成本和低可扩展性，难以适应动态标准。
2. M-PACE框架利用母子MLLM结构，单次评估视觉-语言输入，实现高效合规性检查。
3. 实验表明，M-PACE显著降低推理成本（高达31倍），同时保持与大型模型相当的准确性。

## 📝 摘要（中文）

在各个领域，确保多模态内容符合品牌、法律或平台特定的合规标准是一项日益复杂的挑战。传统的合规框架通常依赖于分离的多阶段流程，这些流程集成了用于图像分类、文本提取、音频转录、手工检查和基于规则的合并的独立模块。这种架构碎片化增加了运营开销，阻碍了可扩展性，并妨碍了有效适应动态准则的能力。随着多模态大型语言模型（MLLM）的出现，将这些工作流程统一在能够联合处理视觉和文本内容的单一通用框架下的潜力越来越大。鉴于此，我们提出了多模态参数无关合规引擎（M-PACE），该框架旨在单次评估视觉-语言输入的属性。作为一个代表性的用例，我们将M-PACE应用于广告合规性，展示了其评估超过15个与合规性相关的属性的能力。为了支持结构化评估，我们引入了一个人工标注的基准，该基准通过模拟具有挑战性的真实世界条件（包括视觉障碍和亵渎注入）的增强样本进行了丰富。M-PACE采用母子MLLM设置，表明更强大的母MLLM评估较小子模型的输出可以显着减少对人工审核员的依赖，从而实现质量控制的自动化。我们的分析表明，推理成本降低了31倍以上，最有效的模型（Gemini 2.0 Flash作为由母MLLM选择的子MLLM）的运行成本为每张图像0.0005美元，而Gemini 2.5 Pro的运行成本为0.0159美元，具有相当的准确性，突出了M-PACE在广告数据的实际部署中实时实现的成本和输出质量之间的权衡。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态内容合规性检查中传统方法的低效问题。现有方法通常采用分离的多阶段流程，涉及图像分类、文本提取等多个独立模块，导致运营成本高昂、可扩展性差，且难以适应不断变化的合规标准。

**核心思路**：论文的核心思路是利用多模态大型语言模型（MLLM）的强大能力，将多个独立的合规性检查任务统一到一个单一的框架中。通过设计一个母子MLLM结构，实现高效且低成本的合规性评估。

**技术框架**：M-PACE框架采用母子MLLM结构。子MLLM负责对输入的多模态内容（例如广告图像和文本）进行初步评估，并生成相应的输出。母MLLM则负责评估子MLLM的输出，并做出最终的合规性判断。这种结构允许母MLLM利用其更强大的能力来纠正子MLLM的错误，从而提高整体的准确性。

**关键创新**：M-PACE的关键创新在于其母子MLLM结构，以及参数无关的设计。母子模型的选择可以根据实际需求进行调整，无需重新训练整个框架。此外，该框架还引入了一个人工标注的基准数据集，用于评估和比较不同模型的性能。

**关键设计**：M-PACE的关键设计包括：1) 母子MLLM的选择策略，根据成本和性能进行权衡；2) 用于评估子MLLM输出的提示工程，确保母MLLM能够有效地利用子模型的输出；3) 基准数据集的构建，包含各种具有挑战性的场景，例如视觉遮挡和恶意文本注入。

## 📊 实验亮点

实验结果表明，M-PACE框架能够显著降低推理成本，同时保持与大型模型相当的准确性。例如，使用Gemini 2.0 Flash作为子MLLM时，每张图像的推理成本仅为0.0005美元，而使用Gemini 2.5 Pro时，成本为0.0159美元。此外，M-PACE框架在广告合规性检查任务中，能够有效识别超过15个与合规性相关的属性。

## 🎯 应用场景

M-PACE框架可广泛应用于各种需要多模态内容合规性检查的领域，例如广告审核、社交媒体内容审核、电商平台商品审核等。该框架能够显著降低人工审核的成本，提高审核效率，并确保内容符合相关的法律法规和平台规范。未来，该框架还可以扩展到其他领域，例如医疗影像分析和自动驾驶等。

## 📄 摘要（原文）

> Ensuring that multi-modal content adheres to brand, legal, or platform-specific compliance standards is an increasingly complex challenge across domains. Traditional compliance frameworks typically rely on disjointed, multi-stage pipelines that integrate separate modules for image classification, text extraction, audio transcription, hand-crafted checks, and rule-based merges. This architectural fragmentation increases operational overhead, hampers scalability, and hinders the ability to adapt to dynamic guidelines efficiently. With the emergence of Multimodal Large Language Models (MLLMs), there is growing potential to unify these workflows under a single, general-purpose framework capable of jointly processing visual and textual content. In light of this, we propose Multimodal Parameter Agnostic Compliance Engine (M-PACE), a framework designed for assessing attributes across vision-language inputs in a single pass. As a representative use case, we apply M-PACE to advertisement compliance, demonstrating its ability to evaluate over 15 compliance-related attributes. To support structured evaluation, we introduce a human-annotated benchmark enriched with augmented samples that simulate challenging real-world conditions, including visual obstructions and profanity injection. M-PACE employs a mother-child MLLM setup, demonstrating that a stronger parent MLLM evaluating the outputs of smaller child models can significantly reduce dependence on human reviewers, thereby automating quality control. Our analysis reveals that inference costs reduce by over 31 times, with the most efficient models (Gemini 2.0 Flash as child MLLM selected by mother MLLM) operating at 0.0005 per image, compared to 0.0159 for Gemini 2.5 Pro with comparable accuracy, highlighting the trade-off between cost and output quality achieved in real time by M-PACE in real life deployment over advertising data.

