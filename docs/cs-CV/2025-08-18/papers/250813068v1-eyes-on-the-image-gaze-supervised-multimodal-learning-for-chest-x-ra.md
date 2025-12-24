---
layout: default
title: "Eyes on the Image: Gaze Supervised Multimodal Learning for Chest X-ray Diagnosis and Report Generation"
---

# Eyes on the Image: Gaze Supervised Multimodal Learning for Chest X-ray Diagnosis and Report Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.13068" class="toolbar-btn" target="_blank">📄 arXiv: 2508.13068v1</a>
  <a href="https://arxiv.org/pdf/2508.13068.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.13068v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.13068v1', 'Eyes on the Image: Gaze Supervised Multimodal Learning for Chest X-ray Diagnosis and Report Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Tanjim Islam Riju, Shuchismita Anwar, Saman Sarker Joy, Farig Sadeque, Swakkhar Shatabda

**分类**: cs.CV, cs.LG

**发布日期**: 2025-08-18

---

## 💡 一句话要点

**提出基于注视监督的多模态学习框架以提升胸部X光诊断与报告生成**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态学习` `胸部X光` `疾病分类` `报告生成` `注视引导` `眼动追踪` `深度学习`

## 📋 核心要点

1. 现有方法在胸部X光图像的疾病分类和报告生成中缺乏有效的区域感知能力，导致诊断准确性不足。
2. 提出的框架通过注视引导的对比学习和模块化报告生成，结合视觉特征和眼动追踪信号，提升了分类和报告生成的效果。
3. 实验结果表明，整合注视数据后，F1分数和AUC均有显著提升，报告质量也得到了改善，显示出该方法的有效性。

## 📝 摘要（中文）

本文提出了一种两阶段的多模态框架，旨在增强胸部X光的疾病分类和区域感知放射学报告生成，利用MIMIC-Eye数据集。在第一阶段，提出了一种基于注视引导的对比学习架构，结合视觉特征、临床标签、边界框和放射科医生的眼动追踪信号，并引入了一种新颖的多项注视注意损失函数。通过整合注视信息，F1分数从0.597提升至0.631（+5.70%），AUC从0.821提升至0.849（+3.41%），同时提高了精确率和召回率，显示了注视信息监督的有效性。在第二阶段，提出了一个模块化的报告生成管道，提取置信度加权的诊断关键词，并通过领域特定的字典将其映射到解剖区域，生成区域对齐的句子。该管道在临床关键词召回和ROUGE重叠方面提高了报告质量。

## 🔬 方法详解

**问题定义**：本文旨在解决胸部X光图像的疾病分类和报告生成中的区域感知不足问题。现有方法往往忽视了放射科医生的注视信息，导致分类性能和报告的可解释性不足。

**核心思路**：论文提出了一种两阶段的多模态学习框架，第一阶段通过注视引导的对比学习提升疾病分类，第二阶段通过模块化的报告生成管道提升报告质量。这样的设计旨在充分利用眼动追踪数据，提高模型的性能和可解释性。

**技术框架**：整体架构分为两个主要阶段：第一阶段为疾病分类，采用注视引导的对比学习架构；第二阶段为报告生成，利用提取的关键词和解剖区域映射生成区域对齐的句子。

**关键创新**：最重要的技术创新在于引入了多项注视注意损失函数，结合均方误差、KL散度、相关性和质心对齐，显著提升了模型的分类性能和报告生成的质量。

**关键设计**：在第一阶段，模型整合了视觉特征、临床标签、边界框和眼动追踪信号，使用了新颖的损失函数来优化注视信息的利用。第二阶段则通过构建领域特定的字典，实现了关键词的置信度加权和区域对齐句子的生成。

## 📊 实验亮点

实验结果显示，整合注视数据后，F1分数从0.597提升至0.631（+5.70%），AUC从0.821提升至0.849（+3.41%），同时提高了精确率和召回率，表明该方法在疾病分类和报告生成方面的显著提升。

## 🎯 应用场景

该研究在医学影像分析领域具有广泛的应用潜力，尤其是在胸部疾病的早期诊断和报告生成方面。通过提高分类准确性和报告的可解释性，能够为临床医生提供更为可靠的决策支持，未来可能推动智能医疗的发展。

## 📄 摘要（原文）

> We propose a two-stage multimodal framework that enhances disease classification and region-aware radiology report generation from chest X-rays, leveraging the MIMIC-Eye dataset. In the first stage, we introduce a gaze-guided contrastive learning architecture for disease classification. It integrates visual features, clinical labels, bounding boxes, and radiologist eye-tracking signals and is equipped with a novel multi-term gaze-attention loss combining MSE, KL divergence, correlation, and center-of-mass alignment. Incorporating fixations improves F1 score from 0.597 to 0.631 (+5.70%) and AUC from 0.821 to 0.849 (+3.41%), while also improving precision and recall, highlighting the effectiveness of gaze-informed attention supervision. In the second stage, we present a modular report generation pipeline that extracts confidence-weighted diagnostic keywords, maps them to anatomical regions using a curated dictionary constructed from domain-specific priors, and generates region-aligned sentences via structured prompts. This pipeline improves report quality as measured by clinical keyword recall and ROUGE overlap. Our results demonstrate that integrating gaze data improves both classification performance and the interpretability of generated medical reports.

