---
layout: default
title: Multimodal Oncology Agent for IDH1 Mutation Prediction in Low-Grade Glioma
---

# Multimodal Oncology Agent for IDH1 Mutation Prediction in Low-Grade Glioma

**arXiv**: [2512.05824v1](https://arxiv.org/abs/2512.05824) | [PDF](https://arxiv.org/pdf/2512.05824.pdf)

**作者**: Hafsa Akebli, Adam Shephard, Vincenzo Della Mea, Nasir Rajpoot

---

## 💡 一句话要点

**提出多模态肿瘤学代理，整合组织学工具与外部生物医学知识，预测低级别胶质瘤IDH1突变。**

**关键词**: `多模态肿瘤学代理` `IDH1突变预测` `低级别胶质瘤` `组织学分析` `外部知识整合` `TCGA-LGG`

## 📋 核心要点

1. 核心问题：低级别胶质瘤IDH1突变预测，对临床预后和治疗有重要意义。
2. 方法要点：结合TITAN基础模型的组织学工具，通过PubMed等外部源推理临床和基因组数据。
3. 实验或效果：在TCGA-LGG队列评估，融合组织学特征后F1分数达0.912，优于基线方法。

## 📄 摘要（原文）

> Low-grade gliomas frequently present IDH1 mutations that define clinically distinct subgroups with specific prognostic and therapeutic implications. This work introduces a Multimodal Oncology Agent (MOA) integrating a histology tool based on the TITAN foundation model for IDH1 mutation prediction in low-grade glioma, combined with reasoning over structured clinical and genomic inputs through PubMed, Google Search, and OncoKB. MOA reports were quantitatively evaluated on 488 patients from the TCGA-LGG cohort against clinical and histology baselines. MOA without the histology tool outperformed the clinical baseline, achieving an F1-score of 0.826 compared to 0.798. When fused with histology features, MOA reached the highest performance with an F1-score of 0.912, exceeding both the histology baseline at 0.894 and the fused histology-clinical baseline at 0.897. These results demonstrate that the proposed agent captures complementary mutation-relevant information enriched through external biomedical sources, enabling accurate IDH1 mutation prediction.

