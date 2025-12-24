---
layout: default
title: "DVS-PedX: Synthetic-and-Real Event-Based Pedestrian Dataset"
---

# DVS-PedX: Synthetic-and-Real Event-Based Pedestrian Dataset

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04117" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04117v1</a>
  <a href="https://arxiv.org/pdf/2509.04117.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04117v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04117v1', 'DVS-PedX: Synthetic-and-Real Event-Based Pedestrian Dataset')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mustafa Sakhai, Kaung Sithu, Min Khant Soe Oke, Maciej Wielgosz

**分类**: cs.CV

**发布日期**: 2025-09-04

**备注**: 12 pages, 8 figures, 3 tables; dataset descriptor paper introducing DVS-PedX (synthetic-and-real event-based pedestrian dataset with baselines) External URL: https://doi.org/10.5281/zenodo.17030898

---

## 💡 一句话要点

**DVS-PedX：用于事件相机行人检测与意图分析的合成与真实数据集**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `事件相机` `行人检测` `意图分析` `神经形态` `合成数据` `真实数据` `领域自适应`

## 📋 核心要点

1. 现有行人检测方法在低延迟、高动态范围和运动鲁棒性方面存在挑战，事件相机技术为此提供了新的解决方案。
2. DVS-PedX数据集通过合成数据和真实数据结合的方式，为事件相机在行人检测和意图分析任务上提供了训练和评估资源。
3. 基线脉冲神经网络实验揭示了合成数据与真实数据之间的差距，表明需要进一步研究领域自适应方法。

## 📝 摘要（中文）

DVS-PedX（动态视觉传感器行人探索）是一个神经形态数据集，专为行人检测和横穿意图分析而设计，适用于正常和恶劣天气条件。该数据集包含两个互补来源：（1）在CARLA模拟器中生成的合成事件流，用于控制“接近-横穿”场景，并具有不同的天气和光照条件；（2）使用v2e工具将真实世界的JAAD行车记录仪视频转换为事件流，保留了自然行为和背景。每个序列包括配对的RGB帧、每帧DVS“事件帧”（33毫秒累积）和帧级标签（横穿与不横穿）。我们还提供原始的AEDAT 2.0/AEDAT 4.0事件文件和AVI DVS视频文件以及元数据，以便灵活地重新处理。使用SpikingJelly的基线脉冲神经网络（SNN）展示了数据集的可用性，并揭示了sim-to-real的差距，从而激发了领域自适应和多模态融合。DVS-PedX旨在加速基于事件的行人安全、意图预测和神经形态感知方面的研究。

## 🔬 方法详解

**问题定义**：论文旨在解决基于事件相机的行人检测和横穿意图分析问题。现有方法在处理低延迟、高动态范围和快速运动场景时面临挑战，缺乏专门针对事件相机的行人数据集。

**核心思路**：论文的核心思路是构建一个包含合成数据和真实数据的混合数据集，以弥补真实事件数据稀缺的问题。合成数据可以提供大量的标注数据，而真实数据可以保证模型的泛化能力。

**技术框架**：DVS-PedX数据集包含两个主要部分：(1) 使用CARLA模拟器生成的合成事件流，模拟各种天气和光照条件下的行人接近和横穿场景；(2) 使用v2e工具将真实世界的JAAD行车记录仪视频转换为事件流。数据集提供配对的RGB帧、每帧DVS事件帧、帧级标签以及原始事件数据文件。

**关键创新**：该数据集的关键创新在于结合了合成数据和真实数据，并提供了多种数据格式，方便研究人员进行不同的实验和算法开发。此外，数据集还提供了行人横穿意图的标注，为相关研究提供了支持。

**关键设计**：合成数据使用CARLA模拟器生成，可以控制各种环境参数，例如天气、光照、行人的行为等。真实数据来自JAAD行车记录仪视频，使用v2e工具转换为事件流。事件帧的累积时间为33毫秒。基线模型使用SpikingJelly框架构建脉冲神经网络。

## 📊 实验亮点

论文使用SpikingJelly框架构建了基线脉冲神经网络，并在DVS-PedX数据集上进行了实验。实验结果揭示了合成数据与真实数据之间的性能差距，表明需要进一步研究领域自适应方法，为后续研究提供了方向。

## 🎯 应用场景

该研究成果可应用于智能驾驶、机器人导航、智能监控等领域，提升系统在复杂环境下的感知能力，尤其是在低光照、高动态范围和快速运动场景下的行人检测和意图预测能力，从而提高安全性。

## 📄 摘要（原文）

> Event cameras like Dynamic Vision Sensors (DVS) report micro-timed brightness changes instead of full frames, offering low latency, high dynamic range, and motion robustness. DVS-PedX (Dynamic Vision Sensor Pedestrian eXploration) is a neuromorphic dataset designed for pedestrian detection and crossing-intention analysis in normal and adverse weather conditions across two complementary sources: (1) synthetic event streams generated in the CARLA simulator for controlled "approach-cross" scenes under varied weather and lighting; and (2) real-world JAAD dash-cam videos converted to event streams using the v2e tool, preserving natural behaviors and backgrounds. Each sequence includes paired RGB frames, per-frame DVS "event frames" (33 ms accumulations), and frame-level labels (crossing vs. not crossing). We also provide raw AEDAT 2.0/AEDAT 4.0 event files and AVI DVS video files and metadata for flexible re-processing. Baseline spiking neural networks (SNNs) using SpikingJelly illustrate dataset usability and reveal a sim-to-real gap, motivating domain adaptation and multimodal fusion. DVS-PedX aims to accelerate research in event-based pedestrian safety, intention prediction, and neuromorphic perception.

