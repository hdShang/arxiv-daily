---
layout: default
title: Evaluating the effects of preprocessing, method selection, and hyperparameter tuning on SAR-based flood mapping and water depth estimation
---

# Evaluating the effects of preprocessing, method selection, and hyperparameter tuning on SAR-based flood mapping and water depth estimation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.11305" class="toolbar-btn" target="_blank">📄 arXiv: 2510.11305v1</a>
  <a href="https://arxiv.org/pdf/2510.11305.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.11305v1" onclick="toggleFavorite(this, '2510.11305v1', 'Evaluating the effects of preprocessing, method selection, and hyperparameter tuning on SAR-based flood mapping and water depth estimation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jean-Paul Travert, Cédric Goeury, Sébastien Boyaval, Vito Bacchi, Fabrice Zaoui

**分类**: cs.CV, physics.geo-ph

**发布日期**: 2025-10-13

---

## 💡 一句话要点

**研究预处理、方法选择和超参数调整对SAR洪水制图和水深估计的影响**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `SAR图像` `洪水制图` `水深估计` `预处理` `超参数优化`

## 📋 核心要点

1. 现有SAR洪水制图方法在预处理、方法选择和超参数调整方面存在不确定性，影响水深估计的准确性。
2. 该研究通过评估不同预处理方法、洪水制图方法和水深估计方法，分析了它们对洪水范围和水深估计的影响。
3. 实验结果表明，方法选择和超参数调整对洪水制图和水深估计的精度有显著影响，应采用集成方法考虑不确定性。

## 📝 摘要（中文）

本研究利用合成孔径雷达(SAR)影像，评估了各种预处理（特别是斑点噪声降低）、洪水制图和水深估计方法，旨在校准和验证水力模型。通过考虑预处理后的图像、洪水地图和水深场的集合，研究了不同步骤中方法选择及其超参数的影响。评估针对2019年和2021年加龙河（法国）的两次洪水事件进行，使用水动力模拟和现场观测作为参考数据。结果表明，斑点滤波器的选择会改变洪水范围的估计，变化可达数平方公里。此外，洪水制图方法的选择和调整也会影响性能。虽然监督方法优于非监督方法，但经过调整的非监督方法（如局部阈值或变化检测）可以获得相当的结果。预处理和洪水制图步骤的复合不确定性也给水深场估计带来了很高的变异性。这项研究强调了考虑整个处理流程的重要性，包括预处理、洪水制图、水深估计方法及其相关的超参数。与其依赖单一配置，不如采用集成方法并考虑方法学的不确定性。对于洪水制图，方法选择的影响最大。对于水深估计，影响最大的处理步骤是洪水制图步骤产生的洪水地图输入以及方法的超参数。

## 🔬 方法详解

**问题定义**：论文旨在解决SAR图像洪水制图和水深估计中，由于预处理方法、洪水制图方法选择以及超参数调整不当导致的不确定性问题。现有方法通常依赖于单一配置，忽略了不同处理步骤之间的相互影响，导致结果不稳定和精度下降。

**核心思路**：论文的核心思路是采用一种集成方法，综合考虑预处理、洪水制图和水深估计三个步骤，并评估不同方法和超参数组合对结果的影响。通过对比分析，找出最佳的配置方案，并量化不同步骤引入的不确定性。

**技术框架**：整体流程包括以下几个阶段：1) SAR图像预处理，包括斑点噪声滤波等；2) 洪水制图，采用监督和非监督方法提取洪水范围；3) 水深估计，利用洪水地图和SAR图像信息计算水深；4) 结果评估，使用水动力模拟和现场观测数据作为参考，评估不同配置方案的性能。

**关键创新**：该研究的关键创新在于强调了整个处理流程的整体性，并采用集成方法来量化不同步骤引入的不确定性。与以往研究只关注单一方法或步骤不同，该研究综合考虑了预处理、洪水制图和水深估计之间的相互影响，从而提高了结果的稳定性和精度。

**关键设计**：论文的关键设计包括：1) 评估多种斑点噪声滤波器，比较其对洪水范围估计的影响；2) 对比监督和非监督洪水制图方法，并优化非监督方法的超参数；3) 使用水动力模拟和现场观测数据作为参考，对水深估计结果进行定量评估；4) 分析不同步骤引入的不确定性，并提出采用集成方法来降低不确定性的建议。

## 📊 实验亮点

研究结果表明，斑点滤波器的选择会显著影响洪水范围的估计，差异可达数平方公里。监督方法通常优于非监督方法，但经过优化的非监督方法（如局部阈值或变化检测）可以达到与监督方法相当的性能。此外，预处理和洪水制图步骤的复合不确定性会对水深估计产生显著影响，强调了考虑整个处理流程的重要性。

## 🎯 应用场景

该研究成果可应用于洪水灾害监测与评估、水资源管理、水利工程设计等领域。通过优化SAR图像处理流程，可以更准确地提取洪水范围和估计水深，为防洪减灾提供科学依据，并为水力模型的校准和验证提供数据支持。此外，该研究提出的集成方法可以推广到其他遥感应用领域，提高数据处理的可靠性和精度。

## 📄 摘要（原文）

> Flood mapping and water depth estimation from Synthetic Aperture Radar (SAR) imagery are crucial for calibrating and validating hydraulic models. This study uses SAR imagery to evaluate various preprocessing (especially speckle noise reduction), flood mapping, and water depth estimation methods. The impact of the choice of method at different steps and its hyperparameters is studied by considering an ensemble of preprocessed images, flood maps, and water depth fields. The evaluation is conducted for two flood events on the Garonne River (France) in 2019 and 2021, using hydrodynamic simulations and in-situ observations as reference data. Results show that the choice of speckle filter alters flood extent estimations with variations of several square kilometers. Furthermore, the selection and tuning of flood mapping methods also affect performance. While supervised methods outperformed unsupervised ones, tuned unsupervised approaches (such as local thresholding or change detection) can achieve comparable results. The compounded uncertainty from preprocessing and flood mapping steps also introduces high variability in the water depth field estimates. This study highlights the importance of considering the entire processing pipeline, encompassing preprocessing, flood mapping, and water depth estimation methods and their associated hyperparameters. Rather than relying on a single configuration, adopting an ensemble approach and accounting for methodological uncertainty should be privileged. For flood mapping, the method choice has the most influence. For water depth estimation, the most influential processing step was the flood map input resulting from the flood mapping step and the hyperparameters of the methods.

