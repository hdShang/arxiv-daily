---
layout: default
title: Self-Supervised Event Representations: Towards Accurate, Real-Time Perception on SoC FPGAs
---

# Self-Supervised Event Representations: Towards Accurate, Real-Time Perception on SoC FPGAs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.07556" class="toolbar-btn" target="_blank">📄 arXiv: 2505.07556v1</a>
  <a href="https://arxiv.org/pdf/2505.07556.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.07556v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.07556v1', 'Self-Supervised Event Representations: Towards Accurate, Real-Time Perception on SoC FPGAs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Kamil Jeziorek, Tomasz Kryjak

**分类**: cs.CV

**发布日期**: 2025-05-12

**备注**: Presented at the Real-time Processing of Image, Depth and Video Information 2025 workshop and to be considered for publication is the SPIE Proceedings

**🔗 代码/项目**: [GITHUB](https://github.com/vision-agh/RecRepEvent)

---

## 💡 一句话要点

**提出自监督事件表示方法以解决事件数据处理挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `事件相机` `自监督学习` `GRU网络` `物体检测` `FPGA实现` `低功耗` `实时感知`

## 📋 核心要点

1. 现有方法在处理事件相机生成的稀疏、异步数据时，往往面临性能和时间保真度之间的权衡。
2. 本文提出的自监督事件表示方法（SSER）通过GRU网络实现事件时间戳和极性的精确编码，避免了时间离散化带来的信息损失。
3. 实验结果显示，SSER在多个数据集上超越了基于聚合的基线，提升了检测精度，并在FPGA上实现了低延迟和低功耗的硬件实现。

## 📝 摘要（中文）

事件相机相较于传统帧基传感器具有微秒级时间分辨率、在不同光照条件下的鲁棒性以及低功耗等显著优势。然而，如何有效处理其稀疏、异步的事件流仍然是一个挑战。现有方法主要分为两类：直接处理事件数据的神经模型和将事件转换为密集表示的手工聚合函数。本文提出了一种新颖的自监督事件表示方法（SSER），利用门控递归单元（GRU）网络实现事件时间戳和极性的逐像素精确编码，而无需时间离散化。实验结果表明，SSER在Gen1和1 Mpx物体检测数据集上分别提高了2.4%的mAP和0.6%。此外，本文首次在系统级芯片FPGA上实现了递归表示，达到了亚微秒延迟和1-2W的功耗，适用于实时、低功耗应用。

## 🔬 方法详解

**问题定义**：本文旨在解决事件相机生成的稀疏、异步事件流的有效处理问题。现有方法在性能和时间保真度之间存在妥协，导致无法充分利用事件相机的优势。

**核心思路**：论文提出的自监督事件表示方法（SSER）通过使用GRU网络，能够逐像素精确编码事件的时间戳和极性，而不需要进行时间离散化，从而保持了事件数据的高保真度。

**技术框架**：SSER的整体架构包括输入层（接收事件数据）、GRU网络（进行自监督训练以优化编码）、输出层（生成事件表示）。该方法支持异步生成事件表示，确保与高吞吐量传感器的兼容性。

**关键创新**：SSER的主要创新在于其自监督训练机制和GRU网络的应用，使得事件时间编码的保真度显著提高。这与传统的聚合方法形成鲜明对比，后者往往牺牲了时间信息的准确性。

**关键设计**：在设计中，GRU网络的参数设置经过精心调整，以最大化事件时间编码的保真度。损失函数采用自监督学习策略，确保网络能够有效学习事件数据的特征。

## 📊 实验亮点

实验结果表明，SSER在Gen1和1 Mpx物体检测数据集上分别提高了2.4%的mAP和0.6%。此外，首次在FPGA上实现的递归表示达到了亚微秒延迟和1-2W的功耗，展示了其在实时应用中的优势。

## 🎯 应用场景

该研究的潜在应用领域包括自动驾驶、机器人视觉、监控系统等需要高时间分辨率和低功耗的实时感知任务。通过提高事件数据处理的准确性和效率，SSER能够推动这些领域的技术进步，促进更智能的系统开发。

## 📄 摘要（原文）

> Event cameras offer significant advantages over traditional frame-based sensors. These include microsecond temporal resolution, robustness under varying lighting conditions and low power consumption. Nevertheless, the effective processing of their sparse, asynchronous event streams remains challenging. Existing approaches to this problem can be categorised into two distinct groups. The first group involves the direct processing of event data with neural models, such as Spiking Neural Networks or Graph Convolutional Neural Networks. However, this approach is often accompanied by a compromise in terms of qualitative performance. The second group involves the conversion of events into dense representations with handcrafted aggregation functions, which can boost accuracy at the cost of temporal fidelity. This paper introduces a novel Self-Supervised Event Representation (SSER) method leveraging Gated Recurrent Unit (GRU) networks to achieve precise per-pixel encoding of event timestamps and polarities without temporal discretisation. The recurrent layers are trained in a self-supervised manner to maximise the fidelity of event-time encoding. The inference is performed with event representations generated asynchronously, thus ensuring compatibility with high-throughput sensors. The experimental validation demonstrates that SSER outperforms aggregation-based baselines, achieving improvements of 2.4% mAP and 0.6% on the Gen1 and 1 Mpx object detection datasets. Furthermore, the paper presents the first hardware implementation of recurrent representation for event data on a System-on-Chip FPGA, achieving sub-microsecond latency and power consumption between 1-2 W, suitable for real-time, power-efficient applications. Code is available at https://github.com/vision-agh/RecRepEvent.

