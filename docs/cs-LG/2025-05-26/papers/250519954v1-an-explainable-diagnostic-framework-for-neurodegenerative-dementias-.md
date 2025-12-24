---
layout: default
title: An Explainable Diagnostic Framework for Neurodegenerative Dementias via Reinforcement-Optimized LLM Reasoning
---

# An Explainable Diagnostic Framework for Neurodegenerative Dementias via Reinforcement-Optimized LLM Reasoning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.19954" class="toolbar-btn" target="_blank">📄 arXiv: 2505.19954v1</a>
  <a href="https://arxiv.org/pdf/2505.19954.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.19954v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.19954v1', 'An Explainable Diagnostic Framework for Neurodegenerative Dementias via Reinforcement-Optimized LLM Reasoning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Andrew Zamai, Nathanael Fijalkow, Boris Mansencal, Laurent Simon, Eloi Navet, Pierrick Coupe

**分类**: cs.LG, cs.CL

**发布日期**: 2025-05-26

---

## 💡 一句话要点

**提出可解释的神经退行性痴呆诊断框架以提升诊断透明度**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `神经退行性痴呆` `可解释性` `深度学习` `大型语言模型` `强化学习` `医学影像分析` `诊断推理`

## 📋 核心要点

1. 现有深度学习方法在神经退行性痴呆的诊断中表现出色，但缺乏透明性，限制了其临床应用。
2. 本文提出的框架通过将3D脑MRI转换为文本报告，并利用大型语言模型进行诊断推理，提升了诊断的可解释性。
3. 实验结果表明，该框架在保持与现有深度学习方法相当的诊断性能的同时，提供了结构化的诊断理由，增强了决策过程的透明度。

## 📝 摘要（中文）

神经退行性痴呆的鉴别诊断是一项具有挑战性的临床任务，主要由于症状表现的重叠和结构神经影像中观察到的模式相似性。为提高诊断效率和准确性，本文提出了一种框架，整合了两个核心组件以增强诊断透明度。首先，构建了一个模块化管道，将3D T1加权脑MRI转换为文本放射学报告。其次，探索现代大型语言模型（LLMs）在基于生成报告的前额叶痴呆亚型、阿尔茨海默病和正常衰老的鉴别诊断中的潜力。通过强化学习激励LLMs的诊断推理，本文的方法在不需要监督推理轨迹或从更大模型中提炼的情况下，能够生成基于神经影像发现的结构化诊断理由。

## 🔬 方法详解

**问题定义**：本文旨在解决神经退行性痴呆的鉴别诊断中，现有深度学习方法缺乏透明性的问题。尽管这些方法在预测性能上表现优异，但其决策过程不透明，限制了临床应用。

**核心思路**：论文提出的框架通过将3D T1加权脑MRI转换为文本放射学报告，并利用大型语言模型进行诊断推理，来提升诊断的可解释性。通过强化学习激励LLMs的诊断推理，生成结构化的诊断理由。

**技术框架**：整体架构包括两个主要模块：首先是将MRI图像转换为文本报告的模块，其次是利用LLMs进行基于报告的诊断推理。框架通过强化学习优化推理过程，确保生成的理由与影像发现相一致。

**关键创新**：最重要的技术创新在于通过强化学习实现了LLMs的诊断推理，而不依赖于监督学习或模型蒸馏。这使得模型能够在推理过程中生成因果性解释，区别于传统的后验解释方法。

**关键设计**：在设计中，采用了强化学习的奖励机制来激励模型生成合理的诊断理由，确保其与影像数据相结合。此外，模型结构和损失函数的选择也经过精心设计，以优化推理的准确性和可解释性。

## 📊 实验亮点

实验结果显示，提出的框架在诊断性能上与现有深度学习方法相当，同时提供了结构化的诊断理由，显著提升了模型的可解释性。这种方法的创新性在于其能够在推理过程中生成因果性解释，而不是事后解释，增强了临床应用的实用性。

## 🎯 应用场景

该研究的潜在应用领域包括临床医学中的神经退行性疾病诊断，尤其是在需要高透明度和可解释性的场景中。通过提供结构化的诊断理由，该框架能够帮助医生更好地理解模型的决策过程，从而提高临床决策的信心和效率。未来，该方法有望推广至其他医学影像分析领域，提升整体诊断水平。

## 📄 摘要（原文）

> The differential diagnosis of neurodegenerative dementias is a challenging clinical task, mainly because of the overlap in symptom presentation and the similarity of patterns observed in structural neuroimaging. To improve diagnostic efficiency and accuracy, deep learning-based methods such as Convolutional Neural Networks and Vision Transformers have been proposed for the automatic classification of brain MRIs. However, despite their strong predictive performance, these models find limited clinical utility due to their opaque decision making. In this work, we propose a framework that integrates two core components to enhance diagnostic transparency. First, we introduce a modular pipeline for converting 3D T1-weighted brain MRIs into textual radiology reports. Second, we explore the potential of modern Large Language Models (LLMs) to assist clinicians in the differential diagnosis between Frontotemporal dementia subtypes, Alzheimer's disease, and normal aging based on the generated reports. To bridge the gap between predictive accuracy and explainability, we employ reinforcement learning to incentivize diagnostic reasoning in LLMs. Without requiring supervised reasoning traces or distillation from larger models, our approach enables the emergence of structured diagnostic rationales grounded in neuroimaging findings. Unlike post-hoc explainability methods that retrospectively justify model decisions, our framework generates diagnostic rationales as part of the inference process-producing causally grounded explanations that inform and guide the model's decision-making process. In doing so, our framework matches the diagnostic performance of existing deep learning methods while offering rationales that support its diagnostic conclusions.

