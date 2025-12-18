---
layout: default
title: Read the Room: Inferring Social Context Through Dyadic Interaction Recognition in Cyber-physical-social Infrastructure Systems
---

# Read the Room: Inferring Social Context Through Dyadic Interaction Recognition in Cyber-physical-social Infrastructure Systems

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.04854" class="toolbar-btn" target="_blank">📄 arXiv: 2510.04854v1</a>
  <a href="https://arxiv.org/pdf/2510.04854.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04854v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.04854v1', 'Read the Room: Inferring Social Context Through Dyadic Interaction Recognition in Cyber-physical-social Infrastructure Systems')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Cheyu Lin, John Martins, Katherine A. Flanigan, Ph. D

**分类**: cs.CV

**发布日期**: 2025-10-06

**备注**: ASCE International Conference on Computing in Civil Engineering 2024

---

## 💡 一句话要点

**提出基于深度传感器的群体交互识别方法，用于增强网络物理社会基础设施系统中的社会感知。**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `人际互动识别` `深度传感器` `隐私保护` `骨骼运动分析` `网络物理社会系统`

## 📋 核心要点

1. 现有网络物理系统侧重于经济效益，忽略了人际互动中的社会效益，缺乏对社会行为的有效测量。
2. 该研究提出利用深度传感器分析骨骼运动，在保护隐私的前提下识别二元人际互动，从而理解更深层次的社会行为。
3. 通过对12种二元交互数据集的实验，比较了五种基于骨骼的交互识别算法，为后续研究奠定基础。

## 📝 摘要（中文）

网络物理系统(CPS)通过集成传感、计算和控制来提升基础设施性能，但往往忽略了以人为本的社会效益。网络物理社会基础设施系统(CPSIS)旨在通过将CPS与社会目标对齐来解决这个问题。这包括定义社会效益，理解人与人以及人与基础设施的互动，开发保护隐私的测量方法，对这些互动进行建模以进行预测，将它们与社会效益联系起来，并驱动物理环境以促进积极的社会结果。本文深入研究了使用真实世界数据识别二元人际互动，这是衡量社会行为的支柱。这为增强对人类互动中固有的更深层含义和相互反应的理解奠定了基础。虽然RGB相机对于交互识别很有用，但会引起隐私问题。深度传感器通过分析骨骼运动提供了一种注重隐私的替代方案。本研究比较了12种二元交互数据集上的五种基于骨骼的交互识别算法。与单人数据集不同，这些交互被分类为诸如象征和情感展示之类的交流类型，提供了对人类交互的文化和情感方面的见解。

## 🔬 方法详解

**问题定义**：论文旨在解决网络物理社会基础设施系统中，如何有效且隐私保护地识别二元人际互动的问题。现有方法主要依赖RGB相机，存在严重的隐私泄露风险。同时，缺乏针对特定社会行为的数据集和算法，难以准确理解人类交互的文化和情感内涵。

**核心思路**：论文的核心思路是利用深度传感器获取人体骨骼数据，替代RGB相机，从而在保护用户隐私的前提下进行人际互动识别。通过分析骨骼运动模式，推断交互类型，进而理解更深层次的社会行为。

**技术框架**：该研究的技术框架主要包括以下几个阶段：1) 数据采集：使用深度传感器获取二元人际互动数据，构建包含12种交互类型的数据集。2) 特征提取：从骨骼数据中提取运动特征，例如关节位置、速度、加速度等。3) 模型训练：使用提取的特征训练五种不同的基于骨骼的交互识别算法。4) 性能评估：在构建的数据集上评估不同算法的性能，并进行比较分析。

**关键创新**：该研究的关键创新在于：1) 提出了一种基于深度传感器的隐私保护的人际互动识别方法。2) 构建了一个包含12种二元交互类型的数据集，这些交互类型涵盖了文化和情感方面的信息，更贴近实际应用场景。3) 对比分析了五种不同的基于骨骼的交互识别算法在二元交互数据集上的性能。

**关键设计**：论文中没有详细描述具体的参数设置、损失函数或网络结构等技术细节。但是，可以推断，算法的选择和参数调整会影响最终的识别性能。未来的研究可以进一步探索更有效的特征提取方法和更先进的深度学习模型，以提高识别精度。

## 📊 实验亮点

该研究构建了一个包含12种二元交互类型的数据集，并在此数据集上比较了五种基于骨骼的交互识别算法的性能。虽然论文中没有给出具体的性能数据和提升幅度，但该研究为后续基于深度传感器的二元人际互动识别研究奠定了基础，并提供了一个可供参考的基准。

## 🎯 应用场景

该研究成果可应用于智能建筑、智慧城市、公共安全等领域。例如，在智能建筑中，系统可以识别人们的交互行为，自动调节室内环境，提升用户体验。在公共安全领域，系统可以识别潜在的冲突或异常行为，及时发出预警。未来，该技术有望促进人与环境的和谐共处，提升社会福祉。

## 📄 摘要（原文）

> Cyber-physical systems (CPS) integrate sensing, computing, and control to improve infrastructure performance, focusing on economic goals like performance and safety. However, they often neglect potential human-centered (or ''social'') benefits. Cyber-physical-social infrastructure systems (CPSIS) aim to address this by aligning CPS with social objectives. This involves defining social benefits, understanding human interactions with each other and infrastructure, developing privacy-preserving measurement methods, modeling these interactions for prediction, linking them to social benefits, and actuating the physical environment to foster positive social outcomes. This paper delves into recognizing dyadic human interactions using real-world data, which is the backbone to measuring social behavior. This lays a foundation to address the need to enhance understanding of the deeper meanings and mutual responses inherent in human interactions. While RGB cameras are informative for interaction recognition, privacy concerns arise. Depth sensors offer a privacy-conscious alternative by analyzing skeletal movements. This study compares five skeleton-based interaction recognition algorithms on a dataset of 12 dyadic interactions. Unlike single-person datasets, these interactions, categorized into communication types like emblems and affect displays, offer insights into the cultural and emotional aspects of human interactions.

