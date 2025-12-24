---
layout: default
title: "FOCUS: Frequency-Optimized Conditioning of DiffUSion Models for mitigating catastrophic forgetting during Test-Time Adaptation"
---

# FOCUS: Frequency-Optimized Conditioning of DiffUSion Models for mitigating catastrophic forgetting during Test-Time Adaptation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.14437" class="toolbar-btn" target="_blank">📄 arXiv: 2508.14437v1</a>
  <a href="https://arxiv.org/pdf/2508.14437.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.14437v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.14437v1', 'FOCUS: Frequency-Optimized Conditioning of DiffUSion Models for mitigating catastrophic forgetting during Test-Time Adaptation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Gabriel Tjio, Jie Zhang, Xulei Yang, Yun Xing, Nhat Chung, Xiaofeng Cao, Ivor W. Tsang, Chee Keong Kwoh, Qing Guo

**分类**: cs.CV

**发布日期**: 2025-08-20

---

## 💡 一句话要点

**提出FOCUS以解决测试时适应中的灾难性遗忘问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `频率优化` `测试时适应` `灾难性遗忘` `语义分割` `深度估计` `数据增强` `扩散模型`

## 📋 核心要点

1. 现有模型在适应领域变化时容易遗忘任务相关知识，导致性能下降。
2. FOCUS通过频率优化的条件方法，利用学习到的空间自适应频率先验来保留语义信息。
3. 在15种腐蚀类型和三个数据集上，FOCUS实现了最先进的性能，并增强了现有模型适应方法的效果。

## 📝 摘要（中文）

测试时适应使模型能够适应不断变化的领域。然而，保持知识的完整性与适应领域变化之间的平衡仍然是模型适应方法面临的挑战。为了解决这一问题，本文提出了FOCUS，一种基于频率的条件方法，旨在通过扩散驱动的输入适应框架来保留任务相关的语义信息。FOCUS利用轻量级的Y形频率预测网络（Y-FPN）来分离噪声图像中的高频和低频信息，从而降低计算成本。通过在15种腐蚀类型和三个数据集上进行实验，FOCUS在语义分割和单目深度估计任务中实现了最先进的平均性能，并有效减轻了灾难性遗忘。

## 🔬 方法详解

**问题定义**：本文旨在解决测试时适应过程中模型在适应新领域时可能出现的灾难性遗忘问题。现有方法在适应领域变化时，往往会导致模型遗忘之前学到的任务相关知识，影响整体性能。

**核心思路**：FOCUS提出了一种基于频率的条件方法，通过扩散驱动的输入适应框架，利用频率先验来保留任务相关的语义信息，从而在适应新领域时减少知识遗忘。

**技术框架**：FOCUS的整体架构包括一个轻量级的Y形频率预测网络（Y-FPN），该网络负责从噪声图像中分离高频和低频信息。通过FrequencyMix数据增强方法，Y-FPN在多种频率带上对图像进行扰动，以提高模型的鲁棒性。

**关键创新**：FOCUS的主要创新在于引入频率优化的条件方法，通过学习的频率先验来指导扩散过程中的反向步骤，从而有效保留任务相关的语义信息。这一方法与传统的模型适应方法相比，显著降低了灾难性遗忘的风险。

**关键设计**：FOCUS采用了Y-FPN网络结构，设计了FrequencyMix作为数据增强策略，确保在不同频率带上对图像进行有效扰动。此外，损失函数的设计也考虑了任务相关信息的保留，进一步增强了模型的适应能力。

## 📊 实验亮点

在实验中，FOCUS在15种不同的图像腐蚀类型和三个数据集上表现出色，达到了最先进的平均性能。与现有模型适应方法相比，FOCUS显著降低了灾难性遗忘的发生，展示了其在实际应用中的有效性和优势。

## 🎯 应用场景

FOCUS的研究成果在多个领域具有广泛的应用潜力，尤其是在计算机视觉任务中，如语义分割和深度估计。随着技术的进步，FOCUS可以帮助模型在动态环境中保持高效的适应能力，减少知识遗忘，从而提升自动驾驶、机器人视觉等领域的智能化水平。

## 📄 摘要（原文）

> Test-time adaptation enables models to adapt to evolving domains. However, balancing the tradeoff between preserving knowledge and adapting to domain shifts remains challenging for model adaptation methods, since adapting to domain shifts can induce forgetting of task-relevant knowledge. To address this problem, we propose FOCUS, a novel frequency-based conditioning approach within a diffusion-driven input-adaptation framework. Utilising learned, spatially adaptive frequency priors, our approach conditions the reverse steps during diffusion-driven denoising to preserve task-relevant semantic information for dense prediction.
>   FOCUS leverages a trained, lightweight, Y-shaped Frequency Prediction Network (Y-FPN) that disentangles high and low frequency information from noisy images. This minimizes the computational costs involved in implementing our approach in a diffusion-driven framework. We train Y-FPN with FrequencyMix, a novel data augmentation method that perturbs the images across diverse frequency bands, which improves the robustness of our approach to diverse corruptions.
>   We demonstrate the effectiveness of FOCUS for semantic segmentation and monocular depth estimation across 15 corruption types and three datasets, achieving state-of-the-art averaged performance. In addition to improving standalone performance, FOCUS complements existing model adaptation methods since we can derive pseudo labels from FOCUS-denoised images for additional supervision. Even under limited, intermittent supervision with the pseudo labels derived from the FOCUS denoised images, we show that FOCUS mitigates catastrophic forgetting for recent model adaptation methods.

