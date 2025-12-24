---
layout: default
title: "A Multimodal Approach to Alzheimer's Diagnosis: Geometric Insights from Cube Copying and Cognitive Assessments"
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

**提出基于图神经网络的多模态融合方法，用于阿尔茨海默病早期诊断。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `阿尔茨海默病诊断` `图神经网络` `多模态融合` `立方体复制任务` `几何特征` `拓扑特征` `早期筛查`

## 📋 核心要点

1. 现有阿尔茨海默病早期诊断方法复杂且可及性差，立方体复制任务提供了一种简单有效的评估视觉空间功能的方式。
2. 该论文提出将手绘立方体图转换为图结构，提取几何和拓扑特征，并结合人口统计学信息进行多模态融合。
3. 实验结果表明，基于图的表示优于传统像素方法，多模态融合进一步提升了诊断性能和鲁棒性。

## 📝 摘要（中文）

阿尔茨海默病(AD)的早期和可及性检测仍然是一项关键的临床挑战，而立方体复制任务提供了一种简单但信息丰富的视觉空间功能评估方法。本研究提出了一种多模态框架，该框架将手绘立方体草图转换为图结构化表示，以捕获几何和拓扑属性，并将这些特征与人口统计信息和神经心理测试(NPT)分数相结合，用于AD分类。立方体图被建模为具有节点特征的图，节点特征编码空间坐标、基于局部图元的拓扑结构和角度几何，这些特征使用图神经网络进行处理，并在后期融合模型中与年龄、教育程度和NPT特征融合。实验结果表明，基于图的表示提供了强大的单模态基线，并且大大优于基于像素的卷积模型，而多模态集成进一步提高了性能和对类不平衡的鲁棒性。基于SHAP的可解释性分析确定了特定的图元模式和几何扭曲是关键预测因子，这与AD中紊乱的立方体图的临床观察结果密切相关。总之，这些结果确立了基于图的立方体复制分析作为一种可解释、非侵入性和可扩展的阿尔茨海默病筛查方法。

## 🔬 方法详解

**问题定义**：阿尔茨海默病(AD)的早期诊断面临挑战，现有方法通常复杂且难以普及。手绘立方体复制任务虽然简单，但蕴含丰富的视觉空间信息，如何有效提取并利用这些信息是关键。现有方法，如基于像素的卷积神经网络，难以捕捉立方体图的几何结构和拓扑关系。

**核心思路**：将手绘立方体图转换为图结构，利用图神经网络(GNN)提取节点特征（空间坐标、局部图元拓扑、角度几何），从而更好地捕捉立方体图的几何和拓扑信息。结合人口统计学信息和神经心理测试(NPT)分数，进行多模态融合，提升诊断准确率。

**技术框架**：整体框架包括以下几个阶段：1) 数据预处理：将手绘立方体图转换为图结构，节点表示立方体的顶点，边表示连接关系。2) 特征提取：提取节点的空间坐标、局部图元拓扑和角度几何特征。3) 图神经网络处理：使用GNN对图结构进行学习，提取图级别的特征表示。4) 多模态融合：将GNN提取的图特征与人口统计学信息和NPT分数进行融合。5) 分类：使用分类器（如全连接网络）进行AD诊断。

**关键创新**：主要创新在于将手绘立方体图转换为图结构，并利用图神经网络进行特征提取。与传统的基于像素的卷积神经网络相比，GNN能够更好地捕捉立方体图的几何结构和拓扑关系，从而提高诊断准确率。此外，多模态融合也进一步提升了性能。

**关键设计**：节点特征包括：1) 空间坐标：节点的二维坐标。2) 局部图元拓扑：使用Graphlet Counting统计每个节点周围的局部图元数量。3) 角度几何：计算节点之间的角度关系。GNN采用Graph Convolutional Network (GCN)或Graph Attention Network (GAT)。损失函数采用交叉熵损失函数。后期融合采用简单的拼接或加权平均方法。

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

实验结果表明，基于图的表示方法在单模态情况下优于基于像素的卷积模型。多模态融合进一步提升了性能，并提高了对类别不平衡的鲁棒性。SHAP分析表明，特定的图元模式和几何扭曲是关键的预测因子，与临床观察结果一致。该方法在阿尔茨海默病诊断任务上取得了显著的性能提升。

## 🎯 应用场景

该研究成果可应用于阿尔茨海默病的早期筛查和诊断，尤其适用于基层医疗机构，具有非侵入性、低成本、易于实施的优点。通过结合手绘立方体图分析和简单的认知测试，可以辅助医生进行初步诊断，为进一步的临床评估提供参考。未来，该方法有望推广到其他神经退行性疾病的早期诊断。

## 📄 摘要（原文）

> Early and accessible detection of Alzheimer's disease (AD) remains a critical clinical challenge, and cube-copying tasks offer a simple yet informative assessment of visuospatial function. This work proposes a multimodal framework that converts hand-drawn cube sketches into graph-structured representations capturing geometric and topological properties, and integrates these features with demographic information and neuropsychological test (NPT) scores for AD classification. Cube drawings are modeled as graphs with node features encoding spatial coordinates, local graphlet-based topology, and angular geometry, which are processed using graph neural networks and fused with age, education, and NPT features in a late-fusion model. Experimental results show that graph-based representations provide a strong unimodal baseline and substantially outperform pixel-based convolutional models, while multimodal integration further improves performance and robustness to class imbalance. SHAP-based interpretability analysis identifies specific graphlet motifs and geometric distortions as key predictors, closely aligning with clinical observations of disorganized cube drawings in AD. Together, these results establish graph-based analysis of cube copying as an interpretable, non-invasive, and scalable approach for Alzheimer's disease screening.

