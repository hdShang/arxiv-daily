---
layout: default
title: ScaleADFG: Affordance-based Dexterous Functional Grasping via Scalable Dataset
---

# ScaleADFG: Affordance-based Dexterous Functional Grasping via Scalable Dataset

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.09602" class="toolbar-btn" target="_blank">📄 arXiv: 2511.09602v1</a>
  <a href="https://arxiv.org/pdf/2511.09602.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.09602v1" onclick="toggleFavorite(this, '2511.09602v1', 'ScaleADFG: Affordance-based Dexterous Functional Grasping via Scalable Dataset')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sizhe Wang, Yifan Yang, Yongkang Luo, Daheng Li, Wei Wei, Yan Zhang, Peiying Hu, Yunjin Fu, Haonan Duan, Jia Sun, Peng Wang

**分类**: cs.RO

**发布日期**: 2025-11-12

**备注**: Accepted by IEEE Robotics and Automation Letters

**🔗 代码/项目**: [PROJECT_PAGE](https://sizhe-wang.github.io/ScaleADFG_webpage)

---

## 💡 一句话要点

**提出ScaleADFG框架，解决机器人灵巧手对多尺度工具的功能性抓取问题。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)**

**关键词**: `灵巧抓取` `可供性` `机器人操作` `数据集构建` `多尺度学习`

## 📋 核心要点

1. 现有方法难以构建大规模数据集，且对不同尺度物体的泛化性不足，这是由于机器人手与人手尺寸差异以及物体尺度多样性造成的。
2. ScaleADFG框架通过全自动数据集构建流程和轻量级抓取生成网络，利用可供性算法合成抓取配置，实现对多尺度物体的有效抓取。
3. 实验结果表明，ScaleADFG框架对不同尺度的物体具有很强的适应性，并具备良好的泛化性和零样本迁移能力。

## 📝 摘要（中文）

本文提出ScaleADFG框架，旨在解决机器人灵巧手有效操作工具的功能性抓取问题。现有方法在构建大规模数据集和确保对日常物体尺度的泛化性方面面临挑战，主要源于机器人手和人手之间的尺寸不匹配以及现实世界物体尺度的多样性。ScaleADFG框架包含一个全自动数据集构建流程和一个轻量级抓取生成网络。该数据集引入了一种基于可供性的算法，用于合成多样化的工具使用抓取配置，无需专家演示，允许灵活的物体-手尺寸比例，并使大型机器人手能够有效地抓取日常物体。此外，利用预训练模型生成大量的3D资产，并促进物体可供性的高效检索。数据集包含五个物体类别，每个类别包含超过1000个独特的形状，具有15个尺度变体。经过过滤后，数据集包含每个灵巧机器人手的超过60000个抓取。在此数据集的基础上，训练了一个轻量级的单阶段抓取生成网络，具有非常简单的损失函数设计，无需后处理优化。实验表明，ScaleADFG框架对不同尺度的物体具有很强的适应性，增强了功能性抓取的稳定性、多样性和泛化性。此外，该网络还表现出对真实世界物体的有效零样本迁移能力。

## 🔬 方法详解

**问题定义**：论文旨在解决机器人灵巧手在不同物体尺度下的功能性抓取问题。现有方法依赖于人工标注或专家演示，难以构建大规模数据集，且难以泛化到不同尺度的物体上。此外，机器人手通常比人手大，直接使用人手抓取数据训练的模型难以直接应用于机器人。

**核心思路**：论文的核心思路是利用可供性（affordance）的概念，自动生成大量不同尺度物体的抓取配置，构建大规模数据集。通过在合成数据上训练轻量级抓取生成网络，提高模型对不同尺度物体的泛化能力，并实现零样本迁移到真实世界。

**技术框架**：ScaleADFG框架主要包含两个部分：全自动数据集构建流程和轻量级抓取生成网络。数据集构建流程包括：1) 利用预训练模型生成3D物体资产；2) 基于可供性算法合成抓取配置，允许灵活的物体-手尺寸比例；3) 对生成的抓取进行过滤，得到高质量的抓取数据集。抓取生成网络是一个单阶段网络，直接预测抓取姿态。

**关键创新**：论文的关键创新在于提出了一种基于可供性的全自动数据集构建方法，能够高效地生成大规模、多尺度的抓取数据集。这种方法无需人工标注或专家演示，降低了数据获取的成本，并提高了模型的泛化能力。此外，轻量级抓取生成网络的设计也降低了计算复杂度。

**关键设计**：数据集包含五个物体类别，每个类别包含超过1000个独特的形状，具有15个尺度变体。损失函数设计简单，无需后处理优化。网络结构采用单阶段设计，直接预测抓取姿态。可供性算法用于合成抓取配置，允许灵活的物体-手尺寸比例。

## 📊 实验亮点

实验结果表明，ScaleADFG框架在模拟和真实机器人上都表现出良好的性能。在模拟环境中，该框架能够成功抓取不同尺度的物体，并具有较高的抓取成功率。在真实机器人实验中，该网络能够实现有效的零样本迁移，成功抓取真实世界中的物体。与现有方法相比，ScaleADFG框架在抓取稳定性、多样性和泛化性方面都有显著提升。

## 🎯 应用场景

该研究成果可应用于工业自动化、家庭服务机器人等领域，使机器人能够灵活抓取和操作不同尺寸的工具和物体，完成各种复杂任务。例如，在智能制造中，机器人可以根据零件的尺寸和形状自动调整抓取姿态，提高生产效率。在家庭服务中，机器人可以抓取不同大小的物品，如餐具、玩具等，提供更智能化的服务。

## 📄 摘要（原文）

> Dexterous functional tool-use grasping is essential for effective robotic manipulation of tools. However, existing approaches face significant challenges in efficiently constructing large-scale datasets and ensuring generalizability to everyday object scales. These issues primarily arise from size mismatches between robotic and human hands, and the diversity in real-world object scales. To address these limitations, we propose the ScaleADFG framework, which consists of a fully automated dataset construction pipeline and a lightweight grasp generation network. Our dataset introduce an affordance-based algorithm to synthesize diverse tool-use grasp configurations without expert demonstrations, allowing flexible object-hand size ratios and enabling large robotic hands (compared to human hands) to grasp everyday objects effectively. Additionally, we leverage pre-trained models to generate extensive 3D assets and facilitate efficient retrieval of object affordances. Our dataset comprising five object categories, each containing over 1,000 unique shapes with 15 scale variations. After filtering, the dataset includes over 60,000 grasps for each 2 dexterous robotic hands. On top of this dataset, we train a lightweight, single-stage grasp generation network with a notably simple loss design, eliminating the need for post-refinement. This demonstrates the critical importance of large-scale datasets and multi-scale object variant for effective training. Extensive experiments in simulation and on real robot confirm that the ScaleADFG framework exhibits strong adaptability to objects of varying scales, enhancing functional grasp stability, diversity, and generalizability. Moreover, our network exhibits effective zero-shot transfer to real-world objects. Project page is available at https://sizhe-wang.github.io/ScaleADFG_webpage

