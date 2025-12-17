---
layout: default
title: Generalizing WiFi Gesture Recognition via Large-Model-Aware Semantic Distillation and Alignment
---

# Generalizing WiFi Gesture Recognition via Large-Model-Aware Semantic Distillation and Alignment

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.13390" target="_blank" class="toolbar-btn">arXiv: 2510.13390v1</a>
    <a href="https://arxiv.org/pdf/2510.13390.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.13390v1" 
            onclick="toggleFavorite(this, '2510.13390v1', 'Generalizing WiFi Gesture Recognition via Large-Model-Aware Semantic Distillation and Alignment')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Feng-Qi Cui, Yu-Tong Guo, Tianyue Zheng, Jinyang Huang

**分类**: cs.CV

**发布日期**: 2025-10-15

**备注**: Accepted by IEEE ICPADS 2025

---

## 💡 一句话要点

**提出GLSDA框架，利用大模型语义知识提升WiFi手势识别泛化能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `WiFi手势识别` `大模型` `语义蒸馏` `跨域泛化` `AIoT` `信道状态信息` `知识迁移`

## 📋 核心要点

1. 现有WiFi手势识别方法泛化性差，缺乏高层语义抽象，难以应对信道状态信息（CSI）的域敏感性。
2. GLSDA框架利用预训练大模型的语义先验，通过语义蒸馏和对齐，增强手势表征学习能力，提升泛化性。
3. 实验表明，GLSDA在Widar3.0数据集上超越现有方法，显著降低模型大小和推理延迟，提升了域内和跨域识别性能。

## 📝 摘要（中文）

本文提出了一种名为GLSDA（Large-Model-Aware Semantic Distillation and Alignment）的通用框架，旨在利用预训练大模型的语义先验知识，增强WiFi手势识别在域内和跨域场景下的表征学习能力。该框架首先设计了一个双路CSI编码流程，通过CSI-Ratio相位序列和多普勒频谱捕获手势的几何和动态模式。然后，这些表征被输入到多尺度语义编码器中，该编码器学习鲁棒的时间嵌入，并通过跨模态注意力机制将其与手势语义对齐。为了进一步增强类别区分度，引入了语义感知的软监督方案，该方案编码类间相关性并减少标签模糊性，特别是对于语义相似的手势。最后，开发了一种鲁棒的双重蒸馏策略，将对齐的模型压缩成轻量级的学生网络，联合从教师模型中蒸馏中间特征和语义信息软标签。在Widar3.0基准上的大量实验表明，GLSDA在域内和跨域手势识别任务中始终优于最先进的方法，同时显著降低了模型大小和推理延迟。该方法为实际AIoT应用中基于RF的通用手势界面提供了一种可扩展且可部署的解决方案。

## 🔬 方法详解

**问题定义**：现有基于WiFi的手势识别方法，由于信道状态信息（CSI）的域敏感性以及缺乏高层语义抽象，导致泛化能力受限，难以在不同环境和用户之间推广。尤其是在跨域场景下，模型性能会显著下降。此外，现有方法通常忽略了手势之间的语义关系，容易混淆语义相似的手势。

**核心思路**：本文的核心思路是利用预训练大模型中蕴含的丰富语义知识，指导WiFi手势识别模型的训练，从而提升模型的泛化能力和语义表达能力。通过语义蒸馏和对齐，将大模型的语义先验知识迁移到轻量级的WiFi手势识别模型中，使其能够更好地理解和区分不同的手势。

**技术框架**：GLSDA框架主要包含以下几个模块：1) 双路CSI编码：分别使用CSI-Ratio相位序列和多普勒频谱提取手势的几何和动态特征。2) 多尺度语义编码器：学习鲁棒的时间嵌入，并通过跨模态注意力机制将CSI特征与手势语义对齐。3) 语义感知的软监督：编码类间相关性，减少标签模糊性。4) 鲁棒的双重蒸馏：将对齐的模型压缩成轻量级学生网络，同时蒸馏中间特征和语义信息软标签。

**关键创新**：该方法最重要的创新点在于利用预训练大模型的语义先验知识来指导WiFi手势识别模型的训练。与传统的监督学习方法相比，GLSDA能够更好地利用手势之间的语义关系，提升模型的泛化能力和鲁棒性。此外，双重蒸馏策略能够有效地将大模型的知识迁移到小模型中，实现模型压缩和加速。

**关键设计**：在双路CSI编码中，CSI-Ratio相位序列和多普勒频谱分别捕捉手势的几何和动态特征，互为补充。多尺度语义编码器采用多层Transformer结构，能够学习不同尺度的特征表示。语义感知的软监督通过计算类间相似度矩阵，生成软标签，指导模型学习类间关系。双重蒸馏策略同时蒸馏中间特征和软标签，保证知识迁移的完整性。损失函数包括交叉熵损失、KL散度损失和均方误差损失，分别用于监督分类、软标签蒸馏和特征蒸馏。

## 📊 实验亮点

实验结果表明，GLSDA在Widar3.0数据集上取得了显著的性能提升。在域内手势识别任务中，GLSDA的准确率超过了现有最佳方法。在跨域手势识别任务中，GLSDA的性能提升更为明显，表明其具有更强的泛化能力。此外，GLSDA通过模型蒸馏，显著降低了模型大小和推理延迟，使其更易于部署在资源受限的设备上。

## 🎯 应用场景

该研究成果可广泛应用于智能家居、智能安防、人机交互等AIoT场景。例如，用户可以通过WiFi手势控制智能家居设备，无需接触任何物理界面，实现非接触式交互。此外，该技术还可以用于老年人或残疾人的辅助生活，通过手势识别监测他们的健康状况和行为模式。未来，该技术有望与虚拟现实、增强现实等技术结合，创造更加沉浸式和自然的交互体验。

## 📄 摘要（原文）

> WiFi-based gesture recognition has emerged as a promising RF sensing paradigm for enabling non-contact and privacy-preserving human-computer interaction in AIoT environments. However, existing methods often suffer from limited generalization and semantic expressiveness due to the domain-sensitive nature of Channel State Information and the lack of high-level gesture abstraction. To address these challenges, we propose a novel generalization framework, termed Large-Model-Aware Semantic Distillation and Alignment (GLSDA), which leverages the semantic prior of pre-trained large foundation models to enhance gesture representation learning in both in-domain and cross-domain scenarios. Specifically, we first design a dual-path CSI encoding pipeline that captures geometric and dynamic gesture patterns via CSI-Ratio phase sequences and Doppler spectrograms. These representations are then fed into a Multiscale Semantic Encoder, which learns robust temporal embeddings and aligns them with gesture semantics through cross-modal attention mechanisms. To further enhance category discrimination, we introduce a Semantic-Aware Soft Supervision scheme that encodes inter-class correlations and reduces label ambiguity, especially for semantically similar gestures. Finally, we develop a Robust Dual-Distillation strategy to compress the aligned model into a lightweight student network, jointly distilling intermediate features and semantic-informed soft labels from the teacher model. Extensive experiments on the Widar3.0 benchmark show that GLSDA consistently outperforms state-of-the-art methods in both in-domain and cross-domain gesture recognition tasks, while significantly reducing model size and inference latency. Our method offers a scalable and deployable solution for generalized RF-based gesture interfaces in real-world AIoT applications.

