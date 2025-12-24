---
layout: default
title: "ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data"
---

# ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15221" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15221v2</a>
  <a href="https://arxiv.org/pdf/2509.15221.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15221v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15221v2', 'ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhaoyang Liu, Jingjing Xie, Zichen Ding, Zehao Li, Bowen Yang, Zhenyu Wu, Xuehui Wang, Qiushi Sun, Shi Liu, Weiyun Wang, Shenglong Ye, Qingyun Li, Xuan Dong, Yue Yu, Chenyu Lu, YunXiang Mo, Yao Yan, Zeyue Tian, Xiao Zhang, Yuan Huang, Yiqian Liu, Weijie Su, Gen Luo, Xiangyu Yue, Biqing Qi, Kai Chen, Bowen Zhou, Yu Qiao, Qifeng Chen, Wenhai Wang

**分类**: cs.CV

**发布日期**: 2025-09-18 (更新: 2025-09-19)

**🔗 代码/项目**: [GITHUB](https://github.com/OpenGVLab/ScaleCUA)

---

## 💡 一句话要点

**ScaleCUA：通过跨平台数据扩展开源计算机使用Agent**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `计算机使用Agent` `跨平台` `视觉-语言模型` `大规模数据集` `自动化` `人机协作` `GUI操作`

## 📋 核心要点

1. 现有计算机使用Agent受限于缺乏大规模开源数据和通用基础模型，阻碍了其在多平台上的应用。
2. ScaleCUA通过闭环流程，结合自动化Agent和人工专家，构建了跨平台、多任务的大规模数据集。
3. ScaleCUA在多个基准测试中显著超越现有方法，并在MMBench-GUI、OSWorld-G和WebArena-Lite-v2上取得了领先成果。

## 📝 摘要（中文）

视觉-语言模型(VLM)已经实现了能够自主操作GUI的计算机使用Agent(CUA)，展现出巨大的潜力，但由于缺乏大规模的开源计算机使用数据和基础模型，进展受到限制。本文介绍了ScaleCUA，旨在扩展开源CUA。它提供了一个跨越6个操作系统和3个任务领域的大规模数据集，该数据集通过一个将自动化Agent与人类专家相结合的闭环流程构建。基于这个扩展的数据集训练的ScaleCUA可以在不同平台之间无缝运行。具体而言，它在基线上实现了显著的提升（WebArena-Lite-v2上+26.6，ScreenSpot-Pro上+10.7），并取得了新的state-of-the-art结果（MMBench-GUI L1-Hard上94.4%，OSWorld-G上60.6%，WebArena-Lite-v2上47.4%）。这些发现强调了数据驱动的扩展对于通用计算机使用Agent的强大作用。我们将发布数据、模型和代码，以促进未来的研究。

## 🔬 方法详解

**问题定义**：现有计算机使用Agent(CUA)的性能提升受限于训练数据的规模和多样性，特别是缺乏跨多个操作系统和任务领域的大规模开源数据集。这限制了CUA的泛化能力和实际应用范围。现有方法难以有效利用不同平台的数据，并且缺乏统一的训练框架。

**核心思路**：ScaleCUA的核心思路是通过构建一个大规模、跨平台的数据集，并利用该数据集训练一个通用的CUA模型。通过闭环流程，自动化Agent生成数据，人工专家进行验证和修正，从而保证数据的质量和多样性。这种数据驱动的方法旨在提升CUA在不同平台和任务上的性能。

**技术框架**：ScaleCUA的整体框架包含以下几个主要模块：1) 数据生成模块：使用自动化Agent在不同操作系统和任务领域生成计算机使用数据。2) 数据验证模块：人工专家对生成的数据进行验证和修正，确保数据的质量。3) 模型训练模块：使用大规模数据集训练CUA模型，使其具备跨平台的操作能力。4) 评估模块：在多个基准测试中评估CUA模型的性能。

**关键创新**：ScaleCUA的关键创新在于构建了一个大规模、高质量、跨平台的数据集，并提出了一个有效的数据生成和验证流程。此外，ScaleCUA还探索了如何利用该数据集训练一个通用的CUA模型，使其能够在不同操作系统和任务领域中无缝运行。该方法强调了数据驱动对于提升CUA性能的重要性。

**关键设计**：ScaleCUA的数据集包含6个操作系统和3个任务领域。数据生成过程采用自动化Agent，并结合人工专家的验证和修正。模型训练采用标准的视觉-语言模型架构，并针对计算机使用任务进行了优化。具体的参数设置、损失函数和网络结构等技术细节在论文中进行了详细描述（具体细节未知）。

## 📊 实验亮点

ScaleCUA在WebArena-Lite-v2上取得了47.4%的成功率，相比基线提升了26.6%。在ScreenSpot-Pro上，成功率提升了10.7%。此外，ScaleCUA还在MMBench-GUI L1-Hard和OSWorld-G上取得了新的state-of-the-art结果，分别为94.4%和60.6%。这些结果表明，ScaleCUA在跨平台计算机使用Agent方面具有显著的优势。

## 🎯 应用场景

ScaleCUA的研究成果可应用于自动化测试、远程协助、智能家居控制等领域。通过让Agent自主操作计算机，可以大幅提升工作效率，降低人力成本。未来，该技术有望进一步发展，实现更加智能和个性化的计算机使用体验，例如辅助残疾人士使用电脑。

## 📄 摘要（原文）

> Vision-Language Models (VLMs) have enabled computer use agents (CUAs) that operate GUIs autonomously, showing great potential, yet progress is limited by the lack of large-scale, open-source computer use data and foundation models. In this work, we introduce ScaleCUA, a step toward scaling open-source CUAs. It offers a large-scale dataset spanning 6 operating systems and 3 task domains, built via a closed-loop pipeline uniting automated agents with human experts. Trained on this scaled-up data, ScaleCUA can operate seamlessly across platforms. Specifically, it delivers strong gains over baselines (+26.6 on WebArena-Lite-v2, +10.7 on ScreenSpot-Pro) and sets new state-of-the-art results (94.4% on MMBench-GUI L1-Hard, 60.6% on OSWorld-G, 47.4% on WebArena-Lite-v2). These findings underscore the power of data-driven scaling for general-purpose computer use agents. We will release data, models, and code to advance future research: https://github.com/OpenGVLab/ScaleCUA.

