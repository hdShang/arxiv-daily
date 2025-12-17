---
layout: default
title: Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation featuring a High-Fidelity Scalable Simulator
---

# Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation featuring a High-Fidelity Scalable Simulator

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.06434" class="toolbar-btn" target="_blank">📄 arXiv: 2511.06434v2</a>
  <a href="https://arxiv.org/pdf/2511.06434.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.06434v2" onclick="toggleFavorite(this, '2511.06434v2', 'Real Garment Benchmark (RGBench): A Comprehensive Benchmark for Robotic Garment Manipulation featuring a High-Fidelity Scalable Simulator')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Wenkang Hu, Xincheng Tang, Yanzhi E, Yitong Li, Zhengjie Shu, Wei Li, Huamin Wang, Ruigang Yang

**分类**: cs.RO

**发布日期**: 2025-11-09 (更新: 2025-11-12)

**备注**: 2026 AAAI Accept

---

## 💡 一句话要点

**提出RGBench：一个用于机器人服装操作的高保真可扩展模拟器基准**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `机器人服装操作` `形变物体模拟` `基准数据集` `高性能模拟器` `cloth simulation`

## 📋 核心要点

1. 刚性物体操作的模拟学习取得了显著进展，但由于缺乏形变物体模型和逼真的非刚体模拟器，其成功难以应用于形变物体。
2. RGBench提供了一个包含大量服装模型和高性能模拟器的基准，并设计了评估模拟质量的协议，旨在解决服装操作模拟的难题。
3. 实验结果表明，RGBench的模拟器在速度和精度上均优于现有布料模拟器，为机器人服装操作研究提供了有力的工具。

## 📝 摘要（中文）

本文提出了Real Garment Benchmark (RGBench)，这是一个用于机器人服装操作的综合基准。它包含超过6000个服装网格模型的多样化集合，一个新的高性能模拟器，以及一个全面的协议，用于评估服装模拟质量，并具有精心测量的真实服装动力学。实验表明，该模拟器在性能上大大优于目前可用的布料模拟器，在保持3倍速度的同时，将模拟误差降低了20%。RGBench将被公开发布，以加速未来机器人服装操作的研究。

## 🔬 方法详解

**问题定义**：现有的机器人操作主要集中在刚性物体上，而服装等柔性物体的操作由于其形变特性，建模和模拟都非常困难。现有的布料模拟器在精度和速度上都无法满足机器人操作学习的需求，缺乏一个高质量的基准来评估和比较不同的算法。

**核心思路**：论文的核心思路是构建一个包含大量真实服装模型和高性能模拟器的基准数据集RGBench。通过提供多样化的服装模型和精确的动力学模拟，RGBench旨在促进机器人服装操作算法的开发和评估。

**技术框架**：RGBench主要包含三个部分：1) 一个包含超过6000个服装网格模型的数据库，这些模型具有多样化的形状和材质属性；2) 一个高性能的布料模拟器，该模拟器针对服装操作进行了优化，能够在保证精度的前提下实现快速模拟；3) 一套评估协议，用于评估模拟器的质量，包括与真实服装动力学的对比。

**关键创新**：RGBench的关键创新在于其综合性和实用性。它不仅提供了大量的服装模型，还开发了一个高性能的模拟器，并设计了一套评估协议。这使得研究人员能够方便地使用RGBench来开发和评估机器人服装操作算法。与现有方法相比，RGBench更加注重模拟的真实性和效率，从而更好地服务于机器人操作学习。

**关键设计**：RGBench的模拟器采用了优化的数值积分方法和碰撞检测算法，以提高模拟速度。为了保证模拟的精度，RGBench使用了精心测量的真实服装动力学数据来校准模拟器的参数。此外，RGBench还提供了一套用于评估模拟器质量的指标，包括服装的形状误差、运动轨迹误差等。

## 📊 实验亮点

实验结果表明，RGBench的模拟器在模拟精度和速度上均优于现有的布料模拟器。具体来说，RGBench的模拟器在保持3倍速度的同时，将模拟误差降低了20%。这些结果表明，RGBench是一个高质量的基准，可以有效地促进机器人服装操作算法的开发和评估。

## 🎯 应用场景

RGBench在服装制造、仓储物流、家政服务等领域具有广泛的应用前景。例如，在服装制造中，机器人可以利用RGBench来学习如何自动折叠、整理和包装服装。在家政服务中，机器人可以利用RGBench来学习如何帮助人们穿戴和整理衣物。该研究的成果将加速机器人技术在服装领域的应用，提高生产效率和服务质量。

## 📄 摘要（原文）

> While there has been significant progress to use simulated data to learn robotic manipulation of rigid objects, applying its success to deformable objects has been hindered by the lack of both deformable object models and realistic non-rigid body simulators. In this paper, we present Real Garment Benchmark (RGBench), a comprehensive benchmark for robotic manipulation of garments. It features a diverse set of over 6000 garment mesh models, a new high-performance simulator, and a comprehensive protocol to evaluate garment simulation quality with carefully measured real garment dynamics. Our experiments demonstrate that our simulator outperforms currently available cloth simulators by a large margin, reducing simulation error by 20% while maintaining a speed of 3 times faster. We will publicly release RGBench to accelerate future research in robotic garment manipulation. Website: https://rgbench.github.io/

