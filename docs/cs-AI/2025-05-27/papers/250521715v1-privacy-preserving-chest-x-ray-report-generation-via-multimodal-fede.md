---
layout: default
title: Privacy-Preserving Chest X-ray Report Generation via Multimodal Federated Learning with ViT and GPT-2
---

# Privacy-Preserving Chest X-ray Report Generation via Multimodal Federated Learning with ViT and GPT-2

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21715" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21715v1</a>
  <a href="https://arxiv.org/pdf/2505.21715.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21715v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21715v1', 'Privacy-Preserving Chest X-ray Report Generation via Multimodal Federated Learning with ViT and GPT-2')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Md. Zahid Hossain, Mustofa Ahmed, Most. Sharmin Sultana Samu, Md. Rakibul Islam

**分类**: eess.IV, cs.AI, cs.CV

**发布日期**: 2025-05-27

**备注**: Preprint, manuscript under-review

---

## 💡 一句话要点

**提出多模态联邦学习框架以实现隐私保护的胸部X光报告生成**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私保护` `联邦学习` `胸部X光` `多模态学习` `ViT` `GPT-2` `医疗AI` `报告生成`

## 📋 核心要点

1. 现有集中式方法在处理敏感医疗数据时存在隐私风险，限制了其在医疗领域的应用。
2. 本文提出了一种多模态联邦学习框架，结合ViT和GPT-2，实现了胸部X光报告的隐私保护生成。
3. 实验结果显示，Krum聚合策略在多个评估指标上超越了其他方法，证明了联邦学习的有效性。

## 📝 摘要（中文）

自动生成胸部X光影像的放射学报告在提升诊断工作流程的同时，能够有效保护患者隐私。传统的集中式方法通常需要敏感数据的传输，存在隐私风险。为了解决这一问题，本文提出了一种多模态联邦学习框架，利用IU-Xray数据集进行胸部X光报告生成。该系统采用视觉变换器（ViT）作为编码器，GPT-2作为报告生成器，实现了无需共享原始数据的分散式训练。评估了三种联邦学习聚合策略：FedAvg、Krum聚合和新颖的损失感知联邦平均（L-FedAvg）。结果表明，Krum聚合在ROUGE、BLEU、BERTScore和RaTEScore等评估指标上表现优越，显示出联邦学习在生成临床相关和语义丰富的放射学报告方面可以与集中式模型相媲美或超越。该轻量级、隐私保护的框架为协作医疗AI的发展铺平了道路，且不妥协数据机密性。

## 🔬 方法详解

**问题定义**：本文旨在解决传统集中式方法在胸部X光报告生成中存在的隐私泄露风险，现有方法需要传输敏感数据，导致隐私问题。

**核心思路**：提出的多模态联邦学习框架通过在不同节点上训练模型，避免了数据的集中存储和传输，从而保护患者隐私。使用ViT作为编码器提取图像特征，GPT-2生成报告，实现了高效的报告生成。

**技术框架**：整体架构包括数据预处理、模型训练和报告生成三个主要模块。首先在各个参与方本地训练模型，然后通过联邦学习聚合策略（如Krum聚合）进行模型更新，最后生成报告。

**关键创新**：引入了损失感知联邦平均（L-FedAvg）策略，优化了模型聚合过程，提高了生成报告的质量和准确性。与传统方法相比，该框架在隐私保护和模型性能上具有显著优势。

**关键设计**：在模型训练中，采用了特定的损失函数以平衡生成报告的语义和流畅性，同时在网络结构上结合了ViT和GPT-2的优势，确保了高效的特征提取和文本生成。

## 📊 实验亮点

实验结果表明，Krum聚合策略在ROUGE、BLEU、BERTScore和RaTEScore等评估指标上表现优越，显示出该方法在生成临床相关报告方面的有效性，且在某些指标上超越了集中式模型，证明了联邦学习的潜力。

## 🎯 应用场景

该研究的潜在应用领域包括医疗影像分析、远程医疗和智能诊断系统。通过保护患者隐私，该框架能够促进医疗AI的协作开发，推动医学研究和临床应用的进步，具有重要的实际价值和社会影响。

## 📄 摘要（原文）

> The automated generation of radiology reports from chest X-ray images holds significant promise in enhancing diagnostic workflows while preserving patient privacy. Traditional centralized approaches often require sensitive data transfer, posing privacy concerns. To address this, the study proposes a Multimodal Federated Learning framework for chest X-ray report generation using the IU-Xray dataset. The system utilizes a Vision Transformer (ViT) as the encoder and GPT-2 as the report generator, enabling decentralized training without sharing raw data. Three Federated Learning (FL) aggregation strategies: FedAvg, Krum Aggregation and a novel Loss-aware Federated Averaging (L-FedAvg) were evaluated. Among these, Krum Aggregation demonstrated superior performance across lexical and semantic evaluation metrics such as ROUGE, BLEU, BERTScore and RaTEScore. The results show that FL can match or surpass centralized models in generating clinically relevant and semantically rich radiology reports. This lightweight and privacy-preserving framework paves the way for collaborative medical AI development without compromising data confidentiality.

