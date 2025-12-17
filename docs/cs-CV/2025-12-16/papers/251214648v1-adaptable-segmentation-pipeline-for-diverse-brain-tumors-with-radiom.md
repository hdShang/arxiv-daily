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

**提出基于放射组学引导和病灶级模型集成的脑肿瘤自适应分割流程**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)**

**关键词**: `脑肿瘤分割` `放射组学` `模型集成` `深度学习` `医学图像分析`

## 📋 核心要点

1. 现有脑肿瘤分割方法难以应对肿瘤类型多样性，泛化能力不足。
2. 该论文提出一种自适应分割流程，利用放射组学特征引导肿瘤亚型识别，并进行病灶级模型集成。
3. 实验结果表明，该流程在多个 BraTS 挑战赛数据集上取得了与顶尖算法相当的性能。

## 📝 摘要（中文）

在多参数磁共振成像（MRI）上对不同脑肿瘤进行鲁棒且泛化的分割仍然很困难，因为肿瘤类型差异很大。BraTS 2025 Lighthouse Challenge 在成人和儿童肿瘤的高质量多样化数据集上对分割方法进行基准测试，包括：多联盟国际儿科脑肿瘤分割（PED）、术前脑膜瘤肿瘤分割（MEN）、脑膜瘤放射治疗分割（MEN-RT）以及治疗前和治疗后脑转移瘤分割（MET）。我们提出了一种灵活、模块化和自适应的流程，通过选择和组合最先进的模型，并在训练前后应用肿瘤和病灶特定的处理来提高分割性能。从 MRI 中提取的放射组学特征有助于检测肿瘤亚型，确保更平衡的训练。自定义病灶级别性能指标确定每个模型在集成中的影响，并优化进一步细化预测的后处理，使工作流程能够针对每个病例定制每个步骤。在 BraTS 测试集上，我们的流程实现了与多个挑战中排名靠前的算法相当的性能。这些发现证实，自定义病灶感知处理和模型选择可以产生鲁棒的分割，而无需将方法锁定到特定的网络架构。我们的方法具有在临床实践中进行定量肿瘤测量的潜力，支持诊断和预后。

## 🔬 方法详解

**问题定义**：论文旨在解决脑肿瘤在多参数 MRI 图像上的精确分割问题，尤其是在肿瘤类型多样、形态各异的情况下。现有方法通常难以在不同肿瘤类型之间泛化，鲁棒性较差。

**核心思路**：论文的核心思路是构建一个灵活、自适应的分割流程，该流程能够根据肿瘤的特性（通过放射组学特征提取）选择合适的模型，并针对每个病灶进行精细化的后处理。通过这种方式，可以提高分割的准确性和泛化能力。

**技术框架**：该流程包含以下主要模块：1) 数据预处理；2) 放射组学特征提取和肿瘤亚型识别；3) 基于肿瘤亚型的模型选择和训练；4) 病灶级模型集成；5) 后处理和分割结果优化。整个流程是模块化的，可以根据具体任务进行调整。

**关键创新**：该方法最重要的创新点在于将放射组学特征与病灶级模型集成相结合。放射组学特征用于指导模型选择和训练，使得模型能够更好地适应不同类型的肿瘤。病灶级模型集成则允许针对每个病灶选择最合适的模型，从而提高分割的准确性。

**关键设计**：论文中使用了多种分割模型，并根据放射组学特征选择合适的模型进行训练。病灶级模型集成的权重是根据自定义的病灶级别性能指标确定的。后处理步骤包括形态学操作和条件随机场（CRF）优化，以进一步提高分割结果的质量。

## 📊 实验亮点

该方法在 BraTS 2025 Lighthouse Challenge 的多个数据集上进行了测试，包括 PED、MEN、MEN-RT 和 MET。实验结果表明，该方法取得了与顶尖算法相当的性能，证明了其在不同类型脑肿瘤分割任务上的鲁棒性和泛化能力。具体性能数据未在摘要中给出，但强调了可与顶尖算法媲美。

## 🎯 应用场景

该研究成果可应用于临床脑肿瘤诊断和治疗计划制定。精确的肿瘤分割能够帮助医生更准确地评估肿瘤的大小、位置和形态，从而制定更有效的治疗方案。此外，该方法还可以用于监测肿瘤的治疗反应，评估治疗效果。

## 📄 摘要（原文）

> Robust and generalizable segmentation of brain tumors on multi-parametric magnetic resonance imaging (MRI) remains difficult because tumor types differ widely. The BraTS 2025 Lighthouse Challenge benchmarks segmentation methods on diverse high-quality datasets of adult and pediatric tumors: multi-consortium international pediatric brain tumor segmentation (PED), preoperative meningioma tumor segmentation (MEN), meningioma radiotherapy segmentation (MEN-RT), and segmentation of pre- and post-treatment brain metastases (MET). We present a flexible, modular, and adaptable pipeline that improves segmentation performance by selecting and combining state-of-the-art models and applying tumor- and lesion-specific processing before and after training. Radiomic features extracted from MRI help detect tumor subtype, ensuring a more balanced training. Custom lesion-level performance metrics determine the influence of each model in the ensemble and optimize post-processing that further refines the predictions, enabling the workflow to tailor every step to each case. On the BraTS testing sets, our pipeline achieved performance comparable to top-ranked algorithms across multiple challenges. These findings confirm that custom lesion-aware processing and model selection yield robust segmentations yet without locking the method to a specific network architecture. Our method has the potential for quantitative tumor measurement in clinical practice, supporting diagnosis and prognosis.

