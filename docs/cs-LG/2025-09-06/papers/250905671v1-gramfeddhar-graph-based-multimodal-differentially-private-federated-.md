---
layout: default
title: "GraMFedDHAR: Graph Based Multimodal Differentially Private Federated HAR"
---

# GraMFedDHAR: Graph Based Multimodal Differentially Private Federated HAR

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.05671" class="toolbar-btn" target="_blank">📄 arXiv: 2509.05671v1</a>
  <a href="https://arxiv.org/pdf/2509.05671.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.05671v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.05671v1', 'GraMFedDHAR: Graph Based Multimodal Differentially Private Federated HAR')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Labani Halder, Tanmay Sen, Sarbani Palit

**分类**: cs.LG, cs.AI, cs.CR, stat.ML

**发布日期**: 2025-09-06

---

## 💡 一句话要点

**GraMFedDHAR：图神经网络与差分隐私联邦学习用于多模态人体活动识别**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人体活动识别` `多模态学习` `图神经网络` `联邦学习` `差分隐私` `传感器数据融合`

## 📋 核心要点

1. 传统集中式深度学习在多模态人体活动识别中面临数据共享限制和隐私问题，联邦学习虽能保护隐私，但异构多模态数据和差分隐私需求带来新的挑战。
2. GraMFedDHAR框架将多模态传感器数据建模为图，利用图卷积神经网络提取特征，并通过注意力机制融合，旨在提升活动识别的鲁棒性和准确性。
3. 实验结果表明，该框架在非差分隐私和差分隐私设置下均优于基线模型，尤其在差分隐私约束下，性能提升显著，验证了图神经网络的有效性。

## 📝 摘要（中文）

本文提出了一种基于图的多模态联邦学习框架GraMFedDHAR，用于人体活动识别(HAR)任务。该框架将压力垫、深度相机和多个加速度计等不同的传感器数据流建模为特定模态的图，通过残差图卷积神经网络(GCNs)进行处理，并通过基于注意力的加权融合，而非简单的拼接。融合后的嵌入能够实现鲁棒的活动分类，而差分隐私则在联邦聚合过程中保护数据。实验结果表明，所提出的MultiModalGCN模型优于基线MultiModalFFN，在集中式和联邦范式中，非差分隐私设置下的准确率提高了2%。更重要的是，在差分隐私约束下观察到显著的改进：MultiModalGCN始终优于MultiModalFFN，性能差距在7%到13%之间，具体取决于隐私预算和设置。这些结果突出了基于图的建模在多模态学习中的鲁棒性，其中GNN被证明更能抵抗由差分隐私噪声引起的性能下降。

## 🔬 方法详解

**问题定义**：论文旨在解决多模态人体活动识别中，由于数据异构性、标注数据稀缺以及隐私保护需求带来的挑战。现有方法，如传统的集中式深度学习，受限于数据共享和隐私泄露风险。联邦学习虽然解决了数据共享问题，但难以有效处理多模态数据的融合，并且在引入差分隐私后，模型性能会显著下降。

**核心思路**：论文的核心思路是将不同的传感器数据（如压力垫、深度相机、加速度计）建模成不同的图结构，利用图卷积神经网络(GCN)提取每个模态的特征，然后通过注意力机制自适应地融合这些特征。这种基于图的建模方式能够更好地捕捉多模态数据之间的关系，并且GCN对差分隐私引入的噪声具有更强的鲁棒性。

**技术框架**：GraMFedDHAR框架包含以下几个主要模块：1) **数据预处理**：将不同模态的传感器数据进行清洗和预处理。2) **图构建**：将每个模态的数据构建成图结构，例如，将加速度计数据构建成时间序列图。3) **图卷积神经网络(GCN)**：使用残差GCN提取每个模态的特征表示。4) **注意力融合**：使用注意力机制对不同模态的特征进行加权融合，得到最终的融合特征。5) **活动分类**：使用分类器（如全连接层）对融合特征进行活动分类。6) **联邦学习聚合**：在联邦学习框架下，客户端本地训练模型，然后将模型参数上传到服务器进行聚合。7) **差分隐私**：在模型参数上传之前，对参数添加噪声，以满足差分隐私的要求。

**关键创新**：论文的关键创新在于：1) **基于图的多模态建模**：将多模态数据建模成图结构，能够更好地捕捉数据之间的关系。2) **残差图卷积神经网络(GCN)**：使用残差GCN提取特征，能够有效解决深层GCN的梯度消失问题。3) **注意力融合机制**：使用注意力机制自适应地融合不同模态的特征，能够更好地利用不同模态的信息。4) **差分隐私联邦学习**：在联邦学习框架下引入差分隐私，能够在保护用户隐私的同时，保证模型的性能。

**关键设计**：论文的关键设计包括：1) **图的构建方式**：根据不同模态数据的特点，设计不同的图结构。例如，对于时间序列数据，可以构建时间序列图；对于空间数据，可以构建空间图。2) **残差GCN的网络结构**：设计合适的残差GCN网络结构，包括GCN的层数、每层的节点数等。3) **注意力机制的设计**：选择合适的注意力机制，例如，自注意力机制或交叉注意力机制。4) **差分隐私的参数设置**：选择合适的差分隐私参数，例如，隐私预算ε和δ，以平衡隐私保护和模型性能。

## 📊 实验亮点

实验结果表明，所提出的MultiModalGCN模型在非差分隐私设置下，相较于基线MultiModalFFN模型，准确率提高了2%。更重要的是，在差分隐私约束下，MultiModalGCN的性能显著优于MultiModalFFN，性能差距在7%到13%之间，证明了图神经网络在多模态学习和差分隐私场景下的鲁棒性。

## 🎯 应用场景

该研究成果可应用于智能家居、医疗健康、养老监护等领域。通过分析用户的活动数据，可以实现跌倒检测、异常行为预警、健康状态评估等功能，从而提高生活质量和安全性。未来，该技术有望与可穿戴设备、物联网传感器等结合，构建更加智能化的健康监测系统。

## 📄 摘要（原文）

> Human Activity Recognition (HAR) using multimodal sensor data remains challenging due to noisy or incomplete measurements, scarcity of labeled examples, and privacy concerns. Traditional centralized deep learning approaches are often constrained by infrastructure availability, network latency, and data sharing restrictions. While federated learning (FL) addresses privacy by training models locally and sharing only model parameters, it still has to tackle issues arising from the use of heterogeneous multimodal data and differential privacy requirements. In this article, a Graph-based Multimodal Federated Learning framework, GraMFedDHAR, is proposed for HAR tasks. Diverse sensor streams such as a pressure mat, depth camera, and multiple accelerometers are modeled as modality-specific graphs, processed through residual Graph Convolutional Neural Networks (GCNs), and fused via attention-based weighting rather than simple concatenation. The fused embeddings enable robust activity classification, while differential privacy safeguards data during federated aggregation. Experimental results show that the proposed MultiModalGCN model outperforms the baseline MultiModalFFN, with up to 2 percent higher accuracy in non-DP settings in both centralized and federated paradigms. More importantly, significant improvements are observed under differential privacy constraints: MultiModalGCN consistently surpasses MultiModalFFN, with performance gaps ranging from 7 to 13 percent depending on the privacy budget and setting. These results highlight the robustness of graph-based modeling in multimodal learning, where GNNs prove more resilient to the performance degradation introduced by DP noise.

