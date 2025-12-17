---
layout: default
title: MRI-Based Brain Age Estimation with Supervised Contrastive Learning of Continuous Representation
---

# MRI-Based Brain Age Estimation with Supervised Contrastive Learning of Continuous Representation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.22102" class="toolbar-btn" target="_blank">📄 arXiv: 2511.22102v1</a>
  <a href="https://arxiv.org/pdf/2511.22102.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.22102v1" onclick="toggleFavorite(this, '2511.22102v1', 'MRI-Based Brain Age Estimation with Supervised Contrastive Learning of Continuous Representation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Simon Joseph Clément Crête, Marta Kersten-Oertel, Yiming Xiao

**分类**: cs.CV, cs.LG

**发布日期**: 2025-11-27

---

## 💡 一句话要点

**提出基于监督对比学习的MRI脑年龄估计方法，提升神经形态学变化建模精度。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `脑年龄估计` `监督对比学习` `MRI` `神经形态学` `Rank-N-Contrast` `深度学习` `生物标志物`

## 📋 核心要点

1. 现有基于深度学习的脑年龄估计方法难以捕捉神经形态学的连续变化，导致特征表示不够理想。
2. 论文提出使用监督对比学习和Rank-N-Contrast损失函数，学习更具区分性的连续特征表示，提升脑年龄估计精度。
3. 实验表明，该方法在小数据集上优于传统深度回归，并可与大数据集上的SOTA方法媲美，且能有效应用于疾病研究。

## 📝 摘要（中文）

本文提出了一种基于监督对比学习的MRI脑年龄估计模型，旨在解决现有深度学习回归方法在捕捉神经形态学连续变化方面的不足。该模型利用Rank-N-Contrast (RNC)损失函数，首次将监督对比学习应用于基于T1w结构MRI的脑年龄估计。实验结果表明，在有限的训练数据集上，该方法取得了4.27年的平均绝对误差(MAE)和0.93的R平方值，显著优于使用相同ResNet骨干网络的传统深度回归方法，并且性能优于或可与使用更大训练数据集的现有最优方法相媲美。此外，Grad-RAM可视化结果显示，RNC损失函数能够提取与年龄回归相关的更细微的特征。作为探索性研究，该方法被用于评估阿尔茨海默病和帕金森病患者的生物年龄与实际年龄之间的差距，并揭示了脑年龄差距与疾病严重程度之间的相关性，证明了其作为神经退行性疾病生物标志物的潜力。

## 🔬 方法详解

**问题定义**：现有的基于深度学习的脑年龄估计方法，通常采用回归模型直接预测年龄。然而，神经形态学的变化是连续的，简单的回归方法难以充分捕捉这种连续性，导致特征表示不够优化，影响预测精度。此外，现有方法对小样本数据的表现不佳，且缺乏对模型预测结果的可解释性。

**核心思路**：论文的核心思路是将脑年龄估计问题转化为一个排序问题，利用监督对比学习的思想，通过Rank-N-Contrast (RNC)损失函数，学习具有区分性的连续特征表示。RNC损失函数鼓励相同年龄的样本在特征空间中更接近，而不同年龄的样本则尽可能远离，从而更好地捕捉神经形态学的连续变化。

**技术框架**：该方法使用T1w结构MRI作为输入，首先通过一个ResNet骨干网络提取特征。然后，将提取的特征输入到监督对比学习模块，使用RNC损失函数进行训练。最后，使用训练好的模型进行脑年龄估计。为了提高模型的可解释性，论文还使用了Grad-RAM技术来可视化模型关注的区域。

**关键创新**：该方法的主要创新点在于首次将监督对比学习和RNC损失函数应用于基于MRI的脑年龄估计。与传统的回归方法相比，监督对比学习能够更好地捕捉神经形态学的连续变化，从而提高预测精度。此外，RNC损失函数能够有效地利用样本的排序信息，进一步提升模型的性能。

**关键设计**：论文使用了ResNet作为骨干网络，并对网络结构进行了一些调整以适应脑年龄估计任务。RNC损失函数的具体形式为：对于每个样本，选择N个与其年龄最接近的样本作为正样本，其余样本作为负样本。损失函数的目标是使正样本的特征向量与该样本的特征向量之间的距离尽可能小，而负样本的特征向量与该样本的特征向量之间的距离尽可能大。论文还使用了Grad-RAM技术来可视化模型关注的区域，从而提高模型的可解释性。

## 📊 实验亮点

实验结果表明，该方法在有限的训练数据集上取得了4.27年的平均绝对误差(MAE)和0.93的R平方值，显著优于使用相同ResNet骨干网络的传统深度回归方法。与使用更大训练数据集的现有最优方法相比，该方法也表现出更好的性能或可比性。此外，Grad-RAM可视化结果显示，RNC损失函数能够提取与年龄回归相关的更细微的特征。

## 🎯 应用场景

该研究成果可应用于神经退行性疾病的早期诊断和风险评估，例如阿尔茨海默病和帕金森病。通过评估患者的生物年龄与实际年龄之间的差距，可以作为疾病进展的生物标志物，辅助临床决策。此外，该方法还可以用于研究不同因素（如生活方式、环境等）对脑年龄的影响，为制定个性化的健康干预措施提供依据。

## 📄 摘要（原文）

> MRI-based brain age estimation models aim to assess a subject's biological brain age based on information, such as neuroanatomical features. Various factors, including neurodegenerative diseases, can accelerate brain aging and measuring this phenomena could serve as a potential biomarker for clinical applications. While deep learning (DL)-based regression has recently attracted major attention, existing approaches often fail to capture the continuous nature of neuromorphological changes, potentially resulting in sub-optimal feature representation and results. To address this, we propose to use supervised contrastive learning with the recent Rank-N-Contrast (RNC) loss to estimate brain age based on widely used T1w structural MRI for the first time and leverage Grad-RAM to visually explain regression results. Experiments show that our proposed method achieves a mean absolute error (MAE) of 4.27 years and an $R^2$ of 0.93 with a limited dataset of training samples, significantly outperforming conventional deep regression with the same ResNet backbone while performing better or comparably with the state-of-the-art methods with significantly larger training data. Furthermore, Grad-RAM revealed more nuanced features related to age regression with the RNC loss than conventional deep regression. As an exploratory study, we employed the proposed method to estimate the gap between the biological and chronological brain ages in Alzheimer's Disease and Parkinson's disease patients, and revealed the correlation between the brain age gap and disease severity, demonstrating its potential as a biomarker in neurodegenerative disorders.

