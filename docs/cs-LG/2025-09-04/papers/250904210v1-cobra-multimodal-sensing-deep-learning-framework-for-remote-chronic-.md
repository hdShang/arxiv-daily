---
layout: default
title: "COBRA: Multimodal Sensing Deep Learning Framework for Remote Chronic Obesity Management via Wrist-Worn Activity Monitoring"
---

# COBRA: Multimodal Sensing Deep Learning Framework for Remote Chronic Obesity Management via Wrist-Worn Activity Monitoring

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04210" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04210v1</a>
  <a href="https://arxiv.org/pdf/2509.04210.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04210v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04210v1', 'COBRA: Multimodal Sensing Deep Learning Framework for Remote Chronic Obesity Management via Wrist-Worn Activity Monitoring')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhengyang Shen, Bo Gao, Mayue Shi

**分类**: cs.CE, cs.LG

**发布日期**: 2025-09-04

**备注**: 19 pages, 4 figures. *Correspondence: m.shi16@imperial.ac.uk. Accepted by the IUPESM World Congress on Medical Physics and Biomedical Engineering 2025

---

## 💡 一句话要点

**COBRA：基于腕戴式多模态传感器的远程慢性肥胖管理深度学习框架**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `慢性肥胖管理` `腕戴式传感器` `多模态融合` `深度学习` `行为识别`

## 📋 核心要点

1. 传统肥胖管理依赖自我报告，但存在主观偏差和回忆困难，难以有效整合到现代数字健康系统中。
2. COBRA框架利用腕戴式多模态传感器数据，结合深度学习模型D-Net，客观识别与肥胖相关的行为模式。
3. 实验结果表明，COBRA在行为识别准确率上优于现有方法，且具有良好的泛化能力和较低的人口统计学差异。

## 📝 摘要（中文）

本研究提出了一种名为COBRA（慢性肥胖行为识别架构）的新型深度学习框架，旨在利用腕戴式多模态传感器进行客观的行为监测，从而实现慢性肥胖管理。传统自报告方法存在严重的信息低报和回忆偏差，且难以与现代数字健康系统集成。COBRA集成了混合D-Net架构，该架构结合了U-Net空间建模、多头自注意力机制和BiLSTM时间处理，将日常活动分为四类与肥胖相关的类别：食物摄入、身体活动、久坐行为和日常生活。在包含51名受试者进行18项活动的WISDM-Smart数据集上验证，COBRA的最佳预处理策略结合了频谱-时间特征提取，在多种架构中实现了高性能。D-Net展示了96.86%的总体准确率，各类别的F1分数分别为98.55%（身体活动）、95.53%（食物摄入）、94.63%（久坐行为）和98.68%（日常生活），在准确率方面优于最先进的基线1.18%。该框架显示出强大的泛化能力，人口统计学差异较小（<3%），能够实现可扩展的部署，用于个性化的肥胖干预和持续的生活方式监测。

## 🔬 方法详解

**问题定义**：论文旨在解决慢性肥胖管理中，依赖主观自我报告进行行为监测的局限性问题。现有方法存在信息低报、回忆偏差等问题，难以准确评估能量平衡行为，并与数字健康系统有效集成。

**核心思路**：论文的核心思路是利用腕戴式多模态传感器获取的客观数据，通过深度学习模型自动识别与肥胖相关的行为模式。通过融合空间、时间和注意力机制，提升行为识别的准确性和鲁棒性。

**技术框架**：COBRA框架主要包含数据预处理、特征提取和行为分类三个阶段。首先，对腕戴式传感器数据进行预处理，包括数据清洗、归一化等。然后，采用频谱-时间特征提取方法，提取有代表性的特征。最后，将提取的特征输入到D-Net模型中进行分类，D-Net模型是一个混合架构，结合了U-Net空间建模、多头自注意力机制和BiLSTM时间处理。

**关键创新**：COBRA的关键创新在于D-Net混合架构的设计，它能够有效地融合空间、时间和注意力信息，从而提升行为识别的准确性和鲁棒性。具体来说，U-Net用于捕捉空间特征，多头自注意力机制用于关注重要的时间步，BiLSTM用于建模时间序列的依赖关系。此外，论文还探索了最佳的预处理策略，进一步提升了模型的性能。

**关键设计**：D-Net模型包含多个U-Net模块，每个模块负责提取不同尺度的空间特征。多头自注意力机制采用8个注意力头，用于捕捉不同时间步之间的依赖关系。BiLSTM采用128个隐藏单元，用于建模时间序列的长期依赖关系。损失函数采用交叉熵损失函数，优化器采用Adam优化器，学习率为0.001。

## 📊 实验亮点

COBRA框架在WISDM-Smart数据集上取得了显著的性能提升。D-Net模型实现了96.86%的总体准确率，各类别的F1分数均超过94%。与最先进的基线方法相比，COBRA在准确率方面提升了1.18%。此外，该框架还表现出良好的泛化能力，人口统计学差异小于3%，表明其具有实际应用潜力。

## 🎯 应用场景

COBRA框架可应用于远程慢性肥胖管理、个性化健康干预、生活方式监测等领域。通过客观、持续地监测用户的行为模式，可以为医生和患者提供更准确的健康评估和干预建议，从而改善肥胖管理效果，降低相关疾病风险。该研究为可穿戴设备在健康领域的应用提供了新的思路。

## 📄 摘要（原文）

> Chronic obesity management requires continuous monitoring of energy balance behaviors, yet traditional self-reported methods suffer from significant underreporting and recall bias, and difficulty in integration with modern digital health systems. This study presents COBRA (Chronic Obesity Behavioral Recognition Architecture), a novel deep learning framework for objective behavioral monitoring using wrist-worn multimodal sensors. COBRA integrates a hybrid D-Net architecture combining U-Net spatial modeling, multi-head self-attention mechanisms, and BiLSTM temporal processing to classify daily activities into four obesity-relevant categories: Food Intake, Physical Activity, Sedentary Behavior, and Daily Living. Validated on the WISDM-Smart dataset with 51 subjects performing 18 activities, COBRA's optimal preprocessing strategy combines spectral-temporal feature extraction, achieving high performance across multiple architectures. D-Net demonstrates 96.86% overall accuracy with category-specific F1-scores of 98.55% (Physical Activity), 95.53% (Food Intake), 94.63% (Sedentary Behavior), and 98.68% (Daily Living), outperforming state-of-the-art baselines by 1.18% in accuracy. The framework shows robust generalizability with low demographic variance (<3%), enabling scalable deployment for personalized obesity interventions and continuous lifestyle monitoring.

