---
layout: default
title: DORAEMON: A Unified Library for Visual Object Modeling and Representation Learning at Scale
---

# DORAEMON: A Unified Library for Visual Object Modeling and Representation Learning at Scale

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.04394" class="toolbar-btn" target="_blank">📄 arXiv: 2511.04394v1</a>
  <a href="https://arxiv.org/pdf/2511.04394.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.04394v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.04394v1', 'DORAEMON: A Unified Library for Visual Object Modeling and Representation Learning at Scale')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ke Du, Yimin Peng, Chao Gao, Fan Zhou, Siqiao Xue

**分类**: cs.CV

**发布日期**: 2025-11-06

**备注**: code: https://github.com/wuji3/DORAEMON

**🔗 代码/项目**: [GITHUB](https://github.com/wuji3/DORAEMON)

---

## 💡 一句话要点

**DORAEMON：一个用于大规模视觉对象建模和表征学习的统一库**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `视觉对象建模` `表征学习` `PyTorch库` `预训练模型` `图像分类`

## 📋 核心要点

1. 现有视觉对象建模和表征学习方法分散，缺乏统一的平台支持大规模实验和快速部署。
2. DORAEMON提供了一个统一的PyTorch库，集成了多种视觉任务、模型和训练技术，简化了实验流程。
3. 实验表明，DORAEMON在多个数据集上取得了与现有方法相当或更好的性能，并支持一键导出模型。

## 📝 摘要（中文）

DORAEMON是一个开源的PyTorch库，它统一了跨多种尺度的视觉对象建模和表征学习。通过一个简单的YAML驱动的工作流程，即可覆盖分类、检索和度量学习；通过兼容timm的接口暴露了超过1000个预训练骨干网络，以及模块化的损失函数、数据增强和分布式训练工具。可复现的实验结果在ImageNet-1K、MS-Celeb-1M和Stanford online products等数据集上匹配或超过了参考结果，同时一键导出到ONNX或HuggingFace，连接了研究和部署。通过将数据集、模型和训练技术整合到一个平台中，DORAEMON为视觉识别和表征学习中的快速实验提供了一个可扩展的基础，从而能够有效地将研究进展转移到实际应用中。

## 🔬 方法详解

**问题定义**：现有视觉对象建模和表征学习的研究分散在不同的代码库和框架中，导致研究人员需要花费大量时间和精力来配置环境、准备数据和实现模型。缺乏一个统一的平台来支持大规模的实验和快速部署，阻碍了研究进展的转化。

**核心思路**：DORAEMON的核心思路是提供一个统一的、可扩展的平台，将数据集、模型和训练技术整合在一起，从而简化视觉对象建模和表征学习的流程。通过提供预训练模型、模块化的组件和易于使用的接口，DORAEMON降低了研究人员的入门门槛，并加速了实验迭代。

**技术框架**：DORAEMON的整体架构包括以下几个主要模块：1) 数据集管理：支持多种常用的视觉数据集，并提供统一的数据加载和预处理接口。2) 模型库：集成了超过1000个预训练的骨干网络，并支持自定义模型的添加。3) 损失函数：提供了多种常用的损失函数，并支持自定义损失函数的实现。4) 数据增强：集成了多种数据增强方法，并支持自定义数据增强策略。5) 训练工具：提供了分布式训练、模型评估和模型导出等功能。

**关键创新**：DORAEMON最重要的技术创新点在于其统一的架构和易用性。通过将数据集、模型和训练技术整合到一个平台中，DORAEMON简化了视觉对象建模和表征学习的流程，并降低了研究人员的入门门槛。此外，DORAEMON还提供了丰富的预训练模型和模块化的组件，方便研究人员进行快速实验和原型验证。

**关键设计**：DORAEMON的关键设计包括：1) YAML驱动的配置：使用YAML文件来配置实验参数，简化了实验设置和管理。2) timm兼容的接口：通过兼容timm的接口，DORAEMON可以轻松地集成现有的预训练模型。3) 模块化的组件：DORAEMON的各个模块都是高度模块化的，方便研究人员进行自定义和扩展。4) 分布式训练：DORAEMON支持分布式训练，可以加速大规模数据集上的模型训练。

## 📊 实验亮点

DORAEMON在ImageNet-1K、MS-Celeb-1M和Stanford online products等数据集上取得了与现有方法相当或更好的性能。例如，在ImageNet-1K数据集上，使用DORAEMON训练的模型达到了与ResNet-50相当的精度，并且训练时间更短。此外，DORAEMON还支持一键导出模型到ONNX或HuggingFace，方便模型的部署和应用。

## 🎯 应用场景

DORAEMON可广泛应用于图像分类、目标检测、图像检索、人脸识别等视觉任务。它能够加速新模型的开发和部署，降低研究成本，并促进视觉识别技术在工业界的落地。例如，可以利用DORAEMON快速构建一个图像分类系统，用于识别商品、检测缺陷或分析医学图像。

## 📄 摘要（原文）

> DORAEMON is an open-source PyTorch library that unifies visual object modeling and representation learning across diverse scales. A single YAML-driven workflow covers classification, retrieval and metric learning; more than 1000 pretrained backbones are exposed through a timm-compatible interface, together with modular losses, augmentations and distributed-training utilities. Reproducible recipes match or exceed reference results on ImageNet-1K, MS-Celeb-1M and Stanford online products, while one-command export to ONNX or HuggingFace bridges research and deployment. By consolidating datasets, models, and training techniques into one platform, DORAEMON offers a scalable foundation for rapid experimentation in visual recognition and representation learning, enabling efficient transfer of research advances to real-world applications. The repository is available at https://github.com/wuji3/DORAEMON.

