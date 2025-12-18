---
layout: default
title: GateFuseNet: An Adaptive 3D Multimodal Neuroimaging Fusion Network for Parkinson's Disease Diagnosis
---

# GateFuseNet: An Adaptive 3D Multimodal Neuroimaging Fusion Network for Parkinson's Disease Diagnosis

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.22507" class="toolbar-btn" target="_blank">📄 arXiv: 2510.22507v1</a>
  <a href="https://arxiv.org/pdf/2510.22507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22507v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.22507v1', 'GateFuseNet: An Adaptive 3D Multimodal Neuroimaging Fusion Network for Parkinson\'s Disease Diagnosis')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Rui Jin, Chen Chen, Yin Liu, Hongfu Sun, Min Zeng, Min Li, Yang Gao

**分类**: cs.CV, cs.AI

**发布日期**: 2025-10-26

**备注**: The first two authors contributed equally to this work. Correspondence to: Yang Gao, E-mail: yang.gao@csu.edu.cn

**🔗 代码/项目**: [GITHUB](https://github.com/YangGaoUQ/GateFuseNet)

---

## 💡 一句话要点

**GateFuseNet：一种自适应3D多模态神经影像融合网络，用于帕金森病诊断**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `帕金森病诊断` `多模态融合` `神经影像` `深度学习` `注意力机制`

## 📋 核心要点

1. 帕金森病MRI诊断面临症状多样性和病理异质性的挑战，传统T1w图像敏感性不足。
2. GateFuseNet通过门控融合模块，自适应地融合QSM和T1w图像，增强ROI特征并抑制噪声。
3. 实验表明，GateFuseNet在帕金森病诊断中优于现有方法，准确率达85.00%，AUC达92.06%。

## 📝 摘要（中文）

由于症状变异性和病理异质性，通过MRI准确诊断帕金森病(PD)仍然具有挑战性。现有方法大多依赖于传统的基于幅度的MRI模态，如T1加权图像(T1w)，但其对PD病理的敏感性低于定量磁化率映射(QSM)。QSM是一种基于相位的MRI技术，可量化深部灰质核团中的铁沉积。本研究提出GateFuseNet，一种自适应3D多模态融合网络，集成了QSM和T1w图像用于PD诊断。核心创新在于门控融合模块，该模块学习模态特定的注意力权重和通道方向的门控向量，以进行选择性的特征调制。这种分层门控机制增强了ROI感知的特征，同时抑制了不相关的信号。实验结果表明，我们的方法优于三种现有的最先进方法，实现了85.00%的准确率和92.06%的AUC。消融研究进一步验证了ROI引导、多模态集成和融合定位的贡献。Grad-CAM可视化证实了该模型对临床相关病理区域的关注。源代码和预训练模型可在https://github.com/YangGaoUQ/GateFuseNet找到。

## 🔬 方法详解

**问题定义**：论文旨在解决帕金森病（PD）诊断中，传统MRI方法（如T1w）对病理敏感性不足的问题。现有方法难以有效利用多模态MRI信息，且易受症状变异性和病理异质性的影响，导致诊断准确率不高。

**核心思路**：论文的核心思路是设计一个自适应的多模态融合网络，利用QSM图像对铁沉积的敏感性，并结合T1w图像的结构信息，通过门控机制选择性地融合不同模态的特征，从而提高PD诊断的准确性。这种设计旨在增强与PD相关的ROI区域的特征，同时抑制不相关的噪声信号。

**技术框架**：GateFuseNet的整体架构包含以下主要模块：1) 特征提取模块：分别从QSM和T1w图像中提取特征。2) 门控融合模块：学习模态特定的注意力权重和通道方向的门控向量，用于选择性地融合不同模态的特征。3) 分类模块：基于融合后的特征进行PD诊断。该网络采用3D卷积神经网络结构，以充分利用MRI图像的三维空间信息。

**关键创新**：最重要的技术创新点在于门控融合模块。该模块通过学习模态特定的注意力权重，自适应地调整不同模态特征的贡献，从而实现更有效的多模态融合。此外，通道方向的门控向量可以进一步选择重要的特征通道，抑制噪声。这种分层门控机制是与现有方法的主要区别。

**关键设计**：门控融合模块的关键设计包括：1) 使用注意力机制学习模态权重，权重值介于0和1之间，表示每个模态的重要性。2) 使用sigmoid函数生成通道方向的门控向量，控制每个通道的特征是否被激活。3) 损失函数包括交叉熵损失，用于优化分类性能。网络结构采用3D卷积，并使用了ReLU激活函数。

## 📊 实验亮点

GateFuseNet在帕金森病诊断任务中取得了显著的性能提升，相较于三种最先进的方法，准确率提高了85.00%，AUC达到了92.06%。消融实验验证了ROI引导、多模态集成和融合定位的有效性。Grad-CAM可视化结果表明，模型能够关注到临床相关的病理区域，例如黑质等。

## 🎯 应用场景

该研究成果可应用于帕金森病的早期诊断和辅助诊断，帮助医生更准确地识别患者。通过结合QSM和T1w等多模态MRI信息，有望提高诊断的敏感性和特异性。未来，该方法可以扩展到其他神经退行性疾病的诊断，并为个性化治疗方案的制定提供依据。

## 📄 摘要（原文）

> Accurate diagnosis of Parkinson's disease (PD) from MRI remains challenging due to symptom variability and pathological heterogeneity. Most existing methods rely on conventional magnitude-based MRI modalities, such as T1-weighted images (T1w), which are less sensitive to PD pathology than Quantitative Susceptibility Mapping (QSM), a phase-based MRI technique that quantifies iron deposition in deep gray matter nuclei. In this study, we propose GateFuseNet, an adaptive 3D multimodal fusion network that integrates QSM and T1w images for PD diagnosis. The core innovation lies in a gated fusion module that learns modality-specific attention weights and channel-wise gating vectors for selective feature modulation. This hierarchical gating mechanism enhances ROI-aware features while suppressing irrelevant signals. Experimental results show that our method outperforms three existing state-of-the-art approaches, achieving 85.00% accuracy and 92.06% AUC. Ablation studies further validate the contributions of ROI guidance, multimodal integration, and fusion positioning. Grad-CAM visualizations confirm the model's focus on clinically relevant pathological regions. The source codes and pretrained models can be found at https://github.com/YangGaoUQ/GateFuseNet

