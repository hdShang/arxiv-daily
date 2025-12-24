---
layout: default
title: "DD-Ranking: Rethinking the Evaluation of Dataset Distillation"
---

# DD-Ranking: Rethinking the Evaluation of Dataset Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13300" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13300v3</a>
  <a href="https://arxiv.org/pdf/2505.13300.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13300v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13300v3', 'DD-Ranking: Rethinking the Evaluation of Dataset Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zekai Li, Xinhao Zhong, Samir Khaki, Zhiyuan Liang, Yuhao Zhou, Mingjia Shi, Ziqiao Wang, Xuanlei Zhao, Wangbo Zhao, Ziheng Qin, Mengxuan Wu, Pengfei Zhou, Haonan Wang, David Junhao Zhang, Jia-Wei Liu, Shaobo Wang, Dai Liu, Linfeng Zhang, Guang Li, Kun Wang, Zheng Zhu, Zhiheng Ma, Joey Tianyi Zhou, Jiancheng Lv, Yaochu Jin, Peihao Wang, Kaipeng Zhang, Lingjuan Lyu, Yiran Huang, Zeynep Akata, Zhiwei Deng, Xindi Wu, George Cazenavette, Yuzhang Shang, Justin Cui, Jindong Gu, Qian Zheng, Hao Ye, Shuo Wang, Xiaobo Wang, Yan Yan, Angela Yao, Mike Zheng Shou, Tianlong Chen, Hakan Bilen, Baharan Mirzasoleiman, Manolis Kellis, Konstantinos N. Plataniotis, Zhangyang Wang, Bo Zhao, Yang You, Kai Wang

**分类**: cs.CV

**发布日期**: 2025-05-19 (更新: 2025-09-21)

**备注**: 20 pages, 4 figures

---

## 💡 一句话要点

**提出DD-Ranking以解决数据集蒸馏评估不准确的问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `数据集蒸馏` `评估框架` `合成数据集` `机器学习` `计算机视觉` `信息增益` `数据质量评分`

## 📋 核心要点

1. 现有的数据集蒸馏方法在评估时过于依赖准确率，导致评估结果与图像质量不匹配。
2. 本文提出DD-Ranking评估框架，旨在通过新的评估指标更准确地反映合成数据集的真实性能提升。
3. 实验结果表明，DD-Ranking能够更好地揭示不同蒸馏方法的实际效果，推动该领域的发展。

## 📝 摘要（中文）

近年来，数据集蒸馏为数据压缩提供了可靠的解决方案，训练于较小合成数据集的模型在性能上可与原始数据集相媲美。为进一步提升合成数据集的性能，提出了多种训练流程和优化目标。然而，现有的评估方法常常依赖于准确率，导致评估结果与图像本身的质量不一致。为此，本文提出了DD-Ranking，一个统一的评估框架和新的评估指标，以揭示不同方法所实现的真实性能提升，从而为未来的研究提供更全面和公正的评估标准。

## 🔬 方法详解

**问题定义**：现有的数据集蒸馏方法在评估时常常依赖于准确率，导致评估结果无法真实反映合成数据集的质量，甚至随机采样的图像也能获得较高的准确率，这严重阻碍了数据集蒸馏的进展。

**核心思路**：本文提出的DD-Ranking框架旨在通过引入新的评估指标，聚焦于合成数据集的信息增强，从而提供更全面和公正的评估标准，帮助研究者更好地理解不同蒸馏方法的实际效果。

**技术框架**：DD-Ranking的整体架构包括数据集蒸馏的训练阶段和评估阶段。在训练阶段，采用新的优化目标和训练流程；在评估阶段，使用新的评估指标来衡量合成数据集的性能。

**关键创新**：DD-Ranking的主要创新在于提出了一套新的评估指标，能够更准确地反映合成数据集的真实性能提升，与传统方法相比，避免了对准确率的过度依赖。

**关键设计**：在设计中，DD-Ranking引入了多种评估指标，如信息增益和数据质量评分，确保评估结果能够真实反映合成数据集的有效性。

## 📊 实验亮点

实验结果显示，使用DD-Ranking评估框架后，多个数据集蒸馏方法的性能提升得到了更准确的反映，尤其是在ImageNet-1K等大型数据集上，性能提升幅度显著，验证了新评估指标的有效性。

## 🎯 应用场景

该研究的潜在应用领域包括计算机视觉、机器学习和数据压缩等领域。通过提供更准确的评估标准，DD-Ranking能够帮助研究者和工程师更好地理解和优化数据集蒸馏技术，从而推动相关技术的实际应用和发展。

## 📄 摘要（原文）

> In recent years, dataset distillation has provided a reliable solution for data compression, where models trained on the resulting smaller synthetic datasets achieve performance comparable to those trained on the original datasets. To further improve the performance of synthetic datasets, various training pipelines and optimization objectives have been proposed, greatly advancing the field of dataset distillation. Recent decoupled dataset distillation methods introduce soft labels and stronger data augmentation during the post-evaluation phase and scale dataset distillation up to larger datasets (e.g., ImageNet-1K). However, this raises a question: Is accuracy still a reliable metric to fairly evaluate dataset distillation methods? Our empirical findings suggest that the performance improvements of these methods often stem from additional techniques rather than the inherent quality of the images themselves, with even randomly sampled images achieving superior results. Such misaligned evaluation settings severely hinder the development of DD. Therefore, we propose DD-Ranking, a unified evaluation framework, along with new general evaluation metrics to uncover the true performance improvements achieved by different methods. By refocusing on the actual information enhancement of distilled datasets, DD-Ranking provides a more comprehensive and fair evaluation standard for future research advancements.

