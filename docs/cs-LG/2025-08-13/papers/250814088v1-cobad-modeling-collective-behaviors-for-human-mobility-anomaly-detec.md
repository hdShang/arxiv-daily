---
layout: default
title: "CoBAD: Modeling Collective Behaviors for Human Mobility Anomaly Detection"
---

# CoBAD: Modeling Collective Behaviors for Human Mobility Anomaly Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14088" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14088v1</a>
  <a href="https://arxiv.org/pdf/2508.14088.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14088v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14088v1', 'CoBAD: Modeling Collective Behaviors for Human Mobility Anomaly Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haomin Wen, Shurui Cao, Leman Akoglu

**分类**: cs.LG, cs.AI, cs.SI

**发布日期**: 2025-08-13

**🔗 代码/项目**: [GITHUB](https://github.com/wenhaomin/CoBAD)

---

## 💡 一句话要点

**提出CoBAD以解决人类移动异常检测中的集体行为建模问题**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `人类移动` `异常检测` `集体行为` `无监督学习` `注意力机制` `数据分析` `公共安全`

## 📋 核心要点

1. 现有的异常检测方法主要集中在个体行为上，缺乏对集体行为的建模，导致无法有效识别集体移动中的异常现象。
2. CoBAD模型通过无监督学习和双阶段注意力机制，能够同时捕捉个体行为和个体间的交互，从而提高集体异常检测的准确性。
3. 在大规模移动数据集上的实验表明，CoBAD在AUCROC和AUCPR指标上均有显著提升，验证了其有效性和优越性。

## 📝 摘要（中文）

检测人类移动中的异常现象对于公共安全和城市规划等应用至关重要。传统的异常检测方法主要关注个体运动模式，而集体异常检测则旨在识别个体间集体移动行为中的不规则性。为了解决这一挑战，本文提出了CoBAD模型，旨在捕捉人类移动异常检测中的集体行为。CoBAD通过无监督学习对集体事件序列进行建模，并采用双阶段注意力机制来同时建模个体移动模式和个体间的交互。实验结果表明，CoBAD在大规模移动数据集上显著优于现有基线，AUCROC提升13%-18%，AUCPR提升19%-70%。

## 🔬 方法详解

**问题定义**：本文旨在解决人类移动异常检测中的集体行为建模问题。现有方法主要关注个体行为，未能有效识别个体间的集体异常，导致检测效果不佳。

**核心思路**：CoBAD模型通过无监督学习对集体事件序列进行建模，利用双阶段注意力机制捕捉个体行为与个体间交互，旨在提高集体异常检测的准确性。

**技术框架**：CoBAD的整体架构包括两个主要阶段：首先，通过构建共现事件图对集体事件序列进行建模；其次，采用双阶段注意力机制，分别建模个体行为和个体间的交互。

**关键创新**：CoBAD的核心创新在于其对集体行为的建模能力，特别是对缺失异常的检测，这在以往研究中被忽视。与传统方法相比，CoBAD能够更全面地捕捉集体移动中的异常现象。

**关键设计**：CoBAD在训练过程中采用了大规模集体行为数据，通过掩码事件和链接重建任务进行预训练，确保模型能够有效学习到个体行为和交互特征。

## 📊 实验亮点

CoBAD在大规模移动数据集上的实验结果显示，其在AUCROC指标上提升了13%-18%，在AUCPR指标上提升了19%-70%，显著优于现有的异常检测基线，验证了其在集体行为异常检测中的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括公共安全监控、城市交通管理和社会行为分析等。通过准确检测人类移动中的异常行为，能够为城市规划和应急响应提供重要支持，提升公共安全水平。未来，该模型还可以扩展到其他领域，如智能交通系统和人群行为分析等。

## 📄 摘要（原文）

> Detecting anomalies in human mobility is essential for applications such as public safety and urban planning. While traditional anomaly detection methods primarily focus on individual movement patterns (e.g., a child should stay at home at night), collective anomaly detection aims to identify irregularities in collective mobility behaviors across individuals (e.g., a child is at home alone while the parents are elsewhere) and remains an underexplored challenge. Unlike individual anomalies, collective anomalies require modeling spatiotemporal dependencies between individuals, introducing additional complexity. To address this gap, we propose CoBAD, a novel model designed to capture Collective Behaviors for human mobility Anomaly Detection. We first formulate the problem as unsupervised learning over Collective Event Sequences (CES) with a co-occurrence event graph, where CES represents the event sequences of related individuals. CoBAD then employs a two-stage attention mechanism to model both the individual mobility patterns and the interactions across multiple individuals. Pre-trained on large-scale collective behavior data through masked event and link reconstruction tasks, CoBAD is able to detect two types of collective anomalies: unexpected co-occurrence anomalies and absence anomalies, the latter of which has been largely overlooked in prior work. Extensive experiments on large-scale mobility datasets demonstrate that CoBAD significantly outperforms existing anomaly detection baselines, achieving an improvement of 13%-18% in AUCROC and 19%-70% in AUCPR. All source code is available at https://github.com/wenhaomin/CoBAD.

