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

**关键词**: `淋巴瘤分型` `全切片图像分析` `多实例学习` `病理基础模型` `多中心基准` `HE染色切片` `注意力机制` `Transformer聚合`

## 📋 核心要点

1. 现有淋巴瘤诊断依赖多模态检测，成本高、耗时长，且缺乏基于HE染色切片的多中心深度学习基准。
2. 论文提出首个多中心淋巴瘤基准数据集，系统评估病理基础模型与多实例学习聚合器在不同放大倍数下的性能。
3. 在分布内测试集上模型准确率超80%，但分布外性能降至约60%，揭示了泛化挑战，并提供了自动化基准流程。

## 📝 摘要（中文）

及时准确的淋巴瘤诊断对指导癌症治疗至关重要。标准诊断实践结合苏木精-伊红（HE）染色全切片图像与免疫组化、流式细胞术和分子遗传学检测来确定淋巴瘤亚型，这一过程需要昂贵设备、熟练人员并导致治疗延迟。深度学习方法可以通过从常规可用的HE染色切片中提取诊断信息来协助病理学家，但目前缺乏基于多中心数据的淋巴瘤分型综合基准。在这项工作中，我们提出了首个多中心淋巴瘤基准数据集，涵盖四种常见淋巴瘤亚型和健康对照组织。我们系统评估了五种公开可用的病理基础模型（H-optimus-1、H0-mini、Virchow2、UNI2、Titan）与基于注意力（AB-MIL）和基于Transformer（TransMIL）的多实例学习聚合器在三种放大倍数（10x、20x、40x）下的组合。在分布内测试集上，模型在所有放大倍数下实现了超过80%的多类平衡准确率，所有基础模型表现相似，两种聚合方法结果相当。放大倍数研究表明，40x分辨率已足够，更高分辨率或跨放大倍数聚合未带来性能提升。然而，在分布外测试集上，性能大幅下降至约60%，突显了显著的泛化挑战。为推进该领域发展，需要覆盖更多罕见淋巴瘤亚型的更大规模多中心研究。我们提供了一个自动化基准测试流程以促进此类未来研究。

## 🔬 方法详解

**问题定义**：论文旨在解决淋巴瘤亚型诊断中依赖昂贵多模态检测导致的延迟问题，现有深度学习方法缺乏基于HE染色全切片图像的多中心综合基准，无法评估模型在实际临床环境中的泛化能力。

**核心思路**：通过构建首个多中心淋巴瘤基准数据集，系统比较多种病理基础模型与多实例学习聚合器的组合，在不同放大倍数下评估性能，以确定最优配置并揭示泛化瓶颈。

**技术框架**：整体流程包括数据收集（多中心HE染色切片，涵盖四种淋巴瘤亚型和健康组织）、特征提取（使用五种预训练病理基础模型）、实例聚合（采用AB-MIL和TransMIL两种方法）、分类输出（预测亚型），并在三种放大倍数（10x、20x、40x）下进行实验。

**关键创新**：最重要的创新是首次建立了多中心淋巴瘤分型基准，并系统评估了基础模型与聚合器的组合，通过放大倍数分析优化了计算效率，同时提供了自动化基准流程以促进可重复研究。

**关键设计**：使用公开病理基础模型（如H-optimus-1、Virchow2）进行特征提取，无需从头训练；聚合器采用基于注意力的AB-MIL和基于Transformer的TransMIL，以处理全切片图像中的多个实例；实验设置包括平衡准确率作为主要评估指标，并在分布内和分布外测试集上进行验证，放大倍数研究固定为10x、20x、40x以评估分辨率影响。

## 📊 实验亮点

在分布内测试集上，所有模型组合在10x、20x、40x放大倍数下均实现超过80%的多类平衡准确率，基础模型性能相似，聚合方法结果相当。放大倍数研究表明40x分辨率已足够，更高分辨率无性能提升。然而，分布外测试集性能大幅下降至约60%，突显泛化挑战。实验覆盖五种基础模型和两种聚合器，提供了首个多中心基准结果。

## 🎯 应用场景

该研究可应用于临床病理学辅助诊断，通过深度学习从常规HE染色切片中自动识别淋巴瘤亚型，减少对昂贵检测的依赖，加速诊断流程。潜在价值包括降低医疗成本、提高诊断一致性，并为罕见亚型研究提供基准。未来影响可能推动多中心AI模型标准化，促进精准医疗发展。

## 📄 摘要（原文）

> Timely and accurate lymphoma diagnosis is essential for guiding cancer treatment. Standard diagnostic practice combines hematoxylin and eosin (HE)-stained whole slide images with immunohistochemistry, flow cytometry, and molecular genetic tests to determine lymphoma subtypes, a process requiring costly equipment, skilled personnel, and causing treatment delays. Deep learning methods could assist pathologists by extracting diagnostic information from routinely available HE-stained slides, yet comprehensive benchmarks for lymphoma subtyping on multicenter data are lacking. In this work, we present the first multicenter lymphoma benchmarking dataset covering four common lymphoma subtypes and healthy control tissue. We systematically evaluate five publicly available pathology foundation models (H-optimus-1, H0-mini, Virchow2, UNI2, Titan) combined with attention-based (AB-MIL) and transformer-based (TransMIL) multiple instance learning aggregators across three magnifications (10x, 20x, 40x). On in-distribution test sets, models achieve multiclass balanced accuracies exceeding 80% across all magnifications, with all foundation models performing similarly and both aggregation methods showing comparable results. The magnification study reveals that 40x resolution is sufficient, with no performance gains from higher resolutions or cross-magnification aggregation. However, on out-of-distribution test sets, performance drops substantially to around 60%, highlighting significant generalization challenges. To advance the field, larger multicenter studies covering additional rare lymphoma subtypes are needed. We provide an automated benchmarking pipeline to facilitate such future research.

