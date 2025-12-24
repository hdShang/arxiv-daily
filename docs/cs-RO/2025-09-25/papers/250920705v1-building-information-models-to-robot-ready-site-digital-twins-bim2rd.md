---
layout: default
title: "Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework"
---

# Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.20705" class="toolbar-btn" target="_blank">📄 arXiv: 2509.20705v1</a>
  <a href="https://arxiv.org/pdf/2509.20705.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.20705v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.20705v1', 'Building Information Models to Robot-Ready Site Digital Twins (BIM2RDT): An Agentic AI Safety-First Framework')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Reza Akhavian, Mani Amani, Johannes Mootz, Robert Ashe, Behrad Beheshti

**分类**: cs.RO

**发布日期**: 2025-09-25

---

## 💡 一句话要点

**BIM2RDT框架：利用Agentic AI构建机器人可用的安全工地数字孪生**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `数字孪生` `建筑信息模型` `机器人` `点云配准` `大型语言模型` `施工安全` `Agentic AI`

## 📋 核心要点

1. 现有方法难以将静态BIM数据转化为动态、机器人可用的数字孪生，缺乏对施工现场安全性的实时监控和响应。
2. BIM2RDT框架通过Agentic AI整合BIM数据、物联网传感器数据和机器人视觉数据，构建动态数字孪生，并利用LLM推理优化点云配准。
3. 实验表明，SG-ICP算法在点云配准精度上显著优于传统ICP算法，RMSE降低高达88.3%，同时集成了HAV监测以保障施工安全。

## 📝 摘要（中文）

本文提出了一种名为BIM2RDT的agentic人工智能框架，旨在将静态的建筑信息模型（BIM）转化为动态的、机器人可用的数字孪生（DT），并在执行过程中优先考虑安全性。该框架通过整合BIM模型的几何和语义信息、物联网传感器网络的活动数据以及机器人收集的视觉空间数据，弥合了预先存在的BIM数据与实时现场条件之间的差距。该方法引入了语义-重力ICP（SG-ICP）算法，该算法利用大型语言模型（LLM）进行推理。与传统方法不同，SG-ICP利用LLM根据BIM语义推断特定于对象的、合理的姿态先验，通过避免收敛到局部最小值来提高对齐精度。这创建了一个反馈循环，其中机器人收集的数据更新DT，进而优化任务路径。该框架采用YOLOE目标检测和Shi-Tomasi角点检测来识别和跟踪建筑元素，同时使用BIM几何作为先验地图。该框架还集成了实时手-臂振动（HAV）监测，使用IFC标准将传感器检测到的安全事件映射到数字孪生，以便进行干预。实验表明，SG-ICP优于标准ICP，在存在遮挡特征的场景中，对齐的RMSE降低了64.3%--88.3%，确保了合理的姿态。HAV集成在超过暴露限值时触发警告，从而加强了对ISO 5349-1的合规性。

## 🔬 方法详解

**问题定义**：论文旨在解决建筑工地上静态BIM模型无法直接应用于机器人自主导航和作业的问题。现有方法，如传统的ICP算法，在点云配准时容易陷入局部最小值，导致配准精度不高，且缺乏对施工现场安全因素的实时监控和反馈机制。

**核心思路**：论文的核心思路是利用Agentic AI框架，将BIM模型、物联网传感器数据和机器人视觉数据融合，构建一个动态的、机器人可用的数字孪生。通过引入LLM进行语义推理，为点云配准提供更准确的姿态先验，从而提高配准精度和鲁棒性。同时，集成安全监测模块，实时检测和响应施工现场的安全事件。

**技术框架**：BIM2RDT框架包含以下主要模块：1) 数据采集模块：从BIM模型、物联网传感器和机器人视觉系统获取数据；2) 数据处理模块：使用YOLOE和Shi-Tomasi算法进行目标检测和特征提取，使用SG-ICP算法进行点云配准；3) 数字孪生构建模块：将处理后的数据集成到数字孪生中，并使用IFC标准进行数据管理；4) 安全监测模块：实时监测HAV等安全指标，并在超过阈值时触发警告；5) 任务规划模块：根据数字孪生信息，优化机器人的任务路径。

**关键创新**：最重要的技术创新点是SG-ICP算法，它利用LLM进行语义推理，为点云配准提供对象特定的、合理的姿态先验。与传统ICP算法相比，SG-ICP能够避免收敛到局部最小值，从而提高配准精度和鲁棒性。此外，将安全监测模块集成到数字孪生中，实现了对施工现场安全事件的实时监控和响应。

**关键设计**：SG-ICP算法的关键设计在于利用LLM根据BIM语义信息推断目标对象的可能姿态范围，并将这些姿态信息作为ICP算法的先验知识。具体而言，LLM接收BIM中对象的类型和上下文信息作为输入，输出该对象可能的姿态分布。然后，SG-ICP算法在ICP迭代过程中，根据LLM提供的姿态先验，对搜索空间进行约束，从而避免陷入局部最小值。

## 📊 实验亮点

实验结果表明，SG-ICP算法在点云配准精度上显著优于标准ICP算法，在存在遮挡特征的场景中，RMSE降低了64.3%--88.3%。此外，HAV集成能够实时监测手-臂振动，并在超过ISO 5349-1规定的暴露限值时触发警告，有效保障施工人员的安全。

## 🎯 应用场景

该研究成果可应用于建筑施工、基础设施建设等领域，实现施工现场的智能化管理和安全监控。通过构建机器人可用的数字孪生，可以提高施工效率、降低安全风险，并为未来的智能建造提供技术支撑。该框架还可扩展到其他领域，如智慧城市、工业自动化等。

## 📄 摘要（原文）

> The adoption of cyber-physical systems and jobsite intelligence that connects design models, real-time site sensing, and autonomous field operations can dramatically enhance digital management in the construction industry. This paper introduces BIM2RDT (Building Information Models to Robot-Ready Site Digital Twins), an agentic artificial intelligence (AI) framework designed to transform static Building Information Modeling (BIM) into dynamic, robot-ready digital twins (DTs) that prioritize safety during execution. The framework bridges the gap between pre-existing BIM data and real-time site conditions by integrating three key data streams: geometric and semantic information from BIM models, activity data from IoT sensor networks, and visual-spatial data collected by robots during site traversal. The methodology introduces Semantic-Gravity ICP (SG-ICP), a point cloud registration algorithm that leverages large language model (LLM) reasoning. Unlike traditional methods, SG-ICP utilizes an LLM to infer object-specific, plausible orientation priors based on BIM semantics, improving alignment accuracy by avoiding convergence on local minima. This creates a feedback loop where robot-collected data updates the DT, which in turn optimizes paths for missions. The framework employs YOLOE object detection and Shi-Tomasi corner detection to identify and track construction elements while using BIM geometry as a priori maps. The framework also integrates real-time Hand-Arm Vibration (HAV) monitoring, mapping sensor-detected safety events to the digital twin using IFC standards for intervention. Experiments demonstrate SG-ICP's superiority over standard ICP, achieving RMSE reductions of 64.3%--88.3% in alignment across scenarios with occluded features, ensuring plausible orientations. HAV integration triggers warnings upon exceeding exposure limits, enhancing compliance with ISO 5349-1.

