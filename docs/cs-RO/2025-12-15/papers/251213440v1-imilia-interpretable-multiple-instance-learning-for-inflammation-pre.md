---
layout: default
title: IMILIA: interpretable multiple instance learning for inflammation prediction in IBD from H&E whole slide images
---

# IMILIA: interpretable multiple instance learning for inflammation prediction in IBD from H&E whole slide images

**arXiv**: [2512.13440v1](https://arxiv.org/abs/2512.13440) | [PDF](https://arxiv.org/pdf/2512.13440.pdf)

**作者**: Thalyssa Baiocco-Rodrigues, Antoine Olivier, Reda Belbahri, Thomas Duboudin, Pierre-Antoine Bannier, Benjamin Adjadj, Katharina Von Loga, Nathan Noiry, Maxime Touzot, Hector Roux de Bezieux

---

## 💡 一句话要点

**提出IMILIA框架，用于从H&E全切片图像预测IBD炎症并解释预测结果。**

**关键词**: `炎症性肠病` `多示例学习` `全切片图像分析` `可解释性AI` `组织病理学`

## 📋 核心要点

1. 核心问题：IBD治疗转向组织学缓解，需准确评估微观炎症以指导治疗。
2. 方法要点：结合多示例学习预测炎症，通过细胞检测和上皮分割模块提供可解释性。
3. 实验或效果：在发现队列中ROC-AUC为0.83，外部验证队列中最高达0.99，可解释结果与生物学一致。

## 📄 摘要（原文）

> As the therapeutic target for Inflammatory Bowel Disease (IBD) shifts toward histologic remission, the accurate assessment of microscopic inflammation has become increasingly central for evaluating disease activity and response to treatment. In this work, we introduce IMILIA (Interpretable Multiple Instance Learning for Inflammation Analysis), an end-to-end framework designed for the prediction of inflammation presence in IBD digitized slides stained with hematoxylin and eosin (H&E), followed by the automated computation of markers characterizing tissue regions driving the predictions. IMILIA is composed of an inflammation prediction module, consisting of a Multiple Instance Learning (MIL) model, and an interpretability module, divided in two blocks: HistoPLUS, for cell instance detection, segmentation and classification; and EpiSeg, for epithelium segmentation. IMILIA achieves a cross-validation ROC-AUC of 0.83 on the discovery cohort, and a ROC-AUC of 0.99 and 0.84 on two external validation cohorts. The interpretability module yields biologically consistent insights: tiles with higher predicted scores show increased densities of immune cells (lymphocytes, plasmocytes, neutrophils and eosinophils), whereas lower-scored tiles predominantly contain normal epithelial cells. Notably, these patterns were consistent across all datasets. Code and models to partially replicate the results on the public IBDColEpi dataset can be found at https://github.com/owkin/imilia.

