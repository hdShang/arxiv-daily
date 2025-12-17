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

**提出EXAONE Path 2.5病理学基础模型，通过多组学对齐解决癌症多模态建模不足的问题**

**关键词**: `病理学基础模型` `多模态对齐` `多组学整合` `对比学习` `精准肿瘤学` `全切片图像分析` `RNA-seq建模` `生物信息学`

## 📋 核心要点

1. 核心问题：现有病理学模型主要依赖图像数据，难以捕捉癌症进展中跨分子层面的相互作用，导致对肿瘤生物学的理解不全面。
2. 方法要点：提出EXAONE Path 2.5，通过多模态SigLIP损失、F-RoPE模块和领域专用基础模型，实现组织学与多组学数据的联合建模。
3. 实验或效果：在Patho-Bench基准上达到最先进性能，在内部临床数据中表现出高适应性，验证了多模态设计的有效性。

## 📝 摘要（中文）

癌症进展源于多个生物层面的相互作用，特别是超越形态学且涉及分子层面的过程，这些是仅依赖图像的模型无法捕捉的。为了更全面地刻画这一生物图景，我们提出了EXAONE Path 2.5，一个病理学基础模型，它联合建模组织学、基因组学、表观遗传学和转录组学等多模态数据，生成反映肿瘤生物学更全面的整合患者表征。我们的方法包含三个关键组件：(1) 多模态SigLIP损失，实现跨异质模态的全配对对比学习；(2) 片段感知旋转位置编码(F-RoPE)模块，保留全切片图像中的空间结构和组织片段拓扑；(3) 针对全切片图像和RNA-seq的领域专用内部基础模型，提供基于生物学的嵌入，以实现稳健的多模态对齐。我们在两个互补基准上评估EXAONE Path 2.5：一个内部真实世界临床数据集和覆盖80个任务的Patho-Bench基准。我们的框架展示了高数据和参数效率，在Patho-Bench上达到与最先进基础模型相当的性能，同时在内部临床设置中表现出最高的适应性。这些结果突显了基于生物学的多模态设计的价值，并强调了整合基因型到表型建模对下一代精准肿瘤学的潜力。

## 🔬 方法详解

EXAONE Path 2.5的整体框架是一个病理学基础模型，旨在整合组织学图像与基因组、表观遗传和转录组等多组学数据。关键技术创新点包括：采用多模态SigLIP损失进行全配对对比学习，以对齐异质模态；设计F-RoPE模块，在全切片图像中保留空间结构和组织片段拓扑；并构建领域专用内部基础模型，为全切片图像和RNA-seq提供生物学基础的嵌入。与现有方法的主要区别在于，它超越了单一图像模态，通过多组学对齐实现更全面的肿瘤生物学表征，提高了模型的生物解释性和适应性。

## 📊 实验亮点

在Patho-Bench基准的80个任务中，EXAONE Path 2.5达到与最先进基础模型相当的性能，同时在内部真实世界临床数据集中表现出最高的适应性，验证了其高数据和参数效率。

## 🎯 应用场景

该研究在精准肿瘤学领域具有广泛应用潜力，可用于癌症诊断、预后预测和治疗响应评估，通过整合多模态数据提供更个性化的医疗决策支持，推动下一代精准医疗的发展。

## 📄 摘要（原文）

> Cancer progression arises from interactions across multiple biological layers, especially beyond morphological and across molecular layers that remain invisible to image-only models. To capture this broader biological landscape, we present EXAONE Path 2.5, a pathology foundation model that jointly models histologic, genomic, epigenetic and transcriptomic modalities, producing an integrated patient representation that reflects tumor biology more comprehensively. Our approach incorporates three key components: (1) multimodal SigLIP loss enabling all-pairwise contrastive learning across heterogeneous modalities, (2) a fragment-aware rotary positional encoding (F-RoPE) module that preserves spatial structure and tissue-fragment topology in WSI, and (3) domain-specialized internal foundation models for both WSI and RNA-seq to provide biologically grounded embeddings for robust multimodal alignment. We evaluate EXAONE Path 2.5 against six leading pathology foundation models across two complementary benchmarks: an internal real-world clinical dataset and the Patho-Bench benchmark covering 80 tasks. Our framework demonstrates high data and parameter efficiency, achieving on-par performance with state-of-the-art foundation models on Patho-Bench while exhibiting the highest adaptability in the internal clinical setting. These results highlight the value of biologically informed multimodal design and underscore the potential of integrated genotype-to-phenotype modeling for next-generation precision oncology.

