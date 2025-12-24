---
layout: default
title: "PPTP: Performance-Guided Physiological Signal-Based Trust Prediction in Human-Robot Collaboration"
---

# PPTP: Performance-Guided Physiological Signal-Based Trust Prediction in Human-Robot Collaboration

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.16677" class="toolbar-btn" target="_blank">📄 arXiv: 2506.16677v1</a>
  <a href="https://arxiv.org/pdf/2506.16677.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.16677v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.16677v1', 'PPTP: Performance-Guided Physiological Signal-Based Trust Prediction in Human-Robot Collaboration')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hao Guo, Wei Fan, Shaohui Liu, Feng Jiang, Chunzhi Yi

**分类**: cs.HC, cs.RO

**发布日期**: 2025-06-20

---

## 💡 一句话要点

**提出PPTP框架以解决人机协作中的信任预测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `信任预测` `人机协作` `生理信号` `多模态融合` `性能评估` `建筑场景` `机器学习`

## 📋 核心要点

1. 信任预测在现有的人机协作研究中面临挑战，尤其是在动态和复杂的环境中，传统方法难以准确评估信任水平。
2. 本文提出的PPTP框架通过整合生理信号与协作性能评估，利用生理反应的标准化特性来补偿个体差异，从而提高信任预测的准确性。
3. 实验结果显示，PPTP在三级信任分类中准确率超过81%，在七级分类中达到74.3%，显著优于现有最佳基线方法，验证了其有效性。

## 📝 摘要（中文）

信任预测是人机协作中的关键问题，尤其在建筑场景中，适当的信任校准对安全和效率至关重要。本文提出了一种基于生理信号的性能引导信任预测框架（PPTP），旨在改善信任评估。我们设计了一个包含三种难度级别的人机协作场景，以诱导不同的信任状态。该方法结合了同步的多模态生理信号（心电图、皮肤电反应和肌电图）与协作性能评估，以预测人类的信任水平。通过广泛的实验，验证了我们跨模态融合方法在显著提高信任分类性能方面的有效性。我们的模型在三级信任分类中实现了超过81%的准确率，较最佳基线方法提升6.7%，并在高分辨率七级分类中达到74.3%的准确率，这在信任预测研究中尚属首次。

## 🔬 方法详解

**问题定义**：本文旨在解决人机协作中的信任预测问题，现有方法在动态环境中难以准确评估信任水平，且个体生理反应存在较大差异。

**核心思路**：PPTP框架通过结合多模态生理信号（如ECG、GSR、EMG）与协作性能评估，利用后者的标准化特性来指导生理信号的处理，从而提高信任预测的准确性。

**技术框架**：该框架包括信号采集、信号处理、性能评估和信任预测四个主要模块。首先采集参与者的生理信号，同时记录协作任务的性能数据，然后通过融合算法进行信任水平的预测。

**关键创新**：本研究的创新点在于将生理信号处理与协作性能评估相结合，利用性能信息作为引导，显著提升了信任分类的准确性，尤其是在高分辨率分类任务中。

**关键设计**：在模型设计中，采用了多模态信号融合技术，设置了适当的损失函数以优化信任预测的准确性，并通过实验验证了不同参数设置对模型性能的影响。

## 📊 实验亮点

实验结果表明，PPTP框架在三级信任分类中实现了超过81%的准确率，较最佳基线方法提升6.7%。在高分辨率的七级分类中，模型达到74.3%的准确率，标志着信任预测研究的新进展。

## 🎯 应用场景

该研究的潜在应用领域包括智能建筑、自动化施工和人机协作机器人等场景。通过提高信任预测的准确性，可以有效提升人机协作的安全性和效率，具有重要的实际价值和广泛的应用前景。

## 📄 摘要（原文）

> Trust prediction is a key issue in human-robot collaboration, especially in construction scenarios where maintaining appropriate trust calibration is critical for safety and efficiency. This paper introduces the Performance-guided Physiological signal-based Trust Prediction (PPTP), a novel framework designed to improve trust assessment. We designed a human-robot construction scenario with three difficulty levels to induce different trust states. Our approach integrates synchronized multimodal physiological signals (ECG, GSR, and EMG) with collaboration performance evaluation to predict human trust levels. Individual physiological signals are processed using collaboration performance information as guiding cues, leveraging the standardized nature of collaboration performance to compensate for individual variations in physiological responses. Extensive experiments demonstrate the efficacy of our cross-modality fusion method in significantly improving trust classification performance. Our model achieves over 81% accuracy in three-level trust classification, outperforming the best baseline method by 6.7%, and notably reaches 74.3% accuracy in high-resolution seven-level classification, which is a first in trust prediction research. Ablation experiments further validate the superiority of physiological signal processing guided by collaboration performance assessment.

