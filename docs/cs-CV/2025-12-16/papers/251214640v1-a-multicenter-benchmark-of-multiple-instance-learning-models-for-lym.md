---
layout: default
title: A Multicenter Benchmark of Multiple Instance Learning Models for Lymphoma Subtyping from HE-stained Whole Slide Images
---

# A Multicenter Benchmark of Multiple Instance Learning Models for Lymphoma Subtyping from HE-stained Whole Slide Images

**arXiv**: [2512.14640v1](https://arxiv.org/abs/2512.14640) | [PDF](https://arxiv.org/pdf/2512.14640.pdf)

**作者**: Rao Muhammad Umer, Daniel Sens, Jonathan Noll, Christian Matek, Lukas Wolfseher, Rainer Spang, Ralf Huss, Johannes Raffler, Sarah Reinke, Wolfram Klapper, Katja Steiger, Kristina Schwamborn, Carsten Marr

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: 17 pages

---

## 💡 一句话要点

**提出首个多中心淋巴瘤分型基准数据集，系统评估病理基础模型与多实例学习聚合器在HE染色全切片图像上的性能。**

**关键词**: `淋巴瘤分型` `全切片图像分析` `多实例学习` `病理基础模型` `多中心基准` `HE染色图像` `注意力机制` `Transformer聚合`

## 📋 核心要点

1. 现有淋巴瘤诊断依赖多模态检测，成本高、耗时长，且缺乏多中心HE图像分型基准。
2. 论文提出首个多中心淋巴瘤基准数据集，并系统评估病理基础模型与多实例学习聚合器的组合。
3. 模型在分布内测试集上准确率超80%，但分布外性能降至约60%，揭示泛化挑战。

## 📝 摘要（中文）

及时准确的淋巴瘤诊断对指导癌症治疗至关重要。标准诊断实践结合苏木精-伊红（HE）染色全切片图像与免疫组化、流式细胞术和分子遗传学检测来确定淋巴瘤亚型，这一过程需要昂贵设备、熟练人员并导致治疗延迟。深度学习方法可通过从常规可用的HE染色切片中提取诊断信息来协助病理学家，但多中心数据上的淋巴瘤分型综合基准仍缺乏。在这项工作中，我们提出了首个多中心淋巴瘤基准数据集，涵盖四种常见淋巴瘤亚型和健康对照组织。我们系统评估了五种公开可用的病理基础模型（H-optimus-1、H0-mini、Virchow2、UNI2、Titan）与基于注意力（AB-MIL）和基于Transformer（TransMIL）的多实例学习聚合器在三种放大倍数（10x、20x、40x）下的组合。在分布内测试集上，模型在所有放大倍数下实现了超过80%的多类平衡准确率，所有基础模型表现相似，两种聚合方法结果相当。放大倍数研究表明，40x分辨率已足够，更高分辨率或跨放大倍数聚合未带来性能提升。然而，在分布外测试集上，性能显著下降至约60%，突显了显著的泛化挑战。为推进该领域，需要覆盖更多罕见淋巴瘤亚型的更大规模多中心研究。我们提供了一个自动化基准测试流程以促进此类未来研究。

## 🔬 方法详解

论文采用多实例学习框架处理全切片图像，将每个切片视为实例包，每个实例对应图像块。核心方法结合预训练的病理基础模型（如H-optimus-1、Virchow2等）提取特征，然后使用基于注意力的AB-MIL或基于Transformer的TransMIL聚合器整合实例级特征，生成切片级预测。关键创新在于首次在多中心淋巴瘤数据集上系统比较多种基础模型与聚合器，并研究放大倍数的影响。与现有方法相比，该方法避免了从头训练，利用公开基础模型，并通过基准测试提供了标准化评估。

## 📊 实验亮点

在分布内测试集上，所有模型组合在10x、20x、40x放大倍数下均实现超过80%的多类平衡准确率，表明40x分辨率已足够且无需更高分辨率。然而，分布外测试集性能大幅下降至约60%，突显模型泛化能力不足，是未来研究的关键挑战。

## 🎯 应用场景

该研究可应用于病理学辅助诊断，帮助从常规HE染色切片中快速识别淋巴瘤亚型，减少对昂贵辅助检测的依赖，加速诊断流程，尤其在资源有限或远程医疗场景中具有实际价值。

## 📄 摘要（原文）

> Timely and accurate lymphoma diagnosis is essential for guiding cancer treatment. Standard diagnostic practice combines hematoxylin and eosin (HE)-stained whole slide images with immunohistochemistry, flow cytometry, and molecular genetic tests to determine lymphoma subtypes, a process requiring costly equipment, skilled personnel, and causing treatment delays. Deep learning methods could assist pathologists by extracting diagnostic information from routinely available HE-stained slides, yet comprehensive benchmarks for lymphoma subtyping on multicenter data are lacking. In this work, we present the first multicenter lymphoma benchmarking dataset covering four common lymphoma subtypes and healthy control tissue. We systematically evaluate five publicly available pathology foundation models (H-optimus-1, H0-mini, Virchow2, UNI2, Titan) combined with attention-based (AB-MIL) and transformer-based (TransMIL) multiple instance learning aggregators across three magnifications (10x, 20x, 40x). On in-distribution test sets, models achieve multiclass balanced accuracies exceeding 80% across all magnifications, with all foundation models performing similarly and both aggregation methods showing comparable results. The magnification study reveals that 40x resolution is sufficient, with no performance gains from higher resolutions or cross-magnification aggregation. However, on out-of-distribution test sets, performance drops substantially to around 60%, highlighting significant generalization challenges. To advance the field, larger multicenter studies covering additional rare lymphoma subtypes are needed. We provide an automated benchmarking pipeline to facilitate such future research.

