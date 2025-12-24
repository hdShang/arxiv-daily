---
layout: default
title: "PIE: Perception and Interaction Enhanced End-to-End Motion Planning for Autonomous Driving"
---

# PIE: Perception and Interaction Enhanced End-to-End Motion Planning for Autonomous Driving

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.18609" class="toolbar-btn" target="_blank">📄 arXiv: 2509.18609v1</a>
  <a href="https://arxiv.org/pdf/2509.18609.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.18609v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.18609v1', 'PIE: Perception and Interaction Enhanced End-to-End Motion Planning for Autonomous Driving')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Chengran Yuan, Zijian Lu, Zhanqi Zhang, Yimin Zhao, Zefan Huang, Shuo Sun, Jiawei Sun, Jiahui Li, Christina Dao Wen Lee, Dongen Li, Marcelo H. Ang

**分类**: cs.RO

**发布日期**: 2025-09-23

---

## 💡 一句话要点

**PIE：面向自动驾驶，提出感知交互增强的端到端运动规划框架**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自动驾驶` `端到端运动规划` `多模态融合` `Mamba` `意图预测` `场景理解` `轨迹规划`

## 📋 核心要点

1. 端到端运动规划面临场景理解和有效预测的挑战，阻碍了其大规模部署。
2. PIE框架通过集成先进的感知、推理和意图建模，动态捕捉自车与周围车辆的交互。
3. PIE在NAVSIM基准测试中，无需集成和数据增强，超越了现有最佳方法。

## 📝 摘要（中文）

本文提出PIE，一种开创性的框架，集成了先进的感知、推理和意图建模，以动态捕捉自车与周围车辆之间的交互。它包含一个双向Mamba融合模块，解决了相机和激光雷达多模态融合中的数据压缩损失。同时，一个新颖的推理增强解码器集成了Mamba和混合专家模型，以促进符合场景的锚点选择和优化自适应轨迹推理。PIE采用动作-运动交互模块，有效地利用周围车辆的状态预测来改进自车规划。该框架在NAVSIM基准上进行了全面验证。PIE在不使用任何集成和数据增强技术的情况下，实现了88.9的PDM分数和85.6的EPDM分数，超过了现有最先进方法的性能。全面的定量和定性分析表明，PIE能够可靠地生成可行且高质量的自车轨迹。

## 🔬 方法详解

**问题定义**：端到端运动规划旨在简化自动驾驶流程，但现有方法在复杂场景理解和周围车辆行为预测方面存在不足，导致决策质量下降，难以应对真实交通环境中的复杂交互。现有方法难以有效融合多模态数据，且推理能力有限，无法准确预测周围车辆的意图，从而影响自车轨迹规划的安全性与效率。

**核心思路**：PIE的核心在于通过融合先进的感知、推理和意图建模技术，提升端到端运动规划的性能。具体而言，它利用双向Mamba融合模块解决多模态数据融合中的信息损失问题，并采用推理增强解码器提升场景理解和轨迹预测能力。此外，PIE还引入动作-运动交互模块，利用周围车辆的状态预测来优化自车轨迹规划。

**技术框架**：PIE框架主要包含以下几个模块：1) 双向Mamba融合模块：用于融合相机和激光雷达等多模态输入数据，减少信息损失。2) 推理增强解码器：集成了Mamba和混合专家模型，用于场景理解、锚点选择和轨迹推理。3) 动作-运动交互模块：利用周围车辆的状态预测来优化自车轨迹规划。整体流程是从多模态感知输入开始，经过融合和推理，最终生成自车的运动轨迹。

**关键创新**：PIE的关键创新在于：1) 双向Mamba融合：相比于传统的融合方法，双向Mamba能够更有效地保留多模态数据中的关键信息，减少信息压缩带来的损失。2) 推理增强解码器：通过集成Mamba和混合专家模型，提升了模型对复杂场景的理解和推理能力，从而更准确地预测周围车辆的意图和行为。3) 动作-运动交互模块：将周围车辆的状态预测纳入自车规划中，实现了更安全、更高效的运动规划。

**关键设计**：双向Mamba融合模块的具体结构未知，但其核心思想是利用Mamba架构的序列建模能力，对多模态数据进行双向处理，从而更好地捕捉数据之间的关联性。推理增强解码器中，Mamba用于序列建模，混合专家模型用于处理不同场景下的轨迹预测。动作-运动交互模块的具体实现方式未知，但其目标是根据周围车辆的预测状态，调整自车的运动轨迹，以避免碰撞或提高通行效率。

## 📊 实验亮点

PIE在NAVSIM基准测试中取得了显著的性能提升，在不使用任何集成和数据增强技术的情况下，实现了88.9的PDM分数和85.6的EPDM分数，超越了现有最先进的方法。这表明PIE框架在复杂场景理解和轨迹规划方面具有强大的能力，能够生成可行且高质量的自车轨迹。

## 🎯 应用场景

PIE框架具有广泛的应用前景，可用于各种自动驾驶场景，包括城市道路、高速公路和停车场等。该框架能够提升自动驾驶系统的安全性、效率和舒适性，并有望加速自动驾驶技术的商业化落地。此外，PIE的设计思路也可以应用于其他需要多模态感知和复杂推理的机器人应用中。

## 📄 摘要（原文）

> End-to-end motion planning is promising for simplifying complex autonomous driving pipelines. However, challenges such as scene understanding and effective prediction for decision-making continue to present substantial obstacles to its large-scale deployment. In this paper, we present PIE, a pioneering framework that integrates advanced perception, reasoning, and intention modeling to dynamically capture interactions between the ego vehicle and surrounding agents. It incorporates a bidirectional Mamba fusion that addresses data compression losses in multimodal fusion of camera and LiDAR inputs, alongside a novel reasoning-enhanced decoder integrating Mamba and Mixture-of-Experts to facilitate scene-compliant anchor selection and optimize adaptive trajectory inference. PIE adopts an action-motion interaction module to effectively utilize state predictions of surrounding agents to refine ego planning. The proposed framework is thoroughly validated on the NAVSIM benchmark. PIE, without using any ensemble and data augmentation techniques, achieves an 88.9 PDM score and 85.6 EPDM score, surpassing the performance of prior state-of-the-art methods. Comprehensive quantitative and qualitative analyses demonstrate that PIE is capable of reliably generating feasible and high-quality ego trajectories.

