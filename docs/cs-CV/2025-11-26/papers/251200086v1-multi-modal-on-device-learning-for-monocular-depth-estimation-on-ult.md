---
layout: default
title: Multi-modal On-Device Learning for Monocular Depth Estimation on Ultra-low-power MCUs
---

# Multi-modal On-Device Learning for Monocular Depth Estimation on Ultra-low-power MCUs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.00086" class="toolbar-btn" target="_blank">📄 arXiv: 2512.00086v1</a>
  <a href="https://arxiv.org/pdf/2512.00086.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.00086v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.00086v1', 'Multi-modal On-Device Learning for Monocular Depth Estimation on Ultra-low-power MCUs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Davide Nadalini, Manuele Rusci, Elia Cereda, Luca Benini, Francesco Conti, Daniele Palossi

**分类**: cs.CV

**发布日期**: 2025-11-26

**备注**: 14 pages, 9 figures, 3 tables. Associated open-source release available at: https://github.com/dnadalini/ondevice_learning_for_monocular_depth_estimation

---

## 💡 一句话要点

**提出一种多模态片上学习方法，用于超低功耗MCU上的单目深度估计。**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `单目深度估计` `片上学习` `多模态融合` `物联网` `超低功耗` `领域自适应` `稀疏更新`

## 📋 核心要点

1. 现有单目深度估计模型在IoT设备上部署时，由于领域迁移导致精度显著下降。
2. 提出一种多模态片上学习方法，利用深度传感器生成伪标签，并在MCU上进行模型微调。
3. 实验表明，该方法在实际场景中能有效降低深度估计误差，且微调过程高效。

## 📝 摘要（中文）

单目深度估计(MDE)在超低功耗(ULP)物联网(IoT)平台中实现空间感知应用方面起着关键作用。然而，为IoT节点设计的MDE深度神经网络的参数数量有限，导致当现场观察到的传感器数据与训练数据集显著不同时，精度会严重下降。为了解决这个领域迁移问题，我们提出了一种多模态片上学习(ODL)技术，部署在集成了Greenwaves GAP9微控制器单元(MCU)、80mW单目相机和8x8像素深度传感器的IoT设备上，功耗约为300mW。在正常运行中，该设置使用单目图像为微型107k参数的μPyD-Net模型提供推理。深度传感器通常被停用以最小化能耗，仅当系统放置在新的环境中时，才与相机一起激活以收集伪标签。然后，使用新数据完全在MCU上执行微调任务。为了优化我们基于反向传播的片上训练，我们引入了一种新颖的内存驱动的稀疏更新方案，该方案将微调内存最小化到1.2MB，比完整更新少2.2倍，同时保持精度（即，在KITTI和NYUv2数据集上仅下降2%和1.5%）。我们的现场测试首次证明，MDE的ODL可以在IoT节点上在17.8分钟内完成，仅使用在实际部署场景中收集的3k个自标记样本，就将均方根误差从4.9米降低到0.6米。

## 🔬 方法详解

**问题定义**：论文旨在解决单目深度估计模型在实际IoT部署中，由于数据分布与训练集差异过大导致的精度下降问题。现有方法通常依赖于预训练模型，难以适应新的环境，且在资源受限的MCU上进行模型更新面临挑战。

**核心思路**：论文的核心思路是利用片上深度传感器获取伪标签，并结合单目图像数据，在MCU上进行模型的在线微调。通过多模态信息的融合，使模型能够快速适应新的环境，提高深度估计的准确性。

**技术框架**：该方法的技术框架主要包括以下几个阶段：1) 使用单目相机进行图像采集；2) 在新环境中，激活深度传感器，与单目相机同步采集数据，生成伪标签；3) 使用采集到的数据，在MCU上对预训练的单目深度估计模型进行微调；4) 微调后的模型用于后续的单目深度估计任务。

**关键创新**：该方法最重要的技术创新点在于提出了一种内存驱动的稀疏更新方案，用于优化片上训练过程。该方案通过选择性地更新模型参数，显著降低了微调所需的内存空间，使得在资源受限的MCU上进行模型微调成为可能。

**关键设计**：论文的关键设计包括：1) 使用微型化的单目深度估计模型（μPyD-Net），以适应MCU的计算能力；2) 设计了一种内存驱动的稀疏更新方案，该方案根据参数的重要性选择性地更新参数，从而减少内存占用；3) 采用反向传播算法进行模型微调，并优化了反向传播过程，以提高训练效率。

## 📊 实验亮点

实验结果表明，该方法在IoT节点上仅用17.8分钟即可完成单目深度估计模型的片上学习，并且仅使用3k个自标记样本，就将均方根误差从4.9米降低到0.6米。同时，提出的内存驱动稀疏更新方案将微调内存降低到1.2MB，比完整更新减少2.2倍，而精度仅下降2%（KITTI）和1.5%（NYUv2）。

## 🎯 应用场景

该研究成果可广泛应用于资源受限的物联网设备，例如智能家居、机器人导航、环境监测等领域。通过片上学习，设备能够适应不同的环境和场景，提高感知能力和智能化水平。该技术还有助于降低对云端计算的依赖，提高数据隐私性。

## 📄 摘要（原文）

> Monocular depth estimation (MDE) plays a crucial role in enabling spatially-aware applications in Ultra-low-power (ULP) Internet-of-Things (IoT) platforms. However, the limited number of parameters of Deep Neural Networks for the MDE task, designed for IoT nodes, results in severe accuracy drops when the sensor data observed in the field shifts significantly from the training dataset. To address this domain shift problem, we present a multi-modal On-Device Learning (ODL) technique, deployed on an IoT device integrating a Greenwaves GAP9 MicroController Unit (MCU), a 80 mW monocular camera and a 8 x 8 pixel depth sensor, consuming $\approx$300mW. In its normal operation, this setup feeds a tiny 107 k-parameter $μ$PyD-Net model with monocular images for inference. The depth sensor, usually deactivated to minimize energy consumption, is only activated alongside the camera to collect pseudo-labels when the system is placed in a new environment. Then, the fine-tuning task is performed entirely on the MCU, using the new data. To optimize our backpropagation-based on-device training, we introduce a novel memory-driven sparse update scheme, which minimizes the fine-tuning memory to 1.2 MB, 2.2x less than a full update, while preserving accuracy (i.e., only 2% and 1.5% drops on the KITTI and NYUv2 datasets). Our in-field tests demonstrate, for the first time, that ODL for MDE can be performed in 17.8 minutes on the IoT node, reducing the root mean squared error from 4.9 to 0.6m with only 3 k self-labeled samples, collected in a real-life deployment scenario.

