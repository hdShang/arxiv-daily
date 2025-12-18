---
layout: default
title: Supervised Contrastive Frame Aggregation for Video Representation Learning
---

# Supervised Contrastive Frame Aggregation for Video Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.12549" class="toolbar-btn" target="_blank">📄 arXiv: 2512.12549v1</a>
  <a href="https://arxiv.org/pdf/2512.12549.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.12549v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.12549v1', 'Supervised Contrastive Frame Aggregation for Video Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shaif Chowdhury, Mushfika Rahman, Greg Hamerly

**分类**: cs.CV, cs.LG

**发布日期**: 2025-12-14

**备注**: 12 pages

---

## 💡 一句话要点

**提出监督对比帧聚合方法，用于高效视频表征学习。**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视频表征学习` `监督对比学习` `帧聚合` `时间上下文` `卷积神经网络`

## 📋 核心要点

1. 现有视频表征学习方法计算成本高昂，难以有效利用时序全局信息。
2. 提出一种视频帧聚合策略，将多帧图像组合成单张图像，利用预训练CNN提取特征。
3. 设计监督对比学习目标，通过不同时间采样构建正样本，提升分类精度并减少过拟合。

## 📝 摘要（中文）

本文提出了一种用于视频表征学习的监督对比学习框架，该框架利用了时间上的全局上下文信息。我们引入了一种视频到图像的聚合策略，将每个视频的多个帧在空间上排列成单个输入图像。这种设计能够使用预训练的卷积神经网络骨干网络（如ResNet50），并避免了复杂视频Transformer模型带来的计算开销。然后，我们设计了一个对比学习目标，直接比较模型生成的成对投影。正样本对被定义为来自共享相同标签的视频的投影，而所有其他投影都被视为负样本。通过从同一底层视频进行不同的时间帧采样，创建同一视频的多个自然视图。这些帧级别的变化产生具有全局上下文的多样化正样本，并减少过拟合，而不是依赖于数据增强。在Penn Action和HMDB51数据集上的实验表明，所提出的方法在分类精度方面优于现有方法，同时需要的计算资源更少。所提出的监督对比帧聚合方法在监督和自监督设置中都能学习有效的视频表征，并支持基于视频的任务，如分类和字幕生成。该方法在Penn Action上实现了76%的分类精度，而ViViT的精度为43%，在HMDB51上实现了48%的精度，而ViViT的精度为37%。

## 🔬 方法详解

**问题定义**：现有的视频表征学习方法，特别是基于Transformer的模型，通常需要大量的计算资源，并且在捕捉视频中的全局时间上下文信息方面存在挑战。此外，过度依赖数据增强来生成正样本可能导致模型泛化能力下降。

**核心思路**：本文的核心思路是将视频帧聚合为单个图像，从而能够利用预训练的CNN模型提取特征，降低计算成本。同时，通过监督对比学习，将同一视频的不同时间采样作为正样本，鼓励模型学习具有全局时间上下文的视频表征。

**技术框架**：该方法主要包含以下几个阶段：1) 视频帧聚合：将视频中的多个帧按照一定的规则排列成一张图像。2) 特征提取：使用预训练的CNN（如ResNet50）提取聚合图像的特征。3) 投影：将提取的特征投影到低维空间。4) 对比学习：使用监督对比损失函数，将同一视频的不同时间采样作为正样本，不同视频的采样作为负样本，训练模型。

**关键创新**：该方法的主要创新在于：1) 提出了视频帧聚合策略，有效利用了预训练的CNN模型，降低了计算成本。2) 使用监督对比学习，通过不同的时间采样构建正样本，避免了过度依赖数据增强，提升了模型的泛化能力。3) 将时间全局上下文信息融入到对比学习框架中，提升了视频表征的质量。

**关键设计**：关键设计包括：1) 帧聚合策略：选择合适的帧数和排列方式，以保留尽可能多的时间信息。2) 对比损失函数：使用监督对比损失函数，鼓励模型学习区分不同类别的视频，并使同一视频的不同时间采样尽可能接近。3) 时间采样策略：采用不同的时间采样方式，生成多样化的正样本。

## 📊 实验亮点

该方法在Penn Action数据集上取得了76%的分类精度，相比ViViT的43%有显著提升。在HMDB51数据集上，该方法取得了48%的分类精度，而ViViT的精度为37%。实验结果表明，该方法在分类精度方面优于现有方法，同时需要的计算资源更少。

## 🎯 应用场景

该研究成果可应用于视频分类、视频检索、视频字幕生成等领域。通过学习高效的视频表征，可以提升这些任务的性能，并降低计算成本。该方法在智能监控、自动驾驶、视频内容分析等领域具有潜在的应用价值。

## 📄 摘要（原文）

> We propose a supervised contrastive learning framework for video representation learning that leverages temporally global context. We introduce a video to image aggregation strategy that spatially arranges multiple frames from each video into a single input image. This design enables the use of pre trained convolutional neural network backbones such as ResNet50 and avoids the computational overhead of complex video transformer models. We then design a contrastive learning objective that directly compares pairwise projections generated by the model. Positive pairs are defined as projections from videos sharing the same label while all other projections are treated as negatives. Multiple natural views of the same video are created using different temporal frame samplings from the same underlying video. Rather than relying on data augmentation these frame level variations produce diverse positive samples with global context and reduce overfitting. Experiments on the Penn Action and HMDB51 datasets demonstrate that the proposed method outperforms existing approaches in classification accuracy while requiring fewer computational resources. The proposed Supervised Contrastive Frame Aggregation method learns effective video representations in both supervised and self supervised settings and supports video based tasks such as classification and captioning. The method achieves seventy six percent classification accuracy on Penn Action compared to forty three percent achieved by ViVIT and forty eight percent accuracy on HMDB51 compared to thirty seven percent achieved by ViVIT.

