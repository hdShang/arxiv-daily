---
layout: default
title: OmniFD: A Unified Model for Versatile Face Forgery Detection
---

# OmniFD: A Unified Model for Versatile Face Forgery Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.01128" class="toolbar-btn" target="_blank">📄 arXiv: 2512.01128v1</a>
  <a href="https://arxiv.org/pdf/2512.01128.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.01128v1" onclick="toggleFavorite(this, '2512.01128v1', 'OmniFD: A Unified Model for Versatile Face Forgery Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Haotian Liu, Haoyu Chen, Chenhui Pan, You Hu, Guoying Zhao, Xiaobai Li

**分类**: cs.CV

**发布日期**: 2025-11-30

**🔗 代码/项目**: [GITHUB](https://github.com/haotianll/OmniFD)

---

## 💡 一句话要点

**OmniFD：用于多功能人脸伪造检测的统一模型，提升效率和泛化性**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `人脸伪造检测` `多任务学习` `Swin Transformer` `跨任务交互` `时空特征提取`

## 📋 核心要点

1. 现有的人脸伪造检测方法通常采用特定任务的模型，导致计算冗余，忽略了相关任务之间的潜在关联。
2. OmniFD提出一个统一的框架，使用单个模型联合处理图像和视频分类、空间定位和时间定位四项任务。
3. 实验表明，OmniFD优于特定任务的模型，通过多任务学习捕获通用表示，并减少了模型参数和训练时间。

## 📝 摘要（中文）

本文提出OmniFD，一个统一的框架，用于联合解决四项核心人脸伪造检测任务，包括图像和视频分类、空间定位和时间定位。该架构包含三个主要组件：共享的Swin Transformer编码器，用于从图像和视频输入中提取统一的4D时空表示；一个具有可学习查询的跨任务交互模块，通过基于注意力的推理动态捕获任务间的依赖关系；以及轻量级的解码头，将精细化的表示转换为所有FFD任务的相应预测。大量实验表明，OmniFD优于特定任务的模型。其统一设计利用多任务学习来捕获跨任务的通用表示，尤其能够实现细粒度的知识迁移，从而促进其他任务。例如，当包含图像数据时，视频分类准确率提高了4.63%。通过在一个框架内统一图像、视频和四个任务，OmniFD在各种基准测试中实现了卓越的性能，同时具有高效率和可扩展性，例如，减少了63%的模型参数和50%的训练时间。它为实际应用中全面的人脸伪造检测建立了一个实用且可推广的解决方案。

## 🔬 方法详解

**问题定义**：现有的人脸伪造检测方法通常针对特定任务设计独立的模型，例如图像分类、视频分类、篡改区域定位和篡改时间段定位。这种方式存在计算冗余，并且忽略了不同任务之间的潜在关联性，例如图像分类的知识可以帮助视频分类，空间定位可以辅助时间定位。因此，如何设计一个统一的模型，同时高效地完成多项人脸伪造检测任务是一个挑战。

**核心思路**：OmniFD的核心思路是利用一个共享的骨干网络提取通用的时空特征，并通过跨任务交互模块学习不同任务之间的依赖关系，最后使用轻量级的解码头完成特定任务的预测。这种设计可以避免重复计算，并促进知识迁移，从而提高整体性能。

**技术框架**：OmniFD的整体架构包含三个主要模块：1) 共享的Swin Transformer编码器：用于从图像和视频输入中提取统一的4D时空表示。2) 跨任务交互模块：使用可学习的查询向量，通过注意力机制动态地捕获不同任务之间的依赖关系。3) 轻量级的解码头：将精细化的表示转换为对应任务的预测结果，例如分类概率、像素级别的篡改概率图或时间段的置信度得分。

**关键创新**：OmniFD最重要的创新在于其统一的框架设计，它将图像和视频分类、空间定位和时间定位四个任务整合到一个模型中。通过共享的特征提取器和跨任务交互模块，模型可以学习到更通用的表示，并实现知识迁移。这与以往的特定任务模型形成了鲜明对比，提高了效率和泛化能力。

**关键设计**：跨任务交互模块是关键设计之一。它使用可学习的查询向量来表示每个任务，并通过注意力机制计算不同任务之间的相关性。Swin Transformer作为骨干网络，能够有效地提取时空特征。损失函数方面，针对不同的任务采用不同的损失函数，例如交叉熵损失用于分类任务，二元交叉熵损失用于像素级别的定位任务。

## 📊 实验亮点

OmniFD在多个基准数据集上取得了显著的性能提升。例如，在视频分类任务中，通过引入图像数据，准确率提高了4.63%。此外，OmniFD还显著降低了模型参数量和训练时间，分别减少了63%和50%。这些结果表明，OmniFD在效率和性能方面都优于传统的特定任务模型。

## 🎯 应用场景

OmniFD可应用于各种安全相关的场景，例如社交媒体平台的内容审核、视频监控系统中的异常检测、以及金融领域的身份验证。通过检测人脸伪造，可以有效防止虚假信息的传播、欺诈行为的发生，维护社会安全和稳定。未来，该技术可以进一步扩展到其他类型的媒体内容，例如音频和文本，以实现更全面的伪造检测。

## 📄 摘要（原文）

> Face forgery detection encompasses multiple critical tasks, including identifying forged images and videos and localizing manipulated regions and temporal segments. Current approaches typically employ task-specific models with independent architectures, leading to computational redundancy and ignoring potential correlations across related tasks. We introduce OmniFD, a unified framework that jointly addresses four core face forgery detection tasks within a single model, i.e., image and video classification, spatial localization, and temporal localization. Our architecture consists of three principal components: (1) a shared Swin Transformer encoder that extracts unified 4D spatiotemporal representations from both images and video inputs, (2) a cross-task interaction module with learnable queries that dynamically captures inter-task dependencies through attention-based reasoning, and (3) lightweight decoding heads that transform refined representations into corresponding predictions for all FFD tasks. Extensive experiments demonstrate OmniFD's advantage over task-specific models. Its unified design leverages multi-task learning to capture generalized representations across tasks, especially enabling fine-grained knowledge transfer that facilitates other tasks. For example, video classification accuracy improves by 4.63% when image data are incorporated. Furthermore, by unifying images, videos and the four tasks within one framework, OmniFD achieves superior performance across diverse benchmarks with high efficiency and scalability, e.g., reducing 63% model parameters and 50% training time. It establishes a practical and generalizable solution for comprehensive face forgery detection in real-world applications. The source code is made available at https://github.com/haotianll/OmniFD.

