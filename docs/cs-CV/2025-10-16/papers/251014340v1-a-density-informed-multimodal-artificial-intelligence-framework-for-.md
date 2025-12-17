---
layout: default
title: A Density-Informed Multimodal Artificial Intelligence Framework for Improving Breast Cancer Detection Across All Breast Densities
---

# A Density-Informed Multimodal Artificial Intelligence Framework for Improving Breast Cancer Detection Across All Breast Densities

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.14340" class="toolbar-btn" target="_blank">📄 arXiv: 2510.14340v1</a>
  <a href="https://arxiv.org/pdf/2510.14340.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.14340v1" onclick="toggleFavorite(this, '2510.14340v1', 'A Density-Informed Multimodal Artificial Intelligence Framework for Improving Breast Cancer Detection Across All Breast Densities')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Siva Teja Kakileti, Bharath Govindaraju, Sudhakar Sampangi, Geetha Manjunath

**分类**: eess.IV, cs.AI, cs.CV, cs.LG

**发布日期**: 2025-10-16

---

## 💡 一句话要点

**提出多模态人工智能框架以改善乳腺癌检测效果**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `乳腺癌检测` `多模态人工智能` `热成像` `乳腺密度` `深度学习` `医疗影像` `放射组学`

## 📋 核心要点

1. 现有的乳腺X光摄影在乳腺组织密度较高的女性中灵敏度显著降低，导致漏诊风险增加。
2. 提出了一种基于乳腺密度的信息的多模态人工智能框架，动态选择适合的成像方式以提高检测效果。
3. 实验结果显示，该框架在不同乳腺密度下均表现优异，灵敏度和特异性均高于单一成像方法。

## 📝 摘要（中文）

乳腺X光摄影是当前乳腺癌筛查的标准方法，但在乳腺组织密度较高的女性中，其灵敏度降低，导致漏诊或延误诊断。本文研究了一种基于乳腺密度的信息的多模态人工智能框架，旨在通过动态选择适当的成像方式来提高癌症检测率。研究中对324名女性进行了乳腺X光摄影和热成像的联合检测，结果表明该框架在不同乳腺组织类型下均表现出色，灵敏度达到94.55%，特异性为79.93%，显著优于单一成像方法。该框架具有可解释性、低成本和易于部署的特点，为提高乳腺癌筛查结果提供了切实可行的路径。

## 🔬 方法详解

**问题定义**：本研究旨在解决乳腺X光摄影在高密度乳腺组织中灵敏度不足的问题，导致乳腺癌的漏诊和延误。现有方法在不同乳腺密度下的表现不均，亟需改进。

**核心思路**：提出的多模态人工智能框架根据乳腺组织的组成动态选择成像方式，利用乳腺X光摄影和热成像的互补优势，以提高整体癌症检测的准确性和灵敏度。

**技术框架**：该框架包括两个主要模块：乳腺X光摄影的多视角深度学习模型和热成像的血管及热特征分析。根据乳腺组织的密度，分别使用不同的AI模型进行分析，从而优化预测结果。

**关键创新**：最重要的创新在于引入了乳腺密度信息来指导成像方式的选择，使得框架能够在不同乳腺组织类型下均保持高灵敏度，克服了单一成像方法的局限性。

**关键设计**：在模型设计中，乳腺X光摄影使用多视角深度学习网络，而热成像则通过血管和热特征的放射组学进行分析。灵敏度和特异性通过交叉验证和统计分析进行评估，确保模型的可靠性。

## 📊 实验亮点

实验结果显示，该多模态框架的灵敏度达到94.55%，特异性为79.93%，显著优于单独使用乳腺X光摄影（灵敏度81.82%，特异性86.25%）和热成像（灵敏度92.73%，特异性75.46%）。在高密度乳腺组织中，乳腺X光摄影的灵敏度降至67.86%，而热成像保持在92.59%，显示出该框架的优势。

## 🎯 应用场景

该研究的多模态人工智能框架可广泛应用于乳腺癌筛查，尤其是在资源有限的环境中，能够有效提高乳腺癌的早期检测率。其低成本和易部署的特点使其适合在不同医疗条件下推广，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> Mammography, the current standard for breast cancer screening, has reduced sensitivity in women with dense breast tissue, contributing to missed or delayed diagnoses. Thermalytix, an AI-based thermal imaging modality, captures functional vascular and metabolic cues that may complement mammographic structural data. This study investigates whether a breast density-informed multi-modal AI framework can improve cancer detection by dynamically selecting the appropriate imaging modality based on breast tissue composition. A total of 324 women underwent both mammography and thermal imaging. Mammography images were analyzed using a multi-view deep learning model, while Thermalytix assessed thermal images through vascular and thermal radiomics. The proposed framework utilized Mammography AI for fatty breasts and Thermalytix AI for dense breasts, optimizing predictions based on tissue type. This multi-modal AI framework achieved a sensitivity of 94.55% (95% CI: 88.54-100) and specificity of 79.93% (95% CI: 75.14-84.71), outperforming standalone mammography AI (sensitivity 81.82%, specificity 86.25%) and Thermalytix AI (sensitivity 92.73%, specificity 75.46%). Importantly, the sensitivity of Mammography dropped significantly in dense breasts (67.86%) versus fatty breasts (96.30%), whereas Thermalytix AI maintained high and consistent sensitivity in both (92.59% and 92.86%, respectively). This demonstrates that a density-informed multi-modal AI framework can overcome key limitations of unimodal screening and deliver high performance across diverse breast compositions. The proposed framework is interpretable, low-cost, and easily deployable, offering a practical path to improving breast cancer screening outcomes in both high-resource and resource-limited settings.

