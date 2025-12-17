---
layout: default
title: Predictive Modeling of Flood-Prone Areas Using SAR and Environmental Variables
---

# Predictive Modeling of Flood-Prone Areas Using SAR and Environmental Variables

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13710" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13710</a>
  <a href="https://arxiv.org/pdf/2512.13710.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13710" onclick="toggleFavorite(this, '2512.13710', 'Predictive Modeling of Flood-Prone Areas Using SAR and Environmental Variables')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Edwin Oluoch Awino, Denis Machanda

**分类**: cs.LG

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**结合SAR与环境数据，提出基于随机森林的洪水易发区预测模型**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `洪水易发性预测` `SAR遥感` `机器学习` `随机森林` `环境因子` `灾害风险评估` `土地利用规划`

## 📋 核心要点

1. 洪水是全球最具破坏性的自然灾害之一，现有方法难以在数据稀缺地区进行准确的洪水易发性预测。
2. 本研究结合SAR数据和环境因子，利用机器学习方法构建洪水易发性预测模型，旨在提高预测精度。
3. 实验结果表明，随机森林模型在尼扬多河流域的洪水易发性预测中表现最佳，准确率达到0.762。

## 📝 摘要（中文）

本研究结合合成孔径雷达(SAR)影像与环境及水文数据，对肯尼亚西部尼扬多河流域的洪水易发性进行建模。利用2024年5月洪涝事件的Sentinel-1双极化SAR数据生成二元洪水清单，作为机器学习(ML)模型的训练数据。结合坡度、海拔、坡向、土地利用/土地覆盖、土壤类型和距河流距离等六个条件因子，训练了逻辑回归(LR)、分类与回归树(CART)、支持向量机(SVM)和随机森林(RF)四种监督分类器。通过准确率、Cohen's Kappa系数和受试者工作特征(ROC)分析评估模型性能。结果表明，RF取得了最高的预测性能(准确率=0.762; Kappa=0.480)，优于LR、CART和SVM。基于RF的易发性地图显示，维多利亚湖附近的低洼卡诺平原具有最高的洪水脆弱性，与历史洪水记录和2024年5月事件的影响一致。这些发现证明了在数据有限的地区，结合SAR数据和集成ML方法进行洪水易发性制图的价值。研究结果为降低灾害风险、土地利用规划和早期预警系统开发提供了重要见解。

## 🔬 方法详解

**问题定义**：论文旨在解决在数据有限的地区，如何准确预测洪水易发区域的问题。现有方法在这些区域往往缺乏足够的数据支持，导致预测精度不高，难以有效支持灾害风险管理和土地利用规划。

**核心思路**：论文的核心思路是结合SAR遥感数据和环境因子，利用机器学习方法构建洪水易发性预测模型。SAR数据能够提供地表水淹信息的直接观测，而环境因子则反映了地形、地貌、土壤等影响洪水发生的潜在因素。通过将两者结合，可以更全面地刻画洪水发生的条件，提高预测精度。

**技术框架**：整体流程包括以下几个主要阶段：1) 数据收集与预处理：收集Sentinel-1 SAR数据、环境因子数据（坡度、海拔等）以及历史洪水事件数据；2) 特征提取与选择：从SAR数据中提取洪水淹没区域，并结合环境因子构建特征向量；3) 模型训练与评估：使用逻辑回归、CART、SVM和随机森林等机器学习模型进行训练，并使用准确率、Kappa系数和ROC曲线等指标评估模型性能；4) 洪水易发性制图：基于训练好的模型，生成洪水易发性地图。

**关键创新**：论文的关键创新在于将SAR数据与环境因子相结合，并采用集成学习方法（随机森林）进行洪水易发性预测。SAR数据能够提供实时的地表水淹信息，弥补了传统方法中数据不足的缺陷。随机森林模型能够有效地处理高维数据和非线性关系，提高预测精度。

**关键设计**：论文中关键的设计包括：1) 使用Sentinel-1双极化SAR数据，能够提供更丰富的地表信息；2) 选择坡度、海拔、坡向、土地利用/土地覆盖、土壤类型和距河流距离等六个关键环境因子；3) 使用准确率、Cohen's Kappa系数和ROC分析等多种指标综合评估模型性能；4) 采用随机森林模型，并对其参数进行优化，以获得最佳的预测效果。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13710/Picture1.jpg" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13710/Picture2.jpg" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.13710/Picture3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，随机森林模型在尼扬多河流域的洪水易发性预测中表现最佳，准确率达到0.762，Kappa系数为0.480，显著优于逻辑回归、CART和SVM等传统机器学习模型。该研究验证了结合SAR数据和集成学习方法在洪水易发性预测中的有效性。

## 🎯 应用场景

该研究成果可应用于洪水灾害风险评估、土地利用规划和早期预警系统开发。通过生成高精度的洪水易发性地图，可以帮助政府和相关机构更好地了解洪水风险分布，制定合理的防洪措施，优化土地利用规划，并建立有效的早期预警系统，从而减少洪水灾害造成的损失。

## 📄 摘要（原文）

> Flooding is one of the most destructive natural hazards worldwide, posing serious risks to ecosystems, infrastructure, and human livelihoods. This study combines Synthetic Aperture Radar (SAR) imagery with environmental and hydrological data to model flood susceptibility in the River Nyando watershed, western Kenya. Sentinel-1 dual-polarization SAR data from the May 2024 flood event were processed to produce a binary flood inventory, which served as training data for machine learning (ML) models. Six conditioning factors -- slope, elevation, aspect, land use/land cover, soil type, and distance from streams -- were integrated with the SAR-derived flood inventory to train four supervised classifiers: Logistic Regression (LR), Classification and Regression Trees (CART), Support Vector Machines (SVM), and Random Forest (RF). Model performance was assessed using accuracy, Cohen's Kappa, and Receiver Operating Characteristic (ROC) analysis. Results indicate that RF achieved the highest predictive performance (accuracy = 0.762; Kappa = 0.480), outperforming LR, CART, and SVM. The RF-based susceptibility map showed that low-lying Kano Plains near Lake Victoria have the highest flood vulnerability, consistent with historical flood records and the impacts of the May 2024 event. These findings demonstrate the value of combining SAR data and ensemble ML methods for flood susceptibility mapping in regions with limited data. The resulting maps offer important insights for disaster risk reduction, land-use planning, and early warning system development.

