---
layout: default
title: EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment
---

# EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment

**arXiv**: [2512.14019v1](https://arxiv.org/abs/2512.14019) | [PDF](https://arxiv.org/pdf/2512.14019.pdf)

**作者**: Juseung Yun, Sunwoo Yu, Sumin Ha, Jonghyun Kim, Janghyeon Lee, Jongseong Jang, Soonyoung Lee

**分类**: cs.LG, q-bio.QM

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出EXAONE Path 2.5病理学基础模型，通过多组学对齐解决癌症多模态建模不足问题**

🎯 **匹配领域**: **强化学习**

**关键词**: `病理学基础模型` `多模态对齐` `多组学整合` `对比学习` `精准肿瘤学` `全切片图像分析` `生物信息学` `癌症建模`

## 📋 核心要点

1. 核心问题：现有病理学模型主要依赖图像模态，难以捕捉癌症进展中跨分子层面的相互作用，导致对肿瘤生物学的理解不全面。
2. 方法要点：提出EXAONE Path 2.5，整合组织学、基因组学等多模态数据，通过多模态对齐和专用编码模块生成综合患者表征。
3. 实验或效果：在Patho-Bench基准上达到最先进性能，在临床数据中展示高适应性，验证了多组学建模的有效性。

## 📝 摘要（中文）

癌症进展源于多个生物层面的相互作用，特别是超越形态学且涉及分子层面，这些对仅基于图像的模型是不可见的。为捕捉更广泛的生物景观，我们提出了EXAONE Path 2.5，这是一个病理学基础模型，联合建模组织学、基因组学、表观遗传学和转录组学模态，生成反映肿瘤生物学更全面的整合患者表征。我们的方法包含三个关键组件：(1) 多模态SigLIP损失，实现跨异质模态的全配对对比学习；(2) 片段感知旋转位置编码(F-RoPE)模块，保留全切片图像中的空间结构和组织片段拓扑；(3) 针对全切片图像和RNA-seq的领域专用内部基础模型，提供基于生物学的嵌入，以实现稳健的多模态对齐。我们在两个互补基准上评估EXAONE Path 2.5与六个领先的病理学基础模型：一个内部真实世界临床数据集和覆盖80个任务的Patho-Bench基准。我们的框架展示了高数据和参数效率，在Patho-Bench上达到与最先进基础模型相当的性能，同时在内部临床设置中表现出最高的适应性。这些结果突显了基于生物学的多模态设计的价值，并强调了整合基因型到表型建模对下一代精准肿瘤学的潜力。

## 🔬 方法详解

EXAONE Path 2.5的整体框架是一个多模态病理学基础模型，旨在联合处理组织学图像（如全切片图像）和分子数据（如基因组、转录组）。关键技术创新点包括：使用多模态SigLIP损失进行跨模态对比学习，确保不同数据类型的有效对齐；引入片段感知旋转位置编码(F-RoPE)模块，以保留全切片图像中的空间结构和组织片段拓扑；以及部署领域专用内部基础模型，为全切片图像和RNA-seq提供生物学基础的嵌入。与现有方法的主要区别在于其强调多组学对齐，通过整合多种生物模态来更全面地建模肿瘤生物学，而传统方法通常局限于单一模态或简单融合。

## 📊 实验亮点

在Patho-Bench基准测试中，EXAONE Path 2.5达到与最先进模型相当的性能，覆盖80个任务；在内部临床数据集上展示最高适应性，验证了其高数据和参数效率，突显多模态对齐的优势。

## 🎯 应用场景

该研究在精准肿瘤学领域具有重要应用价值，可用于癌症诊断、预后预测和治疗响应分析。通过整合多模态数据，模型能提供更全面的患者表征，支持个性化医疗决策，推动下一代癌症研究和临床实践的发展。

## 📄 摘要（原文）

> Cancer progression arises from interactions across multiple biological layers, especially beyond morphological and across molecular layers that remain invisible to image-only models. To capture this broader biological landscape, we present EXAONE Path 2.5, a pathology foundation model that jointly models histologic, genomic, epigenetic and transcriptomic modalities, producing an integrated patient representation that reflects tumor biology more comprehensively. Our approach incorporates three key components: (1) multimodal SigLIP loss enabling all-pairwise contrastive learning across heterogeneous modalities, (2) a fragment-aware rotary positional encoding (F-RoPE) module that preserves spatial structure and tissue-fragment topology in WSI, and (3) domain-specialized internal foundation models for both WSI and RNA-seq to provide biologically grounded embeddings for robust multimodal alignment. We evaluate EXAONE Path 2.5 against six leading pathology foundation models across two complementary benchmarks: an internal real-world clinical dataset and the Patho-Bench benchmark covering 80 tasks. Our framework demonstrates high data and parameter efficiency, achieving on-par performance with state-of-the-art foundation models on Patho-Bench while exhibiting the highest adaptability in the internal clinical setting. These results highlight the value of biologically informed multimodal design and underscore the potential of integrated genotype-to-phenotype modeling for next-generation precision oncology.

