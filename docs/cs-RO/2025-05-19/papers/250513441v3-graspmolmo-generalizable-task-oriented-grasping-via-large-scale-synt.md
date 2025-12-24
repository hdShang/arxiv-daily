---
layout: default
title: GraspMolmo: Generalizable Task-Oriented Grasping via Large-Scale Synthetic Data Generation
---

# GraspMolmo: Generalizable Task-Oriented Grasping via Large-Scale Synthetic Data Generation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13441" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13441v3</a>
  <a href="https://arxiv.org/pdf/2505.13441.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13441v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13441v3', 'GraspMolmo: Generalizable Task-Oriented Grasping via Large-Scale Synthetic Data Generation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Abhay Deshpande, Yuquan Deng, Arijit Ray, Jordi Salvador, Winson Han, Jiafei Duan, Kuo-Hao Zeng, Yuke Zhu, Ranjay Krishna, Rose Hendrix

**分类**: cs.RO

**发布日期**: 2025-05-19 (更新: 2025-09-12)

**🔗 代码/项目**: [PROJECT_PAGE](https://abhaybd.github.io/GraspMolmo/)

---

## 💡 一句话要点

**提出GraspMolmo以解决任务导向抓取的泛化问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知与语义 (Perception & Semantics)**

**关键词**: `任务导向抓取` `自然语言处理` `合成数据集` `视觉语言模型` `机器人操作`

## 📋 核心要点

1. 现有的任务导向抓取方法受限于小型数据集和简单的语言描述，导致泛化能力不足。
2. GraspMolmo通过大规模合成数据集PRISM进行训练，能够根据自然语言指令生成稳定的抓取策略。
3. 在真实世界评估中，GraspMolmo在复杂任务上实现了70%的成功率，显著优于其他方法。

## 📝 摘要（中文）

我们提出了GraspMolmo，一个可泛化的开放词汇任务导向抓取模型。GraspMolmo能够根据自然语言指令和单个RGB-D帧预测语义上合适且稳定的抓取。例如，给定指令“给我倒些茶”，GraspMolmo会选择抓取茶壶的把手而非壶身。与以往受限于小型数据集、简单语言和整洁场景的TOG方法不同，GraspMolmo从PRISM这一新型大规模合成数据集中学习，该数据集包含379k样本，涵盖了杂乱环境和多样化的任务描述。我们在此数据集上微调了Molmo视觉语言模型，使GraspMolmo能够泛化到新的开放词汇指令和物体。在复杂任务的真实世界评估中，GraspMolmo实现了70%的预测成功率，而次优方法仅为35%。GraspMolmo还成功展示了零样本预测语义正确的双手抓取能力。我们发布了合成数据集、代码、模型和基准，以加速任务语义机器人操作的研究，相关视频可在https://abhaybd.github.io/GraspMolmo/获取。

## 🔬 方法详解

**问题定义**：本论文旨在解决任务导向抓取（TOG）模型在复杂环境中对自然语言指令的泛化能力不足的问题。现有方法通常依赖于小型数据集，导致其在多样化场景中的表现不佳。

**核心思路**：GraspMolmo的核心思想是通过大规模合成数据集PRISM进行训练，使模型能够理解并执行开放词汇的自然语言指令，从而提高抓取的准确性和稳定性。

**技术框架**：GraspMolmo的整体架构包括数据预处理、模型训练和评估三个主要阶段。首先，利用PRISM数据集进行模型的训练，接着通过微调Molmo视觉语言模型来增强其对指令的理解能力，最后在真实场景中进行评估。

**关键创新**：GraspMolmo的主要创新在于其使用了大规模合成数据集PRISM，包含379k样本，能够有效提升模型在复杂和杂乱环境中的抓取能力。这一方法与以往依赖小型数据集的TOG方法有本质区别。

**关键设计**：在模型设计上，GraspMolmo采用了先进的视觉语言模型，并通过特定的损失函数来优化抓取策略的稳定性和准确性。关键参数设置经过多次实验调整，以确保模型在多样化任务中的表现。

## 📊 实验亮点

GraspMolmo在复杂任务的真实世界评估中实现了70%的预测成功率，显著高于次优方法的35%。此外，该模型还展示了零样本预测语义正确的双手抓取能力，显示出其强大的泛化能力和实用性。

## 🎯 应用场景

GraspMolmo的研究成果可广泛应用于服务机器人、家庭自动化、工业机器人等领域，能够提升机器人在复杂环境中的抓取能力和任务执行效率。未来，该模型的泛化能力可能推动更多智能机器人在日常生活中的应用，增强人机交互的自然性和智能性。

## 📄 摘要（原文）

> We present GrasMolmo, a generalizable open-vocabulary task-oriented grasping (TOG) model. GraspMolmo predicts semantically appropriate, stable grasps conditioned on a natural language instruction and a single RGB-D frame. For instance, given "pour me some tea", GraspMolmo selects a grasp on a teapot handle rather than its body. Unlike prior TOG methods, which are limited by small datasets, simplistic language, and uncluttered scenes, GraspMolmo learns from PRISM, a novel large-scale synthetic dataset of 379k samples featuring cluttered environments and diverse, realistic task descriptions. We fine-tune the Molmo visual-language model on this data, enabling GraspMolmo to generalize to novel open-vocabulary instructions and objects. In challenging real-world evaluations, GraspMolmo achieves state-of-the-art results, with a 70% prediction success on complex tasks, compared to the 35% achieved by the next best alternative. GraspMolmo also successfully demonstrates the ability to predict semantically correct bimanual grasps zero-shot. We release our synthetic dataset, code, model, and benchmarks to accelerate research in task-semantic robotic manipulation, which, along with videos, are available at https://abhaybd.github.io/GraspMolmo/.

