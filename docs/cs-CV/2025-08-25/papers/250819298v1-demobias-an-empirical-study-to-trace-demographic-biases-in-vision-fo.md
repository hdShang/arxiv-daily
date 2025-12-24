---
layout: default
title: "DemoBias: An Empirical Study to Trace Demographic Biases in Vision Foundation Models"
---

# DemoBias: An Empirical Study to Trace Demographic Biases in Vision Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19298" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19298v1</a>
  <a href="https://arxiv.org/pdf/2508.19298.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19298v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19298v1', 'DemoBias: An Empirical Study to Trace Demographic Biases in Vision Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abu Sufian, Anirudha Ghosh, Debaditya Barman, Marco Leo, Cosimo Distante

**分类**: cs.CV, cs.AI

**发布日期**: 2025-08-25

**备注**: 6 pages, 4 figures, 13th International Workshop on Biometrics and Forensics (IWBF)

**DOI**: [10.1109/IWBF63717.2025.11113455](https://doi.org/10.1109/IWBF63717.2025.11113455)

**🔗 代码/项目**: [GITHUB](https://github.com/Sufianlab/DemoBias)

---

## 💡 一句话要点

**提出DemoBias以追踪视觉基础模型中的人口统计偏见问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `视觉语言模型` `人口统计偏见` `生物识别` `公平性评估` `模型微调`

## 📋 核心要点

1. 现有的视觉语言模型在处理不同人口群体时存在显著的表现差异，尤其是在生物识别面部识别任务中。
2. 本研究通过微调和评估三种预训练的LVLMs，构建了一个人口统计平衡的数据集，以量化模型的偏见程度。
3. 实验结果显示，PaliGemma和LLaVA在某些群体（如西班牙裔/拉丁裔、白人和南亚人）中表现出更高的偏见，而BLIP-2则相对一致。

## 📝 摘要（中文）

大型视觉语言模型（LVLMs）在各种下游任务中表现出色，尤其是在生物识别面部识别（FR）任务中。然而，人口统计偏见仍然是FR中的一个重要问题，因为这些基础模型在不同人口群体（如种族、性别和年龄）中的表现往往不均衡。通过DemoBias，我们进行了实证评估，研究LVLMs在生物识别FR与文本生成任务中的人口统计偏见程度。我们对三种广泛使用的预训练LVLMs（LLaVA、BLIP-2和PaliGemma）进行了微调和评估，并利用自生成的人口统计平衡数据集。我们采用了多种评估指标，如群体特定的BERTScores和公平性差异率，以量化和追踪性能差异。实验结果揭示了LVLMs在不同人口群体中的公平性和可靠性问题。

## 🔬 方法详解

**问题定义**：本研究旨在解决大型视觉语言模型在生物识别面部识别任务中存在的人口统计偏见问题。现有方法未能有效评估不同人口群体的公平性，导致模型在某些群体中的表现不佳。

**核心思路**：通过构建一个人口统计平衡的数据集，并对三种预训练的LVLMs进行微调和评估，研究其在生物识别FR任务中的表现差异。这样设计的目的是为了系统性地量化和追踪模型的偏见。

**技术框架**：整体架构包括数据集构建、模型微调和评估三个主要阶段。首先生成一个平衡的数据集，然后对LLaVA、BLIP-2和PaliGemma进行微调，最后使用多种评估指标进行性能评估。

**关键创新**：本研究的创新点在于通过群体特定的BERTScores和公平性差异率等指标，系统地量化和分析了LVLMs在不同人口群体中的表现差异。这种方法与传统的单一性能评估方法有本质区别。

**关键设计**：在模型微调过程中，采用了特定的损失函数和参数设置，以确保模型在不同群体上的表现尽可能均衡。具体的网络结构和超参数设置在实验中进行了详细记录。

## 📊 实验亮点

实验结果表明，PaliGemma和LLaVA在西班牙裔/拉丁裔、白人和南亚人群体中表现出较高的偏见，具体表现为在这些群体上的性能差异显著。而BLIP-2在各个群体中的表现相对一致，显示出更好的公平性。整体评估指标如公平性差异率提供了对模型表现的深入洞察。

## 🎯 应用场景

该研究的潜在应用领域包括生物识别技术、社交媒体内容审核和人脸识别系统等。通过识别和减轻模型中的人口统计偏见，可以提高这些系统的公平性和可靠性，从而增强用户信任和社会接受度。未来，该研究可能推动更广泛的公平性评估标准在AI模型中的应用。

## 📄 摘要（原文）

> Large Vision Language Models (LVLMs) have demonstrated remarkable capabilities across various downstream tasks, including biometric face recognition (FR) with description. However, demographic biases remain a critical concern in FR, as these foundation models often fail to perform equitably across diverse demographic groups, considering ethnicity/race, gender, and age. Therefore, through our work DemoBias, we conduct an empirical evaluation to investigate the extent of demographic biases in LVLMs for biometric FR with textual token generation tasks. We fine-tuned and evaluated three widely used pre-trained LVLMs: LLaVA, BLIP-2, and PaliGemma on our own generated demographic-balanced dataset. We utilize several evaluation metrics, like group-specific BERTScores and the Fairness Discrepancy Rate, to quantify and trace the performance disparities. The experimental results deliver compelling insights into the fairness and reliability of LVLMs across diverse demographic groups. Our empirical study uncovered demographic biases in LVLMs, with PaliGemma and LLaVA exhibiting higher disparities for Hispanic/Latino, Caucasian, and South Asian groups, whereas BLIP-2 demonstrated comparably consistent. Repository: https://github.com/Sufianlab/DemoBias.

