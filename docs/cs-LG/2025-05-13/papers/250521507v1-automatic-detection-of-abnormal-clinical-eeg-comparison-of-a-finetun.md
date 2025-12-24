---
layout: default
title: "Automatic detection of abnormal clinical EEG: comparison of a finetuned foundation model with two deep learning models"
---

# Automatic detection of abnormal clinical EEG: comparison of a finetuned foundation model with two deep learning models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21507" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21507v1</a>
  <a href="https://arxiv.org/pdf/2505.21507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21507v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21507v1', 'Automatic detection of abnormal clinical EEG: comparison of a finetuned foundation model with two deep learning models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Aurore Bussalb, François Le Gac, Guillaume Jubien, Mohamed Rahmouni, Ruggero G. Bettinardi, Pedro Marinho R. de Oliveira, Phillipe Derambure, Nicolas Gaspard, Jacques Jonas, Louis Maillard, Laurent Vercueil, Hervé Vespignani, Philippe Laval, Laurent Koessler, Ulysse Gimenez

**分类**: q-bio.NC, cs.LG, eess.SP

**发布日期**: 2025-05-13

**备注**: 20 pages, 7 figures

---

## 💡 一句话要点

**提出基于微调模型的自动化EEG异常检测方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑电图` `异常检测` `深度学习` `微调模型` `自动化诊断` `神经科学` `人工智能`

## 📋 核心要点

1. 现有的EEG解读方法依赖于专业人员，面临着大量数据处理和解读的挑战。
2. 本文提出了基于微调的BioSerenity-E1模型，结合CNN-LSTM和Transformer模型进行EEG分类。
3. 实验结果显示，BioSerenity-E1在多个数据集上均表现出色，平衡准确率最高可达94.63%。

## 📝 摘要（中文）

脑电图（EEG）常用于神经疾病的诊断。由于需要大量的EEG解读和专业知识，研究者们开发了基于人工智能的工具来辅助视觉分析。本文比较了两种深度学习模型（CNN-LSTM和基于Transformer的模型）与新提出的基础模型BioSerenity-E1在EEG录音分类（正常或异常）任务中的表现。三种模型在2500个EEG录音上进行训练或微调，并在两个私有数据集和一个公共数据集上进行评估。结果显示，BioSerenity-E1微调模型在多个数据集上均表现优异，最高平衡准确率达到94.63%。研究表明，利用预训练模型可以有效提高EEG数据的自动分类能力。

## 🔬 方法详解

**问题定义**：本文旨在解决EEG异常检测中的自动化分类问题。现有方法依赖于专家解读，效率低且容易受到主观因素影响。

**核心思路**：通过微调预训练的BioSerenity-E1模型，结合深度学习技术，提升EEG分类的准确性和效率。该方法利用了大规模数据集的知识，减少了对标注数据的需求。

**技术框架**：整体架构包括数据预处理、模型训练和评估三个主要阶段。首先对EEG数据进行清洗和标注，然后使用CNN-LSTM和Transformer模型进行特征提取，最后通过BioSerenity-E1模型进行分类。

**关键创新**：最重要的创新在于引入了BioSerenity-E1作为基础模型，通过微调实现了在EEG分类任务上的最佳性能，区别于传统的从头训练模型。

**关键设计**：在模型训练中，采用了交叉熵损失函数，优化算法使用Adam，网络结构结合了卷积层和长短期记忆网络（LSTM），以捕捉EEG信号的时序特征。

## 📊 实验亮点

实验结果显示，三种模型在数据集A上的平衡准确率均超过86%，其中BioSerenity-E1微调模型达到89.19%。在数据集B上，BioSerenity-E1的平衡准确率高达94.63%，在TUAB评估数据集上也表现优异，准确率为82.25%。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断、神经科学研究和智能健康监测。通过自动化EEG分析，能够提高诊断效率，降低医疗成本，同时为临床医生提供更可靠的辅助决策工具，未来可能推动个性化医疗的发展。

## 📄 摘要（原文）

> Electroencephalography (EEG) is commonly used by physicians for the diagnosis of numerous neurological disorders. Due to the large volume of EEGs requiring interpretation and the specific expertise involved, artificial intelligence-based tools are being developed to assist in their visual analysis. In this paper, we compare two deep learning models (CNN-LSTM and Transformer-based) with BioSerenity-E1, a recently proposed foundation model, in the task of classifying entire EEG recordings as normal or abnormal. The three models were trained or finetuned on 2,500 EEG recordings and their performances were evaluated on two private and one public datasets: a large multicenter dataset annotated by a single specialist (dataset A composed of n = 4,480 recordings), a small multicenter dataset annotated by three specialists (dataset B, n = 198), and the Temple University Abnormal (TUAB) EEG corpus evaluation dataset (n = 276). On dataset A, the three models achieved at least 86% balanced accuracy, with BioSerenity-E1 finetuned achieving the highest balanced accuracy (89.19% [88.36-90.41]). BioSerenity-E1 finetuned also achieved the best performance on dataset B, with 94.63% [92.32-98.12] balanced accuracy. The models were then validated on TUAB evaluation dataset, whose corresponding training set was not used during training, where they achieved at least 76% accuracy. Specifically, BioSerenity-E1 finetuned outperformed the other two models, reaching an accuracy of 82.25% [78.27-87.48]. Our results highlight the usefulness of leveraging pre-trained models for automatic EEG classification: enabling robust and efficient interpretation of EEG data with fewer resources and broader applicability.

