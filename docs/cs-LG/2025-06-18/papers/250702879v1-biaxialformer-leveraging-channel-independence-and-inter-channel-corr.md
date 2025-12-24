---
layout: default
title: "Biaxialformer: Leveraging Channel Independence and Inter-Channel Correlations in EEG Signal Decoding for Predicting Neurological Outcomes"
---

# Biaxialformer: Leveraging Channel Independence and Inter-Channel Correlations in EEG Signal Decoding for Predicting Neurological Outcomes

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02879" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02879v1</a>
  <a href="https://arxiv.org/pdf/2507.02879.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02879v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02879v1', 'Biaxialformer: Leveraging Channel Independence and Inter-Channel Correlations in EEG Signal Decoding for Predicting Neurological Outcomes')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Naimahmed Nesaragi, Hemin Ali Qadir, Per Steiner Halvorsen, Ilangko Balasingham

**分类**: eess.SP, cs.LG

**发布日期**: 2025-06-18

**备注**: 12 pages, 3 figures, Article

---

## 💡 一句话要点

**提出Biaxialformer以解决EEG信号解码中的通道相关性问题**

🎯 **匹配领域**: **支柱七：动作重定向 (Motion Retargeting)**

**关键词**: `EEG信号解码` `通道独立性` `Transformer模型` `神经结果预测` `双极EEG信号` `多变量分析` `注意力机制`

## 📋 核心要点

1. 现有的EEG信号解码方法往往忽视通道间的相关性，导致信息损失和预测准确性降低，尤其是在复杂的神经结果预测任务中。
2. Biaxialformer通过两阶段注意力机制独立捕捉时间和空间信息，促进通道间的协同，解决了传统模型的通道间相关性遗忘问题。
3. 在五家医院的I-CARE数据集上，Biaxialformer的平均AUC达到0.7688，AUPRC为0.8643，F1为0.6518，显示出良好的鲁棒性和泛化能力。

## 📝 摘要（中文）

准确解码EEG信号需要全面建模单通道内的时间动态和跨通道的空间依赖性。尽管基于Transformer的模型利用通道独立性策略在各种时间序列任务中表现出色，但往往忽视了多变量EEG信号中至关重要的通道间相关性。为了解决这些挑战，本文提出了Biaxialformer，一个经过精心设计的两阶段注意力框架，能够独立捕捉序列特定（时间）和通道特定（空间）的EEG信息，促进通道间的协同与相互增强，同时不牺牲通道独立性。通过联合学习位置编码，Biaxialformer保留了EEG数据中的时间和空间关系，减轻了传统通道独立模型中常见的通道间相关性遗忘问题。我们在五家医院的多中心I-CARE数据上验证了Biaxialformer的鲁棒性和泛化能力，平均AUC为0.7688，AUPRC为0.8643，F1为0.6518。

## 🔬 方法详解

**问题定义**：本文旨在解决EEG信号解码中通道间相关性被忽视的问题。现有方法在处理多变量EEG信号时，常常导致信息损失和预测准确性降低，尤其是在神经结果预测等复杂任务中。

**核心思路**：Biaxialformer的核心思路是通过两阶段注意力机制独立捕捉时间和空间信息，促进通道间的协同与相互增强，避免传统模型中通道间相关性遗忘的问题。

**技术框架**：Biaxialformer的整体架构包括两个主要模块：一是序列特定的时间注意力机制，二是通道特定的空间注意力机制。通过联合学习位置编码，模型能够有效保留EEG数据中的时间和空间关系。

**关键创新**：Biaxialformer的主要创新在于其两阶段注意力机制，能够同时处理时间和空间信息，解决了传统通道独立模型的局限性，特别是在多变量EEG信号分析中。

**关键设计**：模型设计中采用了可变感受野的标记化模块，以平衡细粒度局部特征和更广泛时间依赖性的提取。此外，利用双极EEG信号捕捉脑半球间的相互作用，增强空间特征提取能力。

## 📊 实验亮点

在五家医院的I-CARE数据集上，Biaxialformer的平均AUC为0.7688，AUPRC为0.8643，F1为0.6518，显示出显著的性能提升，相较于传统模型具有更好的鲁棒性和泛化能力。

## 🎯 应用场景

该研究的潜在应用领域包括神经科学、临床诊断和脑机接口等。通过提高EEG信号解码的准确性，Biaxialformer有助于更好地预测昏迷患者的神经结果，推动相关领域的研究和应用发展。

## 📄 摘要（原文）

> Accurate decoding of EEG signals requires comprehensive modeling of both temporal dynamics within individual channels and spatial dependencies across channels. While Transformer-based models utilizing channel-independence (CI) strategies have demonstrated strong performance in various time series tasks, they often overlook the inter-channel correlations that are critical in multivariate EEG signals. This omission can lead to information degradation and reduced prediction accuracy, particularly in complex tasks such as neurological outcome prediction. To address these challenges, we propose Biaxialformer, characterized by a meticulously engineered two-stage attention-based framework. This model independently captures both sequence-specific (temporal) and channel-specific (spatial) EEG information, promoting synergy and mutual reinforcement across channels without sacrificing CI. By employing joint learning of positional encodings, Biaxialformer preserves both temporal and spatial relationships in EEG data, mitigating the interchannel correlation forgetting problem common in traditional CI models. Additionally, a tokenization module with variable receptive fields balance the extraction of fine-grained, localized features and broader temporal dependencies. To enhance spatial feature extraction, we leverage bipolar EEG signals, which capture inter-hemispheric brain interactions, a critical but often overlooked aspect in EEG analysis. Our study broadens the use of Transformer-based models by addressing the challenge of predicting neurological outcomes in comatose patients. Using the multicenter I-CARE data from five hospitals, we validate the robustness and generalizability of Biaxialformer with an average AUC 0.7688, AUPRC 0.8643, and F1 0.6518 in a cross-hospital scenario.

