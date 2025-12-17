---
layout: default
title: Histology-informed tiling of whole tissue sections improves the interpretability and predictability of cancer relapse and genetic alterations
---

# Histology-informed tiling of whole tissue sections improves the interpretability and predictability of cancer relapse and genetic alterations

**arXiv**: [2511.10432v1](https://arxiv.org/abs/2511.10432) | [PDF](https://arxiv.org/pdf/2511.10432.pdf)

**作者**: Willem Bonnaffé, Yang Hu, Andrea Chatrian, Mengran Fan, Stefano Malacrino, Sandy Figiel, CRUK ICGC Prostate Group, Srinivasa R. Rao, Richard Colling, Richard J. Bryant, Freddie C. Hamdy, Dan J. Woodcock, Ian G. Mills, Clare Verrill, Jens Rittscher

---

## 💡 一句话要点

**提出组织学知情分块方法以改进癌症复发和遗传变异的预测与可解释性**

**关键词**: `数字病理学` `多实例学习` `语义分割` `癌症预测` `腺体提取` `可解释性`

## 📋 核心要点

1. 数字病理学中基于网格的分块忽略组织结构，引入无关信息并限制可解释性。
2. 使用语义分割从全切片图像提取腺体作为多实例学习的生物意义输入补丁。
3. 在多个队列中验证，提升模型AUC 10%，并识别与癌症复发相关的腺体簇。

## 📄 摘要（原文）

> Histopathologists establish cancer grade by assessing histological structures, such as glands in prostate cancer. Yet, digital pathology pipelines often rely on grid-based tiling that ignores tissue architecture. This introduces irrelevant information and limits interpretability. We introduce histology-informed tiling (HIT), which uses semantic segmentation to extract glands from whole slide images (WSIs) as biologically meaningful input patches for multiple-instance learning (MIL) and phenotyping. Trained on 137 samples from the ProMPT cohort, HIT achieved a gland-level Dice score of 0.83 +/- 0.17. By extracting 380,000 glands from 760 WSIs across ICGC-C and TCGA-PRAD cohorts, HIT improved MIL models AUCs by 10% for detecting copy number variation (CNVs) in genes related to epithelial-mesenchymal transitions (EMT) and MYC, and revealed 15 gland clusters, several of which were associated with cancer relapse, oncogenic mutations, and high Gleason. Therefore, HIT improved the accuracy and interpretability of MIL predictions, while streamlining computations by focussing on biologically meaningful structures during feature extraction.

