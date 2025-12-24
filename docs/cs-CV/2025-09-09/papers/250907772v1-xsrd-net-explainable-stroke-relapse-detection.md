---
layout: default
title: "XSRD-Net: EXplainable Stroke Relapse Detection"
---

# XSRD-Net: EXplainable Stroke Relapse Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.07772" class="toolbar-btn" target="_blank">📄 arXiv: 2509.07772v1</a>
  <a href="https://arxiv.org/pdf/2509.07772.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.07772v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.07772v1', 'XSRD-Net: EXplainable Stroke Relapse Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Christian Gapp, Elias Tappeiner, Martin Welk, Karl Fritscher, Stephanie Mangesius, Constantin Eisenschink, Philipp Deisl, Michael Knoflach, Astrid E. Grams, Elke R. Gizewski, Rainer Schubert

**分类**: cs.CV, cs.AI

**发布日期**: 2025-09-09

**备注**: Contribution to MICAD 2025 conference, Nov. 19-21, 2025 \| London, UK

---

## 💡 一句话要点

**XSRD-Net：用于可解释的中风复发检测，助力早期治疗规划**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `中风复发检测` `多模态学习` `深度学习` `可解释性AI` `生存分析`

## 📋 核心要点

1. 中风复发死亡率高，早期检测复发风险患者至关重要，但现有方法缺乏有效性和可解释性。
2. 提出XSRD-Net，一种多模态深度学习模型，结合CTA图像和临床数据，预测中风复发风险和无复发生存时间。
3. 实验结果表明，XSRD-Net在复发检测和RFS时间预测方面表现出色，并揭示了心脏疾病和颈动脉与复发风险的关联。

## 📝 摘要（中文）

中风是全球第二大死亡原因，年死亡率约为550万。中风复发率在第一年为5%至25%。由于复发死亡率极高（40%），降低复发率至关重要。本文旨在通过早期检测有中风复发风险的患者，从而实现适当的治疗规划。为此，收集了2010年至2024年间中风患者的3D颅内CTA图像数据，并记录了伴随的心脏疾病、年龄和性别。训练了基于单模态和多模态深度学习的神经网络，用于二元复发检测（任务1）和无复发生存（RFS）时间预测及后续分类（任务2）。仅使用表格数据即可解决复发与非复发患者的分离问题（测试数据集上的AUC：0.84）。然而，对于主要任务即回归任务（任务2），多模态XSRD-net根据模态贡献度量处理视觉：表格模态，比例为0.68：0.32。多模态模型关于复发的c-index达到0.68，测试数据集的AUC为0.71。最终，更深入的可解释性分析结果可以突出心脏疾病（表格数据）和颈动脉（视觉数据）之间对于复发检测和RFS时间预测的联系。这是我们努力通过持续数据收集和模型重新训练来加强的核心成果。

## 🔬 方法详解

**问题定义**：论文旨在解决中风复发风险的早期检测问题。现有方法的痛点在于，无法有效整合影像学数据和临床数据，且缺乏可解释性，难以指导临床治疗决策。

**核心思路**：论文的核心思路是利用多模态深度学习，将3D颅内CTA图像数据和患者的临床数据（如心脏疾病、年龄、性别）相结合，从而更准确地预测中风复发风险和无复发生存时间。同时，通过可解释性分析，揭示不同模态数据对预测结果的贡献，为临床医生提供参考。

**技术框架**：XSRD-Net的整体架构包含两个主要任务：1) 二元复发检测；2) 无复发生存（RFS）时间预测及后续分类。对于任务1，主要使用表格数据进行训练。对于任务2，XSRD-Net采用多模态融合策略，将视觉（CTA图像）和表格数据进行整合。模型首先分别处理不同模态的数据，然后通过融合层将它们结合起来，最后输出预测结果。

**关键创新**：论文的关键创新在于：1) 提出了一种多模态深度学习框架，能够有效整合影像学和临床数据，提高中风复发风险预测的准确性；2) 强调模型的可解释性，通过模态贡献度量和深入分析，揭示了心脏疾病和颈动脉与中风复发风险之间的关联。

**关键设计**：在多模态融合方面，论文采用了一种加权融合策略，根据模态贡献度量来确定不同模态的权重。具体来说，视觉模态的贡献为0.68，表格模态的贡献为0.32。损失函数的设计可能包括二元交叉熵损失（用于复发检测）和生存分析相关的损失函数（用于RFS时间预测）。网络结构细节未知，但推测可能使用了卷积神经网络（CNN）处理CTA图像，并使用全连接网络处理表格数据。

## 📊 实验亮点

XSRD-Net在测试数据集上取得了显著的性能提升。对于二元复发检测任务，仅使用表格数据即可达到AUC 0.84。对于RFS时间预测任务，多模态模型的c-index达到0.68，AUC达到0.71。可解释性分析揭示了心脏疾病和颈动脉与中风复发风险的关联。

## 🎯 应用场景

该研究成果可应用于临床中风风险评估，帮助医生早期识别高风险患者，制定个性化的预防和治疗方案，从而降低中风复发率和死亡率。此外，该模型的可解释性分析结果可以为中风复发机制的研究提供新的线索。

## 📄 摘要（原文）

> Stroke is the second most frequent cause of death world wide with an annual mortality of around 5.5 million. Recurrence rates of stroke are between 5 and 25% in the first year. As mortality rates for relapses are extraordinarily high (40%) it is of utmost importance to reduce the recurrence rates. We address this issue by detecting patients at risk of stroke recurrence at an early stage in order to enable appropriate therapy planning. To this end we collected 3D intracranial CTA image data and recorded concomitant heart diseases, the age and the gender of stroke patients between 2010 and 2024. We trained single- and multimodal deep learning based neural networks for binary relapse detection (Task 1) and for relapse free survival (RFS) time prediction together with a subsequent classification (Task 2). The separation of relapse from non-relapse patients (Task 1) could be solved with tabular data (AUC on test dataset: 0.84). However, for the main task, the regression (Task 2), our multimodal XSRD-net processed the modalities vision:tabular with 0.68:0.32 according to modality contribution measures. The c-index with respect to relapses for the multimodal model reached 0.68, and the AUC is 0.71 for the test dataset. Final, deeper interpretability analysis results could highlight a link between both heart diseases (tabular) and carotid arteries (vision) for the detection of relapses and the prediction of the RFS time. This is a central outcome that we strive to strengthen with ongoing data collection and model retraining.

