---
layout: default
title: NeuralBoneReg: A Novel Self-Supervised Method for Robust and Accurate Multi-Modal Bone Surface Registration
---

# NeuralBoneReg: A Novel Self-Supervised Method for Robust and Accurate Multi-Modal Bone Surface Registration

**arXiv**: [2511.14286v1](https://arxiv.org/abs/2511.14286) | [PDF](https://arxiv.org/pdf/2511.14286.pdf)

**作者**: Luohong Wu, Matthias Seibold, Nicola A. Cavalcanti, Yunke Ao, Roman Flepp, Aidana Massalimova, Lilian Calvet, Philipp Fürnstahl

---

## 💡 一句话要点

**提出NeuralBoneReg自监督方法以解决骨科手术中多模态骨表面配准问题**

**关键词**: `骨表面配准` `自监督学习` `多模态配准` `隐式神经表示` `骨科手术辅助`

## 📋 核心要点

1. 核心问题：骨科手术中术前与术中数据模态差异大，导致配准困难且易出错
2. 方法要点：使用隐式神经无符号距离场和MLP模块，实现自监督的全局初始化和局部细化配准
3. 实验或效果：在多个数据集上评估，平均RRE/RTE优于或匹配现有方法，展现强泛化性

## 📄 摘要（原文）

> In computer- and robot-assisted orthopedic surgery (CAOS), patient-specific surgical plans derived from preoperative imaging define target locations and implant trajectories. During surgery, these plans must be accurately transferred, relying on precise cross-registration between preoperative and intraoperative data. However, substantial modality heterogeneity across imaging modalities makes this registration challenging and error-prone. Robust, automatic, and modality-agnostic bone surface registration is therefore clinically important. We propose NeuralBoneReg, a self-supervised, surface-based framework that registers bone surfaces using 3D point clouds as a modality-agnostic representation. NeuralBoneReg includes two modules: an implicit neural unsigned distance field (UDF) that learns the preoperative bone model, and an MLP-based registration module that performs global initialization and local refinement by generating transformation hypotheses to align the intraoperative point cloud with the neural UDF. Unlike SOTA supervised methods, NeuralBoneReg operates in a self-supervised manner, without requiring inter-subject training data. We evaluated NeuralBoneReg against baseline methods on two publicly available multi-modal datasets: a CT-ultrasound dataset of the fibula and tibia (UltraBones100k) and a CT-RGB-D dataset of spinal vertebrae (SpineDepth). The evaluation also includes a newly introduced CT--ultrasound dataset of cadaveric subjects containing femur and pelvis (UltraBones-Hip), which will be made publicly available. NeuralBoneReg matches or surpasses existing methods across all datasets, achieving mean RRE/RTE of 1.68°/1.86 mm on UltraBones100k, 1.88°/1.89 mm on UltraBones-Hip, and 3.79°/2.45 mm on SpineDepth. These results demonstrate strong generalizability across anatomies and modalities, providing robust and accurate cross-modal alignment for CAOS.

