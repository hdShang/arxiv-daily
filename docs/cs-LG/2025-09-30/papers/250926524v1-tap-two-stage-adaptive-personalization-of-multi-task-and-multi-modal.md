---
layout: default
title: "TAP: Two-Stage Adaptive Personalization of Multi-task and Multi-Modal Foundation Models in Federated Learning"
---

# TAP: Two-Stage Adaptive Personalization of Multi-task and Multi-Modal Foundation Models in Federated Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.26524" class="toolbar-btn" target="_blank">📄 arXiv: 2509.26524v1</a>
  <a href="https://arxiv.org/pdf/2509.26524.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.26524v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.26524v1', 'TAP: Two-Stage Adaptive Personalization of Multi-task and Multi-Modal Foundation Models in Federated Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Seohyun Lee, Wenzhi Fang, Dong-Jun Han, Seyyedali Hosseinalipour, Christopher G. Brinton

**分类**: cs.LG, cs.AI

**发布日期**: 2025-09-30

**🔗 代码/项目**: [GITHUB](https://github.com/lee3296/TAP)

---

## 💡 一句话要点

**提出TAP：联邦学习中多任务多模态基础模型的两阶段自适应个性化方法**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `联邦学习` `个性化建模` `多任务学习` `多模态学习` `知识蒸馏` `模型替换` `异构联邦学习`

## 📋 核心要点

1. 现有PFL方法在微调多任务多模态基础模型方面存在不足，尤其是在客户端数据、任务和模态异构的情况下。
2. TAP通过利用客户端与服务器之间模型架构的不匹配，自适应地进行模型替换和知识蒸馏，实现个性化。
3. 实验证明，TAP在各种数据集和任务中优于现有基线，验证了其在异构联邦学习环境下的有效性。

## 📝 摘要（中文）

联邦学习(FL)在去中心化地训练多个模型方面表现出令人印象深刻的能力，但最终模型并不一定完全适合每个客户端的需求。虽然在创建定制个性化模型(称为个性化联邦学习PFL)方面已经进行了大量工作，但通过微调具有多任务和多模态属性的基础模型进行个性化的研究较少。此外，文献中对于如何在客户端之间不仅在数据上，而且在任务和模态上存在异构性的情况下微调和个性化此类模型缺乏理解。为了解决文献中的这一空白，我们提出了TAP(两阶段自适应个性化)，它(i)利用客户端和服务器之间不匹配的模型架构，有选择地进行替换操作，当它有利于客户端的本地任务时，以及(ii)进行后FL知识蒸馏，以捕获有益的通用知识而不损害个性化。我们还首次对服务器模型在其模态-任务对架构下的收敛性进行了分析，并证明随着模态-任务对数量的增加，其满足所有任务的能力会受到影响。通过大量的实验，我们证明了我们提出的算法在各种数据集和任务中与多种基线相比的有效性。实现代码可在https://github.com/lee3296/TAP公开获得。

## 🔬 方法详解

**问题定义**：论文旨在解决联邦学习中，如何针对具有多任务和多模态属性的基础模型，在客户端数据、任务和模态异构的情况下，进行有效的个性化建模问题。现有方法难以兼顾模型的通用性和个性化，并且缺乏对异构性的有效处理。

**核心思路**：TAP的核心思路是分两个阶段进行自适应的个性化。第一阶段，利用客户端和服务器之间模型架构的不匹配，选择性地替换客户端模型的部分结构，以适应本地任务。第二阶段，进行后联邦学习的知识蒸馏，将服务器模型的通用知识迁移到客户端模型，同时保留客户端的个性化信息。

**技术框架**：TAP包含两个主要阶段：1) 自适应模型替换：客户端根据本地任务的需要，选择性地替换服务器模型的部分结构。替换的决策基于对本地任务的性能提升评估。2) 后联邦学习知识蒸馏：在联邦学习训练完成后，每个客户端使用本地数据，通过知识蒸馏的方式，从服务器模型中学习通用知识。

**关键创新**：TAP的关键创新在于其两阶段的自适应个性化策略。第一阶段的模型替换允许客户端根据本地任务的特点定制模型结构，而第二阶段的知识蒸馏则保证了客户端模型能够学习到服务器模型的通用知识，从而在个性化和通用性之间取得平衡。此外，论文还对服务器模型在多模态-多任务场景下的收敛性进行了分析。

**关键设计**：在模型替换阶段，客户端需要评估替换不同模型结构对本地任务性能的影响。这可以通过计算替换前后的损失函数差异来实现。知识蒸馏阶段可以使用标准的知识蒸馏损失函数，例如KL散度，来衡量客户端模型和服务器模型输出之间的差异。具体的参数设置需要根据具体的任务和数据集进行调整。

## 📊 实验亮点

实验结果表明，TAP在多个数据集和任务上均优于现有的个性化联邦学习方法。例如，在某个多模态数据集上，TAP相比于基线方法取得了显著的性能提升，验证了其在处理异构数据和任务方面的有效性。论文公开了代码，方便其他研究者复现和改进。

## 🎯 应用场景

TAP可应用于各种需要个性化建模的联邦学习场景，例如：医疗健康领域，不同医院拥有不同类型和格式的患者数据，需要训练个性化的诊断模型；智能推荐系统，不同用户具有不同的兴趣和偏好，需要训练个性化的推荐模型。该研究有助于提升联邦学习在异构环境下的应用效果，并促进多模态数据的有效利用。

## 📄 摘要（原文）

> Federated Learning (FL), despite demonstrating impressive capabilities in the training of multiple models in a decentralized manner, has been shown to produce a final model not necessarily well-suited to the needs of each client. While extensive work has been conducted on how to create tailored personalized models, called Personalized Federated Learning (PFL), less attention has been given to personalization via fine-tuning of foundation models with multi-task and multi-modal properties. Moreover, there exists a lack of understanding in the literature on how to fine-tune and personalize such models in a setting that is heterogeneous across clients not only in data, but also in tasks and modalities. To address this gap in the literature, we propose TAP (Two-Stage Adaptive Personalization), which (i) leverages mismatched model architectures between the clients and server to selectively conduct replacement operations when it benefits a client's local tasks and (ii) engages in post-FL knowledge distillation for capturing beneficial general knowledge without compromising personalization. We also introduce the first convergence analysis of the server model under its modality-task pair architecture, and demonstrate that as the number of modality-task pairs increases, its ability to cater to all tasks suffers. Through extensive experiments, we demonstrate the effectiveness of our proposed algorithm across a variety of datasets and tasks in comparison to a multitude of baselines. Implementation code is publicly available at https://github.com/lee3296/TAP.

