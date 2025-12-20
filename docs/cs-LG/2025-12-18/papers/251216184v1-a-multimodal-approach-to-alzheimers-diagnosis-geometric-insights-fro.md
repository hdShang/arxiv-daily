---
layout: default
title: A Multimodal Approach to Alzheimer's Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments
---

# A Multimodal Approach to Alzheimer's Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.16184" class="toolbar-btn" target="_blank">📄 arXiv: 2512.16184v1</a>
  <a href="https://arxiv.org/pdf/2512.16184.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.16184v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.16184v1', 'A Multimodal Approach to Alzheimer\'s Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jaeho Yang, Kijung Yoon

**分类**: cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**提出基于图神经网络的多模态融合框架，用于阿尔茨海默病早期诊断。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿尔茨海默病诊断` `图神经网络` `多模态融合` `立方体复制任务` `几何特征` `拓扑特征` `早期筛查`

## 📋 核心要点

1. 阿尔茨海默病早期诊断面临挑战，传统方法依赖复杂且耗时的神经心理测试。
2. 该论文提出将手绘立方体图转换为图结构，提取几何和拓扑特征，结合其他信息进行诊断。
3. 实验表明，基于图的表示优于传统像素方法，多模态融合进一步提升了诊断性能和鲁棒性。

## 📝 摘要（中文）

阿尔茨海默病(AD)的早期和可及性检测仍然是一项关键的临床挑战，而立方体复制任务提供了一种简单但信息丰富的视觉空间功能评估方法。本研究提出了一种多模态框架，该框架将手绘立方体草图转换为图结构表示，以捕获几何和拓扑属性，并将这些特征与人口统计信息和神经心理测试(NPT)分数相结合，用于AD分类。立方体图被建模为图，其节点特征编码空间坐标、基于局部图元的拓扑结构和角度几何。这些图通过图神经网络处理，并在后期融合模型中与年龄、教育程度和NPT特征融合。实验结果表明，基于图的表示提供了强大的单模态基线，并且显著优于基于像素的卷积模型，而多模态集成进一步提高了性能和对类不平衡的鲁棒性。基于SHAP的可解释性分析确定了特定的图元基序和几何扭曲是关键预测因子，这与AD中立方体图的临床观察结果非常吻合。总之，这些结果确立了基于图的立方体复制分析作为一种可解释、非侵入性和可扩展的阿尔茨海默病筛查方法。

## 🔬 方法详解

**问题定义**：阿尔茨海默病的早期诊断是临床上的一个难题。传统的诊断方法，如神经心理测试，往往耗时且复杂。立方体复制任务作为一种简单易行的评估方法，能够反映患者的视觉空间功能，但如何有效利用手绘立方体图的信息进行诊断仍然是一个挑战。现有方法，例如基于像素的卷积神经网络，难以充分捕捉立方体图的几何和拓扑结构信息。

**核心思路**：该论文的核心思路是将手绘立方体图转换为图结构，利用图神经网络(GNN)提取图中的几何和拓扑特征。这种方法能够更有效地捕捉立方体图中的结构信息，从而提高阿尔茨海默病的诊断准确率。将立方体图转换为图结构，可以更好地利用图神经网络处理非欧几里得空间数据的优势。

**技术框架**：该论文提出的多模态框架包含以下几个主要阶段：1) 数据预处理：收集手绘立方体图、人口统计信息和神经心理测试(NPT)分数。2) 图构建：将手绘立方体图转换为图结构，节点特征包括空间坐标、局部图元拓扑和角度几何。3) 特征提取：使用图神经网络提取图结构中的特征。4) 多模态融合：将图神经网络提取的特征与人口统计信息和NPT分数进行融合。5) 分类：使用分类器进行阿尔茨海默病的诊断。

**关键创新**：该论文的关键创新在于将手绘立方体图转换为图结构，并利用图神经网络提取特征。这种方法能够更有效地捕捉立方体图中的几何和拓扑结构信息，从而提高阿尔茨海默病的诊断准确率。此外，该论文还提出了一个多模态融合框架，将图神经网络提取的特征与人口统计信息和NPT分数进行融合，进一步提高了诊断性能。

**关键设计**：在图构建阶段，论文使用了局部图元(graphlet)来描述节点的局部拓扑结构。图神经网络使用了Graph Convolutional Network (GCN) 或 Graph Attention Network (GAT) 等常见的图神经网络结构。在多模态融合阶段，使用了后期融合(late-fusion)策略，即将不同模态的特征分别提取后，再进行融合。损失函数使用了交叉熵损失函数，用于分类任务的训练。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16184v1/Figure1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16184v1/Figure2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.16184v1/Figure3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于图的表示方法在立方体复制任务上的表现优于基于像素的卷积模型。多模态融合进一步提升了诊断性能，并提高了对类别不平衡的鲁棒性。SHAP分析揭示了特定的图元基序和几何扭曲是关键的预测因子，与临床观察结果一致。该方法在阿尔茨海默病诊断方面具有显著优势。

## 🎯 应用场景

该研究成果可应用于阿尔茨海默病的早期筛查和辅助诊断，尤其是在医疗资源匮乏的地区。通过简单的立方体复制任务和图神经网络分析，可以实现低成本、非侵入性的初步诊断，为患者争取宝贵的治疗时间。未来，该方法可扩展到其他神经退行性疾病的诊断。

## 📄 摘要（原文）

> Early and accessible detection of Alzheimer's disease (AD) remains a critical clinical challenge, and cube-copying tasks offer a simple yet informative assessment of visuospatial function. This work proposes a multimodal framework that converts hand-drawn cube sketches into graph-structured representations capturing geometric and topological properties, and integrates these features with demographic information and neuropsychological test (NPT) scores for AD classification. Cube drawings are modeled as graphs with node features encoding spatial coordinates, local graphlet-based topology, and angular geometry, which are processed using graph neural networks and fused with age, education, and NPT features in a late-fusion model. Experimental results show that graph-based representations provide a strong unimodal baseline and substantially outperform pixel-based convolutional models, while multimodal integration further improves performance and robustness to class imbalance. SHAP-based interpretability analysis identifies specific graphlet motifs and geometric distortions as key predictors, closely aligning with clinical observations of disorganized cube drawings in AD. Together, these results establish graph-based analysis of cube copying as an interpretable, non-invasive, and scalable approach for Alzheimer's disease screening.

