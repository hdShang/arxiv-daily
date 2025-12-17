---
layout: default
title: Adaptable Segmentation Pipeline for Diverse Brain Tumors with Radiomic-guided Subtyping and Lesion-Wise Model Ensemble
---

# Adaptable Segmentation Pipeline for Diverse Brain Tumors with Radiomic-guided Subtyping and Lesion-Wise Model Ensemble

**arXiv**: [2512.14648v1](https://arxiv.org/abs/2512.14648) | [PDF](https://arxiv.org/pdf/2512.14648.pdf)

**作者**: Daniel Capellán-Martín, Abhijeet Parida, Zhifan Jiang, Nishad Kulkarni, Krithika Iyer, Austin Tapp, Syed Muhammad Anwar, María J. Ledesma-Carbayo, Marius George Linguraru

**分类**: cs.CV, eess.IV

**发布日期**: 2025-12-16

**备注**: 12 pages, 5 figures, 3 tables. Algorithm presented at MICCAI BraTS 2025

---

## 💡 一句话要点

**提出可适应脑肿瘤分割流程，通过影像组学引导亚型识别和病灶级模型集成提升多类型肿瘤分割性能。**

**关键词**: `脑肿瘤分割` `多参数MRI` `影像组学` `模型集成` `病灶级处理` `自适应流程` `临床影像分析` `BraTS挑战赛`

## 📋 核心要点

1. 核心问题：脑肿瘤类型多样，现有分割方法难以在MRI上实现稳健且可泛化的分割，尤其是在成人及儿童肿瘤、脑膜瘤和转移瘤等不同数据集上。
2. 方法要点：提出灵活可适应流程，结合影像组学引导亚型识别、病灶级模型集成和定制后处理，针对不同肿瘤类型优化分割步骤。
3. 实验或效果：在BraTS 2025 Lighthouse挑战赛的多个测试集上，性能与顶级算法相当，证实了方法的有效性和泛化能力。

## 📝 摘要（中文）

在多参数磁共振成像（MRI）上实现稳健且可泛化的脑肿瘤分割仍然困难，因为肿瘤类型差异很大。BraTS 2025 Lighthouse挑战赛在多样化的高质量成人及儿童肿瘤数据集上评估分割方法：国际多中心儿童脑肿瘤分割（PED）、术前脑膜瘤分割（MEN）、脑膜瘤放疗分割（MEN-RT）以及治疗前后脑转移瘤分割（MET）。我们提出了一种灵活、模块化且可适应的流程，通过选择和组合最先进的模型，并在训练前后应用肿瘤和病灶特异性处理来提升分割性能。从MRI中提取的影像组学特征有助于检测肿瘤亚型，确保更平衡的训练。定制的病灶级性能指标确定集成中每个模型的影响，并优化进一步细化预测的后处理，使工作流程能够针对每个病例定制每一步。在BraTS测试集上，我们的流程在多个挑战中取得了与排名靠前算法相当的性能。这些发现证实，定制的病灶感知处理和模型选择能够产生稳健的分割，同时不将方法锁定于特定的网络架构。我们的方法在临床实践中具有定量肿瘤测量的潜力，支持诊断和预后。

## 🔬 方法详解

整体框架是一个模块化、可适应的分割流程，包括模型选择、训练优化和预测后处理。关键技术创新点在于：1）利用影像组学特征进行肿瘤亚型检测，以平衡训练数据；2）采用病灶级性能指标指导模型集成，确定每个模型在集成中的权重；3）应用肿瘤和病灶特异性后处理进一步细化分割结果。与现有方法的主要区别在于，该方法不依赖于单一网络架构，而是通过灵活组合现有模型和定制处理步骤，实现针对不同肿瘤类型的自适应分割，提高了泛化性和鲁棒性。

## 📊 实验亮点

在BraTS 2025 Lighthouse挑战赛的测试集上，该流程在PED、MEN、MEN-RT和MET等多个数据集上均取得了与排名靠前算法相当的分割性能，证明了其在不同肿瘤类型上的稳健性和泛化能力，无需锁定特定网络架构即可实现高效分割。

## 🎯 应用场景

该研究在临床医学影像分析领域具有重要应用价值，可用于脑肿瘤的定量测量，支持诊断、预后评估和治疗规划，特别是在多类型肿瘤（如儿童肿瘤、脑膜瘤、转移瘤）的MRI分割任务中，有助于提升临床决策的准确性和效率。

## 📄 摘要（原文）

> Robust and generalizable segmentation of brain tumors on multi-parametric magnetic resonance imaging (MRI) remains difficult because tumor types differ widely. The BraTS 2025 Lighthouse Challenge benchmarks segmentation methods on diverse high-quality datasets of adult and pediatric tumors: multi-consortium international pediatric brain tumor segmentation (PED), preoperative meningioma tumor segmentation (MEN), meningioma radiotherapy segmentation (MEN-RT), and segmentation of pre- and post-treatment brain metastases (MET). We present a flexible, modular, and adaptable pipeline that improves segmentation performance by selecting and combining state-of-the-art models and applying tumor- and lesion-specific processing before and after training. Radiomic features extracted from MRI help detect tumor subtype, ensuring a more balanced training. Custom lesion-level performance metrics determine the influence of each model in the ensemble and optimize post-processing that further refines the predictions, enabling the workflow to tailor every step to each case. On the BraTS testing sets, our pipeline achieved performance comparable to top-ranked algorithms across multiple challenges. These findings confirm that custom lesion-aware processing and model selection yield robust segmentations yet without locking the method to a specific network architecture. Our method has the potential for quantitative tumor measurement in clinical practice, supporting diagnosis and prognosis.

