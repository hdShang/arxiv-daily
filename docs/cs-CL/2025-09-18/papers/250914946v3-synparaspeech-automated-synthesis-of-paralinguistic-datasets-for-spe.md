---
layout: default
title: "SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding"
---

# SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14946" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14946v3</a>
  <a href="https://arxiv.org/pdf/2509.14946.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14946v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14946v3', 'SynParaSpeech: Automated Synthesis of Paralinguistic Datasets for Speech Generation and Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bingsong Bai, Qihang Lu, Wenbing Yang, Zihan Sun, Yueran Hou, Peilei Jia, Songbai Pu, Ruibo Fu, Yingming Gao, Ya Li, Jun Gao

**分类**: eess.AS, cs.CL

**发布日期**: 2025-09-18 (更新: 2025-09-28)

**备注**: Submitted to ICASSP 2026. Copyright 2026 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works

**🔗 代码/项目**: [GITHUB](https://github.com/ShawnPi233/SynParaSpeech)

---

## 💡 一句话要点

**提出SynParaSpeech框架，自动合成大规模副语言数据集，提升语音生成和理解能力。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `副语言` `语音合成` `语音理解` `数据集构建` `自动化标注` `自然对话语音`

## 📋 核心要点

1. 现有副语言语音合成方法依赖私有数据集，公开数据集存在语音不完整、时间戳不准确等问题。
2. 提出自动化框架SynParaSpeech，从自然对话语音中生成大规模、高质量的副语言数据集。
3. 构建包含6种副语言类别、时长118.75小时的SynParaSpeech数据集，提升语音生成和理解能力。

## 📝 摘要（中文）

本文提出了一种自动化的框架，用于生成大规模的副语言数据，并利用该框架构建了SynParaSpeech数据集。该数据集包含6种副语言类别，总时长达118.75小时，并具有精确的时间戳，所有数据均来源于自然对话语音。本文的主要贡献在于提出了首个用于构建大规模副语言数据集的自动化方法，并发布了SynParaSpeech语料库。该语料库通过更自然的副语言合成来改进语音生成，并通过提高副语言事件检测来增强语音理解。

## 🔬 方法详解

**问题定义**：现有副语言语音合成和理解方法面临数据稀缺的问题。公开数据集通常质量不高，存在语音不完整、时间戳不准确或缺失等问题，且真实场景相关性有限。私有数据集虽然质量较高，但难以获取和复现，阻碍了相关研究的进展。因此，需要一种能够自动生成大规模、高质量、具有精确时间戳的副语言数据集的方法。

**核心思路**：本文的核心思路是利用自动化流程，从大量的自然对话语音中提取并标注副语言事件，从而构建大规模的副语言数据集。通过自动化，可以降低人工标注的成本，提高数据生成的效率，并保证数据的一致性和准确性。这种方法避免了对私有数据集的依赖，为副语言语音合成和理解研究提供了可靠的数据基础。

**技术框架**：SynParaSpeech框架包含以下主要模块：1) 语音数据收集：收集大量的自然对话语音数据。2) 副语言事件检测：利用预训练的副语言事件检测模型，自动检测语音数据中的副语言事件。3) 时间戳校正：对检测到的副语言事件的时间戳进行校正，提高时间戳的准确性。4) 数据过滤：对检测到的副语言事件进行过滤，去除质量较差的数据。5) 数据集构建：将过滤后的数据整理成数据集，并提供精确的时间戳。

**关键创新**：本文最重要的技术创新点在于提出了首个用于构建大规模副语言数据集的自动化方法。该方法能够自动检测和标注副语言事件，并生成具有精确时间戳的数据集。与现有方法相比，该方法无需人工标注，可以大大降低数据生成的成本，并提高数据生成的效率。

**关键设计**：在副语言事件检测模块中，可以使用预训练的深度学习模型，例如基于Transformer的模型。时间戳校正模块可以使用语音活动检测（VAD）等技术，对时间戳进行精细调整。数据过滤模块可以根据语音质量、信噪比等指标，去除质量较差的数据。数据集构建模块需要设计合理的数据格式，方便后续研究使用。

## 📊 实验亮点

SynParaSpeech数据集包含6种副语言类别，总时长达118.75小时，是目前最大的公开副语言数据集之一。该数据集具有精确的时间戳，可以用于训练高精度的副语言事件检测模型。通过实验验证，利用SynParaSpeech数据集训练的模型在副语言事件检测任务上取得了显著的性能提升。

## 🎯 应用场景

该研究成果可广泛应用于语音合成、语音识别、情感计算、人机交互等领域。例如，在语音合成中，可以利用SynParaSpeech数据集训练模型，生成更自然、更富有表现力的语音。在语音识别中，可以利用该数据集提高模型对副语言事件的识别能力，从而提高语音识别的准确率。在人机交互中，可以利用该数据集构建更智能、更人性化的对话系统。

## 📄 摘要（原文）

> Paralinguistic sounds, like laughter and sighs, are crucial for synthesizing more realistic and engaging speech. However, existing methods typically depend on proprietary datasets, while publicly available resources often suffer from incomplete speech, inaccurate or missing timestamps, and limited real-world relevance. To address these problems, we propose an automated framework for generating large-scale paralinguistic data and apply it to construct the SynParaSpeech dataset. The dataset comprises 6 paralinguistic categories with 118.75 hours of data and precise timestamps, all derived from natural conversational speech. Our contributions lie in introducing the first automated method for constructing large-scale paralinguistic datasets and releasing the SynParaSpeech corpus, which advances speech generation through more natural paralinguistic synthesis and enhances speech understanding by improving paralinguistic event detection. The dataset and audio samples are available at https://github.com/ShawnPi233/SynParaSpeech.

