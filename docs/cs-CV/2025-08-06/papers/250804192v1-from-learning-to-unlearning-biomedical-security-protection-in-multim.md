---
layout: default
title: "From Learning to Unlearning: Biomedical Security Protection in Multimodal Large Language Models"
---

# From Learning to Unlearning: Biomedical Security Protection in Multimodal Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.04192" class="toolbar-btn" target="_blank">📄 arXiv: 2508.04192v1</a>
  <a href="https://arxiv.org/pdf/2508.04192.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.04192v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.04192v1', 'From Learning to Unlearning: Biomedical Security Protection in Multimodal Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Dunyuan Xu, Xikai Yang, Yaoqian Li, Jinpeng Li, Pheng-Ann Heng

**分类**: cs.CV

**发布日期**: 2025-08-06

---

## 💡 一句话要点

**提出MLLMU-Med以解决生物医学多模态大语言模型的安全问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `生物医学` `多模态大语言模型` `机器遗忘` `隐私保护` `错误知识去除` `数据生成` `遗忘效率评分`

## 📋 核心要点

1. 现有生物医学多模态大语言模型在训练中容易包含私人信息和错误知识，导致隐私泄露和错误输出。
2. 本文提出了MLLMU-Med基准数据集，通过合成私人数据和事实错误生成训练集，评估模型的遗忘能力。
3. 实验结果显示，五种遗忘方法在去除有害知识方面效果有限，表明该领域的研究仍需深入探索。

## 📝 摘要（中文）

生物医学多模态大语言模型（MLLMs）的安全性日益受到关注。然而，训练样本中可能包含难以检测的私人信息和错误知识，导致隐私泄露或部署后产生错误输出。传统的解决方案是重新处理训练集并从头开始重新训练模型，但这在计算上不可行。机器遗忘作为一种新兴解决方案，可以选择性地移除有害样本中的不必要知识，同时保留正常案例的能力。为此，本文提出了第一个基准数据集MLLMU-Med，旨在评估生物医学MLLMs的遗忘质量，并提出了一种新的遗忘效率评分，反映不同子集的整体遗忘性能。实验表明，现有的五种遗忘方法在去除有害知识方面效果有限，表明该领域仍有很大的改进空间。

## 🔬 方法详解

**问题定义**：本文旨在解决生物医学多模态大语言模型中私人信息和错误知识的遗忘问题。现有方法在去除这些不必要知识时，往往需要完全重新训练模型，计算成本高昂且不切实际。

**核心思路**：论文提出的核心思路是利用机器遗忘技术，选择性地移除有害样本中的知识，而不需要从头开始重新训练模型。通过构建MLLMU-Med基准数据集，评估模型在隐私保护和错误知识去除方面的能力。

**技术框架**：整体架构包括数据生成管道、模型训练和评估模块。数据生成管道负责合成私人数据和错误知识，训练模块使用这些数据训练模型，评估模块则通过遗忘效率评分来衡量模型的遗忘性能。

**关键创新**：本文的关键创新在于提出了MLLMU-Med基准数据集和遗忘效率评分，这为生物医学MLLMs的安全性评估提供了新的工具和方法，填补了现有研究的空白。

**关键设计**：在数据生成过程中，采用了合成技术生成私人信息和错误知识，确保训练集的多样性和复杂性。遗忘效率评分的设计考虑了不同子集的表现，能够全面反映模型的遗忘能力。

## 📊 实验亮点

实验结果表明，五种不同的遗忘方法在去除生物医学多模态大语言模型中的有害知识时效果有限，显示出仅有小幅度的性能提升。这一发现强调了该领域在模型安全性和隐私保护方面的研究仍需进一步深入。

## 🎯 应用场景

该研究的潜在应用领域包括医疗健康、临床决策支持和生物医学研究等。通过提高生物医学多模态大语言模型的安全性，能够更好地保护患者隐私，减少错误信息的传播，从而提升医疗服务的质量和安全性。未来，该研究可能推动相关领域在数据隐私和模型安全性方面的进一步探索与发展。

## 📄 摘要（原文）

> The security of biomedical Multimodal Large Language Models (MLLMs) has attracted increasing attention. However, training samples easily contain private information and incorrect knowledge that are difficult to detect, potentially leading to privacy leakage or erroneous outputs after deployment. An intuitive idea is to reprocess the training set to remove unwanted content and retrain the model from scratch. Yet, this is impractical due to significant computational costs, especially for large language models. Machine unlearning has emerged as a solution to this problem, which avoids complete retraining by selectively removing undesired knowledge derived from harmful samples while preserving required capabilities on normal cases. However, there exist no available datasets to evaluate the unlearning quality for security protection in biomedical MLLMs. To bridge this gap, we propose the first benchmark Multimodal Large Language Model Unlearning for BioMedicine (MLLMU-Med) built upon our novel data generation pipeline that effectively integrates synthetic private data and factual errors into the training set. Our benchmark targets two key scenarios: 1) Privacy protection, where patient private information is mistakenly included in the training set, causing models to unintentionally respond with private data during inference; and 2) Incorrectness removal, where wrong knowledge derived from unreliable sources is embedded into the dataset, leading to unsafe model responses. Moreover, we propose a novel Unlearning Efficiency Score that directly reflects the overall unlearning performance across different subsets. We evaluate five unlearning approaches on MLLMU-Med and find that these methods show limited effectiveness in removing harmful knowledge from biomedical MLLMs, indicating significant room for improvement. This work establishes a new pathway for further research in this promising field.

