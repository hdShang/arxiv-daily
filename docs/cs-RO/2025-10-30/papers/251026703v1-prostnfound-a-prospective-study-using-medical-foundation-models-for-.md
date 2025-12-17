---
layout: default
title: ProstNFound+: A Prospective Study using Medical Foundation Models for Prostate Cancer Detection
---

# ProstNFound+: A Prospective Study using Medical Foundation Models for Prostate Cancer Detection

**arXiv**: [2510.26703v1](https://arxiv.org/abs/2510.26703) | [PDF](https://arxiv.org/pdf/2510.26703.pdf)

**作者**: Paul F. R. Wilson, Mohamed Harmanani, Minh Nguyen Nhat To, Amoon Jamzad, Tarek Elghareb, Zhuoxin Guo, Adam Kinnaird, Brian Wodlinger, Purang Abolmaesumi, Parvin Mousavi

---

## 💡 一句话要点

**提出ProstNFound+以解决前列腺癌微超声检测的临床验证问题**

**关键词**: `前列腺癌检测` `医学基础模型` `微超声成像` `适配器调优` `前瞻性验证` `癌症热图`

## 📋 核心要点

1. 核心问题：医学基础模型在前列腺癌微超声检测中的临床应用未经验证
2. 方法要点：结合医学基础模型、适配器调优和临床生物标志物提示编码
3. 实验或效果：前瞻性验证显示强泛化能力，与临床评分一致

## 📄 摘要（原文）

> Purpose: Medical foundation models (FMs) offer a path to build
> high-performance diagnostic systems. However, their application to prostate
> cancer (PCa) detection from micro-ultrasound ({\mu}US) remains untested in
> clinical settings. We present ProstNFound+, an adaptation of FMs for PCa
> detection from {\mu}US, along with its first prospective validation. Methods:
> ProstNFound+ incorporates a medical FM, adapter tuning, and a custom prompt
> encoder that embeds PCa-specific clinical biomarkers. The model generates a
> cancer heatmap and a risk score for clinically significant PCa. Following
> training on multi-center retrospective data, the model is prospectively
> evaluated on data acquired five years later from a new clinical site. Model
> predictions are benchmarked against standard clinical scoring protocols
> (PRI-MUS and PI-RADS). Results: ProstNFound+ shows strong generalization to the
> prospective data, with no performance degradation compared to retrospective
> evaluation. It aligns closely with clinical scores and produces interpretable
> heatmaps consistent with biopsy-confirmed lesions. Conclusion: The results
> highlight its potential for clinical deployment, offering a scalable and
> interpretable alternative to expert-driven protocols.

