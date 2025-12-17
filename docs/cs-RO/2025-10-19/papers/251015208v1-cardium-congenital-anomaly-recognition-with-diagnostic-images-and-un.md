---
layout: default
title: CARDIUM: Congenital Anomaly Recognition with Diagnostic Images and Unified Medical records
---

# CARDIUM: Congenital Anomaly Recognition with Diagnostic Images and Unified Medical records

**arXiv**: [2510.15208v1](https://arxiv.org/abs/2510.15208) | [PDF](https://arxiv.org/pdf/2510.15208.pdf)

**作者**: Daniela Vega, Hannah V. Ceballos, Javier S. Vera, Santiago Rodriguez, Alejandra Perez, Angela Castillo, Maria Escobar, Dario Londoño, Luis A. Sarmiento, Camila I. Castro, Nadiezhda Rodriguez, Juan C. Briceño, Pablo Arbeláez

---

## 💡 一句话要点

**提出CARDIUM数据集与多模态Transformer架构，以提升产前先天性心脏病检测性能。**

**关键词**: `先天性心脏病检测` `多模态数据集` `Transformer架构` `跨注意力机制` `产前诊断` `医学影像分析`

## 📋 核心要点

1. 核心问题：产前先天性心脏病诊断数据稀缺、不平衡，且缺乏多模态整合。
2. 方法要点：构建首个公开多模态数据集，融合超声图像与临床记录，采用跨注意力机制融合特征。
3. 实验或效果：在CARDIUM数据集上，多模态方法比单模态提升11%和50%，F1得分达79.8±4.8%。

## 📄 摘要（原文）

> Prenatal diagnosis of Congenital Heart Diseases (CHDs) holds great potential
> for Artificial Intelligence (AI)-driven solutions. However, collecting
> high-quality diagnostic data remains difficult due to the rarity of these
> conditions, resulting in imbalanced and low-quality datasets that hinder model
> performance. Moreover, no public efforts have been made to integrate multiple
> sources of information, such as imaging and clinical data, further limiting the
> ability of AI models to support and enhance clinical decision-making. To
> overcome these challenges, we introduce the Congenital Anomaly Recognition with
> Diagnostic Images and Unified Medical records (CARDIUM) dataset, the first
> publicly available multimodal dataset consolidating fetal ultrasound and
> echocardiographic images along with maternal clinical records for prenatal CHD
> detection. Furthermore, we propose a robust multimodal transformer architecture
> that incorporates a cross-attention mechanism to fuse feature representations
> from image and tabular data, improving CHD detection by 11% and 50% over image
> and tabular single-modality approaches, respectively, and achieving an F1 score
> of 79.8 $\pm$ 4.8% in the CARDIUM dataset. We will publicly release our dataset
> and code to encourage further research on this unexplored field. Our dataset
> and code are available at https://github.com/BCVUniandes/Cardium, and at the
> project website https://bcv-uniandes.github.io/CardiumPage/

