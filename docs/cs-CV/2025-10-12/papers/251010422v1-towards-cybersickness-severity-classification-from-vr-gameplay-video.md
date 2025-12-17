---
layout: default
title: Towards Cybersickness Severity Classification from VR Gameplay Videos Using Transfer Learning and Temporal Modeling
---

# Towards Cybersickness Severity Classification from VR Gameplay Videos Using Transfer Learning and Temporal Modeling

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.10422" target="_blank" class="toolbar-btn">arXiv: 2510.10422v1</a>
    <a href="https://arxiv.org/pdf/2510.10422.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.10422v1" 
            onclick="toggleFavorite(this, '2510.10422v1', 'Towards Cybersickness Severity Classification from VR Gameplay Videos Using Transfer Learning and Temporal Modeling')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jyotirmay Nag Setu, Kevin Desai, John Quarles

**分类**: cs.CV

**发布日期**: 2025-10-12

---

## 💡 一句话要点

**提出基于迁移学习和时序建模的VR游戏视频晕动症严重程度分类方法**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `虚拟现实` `晕动症` `迁移学习` `时序建模` `LSTM` `视频分析` `InceptionV3`

## 📋 核心要点

1. 现有VR晕动症预测方法主要依赖VR传感器数据，缺乏对游戏视频视觉信息的有效利用。
2. 利用迁移学习提取视频高级特征，结合LSTM网络建模时序动态，预测晕动症严重程度。
3. 实验结果表明，该方法在晕动症严重程度分类上达到68.4%的准确率，优于现有视频数据模型。

## 📝 摘要（中文）

随着虚拟现实(VR)技术的快速发展，其在医疗、教育和娱乐等领域的应用显著增长。然而，持续存在的晕动症问题，其症状类似于晕动病，仍然阻碍了VR的广泛接受。虽然最近的研究已经探索了利用来自集成VR传感器（如眼动和头部跟踪）数据的多模态深度学习方法，但对于使用基于视频的特征来预测晕动症的研究仍然有限。本研究通过使用迁移学习，利用在ImageNet数据集上预训练的InceptionV3模型从VR游戏视频中提取高级视觉特征来解决这一差距。然后，将这些特征传递给长短期记忆(LSTM)网络，以捕获VR体验的时序动态并预测晕动症的严重程度。我们的方法有效地利用了视频数据的时间序列性质，实现了68.4%的晕动症严重程度分类准确率。这超过了仅在视频数据上训练的现有模型的性能，为VR开发人员提供了一个评估和减轻虚拟环境中晕动症的实用工具。此外，这项工作为未来基于视频的时序建模研究奠定了基础，以提高VR应用中的用户舒适度。

## 🔬 方法详解

**问题定义**：现有方法在预测VR晕动症严重程度时，主要依赖于VR头显内置的传感器数据，如眼动追踪和头部运动数据。然而，游戏视频本身蕴含着丰富的视觉信息，例如场景切换的频率、运动幅度等，这些信息与晕动症的发生密切相关。现有方法未能充分利用这些视频数据，导致预测精度受限。

**核心思路**：本论文的核心思路是利用迁移学习，将预训练的图像识别模型（InceptionV3）应用于VR游戏视频帧，提取高级视觉特征。然后，利用LSTM网络对这些特征进行时序建模，捕捉VR体验过程中晕动症症状随时间变化的动态过程。通过结合视觉特征和时序信息，更准确地预测晕动症的严重程度。

**技术框架**：整体框架包含两个主要阶段：特征提取阶段和时序建模阶段。在特征提取阶段，使用在ImageNet数据集上预训练的InceptionV3模型提取VR游戏视频每一帧的视觉特征。在时序建模阶段，将提取的视觉特征序列输入到LSTM网络中，LSTM网络学习视频帧之间的时序依赖关系，最终输出晕动症严重程度的预测结果。

**关键创新**：本论文的关键创新在于将迁移学习和时序建模相结合，用于VR游戏视频的晕动症严重程度分类。与传统方法相比，该方法能够更有效地利用视频数据中的视觉信息和时序信息，从而提高预测精度。此外，该方法无需额外的VR传感器数据，仅依赖于游戏视频，具有更广泛的适用性。

**关键设计**：InceptionV3模型使用在ImageNet数据集上预训练的权重进行初始化，以加速收敛并提高特征提取能力。LSTM网络的隐藏层大小和层数需要根据数据集进行调整。损失函数采用交叉熵损失函数，优化器采用Adam优化器。在训练过程中，使用dropout技术防止过拟合。

## 📊 实验亮点

实验结果表明，该方法在VR游戏视频的晕动症严重程度分类任务上取得了68.4%的准确率。与仅使用视频数据训练的现有模型相比，该方法的性能显著提升。这表明迁移学习和时序建模能够有效地利用视频数据中的视觉信息和时序信息，从而提高晕动症预测的准确性。

## 🎯 应用场景

该研究成果可应用于VR游戏开发、VR内容评估和VR用户体验优化等领域。VR开发者可以利用该模型评估游戏或应用的晕动症风险，并进行相应的优化，从而提高用户舒适度。此外，该模型还可以用于个性化VR体验设计，根据用户的晕动症敏感度调整游戏难度或场景切换频率，提升用户体验。

## 📄 摘要（原文）

> With the rapid advancement of virtual reality (VR) technology, its adoption across domains such as healthcare, education, and entertainment has grown significantly. However, the persistent issue of cybersickness, marked by symptoms resembling motion sickness, continues to hinder widespread acceptance of VR. While recent research has explored multimodal deep learning approaches leveraging data from integrated VR sensors like eye and head tracking, there remains limited investigation into the use of video-based features for predicting cybersickness. In this study, we address this gap by utilizing transfer learning to extract high-level visual features from VR gameplay videos using the InceptionV3 model pretrained on the ImageNet dataset. These features are then passed to a Long Short-Term Memory (LSTM) network to capture the temporal dynamics of the VR experience and predict cybersickness severity over time. Our approach effectively leverages the time-series nature of video data, achieving a 68.4% classification accuracy for cybersickness severity. This surpasses the performance of existing models trained solely on video data, providing a practical tool for VR developers to evaluate and mitigate cybersickness in virtual environments. Furthermore, this work lays the foundation for future research on video-based temporal modeling for enhancing user comfort in VR applications.

