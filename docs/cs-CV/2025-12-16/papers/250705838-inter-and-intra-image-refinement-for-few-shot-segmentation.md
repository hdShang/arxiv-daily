---
layout: default
title: Inter- and Intra-image Refinement for Few Shot Segmentation
---

# Inter- and Intra-image Refinement for Few Shot Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.05838" class="toolbar-btn" target="_blank">📄 arXiv: 2507.05838</a>
  <a href="https://arxiv.org/pdf/2507.05838.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.05838" onclick="toggleFavorite(this, '2507.05838', 'Inter- and Intra-image Refinement for Few Shot Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ourui Fu, Hangzhou He, Kaiwen Li, Xinliang Zhang, Lei Zhu, Shuang Zeng, Zhaoheng Xie, Yanye Lu

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出Inter- and Intra-image Refinement模型，解决少样本分割中类内差异和类间干扰问题。**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `少样本分割` `语义分割` `原型学习` `类激活映射` `Dropout` `跨域学习`

## 📋 核心要点

1. 现有少样本分割方法依赖单原型表示，导致支持集和查询集之间存在较大的类内差异，生成的先验图谱质量不高。
2. IIR模型通过生成两个原型，分别关注核心区分特征和局部特定特征，从而实现更准确的类间匹配和更鲁棒的先验图谱。
3. 实验结果表明，IIR模型在多个少样本分割基准测试中均取得了领先的性能，证明了其有效性。

## 📝 摘要（中文）

本文提出Inter- and Intra-image Refinement (IIR) 模型，旨在解决少样本语义分割(FSS)中存在的类内差异和类间干扰问题。现有基于原型的方法受限于单原型表示，导致先验图谱分散且噪声大。同时，视觉相似但语义不同的区域会造成支持集和查询集特征匹配不一致，产生错误预测。IIR模型通过类激活映射生成两个原型，分别用于核心区分特征和局部特定特征的匹配，从而生成准确且鲁棒的先验图谱。此外，引入方向性Dropout机制来屏蔽交叉注意力中不一致的支持集-查询集特征对，提升解码器性能。在标准FSS、部分FSS和跨域FSS等9个基准测试中，IIR均取得了state-of-the-art的性能。

## 🔬 方法详解

**问题定义**：少样本语义分割旨在仅使用少量标注样本将模型泛化到新的类别。现有方法，特别是基于原型的方法，在处理类内差异和类间干扰时存在局限性。类内差异指的是同一类别在支持集和查询集图像中可能存在外观、光照等差异，导致单原型表示无法准确捕捉类别特征。类间干扰指的是视觉上相似但语义不同的区域会干扰支持集和查询集之间的特征匹配，导致分割错误。

**核心思路**：IIR模型的核心思路是通过更精细的特征表示和更鲁棒的特征匹配来缓解类内差异和类间干扰。具体来说，IIR模型使用两个原型来表示每个类别，一个原型关注核心区分特征，另一个原型关注局部特定特征。同时，IIR模型使用方向性Dropout机制来过滤掉不一致的特征匹配，从而提高分割的准确性。

**技术框架**：IIR模型主要包含两个模块：Inter-image Refinement和Intra-image Refinement。Inter-image Refinement模块使用类激活映射生成两个原型，用于支持集和查询集之间的特征匹配。Intra-image Refinement模块使用方向性Dropout机制来过滤掉不一致的特征匹配。整个流程是先通过Inter-image Refinement生成更准确的先验图谱，然后通过Intra-image Refinement进一步提升解码器性能。

**关键创新**：IIR模型的关键创新在于以下两点：1) 使用两个原型来表示每个类别，从而更全面地捕捉类别特征，缓解类内差异；2) 引入方向性Dropout机制来过滤掉不一致的特征匹配，从而提高分割的准确性，缓解类间干扰。与现有方法相比，IIR模型能够更有效地处理类内差异和类间干扰，从而取得更好的分割性能。

**关键设计**：Inter-image Refinement模块使用类激活映射(CAM)来生成两个原型。具体来说，首先使用全局平均池化(GAP)得到每个特征图的权重，然后根据权重对特征图进行加权求和，得到类激活图。然后，使用阈值分割将类激活图分成两个区域，分别对应核心区分特征和局部特定特征。Intra-image Refinement模块使用方向性Dropout机制来过滤掉不一致的特征匹配。具体来说，首先计算支持集和查询集特征之间的相似度矩阵，然后根据相似度矩阵对特征进行Dropout，从而过滤掉不一致的特征匹配。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.05838/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.05838/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2507.05838/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

IIR模型在9个少样本分割基准测试中均取得了state-of-the-art的性能，包括标准FSS、部分FSS和跨域FSS。例如，在标准FSS的PASCAL-5i数据集上，IIR模型相比于现有最佳方法取得了显著的性能提升。这些实验结果充分证明了IIR模型的有效性和泛化能力。

## 🎯 应用场景

该研究成果可应用于医疗图像分析、遥感图像解译、自动驾驶等领域。在这些领域中，标注数据通常非常有限，因此少样本分割技术具有重要的应用价值。IIR模型能够有效地利用少量标注样本，提高分割的准确性和鲁棒性，从而为这些领域的应用提供更好的支持。未来，该技术有望进一步推广到更多的实际应用场景中。

## 📄 摘要（原文）

> Deep neural networks for semantic segmentation rely on large-scale annotated datasets, leading to an annotation bottleneck that motivates few shot semantic segmentation (FSS) which aims to generalize to novel classes with minimal labeled exemplars. Most existing FSS methods adopt a prototype-based paradigm, which generates query prior map by extracting masked-area features from support images and then makes predictions guided by the prior map. However, they suffer from two critical limitations induced by inter- and intra-image discrepancies: 1) The intra-class gap between support and query images, caused by single-prototype representation, results in scattered and noisy prior maps; 2) The inter-class interference from visually similar but semantically distinct regions leads to inconsistent support-query feature matching and erroneous predictions. To address these issues, we propose the Inter- and Intra-image Refinement (IIR) model. The model contains an inter-image class activation mapping based method that generates two prototypes for class-consistent region matching, including core discriminative features and local specific features, and yields an accurate and robust prior map. For intra-image refinement, a directional dropout mechanism is introduced to mask inconsistent support-query feature pairs in cross attention, thereby enhancing decoder performance. Extensive experiments demonstrate that IIR achieves state-of-the-art performance on 9 benchmarks, covering standard FSS, part FSS, and cross-domain FSS. Our source code is available at \href{this https URL}{this https URL}.

