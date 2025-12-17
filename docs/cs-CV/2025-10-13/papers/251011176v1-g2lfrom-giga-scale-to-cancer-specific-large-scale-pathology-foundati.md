---
layout: default
title: G2L:From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation
---

# G2L:From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11176" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11176v1</a>
  <a href="https://arxiv.org/pdf/2510.11176.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11176v1" onclick="toggleFavorite(this, '2510.11176v1', 'G2L:From Giga-Scale to Cancer-Specific Large-Scale Pathology Foundation Models via Knowledge Distillation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yesung Cho, Sungmin Lee, Geongyu Lee, Minkyung Lee, Jongbae Park, Dongmyung Shin

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**提出G2L框架，通过知识蒸馏将千亿级病理模型能力迁移至癌症特异性大型模型。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理学` `基础模型` `知识蒸馏` `癌症诊断` `大型模型` `迁移学习` `计算效率`

## 📋 核心要点

1. 现有病理学基础模型计算成本高昂，限制了其在实际癌症诊断中的应用。
2. G2L框架通过知识蒸馏，将大型模型的性能提升至与千亿级模型相当的水平。
3. 实验结果表明，G2L框架在多个基准测试中优于同等规模的模型，甚至超越了教师模型。

## 📝 摘要（中文）

病理学基础模型的研究表明，扩大训练数据规模、多样化癌症类型和增加模型大小能够持续提高性能。然而，在数十种癌症类型和数十万张切片上训练的千亿级基础模型，由于其在开发和部署中巨大的计算成本，给实际应用带来了重大挑战。本文提出了一种名为G2L框架的新策略，旨在将大型模型的性能提升到与千亿级模型相当的水平，而大型模型仅包含千亿级模型15%的参数。我们的方法采用知识蒸馏，仅使用目标癌症（如乳腺癌、前列腺癌等）的1K张病理切片，将千亿级模型的能力转移到大型模型。所得到的蒸馏模型不仅在多个基准测试中优于同等规模（即大型）的最先进模型，而且有趣的是，在某些基准测试中超过了千亿级教师模型和巨型模型。此外，蒸馏模型表现出更高的鲁棒性指标，表明其对来自多个机构的图像变异具有更强的适应性。这些发现表明，所提出的针对大型模型的蒸馏方法是一种数据和参数高效的方式，可以在没有过高计算负担的情况下，实现癌症特异性应用的千亿级性能。

## 🔬 方法详解

**问题定义**：论文旨在解决千亿级病理学基础模型计算成本过高，难以实际部署的问题。现有方法要么计算资源消耗巨大，要么模型性能不足，无法满足癌症特异性诊断的需求。

**核心思路**：论文的核心思路是利用知识蒸馏，将千亿级模型的知识迁移到参数量更小的大型模型上。通过这种方式，可以在保持模型性能的同时，显著降低计算成本，使其更易于部署和应用。

**技术框架**：G2L框架主要包含两个阶段：首先，训练一个千亿级的大型教师模型；然后，使用少量目标癌症的病理切片，通过知识蒸馏将教师模型的知识迁移到大型学生模型上。学生模型在训练过程中学习教师模型的预测结果，从而获得与教师模型相似的性能。

**关键创新**：该方法最重要的创新点在于，它能够在显著降低模型参数量和计算成本的同时，保持甚至超越教师模型的性能。这主要归功于知识蒸馏技术，它能够有效地将大型模型的知识迁移到小型模型上，避免了从头训练带来的困难。

**关键设计**：论文的关键设计包括：1）选择合适的教师模型和学生模型；2）设计有效的知识蒸馏损失函数，例如，可以使用KL散度来衡量学生模型和教师模型预测结果之间的差异；3）选择合适的训练数据，例如，可以使用1K张目标癌症的病理切片进行蒸馏训练。

## 📊 实验亮点

实验结果表明，G2L框架在多个癌症诊断基准测试中优于同等规模的最先进模型，甚至在某些基准测试中超过了千亿级教师模型和巨型模型。此外，蒸馏模型表现出更高的鲁棒性指标，表明其对来自多个机构的图像变异具有更强的适应性。

## 🎯 应用场景

该研究成果可应用于癌症诊断、预后预测和治疗方案选择等领域。通过将千亿级模型的知识迁移到小型模型上，可以降低计算成本，使其更易于部署在资源受限的环境中，例如医院或诊所。此外，该方法还可以用于开发针对特定癌症类型的专用模型，提高诊断的准确性和效率。

## 📄 摘要（原文）

> Recent studies in pathology foundation models have shown that scaling training data, diversifying cancer types, and increasing model size consistently improve their performance. However, giga-scale foundation models, which are trained on hundreds of thousands of slides covering tens of cancer types and contain billions of parameters, pose significant challenges for practical use due to their tremendous computational costs in both development and deployment. In this work, we present a novel strategy, named the G2L framework, to increase the performance of large-scale foundation models, which consist of only $15\%$ of the parameters of giga-scale models, to a comparable performance level of giga-scale models in cancer-specific tasks. Our approach applies knowledge distillation, transferring the capabilities of a giga-scale model to a large-scale model, using just 1K pathology slides of a target cancer (e.g., breast, prostate, etc.). The resulting distilled model not only outperformed state-of-the-art models of the same size (i.e., large-scale) across several benchmarks but also, interestingly, surpassed the giga-scale teacher and huge-scale models in some benchmarks. In addition, the distilled model exhibited a higher robustness index, indicating improved resilience to image variations originating from multiple institutions. These findings suggest that the proposed distillation approach for a large-scale model is a data- and parameter-efficient way to achieve giga-scale-level performance for cancer-specific applications without prohibitive computational burden.

