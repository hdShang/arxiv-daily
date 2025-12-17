---
layout: default
title: Post-TIPS Prediction via Multimodal Interaction: A Multi-Center Dataset and Framework for Survival, Complication, and Portal Pressure Assessment
---

# Post-TIPS Prediction via Multimodal Interaction: A Multi-Center Dataset and Framework for Survival, Complication, and Portal Pressure Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.10464" class="toolbar-btn" target="_blank">📄 arXiv: 2510.10464v1</a>
  <a href="https://arxiv.org/pdf/2510.10464.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10464v1" onclick="toggleFavorite(this, '2510.10464v1', 'Post-TIPS Prediction via Multimodal Interaction: A Multi-Center Dataset and Framework for Survival, Complication, and Portal Pressure Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junhao Dong, Dejia Liu, Ruiqi Ding, Zongxing Chen, Yingjie Huang, Zhu Meng, Jianbo Zhao, Zhicheng Zhao, Fei Su

**分类**: cs.CV

**发布日期**: 2025-10-12

**备注**: 81 pages, 13 figures

---

## 💡 一句话要点

**提出MultiTIPS数据集和多模态交互框架，用于TIPS术后生存、并发症和门静脉压力评估。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `TIPS预后` `多模态学习` `医学图像分析` `多任务学习` `放射组学` `肝性脑病` `门静脉高压`

## 📋 核心要点

1. 现有TIPS预后模型依赖人工标注ROI，单模态方法泛化性差，且评估指标单一，限制了临床应用。
2. 论文提出MultiTIPS数据集和多模态交互框架，通过双选项分割、多模态交互和多任务预测提升预后评估。
3. 实验表明，该方法在MultiTIPS数据集上优于现有方法，具有良好的跨域泛化能力和可解释性。

## 📝 摘要（中文）

经颈静脉肝内门体分流术(TIPS)是治疗门静脉高压的常用方法，但其生存结果差异大，且常发生明显的肝性脑病(OHE)，因此需要准确的术前预后建模。目前的研究通常从术前CT图像或临床特征构建机器学习模型，但面临三个关键挑战：(1)费力的人工感兴趣区域(ROI)标注，(2)单模态方法可靠性和泛化性差，(3)单终点预测评估不完整。此外，缺乏公开可用的数据集限制了该领域的研究。因此，我们提出了MultiTIPS，这是第一个用于TIPS预后的公共多中心数据集，并在此基础上提出了一个新的多模态预后框架。该框架包括三个核心模块：(1)双选项分割，集成了半监督和基于基础模型的流程，以在有限的标注下实现稳健的ROI分割，并促进后续的特征提取；(2)多模态交互，引入了多粒度放射组学注意力(MGRA)、渐进正交解耦(POD)和临床指导的预后增强(CGPE)三种技术，以实现跨模态特征交互和互补表示集成，从而提高模型准确性和鲁棒性；(3)多任务预测，采用分阶段训练策略，对生存、门静脉压力梯度(PPG)和OHE预测进行稳定优化，以进行全面的预后评估。在MultiTIPS上的大量实验表明，所提出的方法优于最先进的方法，并具有强大的跨域泛化能力和可解释性，表明其在临床应用中的前景。数据集和代码均已公开。

## 🔬 方法详解

**问题定义**：现有TIPS预后模型主要依赖于人工标注的CT图像ROI或临床特征，存在标注成本高、单模态信息利用不足、泛化能力差以及评估指标单一等问题。这些问题限制了TIPS预后模型的临床应用价值。

**核心思路**：论文的核心思路是利用多模态信息（CT图像和临床数据）进行互补，通过设计精巧的交互模块，充分挖掘不同模态之间的关联性，从而提升预后预测的准确性和鲁棒性。同时，采用多任务学习框架，综合评估生存率、门静脉压力梯度和肝性脑病等多个指标，提供更全面的预后信息。

**技术框架**：该框架包含三个主要模块：(1) **双选项分割**：利用半监督学习和基于预训练模型的方法，实现对肝脏等关键区域的自动分割，减少人工标注成本。(2) **多模态交互**：通过多粒度放射组学注意力(MGRA)、渐进正交解耦(POD)和临床指导的预后增强(CGPE)三种技术，实现CT图像和临床特征的深度融合和交互。(3) **多任务预测**：采用分阶段训练策略，同时预测生存率、门静脉压力梯度和肝性脑病等多个指标。

**关键创新**：论文的关键创新在于多模态交互模块的设计，特别是MGRA、POD和CGPE三种技术的结合使用。MGRA关注不同粒度的放射组学特征，POD用于解耦模态间的冗余信息，CGPE则利用临床知识指导特征学习，从而实现更有效的跨模态特征融合。此外，MultiTIPS数据集的发布也为该领域的研究提供了宝贵资源。

**关键设计**：在双选项分割模块中，具体采用了哪些半监督学习算法和预训练模型（例如，是否使用了特定的肝脏分割模型？）。在多模态交互模块中，MGRA的具体实现方式（例如，如何定义不同粒度的放射组学特征？注意力机制的具体结构是什么？），POD的解耦策略（例如，如何定义正交性？使用什么损失函数？）以及CGPE的临床知识融入方式（例如，如何将临床先验知识编码到模型中？）是关键的技术细节。多任务学习中，各个任务的损失函数权重如何设置，以及分阶段训练的具体策略也需要进一步了解。

## 📊 实验亮点

实验结果表明，该方法在MultiTIPS数据集上显著优于现有方法，在生存预测、门静脉压力梯度预测和肝性脑病预测方面均取得了更好的性能。同时，该方法具有良好的跨域泛化能力和可解释性，表明其具有很强的临床应用潜力。具体的性能提升数据（例如，AUC、C-index等）需要在论文中查找。

## 🎯 应用场景

该研究成果可应用于临床TIPS手术的术前风险评估，帮助医生更准确地预测患者的预后，制定更合理的治疗方案，降低并发症发生率，提高患者生存率。此外，MultiTIPS数据集的发布将促进TIPS预后相关研究的发展。

## 📄 摘要（原文）

> Transjugular intrahepatic portosystemic shunt (TIPS) is an established procedure for portal hypertension, but provides variable survival outcomes and frequent overt hepatic encephalopathy (OHE), indicating the necessity of accurate preoperative prognostic modeling. Current studies typically build machine learning models from preoperative CT images or clinical characteristics, but face three key challenges: (1) labor-intensive region-of-interest (ROI) annotation, (2) poor reliability and generalizability of unimodal methods, and (3) incomplete assessment from single-endpoint prediction. Moreover, the lack of publicly accessible datasets constrains research in this field. Therefore, we present MultiTIPS, the first public multi-center dataset for TIPS prognosis, and propose a novel multimodal prognostic framework based on it. The framework comprises three core modules: (1) dual-option segmentation, which integrates semi-supervised and foundation model-based pipelines to achieve robust ROI segmentation with limited annotations and facilitate subsequent feature extraction; (2) multimodal interaction, where three techniques, multi-grained radiomics attention (MGRA), progressive orthogonal disentanglement (POD), and clinically guided prognostic enhancement (CGPE), are introduced to enable cross-modal feature interaction and complementary representation integration, thus improving model accuracy and robustness; and (3) multi-task prediction, where a staged training strategy is used to perform stable optimization of survival, portal pressure gradient (PPG), and OHE prediction for comprehensive prognostic assessment. Extensive experiments on MultiTIPS demonstrate the superiority of the proposed method over state-of-the-art approaches, along with strong cross-domain generalization and interpretability, indicating its promise for clinical application. The dataset and code are available.

