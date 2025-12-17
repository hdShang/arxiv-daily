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

🎯 **匹配领域**: **人形机器人** **强化学习**

**关键词**: `淋巴瘤分型` `多实例学习` `病理基础模型` `全切片图像分析` `多中心基准` `HE染色图像` `深度学习评估` `医疗AI`

## 📋 核心要点

1. 核心问题：淋巴瘤诊断依赖多模态检测，过程昂贵耗时，且缺乏基于多中心HE染色全切片图像的深度学习基准。
2. 方法要点：构建首个多中心淋巴瘤基准数据集，系统评估病理基础模型与多实例学习聚合器在不同放大倍数下的性能。
3. 实验或效果：模型在分布内测试集上准确率超80%，但分布外测试集性能降至约60%，揭示泛化挑战。

## 📝 摘要（中文）

及时准确的淋巴瘤诊断对指导癌症治疗至关重要。标准诊断实践结合苏木精-伊红（HE）染色全切片图像与免疫组化、流式细胞术和分子遗传学检测来确定淋巴瘤亚型，这一过程需要昂贵设备、熟练人员并导致治疗延迟。深度学习方法可以通过从常规可用的HE染色切片中提取诊断信息来协助病理学家，但目前缺乏基于多中心数据的淋巴瘤分型综合基准。在这项工作中，我们提出了首个覆盖四种常见淋巴瘤亚型和健康对照组织的多中心淋巴瘤基准数据集。我们系统评估了五种公开可用的病理基础模型（H-optimus-1、H0-mini、Virchow2、UNI2、Titan）与基于注意力（AB-MIL）和基于Transformer（TransMIL）的多实例学习聚合器在三种放大倍数（10x、20x、40x）下的组合。在分布内测试集上，模型在所有放大倍数下实现了超过80%的多类平衡准确率，所有基础模型表现相似，两种聚合方法结果相当。放大倍数研究表明，40x分辨率已足够，更高分辨率或跨放大倍数聚合未带来性能提升。然而，在分布外测试集上，性能显著下降至约60%，突显了显著的泛化挑战。为推进该领域，需要覆盖更多罕见淋巴瘤亚型的更大规模多中心研究。我们提供了一个自动化基准测试流程以促进此类未来研究。

## 🔬 方法详解

**问题定义**：论文旨在解决淋巴瘤亚型诊断中依赖昂贵多模态检测导致的延迟问题，现有深度学习方法缺乏基于多中心HE染色全切片图像的全面性能基准，难以评估模型在实际临床环境中的泛化能力。

**核心思路**：通过构建首个多中心淋巴瘤基准数据集，系统比较多种病理基础模型与多实例学习聚合器的组合，在不同放大倍数下评估性能，以确定最优配置并揭示泛化瓶颈，为临床部署提供数据支持。

**技术框架**：整体流程包括数据收集（多中心HE染色全切片图像，覆盖四种淋巴瘤亚型和健康组织）、特征提取（使用五种预训练病理基础模型生成图像块特征）、特征聚合（应用AB-MIL和TransMIL聚合器整合多实例信息）、分类预测（输出淋巴瘤亚型标签），并在三种放大倍数（10x、20x、40x）下进行端到端评估。

**关键创新**：最重要的创新是首次建立了多中心淋巴瘤分型基准，填补了该领域空白；同时，系统性地探索了基础模型与聚合器的组合效应，以及放大倍数对性能的影响，为模型选择提供了实证依据。

**关键设计**：使用公开病理基础模型（如H-optimus-1、Virchow2）进行特征提取，无需从头训练；聚合器采用标准AB-MIL（基于注意力的多实例学习）和TransMIL（基于Transformer的多实例学习）架构；评估指标为多类平衡准确率，以处理类别不平衡；实验设置包括分布内和分布外测试，以全面评估泛化性。

## 📊 实验亮点

在分布内测试集上，所有模型组合在10x、20x、40x放大倍数下均实现超过80%的多类平衡准确率，基础模型间性能相似，AB-MIL与TransMIL聚合器结果相当。40x分辨率已足够，更高分辨率或跨放大倍数聚合未带来性能提升。然而，在分布外测试集上，性能显著下降至约60%，突显了模型泛化能力不足，需进一步研究以应对多中心数据差异。

## 🎯 应用场景

该研究在医疗AI领域具有重要应用价值，可直接辅助病理学家进行淋巴瘤亚型诊断，减少对昂贵检测设备的依赖，加速诊断流程。未来可扩展至更多罕见淋巴瘤亚型或其他癌症类型，推动精准医疗和自动化病理分析的发展，但需解决泛化挑战以确保临床可靠性。

## 📄 摘要（原文）

> Timely and accurate lymphoma diagnosis is essential for guiding cancer treatment. Standard diagnostic practice combines hematoxylin and eosin (HE)-stained whole slide images with immunohistochemistry, flow cytometry, and molecular genetic tests to determine lymphoma subtypes, a process requiring costly equipment, skilled personnel, and causing treatment delays. Deep learning methods could assist pathologists by extracting diagnostic information from routinely available HE-stained slides, yet comprehensive benchmarks for lymphoma subtyping on multicenter data are lacking. In this work, we present the first multicenter lymphoma benchmarking dataset covering four common lymphoma subtypes and healthy control tissue. We systematically evaluate five publicly available pathology foundation models (H-optimus-1, H0-mini, Virchow2, UNI2, Titan) combined with attention-based (AB-MIL) and transformer-based (TransMIL) multiple instance learning aggregators across three magnifications (10x, 20x, 40x). On in-distribution test sets, models achieve multiclass balanced accuracies exceeding 80% across all magnifications, with all foundation models performing similarly and both aggregation methods showing comparable results. The magnification study reveals that 40x resolution is sufficient, with no performance gains from higher resolutions or cross-magnification aggregation. However, on out-of-distribution test sets, performance drops substantially to around 60%, highlighting significant generalization challenges. To advance the field, larger multicenter studies covering additional rare lymphoma subtypes are needed. We provide an automated benchmarking pipeline to facilitate such future research.

