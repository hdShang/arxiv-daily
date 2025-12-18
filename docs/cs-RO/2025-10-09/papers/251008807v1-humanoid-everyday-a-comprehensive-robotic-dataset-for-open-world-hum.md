---
layout: default
title: Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation
---

# Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.08807" class="toolbar-btn" target="_blank">📄 arXiv: 2510.08807v1</a>
  <a href="https://arxiv.org/pdf/2510.08807.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.08807v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.08807v1', 'Humanoid Everyday: A Comprehensive Robotic Dataset for Open-World Humanoid Manipulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhenyu Zhao, Hongyi Jing, Xiawei Liu, Jiageng Mao, Abha Jha, Hanwen Yang, Rong Xue, Sergey Zakharor, Vitor Guizilini, Yue Wang

**分类**: cs.RO, cs.LG

**发布日期**: 2025-10-09

---

## 💡 一句话要点

**Humanoid Everyday：一个面向开放世界人型机器人操作的综合数据集**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `人形机器人` `操作数据集` `人机交互` `强化学习` `多模态感知` `遥操作` `云平台`

## 📋 核心要点

1. 现有机器人学习数据集主要关注固定机械臂，缺乏对复杂人型机器人全身操作和人机交互的支持。
2. Humanoid Everyday数据集通过人工监督遥操作，收集了包含多模态数据和自然语言标注的大规模人型机器人操作数据。
3. 论文分析了现有策略学习方法在数据集上的表现，并提供了一个基于云的评估平台，以促进标准化评估。

## 📝 摘要（中文）

人形机器人在运动和灵巧操作方面取得了显著进展。然而，当前机器人学习数据集和基准测试主要集中在固定机器人手臂上，而现有的人形机器人数据集要么局限于固定环境，要么在任务多样性方面受到限制，通常缺乏人机交互和下肢运动。此外，缺乏用于评估人形机器人数据学习策略的标准化评估平台。本文提出了Humanoid Everyday，一个大规模、多样化的人形机器人操作数据集，其特点是广泛的任务种类，包括灵巧的物体操作、人机交互、运动集成动作等。利用高效的人工监督遥操作流程，Humanoid Everyday聚合了高质量的多模态感知数据，包括RGB、深度、激光雷达和触觉输入，以及自然语言注释，包含10.3k条轨迹和超过300万帧的数据，涵盖7大类260个任务。此外，我们对数据集上具有代表性的策略学习方法进行了分析，深入了解了它们在不同任务类别中的优势和局限性。为了进行标准化评估，我们引入了一个基于云的评估平台，允许研究人员在我们的受控环境中无缝部署他们的策略并获得性能反馈。通过发布Humanoid Everyday以及我们的策略学习分析和一个标准化的基于云的评估平台，我们旨在推进通用人形机器人操作的研究，并为现实场景中更强大和具身化的机器人代理奠定基础。我们的数据集、数据收集代码和云评估网站已在我们的项目网站上公开发布。

## 🔬 方法详解

**问题定义**：现有的人形机器人数据集在任务多样性、环境复杂性以及人机交互方面存在不足，难以支持通用人形机器人操作的学习和评估。此外，缺乏统一的评估平台来比较不同学习策略的性能。

**核心思路**：通过人工监督遥操作的方式，收集大规模、多样化的真实世界人形机器人操作数据，包括多模态传感器信息和自然语言描述。同时，构建一个基于云的评估平台，为研究人员提供标准化的策略评估环境。

**技术框架**：Humanoid Everyday数据集的构建流程主要包括数据收集、数据标注和数据管理三个阶段。数据收集阶段采用人工监督遥操作，由人类操作员控制人形机器人完成各种任务。数据标注阶段对收集到的数据进行多模态标注，包括RGB图像、深度图像、激光雷达点云、触觉信息以及自然语言描述。数据管理阶段对数据进行清洗、整理和存储，并提供API方便用户访问。同时，论文还构建了一个基于云的评估平台，用户可以将自己的策略部署到平台上进行评估。

**关键创新**：该数据集的关键创新在于其规模和多样性，涵盖了260个任务，涉及灵巧操作、人机交互和运动集成等多个方面。此外，数据集还提供了多模态传感器信息和自然语言描述，为研究人员提供了更丰富的信息。基于云的评估平台也为策略评估提供了标准化的环境。

**关键设计**：数据收集采用高效的人工监督遥操作流程，保证了数据的质量和多样性。数据标注采用了多模态标注方案，为研究人员提供了更丰富的信息。基于云的评估平台采用了模块化设计，方便用户部署和评估自己的策略。

## 📊 实验亮点

论文构建了一个包含10.3k条轨迹和超过300万帧的大规模人形机器人操作数据集，涵盖260个任务。通过对现有策略学习方法在数据集上的分析，揭示了它们在不同任务类别中的优势和局限性。基于云的评估平台为策略评估提供了标准化的环境。

## 🎯 应用场景

该研究成果可广泛应用于人形机器人操作、人机交互、强化学习等领域。Humanoid Everyday数据集能够促进通用人形机器人操作算法的开发，提高机器人在复杂环境中的适应性和自主性。基于云的评估平台能够为研究人员提供标准化的评估环境，加速相关研究的进展。

## 📄 摘要（原文）

> From loco-motion to dextrous manipulation, humanoid robots have made remarkable strides in demonstrating complex full-body capabilities. However, the majority of current robot learning datasets and benchmarks mainly focus on stationary robot arms, and the few existing humanoid datasets are either confined to fixed environments or limited in task diversity, often lacking human-humanoid interaction and lower-body locomotion. Moreover, there are a few standardized evaluation platforms for benchmarking learning-based policies on humanoid data. In this work, we present Humanoid Everyday, a large-scale and diverse humanoid manipulation dataset characterized by extensive task variety involving dextrous object manipulation, human-humanoid interaction, locomotion-integrated actions, and more. Leveraging a highly efficient human-supervised teleoperation pipeline, Humanoid Everyday aggregates high-quality multimodal sensory data, including RGB, depth, LiDAR, and tactile inputs, together with natural language annotations, comprising 10.3k trajectories and over 3 million frames of data across 260 tasks across 7 broad categories. In addition, we conduct an analysis of representative policy learning methods on our dataset, providing insights into their strengths and limitations across different task categories. For standardized evaluation, we introduce a cloud-based evaluation platform that allows researchers to seamlessly deploy their policies in our controlled setting and receive performance feedback. By releasing Humanoid Everyday along with our policy learning analysis and a standardized cloud-based evaluation platform, we intend to advance research in general-purpose humanoid manipulation and lay the groundwork for more capable and embodied robotic agents in real-world scenarios. Our dataset, data collection code, and cloud evaluation website are made publicly available on our project website.

