---
layout: default
title: "CoDrone: Autonomous Drone Navigation Assisted by Edge and Cloud Foundation Models"
---

# CoDrone: Autonomous Drone Navigation Assisted by Edge and Cloud Foundation Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.19083" class="toolbar-btn" target="_blank">📄 arXiv: 2512.19083v1</a>
  <a href="https://arxiv.org/pdf/2512.19083.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.19083v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.19083v1', 'CoDrone: Autonomous Drone Navigation Assisted by Edge and Cloud Foundation Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pengyu Chen, Tao Ouyang, Ke Luo, Weijie Hong, Xu Chen

**分类**: cs.RO

**发布日期**: 2025-12-22

**备注**: This paper is accepted by the IEEE Internet of Things Journal (IoT-J) for publication in the Special Issue on "Augmented Edge Sensing Intelligence for Low-Altitude IoT Systems"

---

## 💡 一句话要点

**CoDrone：边缘云协同，利用基础模型增强无人机自主导航能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `无人机导航` `边缘计算` `云计算` `深度强化学习` `基础模型` `视觉语言模型` `自主导航`

## 📋 核心要点

1. 现有无人机自主导航受限于机载算力，无法部署复杂模型，而卸载到边缘服务器则引入延迟，需要在性能和效率之间权衡。
2. CoDrone提出云-边-端协同框架，利用边缘辅助的基础模型进行深度估计，并结合一维占据栅格导航，提升环境理解能力。
3. 实验表明，CoDrone在不同条件下优于基线方法，平均飞行距离提升40%，导航质量提升5%，展现了其优越性。

## 📝 摘要（中文）

无人机自主导航面临着机载计算资源有限的挑战，这限制了部署的深度神经网络只能采用浅层架构，难以处理复杂环境。将任务卸载到远程边缘服务器会引入高延迟，从而在系统设计中产生固有的权衡。为了解决这些限制，我们提出了CoDrone，这是第一个云-边-端协同计算框架，将基础模型集成到自主无人机巡航场景中，有效地利用基础模型来增强资源受限的无人机平台的性能。为了减少机载计算和数据传输开销，CoDrone采用灰度图像进行导航模型。当需要增强环境感知时，CoDrone利用边缘辅助的基础模型Depth Anything V2进行深度估计，并引入了一种新颖的基于一维占据栅格的导航方法，从而实现细粒度的场景理解，同时提高自主导航的效率和表征简洁性。CoDrone的一个关键组成部分是基于深度强化学习的神经调度器，它将深度估计与自主导航决策无缝集成，从而能够实时适应动态环境。此外，该框架还引入了一个无人机特定的视觉语言交互模块，该模块结合了领域定制的低级飞行原语，以实现云基础模型与无人机之间的有效交互。VLM的引入增强了复杂未知场景中的开放集推理能力。实验结果表明，CoDrone在不同的飞行速度和网络条件下优于基线方法，平均飞行距离提高了40%，平均导航质量提高了5%。

## 🔬 方法详解

**问题定义**：无人机自主导航需要在有限的机载计算资源下实现高效的环境感知和路径规划。现有的方法要么依赖于计算量小的浅层网络，导致环境理解能力不足；要么将计算卸载到远程服务器，引入不可接受的延迟，影响实时性。因此，如何在资源受限的平台上实现高性能的自主导航是一个关键问题。

**核心思路**：CoDrone的核心思路是利用云-边-端协同计算框架，将计算密集型的任务（如深度估计和视觉语言交互）卸载到边缘服务器或云端，同时在无人机端保留轻量级的导航模型。通过智能调度，根据环境需求动态地选择合适的计算资源，从而在性能和效率之间取得平衡。

**技术框架**：CoDrone框架包含三个主要组成部分：1) 无人机端：负责图像采集、轻量级导航和与边缘/云端的通信。2) 边缘服务器：部署Depth Anything V2等基础模型，用于深度估计，并提供低延迟的计算服务。3) 云端：部署视觉语言模型（VLM），用于处理复杂的开放场景推理任务。框架还包含一个基于深度强化学习的神经调度器，用于动态地决定何时使用边缘服务器进行深度估计，以及何时使用云端进行视觉语言交互。

**关键创新**：CoDrone的关键创新在于：1) 提出了一个云-边-端协同计算框架，充分利用了不同计算资源的优势。2) 引入了基于一维占据栅格的导航方法，简化了环境表示，提高了导航效率。3) 设计了一个基于深度强化学习的神经调度器，实现了对计算资源的动态管理和优化。4) 集成了无人机特定的视觉语言交互模块，增强了无人机在复杂未知场景中的推理能力。

**关键设计**：CoDrone的关键设计包括：1) 采用灰度图像作为导航模型的输入，降低了计算和传输开销。2) 使用Depth Anything V2进行深度估计，该模型具有较高的精度和效率。3) 一维占据栅格将三维空间简化为一维，降低了计算复杂度。4) 神经调度器使用深度强化学习算法进行训练，以最大化导航性能和资源利用率。5) 无人机特定的视觉语言交互模块包含领域定制的低级飞行原语，使得云端VLM能够更好地理解无人机的状态和目标。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19083v1/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19083v1/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.19083v1/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，CoDrone在不同的飞行速度和网络条件下均优于基线方法。具体来说，CoDrone的平均飞行距离提高了40%，平均导航质量提高了5%。这些结果验证了CoDrone框架的有效性和优越性，表明其能够在资源受限的平台上实现高性能的自主导航。

## 🎯 应用场景

CoDrone框架具有广泛的应用前景，例如在物流配送、环境监测、灾害救援等领域。通过利用云-边-端协同计算和基础模型，CoDrone可以使无人机在复杂环境中实现更安全、更高效的自主导航，从而提高工作效率和降低运营成本。未来，CoDrone还可以与其他技术（如5G通信、物联网）相结合，构建更智能化的无人机应用生态系统。

## 📄 摘要（原文）

> Autonomous navigation for Unmanned Aerial Vehicles faces key challenges from limited onboard computational resources, which restrict deployed deep neural networks to shallow architectures incapable of handling complex environments. Offloading tasks to remote edge servers introduces high latency, creating an inherent trade-off in system design. To address these limitations, we propose CoDrone - the first cloud-edge-end collaborative computing framework integrating foundation models into autonomous UAV cruising scenarios - effectively leveraging foundation models to enhance performance of resource-constrained unmanned aerial vehicle platforms. To reduce onboard computation and data transmission overhead, CoDrone employs grayscale imagery for the navigation model. When enhanced environmental perception is required, CoDrone leverages the edge-assisted foundation model Depth Anything V2 for depth estimation and introduces a novel one-dimensional occupancy grid-based navigation method - enabling fine-grained scene understanding while advancing efficiency and representational simplicity of autonomous navigation. A key component of CoDrone is a Deep Reinforcement Learning-based neural scheduler that seamlessly integrates depth estimation with autonomous navigation decisions, enabling real-time adaptation to dynamic environments. Furthermore, the framework introduces a UAV-specific vision language interaction module incorporating domain-tailored low-level flight primitives to enable effective interaction between the cloud foundation model and the UAV. The introduction of VLM enhances open-set reasoning capabilities in complex unseen scenarios. Experimental results show CoDrone outperforms baseline methods under varying flight speeds and network conditions, achieving a 40% increase in average flight distance and a 5% improvement in average Quality of Navigation.

