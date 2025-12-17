---
layout: default
title: Probabilistic Hyper-Graphs using Multiple Randomly Masked Autoencoders for Semi-supervised Multi-modal Multi-task Learning
---

# Probabilistic Hyper-Graphs using Multiple Randomly Masked Autoencoders for Semi-supervised Multi-modal Multi-task Learning

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10068" target="_blank" class="toolbar-btn">arXiv: 2510.10068v2</a>
    <a href="https://arxiv.org/pdf/2510.10068.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10068v2" 
            onclick="toggleFavorite(this, '2510.10068v2', 'Probabilistic Hyper-Graphs using Multiple Randomly Masked Autoencoders for Semi-supervised Multi-modal Multi-task Learning')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Pîrvu Mihai-Cristian, Marius Leordeanu

**分类**: cs.CV

**发布日期**: 2025-10-11 (更新: 2025-11-25)

**备注**: Submitted to Neurocomputing

---

## 💡 一句话要点

**提出PHG-MAE模型，结合神经图和掩码自编码器，用于半监督多模态多任务学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `多模态学习` `半监督学习` `掩码自编码器` `概率超图` `知识蒸馏` `多任务学习` `无人机场景`

## 📋 核心要点

1. 现有方法在多模态多任务学习中，难以有效融合不同模态信息，且依赖大量标注数据。
2. 提出PHG-MAE模型，通过随机掩码模态模拟超边分布，并结合预训练和微调，实现模态融合。
3. 实验表明，该模型在无人机场景数据集上表现出色，且可通过知识蒸馏压缩模型规模。

## 📝 摘要（中文）

计算机视觉领域受益于跨多种模态的丰富数据，从而改进各种视觉任务。最近，人们非常关注通过掩码自编码器(MAE)进行自监督预训练的方法，通常将其用作优化下游任务（如分类或回归）的第一步。这非常有用，因为它不需要任何手动标记的数据。在这项工作中，我们介绍了一种基于掩码自编码器的概率超图(PHG-MAE)：一种新颖的模型，它在共同的理论框架下统一了神经图的经典工作与掩码自编码器的现代方法。通过随机掩盖整个模态（而不仅仅是patches），该模型在每次前向传递中从超边的分布中采样。此外，该模型通过将预训练和微调结合到单个训练循环中来改进标准的MAE算法。此外，我们的方法能够创建推理时集成，通过聚合来提高最终预测性能和一致性。最后，我们表明我们可以对集成应用知识蒸馏，而性能损失很小，即使是参数少于100万的模型也是如此。虽然我们的工作主要集中在包含多种世界解释和模态的室外无人机场景，但相同的步骤可以在其他类似领域（如自动驾驶或室内机器人）中遵循。为了简化集成用于计算机视觉多模态多任务学习(MTL)场景的外部预训练专家的过程，我们开发了一个数据管道软件。使用此工具，我们创建并发布了Dronescapes数据集的完全自动化扩展。所有技术细节、代码和重现步骤都已公开发布。

## 🔬 方法详解

**问题定义**：论文旨在解决半监督多模态多任务学习问题，特别是在数据标注稀缺的情况下，如何有效利用多模态信息提升模型性能。现有方法通常需要大量标注数据，且难以充分融合不同模态的特征，导致模型泛化能力受限。

**核心思路**：论文的核心思路是将神经图的思想与掩码自编码器相结合，构建概率超图。通过随机掩码不同的模态，模型可以学习到不同模态之间的依赖关系，并从超边的分布中采样，从而实现模态融合。同时，将预训练和微调整合到单个训练循环中，提高了训练效率。

**技术框架**：PHG-MAE模型主要包含以下几个模块：1) 多个掩码自编码器(MAE)，每个MAE处理一种模态的数据，并随机掩码部分模态；2) 概率超图构建模块，根据MAE的输出构建超图，超边表示不同模态之间的关系；3) 多任务学习模块，利用超图信息进行多任务学习，例如分类、回归等。整个流程包括数据输入、MAE编码、超图构建、多任务学习和结果输出。

**关键创新**：论文最重要的创新点在于将概率超图与掩码自编码器相结合，提出了一种新的多模态融合方法。与传统的模态融合方法相比，PHG-MAE能够更好地捕捉不同模态之间的复杂关系，并且可以通过随机掩码模态来模拟数据缺失的情况，提高模型的鲁棒性。此外，将预训练和微调整合到单个训练循环中，也提高了训练效率。

**关键设计**：在具体实现上，论文采用了随机掩码策略，每次随机选择一部分模态进行掩码，并使用MAE重建被掩码的模态。损失函数包括重建损失和多任务学习损失。网络结构方面，可以采用不同的MAE架构，例如ViT等。此外，论文还探索了知识蒸馏技术，将大型集成模型蒸馏到小型模型中，以减少模型参数量。

## 📊 实验亮点

论文通过实验验证了PHG-MAE模型的有效性。在Dronescapes数据集上，该模型取得了显著的性能提升，尤其是在数据标注稀缺的情况下。此外，通过知识蒸馏，可以将模型参数量减少到1M以下，而性能损失很小，这使得该模型更易于部署到资源受限的设备上。

## 🎯 应用场景

该研究成果可应用于多种需要多模态信息融合的场景，例如自动驾驶、机器人导航、遥感图像分析等。通过融合不同传感器的数据，例如摄像头、激光雷达、雷达等，可以提高环境感知能力，从而提升系统的安全性和可靠性。此外，该方法还可以应用于医疗图像分析、金融风险评估等领域，具有广泛的应用前景。

## 📄 摘要（原文）

> The computer vision domain has greatly benefited from an abundance of data across many modalities to improve on various visual tasks. Recently, there has been a lot of focus on self-supervised pre-training methods through Masked Autoencoders (MAE) \cite{he2022masked,bachmann2022multimae}, usually used as a first step before optimizing for a downstream task, such as classification or regression. This is very useful as it doesn't require any manually labeled data. In this work, we introduce Probabilistic Hyper-Graphs using Masked Autoencoders (PHG-MAE): a novel model that unifies the classical work on neural graphs \cite{leordeanu2021semi} with the modern approach of masked autoencoders under a common theoretical framework. Through random masking of entire modalities, not just patches, the model samples from the distribution of hyper-edges on each forward pass. Additionally, the model adapts the standard MAE algorithm by combining pre-training and fine-tuning into a single training loop. Moreover, our approach enables the creation of inference-time ensembles which, through aggregation, boost the final prediction performance and consistency. Lastly, we show that we can apply knowledge distillation on top of the ensembles with little loss in performance, even with models that have fewer than 1M parameters. While our work mostly focuses on outdoor UAV scenes that contain multiple world interpretations and modalities, the same steps can be followed in other similar domains, such as autonomous driving or indoor robotics. In order to streamline the process of integrating external pre-trained experts for computer vision multi-modal multi-task learning (MTL) scenarios, we developed a data-pipeline software. Using this tool, we have created and released a fully-automated extension of the Dronescapes dataset. All the technical details, code and reproduction steps are publicly released.

