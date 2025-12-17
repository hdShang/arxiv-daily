---
layout: default
title: Dual Cross-Attention Siamese Transformer for Rectal Tumor Regrowth Assessment in Watch-and-Wait Endoscopy
---

# Dual Cross-Attention Siamese Transformer for Rectal Tumor Regrowth Assessment in Watch-and-Wait Endoscopy

**arXiv**: [2512.03883v1](https://arxiv.org/abs/2512.03883) | [PDF](https://arxiv.org/pdf/2512.03883.pdf)

**作者**: Jorge Tapias Gomez, Despoina Kanata, Aneesh Rangnekar, Christina Lee, Julio Garcia-Aguilar, Joshua Jesse Smith, Harini Veeraraghavan

---

## 💡 一句话要点

**提出双交叉注意力孪生Swin Transformer，用于直肠癌观察等待内镜中的肿瘤再生评估。**

**关键词**: `直肠癌再生评估` `孪生Transformer` `双交叉注意力` `内镜图像分析` `纵向医学影像` `Swin Transformer`

## 📋 核心要点

1. 核心问题：直肠癌观察等待期间，从随访内镜图像中早期检测局部再生缺乏客观准确方法。
2. 方法要点：使用孪生Swin Transformer结合双交叉注意力，无需图像空间对齐，整合纵向图像特征。
3. 实验或效果：在62名患者测试集上，模型平衡准确率达81.76%，对图像伪影具有鲁棒性。

## 📄 摘要（原文）

> Increasing evidence supports watch-and-wait (WW) surveillance for patients with rectal cancer who show clinical complete response (cCR) at restaging following total neoadjuvant treatment (TNT). However, objectively accurate methods to early detect local regrowth (LR) from follow-up endoscopy images during WW are essential to manage care and prevent distant metastases. Hence, we developed a Siamese Swin Transformer with Dual Cross-Attention (SSDCA) to combine longitudinal endoscopic images at restaging and follow-up and distinguish cCR from LR. SSDCA leverages pretrained Swin transformers to extract domain agnostic features and enhance robustness to imaging variations. Dual cross attention is implemented to emphasize features from the two scans without requiring any spatial alignment of images to predict response. SSDCA as well as Swin-based baselines were trained using image pairs from 135 patients and evaluated on a held-out set of image pairs from 62 patients. SSDCA produced the best balanced accuracy (81.76\% $\pm$ 0.04), sensitivity (90.07\% $\pm$ 0.08), and specificity (72.86\% $\pm$ 0.05). Robustness analysis showed stable performance irrespective of artifacts including blood, stool, telangiectasia, and poor image quality. UMAP clustering of extracted features showed maximal inter-cluster separation (1.45 $\pm$ 0.18) and minimal intra-cluster dispersion (1.07 $\pm$ 0.19) with SSDCA, confirming discriminative representation learning.

