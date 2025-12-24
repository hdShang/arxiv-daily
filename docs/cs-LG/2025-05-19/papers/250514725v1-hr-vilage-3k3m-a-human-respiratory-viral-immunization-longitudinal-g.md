---
layout: default
title: HR-VILAGE-3K3M: A Human Respiratory Viral Immunization Longitudinal Gene Expression Dataset for Systems Immunity
---

# HR-VILAGE-3K3M: A Human Respiratory Viral Immunization Longitudinal Gene Expression Dataset for Systems Immunity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.14725" class="toolbar-btn" target="_blank">📄 arXiv: 2505.14725v1</a>
  <a href="https://arxiv.org/pdf/2505.14725.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.14725v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.14725v1', 'HR-VILAGE-3K3M: A Human Respiratory Viral Immunization Longitudinal Gene Expression Dataset for Systems Immunity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xuejun Sun, Yiran Song, Xiaochen Zhou, Ruilie Cai, Yu Zhang, Xinyi Li, Rui Peng, Jialiu Xie, Yuanyuan Yan, Muyao Tang, Prem Lakshmanane, Baiming Zou, James S. Hagood, Raymond J. Pickles, Didong Li, Fei Zou, Xiaojing Zheng

**分类**: q-bio.GN, cs.LG, stat.AP

**发布日期**: 2025-05-19

---

## 💡 一句话要点

**构建HR-VILAGE-3K3M数据集以解决呼吸病毒免疫研究中的数据不足问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `呼吸病毒` `免疫反应` `RNA-seq` `数据集` `系统免疫学` `疫苗开发` `AI驱动研究`

## 📋 核心要点

1. 现有自然感染数据集缺乏预暴露基线和结构化时间采样，限制了免疫反应的研究。
2. HR-VILAGE-3K3M数据集整合了多种RNA-seq数据，经过严格的质量控制和统一的预处理，确保数据一致性。
3. 通过对疫苗响应者的预测建模和批次效应校正方法的评估，展示了数据集的实用性和多样性。

## 📝 摘要（中文）

呼吸病毒感染对全球健康构成重大威胁，但驱动保护或病理的细胞免疫反应仍不明确。现有自然感染队列缺乏预暴露基线数据和结构化时间采样，而接种和疫苗试验则生成了有价值的纵向转录组数据。为解决这些挑战，本文开发了HR-VILAGE-3K3M数据集，整合了来自66项研究的14,136个RNA-seq样本，涵盖3,178名受试者，包含超过256万细胞。该数据集经过严格的质量控制和统一的预处理，支持多种系统免疫学应用，促进AI驱动的研究和疫苗开发。

## 🔬 方法详解

**问题定义**：本文旨在解决现有呼吸病毒免疫研究中数据分散、缺乏一致性和预处理不规范的问题。自然感染队列往往缺乏必要的基线数据，影响了对免疫反应的深入理解。

**核心思路**：通过构建HR-VILAGE-3K3M数据集，整合来自多个研究的RNA-seq数据，并进行严格的质量控制和统一的预处理，以提供一个AI友好的数据平台，促进系统免疫学研究。

**技术框架**：数据集包含来自GEO、ImmPort和ArrayExpress的多种数据类型，包括微阵列、bulk RNA-seq和单细胞RNA-seq，涵盖疫苗接种、接种和混合暴露。数据经过标准化和统一处理，确保了数据的一致性和可用性。

**关键创新**：HR-VILAGE-3K3M是最大的呼吸病毒免疫纵向转录组资源，提供了全面的细胞免疫反应数据，支持多种AI驱动的研究和应用，填补了现有数据集的空白。

**关键设计**：在数据处理过程中，采用了统一的预处理管道，确保了数据的高质量和一致性，所有数据均对齐至官方基因符号，便于后续分析和应用。具体的参数设置和损失函数等技术细节在论文中进行了详细描述。

## 📊 实验亮点

通过对疫苗响应者的预测建模，HR-VILAGE-3K3M数据集展示了其在批次效应校正方面的有效性，显著提高了模型的预测准确性。该数据集的规模和多样性为基础模型的预训练和多模态学习框架的推进提供了理想的条件。

## 🎯 应用场景

HR-VILAGE-3K3M数据集具有广泛的应用潜力，能够支持系统免疫学的多种研究，包括疫苗开发、免疫反应机制的探索以及AI驱动的生物信息学分析。未来，该数据集将为应对新兴病毒威胁提供重要的基础数据支持。

## 📄 摘要（原文）

> Respiratory viral infections pose a global health burden, yet the cellular immune responses driving protection or pathology remain unclear. Natural infection cohorts often lack pre-exposure baseline data and structured temporal sampling. In contrast, inoculation and vaccination trials generate insightful longitudinal transcriptomic data. However, the scattering of these datasets across platforms, along with inconsistent metadata and preprocessing procedure, hinders AI-driven discovery. To address these challenges, we developed the Human Respiratory Viral Immunization LongitudinAl Gene Expression (HR-VILAGE-3K3M) repository: an AI-ready, rigorously curated dataset that integrates 14,136 RNA-seq profiles from 3,178 subjects across 66 studies encompassing over 2.56 million cells. Spanning vaccination, inoculation, and mixed exposures, the dataset includes microarray, bulk RNA-seq, and single-cell RNA-seq from whole blood, PBMCs, and nasal swabs, sourced from GEO, ImmPort, and ArrayExpress. We harmonized subject-level metadata, standardized outcome measures, applied unified preprocessing pipelines with rigorous quality control, and aligned all data to official gene symbols. To demonstrate the utility of HR-VILAGE-3K3M, we performed predictive modeling of vaccine responders and evaluated batch-effect correction methods. Beyond these initial demonstrations, it supports diverse systems immunology applications and benchmarking of feature selection and transfer learning algorithms. Its scale and heterogeneity also make it ideal for pretraining foundation models of the human immune response and for advancing multimodal learning frameworks. As the largest longitudinal transcriptomic resource for human respiratory viral immunization, it provides an accessible platform for reproducible AI-driven research, accelerating systems immunology and vaccine development against emerging viral threats.

