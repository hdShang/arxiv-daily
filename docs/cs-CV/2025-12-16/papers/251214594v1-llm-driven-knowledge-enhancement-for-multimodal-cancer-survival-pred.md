---
layout: default
title: LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction
---

# LLM-driven Knowledge Enhancement for Multimodal Cancer Survival Prediction

**arXiv**: [2512.14594v1](https://arxiv.org/abs/2512.14594) | [PDF](https://arxiv.org/pdf/2512.14594.pdf)

**作者**: Chenyu Zhao, Yingxue Xu, Fengtao Zhou, Yihui Wang, Hao Chen

**分类**: cs.CV

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出KEMM模型，通过LLM驱动的知识增强解决多模态癌症生存预测中的特征冗余和对齐难题。**

**关键词**: `多模态学习` `癌症生存预测` `知识增强` `LLM驱动` `跨模态注意力` `病理图像分析` `基因组数据` `预后建模`

## 📋 核心要点

1. 现有方法依赖高维冗余的病理图像和基因组数据，难以提取判别性特征并实现模态对齐，且生存标签监督不足。
2. 提出KEMM模型，整合LLM精炼的专家报告和生成的预后背景知识，通过KECM注意力模块增强特征提取和模态融合。
3. 在五个数据集上实验，KEMM达到最先进性能，验证了知识增强在多模态生存预测中的有效性。

## 📝 摘要（中文）

当前多模态生存预测方法通常依赖病理图像（WSIs）和基因组数据，这些数据具有高维度和冗余性，难以从中提取判别性特征并实现不同模态的对齐。此外，仅使用简单的生存随访标签不足以监督如此复杂的任务。为解决这些挑战，我们提出了KEMM，一种LLM驱动的知识增强多模态模型，用于癌症生存预测，该模型整合了专家报告和预后背景知识。1）专家报告由病理学家逐案提供，并由大型语言模型（LLM）精炼，提供简洁且临床聚焦的诊断陈述，这些信息通常暗示不同的生存结果。2）预后背景知识（PBK）由LLM简洁生成，提供关于不同癌症类型的宝贵预后背景知识，从而增强生存预测。为利用这些知识，我们引入了知识增强跨模态（KECM）注意力模块。KECM能有效引导网络关注来自高度冗余模态的判别性和生存相关特征。在五个数据集上的广泛实验表明，KEMM实现了最先进的性能。代码将在接受后发布。

## 🔬 方法详解

KEMM的整体框架是一个多模态深度学习模型，核心整合病理图像、基因组数据、专家报告和预后背景知识。关键技术创新点包括：1）利用LLM精炼专家报告以提供临床聚焦的诊断信息；2）LLM生成预后背景知识以补充领域知识；3）设计知识增强跨模态（KECM）注意力模块，该模块通过知识引导注意力机制，有效聚焦于判别性和生存相关特征，减少冗余干扰。与现有方法的主要区别在于：现有方法通常仅依赖原始多模态数据和简单标签，而KEMM引入外部知识源（专家报告和PBK），并通过KECM实现知识驱动的特征对齐和融合，从而提升模型鲁棒性和预测准确性。

## 📊 实验亮点

在五个数据集上的实验显示，KEMM实现了最先进的性能，具体提升未知，但验证了知识增强和KECM模块在多模态生存预测中的有效性，显著优于依赖原始数据和简单标签的基线方法。

## 🎯 应用场景

该研究主要应用于癌症预后预测和个性化医疗领域，可辅助临床医生评估患者生存风险，优化治疗决策。潜在价值包括提高预测准确性、减少数据冗余影响，以及通过知识增强提升模型可解释性，推动精准医疗发展。

## 📄 摘要（原文）

> Current multimodal survival prediction methods typically rely on pathology images (WSIs) and genomic data, both of which are high-dimensional and redundant, making it difficult to extract discriminative features from them and align different modalities. Moreover, using a simple survival follow-up label is insufficient to supervise such a complex task. To address these challenges, we propose KEMM, an LLM-driven Knowledge-Enhanced Multimodal Model for cancer survival prediction, which integrates expert reports and prognostic background knowledge. 1) Expert reports, provided by pathologists on a case-by-case basis and refined by large language model (LLM), offer succinct and clinically focused diagnostic statements. This information may typically suggest different survival outcomes. 2) Prognostic background knowledge (PBK), generated concisely by LLM, provides valuable prognostic background knowledge on different cancer types, which also enhances survival prediction. To leverage these knowledge, we introduce the knowledge-enhanced cross-modal (KECM) attention module. KECM can effectively guide the network to focus on discriminative and survival-relevant features from highly redundant modalities. Extensive experiments on five datasets demonstrate that KEMM achieves state-of-the-art performance. The code will be released upon acceptance.

