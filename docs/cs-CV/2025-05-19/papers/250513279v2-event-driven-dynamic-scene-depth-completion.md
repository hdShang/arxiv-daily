---
layout: default
title: Event-Driven Dynamic Scene Depth Completion
---

# Event-Driven Dynamic Scene Depth Completion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13279" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13279v2</a>
  <a href="https://arxiv.org/pdf/2505.13279.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13279v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13279v2', 'Event-Driven Dynamic Scene Depth Completion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhiqiang Yan, Jianhao Jiao, Zhengxue Wang, Gim Hee Lee

**分类**: cs.CV

**发布日期**: 2025-05-19 (更新: 2025-05-20)

**备注**: 9 pages

---

## 💡 一句话要点

**提出EventDC以解决动态场景深度补全问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `深度补全` `动态场景` `事件相机` `卷积神经网络` `运动感知` `深度学习` `计算机视觉`

## 📋 核心要点

1. 动态场景中的深度补全面临快速运动导致的输入模态质量下降，传统方法难以有效处理。
2. 提出EventDC框架，通过事件调制对齐和局部深度过滤，利用事件相机的高时间分辨率进行深度补全。
3. 在新建立的基准测试上，EventDC展示了显著的性能提升，证明了其在动态场景中的有效性。

## 📝 摘要（中文）

动态场景中的深度补全面临着快速自我运动和物体运动带来的重大挑战，这会严重影响RGB图像和LiDAR测量的质量。传统的RGB-D传感器在这种情况下往往难以精确对齐并捕获可靠的深度信息。与此相比，事件相机因其高时间分辨率和对像素级运动的敏感性，提供了在动态环境中特别有益的补充线索。为此，我们提出了EventDC，这是第一个事件驱动的深度补全框架，包含事件调制对齐（EMA）和局部深度过滤（LDF）两个关键组件。实验结果表明，EventDC在深度补全任务中表现优越。

## 🔬 方法详解

**问题定义**：本论文旨在解决动态场景中的深度补全问题，现有方法在快速自我运动和物体运动下难以保持深度信息的准确性，导致RGB-D传感器的对齐和深度捕获效果不佳。

**核心思路**：提出EventDC框架，利用事件相机的高时间分辨率和对运动的敏感性，通过事件调制对齐和局部深度过滤来改善深度补全的质量。

**技术框架**：EventDC框架主要由两个模块组成：事件调制对齐（EMA）和局部深度过滤（LDF）。EMA在编码器中利用事件信息调制RGB-D特征的采样位置，而LDF在解码器中通过学习运动感知的掩码来优化移动物体周围的深度估计。

**关键创新**：EventDC的创新在于首次将事件驱动的机制应用于深度补全任务，特别是通过动态调整卷积操作的偏移量和权重来适应运动敏感的事件流，从而实现更好的对齐和融合。

**关键设计**：在损失函数设计上，EventDC引入了两个损失项，以进一步促进全局对齐和局部深度恢复，确保深度估计的准确性和稳定性。

## 📊 实验亮点

在新建立的事件基础深度补全基准测试上，EventDC展示了显著的性能提升，尤其是在动态场景中，相较于传统方法，深度估计的准确性提高了XX%，并在多个数据集上均表现出优越的鲁棒性和精确性。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人导航和增强现实等动态场景下的深度感知任务。通过提高动态环境中的深度补全精度，EventDC能够显著提升相关技术的可靠性和实用性，推动智能系统在复杂环境中的应用。未来，该框架有望在更多实时处理和高精度需求的场景中发挥重要作用。

## 📄 摘要（原文）

> Depth completion in dynamic scenes poses significant challenges due to rapid ego-motion and object motion, which can severely degrade the quality of input modalities such as RGB images and LiDAR measurements. Conventional RGB-D sensors often struggle to align precisely and capture reliable depth under such conditions. In contrast, event cameras with their high temporal resolution and sensitivity to motion at the pixel level provide complementary cues that are %particularly beneficial in dynamic environments.To this end, we propose EventDC, the first event-driven depth completion framework. It consists of two key components: Event-Modulated Alignment (EMA) and Local Depth Filtering (LDF). Both modules adaptively learn the two fundamental components of convolution operations: offsets and weights conditioned on motion-sensitive event streams. In the encoder, EMA leverages events to modulate the sampling positions of RGB-D features to achieve pixel redistribution for improved alignment and fusion. In the decoder, LDF refines depth estimations around moving objects by learning motion-aware masks from events. Additionally, EventDC incorporates two loss terms to further benefit global alignment and enhance local depth recovery. Moreover, we establish the first benchmark for event-based depth completion comprising one real-world and two synthetic datasets to facilitate future research. Extensive experiments on this benchmark demonstrate the superiority of our EventDC.

