---
layout: default
title: ActiveUMI: Robotic Manipulation with Active Perception from Robot-Free Human Demonstrations
---

# ActiveUMI: Robotic Manipulation with Active Perception from Robot-Free Human Demonstrations

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.01607" target="_blank" class="toolbar-btn">arXiv: 2510.01607v1</a>
    <a href="https://arxiv.org/pdf/2510.01607.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.01607v1" 
            onclick="toggleFavorite(this, '2510.01607v1', 'ActiveUMI: Robotic Manipulation with Active Perception from Robot-Free Human Demonstrations')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Qiyuan Zeng, Chengmeng Li, Jude St. John, Zhongyi Zhou, Junjie Wen, Guorui Feng, Yichen Zhu, Yi Xu

**分类**: cs.RO, cs.CV

**发布日期**: 2025-10-02

**备注**: technique report. The website is available at https://activeumi.github.io

---

## 💡 一句话要点

**ActiveUMI：通过机器人自由的人类演示进行主动感知的机器人操作**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `机器人操作` `主动感知` `VR遥操作` `双手动操作` `数据收集` `策略学习` `泛化能力`

## 📋 核心要点

1. 现有机器人操作学习方法难以有效利用真实世界人类演示数据，限制了机器人泛化能力。
2. ActiveUMI通过便携式VR遥操作套件和传感器控制器，精确对齐人-机器人运动学，捕捉人类操作中的主动感知。
3. 实验表明，基于ActiveUMI数据训练的策略在复杂双手动任务上表现出优异的成功率和泛化能力。

## 📝 摘要（中文）

ActiveUMI是一个数据收集系统框架，旨在将真实场景下的人类演示迁移到能够执行复杂双手动操作的机器人上。ActiveUMI将便携式VR遥操作套件与传感器控制器相结合，通过精确的姿态对齐连接人-机器人运动学。为了确保移动性和数据质量，引入了沉浸式3D模型渲染、独立的穿戴式计算机和高效的校准方法等关键技术。ActiveUMI的核心在于捕捉主动的、以自我为中心的感知。通过记录操作员通过头戴式显示器进行的头部运动，系统学习视觉注意力和操作之间的关键联系。在六项具有挑战性的双手动任务上评估了ActiveUMI。仅使用ActiveUMI数据训练的策略在同分布任务上平均成功率达到70%，并表现出强大的泛化能力，在新物体和新环境中测试时仍保持56%的成功率。结果表明，便携式数据收集系统与学习到的主动感知相结合，为创建可泛化且高性能的真实世界机器人策略提供了一条有效且可扩展的途径。

## 🔬 方法详解

**问题定义**：现有机器人操作学习方法通常依赖于模拟数据或昂贵的实验室环境数据，难以获取真实世界人类操作的丰富信息。此外，现有方法往往忽略了人类操作中的主动感知，即视觉注意力和操作之间的联系，导致机器人难以泛化到新环境和新物体。

**核心思路**：ActiveUMI的核心思路是通过便携式VR遥操作系统，让操作员在虚拟环境中进行操作，同时记录操作员的头部运动和控制器数据。通过这种方式，系统可以学习到人类操作中的主动感知，并将这些知识迁移到机器人上。这样设计的目的是为了克服现有方法在数据获取和泛化能力方面的不足。

**技术框架**：ActiveUMI系统主要包含以下几个模块：1) 便携式VR遥操作套件，包括头戴式显示器和传感器控制器；2) 沉浸式3D模型渲染模块，用于创建虚拟环境；3) 数据采集模块，用于记录操作员的头部运动和控制器数据；4) 策略学习模块，用于训练机器人操作策略。整个流程是：操作员佩戴VR设备在虚拟环境中进行操作，系统记录数据，然后使用这些数据训练机器人策略。

**关键创新**：ActiveUMI最重要的技术创新点在于捕捉主动感知。通过记录操作员的头部运动，系统可以学习到视觉注意力和操作之间的联系。这与现有方法只关注操作轨迹不同，ActiveUMI能够让机器人像人类一样，根据视觉信息调整操作策略。

**关键设计**：ActiveUMI的关键设计包括：1) 使用传感器控制器精确对齐人-机器人运动学；2) 设计高效的校准方法，确保数据质量；3) 使用沉浸式3D模型渲染，提供逼真的虚拟环境；4) 使用独立的穿戴式计算机，保证系统的移动性。

## 📊 实验亮点

实验结果表明，仅使用ActiveUMI数据训练的策略在同分布任务上平均成功率达到70%，在新物体和新环境中测试时仍保持56%的成功率。这表明ActiveUMI能够有效地捕捉人类操作中的主动感知，并将其迁移到机器人上，从而提高机器人的泛化能力。相比于其他数据收集方法，ActiveUMI具有更高的效率和更低的成本。

## 🎯 应用场景

ActiveUMI技术可应用于各种需要复杂双手动操作的机器人任务，例如：远程医疗手术、危险环境下的物体处理、家庭服务机器人等。该技术能够降低机器人操作学习的成本，提高机器人的泛化能力，加速机器人在实际场景中的应用。

## 📄 摘要（原文）

> We present ActiveUMI, a framework for a data collection system that transfers in-the-wild human demonstrations to robots capable of complex bimanual manipulation. ActiveUMI couples a portable VR teleoperation kit with sensorized controllers that mirror the robot's end-effectors, bridging human-robot kinematics via precise pose alignment. To ensure mobility and data quality, we introduce several key techniques, including immersive 3D model rendering, a self-contained wearable computer, and efficient calibration methods. ActiveUMI's defining feature is its capture of active, egocentric perception. By recording an operator's deliberate head movements via a head-mounted display, our system learns the crucial link between visual attention and manipulation. We evaluate ActiveUMI on six challenging bimanual tasks. Policies trained exclusively on ActiveUMI data achieve an average success rate of 70\% on in-distribution tasks and demonstrate strong generalization, retaining a 56\% success rate when tested on novel objects and in new environments. Our results demonstrate that portable data collection systems, when coupled with learned active perception, provide an effective and scalable pathway toward creating generalizable and highly capable real-world robot policies.

