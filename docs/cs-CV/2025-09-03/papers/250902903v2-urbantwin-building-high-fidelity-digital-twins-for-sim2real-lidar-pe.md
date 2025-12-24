---
layout: default
title: "UrbanTwin: Building High-Fidelity Digital Twins for Sim2Real LiDAR Perception and Evaluation"
---

# UrbanTwin: Building High-Fidelity Digital Twins for Sim2Real LiDAR Perception and Evaluation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.02903" class="toolbar-btn" target="_blank">📄 arXiv: 2509.02903v2</a>
  <a href="https://arxiv.org/pdf/2509.02903.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.02903v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.02903v2', 'UrbanTwin: Building High-Fidelity Digital Twins for Sim2Real LiDAR Perception and Evaluation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Muhammad Shahbaz, Shaurya Agarwal

**分类**: cs.CV

**发布日期**: 2025-09-03 (更新: 2025-10-14)

---

## 💡 一句话要点

**UrbanTwin：构建高保真数字孪生，用于Sim2Real LiDAR感知与评估**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `数字孪生` `Sim2Real` `LiDAR感知` `智能交通系统` `合成数据` `深度学习` `开源数据` `高保真仿真`

## 📋 核心要点

1. 现有ITS中基于LiDAR的感知系统依赖大规模标注数据，但数据获取成本高昂，限制了系统扩展。
2. 论文提出利用高保真数字孪生(HiFi DTs)生成逼真的合成数据，从而实现低成本的Sim2Real学习。
3. 通过开源数据建模真实环境，生成了UT-LUMPI等数据集，并在感知任务中超越了真实数据训练的基线。

## 📝 摘要（中文）

基于LiDAR的智能交通系统(ITS)感知依赖于使用大规模标注数据集训练的深度神经网络。然而，创建此类数据集成本高昂、耗时且劳动密集，限制了感知系统的可扩展性。Sim2Real学习提供了一种可扩展的替代方案，但其成功取决于仿真环境对真实世界环境、动态和传感器的保真度。本教程介绍了一个可复现的工作流程，用于构建高保真数字孪生(HiFi DTs)以生成逼真的合成数据集。我们概述了使用开源资源（如卫星图像、OpenStreetMap和传感器规格）对静态几何、道路基础设施和动态交通进行建模的实用步骤。由此产生的环境支持可扩展且经济高效的数据生成，以实现稳健的Sim2Real学习。使用此工作流程，我们发布了三个合成LiDAR数据集，即UT-LUMPI、UT-V2X-Real和UT-TUMTraf-I，它们密切复制了真实位置，并且在感知任务中优于真实数据训练的基线。本指南有助于在ITS研究和部署中更广泛地采用HiFi DTs。

## 🔬 方法详解

**问题定义**：论文旨在解决智能交通系统中，基于LiDAR的感知系统对大规模标注数据集的依赖问题。现有方法获取真实数据的成本过高，严重限制了系统的可扩展性，并且难以覆盖所有 Corner Case。

**核心思路**：论文的核心思路是利用高保真数字孪生（HiFi DTs）技术，构建与真实世界高度相似的虚拟环境，并在该环境中生成大量的合成数据。通过Sim2Real学习，将模型在合成数据上训练的知识迁移到真实世界中，从而降低对真实数据的依赖。

**技术框架**：该工作流程主要包含以下几个阶段：1) 使用开源数据（如卫星图像、OpenStreetMap）对静态几何和道路基础设施进行建模；2) 利用交通仿真软件模拟动态交通；3) 根据传感器规格，在虚拟环境中模拟LiDAR传感器；4) 生成合成LiDAR点云数据；5) 利用合成数据训练感知模型；6) 在真实数据上进行验证和微调。

**关键创新**：论文的关键创新在于提出了一个可复现的、基于开源数据构建高保真数字孪生的工作流程。该流程能够有效地模拟真实世界的环境、动态和传感器特性，从而生成高质量的合成数据。此外，论文还发布了三个基于该流程生成的合成LiDAR数据集，为Sim2Real学习提供了宝贵的资源。

**关键设计**：论文的关键设计包括：1) 精心选择和处理开源数据，以保证数字孪生的几何精度和语义完整性；2) 采用 realistic 的交通仿真模型，以模拟真实的交通流；3) 准确模拟 LiDAR 传感器的物理特性，如扫描模式、噪声分布等；4) 设计合理的评估指标，以衡量合成数据的质量和Sim2Real学习的效果。

## 📊 实验亮点

论文通过实验验证了所提出的高保真数字孪生方法的有效性。在三个合成LiDAR数据集（UT-LUMPI、UT-V2X-Real和UT-TUMTraf-I）上，使用合成数据训练的感知模型在真实数据上的表现优于使用真实数据训练的基线模型。这表明，通过高保真数字孪生生成的合成数据可以有效地替代真实数据，从而降低数据标注成本。

## 🎯 应用场景

该研究成果可广泛应用于智能交通系统领域，例如自动驾驶、智能路灯、交通流量监控等。通过构建高保真数字孪生，可以降低感知算法的开发成本，加速算法的迭代速度，并提高算法的鲁棒性和泛化能力。此外，该方法还可以用于评估和验证新的交通管理策略，为城市规划和交通决策提供支持。

## 📄 摘要（原文）

> LiDAR-based perception in intelligent transportation systems (ITS) relies on deep neural networks trained with large-scale labeled datasets. However, creating such datasets is expensive, time-consuming, and labor-intensive, limiting the scalability of perception systems. Sim2Real learning offers a scalable alternative, but its success depends on the simulation's fidelity to real-world environments, dynamics, and sensors. This tutorial introduces a reproducible workflow for building high-fidelity digital twins (HiFi DTs) to generate realistic synthetic datasets. We outline practical steps for modeling static geometry, road infrastructure, and dynamic traffic using open-source resources such as satellite imagery, OpenStreetMap, and sensor specifications. The resulting environments support scalable and cost-effective data generation for robust Sim2Real learning. Using this workflow, we have released three synthetic LiDAR datasets, namely UT-LUMPI, UT-V2X-Real, and UT-TUMTraf-I, which closely replicate real locations and outperform real-data-trained baselines in perception tasks. This guide enables broader adoption of HiFi DTs in ITS research and deployment.

