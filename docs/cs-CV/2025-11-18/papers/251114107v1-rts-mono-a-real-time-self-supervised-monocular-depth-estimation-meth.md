---
layout: default
title: "RTS-Mono: A Real-Time Self-Supervised Monocular Depth Estimation Method for Real-World Deployment"
---

# RTS-Mono: A Real-Time Self-Supervised Monocular Depth Estimation Method for Real-World Deployment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.14107" class="toolbar-btn" target="_blank">📄 arXiv: 2511.14107v1</a>
  <a href="https://arxiv.org/pdf/2511.14107.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.14107v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.14107v1', 'RTS-Mono: A Real-Time Self-Supervised Monocular Depth Estimation Method for Real-World Deployment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zeyu Cheng, Tongfei Liu, Tao Lei, Xiang Hua, Yi Zhang, Chengkai Tang

**分类**: cs.CV

**发布日期**: 2025-11-18

**备注**: 14 pages, 10 figures

**🔗 代码/项目**: [GITHUB](https://github.com/ZYCheng777/RTS-Mono)

---

## 💡 一句话要点

**RTS-Mono：一种用于真实世界部署的实时自监督单目深度估计方法**

🎯 **匹配领域**: **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `单目深度估计` `自监督学习` `实时推理` `轻量化网络` `自动驾驶`

## 📋 核心要点

1. 现有单目深度估计模型计算资源消耗大，轻量化后性能显著下降，阻碍了其在自动驾驶和机器人导航等领域的实际部署。
2. RTS-Mono采用轻量级编码器-解码器架构，利用Lite-Encoder和多尺度稀疏融合框架，在保证性能的同时，显著降低了计算冗余。
3. 实验结果表明，RTS-Mono在KITTI数据集上以极低的参数量实现了SOTA性能，并在Nvidia Jetson Orin上实现了49 FPS的实时推理。

## 📝 摘要（中文）

本文提出了一种名为RTS-Mono的实时自监督单目深度估计方法，旨在解决现有方法计算资源消耗大、性能下降等问题，从而促进自监督单目深度估计模型在现实世界中的部署。RTS-Mono采用轻量高效的编码器-解码器架构，其中编码器基于Lite-Encoder，解码器采用多尺度稀疏融合框架，以最小化冗余，保证性能并提高推理速度。在KITTI数据集上的实验表明，RTS-Mono以极低的参数量（3M）在高分辨率和低分辨率下均实现了最先进的性能。与轻量级方法相比，RTS-Mono在低分辨率下将Abs Rel和Sq Rel分别提高了5.6%和9.8%，在高分辨率下将Sq Rel和RMSE分别提高了6.1%和1.9%。在真实世界部署实验中，RTS-Mono具有极高的精度，并且可以在Nvidia Jetson Orin上以49 FPS的速度执行实时推理。源代码已在https://github.com/ZYCheng777/RTS-Mono上发布。

## 🔬 方法详解

**问题定义**：论文旨在解决自监督单目深度估计模型在实际部署中面临的计算资源消耗大和性能下降的问题。现有方法要么计算量大难以实时运行，要么为了轻量化而牺牲了精度，无法满足真实场景的需求。

**核心思路**：论文的核心思路是设计一个轻量级但高效的编码器-解码器架构，通过减少冗余计算和优化网络结构，在保证深度估计精度的同时，显著降低模型的参数量和计算复杂度，从而实现实时推理。

**技术框架**：RTS-Mono的整体架构是一个编码器-解码器结构。编码器部分采用Lite-Encoder，用于提取图像特征。解码器部分采用多尺度稀疏融合框架，将不同尺度的特征进行融合，并输出深度图。该框架避免了传统解码器中大量的上采样和卷积操作，从而降低了计算量。

**关键创新**：RTS-Mono的关键创新在于其轻量级解码器的设计，即多尺度稀疏融合框架。该框架通过选择性地融合不同尺度的特征，避免了冗余计算，同时保证了深度估计的精度。此外，Lite-Encoder的使用也进一步降低了模型的参数量。

**关键设计**：解码器中的多尺度稀疏融合模块是关键设计之一。具体来说，该模块首先对不同尺度的特征图进行稀疏采样，然后将采样后的特征进行融合。稀疏采样的比例是一个重要的超参数，需要根据具体任务进行调整。此外，损失函数也对模型的性能有重要影响，论文可能采用了多种损失函数的组合，例如光度一致性损失和深度平滑损失。

## 📊 实验亮点

RTS-Mono在KITTI数据集上取得了显著的性能提升。在低分辨率下，Abs Rel和Sq Rel分别提高了5.6%和9.8%。在高分辨率下，Sq Rel和RMSE分别提高了6.1%和1.9%。更重要的是，RTS-Mono在Nvidia Jetson Orin上实现了49 FPS的实时推理，证明了其在实际应用中的可行性。

## 🎯 应用场景

RTS-Mono具有广泛的应用前景，包括自动驾驶、机器人导航、增强现实等领域。在自动驾驶中，它可以为车辆提供准确的深度信息，从而提高车辆的感知能力和安全性。在机器人导航中，它可以帮助机器人理解周围环境，从而实现自主导航。在增强现实中，它可以将虚拟物体与真实场景进行融合，从而提供更加沉浸式的体验。

## 📄 摘要（原文）

> Depth information is crucial for autonomous driving and intelligent robot navigation. The simplicity and flexibility of self-supervised monocular depth estimation are conducive to its role in these fields. However, most existing monocular depth estimation models consume many computing resources. Although some methods have reduced the model's size and improved computing efficiency, the performance deteriorates, seriously hindering the real-world deployment of self-supervised monocular depth estimation models in the real world. To address this problem, we proposed a real-time self-supervised monocular depth estimation method and implemented it in the real world. It is called RTS-Mono, which is a lightweight and efficient encoder-decoder architecture. The encoder is based on Lite-Encoder, and the decoder is designed with a multi-scale sparse fusion framework to minimize redundancy, ensure performance, and improve inference speed. RTS-Mono achieved state-of-the-art (SoTA) performance in high and low resolutions with extremely low parameter counts (3 M) in experiments based on the KITTI dataset. Compared with lightweight methods, RTS-Mono improved Abs Rel and Sq Rel by 5.6% and 9.8% at low resolution and improved Sq Rel and RMSE by 6.1% and 1.9% at high resolution. In real-world deployment experiments, RTS-Mono has extremely high accuracy and can perform real-time inference on Nvidia Jetson Orin at a speed of 49 FPS. Source code is available at https://github.com/ZYCheng777/RTS-Mono.

