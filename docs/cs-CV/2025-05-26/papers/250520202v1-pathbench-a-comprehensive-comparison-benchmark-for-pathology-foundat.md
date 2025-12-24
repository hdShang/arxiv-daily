---
layout: default
title: PathBench: A comprehensive comparison benchmark for pathology foundation models towards precision oncology
---

# PathBench: A comprehensive comparison benchmark for pathology foundation models towards precision oncology

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.20202" class="toolbar-btn" target="_blank">📄 arXiv: 2505.20202v1</a>
  <a href="https://arxiv.org/pdf/2505.20202.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.20202v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.20202v1', 'PathBench: A comprehensive comparison benchmark for pathology foundation models towards precision oncology')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jiabo Ma, Yingxue Xu, Fengtao Zhou, Yihui Wang, Cheng Jin, Zhengrui Guo, Jianfeng Wu, On Ki Tang, Huajun Zhou, Xi Wang, Luyang Luo, Zhengyu Zhang, Du Cai, Zizhao Gao, Wei Wang, Yueping Liu, Jiankun He, Jing Cui, Zhenhui Li, Jing Zhang, Feng Gao, Xiuming Zhang, Li Liang, Ronald Cheong Kin Chan, Zhe Wang, Hao Chen

**分类**: cs.CV

**发布日期**: 2025-05-26

**备注**: 35 pages, 9 figures

---

## 💡 一句话要点

**提出PathBench以解决病理基础模型评估标准化问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理基础模型` `精准肿瘤学` `全切片图像` `模型评估` `数据泄露防范` `多中心数据集` `自动化评估系统`

## 📋 核心要点

1. 现有的病理基础模型在临床转化中面临最佳模型变异性、数据泄露风险和缺乏标准化评估等挑战。
2. PathBench通过多中心数据集和严格的评估标准，提供了一个全面的基准测试框架，解决了现有方法的不足。
3. 实验结果显示，Virchow2和H-Optimus-1是当前评估的19个PFM中表现最优的模型，具有显著的临床应用潜力。

## 📝 摘要（中文）

病理基础模型的出现彻底改变了计算机组织病理学，使得全切片图像分析在癌症诊断和预后评估中具有高度准确性和广泛适用性。然而，这些模型在临床转化中面临诸多挑战，包括不同癌症类型的最佳模型变异性、评估中的潜在数据泄露以及缺乏标准化基准。为了解决这些问题，本文提出了PathBench，这是第一个全面的基准测试框架，涵盖多中心内部数据集，严格防止数据泄露，评估从诊断到预后的整个临床范围，并提供自动化的排行榜系统以持续评估模型。通过收集来自10家医院的15,888个全切片图像，本文为研究人员提供了一个强大的模型开发平台，并为临床医生提供了在多种临床场景下PFM性能的可操作见解。

## 🔬 方法详解

**问题定义**：本文旨在解决病理基础模型在临床应用中的评估标准化问题。现有方法存在评估偏差、数据泄露风险以及缺乏全面覆盖的局限性。

**核心思路**：PathBench的核心思路是通过构建多中心数据集和自动化评估系统，确保模型评估的客观性和全面性，从而提高临床转化的效率。

**技术框架**：整体架构包括数据收集、数据预处理、模型评估和自动化排行榜四个主要模块。数据来自10家医院，涵盖多种癌症类型，确保了评估的广泛性。

**关键创新**：PathBench的创新在于其严格的数据泄露防范措施和多任务评估能力，使其成为第一个全面覆盖癌症诊断与预后的基准测试框架。

**关键设计**：在数据收集阶段，排除了任何预训练数据的使用，以避免数据泄露风险；在评估阶段，采用了多种性能指标，确保模型在不同临床场景下的有效性。

## 📊 实验亮点

在对19个病理基础模型的评估中，Virchow2和H-Optimus-1表现最佳，显示出显著的性能优势。这一结果为临床医生在选择和应用PFM提供了重要的实证依据，推动了精准肿瘤学的发展。

## 🎯 应用场景

PathBench的研究成果可以广泛应用于癌症诊断和预后评估的临床实践中，帮助医生选择最佳的病理基础模型，从而提高患者的治疗效果和生存率。此外，该基准测试框架还为后续的模型开发和优化提供了重要参考，推动了病理学领域的技术进步。

## 📄 摘要（原文）

> The emergence of pathology foundation models has revolutionized computational histopathology, enabling highly accurate, generalized whole-slide image analysis for improved cancer diagnosis, and prognosis assessment. While these models show remarkable potential across cancer diagnostics and prognostics, their clinical translation faces critical challenges including variability in optimal model across cancer types, potential data leakage in evaluation, and lack of standardized benchmarks. Without rigorous, unbiased evaluation, even the most advanced PFMs risk remaining confined to research settings, delaying their life-saving applications. Existing benchmarking efforts remain limited by narrow cancer-type focus, potential pretraining data overlaps, or incomplete task coverage. We present PathBench, the first comprehensive benchmark addressing these gaps through: multi-center in-hourse datasets spanning common cancers with rigorous leakage prevention, evaluation across the full clinical spectrum from diagnosis to prognosis, and an automated leaderboard system for continuous model assessment. Our framework incorporates large-scale data, enabling objective comparison of PFMs while reflecting real-world clinical complexity. All evaluation data comes from private medical providers, with strict exclusion of any pretraining usage to avoid data leakage risks. We have collected 15,888 WSIs from 8,549 patients across 10 hospitals, encompassing over 64 diagnosis and prognosis tasks. Currently, our evaluation of 19 PFMs shows that Virchow2 and H-Optimus-1 are the most effective models overall. This work provides researchers with a robust platform for model development and offers clinicians actionable insights into PFM performance across diverse clinical scenarios, ultimately accelerating the translation of these transformative technologies into routine pathology practice.

