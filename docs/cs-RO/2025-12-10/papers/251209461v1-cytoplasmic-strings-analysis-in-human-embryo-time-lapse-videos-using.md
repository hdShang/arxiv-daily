---
layout: default
title: Cytoplasmic Strings Analysis in Human Embryo Time-Lapse Videos using Deep Learning Framework
---

# Cytoplasmic Strings Analysis in Human Embryo Time-Lapse Videos using Deep Learning Framework

**arXiv**: [2512.09461v1](https://arxiv.org/abs/2512.09461) | [PDF](https://arxiv.org/pdf/2512.09461.pdf)

**作者**: Anabia Sohail, Mohamad Alansari, Ahmed Abughali, Asmaa Chehab, Abdelfatah Ahmed, Divya Velayudhan, Sajid Javed, Hasan Al Marzouqi, Ameena Saad Al-Sumaiti, Junaid Kashir, Naoufel Werghi

---

## 💡 一句话要点

**提出基于深度学习的细胞质丝分析框架，用于人类胚胎延时视频中的自动化评估。**

**关键词**: `胚胎选择` `细胞质丝检测` `深度学习框架` `不确定性损失` `延时视频分析` `医学图像处理`

## 📋 核心要点

1. 核心问题：胚胎选择依赖手动检查细胞质丝，存在主观性和效率低下的瓶颈。
2. 方法要点：设计两阶段深度学习框架，结合NUCE损失处理数据不平衡和特征不确定性。
3. 实验或效果：在稀疏阳性数据上实现SOTA检测性能，提升F1分数并开源代码。

## 📄 摘要（原文）

> Infertility is a major global health issue, and while in-vitro fertilization has improved treatment outcomes, embryo selection remains a critical bottleneck. Time-lapse imaging enables continuous, non-invasive monitoring of embryo development, yet most automated assessment methods rely solely on conventional morphokinetic features and overlook emerging biomarkers. Cytoplasmic Strings, thin filamentous structures connecting the inner cell mass and trophectoderm in expanded blastocysts, have been associated with faster blastocyst formation, higher blastocyst grades, and improved viability. However, CS assessment currently depends on manual visual inspection, which is labor-intensive, subjective, and severely affected by detection and subtle visual appearance. In this work, we present, to the best of our knowledge, the first computational framework for CS analysis in human IVF embryos. We first design a human-in-the-loop annotation pipeline to curate a biologically validated CS dataset from TLI videos, comprising 13,568 frames with highly sparse CS-positive instances. Building on this dataset, we propose a two-stage deep learning framework that (i) classifies CS presence at the frame level and (ii) localizes CS regions in positive cases. To address severe imbalance and feature uncertainty, we introduce the Novel Uncertainty-aware Contractive Embedding (NUCE) loss, which couples confidence-aware reweighting with an embedding contraction term to form compact, well-separated class clusters. NUCE consistently improves F1-score across five transformer backbones, while RF-DETR-based localization achieves state-of-the-art (SOTA) detection performance for thin, low-contrast CS structures. The source code will be made publicly available at: https://github.com/HamadYA/CS_Detection.

